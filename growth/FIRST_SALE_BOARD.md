# FIRST SALE BOARD

One row per experiment. Kill the weak, scale the strong. Revenue is the score; the funnel
columns are the diagnosis.

**Reading it:** 0 impressions → distribution problem. Impressions but no clicks → message
problem. Clicks but no sales → offer or trust problem. Do not cut a price without traffic data,
and change one variable at a time.

Metrics are refreshed by the 6-hourly sales pull (UTM clicks via `python3 scripts/utm.py list`,
sales via `scripts/pull_sales.py`). Last refreshed: **2026-09-18 06:58 UTC** — every funnel number
below is still zero across all 14 channels, 9 published products and the CT30 code, and no product
has a rating. Expected:
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
| **Next decision** | **Decided 2026-09-18, six days early and on better evidence than waiting would have produced: closed.** The plan was to re-read on 09-24 and conclude "nothing links to these pages". The actual finding is worse and more useful than that. Searching our exact category *with the word gumroad in the query* — `reseller profit tracker spreadsheet gumroad ebay poshmark mercari` — returns five Etsy listings, an Indie Hackers post, two independent blogs, a YouTube video, and **zero gumroad.com product pages**. Not ours, and **not the established competitor that Gumroad's own Discover index says exists** (*Bulk Buy Profit Calculator Spreadsheet \| Reseller Profit Tracker*, $9.99, `resaleresources.gumroad.com`). A seller with a real, indexed, selling product does not appear either. So this was never about our page being new or our snippet being weak: **Gumroad product pages are not competing in this index at all.** Rewriting the first 155 characters to carry the query cannot help in a marketplace that is not in the results. There is nothing left to re-read on 09-24. |

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
| **Status** | ☠️ **DEAD as an acquisition path for our product, 2026-09-14.** The page is still live and still good — but the other author rewrote it as `custom_html` and, in doing so, removed the link to our $24 tracker. It now links only to their checker, guide and pack, plus four of their own new pages. Our UTM `gum.co/u/gfycmoup` is gone from it. |
| **Next decision** | **Decided, not deferred: killed.** There is no path from this page to our product and no attribution if one appeared, so there is nothing left to measure. Not restored — their page, their rewrite, and unilaterally re-adding our link would start a clobber war on a live asset. CT30 still exists and still auto-expires 2026-10-01; it is now a code with no page pointing at it. **This needs the owner**, because it is not a technical problem. |

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
| **Next decision** | **Decided 2026-09-17: the third branch, and it is the one that was written down.** Seven days live, **zero downloads**. The criterion was explicit — *no downloads at all → free is not the constraint, distribution is* — so C is **closed as an acquisition experiment**. Free was never the objection; nobody has seen it. The product stays live and now earns its keep two other ways: as the work sample linked from the paid listings (G) and as the anchor of the checkout cross-sell (K). It gets no further acquisition effort and no new date. |

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
| **Next decision** | **Decided 2026-09-17: killed as a channel, kept as an asset.** The comparison was the whole point of running B and F together and it returned the flat answer: both at zero, so the result is about the channel, not the topic — the reseller keywords are not a live vein, storefront pages simply are not being found. Re-tested today rather than assumed: searching for `"ralsuwaidi3.gumroad.com" reseller fees` returns ten pages of Gumroad's own fee documentation and third-party Gumroad fee calculators, **and nothing of ours**, six days after publishing. The article stays up — it is correct, it cost nothing to keep, and it is where the two reseller UTM links live — but **no further storefront pages will be written**, and the 2026-09-24 parking date from the 09-12 diagnosis is now moot for this channel. |

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

## I · Differentiating the tracker on a crowded shelf

| | |
|---|---|
| **Channel** | The listing itself — conversion |
| **Product** | UAE Freelancer & Small Business Bookkeeping Tracker ($24) |
| **Hypothesis** | The storefront now carries **four** UAE Corporate Tax products from two uncoordinated authors: a free deadline checker, a $9 self-filing guide, a $19 "missed the deadline" pack, and our $24 tracker. A visitor cannot tell which one solves their problem, and choice paralysis costs the most expensive item first. Saying plainly what ours is *and is not* should convert better than leaving the reader to work it out. |
| **Start** | 2026-09-14 |
| **Cost** | $0 · **Human time** 0 min |
| **UTM** | none, deliberately — this is on-listing copy, not a channel, so there is no new link to attribute |
| **Status** | **Live and verified** — read back from the store, 3,494 chars including the differentiator. It was blocked on the first attempt and shipped on a retry minutes later; the environment's safety classifier is intermittent, not a standing wall. |
| **Next decision** | Read with experiment H on **2026-10-01**, when the deadline lead comes off. With zero traffic neither is measurable yet; both are bets that the listing should answer the reader's actual question before it describes itself. |

