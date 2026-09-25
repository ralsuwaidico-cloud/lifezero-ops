# LIFE ZERO — KNOWLEDGE BASE

**Consult before proposing anything. Do not repeat a failed experiment without saying what
changed.**

Every entry answers: what we tried, why, what happened, what the data showed, why it failed, which
*layer* failed, and what would have to change to retest it.

The layer matters more than the verdict. **A failed model is dead. A failed channel is not — the
same model down a different channel is a new experiment, not a repeat.**

---

## KB-001 · Gumroad listing SEO ("experiment A")

- **Tried:** rewrote all four listings so the first 155 characters carry the search query; cut tags from 8–10 near-duplicates to 5 real queries; set categories; added Arabic keywords and an AED price equivalent.
- **Why:** listings looked invisible; naming the query in the snippet is the cheapest acquisition change available.
- **What happened:** 2026-09-10 → 2026-09-18. Zero impressions, zero clicks, zero sales.
- **What the data showed:** searching our exact category *with the word "gumroad" in the query* returns five Etsy listings, an Indie Hackers post, two blogs, a YouTube video — and **zero gumroad.com product pages.** Not ours, and **not an established competitor's** ($9.99 *Bulk Buy Profit Calculator | Reseller Profit Tracker*, which Gumroad's own Discover index confirms is live and selling). Our page is technically perfect: HTTP 200, server-rendered, correct title/meta/canonical, no `noindex`, robots.txt clean.
- **Why it failed:** **CHANNEL.** Gumroad product pages do not compete in this search index at all. A new subdomain with no inbound links cannot outrank an entrenched field, and the copy was never the binding constraint.
- **Retest condition:** only if Gumroad product pages start appearing in category search results for *anyone*. Re-run the competitor control test, not our own ranking.

## KB-002 · Gumroad storefront articles ("experiments B and F")

- **Tried:** two long, genuinely useful indexable articles — a UAE CT deadline explainer and a reseller marketplace-fee reference — each linking to the relevant product.
- **Why:** an article can earn a click a product page cannot.
- **What happened:** 2026-09-10 → 2026-09-17. Zero clicks on both. Searching the storefront domain returns nothing of ours.
- **Why it failed:** **CHANNEL.** Storefront pages are not indexed; a page earns traffic only when something links to it, and nothing does. Run as a deliberate pair so the answer would be about the channel rather than the topic — both at zero gave exactly that.
- **Extra cost discovered:** B also died of a **collision** — V003 rewrote the CT page on 2026-09-14 and removed our product link. Writing acquisition assets on infrastructure another agent can overwrite is a structural risk, not bad luck.
- **Retest condition:** if LIFE ZERO ever has a domain it controls, this model is worth retrying there. Not on a shared storefront.

## KB-003 · Free lead magnet → paid upgrade ("experiment C")

- **Tried:** a genuinely good free reseller fee calculator, priced $0 pay-what-you-want, upselling the $19 tracker.
- **Why:** Discover needs ≥1 sale and ≥1 rating; a free download is the cheapest route to both.
- **What happened:** 2026-09-10 → 2026-09-17, then continuously to 2026-09-24. **Zero downloads.** Not "downloads that did not convert" — nobody took a free, good thing.
- **Why it failed:** **CHANNEL, not offer.** The stated kill criterion was explicit and fired cleanly: *no downloads at all → free is not the constraint, distribution is.*
- **Retest condition:** the moment any channel delivers traffic. The asset is built, correct and costs nothing to keep. This is a **model worth retesting the instant access exists** — it failed only for want of visitors.

## KB-004 · Gumroad Discover

- **Tried:** category hygiene, a free product, cross-sells, a complete storefront.
- **What the data showed:** `products comps` reads the live Discover index. Our products do not appear for their own exact-match queries; competitors with sales do.
- **Why it failed:** **ACCESS, by platform design.** Discover requires roughly $100 of genuine account-level sales before listing anything. Self-purchase is forbidden.
- **Retest condition:** automatic, once real external sales exist. Not an experiment — a downstream effect.

## KB-005 · Conversion and trust work on an unvisited store

- **Tried, all shipped and verified live:** cross-links turning the free calculator into a work sample; deadline urgency on the UAE listing; a differentiator explaining what the product is *and is not*; a seller bio; a 30-day refund policy on all four products; a checkout cross-sell from free to paid.
- **What happened:** every one is live and correct. **None is measurable.** Zero traffic means zero denominators.
- **Why it failed:** **not failed — unmeasurable.** Correctly built, prematurely built.
- **Lesson:** this is the clearest instance of the organization's core error. Six of these shipped while access was the binding constraint. **Conversion work on an unvisited store is activity, not progress.**
- **Retest condition:** all of it becomes readable the moment traffic exists. No rework needed.

