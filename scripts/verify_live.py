#!/usr/bin/env python3
"""Verify what is actually live on Gumroad against products/<slug>/product.json.

Written because "success: true" has twice hidden a partial sync:
  - a create that returned success:false had already made the products server-side;
  - an update that returned success:true left the $95 service with no content attached
    while its description promised a download.
The list endpoint is not sufficient either: its `file_info` stays empty for a product whose
content is a file embed, so content is checked through `products content get`.

Exit code 0 = every published product matches its manifest. Non-zero = drift, listed.
"""
import datetime as dt
import json
import os
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PRODUCTS = ROOT / "products"
BASE = ["--json", "--no-input", "--non-interactive", "--quiet"]


def run(args, parse=True):
    p = subprocess.run(["gumroad"] + args + (BASE if parse else ["--no-input", "--non-interactive"]),
                       capture_output=True, text=True)
    if p.returncode != 0:
        return None
    try:
        return json.loads(p.stdout) if p.stdout.strip() else None
    except json.JSONDecodeError:
        return None


def refund_policy(pid):
    """The product's refund policy, which `products list` does not carry.

    Caught on the day this check was written: the list payload has `refund_policy: null` for
    every product, set or not, so a check built on the list endpoint reports drift on a product
    that is configured correctly - a false alarm that never goes away and trains you to ignore
    the verifier. `products view` returns the real object. Verify against the endpoint that
    actually holds the field, not the one already in hand.
    """
    out = run(["products", "view", pid])
    return ((out or {}).get("product") or {}).get("refund_policy") or {}


def custom_fields(pid):
    """Checkout custom fields, which `products list` does carry but `products view` reports more
    reliably. These are the two compulsory brief questions: they are the only route by which the
    $95 service's brief reaches this repo without going through somebody's email inbox, so a
    silently deleted field does not just lose a form, it puts the 48-hour clock back on a human.
    """
    out = run(["custom-fields", "list", "--product", pid])
    return (out or {}).get("custom_fields") or []


def content_file_count(pid):
    """Number of file embeds in the product's content pages."""
    p = subprocess.run(["gumroad", "products", "content", "get", pid,
                        "--no-input", "--non-interactive"], capture_output=True, text=True)
    if p.returncode != 0 or not p.stdout.strip():
        return None
    try:
        pages = json.loads(p.stdout)
    except json.JSONDecodeError:
        return None
    n = 0
    for page in pages or []:
        for node in ((page.get("description") or {}).get("content") or []):
            if node.get("type") == "fileEmbed":
                n += 1
    return n


