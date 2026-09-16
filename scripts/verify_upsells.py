#!/usr/bin/env python3
"""Verify every checkout cross-sell live on Gumroad matches its source in growth/upsells/.

A cross-sell is the only automated path from the free calculator to the $19 tracker: it is
shown at checkout, so unlike a link in a description nobody has to go looking for it. That
makes it a funnel component with no visible surface in this repo - it does not appear on any
product page, so a paused, deleted, retargeted or duplicated cross-sell is invisible until you
read the API. Three things this checks that have each already gone wrong on this account:

  - `paused`: a paused cross-sell is live-but-silent. Nothing else would ever say so.
  - duplicates: every Gumroad write on this project has appended rather than replaced at least
    once, and `upsells create` has no idempotency key. Two cross-sells for the same pair is not
    hypothetical - the other author already has exactly that (their GH-900 free product carries
    two offers for the same 300-question bank), so a buyer can be shown the same offer twice.
  - the selected-product list: a cross-sell pointed at the wrong product offers the tracker to
    someone who came for UAE tax.

Like verify_live.py this reports what it CHECKED, not what is live, and names the upsells it
does not manage - the other author's - so coverage is never overstated.

Exit 0 = every managed cross-sell matches. Non-zero = drift, listed.
"""
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SPECS = ROOT / "growth" / "upsells"
STATE = ROOT / "state"


def live_upsells():
    p = subprocess.run(["gumroad", "upsells", "list", "--json", "--no-input", "--non-interactive"],
                       capture_output=True, text=True)
    if p.returncode != 0 or not p.stdout.strip():
        return None
    try:
        return json.loads(p.stdout).get("upsells") or []
    except json.JSONDecodeError:
        return None


def product_id(slug):
    f = STATE / f"{slug}.json"
    return json.loads(f.read_text()).get("id") if f.exists() else None


def main():
    if not SPECS.is_dir():
        print("verify_upsells: no growth/upsells/ directory, nothing to check")
        return 0
    live = live_upsells()
    if live is None:
        print("DRIFT: could not read the live upsell list")
        return 1

    problems, checked, managed_ids = [], 0, set()

    for f in sorted(SPECS.glob("*.json")):
        spec = json.loads(f.read_text())
        name = spec["name"]
        matches = [u for u in live if u.get("name") == name]
        if not matches:
            problems.append(f"{f.name}: no live cross-sell named {name!r} - the free-to-paid "
                            f"path at checkout does not exist")
            continue
        if len(matches) > 1:
            problems.append(f"{f.name}: {len(matches)} live cross-sells named {name!r} - a buyer "
                            f"is shown the same offer more than once "
                            f"({', '.join(u.get('id', '?') for u in matches)})")
            managed_ids.update(u.get("id") for u in matches)
            continue
        u = matches[0]
        managed_ids.add(u.get("id"))
        before = len(problems)

        want_offered = product_id(spec["offered_product_slug"])
        got_offered = (u.get("product") or {}).get("id")
        want_selected = {product_id(s) for s in spec["selected_product_slugs"]}
        got_selected = {s.get("id") for s in (u.get("selected_products") or [])}

        if None in want_selected or want_offered is None:
            problems.append(f"{f.name}: a product slug has no state/<slug>.json, so there is "
                            f"nothing to compare the live targeting against")
            continue
        if got_offered != want_offered:
            problems.append(f"{name}: offers the wrong product "
                            f"({got_offered} live vs {want_offered} expected)")
        if got_selected != want_selected:
            problems.append(f"{name}: shown to the wrong buyers "
                            f"(live {sorted(got_selected)} vs expected {sorted(want_selected)})")
        # A paused cross-sell still lists, still reads correct, and shows buyers nothing.
        if bool(u.get("paused")) != bool(spec.get("paused")):
            problems.append(f"{name}: paused={u.get('paused')} live, expected "
                            f"{spec.get('paused')} - a paused cross-sell is silent at checkout")
        if bool(u.get("cross_sell")) != bool(spec.get("cross_sell")):
            problems.append(f"{name}: cross_sell={u.get('cross_sell')} live, expected "
                            f"{spec.get('cross_sell')}")
        if bool(u.get("universal")) != bool(spec.get("universal")):
            problems.append(f"{name}: universal={u.get('universal')} live, expected "
                            f"{spec.get('universal')} - a universal offer is shown to every "
                            f"buyer on this account, including the other author's")
        for field in ("text", "description"):
            if (u.get(field) or "").strip() != (spec.get(field) or "").strip():
                problems.append(f"{name}: {field} differs from growth/upsells/{f.name}")
        if (u.get("discount") or None) != (spec.get("discount") or None):
            problems.append(f"{name}: discount {u.get('discount')!r} live, expected "
                            f"{spec.get('discount')!r}")
        if len(problems) == before:
            checked += 1

    for p in problems:
        print("DRIFT:", p)
    unmanaged = sorted(u.get("name", "?") for u in live if u.get("id") not in managed_ids)
    for n in unmanaged:
        print(f"UNMANAGED: cross-sell {n!r} is live on this account and has no source in "
              f"growth/upsells/ - nothing here checks it")
    if not problems:
        print(f"verify_upsells: {checked} cross-sell(s) match their source "
              f"({len(unmanaged)} live but unmanaged)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
