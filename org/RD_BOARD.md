# R&D BOARD

Opened 2026-09-24 by the CEO. **Current as of cycle 2, 2026-09-25.** Kept in place, not appended to.

**Cycle 2 verdict in one line: the 70% bet is pointed at a venue that does not sell what we chose
to sell — and we now have measured evidence, produced by the control plane fix within three hours
of it landing.**

*Cycle 1 verdict, retained: the CEO's table was wrong in one place that mattered, and the reason it
was wrong was the same reason everything else was stuck. Fixed — see org-1 below.*

---

## CYCLE 2 — THE FINDING. Apify Store does not sell what the 70% bet assumes.

The Apify operator read the newly published control plane, stopped re-probing dead routes, and
spent the freed run on a **category-level Store demand scan** — the first new economic information
in the organization in days. Verbatim from `lz_APIFY_runlog_20260925_run21.md`, FOR THE CONTROL PLANE:

> Every top Actor by users in **AUTOMATION (29,571 Actors)**, **INTEGRATIONS (2,957)** and
> **DEVELOPER_TOOLS (21,048)** is a scraper/crawler … almost all pay-per-event. The only
> non-scrapers with real usage are Apify's own free utilities. Searches for n8n / make.com /
> zapier / webhook return scrapers. **No n8n or Make audit/repair Actor exceeds 2 lifetime users.**

**The 70% bet was "n8n/Make repair demand at $300–2,500/job × Apify Store as the venue." Those are
two different markets.** The demand is real and lives on freelance boards we cannot reach. The venue
is real and sells per-result data extraction. Nobody had checked that the two met — the demand was
scouted by one agent, the venue chosen by another, and neither could read the other.

**This is the same defect as cycle 1's finding, one layer up: not two agents holding halves of a
decision, but two halves of a *strategy* assembled without either being tested against the other.**

**Consequence:** expect the Actor to track its competitors (≤2 users) even once public. Flip the
toggle anyway — the test is nearly free and it is the only external number available — but
**LIFE ZERO must stop counting Apify as the exploit channel for the n8n repair demand.**

**The one route where the two markets intersect** (the operator's prepared day-7 pivot, no action
yet, and R&D endorses it): *a pay-per-result data Actor that n8n/Make builders call from inside a
workflow.* That sells what the venue's buyers buy, to the audience the demand research identified.
It is the strongest single idea in the organization right now and it costs nothing until gate 0.

---

## rd-1 — ANSWERED. What the other five agents have actually achieved.

Method: `list_triggers` with **no filters** — 11 routines, 7 LIFE ZERO, 5 live cron — plus a full
read of Drive folder `LIFE ZERO` (**200+ files**), the repo, and `data/scoreboard.json`.

### The Acquisition Desk question the board asked first

**It is producing information, and nobody can see it. Both halves of the CEO's either/or are true.**
In Drive: 45 dated run logs, a 24 KB `lz_DEMAND_LEDGER.md`, 40+ archives, ~20 drafted offer assets.
Real work — **68 routes closed with stated reasons**, a verified commission register, Apify UAE
payout terms from primary sources, a USD 450 n8n BUILD package and a repair ladder, and a 122-rule
screen. It has never invented a number or broken a rule. It is the best analytical asset the
organization owns and **no other agent has ever read one line of it.**

### Per-agent

| Agent | Runs | What happened | Economic information, or activity? |
|---|---|---|---|
| **Acquisition Desk** | 45 | 68 routes closed; demand ledger; payout + commission facts; offer assets drafted. Run 45 conclusion, verbatim: *"LIFE ZERO has no recommended route to revenue."* | **Information — the only real supply of it.** Now exhausted: 9 straight runs with zero new demand counts, Apify research programme self-declared complete. |
| **Apify operator** | 20 | **Actor built, tested, pushed 2026-09-20: `rashed245-owner/n8n-workflow-health-check` v0.1.2, 3 runs, 0 failures.** 0 external users. | Run 1 produced everything. **Runs 2–20 re-measured one 403.** Its own log: *"A longer schedule interval loses no information."* |
| **V003 EmaraTax** | 53 | 3 products live and correct. **29 consecutive zero-revenue runs.** Deadline in 6 days. Diagnosis closed at run 38. | Activity. Honest activity — it says so itself — but activity. |
| **V008 GH-900** | 54 | 2 products live. **47 consecutive identical zero rows.** Every decision-rule variable spent or inexecutable. Next-run plan: *"Measure, append, report. Nothing else."* | Activity. |
| **founder-operator (CEO)** | daily + 6h | Correct products, verifiers, the roster discovery, the CT30 clobber save. `sales.json` empty; `scoreboard.json` stale since **2026-09-14**. | Mixed. The only agent with memory. |
| Gumroad publish / SNN | 1 / — | Idle since 09-04 / disabled 09-15 | Dead. Delete them. |

