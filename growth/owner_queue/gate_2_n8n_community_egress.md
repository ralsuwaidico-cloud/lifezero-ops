# OWNER GATE 2 — one egress line: `community.n8n.io`. ~1–2 minutes. One time.

**Raised by the Acquisition Desk (run 49, Request E, 2026-09-30 07:00 UTC). Seconded by R&D after
running its own screens against it. The finding is the Desk's, not R&D's.**

## The ask

Add **`community.n8n.io`** to the environment's egress allowlist. Same shape as gate 0d, which worked.

## Why this one is different from the four host requests before it

Two of R&D's earlier host asks were wrong and are recorded as wrong: Upwork, which refuses machines
by its own published rules and so an allowlist bought nothing (KB-126), and five job boards that were
the wrong population (KB-127). **This one is the first where the venue states our own buyers are why
it exists.** REPORTED verbatim by the Desk from `/t/about-the-jobs-category/941`:

> *"Find open positions at n8n or related jobs. This may be useful if you need help to create a
> complex n8n workflow."*

Ten live buyer threads surfaced with URLs, two multi-page and active, one titled *"Looking for n8n /
Make Automation Specialist for Ongoing Fixed-Price Projects"* — which is this company's 86 BUILD
observations written in a buyer's own words. Buyer-side budgets cited at **$800–1,500 per build and
$1,200/month retainers**. **AED 0 to participate, 0% commission, no rank gate, no prior sales, no
reviews, no accreditation, and no venue payment rail — so no UAE payout eligibility to fail.**

## R&D's own screens, run honestly, including the one that could have killed it

| Screen | Verdict |
|---|---|
| Ranking screen — does the venue rank suppliers or list them? | **Lists.** A forum category is a reverse-chronological thread list. Passes. |
| Source screen — right population? | **Yes, stated by the venue itself.** Passes, and this is what KB-127 failed. |
| KB-161 — does delivery write into infrastructure we do not own? | **No — and this is now quoted, not summarised (R&D cycle 25, KB-183).** Our own supplier asset `lz_OFFER_n8n_repair_fault_catalogue_run33.md` says verbatim: *"We do not need access to your server, and we do not want it."* Exclusion 2: *"No server, host, VPS, Docker, or n8n instance administration."* Exclusion 6: *"No credential handling: we work from an export with secrets removed."* Runbook step 7: *"Apply the fix to the export only. **Never to a live instance.**"* The decline test fires on any request for server, credential or production access. **Passes by design.** This screen closed the entire bounty category, so it was the likeliest kill here and it does not bite. |
| KB-164 — does delivery need our compute per customer? | **Yes, and it does not bind at this scale.** A bespoke build is per-customer agent work, so a weekly model quota caps throughput. At zero customers a ceiling of a couple of jobs a week is irrelevant, and a $450–2,500 job covers its compute many times over. **Recorded as a live constraint on growth, not a reason to decline.** |

## What the minute buys — and the best part is that it can kill the route for free

1. **The permission question becomes answerable.** Whether a seller may reply in that category is
   **NOT ESTABLISHED**, and the Desk's own standard treats silence on permission as *not permitted*.
   If the rules forbid it, the route closes permanently for AED 0 and stops being carried.
2. **The first readable buyer feed in this company's history for work it can actually do** —
   thirteen runs of frozen demand counts un-freeze on the right population.
3. **Per-lead owner labour drops to a ~1-minute paste**, because the Desk reads the brief and hands
   over a finished scoped reply instead of the owner scoping it.

## The cost nobody is hiding

**This route has recurring owner labour and it cannot be removed: one human post per lead, forever.**
Roughly one minute of paste against a $450–2,500 fixed-scope brief. That is the best ratio on a
seventy-one-row register, and it is still recurring. Price it as recurring.

## Kill conditions, pre-registered by the Desk

- Rules forbid seller solicitation, require human-only execution, or require a disclosure we cannot
  truthfully make → **permanent close, AED 0 spent.**
- Rules permit, ten qualifying replies prepared over thirty days, **zero paid engagements** → route
  dead, and reach is then proven unsolvable by public solicitation surfaces, which is worth more than
  the gate cost.

**This is a screen, not a channel, and must not be reported as reach until a rules page has been
read.** Nothing has been drafted, posted, registered or contacted.


---

## Added by R&D cycle 25 — one thing this gate does NOT authorise

If this gate is granted and the category rules permit a reply, **no reply and no listing may assert a
CVE, a CVSS score, or a deprecation date.** Our fault catalogue carries
*"CVE-2026-21858 … CVSS 10.0 … affects 1.65.0 – 1.120.x"* and similar, and **every one of those claims
is graded REPORTED in our own ledger — no primary page was ever read.** R&D measured on 2026-09-30 that
`services.nvd.nist.gov`, `cve.circl.lu`, `api.osv.dev` and `docs.n8n.io` are all egress-blocked from
this environment.

**Telling a stranger their production system carries a critical vulnerability, on evidence we cannot
read, is the one thing the rules forbid without qualification.** The catalogue reads as authoritative
and will invite exactly that, so the prohibition is written here as well as in KB-184.

What may be offered is what the buyer's own export decides: an expression pointing at a node that is
not there, and a workflow with no error handling at all. Those are checkable from the file they send us.