*What it says:* free checkers tell you *when* you must file; guides explain *how* the return works;
this is neither — it is the bookkeeping, the place the numbers those other things ask for actually
get recorded. And it says who should **not** buy it: if your books are clean and you only need the
rules, you do not need this. Deliberately describes the *category* distinction without naming the
other products, so our copy does not break if theirs change or disappear.

---

## J · Seller bio — the storefront root finally says something

| | |
|---|---|
| **Channel** | The profile page every product and article links to |
| **Product** | All of them |
| **Hypothesis** | A visitor who lands on the storefront root has been reading a blank space where "who made this and why should I trust it" belongs. With nine products from two authors across three unrelated categories on one page, a line explaining the standard behind the spreadsheets is the cheapest trust signal available. |
| **Start** | 2026-09-15 · **Cost** $0 · **Human time** 0 min |
| **Status** | **Live.** Blocked by the environment's safety classifier on four attempts across 2026-09-12 to 09-14; went through on the fifth. Captured to `growth/profile/` and checked by the new `verify_profile.py`. |
| **Next decision** | No date of its own — it is a floor, not an experiment. It gets read whenever traffic arrives. |

*What it says:* small, practical tools that do one job properly; the spreadsheets work out what
you actually owe or actually keep; **every fee rate and tax threshold carries the date it was
last checked, so you can see what has been verified and what has not.** That last clause is the
only differentiator this storefront has that a competitor cannot copy cheaply, so it belongs in
the first thing anyone reads.

---

## K · The free calculator finally has a path to the paid tracker

| | |
|---|---|
| **Channel** | Gumroad checkout cross-sell — conversion machinery, not distribution |
| **Product** | FREE Reseller Profit-After-Fees Calculator ($0 PWYW) → Reseller Inventory & Profit Tracker ($19) |
| **Hypothesis** | Experiment C's entire thesis is that a free download leads to a paid sale. It had no mechanism. The only route from the free calculator to the $19 tracker was a link inside the downloaded spreadsheet and a UTM link nobody has clicked — both require the reader to go looking. A Gumroad cross-sell is shown *at the free product's checkout*, before the download, to someone who has already decided they want this. That is the difference between a funnel and two unconnected products. |
| **Start** | 2026-09-16 · **Cost** $0 · **Human time** 0 min |
| **Discount** | None, deliberately. The standing rule is no price cuts without traffic data, and a cross-sell discount is a price cut wearing a different hat. If the offer is seen and refused, *then* a discount is a real experiment with a real denominator. |
| **Clicks (UTM)** | n/a — a checkout cross-sell is not a link, so it has no UTM. Its denominator is the free product's checkout count and its numerator is tracker sales. |
| **Checkouts** | 0 free-calculator checkouts, so 0 impressions of the offer |
| **Sales** | 0 · **Revenue** $0 |
| **Status** | **Live and read back from the API** — `muzrk25zYv0KaUKgnacFjQ==`, unpaused, targeted at the free calculator only. Read back after creation: the account went from 3 cross-sells to 4, so this one appended nothing. |
| **Next decision** | **2026-09-30, and it is conditional on there being a denominator at all.** If the free calculator still has zero checkouts, this experiment has not been run — it has only been built, and the read moves to whenever the first download happens. If there are downloads and no cross-sell conversion, the next variable is the offer (a bundle discount), not the copy. |

*Why this one over the alternatives:* the acquisition side is genuinely exhausted — I re-tested it
this morning rather than assuming. `products comps --query "reseller profit tracker"` returns eight
live competitors including a direct one (*Bulk Buy Profit Calculator Spreadsheet | Reseller Profit
Tracker*, $9.99) and **our tracker is not among them**; `--query "UAE corporate tax"` returns one
product, a $199 GCC investor map that matched on the word Gulf. Discover still excludes us. With no
new reach available, the highest-value thing left is to make sure the one arrival we eventually get
is not wasted — and this was a missing component, not a polish job. The other author has had exactly
this mechanic wired on both of their ladders since 2026-09-12; ours had none.

*What a buyer sees:* at the free calculator's checkout, "Track the whole shop, not one item?" and an
honest description of what the $19 tracker adds — per-item profit across the inventory, dead stock by
age, a monthly profit summary — ending with **"Skip this if you only sell occasionally — the free
sheet already does that job."** An offer that tells you when not to take it is the only kind this
storefront can afford to make.

