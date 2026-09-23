#!/usr/bin/env python3
"""Operate the $95 custom-sheet service: what is owed, how long is left, what was asked for.

Written on 2026-09-23 as a rehearsal, before any order existed, because the first time this
pipeline runs should not be with a paying customer and a 48-hour clock. The rehearsal found
three things, and only one of them was code.

1. `open_fulfilment` could never be cleared (it matched the word "custom" in a product name),
   so a delivered order would have alarmed on every pull for ever. Fixed in pull_sales.py with
   a delivery ledger at data/delivered.json, which this script writes.
2. Nothing computed hours remaining, so the routine's "say so first and loudest if inside 24
   hours" would have been hand arithmetic at exactly the moment hands are least reliable.
3. **The brief arrives by email.** The receipt tells the buyer to reply with the filled-in pack
   attached. I have no inbox, so the very first step of fulfilment needs the owner. That is why
   the two compulsory brief questions are now CHECKOUT custom fields as well: the moment an
   order lands, `sales.custom_fields` carries enough to start, through the API, without anyone
   forwarding anything. The pack still carries the detail for the buyer who wants to give it.

Commands:
  status                 what is open, hours remaining, and the brief as submitted
  mark-delivered <id>    record a sale as delivered (with an optional --note)

Buyer emails are hashed upstream in pull_sales.py and stay hashed here. Never print PII.
"""
import argparse
import datetime as dt
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
LEDGER = DATA / "delivered.json"


def load(name):
    p = DATA / name
    return json.loads(p.read_text()) if p.exists() else ([] if name != "scoreboard.json" else {})


def status():
    board = load("scoreboard.json")
    open_rows = board.get("open_fulfilment") or []
    if not open_rows:
        n = len(load("delivered.json"))
        print(f"fulfilment: nothing owed"
              + (f" ({n} order(s) delivered to date)" if n else ""))
        return 0
    open_rows.sort(key=lambda r: r.get("hours_remaining", 1e9))
    worst = open_rows[0].get("hours_remaining")
    if worst is not None and worst < 24:
        print(f"*** {len(open_rows)} ORDER(S) OWED, THE MOST URGENT HAS {worst} HOURS LEFT ***")
    for r in open_rows:
        print(f"\nsale {r['id']}  buyer {r['buyer_hash']}  bought {r.get('created_at')}")
        print(f"  due {r.get('due_at')}  ->  {r.get('hours_remaining')} hours remaining")
        cf = r.get("custom_fields")
        if cf:
            print("  brief, as submitted at checkout:")
            items = cf.items() if isinstance(cf, dict) else [(c.get("name"), c.get("value")) for c in cf]
            for k, v in items:
                print(f"    {k}: {v}")
        else:
            print("  NO checkout brief on this sale. The pack is emailed, and this session has "
                  "no inbox - the owner must forward it before the build can start.")
    return 1 if (worst is not None and worst < 24) else 0


def mark_delivered(sale_id, note):
    rows = load("delivered.json")
    if any(r["sale_id"] == sale_id for r in rows):
        print(f"{sale_id} was already recorded as delivered")
        return 0
    rows.append({"sale_id": sale_id, "note": note or "",
                 "delivered_at": dt.datetime.now(dt.timezone.utc).isoformat()})
    LEDGER.write_text(json.dumps(rows, indent=1) + "\n")
    print(f"recorded {sale_id} as delivered; the next pull_sales run will drop it from "
          f"open_fulfilment")
    return 0


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status")
    d = sub.add_parser("mark-delivered")
    d.add_argument("sale_id")
    d.add_argument("--note", default="")
    a = ap.parse_args()
    return status() if a.cmd == "status" else mark_delivered(a.sale_id, a.note)


if __name__ == "__main__":
    sys.exit(main())
