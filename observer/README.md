# The Observer Office

**https://claude.ai/artifact/D7owTQn2j6KEvPYkMXwyiN** — the owner's window into LIFE ZERO.

Private to the owner's account. It declares the `db` capability, so it is organization-internal
and cannot be shared by public link.

## The rule this directory exists to enforce

**The visual layer is playful. The data underneath is real.**

No agent maintains this page. Agents write state; the observer reads state. That is the whole
architecture, and it is what stops seven agents fighting over one UI:

```
agents  ->  observer/state.json  ->  build_observer.py  ->  office.html  ->  owner
```

`state.json` is the only file that should change between builds. Editing `office.html` by hand
gets overwritten on the next build; editing `office.template.html` changes the page for good.

## Rebuilding

```
python3 scripts/build_observer.py --check    # validate the state only
python3 scripts/build_observer.py            # validate, then write office.html
```

Then republish `observer/office.html` with the Artifact tool, passing the URL above so it updates
in place instead of creating a second office. The CEO cycle does this daily (step 8).

## The validator is the point

`build_observer.py` refuses to build a state that describes an organization which cannot exist.
It is not a schema check — it is a lie detector, and every rule in it corresponds to a way this
page could quietly mislead the owner:

- an agent claiming revenue the scoreboard does not have
- the scoreboard showing revenue with no customers, or not balancing
- an agent that has never run claiming accomplishments
- an agent shown as BLOCKED with nothing named as blocking it, or the reverse
- a feed event or message attributed to an agent that does not exist
- an agent blocked by a gate that is not on the board
- the agent count disagreeing with the agents actually defined

All seven were verified by injecting each fault and confirming the build fails loudly. A guard
that has only ever seen clean data has not been tested.

**Unmeasured is not zero.** Fields nobody measured are `null` and render as "not measured".
Never write a plausible number into one to make the page look complete — `runs` on the CEO is
null for exactly this reason: routine metadata keeps only the last run, so there is no count.

## Observation is read-only

Opening an agent, or asking it a question, does not pause, redirect or modify anything. The
answer is generated from that agent's record in `state.json` plus the company summary, with an
instruction to refuse rather than invent. It is not roleplay from a job title.

**Owner Command mode is separate and explicit.** It writes to the `commands` collection in the
page's shared store. The CEO cycle reads that collection as step 1 of its daily run, acts, and
writes `status` and a one-line `result` back. A command does not interrupt a running agent — it
is queued, and the page says so.

## What V1 deliberately does not do

- No animation loop. No live socket. The page is a snapshot with an honest timestamp.
- No per-agent push. The CEO refreshes it once a day, or whenever something material happens.
- The Time Machine filters the real event feed by timestamp. It does not reconstruct past state,
  because past state was never stored. A window with no events says so rather than inventing one.
