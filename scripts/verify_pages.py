#!/usr/bin/env python3
"""Verify each storefront page live on Gumroad matches its source in growth/pages/.

Two storefront pages are now real acquisition assets, and the only way to edit one is a raw
PUT to /v2/pages/<slug> - there is no `gumroad pages update`. A page can therefore drift, be
truncated, or be overwritten (it has happened: a probe PUT once replaced a whole page with the
word "probe") with nothing noticing. The repo holds the source of truth; this compares it.

Gumroad's sanitiser inserts <tbody> around table rows, so the files in growth/pages/ are stored
already normalised and the comparison is exact rather than fuzzy.

Exit 0 = every page matches. Non-zero = drift, listed.
"""
import json
import os
import pathlib
import sys
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES = ROOT / "growth" / "pages"


def fetch(slug):
    req = urllib.request.Request(f"https://api.gumroad.com/v2/pages/{slug}")
    # Token comes from the environment and is never printed, including on the error paths.
    req.add_header("Authorization", "Bearer " + os.environ["GUMROAD_ACCESS_TOKEN"])
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r).get("page")
    except urllib.error.HTTPError as e:
        print(f"  (HTTP {e.code} reading {slug})", file=sys.stderr)
        return None


def main():
    if not PAGES.is_dir():
        print("verify_pages: no growth/pages/ directory, nothing to check")
        return 0
    problems = []
    checked = 0
    for f in sorted(PAGES.glob("*.html")):
        slug = f.stem
        page = fetch(slug)
        if page is None:
            problems.append(f"{slug}: could not read the live page")
            continue
        # A page can hold rich-text `content` OR `custom_html`, and the two are exclusive.
        # On 2026-09-14 the other author converted ct-deadline-2026 from content to
        # custom_html; this checker only read `content`, so it reported the page EMPTY and
        # very nearly had me "restore" my copy over their rewrite. Read both, and say which.
        live_content = (page.get("content") or "").strip()
        live_html = (page.get("custom_html") or "").strip()
        local = f.read_text().strip()

        if not live_content and not live_html:
            problems.append(f"{slug}: the live page is EMPTY - buyers see a blank article")
        elif live_html and not live_content:
            problems.append(f"{slug}: live page is now custom_html ({len(live_html)} chars), not "
                            f"the rich-text content this repo holds ({len(local)} chars). Someone "
                            f"rewrote it - look before overwriting")
        elif live_content != local:
            problems.append(f"{slug}: live content differs from growth/pages/{f.name} "
                            f"({len(live_content)} chars live vs {len(local)} local)")
        else:
            checked += 1
    for p in problems:
        print("DRIFT:", p)
    if not problems:
        print(f"verify_pages: {checked} storefront page(s) match their source")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
