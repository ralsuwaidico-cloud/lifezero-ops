# AUTONOMY_LEDGER

| # | Task | Why human was required | Time | Recurring? | Eliminable? | Automation solution | Status |
|---|------|------------------------|------|-----------|-------------|---------------------|--------|
| 1 | Create Gumroad account + payout KYC | Account ownership, identity/banking verification | ~10 min | One-time | No (legal gate) | — | DONE (Rashed, Day 1) |
| 2 | Upload 3 listings to Gumroad by hand | My mistake: treated "sandbox can't reach Gumroad" as "human must do it" | — | Would have recurred per product | YES | GitHub Actions runner (open egress) runs `gumroad` CLI from `products/*/product.json`; idempotent sync on every push | REPLACED — request withdrawn, route closed |
| 3 | Grant API credentials once: GitHub PAT + Gumroad access token | Account-owner permission grant (allowed category) | ~3 min | One-time | Converts every future upload/price change/sales read to zero-human | Secrets stored in GitHub Actions; all later operations automated | PENDING — see #4 |
| 4 | Set a real `GUMROAD_ACCESS_TOKEN` on the cloud environment | Credential issuance is an account-owner act; the current value is placeholder text, so every call 401s | ~3 min | One-time | No (legal/ownership gate), but it is the *only* remaining human step | Once set, the 6-hourly routine publishes all three products unattended on its next run; `sync_products.py` is idempotent so it cannot duplicate | PENDING (2026-09-04) |
| 5 | Repair the build container (openpyxl, Pillow, libreoffice-calc, pdftoppm) | Runbook assumed these were present; `libreoffice-calc` was absent, so LibreOffice could not open any .xlsx and `recalc.py` reported a misleading timeout | ~25 min | Would recur on every fresh container | YES | Fixes documented in `lifezero_run_log.md` and referenced from both routines; fold into a session-start hook or image if it recurs a third time | DONE (2026-09-04) |

Standing rule: every operational request must pass the Autonomy Engineer check (API? integration? script? other agent? other platform? one-time auth instead?) before it reaches Rashed. Second occurrence of any manual task → flag for automation; third → requires written justification here.

Sandbox egress facts: only github.com/api.github.com and package registries are reachable. GitHub Actions is the bridge to every other service.

2026-09-06 — The reseller Dashboard computed Net Profit as `Shipping Net − Overhead` instead of
`Item Profit − Overhead`, reporting a loss on a profitable year. It recalculated with 0 formula
errors throughout, so the existing build gate could never have caught it; the workbook's own
"should equal line 15" cross-check row was printed for the buyer but never verified by anything.
Automated: `build/build_all.py` now asserts Tax Summary line 15 equals the Dashboard total on
every build. Lesson for the daily cycle — "0 formula errors" proves the sheet computes, not that
it computes the right thing. Any figure the workbook claims reconciles needs a build-time
assertion, not a promise in a label.

2026-09-07 — Same silent-drop class as the reseller fee bug, but on a tax filing. Every VAT Return
box matches an exact treatment string, so an unrecognised value in Income!G (a pasted "Standard",
a typo, a renamed Settings entry) charged no VAT AND matched no box: the invoice vanished from the
return. Measured on the sample book, one bad string on a 12,000 AED invoice took net VAT payable
from AED 630 to AED 30 — a 95% understatement — with 0 formula errors throughout. Added two CHECK
rows to the VAT Return, red-flagged the offending cell on Income/Expenses, and asserted both checks
at build time. Method that found it and is now standing practice: do not confirm a guard by reading
0 on clean data — inject the bad value, recalculate, and watch the number move. Both guards were
proven to fire before shipping.
