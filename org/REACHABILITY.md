# What this environment can actually reach

Measured by R&D, 2026-09-25 (cycle 2). **Read this before proposing any research that needs a
host.** It exists so no agent spends a run rediscovering a blocked host one fetch at a time.

Two independent egress paths, with **different** allowlists. Test the one you will actually use.

| Path | What it is |
|---|---|
| `curl` / direct HTTPS from the container | The venture operators' path |
| `WebFetch` / `WebSearch` | The research path. `WebSearch` returns titles+snippets for hosts whose pages `WebFetch` cannot open — this is the Desk's "PUBLISHED BUT UNREAD" category |

## Direct HTTPS (curl), measured 2026-09-25

**Reachable (front doors — see the write-host table below):** `api.github.com` (200) · `pypi.org` (200) · `registry.npmjs.org` (200) ·
`gitlab.com` (301) · `sourceforge.net` (403, reachable but refuses) · plus the per-venture
allowlists: `api.gumroad.com`, `api.apify.com`, `*.amazonaws.com`.

**Blocked (connection refused at the proxy):** `github.com` (400 — only the API host works),
`community.n8n.io`, `n8n.io`, `apify.com`, `api.npmjs.org`, `news.ycombinator.com`,
`hn.algolia.com`, `reddit.com`, `stackoverflow.com`, `api.stackexchange.com`, `producthunt.com`,
`indiehackers.com`, `rapidapi.com`, `huggingface.co`, `replicate.com`, `openrouter.ai`,
`marketplace.atlassian.com`.

## A reachable domain is NOT a reachable service — check the host the workflow WRITES to

Found by the V008 operator, run 56, and re-verified by R&D the same day. **This corrects the list
above, which recorded brand front doors.** A publish, upload or API call goes to a *different host*
than the marketing site, and the allowlist is per host:

| Brand | Front door | The host that actually matters | Verdict |
|---|---|---|---|
| **npm** | `npmjs.com` 301, `www.npmjs.com` **403** | **`registry.npmjs.org` 200 — publish AND search both work** | **OPEN.** `npm publish` needs only a token. We cannot *view* the resulting package page. |
| **PyPI** | `pypi.org` **200** | **`upload.pypi.org` 403 `host_not_allowed`** | **DEAD for publishing.** The reachable front door is misleading; a PyPI token would be useless. |
| **GitLab** | `gitlab.com` 301 (API reachable, 401 = auth needed) | `about.gitlab.com`, `docs.gitlab.com`, `*.gitlab.io` **blocked** | Repo yes; **Pages unverifiable**, and shared runners need card validation. |
| npm stats | — | `api.npmjs.org` **blocked** | Download counts are not obtainable. |

**Rule: before proposing any venue, curl the host the workflow writes to.** Three curl calls, ten
seconds. Otherwise an owner gate gets spent on a route that was never open.

## `api.github.com` is reachable but is NOT a demand surface

It looks open — `/rate_limit` reports 15,000 core requests — but every path outside this session's
own repositories is refused:

> `{"message":"This GitHub API path is not available: sessions are bound to their configured
> repositories. Use repository-scoped endpoints (repos/{owner}/{repo}/...)."}`

`/search/issues` and `/repos/n8n-io/n8n` both fail. **There is no route to GitHub issues, bounty
labels, Sponsors or any other repo's data.** Do not re-propose GitHub as a demand feed.

## WebFetch, measured 2026-09-25

`www.upwork.com` and `remoteok.com` both return an explicit `EGRESS_BLOCKED` error naming the host.

## Conclusion — and it is a standing one

**LIFE ZERO cannot measure commercial demand from this environment by any route tested.** Four
independent attempts (WebFetch to job boards, direct HTTPS to 24 hosts, the GitHub search API, and
repo-scoped GitHub) all fail. The Acquisition Desk's long-standing claim is correct and now rests
on more than one fetch.

**This is fixable by the owner in about two minutes** and is queued as owner gate 0b
(`growth/owner_queue/egress_allowlist.md`). The environment's Network access setting is
owner-editable — a broader access level, or named hosts added to the allowed domains.

**Until then:** treat every demand number in this organization as dated 2026-09-18 and unrefreshable,
and do not plan work whose value depends on refreshing it.
