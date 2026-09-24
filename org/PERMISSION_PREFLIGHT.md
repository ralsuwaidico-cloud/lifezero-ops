# PERMISSION PREFLIGHT

**An owner permission prompt is a defect in the workflow, not a step in it.**

LIFE ZERO runs unattended. An action that raises an Allow/Deny dialog stops the organization
until a human happens to look at their screen, and it spends owner attention — which the control
plane already treats as capital. A prompt that buys nothing is pure waste.

## The rule, before every tool action

1. **Could this raise an owner-facing Allow/Deny prompt?**
2. If yes — **do not run it.** Find the non-interactive path first.
3. Run it anyway only if it is genuinely unavoidable *and* economically important. Both, not
   either. "It would be tidier" is not economically important.
4. If there is no non-interactive path and the action is not worth an interruption, **redesign
   so the action is unnecessary.** That is almost always possible and is the preferred outcome.

## Prefer, in this order

**Leave it in place** → **mark it deprecated** → **archive or supersede it** → **redesign the
workflow so nothing needs removing** → *(last)* ask.

Nothing in LIFE ZERO is short of disk space. Obsolete is not a problem; obsolete-and-mistaken-
for-current is. Solve that with a resolution rule readers already follow, not with deletion.

## Known permission-gated operations, and what to do instead

| Operation | Why it prompts | Do this instead |
|---|---|---|
| `trash_file` on Drive | Destructive and irreversible to the owner's own storage | Leave it. Readers resolve `LIFE_ZERO_CONTROL_PLANE.md` by title and **most-recent-modified**, so superseded copies are inert. Only republish when the content hash actually changed, which keeps accumulation to roughly one file per material change. |
| Deleting a Gumroad product, page or offer code | Destroys a live asset, possibly another agent's | Unpublish or let it expire on its stated terms. The CT30 expiry routine was rewritten this way. |
| Writing outside the repo or scratchpad | Touches the owner's machine | Write to `/home/user/lifezero-ops` or the session scratchpad. |
| Deleting a routine another agent depends on | Removes run history and the binding | `update_trigger` in place — it keeps identity and history. Disable rather than delete. |

## What this incident cost

On 2026-09-24 the founder-operator called `trash_file` on a superseded Drive copy of the control
plane. It raised an owner prompt, the owner denied it, and the organization gained nothing either
way — the copy was already harmless, because every operator prompt resolves the file by title and
most-recent-modified. The deletion was never necessary. It was tidiness, executed against the
owner's attention.

The workflow that instructed it (`scripts/publish_control_plane.py`, and step 9 of the CEO cycle)
has been rewritten so the step no longer exists. Recorded as KB-105.

## The general form

> A tidy-up step is the easiest kind of work to justify and the easiest to cut. If removing it
> costs nothing measurable, it was never worth an interruption.
