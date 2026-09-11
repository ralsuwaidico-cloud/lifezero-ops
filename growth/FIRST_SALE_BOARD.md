# FIRST SALE BOARD

One row per experiment. Kill the weak, scale the strong. Revenue is the score; the funnel
columns are the diagnosis.

**Reading it:** 0 impressions → distribution problem. Impressions but no clicks → message
problem. Clicks but no sales → offer or trust problem. Do not cut a price without traffic data,
and change one variable at a time.

Metrics are refreshed by the 6-hourly sales pull (UTM clicks via `python3 scripts/utm.py list`,
sales via `scripts/pull_sales.py`). Last refreshed: **2026-09-11 07:30 UTC** — every funnel number
below is still zero across all 12 channels, 4 products and the CT30 code. Expected: nothing links
to any of these pages yet, and the two channels that would are the owner-queue items.

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
| **Status** | Live — 12 links |
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

## Rejected for now

- **Etsy** — $15 to open a shop. Revisit after the first revenue.
- **Reddit / UAE Facebook and Telegram groups** — promotion is against the rules or needs
  community standing. Only the owner, only where a real answer is on-topic.
- **Paid ads** — no budget, and no conversion data to spend it against.
- **A new spreadsheet product** — the directive is explicit: not until customer or search
  evidence demands one. The free calculator is a distribution move, not a new product line.
