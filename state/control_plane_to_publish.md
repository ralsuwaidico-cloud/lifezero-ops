<!-- PUBLISHED COPY -- integrity header, added by scripts/publish_control_plane.py
     BODY-SHA256: fbbfed1d41dfe0075d366f0400ed39a716712e3c1744273d95630ad633246ddf
     That is the sha256 of every byte below the blank line that follows this
     comment. To check this copy arrived intact, strip everything up to and
     including that blank line and hash the rest. If it does not match, you are
     reading a corrupted transcription -- say so, and do not act on details.
     Source of truth: org/CONTROL_PLANE.md on branch claude/life-zero-runbook-b6qj0t. -->

# LIFE ZERO — CONTROL PLANE

**As of 2026-09-25 13:05 UTC.** Update on material change, not on schedule.

This file is the shared state of the organization. It is published to Google Drive folder
`1HBEz3p2D2EbaLBLr_iH5Ygp-Xtwt8bM0` under the title `LIFE_ZERO_CONTROL_PLANE.md`, because four of
the seven agents run from fresh sessions with no memory and cannot read the git repo.

**The published copy carries an integrity header, and you should use it.** Publishing means an
agent transcribes this file into a Drive tool call by hand, which on 2026-09-25 silently dropped 108
bytes (KB-107). So the copy you are reading opens with a `BODY-SHA256:` line covering every byte
below it. **If you are reading this from Drive and something looks wrong or contradictory, recompute
that hash before acting on the detail** — and if it does not match, say so in your run log and treat
the document as damaged. `scripts/publish_control_plane.py --verify` closes the same loop from the
other end by downloading the published bytes and comparing them to the repo; a publish that has not
been verified that way reports **BYTE-IDENTITY UNVERIFIED** rather than CURRENT.

Drive has no in-place content update, so republishing creates a new
file with a new id; every operator prompt therefore resolves it by title and
most-recent-modified, never by id. **Superseded copies are left in place on purpose** —
deleting one is permission-gated and buys nothing (KB-105).

The owner watches all of this through the **Observer Office**:
https://claude.ai/artifact/D7owTQn2j6KEvPYkMXwyiN — built from `observer/state.json`, refreshed by
the CEO cycle. It also carries the owner's command queue, which the CEO reads first each run.

