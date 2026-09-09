#!/usr/bin/env python3
"""Idempotent Gumroad product sync.

For every products/<slug>/product.json:
  - no state/<slug>.json  -> create product (files, cover, tags, price, description), then publish
  - state exists          -> update mutable fields if the manifest hash changed, ensure published
Writes state/<slug>.json with {id, short_url, hash, published}.
Requires the `gumroad` CLI on PATH and GUMROAD_ACCESS_TOKEN in the env.
Set DRY_RUN=1 to preview without mutating.
"""
import hashlib, json, os, subprocess, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
PRODUCTS = ROOT / "products"
STATE = ROOT / "state"
STATE.mkdir(exist_ok=True)
DRY = os.environ.get("DRY_RUN") == "1"
BASE = ["--json", "--no-input", "--non-interactive", "--quiet"] + (["--dry-run"] if DRY else [])


def run(args, check=True):
    cmd = ["gumroad"] + args + BASE
    print("$", " ".join(a if " " not in a else repr(a[:40]) for a in cmd), flush=True)
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0 and check:
        print(p.stdout[-2000:], p.stderr[-2000:], file=sys.stderr)
        raise SystemExit(f"gumroad failed: {' '.join(args[:3])}")
    try:
        return json.loads(p.stdout) if p.stdout.strip() else {}
    except json.JSONDecodeError:
        return {"raw": p.stdout}


def manifest_hash(p, d):
    h = hashlib.sha256(json.dumps(p, sort_keys=True).encode())
    for f in p.get("files", []) + [p.get("cover", "")]:
        fp = d / f
        if f and fp.exists():
            h.update(fp.read_bytes())
    return h.hexdigest()[:16]


def common_flags(p):
    flags = ["--name", p["name"], "--price", str(p["price"]), "--description", p["description_html"]]
    if p.get("summary"):
        flags += ["--custom-summary", p["summary"]]
    if p.get("custom_receipt"):
        flags += ["--custom-receipt", p["custom_receipt"]]
    for t in p.get("tags", []):
        flags += ["--tag", t]
    return flags


def existing_products():
    """Map custom_permalink and name -> product dict for idempotency across fresh sessions."""
    out = run(["products", "list"], check=False)
    m = {}
    for pr in out.get("products", []) or []:
        for k in (pr.get("custom_permalink"), pr.get("name")):
            if k: m[k] = pr
    return m


def main():
    results = []
    existing = existing_products() if not DRY else {}
    for d in sorted(PRODUCTS.iterdir()):
        mf = d / "product.json"
        if not mf.exists():
            continue
        p = json.loads(mf.read_text())
        slug = d.name
        sf = STATE / f"{slug}.json"
        st = json.loads(sf.read_text()) if sf.exists() else {}
        h = manifest_hash(p, d)
        try:
            if not st.get("id"):
                pr = existing.get(p["permalink"]) or existing.get(p["name"])
                if pr:
                    # hash=None on purpose: an adopted product is of unknown completeness, so the
                    # update branch below must run. A create that fails partway (Gumroad rejected
                    # our 16:9 thumbnail but still made the product) leaves exactly this state, and
                    # recording the current hash here would mark it "unchanged" and never repair it.
                    st = {"id": pr.get("id"), "short_url": pr.get("short_url"), "hash": None,
                          "published": bool(pr.get("published"))}
                    print(f"adopted existing {slug}: {st['id']} {st['short_url']} (will re-sync)")
            if not st.get("id"):
                args = ["products", "create"] + common_flags(p) + ["--custom-permalink", p["permalink"]]
                for f in p.get("files", []):
                    args += ["--file", str(d / f)]
                if p.get("cover") and (d / p["cover"]).exists():
                    args += ["--cover-image", str(d / p["cover"])]
                    # Gumroad requires a SQUARE thumbnail and rejects the 16:9 cover here.
                    thumb = p.get("thumbnail")
                    if thumb and (d / thumb).exists():
                        args += ["--thumbnail", str(d / thumb)]
                out = run(args)
                prod = out.get("product", out)
                st = {"id": prod.get("id"), "short_url": prod.get("short_url"), "hash": h, "published": False}
                print(f"created {slug}: {st['id']} {st['short_url']}")
            elif st.get("hash") != h:
                args = ["products", "update", st["id"]] + common_flags(p)
                # Deliberately NOT re-pushing --cover-image here. It APPENDS a gallery cover
                # rather than replacing one, so three syncs left every product showing the same
                # image three times on its storefront. The gallery is owned by
                # scripts/sync_covers.py, which counts what is live before adding anything.
                # --thumbnail is safe: it replaces the single thumbnail slot.
                thumb = p.get("thumbnail")
                if thumb and (d / thumb).exists():
                    args += ["--thumbnail", str(d / thumb)]
                out = run(args)
                st["hash"] = h
                print(f"updated {slug}")
            else:
                print(f"unchanged {slug}")
            if p.get("publish") and not st.get("published") and st.get("id"):
                run(["products", "publish", st["id"]])
                st["published"] = True
                print(f"published {slug}")
            if not DRY:
                sf.write_text(json.dumps(st, indent=2))
            results.append((slug, "ok", st.get("short_url")))
        except SystemExit as e:
            results.append((slug, f"FAILED: {e}", None))
    print("\nSUMMARY")
    for r in results:
        print(" ", *r)
    failed = any("FAILED" in r[1] for r in results)

    # A clean summary is not proof: an update can report success and still leave a product
    # without the content its description promises. Check what is actually live.
    if not DRY:
        print()
        rc = subprocess.run([sys.executable, str(ROOT / "scripts" / "verify_live.py")]).returncode
        if rc != 0:
            print("verify_live reported drift — the store does not match the manifests", file=sys.stderr)
            failed = True

    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
