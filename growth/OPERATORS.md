# Who else is running LIFE: ZERO

> **Superseded in part, 2026-09-24.** The owner's R&D directive reorganised this. The portfolio
> view now lives in `../org/CONTROL_PLANE.md`; the failures in `../org/KNOWLEDGE_BASE.md`. Two
> roles were created that are not in the table below: **CEO / Capital Allocator** (this persistent
> session) and an independent **R&D agent** (`session_01BFRuz1vq1KBRVPgRzsDz6N`, persistent, every
> 6h at :27). The Gumroad routines were demoted — 6-hourly pull → daily maintenance, daily growth
> → CEO cycle. This file remains the reference for who owns which asset and where agents collide.

**Written 2026-09-24, after finding out that the "other author" is not a person.**

For two weeks this repo has described an unnamed "other actor" on the shared Gumroad account,
escalated "who owns what between two uncoordinated authors" to the owner as a governance question,
and treated it as unanswerable from here. It was answerable from here the whole time.
`list_triggers` returns **ten routines on this account, six of them live LIFE ZERO operators**.
The other author is two of them.

I had that tool from the first day. On 2026-09-19 I used it to audit my own scheduled one-shots
and passed `recurring: false` — which filtered out **every single one of these**, because they are
all cron routines. The narrative I built on top of that gap was careful, well-hedged and wrong
about the one fact that mattered.

---

## The roster

| Operator | Routine | Runs | Session | Since | What it owns |
|---|---|---|---|---|---|
| **This one** (founder-operator) | `trig_01ABomHe9Zx2SftMc5NtHnGz` (pull) + `trig_014SCnUoGy8uTScFdyN6NqgC` (growth) | every 6h at :58, daily 07:17 | **persistent** — one continuous conversation | 2026-09-04 | The four products in `products/`, `growth/pages/reseller-fees-2026`, the seller profile, the free→paid cross-sell, `data/facts.json`, every verifier, CT30 |
| **EmaraTax Ready** (was "V003" — codes retired 2026-09-25) | `trig_011WKjfGcsgKsfjPyHtLQUHu` | daily 06:43 | fresh each fire | 2026-09-11 | The UAE CT deadline **page**, the free deadline checker, the $9 self-filing guide, the $19 "missed the deadline" pack. **This is the "other author" of 2026-09-10 to 09-14.** |
| **GH-Cert Drills** (was "V008" — codes retired 2026-09-25) | `trig_01YQNReiBPzxBXtzEjKzYPjq` | daily 06:44 | fresh each fire | 2026-09-11 | GH-900 Free 50, and the 300-question GitHub Foundations bank |
| **Acquisition Desk** | `trig_016mi2S1e7a7WtDjFLoRGi4e` | every 6h at :51 | fresh each fire | 2026-09-12 | Explicitly builds nothing. "Your entire job is finding buyers and getting an offer in front of them." Working Mahir UAE and Apify. |
| **Apify operator** | `trig_01RgJbe9SM2z1thn2m22QH2i` | every 6h at :14 | fresh each fire | 2026-09-19 | The Apify Store channel end to end. Has its own `APIFY_TOKEN`. Targeting n8n/Make automation at $300–2,500 a job. |
| **IT Support** | `trig_01Ba5YktF9MVHNV7PZVuRtbj` | daily 06:05 | fresh each fire | 2026-09-25 | Every connection problem in the company. Owns `org/IT_SUPPORT.md`, `org/REACHABILITY.md`, `scripts/probe_reachability.py`. Runs before every operator so they start the day knowing what is open. No Drive tools (KB-104) — reads the repo via git. |
| Gumroad publish run | `trig_01WegGwCQVHTVHqHmUhuEjmz` | fire-only, no schedule | fresh | 2026-09-04 | Legacy bootstrap worker. Has not run since 2026-09-04. |
| SNN daily production | `trig_01AV4HXAFLEUgBVFTg7iAcfA` | **disabled** since 2026-09-15 | fresh | 2026-08-21 | A short-form video channel. Not running. |

---

## What this explains, and what it changes

**It explains the entire "not mine" section of the board.** The CT deadline page appearing at
13:42 on 09-10; the UAE ladder on 09-11; the GH-900 vertical on 09-12; the rename to a
question-format title on 09-13 using the same snippet-for-the-query logic as my own experiment A
(same reasoning, same training); the custom_html rewrite on 09-14; the "Internal build archive
(not for sale)" drafts, which are a fresh-session agent parking build artefacts where it can find
them again, because unlike me it has **no repo and no memory between runs**.

**It does not change the 2026-09-14 decision to leave their page alone** — but it sharpens the
reason. I declined to restore our link because it would start a clobber war on a live asset. That
was right, and it is now more obviously right: V003 fires every six hours from a blank slate. An
edit war between two agents on a 6-hour cycle would run indefinitely with neither side remembering
the previous round.

**It corrects a claim I have made in almost every report.** I have written "I have no unblocked
acquisition lever" for twelve days. That was true *of me* and I will keep saying it in that form —
but a dedicated **Acquisition Desk has been running four times a day since 09-12**, and I did not
know. What I could not see is not the same as what does not exist.

---

## The coupling nobody designed

These are the places where two agents touch the same object with no lock and no shared state.

1. **One Gumroad account, four tokens' worth of write access.** Every trap this repo has
   documented — `products list` paginating at 10, `--file` and `--cover-image` appending rather
   than replacing, `custom-fields create` having no idempotency key — is a trap that two agents
   can spring on each other, not just on themselves.
2. **CT30 is mine and lives on V003's page.** Their page names the code; it no longer links our
   tracker. When the 2026-10-01 one-shot deletes the code to honour our own stated expiry, their
   page will carry a dead reference. They will not know why.
3. **`sync_products.py` adopts by permalink.** If V003 or V008 ever created a product using one of
   our four permalinks, my sync would adopt it and push our manifest over it. The pagination guard
   protects against duplication; nothing protects against collision.
4. **Draft products in the shared list.** "Internal build archive" sits one click from published
   on a live storefront. It is invisible to buyers today.
5. **No shared state at all.** None of them can read this repo. I cannot read their working notes.
   Every one of them re-derives the situation from its prompt on every fire.

---

## What is the owner's to decide, stated properly this time

The old escalation asked "who owns what on a Gumroad account with two uncoordinated authors",
which was the wrong question because it assumed a colleague. The real one:

**Six autonomous operators share one Gumroad account, one storefront and one brand, with no shared
state and no coordination mechanism. Is that the intent?** If it is, the account needs a written
division — which permalinks, which pages, which categories belong to whom — because at the moment
the only thing preventing a collision is that we happen not to have overlapped yet. If it is not,
some of these should be consolidated or stopped.

**I have not touched any other operator's routine, products or pages, and I will not.** The one
exception is defensive and within my own remit: on 2026-09-24 I rewrote **my own** CT30 one-shot,
which still carried an instruction from 09-10 to PUT our retired copy of the CT page over the live
one. Left alone it would have destroyed 7,949 characters of V003's current work on 1 October. That
is the concrete cost of not knowing who else is here, and it was seven days from happening.
