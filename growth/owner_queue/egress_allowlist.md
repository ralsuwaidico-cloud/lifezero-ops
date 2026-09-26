# OWNER GATE 0d — WITHDRAWN by R&D after testing. No owner action needed.

**No owner action requested.** Rewritten by R&D 2026-09-26. I proposed six hosts, then tested the
one that was already open and found all six measure a population we cannot serve. **Withdrawn before
it cost a minute.** Kept here because the reasoning is the point.

## What went wrong with gate 0b, and the rule that follows

Gate 0b was granted. **I had ranked `www.upwork.com` first, and it was the wrong host.** Upwork
answered with a 403 challenge page to both the job search and the RSS feed. Reachability is not
readability, and Upwork's terms bar automated collection anyway — which **this organization's own
route register already recorded** (K-006). The answer was in our knowledge base and I did not check
it before spending an owner minute. That is my error, not the owner's and not the CEO's.

**Standing rule, now also in `OPPORTUNITY_SCORING.md`:** before asking for a host, state whether
that source **publishes for machines or defends against them**, and cite where you checked. An
allowlist entry for a bot-walled site spends owner minutes and buys nothing.

## STOP — I tested it, and my own six are the wrong population

`remoteok.com` was **already allowlisted** when I checked, so I did not have to predict. I fetched
`https://remoteok.com/api` directly: **HTTP 200, 607 KB of clean JSON, 99 live postings dated
2026-08-01 to 2026-09-24, no authentication.** The machine-facing screen works — that part of the
method is sound, and RemoteOK is exactly the kind of source it was meant to find.

**Then I measured, and the result disqualifies my own proposal.**

| Term | Postings mentioning it (of 99) |
|---|---|
| excel | 40 (40.4%) |
| api | 31 (31.3%) |
| workflow | 25 (25.3%) |
| automation | 12 (12.1%) |
| integration | 12 (12.1%) |
| **n8n** | **1 (1.0%)** |
| make.com / zapier | 1 each |

**RemoteOK is a remote *employment* board. So are all six hosts I listed.** They advertise salaried
roles, not the $300–2,500 fixed-scope projects the demand research counted. The Acquisition Desk's
own register puts employment in a category it marks **"out of mandate as work"** (19 observations).

So the honest position: **the n8n 1/99 figure is not a refutation of the Desk's 86 BUILD
observations — it is a different population, and a weak background control at best.** And asking the
owner to allowlist five more boards of the same kind would buy five more measurements of a market we
have already decided we cannot serve.

**Withdrawn:** `remotive.com`, `himalayas.app`, `remotejobs.org`, `arbeitnow.com`, `jobicy.com`.
Do not queue them. Keep `remoteok.com`, which is already granted and free to keep reading.

## What would actually measure project demand — and what must be checked first

The population we need is **fixed-scope freelance projects**, not roles. Upwork and Fiverr are that
population and both are bot-walled. The remaining candidate worth screening is **`freelancer.com`,
which publishes a documented public API** — grade **REPORTED**, not verified, and it must clear the
same two questions before it costs an owner minute:

1. Does the API serve **project listings** without authentication, or only to registered developers?
2. Do their terms permit reading it for analysis?

**I am not queueing it yet.** I have now been wrong twice about this gate — first ranking Upwork,
then proposing six sources of the wrong population — and the correct response is to check before
asking, not to ask faster.

## Standing rules this gate produced

1. **State whether a source publishes for machines or defends against them**, and cite where you
   checked. (Gate 0b, spent on a bot-walled host that our own K-006 already described.)
2. **State which *population* the source measures, and confirm it is one we can serve.** A perfectly
   machine-readable feed of the wrong market is a measurement we cannot act on.

Both now belong in `OPPORTUNITY_SCORING.md` alongside the ranking screen.

## Kill condition

Unchanged from gate 0b, and it should be honoured: if two cycles of restored measurement change no
allocation decision, **cut the demand-research function** rather than keep it running.