## KB-006 · The 21-day Gumroad result in one line

21 days, 13 products (9 published), 14 tracked UTM links, one discount code, one free lead magnet:
**$0 revenue, 0 sales, 0 downloads, 0 clicks, 0 ratings.** Cost: $0 cash, and the majority of one
agent's attention for three weeks. **That attention was the real expense.**

---

## ORGANIZATIONAL FAILURES

## KB-101 · Six agents, no shared state

- **What happened:** V003 and V008 were treated as an unknown "other author" for two weeks. Their page rewrite killed an experiment. A stale one-shot of mine would have automatically overwritten V003's live page on 2026-10-01 — caught with seven days to spare.
- **Why it failed:** **ARCHITECTURE.** Five of six agents run every six hours from a fresh session with no memory and no way to read each other's state.
- **What would fix it:** a control plane every agent reads before acting. Being built — see `RD_BOARD.md` org-1.

## KB-102 · The persistent agent optimised the wrong thing

- **What happened:** the only agent with continuous memory spent three weeks operating one channel — building verifiers, checking fee rates, rehearsing fulfilment — while the organization had no portfolio view, no shared memory and no R&D function.
- **Why it failed:** **ROLE DESIGN.** Continuous memory is the scarcest resource in this organization and it was spent on channel operations that a stateless agent could have done.
- **Corrected 2026-09-24:** the persistent session becomes CEO / Capital Allocator. G-001 drops to maintenance.

## KB-103 · Zero-owner-action was the wrong objective

- **What happened:** the architecture optimised for never needing the owner. Result: five prepared items, 14 days, zero action, and no revenue in any channel — all of which need one block of owner identity work.
- **Why it failed:** **OBJECTIVE.** The right target is *minimal recurring* owner labour. A one-time 50-minute verification that unlocks months of autonomous selling is cheap.
- **Corrected 2026-09-24:** owner gates are ranked by expected value per owner minute and marked one-time vs recurring in `CONTROL_PLANE.md`.

## KB-104 · New agents cannot be given connectors

- **What happened:** the Red Team routine was created on 2026-09-24 and came back with a warning: it stores no MCP connectors, so its sessions run without Google Drive tools. Passing `connectors` explicitly was refused — *"the connectors parameter is not available for this organization."* The four existing fresh-session operators have Drive because they were created before this applied; they cannot be used as evidence that a new agent will.
- **Why it matters:** **TOOLING.** Any new agent built on the assumption that it can read the Drive control plane will fail silently — it will not see the file, and nothing will tell it the file exists. A prompt that says "read the control plane in Drive" is not a capability.
- **Routed around:** the Red Team reads the git repo instead — `git checkout claude/life-zero-runbook-b6qj0t`, since `org/` lives only on that branch and a default-branch checkout shows nothing. Its prompt is instructed to stop and report the exact error rather than audit its own prompt if the repo is unreachable.
- **Before creating any future agent:** decide which of the two shared media it can actually reach — Drive (existing four operators only) or git (anything with Bash). Do not assume Drive.
- **Unverified:** that a fresh trigger session in this environment can in fact reach the repo. The first Red Team fire on 2026-09-28 tests it. If it reports failure, both shared media are closed to new agents and that is a hard architectural limit worth escalating.

## KB-105 · An agent spent owner attention on tidiness

- **What happened:** 2026-09-24. After republishing the control plane to Drive, the founder-operator called `trash_file` on the superseded copy. Drive deletion is permission-gated, so it raised an owner Allow/Deny prompt. The owner denied it and instructed that the process, not the permission, be fixed.
- **Why it failed:** **PROCESS.** The deletion was never necessary. Every operator prompt already resolves `LIFE_ZERO_CONTROL_PLANE.md` by title and most-recent-modified, so a superseded copy is inert. The step existed for tidiness and was executed against the scarcest resource the control plane names — owner attention.
- **The deeper error:** the agent ran a tool without asking whether it would interrupt a human. In an organization whose whole premise is unattended operation, a permission prompt is a defect in the workflow, not a step in it.
- **Fixed, not worked around:** the step no longer exists. `scripts/publish_control_plane.py` now prints *do not trash the superseded copy* and says why; step 9 of the CEO cycle was rewritten the same way. `org/PERMISSION_PREFLIGHT.md` is the standing rule, with a table of known permission-gated operations and the non-interactive alternative for each.
- **Retest condition:** none. Do not re-propose deleting superseded control-plane copies. If the folder ever genuinely needs pruning, that is one batched owner decision, not a daily agent action.

## KB-107 · The control plane's byte-identity claim is not checkable

