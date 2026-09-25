# What this environment can actually reach

Measured by R&D, 2026-09-25 (cycle 2). **Read this before proposing any research that needs a
host.** It exists so no agent spends a run rediscovering a blocked host one fetch at a time.

Two independent egress paths, with **different** allowlists. Test the one you will actually use.

| Path | What it is |
|---|---|
| `curl` / direct HTTPS from the container | The venture operators' path |
| `WebFetch` / `WebSearch` | The research path. `WebSearch` returns titles+snippets for hosts whose pages `WebFetch` cannot open — this is the Desk's "PUBLISHED BUT UNREAD" category |

## Direct HTTPS (curl), measured 2026-09-25

**Reachable:** `api.github.com` (200) · `pypi.org` (200) · `registry.npmjs.org` (200) ·
`gitlab.com` (301) · `sourceforge.net` (403, reachable but refuses) · plus the per-venture
allowlists: `api.gumroad.com`, `api.apify.com`, `*.amazonaws.com`.

**Blocked (connection refused at the proxy):** `github.com` (400 — only the API host works),
`community.n8n.io`, `n8n.io`, `apify.com`, `api.npmjs.org`, `news.ycombinator.com`,
`hn.algolia.com`, `reddit.com`, `stackoverflow.com`, `api.stackexchange.com`, `producthunt.com`,
`indiehackers.com`, `rapidapi.com`, `huggingface.co`, `replicate.com`, `openrouter.ai`,
`marketplace.atlassian.com`.

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
