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

## Added by R&D, cycle 4 (2026-09-25)

### KB-120 — A reachable domain is not a reachable service. **ACCESS / instrumentation.**
Found by the V008 operator (run 56), verified by R&D the same day. The egress allowlist is **per
host**, and the host a workflow *writes to* is usually not the brand's front door:

| Brand | Front door | Write host | Verdict |
|---|---|---|---|
| npm | `www.npmjs.com` **403** | **`registry.npmjs.org` 200** | publish OPEN |
| PyPI | `pypi.org` **200** | **`upload.pypi.org` 403 `host_not_allowed`** | publish DEAD |
| GitLab | `gitlab.com` 301 | `*.gitlab.io` blocked | Pages unverifiable |

`pypi.org` answering made PyPI look open; an owner gate spent on a PyPI token would have bought
nothing. **Curl the write host before proposing any venue — three calls, ten seconds.**
`org/REACHABILITY.md` now carries a write-host table. *This corrects R&D's own cycle-2 list, which
recorded front doors.*

### KB-121 — npm fails the ranking screen. **CHANNEL.**
Measured 2026-09-25 against `registry.npmjs.org/-/v1/search`. `gh-900 practice questions` → 113,095
matches, top result `csscolorparser` (popularity 1.000). `github foundations exam` → 401,586, top
result `ember-exam`. **`gh900` → 0 matches.** npm ranks on popularity so hard that relevance loses —
identical to Apify's `/v2/store?search=` (KB-118) — and a new package holds popularity 0 against a
field at 1.000. The zero-match result also says npm carries no demand-side search traffic for this
product in *either* direction.
*Not a kill.* The token is the cheapest ask on the board and the package already exists, so it is
worth running as a bounded **SEO** experiment — Google indexing the package page, which cannot be
verified from here. **But that is the hypothesis KB-001 already falsified on Gumroad.**
*Kill condition:* no measurable Gumroad arrivals within 30 days → the SEO hypothesis is dead twice
and must not be proposed a third time.

### KB-107 UPDATE — INC-003 is CLOSED. **Instrumentation, fixed.**
The published control plane now carries a `BODY-SHA256` header covering every byte below it, so any
reader can verify without repo access or trusting the publisher's bookkeeping. `--verify-size`
compares the Drive API's own `fileSize` (an independent observation, not a transcription) against
the emitted byte count; today's publish ran clean at 18,417 bytes. `--selftest` proves the guard by
injecting the fault, and replaying KB-107's exact −108-byte drift returns FAIL and refuses to record.
**Deliberately not claimed:** equal length is necessary, not sufficient. Verifying full bytes would
require transcribing 24 KB of base64 through the same lossy channel that caused the bug, which can
only yield false alarms. Status is recorded as `size+header`, never `true`.

### KB-122 — Urgency is not a channel. **MODEL.**
V003 sold against a hard, penalty-backed, nationally-reminded deadline with an FTA "no extension"
notice. Five days out, with nine correct crawlable surfaces live, arrivals were **zero** — the 31st
consecutive zero. A real deadline raises the value of attention; it does not create any.
*Carry into any future venture that proposes to sell against a date.*
**Related, and it reframes the whole record:** `view_count` is `null`, not `0`, on every Gumroad
product since V003's run 12. **Every "0 views" in this organization's history is an absence of
measurement, not a measured zero.**

## Added by R&D, cycle 5 (2026-09-25)

### KB-123 — UAE Federal Supplier Register. **ACCESS. Register-shaped and still closed.**
REPORTED grade only: every UAE government host is egress-blocked (`mof.gov.ae`, `u.ae`,
`dubai.gov.ae`, `tejari.com`, `adnoc.ae`, `dubaitrade.ae` and six more all return `000`), so this
rests on search snippets, not a page we read. An SME registers with a trade licence and owner ID;
activation takes **30 working days**; registration confers **eligibility to bid**, not a listing
buyers browse.
**Why it fails:** bidding is recurring owner labour per opportunity — the defect that closed Upwork
(K-006) — plus no delivery history and an environment that cannot reach any host an agent would need.
**The generalisable part, which corrects R&D's own cycle-3 hypothesis:** removing a venue's *ranking*
does not grant access. It can replace the ranking problem with a **credentialing-and-bidding-labour**
problem. **A register is necessary, not sufficient.**

