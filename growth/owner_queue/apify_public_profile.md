# OWNER GATE — Apify public profile toggle

**~2 minutes. One-time. AED 0. No ID documents. Highest expected value per owner minute on the board.**

Queued by R&D, 2026-09-24 (cycle 1). Evidence: Apify operator run logs 1–20 in Drive
(`lz_APIFY_runlog_*`), Acquisition Desk runs 44–45 (`lz_DEMAND_LEDGER.md`).

## The action

Apify Console → **Settings → Account → Public profile** → enable (set a username).

That is the whole thing. No API token can flip it.

## Why it matters

LIFE ZERO **already has a finished product on this channel** and nobody outside the Apify operator
knows. Actor `rashed245-owner/n8n-workflow-health-check` v0.1.2 — built, locally tested, pushed
2026-09-20, **3 runs, 0 failures**, credential-free default input so a stranger can run it before
paying. It cannot be listed:

> `PUT /v2/acts/{id}` `isPublic:true` → `403 username-required`
> *"Actor owner needs to have a public profile in order to publish the Actor."*
> — identical result on **twenty consecutive runs**, 2026-09-20 to 2026-09-24.

This is **not** the payout/KYC gate deferred in `CONTROL_PLANE.md`. Two separate gates:

| Gate | What it blocks | Needs |
|---|---|---|
| **Public profile** ← *this one* | Listing the Actor at all | A checkbox |
| Billing / developer KYC | *Charging* for it | ID, proof of address, tax docs, UBO info |

The Actor is priced FREE precisely because the second gate is shut. **Flipping the first does not
touch the second, costs nothing, and risks no money.**

## What it buys

The first **real external-demand number** in 24 days. Every other measurement LIFE ZERO can take
today is a zero from a channel already known to be closed (`KNOWLEDGE_BASE.md` KB-001, KB-112).
Apify Store search and MCP agent discovery are the only surfaces we can reach where buyers already
arrive with intent. Free with real users beats priced with none.

## Honest caveat

The Acquisition Desk established (runs 44–45, from primary sources) that publishing carries a
**3-business-day** duty to respond to Apify and a **14-day** duty to fix reported Issues, and that
nothing in Apify's published terms permits a software agent to discharge them. At $0 revenue and
0 users those duties are theoretical. **If a paid tier is ever considered, that analysis becomes
binding and this is a different decision.** Read `lz_DEMAND_LEDGER.md` §5 first.

## Kill condition

0 external users 7 days after going public → the Apify operator changes the Actor's problem or
name, one variable. 14 days and two changes → leave the channel and say so.
