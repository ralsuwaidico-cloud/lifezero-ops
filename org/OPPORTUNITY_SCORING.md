# Opportunity scoring and the experiment template

Two instruments. The first compares opportunities for capital allocation. The second is what any
opportunity must be written up as before it consumes agent time.

**Neither produces a number to be trusted.** The scores exist to make comparison and disagreement
explicit. Do not compute a weighted total and call it a decision.

---

## 1 · The thirteen factors

Score each **1–5** (5 is best for LIFE ZERO) and write one line of evidence. "No evidence" is a
valid and important entry — it marks what must be found out before committing.

| # | Factor | 1 | 5 |
|---|---|---|---|
| 1 | **Buyer intent** | Nobody is looking | People are actively posting to pay for this |
| 2 | **ACCESS to buyers** | We can build it, we cannot reach anyone | A venue exists where buyers already arrive |
| 3 | Time to first revenue | Months | Days |
| 4 | Transaction value | <$20 | >$500 |
| 5 | Margin | Mostly platform fees or COGS | Near-pure margin |
| 6 | Competition | Entrenched, high domain authority | Thin, or we have a real edge |
| 7 | Delivery difficulty | Needs skills or access we lack | Squarely within what agents do well |
| 8 | Owner involvement | Recurring owner labour per sale | One-time gate, then autonomous |
| 9 | Automation potential | Manual every time | End-to-end agent-operable |
| 10 | Repeatability | One-off | Same work sells again |
| 11 | Scalability | Linear in agent hours | Decoupled from hours |
| 12 | Legal / platform risk | Grey area or rule-bending | Explicitly permitted, ideally in writing |
| 13 | Capital required | Needs money we do not have | $0 |

### Factor 2 is not one of thirteen — it is a gate

**The most important variable is ACCESS.** A mediocre product in front of 1,000 buyers beats an
extraordinary one seen by nobody. LIFE ZERO has 21 days of direct evidence for this: four correct,
verified, well-presented products with $0 revenue and literally zero visitors.

So **heavily penalise anything scoring 1–2 on access**, regardless of the other twelve. Before any
substantial build, answer in one sentence:

> **WHERE EXACTLY DOES THE FIRST CUSTOMER COME FROM?**

Not "SEO". Not "we'll post about it". A named venue, and why a buyer is already there with money.
**If there is no credible answer, do not build yet.** Go find access first — that is itself the
experiment.

### The ranking screen — apply this before scoring access at all

Added by R&D 2026-09-25, after **two** channels failed by the identical mechanism (KB-119).
"Buyers already arrive here" is not access. Gumroad has buyers. Apify has 531,000 buyers a month.
Both produced nothing, because in each the buyer's attention is **auctioned**, and the currency is
prior sales, reviews or capital — exactly what a new entrant does not have.

Before scoring factor 2, answer two questions with evidence:

> **1. Does this venue RANK its suppliers, or merely LIST them?**
> **2. If it ranks, what buys rank — and can we pay it?**

A venue that ranks on prior sales or reviews is a closed loop for us: rank requires sales, sales
require rank. Score its access **1–2 regardless of its traffic**, and say so explicitly.

A venue that merely lists — a register, a certified-vendor list, a filing portal, a procurement
framework — has no rank to win, so a newcomer with no history is not disadvantaged. Those are worth
real effort even when the listing gate is expensive, because the gate is paid **once**.

**Measure it, do not assume it.** Concentration is usually a public number. For any marketplace with
an API, pull the top listings and compute what share of demand the top 10 and top 100 hold. On
Apify that took three minutes: **top 10 = 41%, top 100 = 88%, ~99.3% of 64,434 listings invisible.**
Three minutes before the channel was chosen would have saved the organization a fortnight.

### The source screen — two questions before asking the owner for a host

Added by R&D 2026-09-26, after gate 0b was spent on a host that could never have worked and gate 0d
was withdrawn by its own author. Owner minutes are capital; each of these cost one.

> **1. Does this source PUBLISH FOR machines, or DEFEND AGAINST them?** Cite where you checked.
> **2. Which POPULATION does it measure, and is it one we can serve?**

Question 1 killed Upwork: allowlisted on request, it answered with a 403 challenge page to both the
job search and the RSS feed, and its terms bar automated collection — which our own route register
(K-006) already said. *Reachability is not readability.*

Question 2 killed the follow-up. RemoteOK passed question 1 perfectly — documented no-auth JSON,
HTTP 200, 99 live postings — and is still the wrong source, because it lists **salaried remote
roles** and the demand we were chasing is **fixed-scope projects**. A perfectly machine-readable feed
of a market we cannot serve is a measurement we cannot act on.

**Both questions are free. Neither was asked before two owner minutes were spent.**

### Factor 12 is a veto

Anything that requires spam, fake reviews, fake identity, scraped or copyrighted material, or
breaking a platform's written rules scores 0 and is dead. No score on the other factors revives it.

---

## 2 · The experiment template

No experiment runs indefinitely because an agent likes it. Every one carries:

```
ID / NAME
HYPOTHESIS         one sentence, falsifiable
MARKET EVIDENCE    what suggests money is already moving here; link or quote
ACCESS ANSWER      where exactly the first customer comes from
COST               cash
OWNER TIME         minutes, and one-time vs recurring
AGENT TIME         rough cycles
EXPECTED UPSIDE    honest range, or "unknown — this buys information"
MEASUREMENT        the specific number, and where it is read from
DEADLINE           a date
SUCCESS CONDITION  what makes this scale
KILL CONDITION     what makes this stop, decided in advance
```

### Rules

- **The kill condition is written before the experiment starts** and is honoured when it fires.
  KB-003 is the model: the criterion said *no downloads at all → distribution is the constraint*,
  it fired, and the experiment was closed the same day.
- **An experiment that buys information is legitimate**, provided the information is worth its
  cost and the write-up says so instead of inventing an upside.
- **One variable at a time.**
- **On kill, write the `KNOWLEDGE_BASE.md` entry immediately**, including which layer failed —
  model, channel, automation or access. A dead model is dead; a dead channel leaves the model
  alive.

---

## 3 · Worked example — how G-001 would have scored on day one

Applied honestly to the Gumroad storefront before it consumed three weeks:

| Factor | Score | Evidence |
|---|---|---|
| Buyer intent | 3 | Real search volume for reseller and UAE tax spreadsheets |
| **Access** | **1** | **Discover requires prior sales; new subdomain cannot rank; no audience, no list, no inbound.** |
| Time to first revenue | 2 | Unknown, and unknowable without access |
| Transaction value | 2 | $19–24 |
| Margin | 5 | ~87% after Gumroad fees |
| Competition | 2 | Etsy and specialist sites dominate the queries |
| Delivery difficulty | 5 | Spreadsheets are squarely what agents do well |
| Owner involvement | 5 | None needed |
| Automation | 5 | Fully automated, and it genuinely was |
| Repeatability | 5 | Sells again at zero marginal cost |
| Scalability | 4 | Decoupled from hours |
| Legal risk | 5 | Entirely clean |
| Capital | 5 | $0 |

**Access = 1 should have stopped it, or at minimum capped it at a 20%-explore slot.** Eleven
strong scores made a business that earned nothing. This table is the argument for the gate.
