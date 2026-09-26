#!/usr/bin/env python3
"""Build the LIFE ZERO Observer Office page from shared organizational state.

The page is a view. `observer/state.json` is the data, and it is the only thing
that should change between builds -- the agents write state, the observer reads
it. Editing the generated HTML by hand defeats that and will be overwritten.

    python3 scripts/build_observer.py          # build, then publish office.html
    python3 scripts/build_observer.py --check  # validate state.json only
"""

import argparse
import datetime
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from company_clock import clock  # noqa: E402  -- the 7:1 ratio, one definition

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE = os.path.join(REPO, "observer", "state.json")
TEMPLATE = os.path.join(REPO, "observer", "office.template.html")
OUT = os.path.join(REPO, "observer", "office.html")
MARKER = "__LIFEZERO_STATE__"

REQUIRED_AGENT = ["id", "display", "role", "room", "status", "avatar",
                  "current_task", "why", "schedule", "next_run", "priority"]
STATUSES = {"WORKING", "RESEARCHING", "WAITING", "BLOCKED", "ERROR", "IDLE", "REVENUE"}


def fail(msg):
    print("FAIL: " + msg)
    return False


def validate(s):
    """Catch the failure this page must never have: showing something untrue."""
    ok = True
    rooms = {r["id"] for r in s.get("rooms", [])}
    gates = {g["id"] for g in s.get("gates", [])}
    agents = {a.get("id") for a in s.get("agents", [])}

    for a in s.get("agents", []):
        who = a.get("id", "?")
        for k in REQUIRED_AGENT:
            if a.get(k) in (None, "") and not (k == "next_run" and a.get("next_run") is None):
                ok = fail("agent %s is missing %s" % (who, k))
        if a.get("status") not in STATUSES:
            ok = fail("agent %s has unknown status %r" % (who, a.get("status")))
        if a.get("room") not in rooms:
            ok = fail("agent %s sits in unknown room %r" % (who, a.get("room")))
        b = a.get("blocked_by")
        if b and b not in gates and b != "egress":
            ok = fail("agent %s is blocked by unknown gate %r" % (who, b))
        if a.get("status") == "BLOCKED" and not b:
            ok = fail("agent %s shows BLOCKED but names nothing blocking it" % who)
        if b and a.get("status") != "BLOCKED":
            ok = fail("agent %s names a blocker but does not show BLOCKED" % who)
        if a.get("runs") == 0 and a.get("accomplished"):
            ok = fail("agent %s has never run but claims accomplishments" % who)

    for e in s.get("feed", []):
        if e.get("who") not in agents:
            ok = fail("feed event at %s is attributed to unknown agent %r"
                      % (e.get("t"), e.get("who")))
    for m in s.get("messages", []):
        if m.get("from") not in agents:
            ok = fail("message %r is from unknown agent %r" % (m.get("subject"), m.get("from")))
        if m.get("to") not in agents and m.get("to") != "all":
            ok = fail("message %r is to unknown agent %r" % (m.get("subject"), m.get("to")))

    sb = s.get("scoreboard", {})
    if sb.get("revenue", 0) != sb.get("profit", 0) + sb.get("expenses", 0):
        ok = fail("scoreboard does not balance: revenue != profit + expenses")
    if sb.get("revenue", 0) > 0 and not sb.get("revenue_ever"):
        ok = fail("revenue is above zero but revenue_ever is false")
    if sb.get("customers", 0) == 0 and sb.get("revenue", 0) > 0:
        ok = fail("revenue with no customers -- one of the two is wrong")
    claimed = sum(a.get("revenue_attributed") or 0 for a in s.get("agents", []))
    if claimed != sb.get("revenue", 0):
        ok = fail("agents claim $%s of revenue but the scoreboard says $%s"
                  % (claimed, sb.get("revenue", 0)))
    if sb.get("active_agents") != len(s.get("agents", [])):
        ok = fail("scoreboard says %s agents; %s are defined"
                  % (sb.get("active_agents"), len(s.get("agents", []))))
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="validate state.json and stop")
    args = ap.parse_args()

    with io.open(STATE, encoding="utf-8") as fh:
        s = json.load(fh)

    # The company runs seven days to the owner's one (chairman, 2026-09-26).
    # Stamped here so the public page and every reader agree; the office page
    # recomputes it live from the viewer's clock so it never goes stale.
    s["meta"]["clock"] = clock()
    s["meta"]["day"] = s["meta"]["clock"]["company_days"]

    if not validate(s):
        sys.exit("\nstate.json describes an organization that cannot exist. "
                 "Fix the state, not the page.")
    print("state.json is consistent: %d agents, %d gates, %d events, %d buried."
          % (len(s.get("agents", [])), len(s.get("gates", [])),
             len(s.get("feed", [])), len(s.get("graveyard", []))))

    stale = datetime.datetime.now(datetime.timezone.utc) - datetime.datetime.fromisoformat(
        s["meta"]["generated_at"].replace("Z", "+00:00"))
    if stale.total_seconds() > 36 * 3600:
        print("WARNING: meta.generated_at is %.0f hours old. The office will show a stale "
              "organization." % (stale.total_seconds() / 3600))

    if args.check:
        return

    with io.open(TEMPLATE, encoding="utf-8") as fh:
        tpl = fh.read()
    if MARKER not in tpl:
        sys.exit("FAIL: template has no %s marker" % MARKER)

    # </script> inside the JSON would close the host <script> tag early.
    blob = json.dumps(s, ensure_ascii=False).replace("</", "<\\/")
    with io.open(OUT, "w", encoding="utf-8") as fh:
        fh.write(tpl.replace(MARKER, blob))
    print("wrote %s (%.1f KB)" % (os.path.relpath(OUT, REPO), os.path.getsize(OUT) / 1024.0))
    print("Now publish it with the Artifact tool, capabilities {sample:{}, db:{}}.")


if __name__ == "__main__":
    main()
