#!/usr/bin/env python3
"""Find out whether a host is usable, and say WHICH layer refuses us.

Built after KB-120. The owner spent two minutes allowlisting Upwork, the network
opened exactly as promised, and Upwork then served a bot challenge. "Blocked" is
not one thing, and telling the owner "it's blocked" when the real answer is "they
refuse robots and their terms bar us anyway" wastes their time twice.

Verdicts:
  OPEN          usable now
  BOT_WALL      network is fine, the site refuses automated requests
  AUTH          needs credentials we do not have
  NOT_FOUND     reachable, wrong path
  NET_BLOCKED   the environment's allowlist does not include it
  ERROR         something else, reported verbatim

    python3 scripts/probe_reachability.py                # the standing list
    python3 scripts/probe_reachability.py URL [URL ...]  # ad hoc
"""

import json
import os
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(REPO, "state", "reachability.json")
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")

# What the organization actually depends on, and what it wishes it had.
STANDING = [
    ("gumroad api",      "https://api.gumroad.com/v2/products", "depended on"),
    ("apify api",        "https://api.apify.com/v2/users/me",   "depended on"),
    ("pypi",             "https://pypi.org/simple/",            "depended on"),
    ("github api",       "https://api.github.com/rate_limit",   "depended on"),
    ("upwork search",    "https://www.upwork.com/nx/search/jobs/?q=n8n", "demand source"),
    ("remoteok api",     "https://remoteok.com/api",            "demand source"),
    ("n8n community",    "https://community.n8n.io/latest.json", "demand source"),
    ("hacker news jobs", "https://hacker-news.firebaseio.com/v0/jobstories.json", "demand source"),
]

BOT_MARKERS = ["challenge", "are you a robot", "captcha", "cf-browser-verification",
               "attention required", "access denied", "just a moment",
               "enable javascript and cookies"]


def probe(url):
    try:
        r = subprocess.run(
            ["curl", "-sS", "--max-time", "20", "-A", UA, "-w", "\n__%{http_code}__", url],
            capture_output=True, text=True, timeout=30)
    except subprocess.TimeoutExpired:
        return {"verdict": "NET_BLOCKED", "detail": "timed out with no response"}

    body = r.stdout
    code = ""
    if "__" in body:
        code = body.rsplit("__", 2)[-2] if body.rstrip().endswith("__") else ""
    try:
        code = int(code)
    except ValueError:
        code = 0
    text = body.lower()

    if code == 0:
        err = (r.stderr or "").strip().splitlines()
        return {"verdict": "NET_BLOCKED",
                "detail": err[-1] if err else "no response from the host"}
    if code in (401, 403):
        if any(m in text for m in BOT_MARKERS):
            return {"verdict": "BOT_WALL", "http": code,
                    "detail": "the site answered, and refused an automated request"}
        return {"verdict": "AUTH", "http": code,
                "detail": "reachable; needs credentials or is forbidden to us"}
    if code == 404:
        return {"verdict": "NOT_FOUND", "http": code, "detail": "reachable, wrong path"}
    if 200 <= code < 400:
        return {"verdict": "OPEN", "http": code,
                "detail": "usable (%d bytes)" % len(body)}
    return {"verdict": "ERROR", "http": code, "detail": "unexpected status"}


def main():
    targets = ([(u, u, "ad hoc") for u in sys.argv[1:]] if len(sys.argv) > 1 else STANDING)
    rows, worst = [], []
    for name, url, why in targets:
        r = probe(url)
        r.update({"name": name, "url": url, "why": why})
        rows.append(r)
        print("%-9s %-18s %s" % (r["verdict"], name, r["detail"]))
        if r["verdict"] in ("NET_BLOCKED", "BOT_WALL") and why == "depended on":
            worst.append(name)

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump({"checked": rows}, fh, indent=2)
        fh.write("\n")

    usable = [r["name"] for r in rows if r["verdict"] == "OPEN" and r["why"] == "demand source"]
    print("")
    print("demand sources usable: %s" % (", ".join(usable) if usable else "NONE"))
    if worst:
        print("REGRESSION on something we depend on: %s" % ", ".join(worst))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