def main():
    live = run(["products", "list", "--all"]) or {}
    by_permalink = {p.get("custom_permalink"): p for p in live.get("products", []) if p.get("custom_permalink")}

    problems = []
    for d in sorted(PRODUCTS.iterdir()):
        mf = d / "product.json"
        if not mf.exists():
            continue
        m = json.loads(mf.read_text())
        slug, permalink = d.name, m["permalink"]
        pr = by_permalink.get(permalink)
        if not pr:
            problems.append(f"{slug}: not found on Gumroad (permalink {permalink})")
            continue

        if m.get("publish") and not pr.get("published"):
            problems.append(f"{slug}: manifest says publish, but the product is not published")

        want_price = int(float(m["price"]) * 100)
        if pr.get("price") != want_price:
            problems.append(f"{slug}: price is {pr.get('price')} cents, manifest says {want_price}")

        # Gumroad reports pay-what-you-want as `customizable_price`. Without this check a
        # free product that quietly reverted to a fixed $0 would still verify clean, and the
        # tip jar the lead magnet depends on would be gone with no signal.
        want_pwyw = bool(m.get("pay_what_you_want"))
        if bool(pr.get("customizable_price")) != want_pwyw:
            problems.append(f"{slug}: pay-what-you-want is {bool(pr.get('customizable_price'))}, "
                            f"manifest says {want_pwyw}")

        if m.get("thumbnail") and not pr.get("thumbnail_url"):
            problems.append(f"{slug}: manifest declares a thumbnail but none is live")

        if m.get("cover") and not pr.get("preview_url"):
            problems.append(f"{slug}: manifest declares a cover but none is live")

        # Tags went unnoticed once: two updates failed on an over-length tag and this still
        # reported everything matching, because it was not looking at tags at all.
        want_tags, got_tags = m.get("tags", []), pr.get("tags") or []
        if sorted(want_tags) != sorted(got_tags):
            missing = [t for t in want_tags if t not in got_tags]
            extra = [t for t in got_tags if t not in want_tags]
            problems.append(f"{slug}: tags differ (missing {missing}, unexpected {extra})")

        # Category was pushed for the first time today; a field the store carries but the
        # verifier never looks at is a field that silently drifts (see tags, 2026-09-09).
        want_cat = m.get("category")
        if want_cat and pr.get("category") != want_cat:
            problems.append(f"{slug}: category is {pr.get('category')!r}, manifest says {want_cat!r}")

        # Shipped 2026-09-17 and therefore checked 2026-09-17. The trap here is specific:
        # `refund_period: "inherit"` is what every product read BEFORE this change, and the
        # account policy it inherits reports `in_effect: false` - so "inherit" renders as no
        # refund terms shown to the buyer at all, while looking like a configured value. A
        # product that silently reverts to inherit would show a clean listing and a silent page.
        # Shipped 2026-09-23, checked 2026-09-23. `custom-fields create` has no idempotency
        # key, so a second sync could append duplicates of the same question - the buyer would
        # be asked twice at checkout on a $95 purchase.
        want_cf = m.get("custom_fields")
        if want_cf:
            live_cf = custom_fields(pr["id"])
            want_names = [c["name"] for c in want_cf]
            got_names = [c.get("name") for c in live_cf]
            # Duplicates FIRST. Found by injecting a real duplicate on the live product: the
            # set comparison below fires on it too, but reports "missing [], unexpected []",
            # which reads like a broken checker rather than a duplicated question. The operator
            # needs to be told what actually happened, not handed two empty lists.
            if len(got_names) != len(set(got_names)):
                dupes = sorted({n for n in got_names if got_names.count(n) > 1})
                problems.append(f"{slug}: a checkout custom field is DUPLICATED - the buyer is "
                                f"asked the same question twice at a $95 checkout ({dupes})")
            elif sorted(got_names) != sorted(want_names):
                missing = [n for n in want_names if n not in got_names]
                extra = [n for n in got_names if n not in want_names]
                problems.append(f"{slug}: checkout custom fields differ (missing {missing}, "
                                f"unexpected {extra})")
            else:
                by_name = {c.get("name"): c for c in live_cf}
                for c in want_cf:
                    if bool(by_name[c["name"]].get("required")) != bool(c.get("required")):
                        problems.append(
                            f"{slug}: custom field {c['name']!r} is "
                            f"required={by_name[c['name']].get('required')} live, manifest says "
                            f"{c.get('required')}")

        # A dated claim is the only kind of copy that goes wrong while nobody touches it.
        # "UAE Corporate Tax is due 30 September 2026" is the strongest sentence on that
        # listing until 1 October, when it becomes a page telling buyers about a deadline they
        # have already missed. scripts/expire_deadline_copy.py swaps in the evergreen version;
        # this is the check that the swap actually reached the store, and it reads the LIVE
        # description rather than the manifest, because a manifest that was swapped and never
        # synced looks identical to one that was.
        exp = m.get("copy_expires")
        if exp:
            as_of = os.environ.get("VERIFY_AS_OF")
            today = dt.date.fromisoformat(as_of) if as_of else dt.date.today()
            if today > dt.date.fromisoformat(exp):
                live_text = (pr.get("description") or "") + " " + (pr.get("custom_summary") or "")
                stale = [p for p in m.get("expired_phrases", []) if p in live_text]
                if stale:
                    problems.append(f"{slug}: the live listing still claims {stale[0]!r} after "
                                    f"{exp} - buyers are being sold on a deadline that has "
                                    f"passed. Run scripts/expire_deadline_copy.py and sync")
            days = (dt.date.fromisoformat(exp) - today).days
            if 0 <= days <= 3:
                print(f"NOTE: {slug} dated copy expires in {days} day(s) ({exp}); "
                      f"expire_deadline_copy.py will swap it")

        # Injection found the blind spot the moment the check existed: gated on the manifest
        # declaring a period, DELETING the field from a manifest made the whole check vanish
        # silently while the guarantee could disappear from the store. This storefront has
        # decided every product carries 30 days, so an undeclared one is itself the drift.
        want_refund = m.get("refund_period")
        if not want_refund:
            problems.append(f"{slug}: manifest declares no refund_period - every product on "
                            f"this storefront is supposed to carry one, and a missing field "
                            f"silently disables the rest of this check")
        if want_refund:
            live_rp = refund_policy(pr["id"])
            got_refund = str(live_rp.get("refund_period") or "")
            if got_refund != str(want_refund):
                problems.append(f"{slug}: refund period is {got_refund!r}, manifest says "
                                f"{str(want_refund)!r}"
                                + (" - 'inherit' means the buyer is shown nothing, because the "
                                   "account policy is not in effect" if got_refund == "inherit"
                                   else ""))
            if live_rp.get("inherited"):
                problems.append(f"{slug}: refund policy is still inherited from the account, "
                                f"which reports in_effect:false - no terms reach the buyer")
            want_fp = (m.get("refund_fine_print") or "").strip()
            got_fp = (live_rp.get("fine_print") or "").strip()
            if want_fp and got_fp != want_fp:
                problems.append(f"{slug}: refund fine print differs from the manifest "
                                f"({len(got_fp)} chars live vs {len(want_fp)} local)")

        # `covers add` appends, so three cover pushes once left every product showing the same
        # image three times. Count them.
        want_covers = 1 + len(m.get("previews", [])) if m.get("cover") else len(m.get("previews", []))
        got_covers = len(pr.get("covers") or [])
        if want_covers and got_covers != want_covers:
            problems.append(f"{slug}: {got_covers} gallery cover(s) live, manifest implies "
                            f"{want_covers} (duplicates? `covers add` appends)")

        # The important one: a product whose description promises a download must deliver one.
        want_files = len(m.get("files", []))
        if want_files:
            got = content_file_count(pr["id"])
            if got is None:
                problems.append(f"{slug}: could not read product content to verify files")
            elif got == 0:
                problems.append(f"{slug}: manifest declares {want_files} file(s) but NOTHING is "
                                f"attached - buyers would pay and receive no content")
            elif got != want_files:
                problems.append(f"{slug}: {got} file embed(s) live, manifest declares {want_files} "
                                f"(duplicate embeds? `--file` appends, it does not replace)")

    # Live products with no manifest are not necessarily wrong - they may be managed elsewhere -
    # but nothing in this repo verifies them, and on 2026-09-11 two appeared on the account that
    # this repo had never heard of. The old success line counted every live product and so
    # claimed to have checked them; silence about the gap is how a store drifts. Name them.
    manifest_permalinks = {json.loads((d / "product.json").read_text())["permalink"]
                           for d in PRODUCTS.iterdir() if (d / "product.json").exists()}
    unmanaged = sorted(set(by_permalink) - manifest_permalinks)

    for p in problems:
        print("DRIFT:", p)
    for u in unmanaged:
        print(f"UNMANAGED: {u} is live on Gumroad with no manifest in products/ - "
              f"nothing in this repo verifies it")
    if not problems:
        print(f"verify_live: {len(manifest_permalinks)} manifest(s) checked, all matching "
              f"({len(by_permalink)} product(s) live in total)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