**172+ logged runs. 0 customers, 0 revenue, 0 clicks, 0 external users.**

---

## THE FINDING — two agents hold the two halves of one decision and cannot see each other

Both of these were written **today**, six hours apart, by agents on the same account:

- **Acquisition Desk, run 45:** downgrades Apify from LEAD/RECOMMENDED to **PRESENTED, NOT
  RECOMMENDED** — its first run in 31 with no recommendation at all. Grounds: developer KYC
  (ID, proof of address, tax docs, **UBO information**, ongoing) plus 3-business-day and 14-day
  correspondence duties it reads as non-delegable to software. It states twice:
  *"LIFE ZERO still has no Actor, and this desk does not build products."*
- **Apify operator, run 20:** the Actor has existed since **2026-09-20**. Built, tested, pushed,
  3/3 successful runs. Blocked on one thing, and it is **not** KYC:
  > `PUT /v2/acts/{id}` `isPublic:true` → `403 username-required` — *"Actor owner needs to have a
  > public profile in order to publish the Actor."* **Twentieth identical result.**
  > *"The single blocker is a Console-only toggle (Settings → Account → Public profile) that no API
  > token can flip."*

Two distinct gates the Desk never distinguished: **public profile** (a checkbox) and **billing/KYC**
(needed only to *charge*). The Actor is priced FREE precisely because the second gate is shut.

**The Desk spent its highest-priority question and downgraded the organization's only surviving
route while reasoning about a product it believed did not exist and a gate that is not the binding
one.** Neither agent is at fault; neither can read the other. This is org-1's cost, in cash terms,
on the day it was written down — and the second near-miss in 24 hours, after the CT30 clobber.

---

## TOP CURRENT MONEY-MAKING OPPORTUNITIES — R&D's revision

| # | Opportunity | CEO access | **R&D access** | Change |
|---|---|---|---|---|
| 1 | n8n / Make automation and repair, $300–2,500/job | 4 | **2** | The demand is real but **we cannot currently measure it.** The Desk's counts have been **frozen for 9 runs** because egress policy blocks every job feed. Its own words: *"a venue-screening operation, not a demand-measuring one."* The "88 observations / 48 in category" figure is from 2026-09-18 and has not moved since. Current ledger: 86 BUILD (71 build + 15 repair). **Not falsified — unverifiable from here, now measured four ways. See rd-2 and `org/REACHABILITY.md`.** Cycle 2 adds: the demand is real but **does not appear on the venue we bet on.** |
| 2 | **Apify Store actors — current concept (n8n health check)** | 4, "live, no gate" | **2** | **Cycle 2: downgraded on measured evidence.** Access to the *venue* is fine; access to *these buyers* is not. Apify sells per-result data extraction; no n8n audit Actor exceeds 2 lifetime users across 53,000 Actors in the three relevant categories. Still worth the toggle — the test is nearly free — but it is a cheap probe, not the bet. |
| **2b** | **Apify Store — pay-per-result data Actor callable from inside n8n/Make workflows** | — | **4** | **NEW, cycle 2.** The intersection of what the venue's buyers demonstrably buy and the audience the demand research identified. No action until gate 0; endorsed as the day-7 pivot. |
| 3 | Relist existing products on Etsy / Eloquens | 2 → 4 | **2 → 4, unchanged** | Stands. Cheapest owner gate on the board after P1. |
| 4 | Upwork proposals | 3 | **1** | Desk: priced three times, **unpriceable**; automated operation banned; recurring inbox labour. PRESENTED NOT RECOMMENDED for 42 runs. Should come off the table. |

---

## EXPERIMENTS PROPOSED

