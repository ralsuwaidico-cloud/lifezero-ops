# AUTONOMY_LEDGER

| # | Task | Why human was required | Time | Recurring? | Eliminable? | Automation solution | Status |
|---|------|------------------------|------|-----------|-------------|---------------------|--------|
| 1 | Create Gumroad account + payout KYC | Account ownership, identity/banking verification | ~10 min | One-time | No (legal gate) | — | DONE (Rashed, Day 1) |
| 2 | Upload 3 listings to Gumroad by hand | My mistake: treated "sandbox can't reach Gumroad" as "human must do it" | — | Would have recurred per product | YES | GitHub Actions runner (open egress) runs `gumroad` CLI from `products/*/product.json`; idempotent sync on every push | REPLACED — request withdrawn, route closed |
| 3 | Grant API credentials once: GitHub PAT + Gumroad access token | Account-owner permission grant (allowed category) | ~3 min | One-time | Converts every future upload/price change/sales read to zero-human | Secrets stored in GitHub Actions; all later operations automated | PENDING — see #4 |
| 4 | Set a real `GUMROAD_ACCESS_TOKEN` on the cloud environment | Credential issuance is an account-owner act; the current value is placeholder text, so every call 401s | ~3 min | One-time | No (legal/ownership gate), but it is the *only* remaining human step | Once set, the 6-hourly routine publishes all three products unattended on its next run; `sync_products.py` is idempotent so it cannot duplicate | DONE (2026-09-08) — store live |
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

2026-09-08 — STORE IS LIVE. Token became valid; all three products published on the first
authenticated cycle, unattended. Two things surfaced that the dry run could not:
(1) Gumroad rejects a non-square thumbnail ("Please upload a square thumbnail"), so the 16:9 cover
could not double as one — build_all.py now generates real 1000x1000 tiles and the manifests carry
a `thumbnail` field. (2) That failed create still made the products server-side while returning
success:false, so the account held three half-configured products with no state files. Adoption by
permalink prevented duplicates exactly as designed, but it recorded the current hash and reported
"unchanged", which would have left them permanently missing their thumbnails. Fixed: adoption now
records hash=None so an adopted product is always re-synced, and the update branch pushes
cover/thumbnail too. Verified by deleting state/ and re-running: all three re-synced clean.
Lesson: a failed API call is not proof that nothing happened — check the remote state, not the
exit code.

Item 4 (set a real GUMROAD_ACCESS_TOKEN) is now DONE. No human step remains.

2026-09-08 (2) — The $95 service was live with NO content attached: the buyer paid and received
only an instruction to email. Gumroad rejected an update on exactly that policy ("This product has
no content attached and directs buyers to message you on another platform"), which was a fair
call. Fixed properly rather than by rewording: built a Project Brief & Intake Pack (.xlsx) that the
buyer downloads at purchase — a nine-question brief, a data-sample tab, and a how-it-works page —
and reframed the listing around it. The pack also earns its keep operationally: a structured brief
is what stops a round-trip eating the 48 hours. Also made the 48-hour clock explicit as starting
when the brief arrives, not at checkout, which protects both sides.

Automated: `scripts/verify_live.py` checks what is actually live on Gumroad against each manifest
(published, price, cover, thumbnail, and file embeds) and `sync_products.py` now runs it after
every real sync. This exists because "success" has now twice hidden a partial sync — a create that
returned success:false had already made the products, and an update that returned success:true
left the service with no content while its description promised a download. The list endpoint's
`file_info` is useless for this (empty for a product whose content is a file embed), so the check
reads `products content get`. Proven to fire: injecting a wrong price and a phantom second file
made it report both and exit non-zero.

2026-09-09 — Found and fixed a mess I made. `products update --cover-image` APPENDS a gallery
cover rather than replacing one, and sync_products.py pushed it on every update, so all three
listings were showing the same image three times on their storefronts. Removed the six duplicates
(`covers remove` needs `--yes`), took cover pushing out of the update path entirely, and gave the
gallery its own owner: `scripts/sync_covers.py` counts what is live before adding anything, so a
second run is a no-op. Same append-not-replace trap as `--file`; that is now two features with it,
so treat "does this append or replace?" as the first question about any Gumroad write.

Also: two product updates failed on an over-length tag (must be under 20 characters) and
`verify_live.py` still reported everything matching, because it was not checking tags. It now
checks tags and gallery cover counts as well. Proven by injection. The lesson repeats — a verifier
only catches the fields it actually looks at, so every new field pushed to the store needs a
matching check the same day.
