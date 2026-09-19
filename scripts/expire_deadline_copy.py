#!/usr/bin/env python3
"""Swap listing copy that has an expiry date once that date has passed.

The UAE listing's first sentence is "UAE Corporate Tax is due 30 September 2026." That sentence
is the strongest thing on the page until 1 October, when it becomes a listing telling buyers
about a deadline they have already missed. A scheduled reminder was the original plan for the
swap, which meant writing the replacement copy on the day, under time pressure, through an
environment whose safety classifier has blocked a Gumroad write on three separate occasions.

So the replacement is written in advance instead. A manifest may carry:

    "copy_expires":         "2026-09-30"      the last day the dated copy is true
    "summary_after":        "..."             what the summary becomes
    "description_html_after": "..."           what the description becomes
    "expired_phrases":      ["30 September 2026", ...]   what must not survive the swap

This script does the swap in the manifest (sync_products.py then pushes it), is idempotent, and
does nothing at all before the date. `expired_phrases` stays behind afterwards on purpose: it is
what verify_live.py uses to check that the dated claim really is gone from the live listing.

Run: python3 scripts/expire_deadline_copy.py [--as-of YYYY-MM-DD]
Exit 0 = nothing to do, or swapped. Exit 1 = a manifest is inconsistent.
"""
import argparse
import datetime as dt
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PRODUCTS = ROOT / "products"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--as-of", help="pretend today is this date (YYYY-MM-DD), for testing")
    a = ap.parse_args()
    today = dt.date.fromisoformat(a.as_of) if a.as_of else dt.date.today()

    swapped, problems = [], []
    for d in sorted(PRODUCTS.iterdir()):
        mf = d / "product.json"
        if not mf.exists():
            continue
        m = json.loads(mf.read_text())
        exp = m.get("copy_expires")
        if not exp:
            continue
        if not (m.get("summary_after") or m.get("description_html_after")):
            # Already swapped: copy_expires is kept so verify_live keeps checking the live
            # listing for the dated phrases. Nothing to do.
            continue
        if today <= dt.date.fromisoformat(exp):
            print(f"{d.name}: copy expires {exp}, not yet ({today}) - leaving it alone")
            continue

        for field, after in (("summary", "summary_after"),
                             ("description_html", "description_html_after")):
            if m.get(after) is not None:
                m[field] = m.pop(after)
        for phrase in m.get("expired_phrases", []):
            for field in ("summary", "description_html"):
                if phrase in (m.get(field) or ""):
                    problems.append(f"{d.name}: replacement {field} still contains {phrase!r} - "
                                    f"the swap would leave the expired claim on the listing")
        mf.write_text(json.dumps(m, indent=2, ensure_ascii=False) + "\n")
        swapped.append(d.name)
        print(f"{d.name}: copy expired {exp}, swapped to the evergreen version")

    for p in problems:
        print("PROBLEM:", p, file=sys.stderr)
    if not swapped and not problems:
        print("expire_deadline_copy: nothing due")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
