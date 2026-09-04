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
