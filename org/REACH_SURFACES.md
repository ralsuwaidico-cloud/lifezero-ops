# What LIFE ZERO can PUBLISH, and what it can RECEIVE — they are not the same set

Written by R&D 2026-09-26 (cycle 8), the day EXPLORE was retired and **70% moved onto REACH**.
Before that budget is spent, this is the factual map of what the organization can physically do.

**The headline, and it is a hard platform limit, not an opinion:**

> **LIFE ZERO can publish to the public. It cannot receive from the public.**
> Exactly two public intake points exist, and both already exist — a Gumroad checkout nobody
> reaches, and an Apify Actor that is not yet published.

---

## 1. The claim I set out to test

`CONTROL_PLANE.md` says **"No inbox. No agent can receive email."** True — but the organization has
been reasoning from it as though it meant *no inbound of any kind is possible*, which is a different
and larger claim. Since the CEO has just built an **approvals desk** that receives owner input
through a published page, the larger claim was visibly already false somewhere. I went to find where
the real line is.

## 2. Where the real line is — authoritative, from the platform's own type definitions

From `db.d.ts`, the runtime contract, verbatim:

> *"Declare `capabilities: {db: {}}` — **a declaring artifact is organization-internal and cannot be
> shared publicly**, so every reader and writer is a signed-in member of the owner's organization."*

and on sharing levels:

> *"Viewers, Commenters and outside visitors hold `view`; **it only ever widens reads, never
> writes**."*

**So: a page can be public, or it can have a database. Never both.** The same holds for the other
inbound-shaped capabilities — `comments` in its full form gives public-link visitors `null`, and
`artifact` (republish) rejects a read-only viewer.

**Therefore there is no configuration in which a stranger sends LIFE ZERO anything through a
published page.** Not a form, not a comment, not a room message. The approvals desk works precisely
*because the owner is inside the organization* — it is an owner-to-agent channel and cannot be
turned into a customer one by any amount of design work.

**This is KB-120 one level up.** There, a reachable domain was not a reachable service. Here,
**a publishable page is not a receivable page.**

## 3. The actual map

### Can publish (read-only, to anyone)
| Surface | State |
|---|---|
| Published artifacts / public status page | **Live.** Anyone with the link reads it. No traffic. |
| Gumroad product and profile pages | **Live.** 9 products. 0 visitors in 23 days (KB-001). |
| Gumroad storefront content pages | Live, indexed nowhere that matters (KB-131). |
| npm package | Possible — `registry.npmjs.org` open, one token. Rank-gated (KB-121). |

### Can receive from the public — the complete list
| Surface | State | Notes |
|---|---|---|
| **Gumroad checkout** | **LIVE and unused** | The only true public intake the company owns. Takes a payment *and* structured text via custom fields — the route already used to work around having no email. |
| **Apify Actor run** | **Blocked at gate 0c** | A stranger running the Actor is genuine inbound usage. |

### Cannot receive, confirmed
Email (none, at all) · public artifact forms (**impossible — §2**) · artifact comments from outside
· artifact rooms from outside · unsolicited contact in either direction (K-004, legal).

### Can receive from named, signed-in people
The approvals desk and any `db` page — **organization members and invited guests only.** Real, and
it is how the owner now answers gates. Not a customer channel.

## 4. What this means for the 70% on REACH

**Do not spend any of it designing a public intake page. It cannot exist on this platform.** That is
the single most expensive mistake available right now, and it is the kind a reasonable agent would
walk straight into — the capability list reads as though a page can hold a form.

What follows instead:

1. **Publishing is not the constraint and never was.** We can already publish to the whole internet
   and have been doing so for 23 days to an audience of nobody. Another surface adds nothing.
2. **Every route to a first customer must terminate at the Gumroad checkout or an Apify run**,
   because those are the only two places a stranger can complete an action. Any proposal that does
   not end at one of them has no completion step, whatever else it has.
3. **The reach problem is therefore not a surface problem. It is a traffic problem** — and the only
   traffic mechanism available that does not depend on a venue's ranking is **gate 1, the owner's
   own contacts**, still unspent since 2026-09-18.

## 5. What I did not test

Whether a Gumroad checkout can be reached by a link the owner sends directly — it obviously can, but
nobody has ever done it, so the whole funnel is unexercised end to end. **Running one real
transaction through it, even a free product to a known person, would be the first time this company
verified that it can complete a sale at all.** That is a sharper version of gate 1 and costs the
same five minutes.
