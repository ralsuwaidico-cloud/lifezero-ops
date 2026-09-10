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

- UAE VAT Excel tools sell at **$49–83** (Eloquens, excelaccountingtemplate). Free VAT 201 sheets
  rank well (ExcelDataPro, MSOfficeGeek, Daftra). Nothing found combines VAT + Corporate Tax +
  freelancer bookkeeping at a low price — that is our gap, and our $24 sits under everyone.
- Reseller sheets clear on Etsy at **$10–20** (TheSpreadsheetGuys $9.99 with 4.8k sales;
  AllThingsResale $20.19). The free email-gated sheets (Hustle & Slow, Sheetrix) have no
  per-platform fee maths and no tax summary — which is precisely what our free calculator gives
  away, so it competes on the one axis they are weak on.

## Marketplace fee rates (feeds both reseller products)

Verified 2026-09-10 against multiple independent secondary sources. **ebay.com and mercari.com
are blocked by this environment's egress proxy**, so these rest on corroborating write-ups, not
the primary fee pages.

| Marketplace | Rate | Checked |
|---|---|---|
| eBay | 13.6% of total incl. buyer-paid shipping + $0.40/order ($0.30 on orders ≤ $10) | 2026-09-10 |
| Poshmark | flat $2.95 under $15, else 20% of sale price; no separate processing fee | 2026-09-10 |
| Mercari | flat 10% on item + buyer-paid shipping (2.9% + $0.50 seller processing removed 6 Jan 2025) | 2026-09-10 |
| Depop | US selling fee moved to buyer; ~3.3% + $0.45 processing remains | not re-verified |
| Facebook Marketplace | ~5% on shipped orders, ~$0.40 minimum | not re-verified |

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
