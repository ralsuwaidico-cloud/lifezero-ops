#!/usr/bin/env python3
"""Inter-agent mail for LIFE ZERO.

Four agents run from fresh sessions and cannot read this repo, so the control
plane carries the mail. A memo is addressed to a function by name, renders into
CONTROL_PLANE.md, and the recipient answers in its run log. The CEO moves the
mail; it does not answer on anyone's behalf.

    memo.py send --from rnd --to apify --subject "..." --body "..."
    memo.py inbox apify
    memo.py answer m-004 --body "..."
    memo.py close m-004
    memo.py list [--all]
    memo.py render          # rewrite the MEMOS block in CONTROL_PLANE.md
"""

import argparse
import datetime
import io
import json
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORE = os.path.join(REPO, "state", "memos.json")
PLANE = os.path.join(REPO, "org", "CONTROL_PLANE.md")
START, END = "<!--MEMOS:START-->", "<!--MEMOS:END-->"

WHO = {
    "chairman": "Chairman (owner)", "ceo": "CEO", "rnd": "R&D",
    "apify": "Apify operator", "acq": "Acquisition Desk",
    "v003": "V003", "v008": "V008", "redteam": "Red Team", "all": "everyone",
}


def load():
    try:
        with io.open(STORE, encoding="utf-8") as fh:
            return json.load(fh)
    except (IOError, OSError, ValueError):
        return {"memos": []}


def save(d):
    os.makedirs(os.path.dirname(STORE), exist_ok=True)
    with io.open(STORE, "w", encoding="utf-8") as fh:
        json.dump(d, fh, indent=2, ensure_ascii=False)
        fh.write("\n")


def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def check(who, field):
    if who not in WHO:
        sys.exit("unknown %s %r. known: %s" % (field, who, ", ".join(sorted(WHO))))


def render(d):
    """Rewrite the MEMOS block in the control plane. Open memos only -- the
    control plane is a working document, not an archive; closed mail lives in
    state/memos.json."""
    openm = [m for m in d["memos"] if m["status"] != "closed"]
    lines = [START, "", "## MEMOS — open mail", ""]
    if not openm:
        lines += ["No open memos. (Governance: `GOVERNANCE.md`. Mail is sent with",
                  "`scripts/memo.py` and answered in your run log.)", ""]
    else:
        lines += ["**If your name is in the TO column, this is addressed to you.** Answer it in",
                  "your run log under a heading `REPLY TO <id>`. The CEO harvests replies and",
                  "closes the memo. A memo is a question or an instruction — status goes in run",
                  "logs, not here.", ""]
        for m in sorted(openm, key=lambda x: x["id"]):
            lines.append("### %s &nbsp;&nbsp; %s &rarr; **%s** &nbsp;&nbsp; *%s*"
                         % (m["id"], WHO[m["from"]], WHO[m["to"]].upper(), m["sent"]))
            lines.append("")
            lines.append("**%s**" % m["subject"])
            lines.append("")
            lines.append(m["body"])
            lines.append("")
            if m.get("reply"):
                lines.append("> **%s replied %s:** %s"
                             % (WHO[m["to"]], m.get("replied", "?"), m["reply"]))
                lines.append("")
    lines.append(END)
    block = "\n".join(lines)

    with io.open(PLANE, encoding="utf-8") as fh:
        s = fh.read()
    if START in s and END in s:
        s = s[:s.index(START)] + block + s[s.index(END) + len(END):]
    else:  # first time: put it directly above SCHEDULED ACTIONS
        anchor = "## SCHEDULED ACTIONS"
        if anchor not in s:
            sys.exit("cannot place MEMOS block: no SCHEDULED ACTIONS heading")
        s = s.replace(anchor, block + "\n\n" + anchor, 1)
    with io.open(PLANE, "w", encoding="utf-8") as fh:
        fh.write(s)
    return len(openm)


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("send")
    p.add_argument("--from", dest="frm", required=True)
    p.add_argument("--to", required=True)
    p.add_argument("--subject", required=True)
    p.add_argument("--body", required=True)

    p = sub.add_parser("answer")
    p.add_argument("id")
    p.add_argument("--body", required=True)

    p = sub.add_parser("close"); p.add_argument("id")
    p = sub.add_parser("inbox"); p.add_argument("who")
    p = sub.add_parser("list"); p.add_argument("--all", action="store_true")
    sub.add_parser("render")

    a = ap.parse_args()
    d = load()

    if a.cmd == "send":
        check(a.frm, "sender"); check(a.to, "recipient")
        if a.frm == a.to:
            sys.exit("a memo to yourself is a note, not a memo")
        if a.to == "chairman" and a.frm not in ("ceo", "redteam"):
            sys.exit("only the CEO addresses the chairman. The Red Team may, but only when a "
                     "finding has been ignored twice. Everyone else writes a CEO REQUEST.")
        mid = "m-%03d" % (len(d["memos"]) + 1)
        d["memos"].append({"id": mid, "from": a.frm, "to": a.to, "subject": a.subject,
                           "body": a.body, "sent": now(), "status": "open"})
        save(d); n = render(d)
        print("sent %s: %s -> %s. %d open." % (mid, WHO[a.frm], WHO[a.to], n))

    elif a.cmd == "answer":
        m = [x for x in d["memos"] if x["id"] == a.id]
        if not m:
            sys.exit("no memo %s" % a.id)
        m[0]["reply"] = a.body; m[0]["replied"] = now(); m[0]["status"] = "answered"
        save(d); render(d)
        print("%s answered by %s" % (a.id, WHO[m[0]["to"]]))

    elif a.cmd == "close":
        m = [x for x in d["memos"] if x["id"] == a.id]
        if not m:
            sys.exit("no memo %s" % a.id)
        if not m[0].get("reply"):
            print("WARNING: closing %s with no reply on record." % a.id)
        m[0]["status"] = "closed"; save(d); n = render(d)
        print("closed %s. %d open." % (a.id, n))

    elif a.cmd == "inbox":
        check(a.who, "agent")
        mine = [x for x in d["memos"]
                if x["status"] != "closed" and x["to"] in (a.who, "all")]
        if not mine:
            print("%s: no open memos." % WHO[a.who]); return
        for m in mine:
            print("%s  from %s  [%s]\n  %s\n  %s\n"
                  % (m["id"], WHO[m["from"]], m["status"], m["subject"], m["body"][:160]))

    elif a.cmd == "list":
        for m in d["memos"]:
            if a.all or m["status"] != "closed":
                print("%s  %-10s -> %-10s  %-9s  %s"
                      % (m["id"], m["from"], m["to"], m["status"], m["subject"][:60]))

    elif a.cmd == "render":
        print("%d open memos rendered into the control plane." % render(d))


if __name__ == "__main__":
    main()
