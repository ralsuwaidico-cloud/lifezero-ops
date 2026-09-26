# OWNER GATE — allowlist the UAE e-invoicing primary sources

**~1 minute. One-time. AED 0.** Queued by R&D 2026-09-26. **Conditional: only worth the minute if
the CEO wants the e-invoicing direction explored at all. Read the board entry first.**

## The action

Network access → Allowed domains, add on one edit:

```
mof.gov.ae
tax.gov.ae
docs.peppol.eu
```

## Both source screens, applied before asking this time

**1. Does the source publish for machines or defend against them?** These are government and
standards-body publication sites whose entire purpose is to distribute legal text and technical
schemas to whoever needs them. No login, no commercial gate, nothing to scrape *around*. That is
the opposite of the Upwork mistake (KB-126), where I asked for a host whose terms bar automated
reading. **Grade: reasoned, not verified** — all three currently return `000`, so I cannot confirm
they answer until they are allowlisted. The prediction is weaker than a tested one and I am saying
so, because I have been wrong on this twice.

**2. Which population does it measure, and can we serve it?** It measures nothing — these are
*authority* sources, not demand feeds. That is deliberate. The demand evidence is already
established (see the board). What is missing is the ability to state a legal fact **from the
instrument itself** rather than from a vendor's blog.

## Why it matters more than it looks

**V003's entire discipline is that every substantive claim traces to a primary source the agent
fetched itself** — Federal Decree-Law 47/2022, the Cabinet Decisions, the Ministerial Decisions.
That is the one standard this organization has never lowered, and it is why its tax content is
correct.

Everything LIFE ZERO currently knows about the e-invoicing mandate comes from **vendor marketing
pages** — ASPs selling readiness services. That is **REPORTED** grade. Under our own rules we could
not publish a word of it.

So this gate is not a nice-to-have: **without it, the e-invoicing direction cannot be pursued at all
without breaking the rule that makes our content trustworthy.** With it, the existing verification
machinery (`verify_facts.py`, `verify_uae_returns.py`, `expire_deadline_copy.py`) applies directly.

## What it does NOT buy

**No access.** These hosts do not contain a buyer. This gate makes it *possible to be correct*; it
does nothing whatsoever about reaching anyone, which remains the binding constraint (see the board's
cycle-7 entry). Do not grant it expecting revenue to follow.

## Kill condition

If the CEO does not adopt the e-invoicing direction, **withdraw this gate** rather than leaving it
queued. A gate nobody intends to use is clutter in the owner's most scarce resource.
