# FIRST SALE BOARD

One row per experiment. Kill the weak, scale the strong. Revenue is the score; the funnel
columns are the diagnosis.

**Reading it:** 0 impressions → distribution problem. Impressions but no clicks → message
problem. Clicks but no sales → offer or trust problem. Do not cut a price without traffic data,
and change one variable at a time.

Metrics are refreshed by the 6-hourly sales pull (UTM clicks via `python3 scripts/utm.py list`,
sales via `scripts/pull_sales.py`). Last refreshed: **2026-09-13 07:40 UTC** — every funnel number
below is still zero across all 14 channels, 8 published products and the CT30 code. Expected:
nothing links to any of these pages yet, and the two channels that would are the owner-queue
items. Only four of those products are managed from this repo — see "Not mine" at the foot.

---

## A · Gumroad SEO / Discover hygiene

| | |
|---|---|
| **Channel** | Organic search (Google snippet) + Gumroad Discover |
| **Product** | All four |
| **Hypothesis** | The listings were invisible because the first 155 characters read like brand copy rather than the query, and the tags were near-duplicates. Naming the search term in the snippet is the cheapest possible acquisition change. |
| **Start** | 2026-09-10 |
| **Cost** | $0 |
| **Human time** | 0 min |
| **Impressions** | — (Gumroad exposes no impression count; proxy is UTM clicks + sales) |
| **Clicks (UTM)** | 0 |
| **Checkouts** | 0 |
| **Sales** | 0 |
| **Revenue** | $0 |
| **Status** | Shipped |
| **Next decision** | Google needs 1–3 weeks to re-crawl. Re-read on **2026-09-24**. If still zero, the problem is not the snippet — it is that nothing links to these pages, and effort moves to the owner-queue channels. |

