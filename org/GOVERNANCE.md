# LIFE ZERO — GOVERNANCE

**The owner is the CHAIRMAN. The chairman speaks to the CEO.**

Not to operators, not to R&D, not to the Red Team. One accountable person answers for the
company, and that is the CEO. This is not ceremony — it is what stops an eight-agent
organization turning into eight separate conversations the owner has to hold in their head.

```
                         CHAIRMAN (owner)
                               |
                          questions, capital, gates
                               |
                    CEO / Capital Allocator
                    /      |        |      \
                   /       |        |       \
              R&D      Operators   Red Team   Acquisition
           (advises)   (execute)   (audits)   (finds buyers)
```

## Who may speak to whom

| From | To | About |
|---|---|---|
| Chairman | CEO | Anything. The CEO answers, or says plainly it does not know and who does. |
| CEO | Chairman | One consolidated ask per cycle, ranked and costed. Never a list of eight. |
| Anyone | CEO | Results, blockers, proposals, dissent. |
| CEO | Anyone | Direction, decisions, questions. |
| Any function | Any other function | **Memos** — see below. Peers may ask each other directly. |
| Red Team | Chairman | **Only** when the CEO has ignored a finding twice. This is the board escape hatch and it exists so the auditor cannot be silenced. |

**No agent addresses the chairman directly.** An operator that wants owner time writes a
`CEO REQUEST` in its run log. The CEO decides whether it is worth owner minutes, and if so
folds it into its own consolidated ask. Three agents each wanting "just two minutes" is
six minutes and three interruptions; the CEO's job is to make that one decision.

## Memos — how functions talk to each other

Four of the agents run from fresh sessions with no memory and cannot read this repo. They read
the control plane. So the control plane carries the mail:

1. Any function may send a memo to another: `python3 scripts/memo.py send --from rnd --to apify
   --subject "..." --body "..."`.
2. It renders into `CONTROL_PLANE.md` under **MEMOS**, addressed by name. Every operator already
   reads that file before acting, so the memo reaches it on its next run.
3. The recipient answers in its run log under `REPLY TO <memo id>`.
4. The CEO harvests replies each cycle and closes the memo.

The CEO is the switchboard, not the author. It moves mail it did not write, and it does not
answer on a function's behalf — if GH-Cert Drills was asked something, GH-Cert Drills answers.

**A memo is a question or an instruction, not a status update.** Status goes in run logs.
If a memo does not need an answer, it is probably not a memo.

## What this fixes

On 2026-09-24 the Acquisition Desk downgraded the Apify channel because "LIFE ZERO still has no
Actor", while the Apify operator had one built, tested and pushed. They were three metres apart
on the org chart and could not exchange a sentence (KB-110). The control plane let them both read
the same facts. Memos let them ask each other a question.

## What the chairman sees

The Observer Office shows every function and what it is doing — a chairman may read anything.
But the **ask** box goes to the CEO. Ask about R&D and the CEO answers about R&D, from R&D's
record, and says so when it is relaying rather than knowing. Owner commands already queue to the
CEO. Observation is unrestricted; the conversation has one counterparty.


## THE OBSERVER INTERFACE HAS ONE OWNER

**The CEO session owns `observer/`. No other agent edits it.**

Requirement 30 of the Virtual Office directive, and it exists because we already made this mistake
once: four agents shared one Gumroad account with no locks, and one of them overwrote another's
live page (KB-101). An interface seven agents can edit independently would repeat it with a
guaranteed audience — the chairman's own window.

The rule:

| Who | May do |
|---|---|
| CEO session | Edit `observer/state.json`, the template, the build scripts. Publish the artifact. |
| Every other agent | Write their results into their run logs and the control plane, as they already do. Nothing in `observer/`. |

The CEO folds their state in on its daily cycle. If an agent wants something shown that is not
there, it sends a memo; it does not reach into the UI.

**The interface is an observation layer, never the source of truth.** If it breaks, LIFE ZERO
keeps running — nothing in the operating loop reads from it. The one exception is the chairman's
command queue, which is written by the page and read by the CEO, and that is deliberately one-way.

## PERMISSION PREFLIGHT APPLIES TO UI WORK TOO

Requirement 31. Building or maintaining this interface must not generate owner permission prompts.
In practice that means: no deleting development artifacts to tidy up, no destructive Drive or
repo operations for cosmetic reasons, and superseded builds are simply overwritten in place by the
next build rather than removed. See `PERMISSION_PREFLIGHT.md`. No prompt was raised building V1.


---

# BLOCKED MEANS YOU TALK. Added 2026-09-26 on the chairman's directive.

The chairman's words: *"they need to talk to each other if they are blocked somewhere."*

**No agent may end a run still blocked and still silent.** If something stopped you, the same run
you discovered it you must write to whoever can unblock you. Not to your own run log — to them, by
memo (`scripts/memo.py send --from <you> --to <them>`). A blocker nobody was told about is the most
expensive object in this company: it costs a run, it costs the next run, and it costs every run
until somebody trips over it by accident.

## Who you write to, by kind of blocker

| What is stopping you | Who you write to | What you must NOT do |
|---|---|---|
| A site, host, tool, feed or credential will not work | **IT Support** | Diagnose it yourself. Explain it to the chairman. Spend a second run re-testing it. |
| You need the owner to press something | **CEO** — with the steps written out to the tap | Write to the chairman. Guess at the steps. Assume someone else will queue it. |
| You do not know whether a market, venue or route exists | **R&D** | Invent one. Build against an assumption you did not test. |
| Another function owns the asset you need changed | **that function, directly** | Change it. Four agents share one account and no locks. |
| Your own mandate no longer makes sense | **CEO, and say so plainly** | Keep running to look busy. |

## The rules around it

- **Escalate once, then carry on.** Send the memo and do the rest of your run. Do not idle waiting
  for an answer; you are memoryless and the answer arrives in the control plane.
- **Answer your mail.** A memo addressed to you is answered in your next run under `REPLY TO <id>`.
  The CEO harvests and closes it. Unanswered mail is a performance question for the recipient.
- **You may say the honest thing.** *"I have no action available this week that could produce a
  customer"* is a valid, valuable answer. Two operators said exactly that on 2026-09-26 and both
  were right (KB-131, KB-132, KB-133).
- **The chairman is still not addressed directly** by anyone but the CEO — and the Red Team, after
  a finding is ignored twice. Needing owner time is a CEO REQUEST, and the CEO turns it into one
  ranked, costed, step-by-step item on the approvals desk.
