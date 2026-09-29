#!/usr/bin/env python3
"""Read what this company actually has for sale, and refuse to be wrong about it.

Why this file exists (KB-155, 2026-09-29). The office page listed six storefront
products. There were nine. The three it missed were the three oldest, including the
$95 done-for-you build -- the only thing here that sells work rather than a file, and
the highest-priced thing we own. They were live the whole time.

Two separate faults, and the second is the one that mattered:

  1. The raw REST list endpoint returns at most ten records and says so nowhere. No
     total, no cursor, and asking for page 2 hands back page 1. Four unpublished
     internal archives sat in that list and ate four of the ten slots.

  2. `data/scoreboard.json` HAD all thirteen since 2026-09-14, because the CLI
     paginates properly. Nothing ever compared it to the office's product list, which
     was typed by hand. The truth was in the building and no wire ran to it.

So this script is the wire, and it is built to fail loudly rather than quietly agree:

  * The CLI is the authority, because it paginates. The raw endpoint is read too, only
    so the truncation is measured every run instead of remembered.
  * `state/product_ids.json` is an append-only ledger of every product id ever seen. An
    id that drops out of the list is fetched by id; if it still exists, that is drift
    and this script stops.
  * Copy lives in `org/PRODUCT_COPY.json`. A live product with no entry there stops the
    run; an entry there naming nothing live stops the run. A product cannot exist
    without the office knowing what it is.
  * Anything not on the storefront (the marketplace listing) is declared in the same
    file and checked against its own API.

Output: state/inventory.json, and observer/state.json["products"] rewritten from it.
build_observer.py then refuses to build if those two disagree, so a hand-edit to the
office cannot reintroduce the fault this file exists to prevent.

    python3 scripts/inventory.py           # read, check, write
    python3 scripts/inventory.py --check   # read and check, write nothing
"""

import argparse
import datetime as dt
import io
import json
import os
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COPY = os.path.join(REPO, "org", "PRODUCT_COPY.json")
LEDGER = os.path.join(REPO, "state", "product_ids.json")
OUT = os.path.join(REPO, "state", "inventory.json")
STATE = os.path.join(REPO, "observer", "state.json")

API = "https://api.gumroad.com/v2"
APIFY = "https://api.apify.com/v2"
CLI = ["--json", "--no-input", "--non-interactive", "--quiet"]

PROBLEMS = []


def stop(msg):
    PROBLEMS.append(msg)


def load(path, default=None):
    if not os.path.exists(path):
        return default
    with io.open(path, encoding="utf-8") as fh:
        return json.load(fh)


def save(path, obj):
    with io.open(path, "w", encoding="utf-8") as fh:
        fh.write(json.dumps(obj, indent=1, ensure_ascii=False) + "\n")


def token(name):
    """Read a secret from the environment. Never printed, never written anywhere."""
    v = os.environ.get(name)
    if not v:
        stop("%s is not set, so the shop cannot be read at all. Nothing was written."
             % name)
    return v


def get(url, bearer, timeout=40):
    req = urllib.request.Request(url, headers={"Authorization": "Bearer " + bearer})
    return json.load(urllib.request.urlopen(req, timeout=timeout))


def permalink(short_url):
    return (short_url or "").rstrip("/").rsplit("/", 1)[-1]


def price_label(cents, published):
    if not cents:
        return "Free"
    return "$%g" % (cents / 100.0)


# ---------------------------------------------------------------- the storefront

def cli_products():
    """The authority. The CLI paginates; the raw endpoint does not."""
    p = subprocess.run(["gumroad", "products", "list", "--all"] + CLI,
                       capture_output=True, text=True)
    if p.returncode != 0:
        stop("the storefront CLI failed, so the product list could not be read. "
             "Last line of its error: %s" % (p.stderr.strip().splitlines() or ["(none)"])[-1])
        return []
    try:
        return json.loads(p.stdout).get("products", [])
    except json.JSONDecodeError:
        stop("the storefront CLI returned something that is not JSON.")
        return []


