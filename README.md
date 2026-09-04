# lifezero-ops — autonomous store operations
Private ops repo for the LIFE: ZERO store. `products/<slug>/product.json` is the source of truth; pushing to `main` syncs Gumroad (create/update/publish) via GitHub Actions. `sales.yml` pulls sales every 6 h into `data/`. Never commit buyer PII (emails are hashed).
