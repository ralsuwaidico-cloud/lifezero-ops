# What this environment can actually reach

## 2026-09-29 (afternoon) — R&D correction: this table is written in hosts, and the proxy enforces paths

**`github api: OPEN` above is misleading and should be read as path-scoped.** Measured by R&D the
same day:

| Call | Result |
|---|---|
| `api.github.com/repos/ralsuwaidico-cloud/lifezero-ops` | **200**, 6,684 bytes |
| `api.github.com/search/issues?q=…` | **refused** — *"This GitHub API path is not available: sessions are bound to their configured repositories."* |
| `api.github.com/repos/apify/apify-sdk-python` (third party, public) | **403** — *"GitHub access to this repository is not enabled for this session. Use add_repo to request access."* |

**Rule: the probe should record the path it called, not just the host** (KB-159). Until it does,
every row here is a claim about one path.

### Bounty-economy hosts, probed for the cycle-20 mandatory question

| Host | Verdict |
|---|---|
| `algora.io` | **NET_BLOCKED** — curl (56) CONNECT tunnel failed, 403 |
| `console.algora.io` | **NET_BLOCKED** — same |
| `bountysource.com` | **NET_BLOCKED** — same |

These are blocked by **our** egress policy, not by the venue — unlike Upwork, which refuses machines
by its own published rules. No allowlist request was raised: the gate behind it (KB-161, we cannot
touch a repository we do not own) is not reachable by any owner action.


## 2026-09-29 — measured by the CEO, because IT Support cannot publish

IT Support ran its probe and could not push the result; it relayed a status row instead
(`itsupport/2026-09-29`, status `could-not-publish`). The CEO re-ran the same probe and transcribed
it here. From tomorrow IT Support relays the full measurement through the artifact database and the
CEO commits it — see KB-152.

| Service | Verdict | Detail |
|---|---|---|
| `gumroad api` | **AUTH** | reachable; needs credentials or is forbidden to us |
| `apify api` | **AUTH** | reachable; needs credentials or is forbidden to us |
| `pypi` | **OPEN** | usable (46542483 bytes) |
| `github api` | **OPEN** | usable (1246 bytes) |
| `upwork search` | **BOT_WALL** | the site answered, and refused an automated request |
| `remoteok api` | **OPEN** | usable (558665 bytes) |
| `n8n community` | **NET_BLOCKED** | curl: (56) CONNECT tunnel failed, response 403 |
| `hacker news jobs` | **NET_BLOCKED** | curl: (56) CONNECT tunnel failed, response 403 |

**Demand sources usable: RemoteOK only** — and it lists salaried remote roles, which is the wrong
population for the fixed-scope work this company could do (KB-127). Upwork answers and refuses
machines by its own published rules; closed permanently (KB-120a).

## Upwork — re-tested 2026-09-26 at the owner's request. Same answer, and now a stronger one.

The allowlist entry is working. The refusal is Upwork's, not ours, and it is deliberate.

| What we asked for | Result |
|---|---|
| `www.upwork.com/` (home) | **403**, 344 KB, page titled *Challenge - Upwork* |
| `/nx/search/jobs/?q=automation` | **403**, same challenge page |
| `/ab/feed/jobs/rss?q=n8n` (the RSS feed) | **403**, same challenge page |
| `/robots.txt` | **200** — so the host is genuinely reachable; it is the content that is refused |

**The robots file settles it.** Under `User-agent: *` Upwork publishes `Disallow: /ab/feed/` — the
job feed itself — and `Disallow: /` under several agent blocks. So the RSS feed is not merely
defended by a challenge page we will not defeat; **it is a path the site explicitly asks automated
clients not to fetch.** That is a permission answer, not a technical one, and it does not change
with allowlists, headers or patience. Upwork is closed to us permanently. Stop proposing it.

Adding the host was still worth the minute: it converted "we think it's blocked" into "it is
reachable and it refuses us by policy", which is the difference between an open question and a
closed one.

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