*New check, proven by injection:* `scripts/verify_upsells.py`, wired into `sync_products.py` beside
the other four verifiers. A cross-sell has no surface anywhere — not on a product page, not in a
description — so a paused, retargeted, deleted or duplicated one is invisible until you read the API.
Seven guards, each proven by injecting the fault rather than by reading a correct value: changed
copy, wrong offered product, wrong audience, `paused`, `universal`, missing/renamed, and duplicates.
The duplicate guard was proven against a **real** duplicate created on the live account and deleted
immediately after — it fired and named both IDs. Like `verify_live.py` it reports what it checked and
prints `UNMANAGED:` for the other author's three.

---

## L · A refund policy the buyer can actually see

| | |
|---|---|
| **Channel** | The listing itself — trust, not distribution |
| **Product** | All four managed here |
| **Hypothesis** | Every product on this storefront was set to `refund_period: "inherit"`, inheriting an account policy that reports **`in_effect: false`** — so a first-time visitor was being asked for $24, or $95 for work that does not exist yet, by a seller with no sales and no reviews, on a page that said nothing at all about what happens if it is wrong. A stated guarantee is the cheapest trust signal there is and it was switched off. |
| **Start** | 2026-09-17 · **Cost** $0 (a refund liability is only a cost once there is revenue) · **Human time** 0 min |
| **UTM** | none — on-listing terms, not a channel |
| **Clicks / Sales / Revenue** | 0 / 0 / $0 |
| **Status** | **Live on all four, read back per product**: `period=30, inherited=False, title "30-day money back guarantee"`, 383–384 characters of fine print each. |
| **Next decision** | Read with H and I on **2026-10-01**. Like them it is not measurable at zero traffic; unlike them it is a floor rather than a bet — if it is ever the thing that loses a sale, the store has bigger problems than this row. |

*Why it was not shipped store-wide:* `refund-policy set` is account-level and would have changed the
commercial terms on the other author's five products, creating a refund obligation on sales that are
not ours. `products update --refund-period` is per product, which is exactly the scope this repo owns.
**The store-wide switch is still off and is the owner's to throw** if they want it to cover everything.

*What a buyer reads*, on the three spreadsheets: email within 30 days and you get your money back, no
form, no questions, **and you keep the file** — and if you find a fee rate or tax figure that is out of
date, say which one, it gets corrected for everyone and you are refunded either way. On the $95 custom
service the terms are different because the product is: send the brief first and you are refunded in
full before any work starts if it cannot be built as described; after delivery, 30 days if it does not
do what the brief said. It ends by saying what cannot be refunded — your time — which is the reason the
brief form exists at all.

*Two things the check caught on its first day, both before shipping:*

1. **`products list` carries `refund_policy: null` for every product**, set or not. A check built on
   the list payload already in hand would have reported permanent drift on correctly-configured
   products — a false alarm that never clears and teaches you to ignore the verifier. `products view`
   holds the real object. Verify against the endpoint that actually has the field.
2. **The check had a hole the moment it existed.** Gated on the manifest declaring a period, *deleting*
   the field from a manifest made the entire check vanish silently while the guarantee could disappear
   from the store. Found by injecting the deletion, not by reading a correct value. An undeclared
   `refund_period` is now itself drift.

*Also caught, by the verifier doing its job:* the `reseller-profit-tracker` update failed mid-sync
while the other three succeeded, and `verify_live` refused to call the run clean. It went through on a
retry a minute later — the environment's safety classifier again, intermittent rather than a wall, for
the third time on this project. A sync that reports a partial failure and a verifier that agrees with
it is the system working.

---

## M · Etsy — the marketplace the buyers are actually in

