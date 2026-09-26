#!/usr/bin/env python3
"""LIFE ZERO runs on dog years: seven company days for every human day.

Set by the chairman on 2026-09-26. One calendar day is divided into seven
company days of 24/7 hours each (3h25m42.857s). They are numbered 1 to 7 within
the date and written `<n>-DD/MM/YYYY` -- 1-26/09/2026 through 7-26/09/2026, then
1-27/09/2026. The company's age is the count of those segments since it started.

Why it is written down rather than assumed: every "we have been at $0 for N
days" line in this organization is now seven times larger than it looked, and
that is the point of the ratio. A week of the owner's patience is a year and a
half of this company's life.

    python3 scripts/company_clock.py           # now
    python3 scripts/company_clock.py --at 2026-09-26T21:00:00Z
"""

import argparse
import datetime
import json

START = datetime.date(2026, 9, 4)          # first day of LIFE ZERO
SEGMENTS = 7                               # company days per human day
SEG_SECONDS = 86400.0 / SEGMENTS


def clock(now=None):
    now = now or datetime.datetime.now(datetime.timezone.utc)
    if now.tzinfo is None:
        now = now.replace(tzinfo=datetime.timezone.utc)
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    elapsed = (now - midnight).total_seconds()
    # 1..7; the clamp only matters on a leap second
    segment = min(SEGMENTS, int(elapsed // SEG_SECONDS) + 1)
    human_days = (now.date() - START).days
    seg_start = midnight + datetime.timedelta(seconds=(segment - 1) * SEG_SECONDS)
    seg_end = midnight + datetime.timedelta(seconds=segment * SEG_SECONDS)
    return {
        "label": "%d-%s" % (segment, now.strftime("%d/%m/%Y")),
        "segment": segment,
        "of": SEGMENTS,
        "human_days": human_days,
        "company_days": human_days * SEGMENTS + segment,
        "ratio": "7:1",
        "started": START.isoformat(),
        "segment_started": seg_start.strftime("%H:%M UTC"),
        "segment_ends": seg_end.strftime("%H:%M UTC"),
        "note": ("Seven company days to one human day, set by the chairman on 2026-09-26. "
                 "Every zero this company has recorded is seven times longer than it looks."),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--at", help="ISO instant to evaluate instead of now")
    a = ap.parse_args()
    now = None
    if a.at:
        now = datetime.datetime.fromisoformat(a.at.replace("Z", "+00:00"))
    c = clock(now)
    print(json.dumps(c, indent=1))
    print("\n%s  —  company day %d of its life (human day %d)"
          % (c["label"], c["company_days"], c["human_days"]))


if __name__ == "__main__":
    main()