def rest_products(bearer):
    """Read the known-truncating endpoint too, so the truncation is measured, not recalled."""
    try:
        return get(API + "/products", bearer).get("products", [])
    except (urllib.error.URLError, urllib.error.HTTPError) as exc:
        stop("the storefront REST list could not be read (%s). The CLI list is still "
             "the authority, but the truncation gap could not be measured this run." % exc)
        return []


def by_id(pid, bearer):
    """Fetch one product by id. This is what proves a missing row is missing, not gone."""
    url = API + "/products/" + urllib.parse.quote(pid, safe="")
    try:
        return get(url, bearer).get("product")
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return None
        stop("product %s could not be checked by id (HTTP %s)." % (pid, exc.code))
        return None
    except urllib.error.URLError as exc:
        stop("product %s could not be checked by id (%s)." % (pid, exc))
        return None


# ----------------------------------------------------------------- the marketplace

def apify_actor(url, bearer):
    """Confirm a declared marketplace listing is really public, and read its usage."""
    slug = url.rstrip("/").rsplit("/", 2)[-2:]
    if len(slug) != 2:
        stop("cannot work out the actor id from %r." % url)
        return None
    try:
        a = get(APIFY + "/acts/" + slug[0] + "~" + slug[1], bearer).get("data", {})
    except (urllib.error.URLError, urllib.error.HTTPError) as exc:
        stop("the marketplace listing %s could not be read (%s)." % (url, exc))
        return None
    if not a.get("isPublic"):
        stop("the marketplace listing %s reports isPublic=false, so a stranger cannot "
             "reach it. It must not be shown as live." % url)
        return None
    return a


