#!/usr/bin/env python3
"""Reconcile each product's gallery covers with its manifest.

`products covers add` appends — calling it every sync would pile up duplicate images, the same
trap `--file` sets. So this compares the live cover count against 1 (the main cover) + the
declared previews, and only adds the shortfall. Idempotent: a second run is a no-op.

Run:  python3 scripts/sync_covers.py [--dry-run]
"""
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PRODUCTS = ROOT / "products"
BASE = ["--json", "--no-input", "--non-interactive", "--quiet"]
DRY = "--dry-run" in sys.argv


def gumroad(args):
    p = subprocess.run(["gumroad"] + args + BASE, capture_output=True, text=True)
    if p.returncode != 0:
        print(p.stdout[-500:], p.stderr[-500:], file=sys.stderr)
        return None
    try:
        return json.loads(p.stdout) if p.stdout.strip() else {}
    except json.JSONDecodeError:
        return {}


def main():
    live = gumroad(["products", "list"]) or {}
    by_permalink = {p.get("custom_permalink"): p for p in live.get("products", [])}

    rc = 0
    for d in sorted(PRODUCTS.iterdir()):
        mf = d / "product.json"
        if not mf.exists():
            continue
        m = json.loads(mf.read_text())
        slug = d.name
        previews = [f for f in m.get("previews", []) if (d / f).exists()]
        if not previews:
            continue
        pr = by_permalink.get(m["permalink"])
        if not pr:
            print(f"{slug}: not live, skipping")
            rc = 1
            continue

        have = len(pr.get("covers") or [])
        want = 1 + len(previews)          # main cover + declared previews
        if have >= want:
            print(f"{slug}: {have} cover(s) live, nothing to add")
            continue

        missing = previews[have - 1:] if have >= 1 else previews
        print(f"{slug}: {have} live, want {want} — adding {len(missing)}")
        for f in missing:
            if DRY:
                print(f"   would add {f}")
                continue
            out = gumroad(["products", "covers", "add", pr["id"], "--image", str(d / f)])
            ok = bool(out) and out.get("success", True)
            print(f"   {'added' if ok else 'FAILED'} {f}")
            if not ok:
                rc = 1
    return rc


if __name__ == "__main__":
    sys.exit(main())
