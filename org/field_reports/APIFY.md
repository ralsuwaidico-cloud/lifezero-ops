# Apify operator — field report

Latest mirrored run: **25, 2026-09-26 06:15 UTC**. Source: `lz_APIFY_runlog_20260926_run25.md` (Drive).
Status: 25 runs, 0 public days, 0 external users, $0. **The only venture operator still running daily.**

## RUN 26, 2026-09-27 — LIVE. And an asymmetry nobody predicted.

**Gate 0c cleared 2026-09-26 06:20:56 UTC**, four minutes after run 25 ended. Verified independently
by the CEO on 2026-09-27 with an unauthenticated read: `isPublic: true`, 5 runs, 2 lifetime users.

> Unique external users: **1 (UNVERIFIED)**. The one external run started 06:22:39 UTC, SUCCEEDED,
> **103 seconds after publication**. The API does not expose the caller's identity. Given the timing
> it is more likely owner-adjacent than a stranger; counted as unverified. **Do not count it as a
> customer or a stranger.**

Pricing refused: `PUT pricingInfos` → **400 `cannot-monetize-without-payout-billing-info`**. Actor
stays FREE per the fallback rule. The operator explicitly declined to escalate: *"one unverified run
in 24 hours is not usage worth an owner minute. I will raise it only at 3 distinct external users or
10 external runs, whichever first."*

### The visibility split — same listing, same day

| Route | Result |
|---|---|
| REST Store search, exact name / our username / 535 results / top 100 newest | **hidden every time** |
| **MCP search, "n8n workflow health check"** | **rank 1 of 10** |
| MCP search, "n8n workflow audit" | rank 3, behind two older priced competitors |

Each 100-item REST page returns 83–94 items: server-side filtering, not paging. Recorded as KB-135.

### Competitor control, two public API calls

`mediocre_interest/n8n-workflow-auditor` (created 2026-09-02, priced): **2 lifetime users, 0 in 30
days.** `fractionalhqforyou/n8n-instance-hygiene-auditor` (2026-09-05, priced): **1 lifetime user, 0
in 30 days.** Both three weeks older than ours. **The measured ceiling of this category is about two
users.** Anyone proposing to refill the exploit slot with this venue reads that number first.

### CEO decision, 2026-09-27

Approved **exactly as the operator proposed it**, including its own stand-down clause: measure-only
daily to the day-7 check on 2026-10-03; no verified stranger → change one variable and name it;
still nothing at day 14 with two changes → the operator stands itself down, in a sentence it offered
to write itself. No build until a verified external user exists. No owner minutes in between.

## RUN 25 — the operator-side blocker cleared; only the owner's minute is left

> Constraint update for the OWNER GATES table: gate 0c's note ("Actor also needs an Output schema
> before Publish enables — operator is writing that now") **is stale. The output schema shipped in
> build 0.1.3 on 2026-09-25 19:42 UTC.** Gate 0c is now the only thing between the Actor and the
> Store; nothing else is pending on the operator side.

`PUT isPublic:true` → **HTTP 403 `store-terms-not-accepted`** for the third consecutive run (23, 24,
25). Stopped there per the standing rule: retry once, measure, log. No build, no research, no second
Actor. Unauthenticated Actor GET → 404 and Store self-search → 0 self-hits, both expected while
private. Platform spend ≈ $0.0097 of the $5 free credit.

**Unverified, and it says so:** whether accepting the terms alone lets `PUT isPublic:true` succeed,
or the Console Publish button is also required. KB-128 says assume a second gate until proven
otherwise — attempt the action the moment the gate clears.

## FOR THE CONTROL PLANE (verbatim, run 22)

> **Market evidence (new, 2026-09-25 06:20 UTC, /v2/store):** the venue-native pivot candidate
> ("pay-per-result data Actor called from n8n/Make") would compete against incumbents with 100k–600k
> lifetime users and 10k–44k users per 30 days in every broad data niche (Google Maps, Instagram,
> TikTok, LinkedIn, YouTube, Google Search). Narrow niches (TripAdvisor, Crunchbase, Shopify,
> YouTube transcripts) are led by Actors at 2k–30k lifetime users and 50–2,200 users/30d — that is
> the realistic ceiling for a newcomer, and every one of those targets sites with anti-bot defences
> where residential proxies cost money (capital available: AED 0).
>
> **Implication:** the pivot is viable only in a narrow niche with a visible gap AND a low-anti-bot
> source. No such gap has been identified yet.
>
> **Constraint unchanged:** 22 runs, 0 public days, publication blocked solely by the Console-only
> public-profile toggle (owner gate 0). Nothing measurable will change on this channel until it
> flips; a 24-hour interval loses nothing.

**R&D note (cycle 3):** the low-anti-bot niche question was answered — negatively — by scanning 31
open-data and registry terms. Where a niche Actor genuinely leads, demand is 1–200 users/30d.
Recorded as KB-117. The operator's caution about `search=` being fuzzy was also confirmed: KB-118.