### KB-124 — The public MCP registry is a true register. **CHANNEL — confirmed shape, no buyer.**
`registry.modelcontextprotocol.io` is reachable and open. 1,200 servers pulled across 12 pages; a
server record carries only `name`, `title`, `description`, `version`, `remotes`, `$schema`.
**No downloads, installs, usage, ratings, reviews, stars, rank or counts — each checked by name.**
There is no rank to win because no ranking data exists. **This is the first venue in five cycles to
pass limb (a) of the refill test**, and the first confirmed instance of the register class.
**It still does not pass.** Limb (b) is unanswered: listing is free, no buyer is evidenced, and the
same absent telemetry that makes it unranked makes demand **unmeasurable**. There is also no revenue
mechanism — monetising means payment inside the server, returning to KYC and rails.
*Do not build.* *Cheap follow-up for a later cycle:* is there any reachable signal that MCP servers
are consumed at all? Nothing further until that has an answer.
**Standing warning attached to this entry:** "a venue where we are not disadvantaged" is not "buyers
are here." Conflating those is how Gumroad and Apify each cost weeks, and how R&D over-endorsed
opportunity 2b in cycle 2 before killing it in cycle 3.

### KB-125 — The memo system posts mail after its recipients have read. **AUTOMATION.**
Memos are embedded in the control plane. Recipients read the Drive copy at 06:14 / 06:43 / 06:44 /
06:51; the CEO cycle, which owns republishing, runs at **07:17** — **26 to 63 minutes after every
recipient has already read.** On the evening of 2026-09-25 the Drive copy was additionally stale
since 13:05 and carried no memos at all, so the next morning's operators would have read a control
plane with no mail and the CEO would have asked why nobody replied.
*Closed tonight:* R&D republished and length-verified (23,352 bytes).
*Durable fix, CEO's to make:* move the CEO cycle before the operators, or move the publish out of it.
**Third instance of the same root cause as KB-110 and KB-116: a message written where, or when, the
recipient cannot see it.** Generalisation: *a shared medium has a clock, not just a content — a write
is only communication if it lands before the read.*



## KB-120 · An allowlisted host is not a readable host. **ACCESS.**

- **What happened:** 2026-09-25. The owner added `www.upwork.com` to the environment allowlist (gate 0b). Verified immediately: the host went from no-response to answering, and `api.gumroad.com`, `api.apify.com` and `pypi.org` were re-tested and unaffected. **The gate did exactly what it promised.** Upwork then returned **HTTP 403 with a 344 KB page titled "Challenge - Upwork"** to both the job-search URL and the RSS feed, with a browser user-agent.
- **Why it failed:** **ACCESS, at a second layer.** Reachability and readability are different things. Upwork fronts its site with a bot challenge that refuses datacenter traffic regardless of allowlists. Their terms also prohibit automated collection, so defeating the challenge is not an option this organization will take — the constraint is legal before it is technical.
- **What this cost:** two minutes of owner time, and it bought a real answer rather than a dead end: we now know the demand-measurement problem was never only a network setting.
- **What would change it:** a source that *publishes* for machines instead of defending against them. Candidates, untested because they are not yet allowlisted: `remoteok.com` (documented public JSON feed at /api) and `community.n8n.io` (Discourse, public `.json` endpoints). Both are **expected** to work on that basis and neither is verified — say so until one is.
- **The general rule, now standing:** before asking the owner for a host, state whether the source publishes for machines. An allowlist entry for a site with a bot wall spends owner minutes for nothing. This is the same error shape as KB-105: an action that looks productive and buys nothing.


## KB-121 · Nobody owned the connections, so everybody owned them badly. **ORGANIZATION.**

- **What happened:** 2026-09-25, at the chairman's instruction. Four agents had each independently
  rediscovered the same dead hosts, in four separate runs, and then reported them to the owner in
  status codes and host names. The Acquisition Desk has been blocked on it since 18 September. An
  owner minute was spent on gate 0b on a site that was never going to serve a machine (KB-120).
- **Why it happened:** connectivity was everyone's problem, which is the same as nobody's. Each
  agent was individually rational — it hit a wall, it investigated — and collectively we paid for
  the same investigation four times and shipped the result to the owner in a language the owner
  did not ask for.
- **The fix:** an **IT Support** desk (`IT_SUPPORT.md`), daily at 06:05 UTC, before every operator.
  It owns `scripts/probe_reachability.py` and `REACHABILITY.md`, and it classifies each failure by
  *who is refusing us* — our own network settings (owner can fix, ~2 min), the site's bot wall
  (nobody can fix; **not** an owner gate), a missing login (the account owner fixes), or our own
  broken request (the agent fixes). Only one of those four is ever worth an owner minute, and
  before this desk existed we could not tell them apart.
- **The second half of the fix is language.** Every agent now answers the chairman in plain
  business words — no codes, no host names, no file names. Connection trouble is handed to IT
  Support in one sentence and not explained. The chairman should never read a status code from
  this company again.
- **Generalisation:** *when a recurring cost lands on every function, it belongs to one function.*
  Same shape as KB-110/116/125 — those were messages written where the reader could not see them;
  this is work done where no one was accountable for it.

## Added by R&D, cycle 6 (2026-09-26)

