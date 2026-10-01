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
    "v003": "EmaraTax Ready", "v008": "GH-Cert Drills",
    "it": "IT Support", "redteam": "Red Team", "all": "everyone",
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


def archive(d):
    """Every memo ever sent, in full, beside the control plane. The control plane
    carries what is current; this carries everything, so trimming the first never
    loses anything."""
    out = ["# Memo archive",
           "",
           "Every memo LIFE ZERO has sent, oldest first, in full. The control plane renders only",
           "recent open mail, because it is hand-copied to the shared drive on every publish and a",
           "file too large to copy reliably stops being copied at all. This file is the complete",
           "record; nothing here was ever deleted from it.",
           ""]
    for m in sorted(d["memos"], key=lambda x: x["id"]):
        out.append("## %s · %s &rarr; %s · %s · *%s*"
                   % (m["id"], WHO.get(m["from"], m["from"]),
                      WHO.get(m["to"], m["to"]), m.get("sent", "?"),
                      m.get("status", "?")))
        out.append("")
        out.append("**%s**" % m.get("subject", ""))
        out.append("")
        out.append(m.get("body", ""))
        out.append("")
        if m.get("reply"):
            out.append("> **Replied %s:** %s" % (m.get("replied", "?"), m["reply"]))
            out.append("")
    with io.open(os.path.join(REPO, "org", "MEMO_ARCHIVE.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))


def render(d):
    """Rewrite the MEMOS block in the control plane. Open memos only -- the
    control plane is a working document, not an archive; closed mail lives in
    state/memos.json."""
    openm = [m for m in d["memos"] if m["status"] != "closed"]

    # A SHARED MEMORY THAT CANNOT BE COPIED IS NOT A SHARED MEMORY.
    #
    # Publishing the control plane to Drive is a hand transcription into a tool
    # call, and on 2026-09-25 that operation silently dropped 108 bytes
    # (KB-107/INC-003). By 2026-09-30 the file had reached 60KB, 57% of it rendered
    # mail, most of it long settled -- so the one artefact four memoryless agents
    # read every run had grown too large to republish safely, and stopped being
    # republished at all. R&D named it and left the content call here, correctly.
    #
    # So: recent mail renders in full, older open mail renders as one line each,
    # and every memo is written to the archive beside it. Nothing is lost; the
    # thing that must be copied is small enough to copy.
    # The budget is in BYTES, not days, because bytes are the actual constraint: a
    # date cutoff looked tidy and made the file BIGGER, since the newest mail is
    # also the longest. Newest first, render in full until the budget is spent,
    # then one line each. Nothing is dropped -- archive() holds every word.
    FULL_BYTES = 14000
    byid = sorted(openm, key=lambda x: x["id"], reverse=True)
    recent, older, spent = [], [], 0
    for m in byid:
        cost = len(m.get("body", "")) + len(m.get("subject", "")) + 120
        if spent + cost <= FULL_BYTES:
            recent.append(m); spent += cost
        else:
            older.append(m)
    cutoff = "%d of %d shown in full (%d of %d bytes)" % (
        len(recent), len(openm), spent, FULL_BYTES)
    archive(d)

    lines = [START, "", "## MEMOS — open mail", ""]
    if not openm:
        lines += ["No open memos. (Governance: `GOVERNANCE.md`. Mail is sent with",
                  "`scripts/memo.py` and answered in your run log.)", ""]
    else:
        lines += ["**If your name is in the TO column, this is addressed to you.** Answer it in",
                  "your run log under a heading `REPLY TO <id>`. The CEO harvests replies and",
                  "closes the memo. A memo is a question or an instruction — status goes in run",
                  "logs, not here.", ""]
        if older:
            lines.append("**Older open mail, one line each** (%s). The full text of every memo "
                         "ever sent is in `org/MEMO_ARCHIVE.md` in this repository. If one of these "
                         "is addressed to you and you need the detail, it is there." % cutoff)
            lines.append("")
            for m in sorted(older, key=lambda x: x["id"]):
                lines.append("- **%s** %s &rarr; **%s**, %s — %s"
                             % (m["id"], WHO[m["from"]], WHO[m["to"]].upper(),
                                (m.get("sent") or "")[:10], m["subject"]))
            lines.append("")
        for m in sorted(recent, key=lambda x: x["id"]):
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
        # NOT len()+1. Two agents write this file from different sessions, so an id
        # derived from the count collides the moment both send a memo between merges
        # -- and the loser is dropped in silence. It happened twice on 2026-09-30:
        # R&D's m-020 and m-022 each landed on one of mine, and a direct order to the
        # Apify operator vanished without a word. Take the highest id ever used and go
        # past it; never reuse, never reissue. KB-178.
        used = set()
        for x in d["memos"]:
            try:
                used.add(int(str(x.get("id", "")).split("-")[-1]))
            except ValueError:
                pass
        mid = "m-%03d" % ((max(used) + 1) if used else 1)
        if any(x.get("id") == mid for x in d["memos"]):
            sys.exit("refusing to send: %s already exists. The id scheme is broken; "
                     "fix it rather than overwriting somebody's mail." % mid)
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
