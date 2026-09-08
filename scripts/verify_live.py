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
import json
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
    live = run(["products", "list"]) or {}
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

        if m.get("thumbnail") and not pr.get("thumbnail_url"):
            problems.append(f"{slug}: manifest declares a thumbnail but none is live")

        if m.get("cover") and not pr.get("preview_url"):
            problems.append(f"{slug}: manifest declares a cover but none is live")

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

    for p in problems:
        print("DRIFT:", p)
    if not problems:
        print(f"verify_live: {len(by_permalink)} product(s) match their manifests")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
