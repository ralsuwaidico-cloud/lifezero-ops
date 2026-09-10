#!/usr/bin/env python3
"""Replace a product's attached file when the local file changes.

`products update --file` APPENDS an embed, it does not replace one, and nothing in the sync
noticed when a rebuilt workbook never reached buyers. A corrected Mercari fee sat in git for a
build while the live product still served the old workbook, and verify_live could not see it
because it counts embeds rather than comparing content.

So: record a hash of each declared file in state/<slug>.files.json. When the hash changes,
upload the new file and prune the previous embed via `products content set`, leaving exactly one.

Run:  python3 scripts/sync_files.py [--dry-run]
"""
import hashlib
import json
import pathlib
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
PRODUCTS = ROOT / "products"
STATE = ROOT / "state"
STATE.mkdir(exist_ok=True)
BASE = ["--json", "--no-input", "--non-interactive", "--quiet"]
DRY = "--dry-run" in sys.argv


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


def gumroad(args, parse=True):
    flags = BASE if parse else ["--no-input", "--non-interactive"]
    p = subprocess.run(["gumroad"] + args + flags, capture_output=True, text=True)
    if p.returncode != 0:
        print(p.stdout[-400:], p.stderr[-400:], file=sys.stderr)
        return None
    if not parse:
        return p.stdout
    try:
        return json.loads(p.stdout) if p.stdout.strip() else {}
    except json.JSONDecodeError:
        return {}


def embed_ids(pid):
    raw = gumroad(["products", "content", "get", pid], parse=False)
    if raw is None:
        return None, None
    pages = json.loads(raw)
    ids = [n["attrs"]["id"]
           for pg in pages
           for n in (pg.get("description") or {}).get("content") or []
           if n.get("type") == "fileEmbed"]
    return pages, ids


def prune(pid, pages, keep):
    for pg in pages:
        d = pg.get("description") or {}
        d["content"] = [n for n in (d.get("content") or [])
                        if not (n.get("type") == "fileEmbed" and n["attrs"].get("id") != keep)]
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as fh:
        json.dump(pages, fh)
        tmp = fh.name
    out = gumroad(["products", "content", "set", pid, tmp], parse=False)
    return out is not None


def main():
    live = gumroad(["products", "list"]) or {}
    by_permalink = {p.get("custom_permalink"): p for p in live.get("products", [])}

    rc = 0
    for d in sorted(PRODUCTS.iterdir()):
        mf = d / "product.json"
        if not mf.exists():
            continue
        m = json.loads(mf.read_text())
        files = [f for f in m.get("files", []) if (d / f).exists()]
        if not files:
            continue
        slug = d.name
        pr = by_permalink.get(m["permalink"])
        if not pr:
            print(f"{slug}: not live, skipping")
            continue

        sf = STATE / f"{slug}.files.json"
        known = json.loads(sf.read_text()) if sf.exists() else {}
        want = {f: sha(d / f) for f in files}
        if known == want:
            print(f"{slug}: attached file unchanged")
            continue

        print(f"{slug}: file changed — replacing on Gumroad")
        if DRY:
            print("   (dry run)")
            continue

        for f in files:
            if gumroad(["products", "update", pr["id"], "--file", str(d / f)]) is None:
                print(f"   FAILED to upload {f}")
                rc = 1
                break
        else:
            pages, ids = embed_ids(pr["id"])
            if not ids:
                print("   could not read embeds back")
                rc = 1
            elif len(ids) > 1 and not prune(pr["id"], pages, keep=ids[-1]):
                print("   FAILED to prune old embed")
                rc = 1
            else:
                _, final = embed_ids(pr["id"])
                if final and len(final) == len(files):
                    sf.write_text(json.dumps(want, indent=2))
                    print(f"   replaced; {len(final)} embed(s) live")
                else:
                    print(f"   unexpected embed count {final}")
                    rc = 1
    return rc


if __name__ == "__main__":
    sys.exit(main())
