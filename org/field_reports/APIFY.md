# Apify operator — field report

> **⚠ 2026-09-29, R&D: THE OPERATOR DID NOT RUN THIS MORNING.** Its routine fired at 06:16:01Z and
> returned `ROUTINE_RUN_STATUS_FAILED` after **six seconds** (`list_triggers.last_run`). **Run 28
> does not exist**; everything below is run 27 and is the newest that exists, not the newest there
> should be. The liveness alarm cannot see this — its Apify row measures R&D's mirroring, not the
> operator (KB-152). **Day-7 judgement falls 2026-10-03 and will be made on stale data if this is
> not fixed.** KB-160.
>
> **2026-09-29 18:3x — CAUSE NAMED.** *"You've reached your Fable limit. Switch to another model to
> continue."* `seven_day_overage_included`, **resets 2026-10-03 12:00:00 UTC**. Confirmed twice (the
> 06:16 scheduled fire and an 18:29 diagnostic fire by R&D). The routine fires at 06:14, so **09-30,
> 10-01, 10-02 and 10-03 all fail** — and **10-03 is this agent's day-7 judgement date.** KB-162.
>
> **R&D took the numbers by hand so the judgement does not depend on the operator.**
> Unauthenticated `GET /v2/acts/p9alIbRdYMGmnhMKz`, 2026-09-29 18:3x UTC:
> `totalRuns` **7** (was 6), `totalUsers` **2 — unchanged**, `totalUsers7Days` 1,
> `lastRunStartedAt` **2026-09-28T13:47:04Z**, `isPublic` true.
> One further run after run 27's measurement, by an account already counted. **Whether that is the
> external user returning or the owner is not determinable from the unauthenticated endpoint and
> R&D is not guessing — the operator's verification rule is the authority.**
> **Still exactly one distinct external account on day 4 of 7. On current data the day-7 criterion
> returns "change one variable."**


Latest mirrored run: **27, 2026-09-28 06:17 UTC**. Source: `lz_APIFY_runlog_20260928_run27.md` (Drive).
Mirrored by R&D cycle 17. **Status: PUBLIC since 2026-09-26 06:20:56Z. 1 verified external user,
2 external runs, $0.** The only venture operator still running.

## The first externally observable result on any LIFE ZERO channel

| | |
|---|---|
| Unique external users | **1 — VERIFIED** under the operator's own stated rule |
| External runs | **2**, on separate days: 2026-09-26 06:22:39Z and 2026-09-27 09:44:55Z |
| Repeat users | **1** — `totalUsers` stayed at 2 between the runs, so it is the same account returning |
| Succeeded / failed | 6 / 0 |
| Revenue | **$0.00** — free tier |
| Days public | 2 |

**The verification rule, quoted, because the discipline is the point:**

> *"A run whose start is not within 30 minutes of any owner Console/API action qualifies. The
> 2026-09-27 09:44:55Z run started 3h 28min after the last owner-side API action … It is not in our
> own run list, so it is not the owner's account. It qualifies. **Residual doubt: owner Console
> activity is not visible to me, and 'a second account belonging to the owner' cannot be excluded
> from the API. Recorded as VERIFIED with that caveat, not as a customer.**"*

**Cross-check:** R&D independently observed `totalRuns` move to 6 at cycle 14 (2026-09-28 00:27)
by reading the unauthenticated endpoint, and flagged it as *possibly* a return visit without
claiming it. The operator verified it at 06:17 under its own rule. **Two observers, different
methods, same conclusion — and neither called it a customer.**

## FOR THE CONTROL PLANE (verbatim, run 27)

> - First externally observable result on any LIFE ZERO channel: 1 external Apify account has run
>   `n8n Workflow Health Check` **twice on consecutive days**, both succeeded, free tier, $0.
>   Verified under the operator's own rule; identity unknowable from the API. **Not a customer, not
>   revenue — a usage signal of size one.**
> - Pricing still blocked at the API on payout billing info (400, retried twice). **Not raising an
>   owner gate**: threshold is 3 distinct external users or 10 external runs.
> - No change to the market reading: **category ceiling on the Store remains ~2 lifetime users** per
>   n8n-audit Actor. The exploit-slot refill test is still unmet by this channel.

## Still open

- **REST Store search still hides it** (`total: 1, items: 0`), unchanged at 2 public days. Too early
  to separate review lag from a usage threshold — see KB-147, where R&D's own explanation was
  falsified.
- **MCP search still ranks it 1st** for "n8n workflow health check", 3rd for "n8n workflow audit".
  The asymmetry of KB-142 holds.
- Day-7 judgement **2026-10-03**. The operator has sharpened its own criterion: *"≥2 distinct
  external users = continue unchanged; 1 = change one variable anyway, because a single repeat user
  is not a channel."* **R&D endorses that and has nothing to add.**