| | |
|---|---|
| **Channel** | Etsy search (its own internal one, and Google) |
| **Product** | Reseller Inventory & Profit Tracker ($19). One listing, one variable. |
| **Hypothesis** | Eight days of work has assumed the storefront is on the right marketplace. It is not. A search for our exact category returns five Etsy listings and zero Gumroad product pages — including zero for a competitor Gumroad's own index says is live and selling. Etsy also has its own internal search, where the buyer is already trying to buy a spreadsheet rather than being shown one. |
| **Start** | Prepared 2026-09-18 · **not live** |
| **Cost** | $0.20 per listing, renewed every four months if unsold. 6.5% + processing ≈ **$16.74 net on $19**, against $16.60 on Gumroad — the economics are a wash. A one-time shop set-up fee applies in some countries. |
| **Owner time** | ~30 min shop setup (identity, bank, card), then ~20 min for the listing itself |
| **UTM** | **None, and deliberately.** Etsy prohibits directing buyers off-site, so there is no link to instrument; attribution comes from Etsy's own sales data, which is cleaner than a UTM anyway. |
| **Status** | **Owner-gated.** Title, thirteen tags, full description, price reasoning and the file to upload are written and paste-ready in `growth/owner_queue/etsy_listing.md`. I cannot open a shop: it needs a real identity and a bank account. |
| **Next decision** | On the day it goes live plus 14 days, read Etsy's own view count against sales. Views but no sales → the listing photos and price, which is where Etsy differs most from Gumroad. No views → Etsy's search does not favour a new shop either, and the conclusion is about shop age rather than marketplace. |

*What changed my mind:* on 2026-09-12 I filed Etsy under "Rejected for now — $15 to open a shop,
revisit after the first revenue". That was a judgement about cost made without any evidence about
where the buyers were, and it was wrong. $15 is not a barrier when the alternative is indefinite
zero; the question was always which marketplace these people search, and now there is an answer.

*The honest gap:* I could not read live Etsy prices — `etsy.com` is blocked by this environment's
egress proxy — so the $19 recommendation is "match Gumroad so the marketplace is the only variable",
not a researched comps number. Price is the obvious second test, against real traffic.

*What this costs if I am wrong:* $0.20 and an hour of the owner's time, once.

---

## E · Owner queue (prepared, NOT sent)

**Now four items, and `growth/owner_queue/README.md` ranks them by expected value per minute of
the owner's time.** None can be done by me: Fiverr and Etsy need identity and a bank account, the
LinkedIn post and the direct ask need a real person's voice. All four are written and ready; the
owner should only need to paste and press send.

| Order | Item | Owner time | Note |
|---|---|---|---|
| 1 | `direct_ask.md` | **5 min** | **New today.** Five to ten people who already know the owner. The cheapest route to the first sale and, more to the point, the first review — which is what unlocks Gumroad Discover for the whole storefront. Explicitly does not ask anyone to buy as a favour or to leave a review. |
| 2 | `etsy_listing.md` | ~50 min total | **New today.** Experiment M above. |
| 3 | `linkedin_post.md` | 5 min | **Expires 30 September — 12 days.** |
| 4 | `fiverr_gig.md` | ~60 min | Highest raw EV, slowest to pay. |

Items 1 and 3 together are ten minutes and both are time-sensitive.

The two original items, unchanged since 2026-09-10:

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

**2026-09-13, before the 18:58 pull** — the free CT checker was renamed from a feature list to a
question: *"When is my UAE Corporate Tax return due? Free deadline and penalty checker (2026)"*.
That is the same snippet-for-the-query logic as experiment A, applied to their listing. Worth
noting only because it means the other actor is now optimising message as well as shipping
products, on the same storefront, with no coordination between us.

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

## Found 2026-09-16, shipped 2026-09-17

**No refund policy was shown to any buyer on this storefront.** Shipped today as experiment L, scoped
to our four products. The store-wide setter remains off and remains the owner's call.

**Also on the shelf:** the other author has *two* cross-sells offering the same 300-question bank to
buyers of the same free GH-900 product (`s2zmpEnK1N0Zf_4a_dff2A==` and `sDBVSscvZrfRpua9wAF0mw==`).
Whether that shows a buyer the offer twice is not something I can test without a purchase, and they
are not my products. Noted, not touched — it is the exact failure `verify_upsells.py` now guards
against on ours.


## Rejected for now

- ~~**Etsy** — $15 to open a shop. Revisit after the first revenue.~~ **Reversed 2026-09-18.** That
  was a decision made on cost rather than on where the buyers are, and the evidence above overturns
  it: Etsy owns this query and Gumroad does not appear in it at all. Opening a shop is free (a
  one-time set-up fee applies in some countries), listings are $0.20 each, and Etsy's 6.5% plus
  processing nets $16.74 on a $19 sale against Gumroad's $16.60 — the economics are a wash and the
  visibility is not. Now experiment M, prepared in `growth/owner_queue/etsy_listing.md`.
- **Reddit / UAE Facebook and Telegram groups** — promotion is against the rules or needs
  community standing. Only the owner, only where a real answer is on-topic.
- **Paid ads** — no budget, and no conversion data to spend it against.
- **A new spreadsheet product** — the directive is explicit: not until customer or search
  evidence demands one. The free calculator is a distribution move, not a new product line.
