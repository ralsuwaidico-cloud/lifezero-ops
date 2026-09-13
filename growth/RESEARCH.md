# LIFE: ZERO — growth research

Evidence behind the Phase 2 experiments. Recorded 2026-09-10.

Most of this came with the owner's Phase 2 directive. Where I checked a claim myself, or found
it wrong, the line says so — an inherited number that nobody re-derived is exactly how the
stale Mercari fee survived in the paid tracker for a week.

## The funnel we are actually in

Three products live, **zero sales, zero ratings**, so the bottleneck is distribution, not the
product. Budget attention ~70% acquisition / 20% offer / 10% product until the first sale.
Diagnose by stage: 0 impressions = distribution; impressions but no clicks = message; clicks
but no sales = offer or trust.

## Gumroad Discover

- Discover effectively excludes products with 0 sales and 0 ratings. A product needs **≥1 sale
  and ≥1 rating** before it surfaces, and Discover-attributed sales are charged at 30%.
- Therefore **the first sale cannot come from Discover.** It has to come from search, a
  storefront page, or a channel the owner posts to.
- Product name is the page title; the **first ~155 characters of the description become the
  Google snippet**; the Summary field is used in listings; tags only matter inside Discover's
  own search. Category "Other" is a graveyard.

## UAE Corporate Tax — a time-boxed wave

- Return and payment are due **9 months after the financial-year end**; for a 31 Dec 2025 year
  end that is **30 September 2026**. About 20 days of search demand left at the time of writing.
- Late filing: AED 500/month for the first 12 months, then AED 1,000/month (Cabinet Decision 75
  of 2023). Late payment: 14%/year on unpaid tax. Never registering when required: AED 10,000.
- **Small Business Relief: revenue ≤ AED 3M, and the window now runs to tax periods ending on or
  before 31 December 2029** — extended from 2026 by Ministerial Decision 131 of 2026, issued
  29 July 2026.
  - *Checked by me on 2026-09-10, because it contradicted our own product.* Confirmed against
    DLA Piper, IFC Review, willow.law and several UAE advisory firms, all naming MD 131/2026.
  - **This made our UAE tracker wrong**, and the fix shipped the same day. See the ledger entry.

## Competitor pricing

The figures below came with the directive and describe **other platforms** (Eloquens, Etsy). On
2026-09-13 I queried Gumroad's own catalogue directly with `gumroad products comps`, which reads
the live Discover index, and the picture on the platform we actually sell on is different:

| Query | Products found | p25 | median | p75 |
|---|---|---|---|---|
| reseller inventory tracker spreadsheet | 5 | $7.99 | **$9.99** | $30.00 |
| custom spreadsheet service | 35 | $4.49 | **$27.00** | $99.25 |
| UAE VAT excel template | **0** | — | — | — |
| corporate tax uae spreadsheet | **0** | — | — | — |

Three things follow:

1. **Our $19 reseller tracker is roughly 2× the category median.** The direct competitor found
   (*Bulk Buy Profit Calculator Spreadsheet*, resaleresources) sells at $9.99; others at $4.99 and
   $8.99. We are not mispriced — we do considerably more — but the listing has to earn that gap in
   the first thing a buyer sees, because on a grid we look like twice the price. No price change
   without traffic data; recorded so the decision is evidence-backed when there is any.
2. **Our $95 service sits at the p75 of 35 comparables** (median $27). In band, at the top of it.
3. **There is not one UAE VAT or Corporate Tax product on Gumroad.** Zero. That cuts both ways:
   nothing competes with our $24 tracker, and nobody has found demand for this on this platform
   either. With a hard filing deadline on 30 September it is still the asset most worth pointing
   urgency at, which is what experiment H does.

**Verified 2026-09-13:** querying `products comps` with our own exact product names —
"Reseller Inventory Profit Tracker 2026", "UAE Freelancer Small Business Bookkeeping Tracker" —
returns **0 results**, while generic queries return up to 20. Our products are genuinely absent
from the Discover catalogue. The "Discover excludes 0-sale products" claim above arrived as an
assertion in the directive; it is now a tested fact, and the strategy that rests on it (the first
sale must come from outside Discover) is correctly founded.

## Marketplace fee rates (feeds both reseller products)

Verified 2026-09-10 against multiple independent secondary sources. **ebay.com and mercari.com
are blocked by this environment's egress proxy**, so these rest on corroborating write-ups, not
the primary fee pages.

| Marketplace | Rate | Checked |
|---|---|---|
| eBay | 13.6% of total incl. buyer-paid shipping + $0.40/order ($0.30 on orders ≤ $10) | 2026-09-10 |
| Poshmark | flat $2.95 under $15, else 20% of sale price; no separate processing fee | 2026-09-10 |
| Mercari | flat 10% on item + buyer-paid shipping (2.9% + $0.50 seller processing removed 6 Jan 2025) | 2026-09-10 |
| Depop | no US selling commission since 2024; 3.3% + $0.45 processing on item + shipping + tax | 2026-09-11 |
| Facebook Marketplace | **10% of the buyer's total, $0.80 minimum**, shipped orders only; local pickup free | 2026-09-11 |

**Correction found 2026-09-11:** Facebook Marketplace raised its shipped-order fee from 5%
(minimum $0.40) to **10% (minimum $0.80) on 15 April 2024**. Our free calculator shipped on
2026-09-10 with the old 5%, understating the fee by half on every Facebook sale — while our own
paid tracker already said 10%. Two products of the same business disagreeing is the same signal
that surfaced the Small Business Relief bug a day earlier. A lot of fee guides still print 5%.

**Correction to the Phase 2 directive:** it gave eBay as "~13.25% + $0.40". That is the older
rate. Current is **13.6% + $0.40**, and the per-order fee is $0.30 at or below $10. Both products
use 13.6%.

## Channels

- **Reddit** (r/Flipping, r/poshmark, r/dubai), UAE Facebook and Telegram groups: promotion is
  against the rules or needs standing in the community. Owner-only, and only where a genuinely
  useful answer is on-topic. Not something to automate.
- **Etsy**: $15 to open a shop. Off the table until there is revenue.
- **Fiverr**: needs owner ID verification (~45 min). Comparable custom-spreadsheet gigs sit at
  **$95–157**, so the $95 service is priced in-band with built-in demand. Highest-EV owner action.
- **LinkedIn**: the CT-deadline post is topical for ~20 days and is the owner's own network.

## High-intent queries

**UAE:** "UAE VAT return excel template freelancer" · "VAT 201 excel template UAE" · "UAE
corporate tax calculator small business relief" · "corporate tax return deadline 30 September
2026" · "freelancer bookkeeping template UAE" · Arabic "جدول اكسل ضريبة القيمة المضافة الإمارات"
· "حاسبة ضريبة الشركات الإمارات".

**Reseller:** "ebay poshmark profit tracker spreadsheet" · "poshmark fee calculator spreadsheet"
· "profit after ebay fees calculator" · "reseller spreadsheet schedule C" · "COGS tracking
thrift flipping".

## Standing rules for this phase

Never spam. Never fake a review. Never post where promotion is prohibited. Never disguise an ad.
A manual channel that makes money beats an autonomous one that makes $0 — but once a channel
works, automate it.
