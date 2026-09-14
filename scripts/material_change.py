#!/usr/bin/env python3
"""Decide whether data/scoreboard.json changed in a way worth committing.

The 6-hourly routine defines material as: any new sale, refund, payout, product, first
publish, first rating, or any UTM click or offer-code use that was not there last run. Until
now that comparison was made by eye every cycle, which is exactly the kind of judgement that
drifts - and it started costing real noise once a SECOND AUTHOR began working on the same
Gumroad account. Their product renames are not commercial events, but they do change the
scoreboard, so an uncommitted diff re-tripped the gate every six hours until it was committed
to silence it.

So the rule is written down instead:
  - `generated_at` never counts.
  - For products this repo manages (a manifest in products/), ANY field change counts - a
    price or publish flag moving without us doing it is exactly what we want to hear about.
  - For products managed elsewhere, appearing and disappearing counts, and so does any change
    to sales_count or price. A rename does not.

Exit 0 = material (commit it). Exit 1 = not material (revert and report one line).
Run: python3 scripts/material_change.py
"""
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCOREBOARD = ROOT / "data" / "scoreboard.json"
PRODUCTS = ROOT / "products"

# A rename is cosmetic; these are not.
TRACKED_FIELDS = ("published", "sales_count", "sales_usd_cents", "price")


def committed():
    p = subprocess.run(["git", "show", "HEAD:data/scoreboard.json"],
                       cwd=ROOT, capture_output=True, text=True)
    return json.loads(p.stdout) if p.returncode == 0 else {}


def managed_permalinks():
    return {json.loads((d / "product.json").read_text())["permalink"]
            for d in PRODUCTS.iterdir() if (d / "product.json").exists()}


def by_permalink(board):
    out = {}
    for p in board.get("products", []) or []:
        out[p.get("url", "").rsplit("/", 1)[-1]] = p
    return out


def main():
    new, old = json.loads(SCOREBOARD.read_text()), committed()
    mine = managed_permalinks()
    reasons = []

    for k in ("lifetime_sales", "lifetime_revenue_usd", "refunds", "unique_buyers",
              "sales_by_product", "revenue_by_product_usd", "open_fulfilment", "payouts"):
        if new.get(k) != old.get(k):
            reasons.append(f"{k}: {old.get(k)!r} -> {new.get(k)!r}")

    n, o = by_permalink(new), by_permalink(old)
    for perm in sorted(set(n) | set(o)):
        if perm not in o:
            reasons.append(f"new product: {perm}")
        elif perm not in n:
            reasons.append(f"product disappeared: {perm}")
        elif perm in mine:
            for f in set(n[perm]) | set(o[perm]):
                if n[perm].get(f) != o[perm].get(f):
                    reasons.append(f"{perm} (ours) {f}: {o[perm].get(f)!r} -> {n[perm].get(f)!r}")
        else:
            for f in TRACKED_FIELDS:
                if n[perm].get(f) != o[perm].get(f):
                    reasons.append(f"{perm} {f}: {o[perm].get(f)!r} -> {n[perm].get(f)!r}")

    if reasons:
        print("MATERIAL:")
        for r in reasons:
            print("  -", r)
        return 0
    print("not material (renames by other authors and generated_at do not count)")
    return 1


if __name__ == "__main__":
    sys.exit(main())