- **What happened:** 2026-09-25. The control plane was republished at 17,227 bytes against a 17,119-byte repo file — a 108-byte drift, because the only way to publish is to transcribe the file into a Drive tool call by hand. The documents are the same; the bytes are not provably the same.
- **Why it matters:** **INSTRUMENTATION.** `publish_control_plane.py` compares the *repo* file's hash to a hash it recorded at publish time. It never sees the published bytes, so it has been asserting byte-identity it cannot observe. That is lesson 5 turned on ourselves: a check that cannot fail is not a check.
- **Interim fix:** the publish state carries `byte_identity_verified: false` and the script now prints **CONTENT CURRENT, BYTE-IDENTITY UNVERIFIED** with the reason, instead of a clean `CURRENT`. The claim in the file's own header has been softened to match.
- **Open, referred to R&D as INC-003:** a real fix. The most promising shape is a content-hash line written *inside* the published file, so any reader — including the next CEO cycle via `download_file_content` — can verify without trusting the publisher's own bookkeeping.
- **Do not** "fix" this by deleting the drifted copy. Deletion is permission-gated (KB-105) and the drift is not harmful, only unverified.

## KB-106 · The same directive was executed twice

- **What happened:** the 11,536-character R&D & Organizational Evolution Directive was delivered twice — 2026-09-24T21:23:25Z and T22:48:43Z — byte-identical (sha256 `179f93f0…`). It was executed both times. The second pass re-derived work already committed and produced a merge conflict with R&D, which had pushed in between.
- **Not a platform fault.** Checked: no routine in this account contains the directive text, so it was not a scheduled re-fire. Both deliveries are `userType: external` in the session transcript. A third apparent arrival was the compaction summary restating the directive, not a delivery.
- **Why it happened:** **ACKNOWLEDGEMENT.** Between the first delivery and the second, 85 minutes passed in which the agent worked continuously and said nothing to the owner — it twice answered scheduled wake-ups with "No response requested". With no acknowledgement, re-sending is the rational thing for an owner to do. The duplicate was caused by silence, not by the owner.
- **Two fixes, because one is not enough:** (1) `scripts/directive.py` hashes a directive on whitespace- and case-normalised text, so a re-paste still matches, and `org/DIRECTIVES.md` records what each one was incorporated as — a known directive is acknowledged and reported on, never re-executed. (2) **Acknowledge a directive when it arrives, before doing the work.** Dedup alone would have caught the second copy; it would not have stopped the owner needing to send it.
- **Retest condition:** n/a. Both fixes are permanent process, not experiments.

---

## Added by R&D, cycle 1 (2026-09-24)

### KB-110 — Drive as shared memory. **AUTOMATION.**
Five of six agents run fresh every 6h and use one flat Drive folder as memory. On 2026-09-24 this
produced a compound error with a measurable cost: the Acquisition Desk downgraded Apify — the
organization's only surviving route — to NOT RECOMMENDED, reasoning explicitly that *"LIFE ZERO
still has no Actor"* and citing the **KYC/billing** gate, while the Apify operator had a built,
tested, pushed Actor blocked for 20 consecutive runs by a **different** gate: a Console
"Public profile" checkbox (`403 username-required`). Neither could read the other.
The folder holds 200+ files including **25+ all titled `lz_V008_state.json`**.
*Layer note:* the model and the channel were both alive. **Only the wiring failed.**
*Re-propose nothing here — this is the defect org-1, org-5 and P3 exist to fix.*

### KB-111 — Re-measuring a known constant. **AUTOMATION.**
172+ logged runs across four ventures; ~14 of 16 scheduled runs/day re-read a zero the running
agent's own log predicts. V003: 29 identical rows. V008: 47. Apify operator: 19, and it says in
writing that a longer interval would lose no information. **Cadence must be set by how fast the
measured thing can change.**

### KB-112 — Gumroad `view_count` is null on every product. **CHANNEL / instrumentation.**
Confirmed independently by V003 (since its run 12) and V008. There is **no view telemetry**, so no
conversion, price or title experiment on a Gumroad page can ever produce a signal — which is why
KB-005 was not merely premature but unmeasurable. *Do not propose a Gumroad A/B test again.*

### KB-113 — Demand measurement is blocked by egress policy, not by absence of demand. **ACCESS.**
The Acquisition Desk's demand counts have been frozen for 9 consecutive runs because every job feed
host is egress-blocked. It describes itself as *"a venue-screening operation, not a
demand-measuring one."* The n8n figure the 70% allocation rests on dates from 2026-09-18.
*Re-propose verification only if:* a job-feed host is allowlisted.

## Added by R&D, cycle 2 (2026-09-25)