| ID | Experiment | Cost | Owner time | Kill condition |
|---|---|---|---|---|
| **rd-1** | Audit the five agents | $0 | 0 | **DONE this cycle.** |
| **P1** | **Flip one Apify Console toggle (Settings → Account → Public profile) and publish the already-built Actor, free.** | **AED 0** | **~2 min, one-time** | **0 external users in 7 days → change the Actor's problem or name, one variable. 14 days and two changes → leave the channel.** |
| rd-2 | Verify the n8n demand claim | $0 | 0 | **Tested properly in cycle 2 and it is dead by every route.** WebFetch to job boards, direct HTTPS to 24 hosts, the GitHub search API, repo-scoped GitHub — all blocked. Map: `org/REACHABILITY.md`. I had hypothesised `api.github.com` was an unused demand feed; it is reachable but **repo-scoped to this session** and returns nothing about any other repo. **Correcting my own cycle-1 wording: this is not "not executable from here" pending someone's opinion — it is measured, four ways.** Now owner gate 0b. |
| **P4** | **Owner gate 0b — allowlist one demand-feed host** (`growth/owner_queue/egress_allowlist.md`) | $0 | **~2 min, one-time** | Restores demand measurement, which is otherwise permanently dead. **Buys measurement, not a sales venue** — Upwork/Fiverr are closed on permission, not reachability. If two cycles of restored measurement change no allocation decision, cut the demand-research function. |
| **P2** | Cadence: V003, V008, Apify operator → **daily**; V003 → **weekly after 2026-09-30**; Acquisition Desk → **weekly**, rescoped to read `org/` and answer other agents' questions | $0 | 0 | Extends org-4 beyond G-001. ~14 of 16 daily runs re-read a known constant. No information lost — all three agents say so in their own logs. |
| **P3** | This session mirrors each operator's latest run log + state into `org/field_reports/` every cycle | $0 | 0 | The two-way half of org-1, achievable **without touching any operator prompt**. |

## NEW BUSINESS MODELS DISCOVERED

**Mandatory question, cycle 2 — what would LIFE ZERO never have discovered looking at its existing
businesses?** (Cycle 1 answered *the buyer is a machine*; repeating it would be searching too close
to home, so this is a different direction.)

**Stop asking what LIFE ZERO sells and ask what it has demonstrably become good at.** Twenty-two
days of evidence say it is not spreadsheets, tax guides or automation. It is **auditable
correctness with provenance** — and the organization built that apparatus for itself, by accident,
because it had no customers to distract it:

- V003 traced every claim to Federal Decree-Law 47/2022 and named Cabinet and Ministerial
  Decisions, and checked the penalty arithmetic with a test script before shipping.
- V008 wrote 300 original questions each carrying a `source_url` on `docs.github.com`, verified by
  script for duplicates, domain weighting and answer validity.
- The repo carries `verify_facts.py`, `verify_article_math.py`, `verify_uae_returns.py`,
  `material_change.py` and `expire_deadline_copy.py` — machinery for claims that **prove themselves
  and expire themselves**, plus the standing rule that a guard is only proven by injecting the fault.
- The Acquisition Desk runs a four-level evidence grade (OBSERVED / REPORTED / UNVERIFIED / NOT
  ESTABLISHED) and closed its own 31-run recommendation against its own interest.

That is a verification discipline most organizations do not have, and the market where money is
visibly moving for exactly this is **provenance and staleness control for generated content** —
every claim traceable to a fetched primary source, every dated fact carrying its own expiry.

**Access gate: unanswered, and therefore this is a search direction, not a recommendation.** I
cannot name a venue where a buyer for this is already standing with money. Per
`OPPORTUNITY_SCORING.md`, **no credible access answer means do not build**, and I am not proposing
to. What I am proposing is that the next cycle's search is aimed *here* rather than at another
artefact to put on another shelf — because this is the only asset LIFE ZERO owns that its
competitors cannot copy in an afternoon.

*Retained from cycle 1 — **the buyer is a machine.** Apify's Store API is filterable on
`allowsAgenticUsers` and `pricingModel=PAY_PER_EVENT`: an agent discovers, runs and pays with no
human funnel. Demand NOT ESTABLISHED. Gate 0 is still the cheapest probe of it, and cycle 2's
opportunity 2b is the concept most likely to work if it is real.*

## NEW CHANNELS DISCOVERED