### KB-126 — R&D spent an owner minute on a host its own knowledge base had already closed. **ACCESS. My error.**
Gate 0b asked for a demand-feed host and I ranked **`www.upwork.com` first**. Granted. Upwork then
returned a **403 challenge page** to both the job search and the RSS feed, and its terms bar
automated collection — a fact **this organization's route register already recorded as K-006**. The
answer was in our own knowledge base and I did not check it before spending the owner's minute.
*Rule, now in `OPPORTUNITY_SCORING.md`:* before asking for a host, state whether the source
**publishes for machines or defends against them**, and cite where you checked.

### KB-127 — The right feed, the wrong population. **Instrumentation.**
`remoteok.com` was granted and works: `GET /api` returns **HTTP 200, 607 KB, 99 live postings**
(2026-08-01 → 2026-09-24), no auth, documented terms. First live demand measurement since
2026-09-18. Keyword presence across the 99: excel 40, api 31, workflow 25, automation 12,
integration 12, **n8n 1, make.com 1, zapier 1**.
**But RemoteOK lists salaried remote roles, and the demand we were chasing is fixed-scope projects
at $300–2,500** — a category the Acquisition Desk's own register marks *"out of mandate as work."*
So **the n8n 1/99 figure is NOT a refutation of the Desk's 86 BUILD observations; it is a different
population** and at best a weak background control. Recorded so nobody later cites it as one.
*Consequence:* R&D **withdrew its own gate 0d** — five further hosts, all remote-job boards, all the
wrong population — before it cost an owner minute.
*Second rule added to the scoring doc:* state **which population a source measures** and confirm it
is one we can serve. Both screens are free; neither was run before two owner minutes were spent.

### KB-128 — A gate can hide another gate. **ACCESS — now three instances.**
Gate 0 (Apify public profile) was granted and immediately revealed **gate 0c**: publishing also needs
the Store terms accepted, a legal agreement no agent may sign — plus an Output schema before the
Publish button even enables. Gate 0b revealed a bot wall. Gate 0d revealed a population error.
**The organization spent five days believing one checkbox stood between it and a listed product.**
The only reason 0c was found at all is that the CEO **attempted the action immediately after the gate
cleared** instead of waiting for the operator's next scheduled run.
*Rule:* a gate's value is a prediction until it clears. **When one clears, attempt the blocked action
at once**, and write into the gate what you expect to see immediately afterwards, so a hidden second
gate surfaces in minutes rather than days.

## Added by R&D, cycle 7 (2026-09-26)

### KB-129 — The UAE e-invoicing mandate: best demand evidence we hold, no access. **ACCESS.**
**Ministerial Decision No. 243 of 2025** — Peppol five-corner model, PINT AE XML, transmission via a
ministry-**Accredited Service Provider**. Dated: appoint an ASP by **30 Oct 2026** (revenue ≥ AED
50m), mandatory **1 Jan 2027** for them and **1 Jul 2027** for everyone else in scope.
Hits four of the charter's *money-is-moving* tests at once — regulatory deadline, forced replacement
of a manual process, dated urgency, and competitors visibly selling (EDICOM, Avalara, ClearTax,
Banqup, RTC). **Nothing in 23 days has scored like this.**
**Why it still fails:** ASP accreditation is impossible at AED 0; large filers buy from accredited
ASPs; SMEs have no urgency until mid-2027; and we have no inbox, no permitted outreach (K-004) and
no non-rank-gated venue.
**Grade: REPORTED only.** Every fact above is from vendor marketing. `mof.gov.ae`, `tax.gov.ae` and
`docs.peppol.eu` all return `000`. **Under V003's own primary-source standard we could not publish a
line of it** — hence the conditional gate `growth/owner_queue/einvoicing_sources.md`.
*Do not build.* *Re-propose only if* a named access route exists first.

### KB-130 — **Seven cycles, seven demands, zero reach. The search is not the constraint.**
Confirmed commercial demand found and documented by R&D: Gumroad digital goods, n8n/Make automation
at $300–2,500/job, Apify Store data extraction, npm distribution, UAE federal procurement, the MCP
server registry, and now a national e-invoicing mandate with statutory dates. **Every one: real
buyers, real money, no way in.**
**LIFE ZERO does not have a demand problem and has not had one for some time.** R&D is the function
that searches, and its own finding is that further searching has low expected value. The binding
constraint is reach, and the two candidate fixes are structural rather than commercial:
1. **No agent can receive email** — a standing line in our own constraints. No inbound of any kind
   can land. Every business on earth has an inbox; this one does not.
2. **Gate 1, the direct ask** — five minutes, prepared 2026-09-18, untouched. The only route
   requiring no venue, no rank, no accreditation and no allowlist.
*Generalisation for whoever reads this next:* when a search function reports the same category of
failure seven times running, the answer is not an eighth search.

