#!/usr/bin/env python3
"""Pull Gumroad sales + payouts and write data/sales.json and data/scoreboard.json.
Buyer emails are hashed; no PII is committed."""
import hashlib, json, subprocess, sys, pathlib, datetime as dt, collections

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)
BASE = ["--json", "--no-input", "--non-interactive", "--quiet"]


def run(args):
    p = subprocess.run(["gumroad"] + args + BASE, capture_output=True, text=True)
    if p.returncode != 0:
        print(p.stderr[-1500:], file=sys.stderr)
        return {}
    try:
        return json.loads(p.stdout)
    except json.JSONDecodeError:
        return {}


def main():
    sales = run(["sales", "list", "--all", "--page-delay", "300ms"]).get("sales", [])
    payouts = run(["payouts", "list"]).get("payouts", [])
    products = run(["products", "list"]).get("products", [])

    clean = []
    for s in sales:
        clean.append({
            "id": s.get("id"), "product": s.get("product_name"), "product_id": s.get("product_id"),
            "created_at": s.get("created_at"), "price_cents": s.get("price"), "currency": s.get("currency"),
            "refunded": s.get("refunded", False), "country": s.get("country"),
            "referrer": s.get("referrer"), "utm": {k: s.get(k) for k in ("utm_source", "utm_medium", "utm_campaign") if s.get(k)},
            "buyer_hash": hashlib.sha256((s.get("email") or "").lower().encode()).hexdigest()[:12],
            "needs_fulfilment": "custom" in (s.get("product_name") or "").lower(),
            "custom_fields": s.get("custom_fields"),
        })
    now = dt.datetime.now(dt.timezone.utc)
    def cents(rows): return sum(int(r.get("price_cents") or 0) for r in rows if not r.get("refunded"))
    def since(days):
        cutoff = (now - dt.timedelta(days=days)).isoformat()
        return [r for r in clean if (r.get("created_at") or "") >= cutoff]
    by_product = collections.Counter()
    rev_product = collections.Counter()
    for r in clean:
        if not r["refunded"]:
            by_product[r["product"]] += 1
            rev_product[r["product"]] += int(r.get("price_cents") or 0)
    board = {
        "generated_at": now.isoformat(),
        "lifetime_sales": len([r for r in clean if not r["refunded"]]),
        "lifetime_revenue_usd": cents(clean) / 100,
        "last_7d_revenue_usd": cents(since(7)) / 100,
        "last_30d_revenue_usd": cents(since(30)) / 100,
        "refunds": len([r for r in clean if r["refunded"]]),
        "unique_buyers": len({r["buyer_hash"] for r in clean}),
        "sales_by_product": dict(by_product),
        "revenue_by_product_usd": {k: v / 100 for k, v in rev_product.items()},
        "open_fulfilment": [r for r in clean if r["needs_fulfilment"]],
        "products": [{"id": p.get("id"), "name": p.get("name"), "url": p.get("short_url"), "published": p.get("published"),
                      "sales_count": p.get("sales_count"), "sales_usd_cents": p.get("sales_usd_cents"), "price": p.get("price")} for p in products],
        "payouts": [{"date": p.get("payout_date") or p.get("date"), "amount_cents": p.get("amount_cents") or p.get("amount"), "status": p.get("status")} for p in payouts],
    }
    (DATA / "sales.json").write_text(json.dumps(clean, indent=1))
    (DATA / "scoreboard.json").write_text(json.dumps(board, indent=1))
    print(json.dumps({k: board[k] for k in ("lifetime_sales", "lifetime_revenue_usd", "last_7d_revenue_usd", "sales_by_product")}, indent=1))


if __name__ == "__main__":
    main()