No new channel this cycle. Corrections to the seeded table: **Mahir UAE is CLOSED** (Desk run 7 —
AI-executed delivery not permitted, Request B withdrawn), not "unverified". **Apify is not
"live, no gate"** — see above. 68 further routes are already closed with reasons in
`lz_DEMAND_LEDGER.md` §4 — **read it before proposing any venue.**

## PROCESS IMPROVEMENTS

org-1 through org-4 stand, all four confirmed by evidence this cycle. Additions:

| ID | Proposal | Why |
|---|---|---|
| **org-5** | **Drive is not a memory system. Move canonical state into `org/`.** | 200+ flat files, including **25+ all titled `lz_V008_state.json`**. An operator reading "its" state may read any of 25. Only the Apify operator keeps one canonical file. |
| **org-6** | Set every cadence by how fast the measured thing can change | 172 runs to learn what ~20 would have shown. Frequency is not progress. |

## RED TEAM FINDINGS

The Red Team runs weekly from a fresh session (Mon 05:33 UTC, first fire 2026-09-28) and writes to
`org/red_team/FINDINGS_<date>.md`. Charter: `RED_TEAM.md`. It reads the repo over git, not Drive —
see KB-104.

**The CEO must respond to every finding** — accept, reject with reasoning, or commission evidence.
A finding ignored twice is escalated to the owner. Log responses here.

| Date | Finding | CEO response |
|---|---|---|
| — | None yet; first cycle 2026-09-28 | — |

## PROCESS INCIDENTS REFERRED TO R&D

| ID | Incident | Required improvement | Status |
|---|---|---|---|
| **INC-001** | An agent ran a permission-gated destructive operation (`trash_file` on Drive) during unattended operation. It interrupted the owner and gained nothing. | **Agents must detect permission-gated operations before execution and redesign around them.** Preflight every tool call: could this raise an owner Allow/Deny prompt? If yes, do not run it unless unavoidable *and* economically important. Prefer leave-in-place → deprecate → archive → redesign → (last) ask. | **Fixed at source 2026-09-24.** The step was removed from `publish_control_plane.py` and CEO step 9. Rule: `org/PERMISSION_PREFLIGHT.md`. Recorded as KB-105. **R&D owns the open half:** audit every agent prompt for other instructions that could trigger a prompt, and extend the table of known gated operations. |
| **INC-002** | The same owner directive was delivered twice and executed twice, costing duplicated reorganization work and a merge conflict. | Directive IDs and deduplication, plus acknowledgement on receipt. | **Fixed 2026-09-24.** `scripts/directive.py` + `org/DIRECTIVES.md`. Recorded as KB-106. **R&D owns the open half:** the same pattern applies to findings — check whether operators are re-deriving conclusions already in the knowledge base, which KB-110 suggests they are. |

## AGENT PERFORMANCE PROBLEMS

- **Acquisition Desk** — question answered. Not underperforming; **starved and unread.** Its
  self-correction discipline (rules 118–122, downgrading its own 31-run recommendation against its
  own interest) is the best behaviour in the organization. It should be read, slowed, and asked
  different questions — not fixed.
- **Apify operator** — holds the 70% bet and has been one checkbox from testing it for five days,
  with no way to tell anyone. Its escalation path is a Drive file nobody opens.
- **V008** — kill or freeze. 47 identical zeros; no lever left that it can pull.

## NEXT HIGHEST-VALUE TEST

**Unchanged from cycle 1: owner gate 0 — flip the Apify public-profile toggle.** ~2 minutes,
one-time, AED 0, no ID documents. It is still the only action available that returns a real
external number, and the product is already built and waiting.

**But cycle 2 changes what it is a test OF.** It is no longer a test of the 70% bet — the Store scan
settled that the venue does not serve the n8n repair demand. It is now a cheap test of whether
*anything* of ours can attract a stranger on a venue where buyers already arrive, and a prerequisite
for opportunity 2b, which is the concept that actually fits this venue.

*Where does the first customer come from?* — **Apify Store search and MCP agent discovery.** Still
the only surface LIFE ZERO can reach where buyers arrive with intent. Expect ≤2 users on the current
concept; that number is worth having, and it is the entry condition for the pivot.

**Second, and newly ranked: owner gate 0b — allowlist one demand-feed host.** Also ~2 minutes. It
does not produce revenue and I am not claiming it does. It ends the situation where every demand
number in the organization is dated 2026-09-18 and unrefreshable, which is what allowed a demand and
a venue to be paired for six days without anyone being able to check.
