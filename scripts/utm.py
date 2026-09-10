#!/usr/bin/env python3
"""Create/list Gumroad UTM links.

The Gumroad CLI has no utm_links command, so this talks to /v2/utm_links directly.
The token is read from the environment and never printed: it goes into a header and
nothing in this script echoes it, including on the error paths.

Usage:
  python3 scripts/utm.py list
  python3 scripts/utm.py ensure <title> <product_id> <source> <medium> <campaign>
"""
import json
import os
import sys
import urllib.parse
import urllib.request

API = "https://api.gumroad.com/v2/utm_links"


def _token():
    t = os.environ.get("GUMROAD_ACCESS_TOKEN")
    if not t:
        sys.exit("GUMROAD_ACCESS_TOKEN is not set")
    return t


def _call(method, url, data=None):
    body = urllib.parse.urlencode(data).encode() if data else None
    req = urllib.request.Request(url, data=body, method=method)
    req.add_header("Authorization", "Bearer " + _token())
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        # Deliberately does not echo the request headers.
        return {"success": False, "status": e.code, "body": e.read().decode()[:400]}


def links():
    return _call("GET", API).get("utm_links", []) or []


def ensure(title, pid, source, medium, campaign):
    """Idempotent: Gumroad keys a link by target + the three utm_ fields, so match on those."""
    for l in links():
        if (l.get("target_resource_id") == pid and l.get("utm_source") == source
                and l.get("utm_medium") == medium and l.get("utm_campaign") == campaign):
            print(f"exists  {l['short_url']}  {title}")
            return l
    out = _call("POST", API, {
        "title": title, "target_resource_type": "product_page", "target_resource_id": pid,
        "utm_source": source, "utm_medium": medium, "utm_campaign": campaign,
    })
    l = out.get("utm_link")
    if not l:
        print(f"FAILED  {title}: {json.dumps(out)[:300]}", file=sys.stderr)
        return None
    print(f"created {l['short_url']}  {title}")
    return l


if __name__ == "__main__":
    if sys.argv[1] == "list":
        for l in sorted(links(), key=lambda x: x["title"]):
            print(f"{l['short_url']:34} {l['total_clicks']:>4} clicks "
                  f"({l['unique_clicks']} unique)  {l['title']}")
    elif sys.argv[1] == "ensure":
        ensure(*sys.argv[2:7])