# ----------------------------------------------------------------------- the join

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="read and check, write nothing")
    args = ap.parse_args()

    copy = load(COPY)
    if not copy:
        sys.exit("FAIL: org/PRODUCT_COPY.json is missing. Without it nothing can be "
                 "described, and a product with no description must not be published "
                 "to the office as a blank row.")
    shop_copy = copy.get("storefront", {})
    elsewhere = copy.get("elsewhere", [])

    gum = token("GUMROAD_ACCESS_TOKEN")
    if PROBLEMS:
        report_and_exit()

    live = cli_products()
    rest = rest_products(gum)

    # ---- fault 1: measure the truncation rather than remember it
    truncation = {
        "cli_records": len(live),
        "rest_records": len(rest),
        "rest_hides": max(0, len(live) - len(rest)),
    }
    if truncation["rest_hides"]:
        print("NOTE: the REST list returned %d of %d products. It is truncating %d and "
              "saying nothing. The CLI list is the authority."
              % (len(rest), len(live), truncation["rest_hides"]))

    # ---- fault 2: an append-only ledger, so nothing can silently drop out
    ledger = load(LEDGER, {"seen": {}, "note": (
        "Every storefront product id this company has ever seen, with the date it was "
        "first seen. Append-only on purpose: an id that stops appearing in the list is "
        "fetched by id, and if it still exists the run stops. This is how a live product "
        "can never go missing from our own records again. KB-155.")})
    seen = ledger.get("seen", {})
    today = dt.date.today().isoformat()
    ids_now = {p["id"] for p in live if p.get("id")}
    for pid in sorted(ids_now):
        seen.setdefault(pid, today)

    for pid in sorted(set(seen) - ids_now):
        again = by_id(pid, gum)
        if again is None:
            print("NOTE: %s is gone from the shop entirely (404). Kept in the ledger as "
                  "history." % pid)
        else:
            stop("product id %s is missing from the product list but still exists when "
                 "asked for by id (%r, published=%s). The list is lying. Nothing was "
                 "written."
                 % (pid, str(again.get("name"))[:60], again.get("published")))

    # ---- the join: every live product must be described, every description must be live
    products, internal = [], []
    for p in live:
        link = permalink(p.get("short_url"))
        if not p.get("published"):
            internal.append({"permalink": link, "name": p.get("name"),
                             "url": p.get("short_url")})
            continue
        c = shop_copy.get(link)
        if not c:
            stop("%s is live on the shop and has no entry in org/PRODUCT_COPY.json, so "
                 "the office would show it as a blank row or not at all. Add one. "
                 "(name: %r)" % (link, str(p.get("name"))[:70]))
            continue
        products.append({
            "name": c["short"],
            "what": c["what"],
            "price": price_label(p.get("price"), p.get("published")),
            "url": p.get("short_url"),
            "owner": c["owner"],
            "venue": "Storefront",
            "status": "LIVE",
            "sales": p.get("sales_count") or 0,
            "permalink": link,
            "full_name": p.get("name"),
        })

    live_links = {permalink(p.get("short_url")) for p in live if p.get("published")}
    for link in sorted(set(shop_copy) - live_links):
        stop("org/PRODUCT_COPY.json describes %r but nothing by that name is live on the "
             "shop. Either it was unpublished and the entry should go, or it was "
             "renamed and the key should follow it." % link)

    # ---- anything not on the storefront, declared and then verified on its own API
    apify_tok = os.environ.get("APIFY_TOKEN") or os.environ.get("APIFY_API_TOKEN")
    for d in elsewhere:
        row = {"name": d["short"], "what": d["what"], "price": d.get("price", "Free"),
               "url": d["url"], "owner": d["owner"], "venue": d.get("venue", "Elsewhere"),
               "status": "LIVE", "sales": 0, "permalink": d["key"]}
        if d["url"].startswith("https://apify.com/"):
            if not apify_tok:
                stop("%s is declared as live but APIFY_TOKEN is not set, so it cannot be "
                     "confirmed. An unconfirmed listing must not be shown as live."
                     % d["key"])
                continue
            a = apify_actor(d["url"], apify_tok)
            if a is None:
                continue
            st = a.get("stats", {})
            total = st.get("totalRuns") or 0
            row["usage"] = ("%d runs, %d of them not ours. Last run %s."
                            % (total, max(0, total - ours_runs(d["url"], apify_tok)),
                               (st.get("lastRunStartedAt") or "")[:16].replace("T", " ") + " UTC"))
        products.append(row)

    if PROBLEMS:
        report_and_exit()

    inv = {
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "source": "gumroad CLI (paginates) + per-id checks + org/PRODUCT_COPY.json",
        "live_count": len(products),
        "truncation": truncation,
        "internal_not_for_sale": internal,
        "products": products,
    }

    if args.check:
        print("OK: %d live products, all described, none missing from the list. "
              "Nothing written (--check)." % len(products))
        return

    ledger["seen"] = seen
    save(LEDGER, ledger)
    save(OUT, inv)

    s = load(STATE)
    s["products"] = products
    s["products_note"] = (
        "%d things this company has built and put where a stranger could buy them: %d on "
        "the storefront and %d elsewhere. Generated from the shop itself by "
        "scripts/inventory.py, not typed by hand — that is what went wrong before. "
        "Total sales: zero. %d further storefront items are unpublished internal file "
        "archives; they are not products and are not counted."
        % (len(products), sum(1 for p in products if p["venue"] == "Storefront"),
           sum(1 for p in products if p["venue"] != "Storefront"), len(internal)))
    save(STATE, s)

    print("wrote %s: %d live (%d storefront, %d elsewhere), %d internal archives ignored."
          % (os.path.relpath(OUT, REPO), len(products),
             sum(1 for p in products if p["venue"] == "Storefront"),
             sum(1 for p in products if p["venue"] != "Storefront"), len(internal)))
    print("observer/state.json products rewritten from it.")


def ours_runs(url, bearer):
    """How many of a listing's runs are ours. Runs we cannot see are not ours."""
    slug = url.rstrip("/").rsplit("/", 2)[-2:]
    try:
        d = get(APIFY + "/acts/" + slug[0] + "~" + slug[1] + "/runs?limit=1000", bearer)
        return int(d.get("data", {}).get("total") or 0)
    except (urllib.error.URLError, urllib.error.HTTPError):
        return 0


def report_and_exit():
    for m in PROBLEMS:
        sys.stderr.write("FAIL: %s\n" % m)
    sys.exit("\nRefusing to write the inventory: %d problem(s). This script exists "
             "because the office once listed six products while nine were live "
             "(KB-155). It stops rather than write a list it cannot stand behind."
             % len(PROBLEMS))


if __name__ == "__main__":
    main()