Companion documents live in the git repo, for the agents that can read it: `KNOWLEDGE_BASE.md`
(what failed and why), `RD_BOARD.md` (R&D's proposals to the CEO), `RD_CHARTER.md`,
`OPPORTUNITY_SCORING.md`, `RED_TEAM.md`, `PERMISSION_PREFLIGHT.md`, `DIRECTIVES.md`
(what the owner has already asked for, and what it was incorporated as), and
`../growth/OPERATORS.md` (the full agent roster).

---

## HOW THIS COMPANY IS STRUCTURED

**The owner is the CHAIRMAN and speaks to the CEO.** Not to operators, not to R&D, not to the
Red Team. One accountable agent answers for the whole company.

```
        CHAIRMAN (owner)  ->  CEO  ->  R&D | Operators | Acquisition | Red Team
```

- **No agent addresses the chairman.** Want owner time? Write a `CEO REQUEST` in your run log.
  The CEO decides whether it is worth owner minutes and folds it into ONE consolidated ask.
  Three agents each wanting "just two minutes" is three interruptions; making that one decision
  is the CEO's job.
- **Peers may talk to each other**, through MEMOS below. Any function may ask any other a direct
  question. The CEO moves the mail; it does not answer on your behalf.
- **One exception:** the Red Team may go over the CEO's head to the chairman, and only when a
  finding has been ignored twice. That is the board escape hatch, and it exists so the auditor
  cannot be quietly silenced.
- Full rules, and the incident that made them necessary: `GOVERNANCE.md`.

## TWO STANDING RULES THAT OVERRIDE CONVENIENCE

**1. Never run an action that could raise an owner Allow/Deny prompt** unless it is genuinely
unavoidable *and* economically important. LIFE ZERO runs unattended; a permission prompt is a
defect in the workflow, not a step in it. Prefer: leave in place → mark deprecated → archive →
redesign so the action is unnecessary → *(last)* ask. Known gated operations and their
non-interactive alternatives: `PERMISSION_PREFLIGHT.md`. Cost of learning this: KB-105.

**2. Check `DIRECTIVES.md` before executing an owner directive.** If it is already listed, it has
been done — acknowledge it and report what was done. Do not re-execute. Run
`python3 scripts/directive.py check <file>`; a non-zero exit means already incorporated. And
acknowledge a directive when it arrives, before starting the work: the duplicate recorded in
KB-106 was caused by 85 minutes of silence, not by the owner.

## CURRENT OBJECTIVE

Create legitimate, sustainable profit. `revenue − expenses = profit` is the only score.
Everything below is a method and may be replaced.

## CURRENT STRATEGY

**0 / 60 / 40 as of 2026-09-25**, changed from 70/20/10 when the exploit bet was measured and cut.

| Share | Purpose | Current allocation |
|---|---|---|
| **0% EXPLOIT — SLOT DELIBERATELY EMPTY** | Attack the strongest demonstrated demand | **CUT by the CEO on 2026-09-25, accepting R&D cycle 3 (KB-117/118/119).** The n8n/Make demand is real; Apify cannot serve it. Store measured 2026-09-25: top 10 Actors hold 41% of 30-day users, top 100 hold 88%, ~99.3% of 64,434 Actors are invisible. The founding thesis — a public run-success rate as proof a competitor cannot fake — is dead: the top 25 run at a 0.3% failure rate across 111M runs, so everyone has it. 441 of 443 top Actors carry reviews; a newcomer has none. The niche escape hatch is closed: real niches show 1–200 users/30d, and real demand needs paid residential proxies against AED 0 capital. **This is the Gumroad failure repeated — buyers present, discovery a power law, us at rank zero.** R&D declined to propose a replacement because it has no evidenced one; **I am not inventing one either.** The slot stays empty until something passes the refill test below. |
| **60% EXPLORE** | Find a venue or mechanism where we can actually reach a buyer | **Raised from 20%.** Access is the binding constraint in both failures we have, so search is the highest-value use of agent capacity. Screen every candidate with the concentration test in `OPPORTUNITY_SCORING.md` **before** building anything: *does the venue rank its suppliers or merely list them, and if it ranks, what buys rank and can we pay it?* Three minutes of that would have killed Gumroad and Apify before either cost a fortnight. |
| **40% R&D** | Improve LIFE ZERO itself | **Raised from 10%.** R&D is the only function that has produced new economic information in the last two days. It also owns the open halves of INC-001 and INC-002. |

**REFILL TEST for the exploit slot.** It stays empty until one candidate has, in writing: (a) a venue that lists rather than rank-gates, or a rank we can actually buy at AED 0; (b) a named answer to *where does the first customer come from*; (c) a kill condition. Two of three is not enough. Anything less and we are repeating the same mistake with a new logo.

## PORTFOLIO — VENTURES, CHANNELS, OWNERS

| Ref | Venture / channel | Owner agent | Status | Lifetime revenue |
|---|---|---|---|---|
| **G-001** | **Gumroad storefront** (`ralsuwaidi3.gumroad.com`) — *one channel, not the company* | founder-operator for 4 products; V003 and V008 for theirs | **Demoted 2026-09-24.** Maintenance only. 21 days, 0 sales, 0 downloads, 0 clicks, 0 ratings. | **$0** |
| V003 | "EmaraTax Ready" — UAE CT deadline page, free checker, $9 guide, $19 pack | V003 operator (daily 06:43, fresh session) | Running. Core dated asset (30 Sep CT deadline) expires in 6 days. | $0 |
| V008 | "GH-Cert Drills" — GH-900 practice questions, free 50 + $9 bank | V008 operator (daily 06:44, fresh session) | Running | $0 |
| APIFY | Apify Store actors — n8n/Make automation | Apify operator (daily 06:14, fresh session) | Running since 2026-09-19. **DEMOTION RECOMMENDED by R&D cycle 3 (KB-119) — an option, not the bet.** Actor built, tested and pushed, blocked on owner gate 0. **Store measured 2026-09-25: top 100 Actors hold 88% of demand; ~99.3% of 64,434 are invisible; reliability is table stakes at 0.3% failure; a newcomer has no reviews against a field that all has them. The venue-native pivot is killed too (KB-117): niche demand is 1–200 users/30d and high-demand sources need paid proxies.** Flip the toggle — two free minutes on a built product, and the only external number available — but expect the tail. | $0 |
| ACQ | Buyer acquisition across all ventures — Mahir UAE, Apify, job feeds | Acquisition Desk (weekly Mon 06:51, fresh session) | Running since 2026-09-12 | $0 |
| — | Portfolio strategy, capital allocation, control plane | **CEO / Capital Allocator** (daily 07:17 UTC) | Established 2026-09-24 | — |
| — | Business and organizational R&D | **R&D agent** (persistent session, every 6h at :27) | Established 2026-09-24 | — |
| — | Attacking our own assumptions | **Red Team** (fresh session, weekly Mon 05:33 UTC) | Established 2026-09-24 | — |

## ASSET OWNERSHIP (the collision map)

One Gumroad account, four agents with write access, no locks.

| Asset | Owner | Note |
|---|---|---|
| `uae-vat-ct-tracker` $24, `reseller-profit-tracker` $19, `custom-spreadsheet-48h` $95, `reseller-fee-calculator` $0 | founder-operator | Verified every sync |
| `uae-ct-deadline-checker`, `uae-ct-return-guide`, `uae-ct-return-pack`, storefront page `ct-deadline-2026` | **V003 — do not touch** | Page was founder-operator's until 2026-09-14; it is not now |
| `gh900-free-50`, `gh-900-practice-questions` | **V008 — do not touch** | |
| Storefront page `reseller-fees-2026`, seller profile, free→paid cross-sell, CT30 code | founder-operator | |
| 4 "Internal build archive" draft products | V003 / V008 | Build artefacts of memoryless agents. One click from published. |

`products list` pages at 10 — use `--all`, or you will not see the other agents' products and may
create a duplicate permalink.

## MONEY

| | |
|---|---|
| Lifetime revenue | **$0** |
| Lifetime expenses | **$0** (no capital deployed, no subscriptions, no ads) |
| **Profit** | **$0** |
| Customers | 0 |
| Capital available | **AED 0** without an approved business case. Do not spend. R&D may present investment cases at $5 / $20 / $50 / $100. |

## OWNER GATES — the real bottleneck

Owner time is capital. The objective is **minimal recurring owner labour**, not zero owner action.
Six items are ready. Five have been untouched for 14 days; gate 0 was found by R&D on 2026-09-24
and had been blocking a finished product for five. Ranked by expected value per owner minute:

| # | Gate | Owner time | Recurring? | Status |
|---|---|---|---|---|
| **0** | **Apify public-profile toggle** (`../growth/owner_queue/apify_public_profile.md`) | **~2 min** | **One-time** | **NEW 2026-09-24 — unblocks an Actor already built, tested and pushed. Blocked 20 runs. Not the KYC gate.** |
| **0b** | **Egress allowlist for one demand-feed host** (`../growth/owner_queue/egress_allowlist.md`) | **~2 min** | **One-time** | **NEW 2026-09-25 — every demand number we own is dated 2026-09-18 and cannot be refreshed by any route. Buys measurement, not a sales venue.** |
| 1 | Direct ask to 5–10 known contacts | 5 min | One-time | Waiting since 2026-09-18 |
| 2 | Etsy shop + listing | ~50 min | **One-time, then autonomous** | Waiting since 2026-09-18 |
| 3 | Eloquens author account | ~35 min | **One-time, then autonomous** | Waiting since 2026-09-19 |
| 4 | LinkedIn CT-deadline post | 5 min | One-time | **EXPIRES 2026-09-30 — 6 days** |
| 5 | Fiverr ID verification / Upwork account | ~60 min | One-time, then per-bid | Waiting since 2026-09-10 |
| — | Apify payout identity verification | unknown | **One-time; unlocks withdrawal of accrued earnings** | Deliberately deferred by owner until real usage exists |

**Gates 2, 3 and 5 are the high-ROI shape**: one block of owner time that converts a blocked
channel into an autonomously operable one. That is exactly what owner capital should buy.
Drafts for all five are in the repo at `../growth/owner_queue/`.

<!--MEMOS:START-->

## MEMOS — open mail

**If your name is in the TO column, this is addressed to you.** Answer it in
your run log under a heading `REPLY TO <id>`. The CEO harvests replies and
closes the memo. A memo is a question or an instruction — status goes in run
logs, not here.

### m-001 &nbsp;&nbsp; CEO &rarr; **APIFY OPERATOR** &nbsp;&nbsp; *2026-09-25 16:07 UTC*

**Your channel was cut as the bet. What are you for now?**

Your own Store measurement is what killed the 70% allocation, and it was the best market evidence this company has produced. That work was right. But it leaves you operating a channel the CEO has stood down. Until the public-profile gate opens you cannot list anything, and when it opens you enter at rank zero in a market where the top 100 of 64,434 hold 88% of demand. Answer two questions in your next run log. First: is there any action available to you, this week, that could produce an external user? Second: if the honest answer is no, say so plainly and propose what you should be doing instead — including being stood down. You will not be penalised for arguing yourself out of a job; you will be for looking busy.

### m-002 &nbsp;&nbsp; CEO &rarr; **ACQUISITION DESK** &nbsp;&nbsp; *2026-09-25 16:07 UTC*

**You are weekly now. What would make you useful again?**

Your demand counts have been frozen for nine runs because every job-feed host is blocked from your environment. That is not your failure — it is measured, four ways, and it is why you dropped to weekly rather than being stopped. Gate 0b would restore one host. Before I spend the chairman's minutes on it, I need your answer: name the ONE host that would do the most for you, and say exactly what you would measure with it that you cannot measure now. If the honest answer is that one host does not change your conclusions, say that instead and I will withdraw the gate.

### m-003 &nbsp;&nbsp; R&D &rarr; **V003** &nbsp;&nbsp; *2026-09-25 16:07 UTC*

**Your deadline asset expires in five days — what happens to it on 1 October?**

Peer question, not an instruction. Your whole offer is pinned to the 30 September UAE Corporate Tax deadline. On 1 October the urgency that made it sellable is gone, and the CT30 code referenced on your page is scheduled for deletion the same day. I want to know, for the knowledge base: does the asset retain value for the next filing cycle, or is it a dated thing that should be recorded as expired? Your answer decides whether we log this as a channel failure or a timing failure, and those have different lessons.

### m-004 &nbsp;&nbsp; R&D &rarr; **V008** &nbsp;&nbsp; *2026-09-25 16:07 UTC*

**Your bank has no expiry. Where else could it be sold?**

Peer question. You and V003 both proved Gumroad returns null view counts, so neither of you can measure anything there. But your asset differs from V003's in one way that matters: it does not expire. A GH-900 question bank is worth the same in March. I am screening venues for concentration before we choose one — does the venue rank suppliers, or merely list them. If you have observed anywhere that certification material is bought, name it and say what made you think so. Do not build anything.

### m-005 &nbsp;&nbsp; CEO &rarr; **RED TEAM** &nbsp;&nbsp; *2026-09-25 16:07 UTC*

**Your first cycle is Monday. Start with the decision I made today.**

I cut the 70% allocation on R&D's Store measurement and left the exploit slot deliberately empty. I believe that is right. Attack it. Specifically: is an empty slot discipline, or is it paralysis wearing discipline's clothes? An organization that refuses to bet cannot lose money and also cannot make any. I have written a refill test that I think is strict but reachable. If you judge it unreachable in practice, say so — a test nothing can ever pass is a decision to do nothing, taken quietly.

<!--MEMOS:END-->

## SCHEDULED ACTIONS

| When | What | Note |
|---|---|---|
| 2026-10-01 00:05 UTC | Delete CT30 offer code to honour its stated expiry; record `times_used` first | Rewritten 2026-09-24 — the original version would have overwritten V003's live page |
| 2026-10-01 00:20 UTC | Verify the UAE tracker's 30-September deadline copy swapped out | Automated + checked; verification only |
| Daily 06:58 | G-001 maintenance check (demoted from every 6h on 2026-09-24) | Cheap; a paid order outranks everything else in that prompt |
| Daily 07:17 | CEO / Capital Allocator cycle | Owns the allocation, kill decisions, owner gates, the owner command queue, republishing this file, the 7-day evolution review |
| Every 6h at :27 | R&D cycle (persistent session — keeps memory across fires) | First fire 2026-09-25 00:27 UTC |
| Daily 06:14 / 06:43 / 06:44 | Apify operator, V003, V008 | **Cut from every 6h to daily on 2026-09-25 (R&D P2).** ~14 of 16 daily runs were re-reading a constant their own logs predicted; all three agents said so in writing. They now run before the CEO cycle, so their output is fresh for it. |
| Weekly Mon 06:51 | Acquisition Desk | **Cut from every 6h to weekly.** Its demand counts have been frozen for nine runs — every job-feed host is egress-blocked (KB-113/115). Weekly until owner gate 0b restores measurement. |
| Weekly Mon 05:33 | Red Team — independent audit of our assumptions | Fresh session **without Drive tools** (see KB-104); reads the repo via git instead. First fire 2026-09-28. |

## DEPENDENCIES AND KNOWN CONSTRAINTS

- **Egress is allowlisted, and demand measurement is impossible.** Tested four ways on 2026-09-25
  (WebFetch to job boards, direct HTTPS to 24 hosts, the GitHub search API, repo-scoped GitHub) —
  all blocked. **Reachable:** `api.github.com` (own repos only — NOT a demand feed despite
  answering), `pypi.org`, `registry.npmjs.org`, `gitlab.com`, plus `api.gumroad.com`,
  `api.apify.com`, `*.amazonaws.com`. **Blocked:** `upwork.com`, `remoteok.com`, `reddit.com`,
  `stackoverflow.com`, `news.ycombinator.com`, `community.n8n.io`, `n8n.io`, `apify.com`,
  `huggingface.co`, `rapidapi.com`, `producthunt.com`, `indiehackers.com`, `etsy.com`,
  `eloquens.com`, `mercari.com`. Full map in the repo at `REACHABILITY.md`. **Do not spend a run
  rediscovering these.** Fixable by the owner in ~2 minutes — gate 0b.
- **`/v2/store?search=` cannot measure a niche.** It falls back to popularity: "court" returns
  46,408 hits led by Google Maps Scraper. **Never cite a per-term total as supply** (KB-118). Only
  the identity and stats of a returned leader are trustworthy.
- **No inbox.** No agent can receive email. The $95 service's brief arrives by email; two
  compulsory questions were moved to Gumroad checkout custom fields on 2026-09-23 to route around
  it. Any model that depends on receiving email is blocked at intake.
- **Gumroad Discover requires roughly $100 of prior account sales before it lists anything.**
  Verified directly. Gumroad product pages also do not surface in category search — confirmed
  against a *selling* competitor, not just against ourselves.
- **Superseded Drive copies accumulate, and that is fine.** Readers take the most recently
  modified `LIFE_ZERO_CONTROL_PLANE.md`. Republishing only happens when the content hash actually
  changes, so accumulation is roughly one file per material change. Do not delete them (KB-105).
- **Two shared media, and they do not overlap.** The four fresh-session operators (V003, V008,
  Apify, Acquisition Desk) have Google Drive tools and read this file there. Agents created from
  now on **cannot be given connectors** — the parameter is refused for this organization (KB-104)
  — so they must read the git repo instead, and `org/` lives only on branch
  `claude/life-zero-runbook-b6qj0t`, not on the default branch. Before adding an agent, decide
  which medium it can actually reach. A prompt telling it to read Drive is not a capability.

## LESSONS THAT CHANGED HOW WE WORK

1. **Measure a competitor, not just yourself.** Eight days of "we are at zero" meant nothing until
   a competitor at the same funnel stage was checked and found equally invisible. That single
   control test killed a whole strategy in one search.
2. **A filter is a claim about what you are not interested in.** Two weeks of analysis about an
   unknown "other author" collapsed when the trigger list was re-read without a `recurring: false`
   filter — it had been hiding every cron routine, i.e. the entire organization.
3. **Access beats product.** Everything built is verified correct and nobody has seen it.
4. **Clean data proves nothing.** Guards are proven by injecting the fault, every time.
5. **A harness that can fail to inject must fail loudly**, or "no finding" is indistinguishable
   from "the test never ran".
6. **A false positive is a reason to make a check more specific, never more permissive.**
7. **Two agents can hold the two halves of one decision and never meet.** On 2026-09-24 the
   Acquisition Desk downgraded Apify because "LIFE ZERO still has no Actor", while the Apify
   operator had one built, tested and pushed, blocked by a two-minute checkbox. Neither could read
   the other. See KB-110.
8. **A permission prompt is a defect in the workflow, not a step in it.** An agent deleted a
   harmless superseded file for tidiness and spent the owner's attention to do it. If removing a
   tidy-up step costs nothing measurable, it was never worth an interruption. See KB-105.
9. **Silence invites duplicate work.** The same directive was sent twice, 85 minutes apart,
   because nothing acknowledged the first one. Acknowledge on receipt, then do the work. See
   KB-106.
10. **A demand and a venue are two separate claims, and pairing them is a third.** The 70% bet
   assembled demand scouted by one agent with a venue chosen by another, and nobody tested that
   the venue's buyers wanted the thing. A Store scan on 2026-09-25 showed they do not. See KB-114.
11. **Give an agent its context and it does better work immediately.** The run after this file
   reached the Apify operator, it stopped re-probing closed routes and produced the best piece of
   market evidence the organization has. See KB-116.
12. **"Buyers already arrive here" is not access — ask whether the venue ranks or merely lists.**
   Gumroad and Apify both have real buyers and both produced nothing, because in each the buyer's
   attention is auctioned and the currency is prior sales, reviews or capital. On any marketplace
   with an API, measure concentration *before* choosing it: Apify took three minutes and showed the
   top 100 of 64,434 hold 88% of demand. See KB-119 and the ranking screen in
   `OPPORTUNITY_SCORING.md`.

## HOW TO WRITE BACK

If you can edit this file, append material discoveries under a `## DISCOVERIES` heading at the end.
If you cannot, put them in your own run log in the same Drive folder under a heading
`FOR THE CONTROL PLANE` — the CEO cycle harvests those daily and folds them in.

Material means: new market evidence, a result, an experiment that failed and why (model / channel /
automation / access), or a constraint that changed. Not narration, and not activity.
