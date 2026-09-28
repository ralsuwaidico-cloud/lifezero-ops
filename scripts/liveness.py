#!/usr/bin/env python3
"""Did each agent actually DO anything, or did it merely get woken?

Written 2026-09-28 after the Red Team was found to have never worked. Its first
four weekly fires all reported SUCCEEDED -- which means the wake was delivered,
not that work happened. It ran for 116 seconds, wrote nothing, and could not
report the failure because its only output channel was the repository it had
failed to reach. Four weeks of a silent, broken auditor (KB-149).

R&D named the durable fix and this is it: **a run that produces no artefact is
indistinguishable from a run that never started, unless something checks.**

So this checks. Every agent has a path in this repo that it must touch when it
works. If the newest commit touching that path is older than the agent's own
cadence allows, the agent is presumed not to have run, and the CEO cycle is
expected to go and find out why rather than assume a quiet week.

    python3 scripts/liveness.py          # exits 1 if anything is overdue
    python3 scripts/liveness.py --all    # show the healthy ones too
"""

import argparse
import datetime
import subprocess
import sys

# hours: the agent's cadence plus a margin. Stale beyond this and it is silent,
# not quiet. Keep the margin tight -- a generous margin is how four weeks pass.
WATCH = [
    # NOT the directory -- it holds a .gitkeep, which would make this check
    # pass forever without a single audit ever being written. A check that
    # cannot fail is not a check (lesson 5).
    ("Red Team",     ["org/red_team/FINDINGS_*.md"],                    7 * 24 + 6,
     "weekly Mon 05:33. Was broken and silent for four fires."),
    ("R&D",          ["org/RD_BOARD.md", "org/KNOWLEDGE_BASE.md"],      14,
     "every 6h at :27, persistent session."),
    ("IT Support",   ["org/REACHABILITY.md", "state/reachability.json"], 30,
     "daily 06:05, fresh session."),
    ("Apify Store",  ["org/field_reports/APIFY.md"],                    30,
     "daily 06:14 into Drive; mirrored here by R&D. A stale file means the "
     "operator OR the mirror is down -- both matter."),
    ("Acquisition",  ["org/field_reports/ACQUISITION_DESK.md"],     7 * 24 + 8,
     "weekly Mon 06:51 into Drive; mirrored here by R&D."),
    ("CEO",          ["org/CONTROL_PLANE.md"],                          30,
     "daily 07:17. If this is stale, the thing reading this is what failed."),
]


def last_touch(paths):
    out = subprocess.run(["git", "log", "-1", "--format=%cI", "--"] + paths,
                         capture_output=True, text=True).stdout.strip()
    if not out:
        return None
    return datetime.datetime.fromisoformat(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true", help="also list the healthy")
    a = ap.parse_args()

    now = datetime.datetime.now(datetime.timezone.utc)
    overdue = []
    for name, paths, limit, note in WATCH:
        t = last_touch(paths)
        if t is None:
            overdue.append((name, None, limit, note, "never touched"))
            continue
        age = (now - t).total_seconds() / 3600.0
        if age > limit:
            overdue.append((name, age, limit, note, "stale"))
        elif a.all:
            print("  ok       %-14s %5.1fh ago (limit %dh)" % (name, age, limit))

    if not overdue:
        print("every agent has produced an artefact inside its own cadence.")
        return 0

    for name, age, limit, note, why in overdue:
        print("OVERDUE    %-14s %s (limit %dh)"
              % (name, "never touched its output path" if age is None
                 else "%.1fh since it last wrote anything" % age, limit))
        print("           %s" % note)
    print("\nA run that produces no artefact is indistinguishable from a run that\n"
          "never started. Go and look -- do not record this as a quiet week.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