*What changed:* all three paid listings rewritten so the first sentence carries the query
("A UAE VAT return (VAT 201) and Corporate Tax estimate…", "See your profit after eBay,
Poshmark, Mercari, Depop and Whatnot fees…"), summaries rewritten, tags cut from 8–10
near-duplicates to 5 real queries each, one Arabic keyword sentence plus "$24 ≈ AED 88" added to
the UAE listing. Category was already `business-and-money/accounting`, not "Other" — the
directive's assumption was out of date, so no move was needed. Category is now declared in each
manifest and checked by `verify_live.py`.

---

## B · UAE Corporate Tax deadline page + CT30

| | |
|---|---|
| **Channel** | Gumroad storefront page → UAE tracker |
| **Product** | UAE Freelancer & Small Business Bookkeeping Tracker ($24) |
| **Hypothesis** | A genuinely useful, correct page about a deadline 20 days out earns the click that a product page cannot. The discount converts the reader who came for information. |
| **Start** | 2026-09-10 |
| **Cost** | $0 (30% margin on any CT30 sale: $24 → $16.80) |
| **Human time** | 0 min |
| **Impressions** | — |
| **Clicks (UTM)** | 0 · `https://gum.co/u/gfycmoup` |
| **Checkouts** | 0 |
| **Sales** | 0 · CT30 `times_used` = 0 |
| **Revenue** | $0 |
| **Status** | Live — <https://ralsuwaidi3.gumroad.com/ct-deadline-2026> |
| **Next decision** | Check CT30 `times_used` and page clicks on **2026-09-17**. Zero clicks with the deadline this close means nothing is linking to the page, which is an argument for the LinkedIn post in the owner queue, not for rewriting the page. CT30 auto-expires 2026-10-01 (scheduled). |

*Note:* the page and four UTM links already existed when the directive arrived (created
13:42–13:43 UTC). I verified the page, corrected its Small Business Relief section's relationship
to our product, and added the CT30 paragraph. The page's HTML now lives in
`growth/pages/ct-deadline-2026.html` as the source of truth.

---

## C · Free reseller profit-after-fees calculator

| | |
|---|---|
| **Channel** | Gumroad Discover + organic search, free download |
| **Product** | New: FREE Reseller Profit-After-Fees Calculator 2026 → upsells the $19 tracker |
| **Hypothesis** | Discover will not show a product with 0 sales and 0 ratings. A free download that is genuinely good is the cheapest route to the first sale *and* the first rating, which is what unlocks Discover for the paid tracker behind it. |
| **Start** | 2026-09-10 |
| **Cost** | $0 |
| **Human time** | 0 min |
| **Impressions** | — |
| **Clicks (UTM)** | 0 · upsell link `https://gum.co/u/ysjnz0ld` |
| **Checkouts** | 0 downloads |
| **Sales** | 0 (pay-what-you-want, $0 floor, $5 suggested) |
| **Revenue** | $0 |
| **Status** | Live — <https://ralsuwaidi3.gumroad.com/l/reseller-fee-calculator> |
| **Next decision** | Downloads and ratings on **2026-09-17**. Downloads but no upsell clicks → the in-file CTA is too quiet. Downloads *and* a rating → the paid tracker should start appearing in Discover; check that directly. No downloads at all → free is not the constraint, distribution is. |

*What it is:* one item typed once, priced across eBay, Poshmark, Mercari, Depop and Facebook
Marketplace side by side, with the best marketplace named and losses flagged red; a 20-row batch
sheet; and an editable fee table where each row carries the date it was last checked. The fee
maths is pinned by a build-time assertion against hand-worked rates, including the three tier
edges (eBay's $0.30/$0.40 per-order split at $10, Poshmark's $2.95→20% cliff at $15, Facebook's
$0.40 minimum).

---

## D · UTM links per channel

| | |
|---|---|
| **Channel** | Instrumentation, not a channel |
| **Product** | All |
| **Hypothesis** | Without per-channel clicks, every future result is unattributable and the funnel cannot be diagnosed. |
| **Start** | 2026-09-10 |
| **Cost / human time** | $0 / 0 min |
| **Status** | Live — 14 links |
| **Next decision** | Reviewed every 6 hours by the sales-pull routine. |

| Link | Channel → target | Clicks |
|---|---|---|
| `https://gum.co/u/gfycmoup` | CT deadline page → UAE tracker | 0 |
| `https://gum.co/u/sxsym2tr` | LinkedIn CT post → UAE tracker | 0 |
| `https://gum.co/u/tr0smurx` | Reddit CT deadline → UAE tracker | 0 |
| `https://gum.co/u/sgiv9yc6` | WhatsApp/Telegram groups → UAE tracker | 0 |
| `https://gum.co/u/glgzmwqt` | Gumroad profile → UAE tracker | 0 |
| `https://gum.co/u/rg6exxu1` | Gumroad profile → reseller tracker | 0 |
| `https://gum.co/u/f3qxwgwu` | Reddit r/Flipping → reseller tracker | 0 |
| `https://gum.co/u/ysjnz0ld` | Free calculator upsell → reseller tracker | 0 |
| `https://gum.co/u/byva53km` | LinkedIn → custom sheet service | 0 |
| `https://gum.co/u/opzpsbc2` | Fiverr gig → custom sheet service | 0 |
| `https://gum.co/u/cq0pgrpj` | Reseller fees page → free calculator | 0 |
| `https://gum.co/u/qsqbak1m` | Reseller fees page → paid tracker | 0 |
| `https://gum.co/u/8si9vikr` | Reseller tracker page → free calculator | 0 |
| `https://gum.co/u/wwdxkqkm` | Custom sheet service → free calculator (work sample) | 0 |

---

## F · Reseller marketplace-fee reference page

| | |
|---|---|
| **Channel** | Gumroad storefront page → free calculator + $19 tracker |
| **Product** | Both reseller products |
| **Hypothesis** | Experiment B bet that a useful, correct article on an indexable storefront page earns clicks a product page cannot. This is the same bet aimed at a much larger keyword pool — "poshmark fee calculator spreadsheet", "profit after ebay fees calculator" — and at the free product, where a download and a rating are what unlock Discover for the $19 tracker behind it. |
| **Start** | 2026-09-11 |
| **Cost** | $0 |
| **Human time** | 0 min |
| **Impressions** | — |
| **Clicks (UTM)** | 0 · free calculator `https://gum.co/u/cq0pgrpj` · tracker `https://gum.co/u/qsqbak1m` |
| **Checkouts** | 0 |
| **Sales** | 0 |
| **Revenue** | $0 |
| **Status** | Live — <https://ralsuwaidi3.gumroad.com/reseller-fees-2026> |
| **Next decision** | Read alongside experiment B on **2026-09-17**. B and F are the same channel with different topics and audiences, so compare them: if both are at zero, the storefront-page channel is not being indexed and the conclusion is about distribution, not topic. If F moves and B does not, the reseller keywords are the live vein and the UAE effort should follow the CT deadline out on 30 September rather than being renewed. |

*Why this one over the alternatives:* the funnel is zero at every stage on every channel, which is a
distribution reading — there is nothing to diagnose about message or offer until something is
being seen. Of the things I can do without the owner, an indexable page targeting queries people
actually type is the only one that creates new reach rather than polishing existing reach. It also
pairs with B to turn "does the storefront-page channel work at all?" into an answerable question
instead of a single data point.

*What it is:* the real fee structure of all five marketplaces with what each one charges against,
four traps worked out in numbers (fee charged on buyer-paid shipping; Poshmark's 29.5% effective
rate under $12; Facebook's April 2024 doubling; Depop's commission moving to the buyer), and the
same $45 item priced across all five showing a $7.07 profit spread. Soft CTA to the free
calculator, then the tracker.

---

## G · Storefront coherence and the free calculator as a work sample

| | |
|---|---|
| **Channel** | On-site conversion, not acquisition |
| **Product** | All four managed here |
| **Hypothesis** | Four products sat as four unconnected pages: a visitor landing on one could not see the others, and a $95 custom service with zero reviews was asking for trust it had not earned. Linking the free calculator from the paid pages turns it into a work sample — download it, judge the quality, then decide — and gives every arrival somewhere free to go. |
| **Start** | 2026-09-12 |
| **Cost** | $0 · **Human time** 0 min |
| **Clicks (UTM)** | 0 · tracker → free calc `https://gum.co/u/8si9vikr` · service → free calc `https://gum.co/u/wwdxkqkm` |
| **Sales** | 0 · **Revenue** $0 |
| **Status** | Live on all four listings, verified |
| **Next decision** | This cannot be read before there is traffic, so it has no date of its own. When the first arrivals land, the two cross-sell links say whether the free calculator is doing trust work or is just another link. |

*Why this one:* not because it is the best idea available, but because **it is the best idea still
available to me.** See the diagnosis below.

*What changed:* the $19 tracker and the $95 service now both offer the free calculator as
something you can download and judge before paying; the UAE tracker points at the free CT-deadline
explainer and says "read that first, buy this only if the bookkeeping is what is standing in your
way"; the free calculator points at the fees article. Four pages became a shop.

---

## Diagnosis, 2026-09-12: the page channel is not indexed, and my acquisition levers are spent

Searching Google for our exact page title — *"UAE Corporate Tax deadline 30 Sept 2026: checklist
+ penalty math"* — returns ten established consultancies and law firms and **not our page**.
Searching for the storefront domain returns nothing of ours either. Two days in, nothing we have
published is findable.

Two conclusions, and the second is the uncomfortable one:

1. **Experiments B and F are assets, not channels.** A storefront page earns traffic only when
   something links to it. Google may still index them — 1–3 weeks is normal, and experiment A's
   re-read date of 2026-09-24 stands — but the keyword field is crowded with domain-authority
   sites, and a three-day-old Gumroad subdomain will not outrank DLA Piper on UAE tax. I should
   stop building more pages on the expectation that they will rank. **Parked, not killed:** no
   further page effort until 2026-09-24 shows whether anything indexes at all.
2. **I have no unblocked acquisition lever left.** Everything I can reach without the owner —
   listing SEO, storefront pages, a free lead magnet, instrumentation, now cross-linking — is
   shipped and sitting at zero. Gumroad Discover needs ≥1 sale and ≥1 rating, and the free
   calculator would provide both, but it needs one visitor first. Every remaining route to that
   first visitor runs through a person: Fiverr needs ID verification, LinkedIn needs a real
   account and voice, the communities need standing. That is not a reason to stop working, but
   it is the honest shape of the problem, and today's experiment is conversion work precisely
   because the acquisition side is exhausted rather than because it is the higher-value half.

**The critical path is now the owner queue, and half of it expires.** The LinkedIn CT-deadline
post is worthless after 30 September — 18 days. Both items have been ready since 2026-09-10.

---

## H · Deadline urgency on the UAE listing

| | |
|---|---|
| **Channel** | The listing itself — message, not distribution |
| **Product** | UAE Freelancer & Small Business Bookkeeping Tracker ($24) |
| **Hypothesis** | Two facts make this the one listing worth changing today. `gumroad products comps` returns **zero** UAE VAT or Corporate Tax products in the whole Gumroad catalogue, so nothing competes with it; and its buyer has a hard statutory deadline on 30 September. A description that opens with a date the reader is already worried about converts better than one that opens with a description of a spreadsheet. |
| **Start** | 2026-09-13 · **Cost** $0 · **Human time** 0 min |
| **Clicks (UTM)** | 0 · **Sales** 0 · **Revenue** $0 · CT30 `times_used` 0 |
| **Status** | Live and verified — first 155 chars now read *"UAE Corporate Tax is due 30 September 2026. Log your invoices and expenses once and this fills in your VAT 201 boxes and your Corporate Tax estimate."* Summary changed to match. |
| **Next decision** | **2026-10-01, and it is a removal, not a read.** The claim expires with the deadline; a one-shot is scheduled to strip it and restore the evergreen lead. Any signal before then is a bonus — with zero traffic this is not expected to be readable, and it is not the reason for shipping it. |

*Why now rather than at experiment A's 2026-09-24 read:* this does contaminate A's read for one of
four products, and normally that would be a reason to wait. It is not, because the asset expires
on 30 September. Optimising a deadline product eleven days after you could have is worse than a
slightly muddied experiment, and A's other three listings still give a clean read.

*Note on evidence:* the pricing paragraph in RESEARCH.md that this replaces described Eloquens and
Etsy — other platforms. Queried against Gumroad's own catalogue the numbers are different, and
recorded there in full: our $19 tracker is ~2× the $9.99 category median (not mispriced, but the
listing must earn the gap), and our $95 service sits at the p75 of 35 comparables.

---

## E · Owner queue (prepared, NOT sent)

Neither of these can be done by me: Fiverr needs the owner's ID verification, and the LinkedIn
post has to come from a real person's account and voice. Both are written and ready in
`growth/owner_queue/`; the owner should only need to press Post.

| | Fiverr gig | LinkedIn CT-deadline post |
|---|---|---|
| **File** | `growth/owner_queue/fiverr_gig.md` | `growth/owner_queue/linkedin_post.md` |
| **Owner time** | ~45 min ID verification + ~15 min setup | ~5 min |
| **Cost** | $0 to list (Fiverr takes 20% of each order) | $0 |
| **Expected value** | **~$150–300 in 30 days.** Comparable gigs clear $95–157; Fiverr's own search demand is the point. A conservative 2–4 orders/month at $95 net of the 20% fee is $152–304. Highest-EV action available to anyone right now. | **~$25–75, plus real signal.** ~40 relevant UAE connections × a 3–8% click rate → 1–3 clicks per 100 impressions; at a 3–5% conversion on a $24 product this is 0–1 sales. Its real value is the first genuine impression data we would have. |
| **Risk** | 20% platform fee; a first order with no reviews takes time to arrive. | Posting on a deadline topic is normal LinkedIn behaviour and is not spam — but it must be the owner's own words and account. |
| **Status** | Awaiting owner | Awaiting owner |

---

## Not mine: the account now holds nine products, five of them not from this repo

Another actor is building on this Gumroad account. It appeared first on 2026-09-10 at 13:42 (the
CT-deadline page and four UTM links), then twice more:

**2026-09-11, between the 12:58 and 18:58 pulls** — a UAE Corporate Tax ladder:

| Product | Price | Permalink | Category | Content |
|---|---|---|---|---|
| UAE Corporate Tax Return 2026 — self-filing guide | $9 | `uae-ct-return-guide` | **`other`** | 3 file embeds |
| UAE Corporate Tax Deadline & Penalty Checker 2026 | $0 PWYW | `uae-ct-deadline-checker` | `business-and-money/accounting` | 2 file embeds |

**2026-09-12, before the 00:58 pull** — an entirely new vertical, GitHub certification prep:

| Product | Price | Permalink | Category |
|---|---|---|---|
| GH-900 Practice Questions — Free 50, with explanations + offline quiz app | $0 | `gh900-free-50` | `education/test-prep` |
| GH-Cert Drills — 300 GitHub Foundations (GH-900) practice questions | $9 | `gh-900-practice-questions` | `education/test-prep` |
| Internal build archive (not for sale) | $0 | — | `other` · **unpublished draft** |

**2026-09-12, before the 18:58 pull** — a second draft of the same kind: *Internal build archive 2
— checker (not for sale)*, unpublished. Parking build artefacts as draft products is now a
pattern rather than a one-off, which is worth naming: nothing reaches buyers, but the product
list is becoming a scratch directory and a mis-click publishes whatever is in one.

All the published ones deliver content, so no buyer is paying for nothing. Both ladders use the
same free → $9 shape, which is a reasonable structure and the same one I would have built.

Two things worth the owner's attention rather than mine. First, **the business is now two
unrelated verticals** — spreadsheets and certification prep — and my Phase 2 directive ("no new
products unless customer or search evidence demands it, 70% of attention on acquisition") was
written for one. Whether that directive binds the other actor is not something I can decide.
Second, **the draft "Internal build archive" sits one click from published** on a live storefront.
It is invisible to buyers today. I have not opened it and will not, but a thing named that should
probably not live in a product list at all.

**I have not touched any of them, and I am not going to without being asked.** Two things
follow from that, and both matter more than the products themselves:

1. **Something else writes to this account.** The CT-deadline page and the first four UTM links
   also appeared from outside this session, on 2026-09-10 at 13:42. My routines were written
   assuming sole ownership of the store. They are not: `sync_products.py` adopts by permalink and
   pushes manifest state, and if two actors both "fix" the same product we get the duplicate-cover
   mess of 2026-09-09 again, but concurrent. Worth the owner deciding who owns what before either
   of us touches the other's listings.
2. **Nothing verifies them.** They have no manifest, so `verify_live.py` never looked at them —
   and its success line used to count every live product, so it cheerfully reported "6 product(s)
   match their manifests" when it had checked 4. Fixed today: it now reports manifests checked and
   prints an `UNMANAGED:` line for every live product this repo does not cover.

One observation offered rather than acted on: the $9 guide sits in category **`other`**, which our
own research file calls a Discover graveyard, while its free sibling is correctly in
`business-and-money/accounting`. That is a one-field change worth roughly whatever Discover
traffic is worth — but it is somebody else's product.

---

## Rejected for now

- **Etsy** — $15 to open a shop. Revisit after the first revenue.
- **Reddit / UAE Facebook and Telegram groups** — promotion is against the rules or needs
  community standing. Only the owner, only where a real answer is on-topic.
- **Paid ads** — no budget, and no conversion data to spend it against.
- **A new spreadsheet product** — the directive is explicit: not until customer or search
  evidence demands one. The free calculator is a distribution move, not a new product line.