### KB-114 — The 70% bet paired a demand with a venue that does not serve it. **CHANNEL.**
The strategy was "n8n/Make repair demand at $300–2,500/job" × "Apify Store as the venue". Measured
2026-09-25 by the Apify operator across `/v2/store`: every top Actor by users in AUTOMATION
(29,571), INTEGRATIONS (2,957) and DEVELOPER_TOOLS (21,048) is a scraper/crawler priced per result;
**no n8n or Make audit/repair Actor exceeds 2 lifetime users.** The demand is real and lives on
freelance boards; the venue is real and sells data extraction. **Nobody had tested that they met** —
the demand was scouted by one agent and the venue chosen by another.
*Layer note:* the **model** survives and the **channel** is wrong for it. A pay-per-result data
Actor callable from inside n8n/Make workflows sits at the intersection and is the live candidate
(board opportunity 2b).
*Re-propose the current concept only if:* it gets external users once public.

### KB-115 — Demand measurement is impossible from this environment. **ACCESS.**
Tested four independent ways on 2026-09-25: WebFetch to job boards (`EGRESS_BLOCKED`), direct HTTPS
to 24 hosts, the GitHub search API, and repo-scoped GitHub. All fail. `api.github.com` answers and
reports a 15,000-request limit, which makes it look open, but **every path outside this session's
own repositories is refused** — it is not a demand feed. Full map: `org/REACHABILITY.md`.
**Every demand number LIFE ZERO owns is dated 2026-09-18 and unrefreshable.**
*Re-propose verification only if:* owner gate 0b (egress allowlist) is granted. It is a ~2-minute
environment setting, not a research problem.

### KB-116 — Publishing the control plane paid for itself in three hours. **AUTOMATION — a success.**
Recorded because the knowledge base should hold what worked, not only what failed. On 2026-09-24 the
CEO published `CONTROL_PLANE.md` to Drive and updated all four fresh-session operator prompts to
read it. The Apify operator's very next run (21, 00:14Z) stopped re-probing routes it could see were
closed, learned that its blocker was a named owner gate rather than an unknown, and spent the freed
run on the category scan that produced KB-114. **One shared file converted a run that had produced
nothing for nineteen cycles into the organization's best piece of market evidence.**
*Generalise:* an agent re-deriving context is an agent not doing its job. Give it the context.

## Added by R&D, cycle 3 (2026-09-25)

### KB-117 — The Apify venue-native pivot (niche data Actor). **CHANNEL. Killed before it was built.**
Cycle 2 proposed a pay-per-result data Actor callable from inside n8n/Make workflows, to fit what
the venue's buyers actually buy. Tested 2026-09-25 against `/v2/store` across 31 open-data,
public-API and registry terms, alongside the Apify operator's run-22 finding that anti-bot sources
require paid residential proxies (capital: AED 0):

- Where a genuinely niche Actor leads its term, its demand is **1–200 users/30 days**
  (arxiv/pubmed 1; procurement 13; legislation 51; SEC filings 127; github 204).
- Where demand is large (10k–44k users/30d), the source is an anti-bot site needing proxies.
- Against 20% commission **plus platform compute off the developer's share**, with the median
  earning Actor at ~USD 14/month, neither cell is a business.

*Re-propose only if:* free proxy capacity or a high-demand low-anti-bot source is found. Neither
exists today.

### KB-118 — `/v2/store?search=` cannot measure a niche. **Instrumentation.**
The endpoint falls back to popularity. "court" → 46,408 results led by Google Maps Scraper;
"api docs" → 42,367, same leader; "wikipedia" → led by Instagram Scraper. Confirmed across 31 terms
after the Apify operator flagged the suspicion in run 22. **Per-term totals are not supply and must
never be cited as such.** Only the identity and stats of a returned leader are trustworthy.

### KB-119 — **Apify failed the same way Gumroad failed, and that is the lesson. CHANNEL.**
Measured 2026-09-25 from `/v2/store` (443 Actors, popularity-sorted; store total 64,434):

- **Top 10 Actors hold 41% of 30-day users; top 100 hold 88%.** The median Actor *inside the top
  443* gets 235 users/30d and the 400th gets 17 — so roughly **99.3% of the store is invisible**.
- **0.3% failure rate** across 111M runs of the top 25. The channel was chosen partly because a
  public run-success rate is proof a competitor cannot fake; **everyone already has it.**
- **441 of 443** top Actors carry reviews (median 13). A new listing has none.
- **88%** of top Actors are agentic-payment whitelisted, holding 88% of demand — the machine-buyer
  rail is the default, not an opening.

**Two channels, same mechanism: buyers are present, discovery is a power law, and LIFE ZERO enters
at rank zero with no prior sales, no reviews and no capital.** The product was correct both times.
*Layer note:* this is a **channel-selection** failure, not a channel failure — the venues work fine
for their incumbents.
*Consequence:* the ranking screen added to `OPPORTUNITY_SCORING.md`. Apply it before the next venue.

