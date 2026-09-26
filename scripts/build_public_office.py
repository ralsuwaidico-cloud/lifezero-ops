#!/usr/bin/env python3
"""Build the PUBLIC LIFE ZERO office page from the same shared state.

Public means world-readable: anyone with the URL. So this deliberately publishes
a SUBSET and the filter is the point of the file.

  PUBLISHED : the money scoreboard, the agents with their live status, current
              task, last/next run, and the activity feed.
  WITHHELD  : strategy and allocation, owner-gate detail, the knowledge base,
              the graveyard, agent-to-agent messages, and the problem list.

The private office at claude.ai keeps all of it. This page says plainly that it
is partial, so nobody mistakes it for the whole picture.

    python3 scripts/build_public_office.py
"""

import html
import io
import json
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE = os.path.join(REPO, "observer", "state.json")
OUT = os.path.join(REPO, "observer", "public", "index.html")
OUT_ARTIFACT = os.path.join(REPO, "observer", "public", "office_public.html")

# Fields copied to the public page. Anything not listed here never leaves.
AGENT_PUBLIC = ["id", "display", "role", "room", "status", "avatar",
                "current_task", "schedule", "last_run", "next_run", "last_result"]

# A field-level allowlist does NOT make a field safe: strategy can be written inside
# an allowed free-text field. `public_task` overrides `current_task` on the public
# page when an agent's real task would say too much, and SENSITIVE is the backstop --
# the build FAILS rather than publishing a page containing any of these.
SENSITIVE = [
    "refill test", "exploit slot", "% exploit", "70% bet", "70/20/10",
    "kill condition", "owner gate", "gate 0", "gate 0b", "KB-1", "INC-0",
    "public profile", "public-profile", "egress allowlist", "sunk cost",
    "power law", "R&D board", "concentration", "allocation to zero",
]

STATUS = {
    "WORKING": ("var(--working)", "Working"),
    "RESEARCHING": ("var(--researching)", "Researching"),
    "WAITING": ("var(--waiting)", "Waiting"),
    "BLOCKED": ("var(--blocked)", "Blocked"),
    "ERROR": ("var(--error)", "Error"),
    "IDLE": ("var(--idle)", "Idle"),
    "REVENUE": ("var(--money)", "Revenue"),
}

AVATAR = {
    "ceo": '<rect x="13" y="7" width="16" height="4" rx="1.4" fill="{c}"/>'
           '<path d="M15 7l2-3h8l2 3z" fill="{c}" opacity=".55"/>',
    "rnd": '<circle cx="31" cy="12" r="5.2" fill="none" stroke="{c}" stroke-width="1.8"/>'
           '<path d="M34.6 15.6L38 19" stroke="{c}" stroke-width="1.8" stroke-linecap="round"/>',
    "builder": '<rect x="6" y="30" width="30" height="3" rx="1.4" fill="{c}" opacity=".45"/>'
               '<rect x="12" y="24" width="18" height="6" rx="1.2" fill="none" stroke="{c}" stroke-width="1.6"/>',
    "scout": '<path d="M31 10l7 4-7 4z" fill="{c}" opacity=".6"/>'
             '<circle cx="12" cy="12" r="4.4" fill="none" stroke="{c}" stroke-width="1.7"/>'
             '<path d="M15 15l3 3" stroke="{c}" stroke-width="1.7" stroke-linecap="round"/>',
    "operator": '<rect x="11" y="25" width="20" height="9" rx="1.6" fill="none" stroke="{c}" stroke-width="1.6"/>'
                '<path d="M15 29h12" stroke="{c}" stroke-width="1.4" stroke-linecap="round" opacity=".7"/>',
    "auditor": '<path d="M21 6l10 4v6c0 5.6-4.2 9.4-10 11-5.8-1.6-10-5.4-10-11v-6z" fill="none" stroke="{c}" stroke-width="1.7"/>'
               '<path d="M17 15l3 3 5-6" stroke="{c}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>',
}


def avatar(kind, c):
    prop = AVATAR.get(kind, "").format(c=c)
    return (
        '<svg viewBox="0 0 42 46" aria-hidden="true">'
        '<ellipse cx="21" cy="43.5" rx="11" ry="2.2" fill="%s" opacity=".16"/>'
        '<path d="M9 42v-9a12 12 0 0 1 24 0v9z" fill="%s" opacity=".22"/>'
        '<path d="M9 42v-9a12 12 0 0 1 24 0v9" fill="none" stroke="%s" stroke-width="1.7" stroke-linejoin="round"/>'
        '<circle cx="21" cy="20" r="7.4" fill="var(--surface)" stroke="%s" stroke-width="1.8"/>'
        '<circle cx="18.4" cy="19.6" r="1.05" fill="%s"/><circle cx="23.6" cy="19.6" r="1.05" fill="%s"/>'
        '%s</svg>' % (c, c, c, c, c, c, prop))


def e(x):
    return html.escape("" if x is None else str(x), quote=True)


def fmt(t):
    return "never" if not t else t.replace("T", " ").replace("Z", "")[:16] + " UTC"


def main():
    with io.open(STATE, encoding="utf-8") as fh:
        s = json.load(fh)

    agents = []
    for a in s["agents"]:
        pub = {k: a.get(k) for k in AGENT_PUBLIC}
        if a.get("public_task"):
            pub["current_task"] = a["public_task"]
        if a.get("public_result") is not None:
            pub["last_result"] = a["public_result"] or None
        agents.append(pub)

    sb, meta = s["scoreboard"], s["meta"]
    # Seven company days to one human day (chairman, 2026-09-26). Derived here
    # rather than read from state so both pages always agree.
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from company_clock import clock
    meta = dict(meta, day=clock()["company_days"])
    blocked = sum(1 for a in agents if a["status"] == "BLOCKED")
    gates = len(s.get("gates", []))

    figs = "".join(
        '<div class="fig%s"><dt>%s</dt><dd>%s</dd></div>' % (c[2], c[0], e(c[1]))
        for c in [("Revenue", "$%s" % sb["revenue"], ""),
                  ("Expenses", "$%s" % sb["expenses"], ""),
                  ("Profit", "$%s" % sb["profit"], " profit"),
                  ("Customers", sb["customers"], "")])

    rooms = {r["id"]: r for r in s["rooms"]}
    by_room = {}
    for a in agents:
        by_room.setdefault(a["room"], []).append(a)

    office = ""
    for r in s["rooms"]:
        crew = by_room.get(r["id"], [])
        if not crew:
            # The private office explains WHY a room is empty; the public page
            # says only that it is. `room_empty` is internal commentary and is
            # deliberately not part of the public disclosure surface.
            body = '<div class="empty">Nobody here.</div>' 
        else:
            body = '<div class="crew">' + "".join(
                '<div class="person"><span class="ava">%s<span class="dot" style="background:%s">'
                '</span></span><div class="pm"><div class="pn"><b>%s</b>'
                '<span class="status" style="color:%s;background:color-mix(in srgb,%s 14%%,transparent)">%s</span></div>'
                '<div class="prole">%s</div><p class="ptask">%s</p>'
                '<div class="pruns">Last run %s &middot; next %s</div></div></div>'
                % (avatar(a["avatar"], STATUS.get(a["status"], STATUS["IDLE"])[0]),
                   STATUS.get(a["status"], STATUS["IDLE"])[0],
                   e(a["display"]),
                   STATUS.get(a["status"], STATUS["IDLE"])[0],
                   STATUS.get(a["status"], STATUS["IDLE"])[0],
                   STATUS.get(a["status"], STATUS["IDLE"])[1],
                   e(a["role"]), e(a["current_task"]),
                   e(fmt(a["last_run"])), e(fmt(a["next_run"])))
                for a in crew) + "</div>"
        office += ('<section class="room"><header><h2>%s</h2><p>%s</p></header>%s</section>'
                   % (e(r["name"]), e(r["line"]), body))

    public_feed = []
    for x in sorted(s["feed"], key=lambda x: x["t"], reverse=True):
        if x.get("public") is False:
            continue
        public_feed.append({"t": x["t"], "text": x.get("public_text") or x["text"]})
        if len(public_feed) >= 14:
            break
    s_rooms = s["rooms"]

    feed = "".join(
        '<div class="ev"><time>%s</time><p>%s</p></div>'
        % (e(x["t"].replace("T", " ").replace("Z", "")[5:16]), e(x["text"]))
        for x in public_feed)

    page = TEMPLATE.format(
        generated=e(meta["generated_at"].replace("T", " ").replace("Z", " UTC")),
        day=meta["day"], figs=figs, office=office, feed=feed,
        capital=e(sb["capital"]), agents=len(agents), ventures=sb["active_ventures"],
        blocked=blocked, gates=gates,
        blockline=("%d of %d agents blocked &middot; %d items waiting on the owner"
                   % (blocked, len(agents), gates)) if blocked else
                  ("%d items waiting on the owner" % gates))

    scanned = []
    for a in agents:
        scanned += [("agent %s.%s" % (a["id"], k), a.get(k)) for k in
                    ("display", "role", "current_task", "last_result", "schedule")]
    scanned += [("feed %s" % x["t"], x["text"]) for x in public_feed]
    scanned += [("room %s" % r["id"], r["name"] + " -- " + r["line"]) for r in s_rooms]
    # room_empty is not published, so it is not screened.

    found = []
    for where, text in scanned:
        if not text:
            continue
        low = str(text).lower()
        for t in SENSITIVE:
            if t.lower() in low:
                found.append((t, where, str(text)))
    if found:
        for t, where, text in found:
            sys.stderr.write("LEAK: %r in %s -> %s\n" % (t, where, text[:110]))
        sys.exit("\nRefusing to write the public page: %d withheld term(s) in published "
                 "data. Fix by setting `public_task` / `public_result` on that agent, "
                 "`public_text` or `public: false` on that feed event, or rewording."
                 % len(found))

    with io.open(OUT, "w", encoding="utf-8") as fh:
        fh.write(page)
    print("wrote %s (%.1f KB)" % (os.path.relpath(OUT, REPO), len(page) / 1024.0))

    # The Artifact host supplies its own <!doctype>/<html>/<head> skeleton, so the
    # hosted copy is the same page with that wrapper stripped. Same screened data,
    # one generator -- the two can never say different things.
    body = page[page.index("<title>"):]
    body = body.replace("</head><body>", "").replace("</body></html>", "")
    body = body.replace('<link rel="icon"', '<!-- icon set at publish --><link rel="ignored-icon"')
    with io.open(OUT_ARTIFACT, "w", encoding="utf-8") as fh:
        fh.write(body)
    print("wrote %s (%.1f KB) -- artifact-shaped copy"
          % (os.path.relpath(OUT_ARTIFACT, REPO), len(body) / 1024.0))
    print("PUBLIC page: %d agents, %d feed events. Withheld: strategy, gate detail, "
          "knowledge base, graveyard, messages, problems." % (len(agents), len(s["feed"])))


TEMPLATE = """<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex, nofollow">
<title>LIFE ZERO Status</title>
<link rel="apple-touch-icon" sizes="180x180" href="icon-180.png">
<link rel="icon" type="image/png" sizes="32x32" href="icon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="icon-192.png">
<link rel="manifest" href="manifest.json">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="LIFE ZERO">
<meta name="theme-color" content="#F5F7F3" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0D1317" media="(prefers-color-scheme: dark)">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='7' fill='%2317696F'/><text x='16' y='23' font-size='19' font-family='system-ui' font-weight='700' text-anchor='middle' fill='white'>0</text></svg>">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800&amp;family=IBM+Plex+Mono:wght@400;600&amp;family=IBM+Plex+Sans:wght@400;500;600&amp;display=swap">
<style>
:root{{--paper:#F5F7F3;--surface:#FFF;--surface-2:#EDF0EB;--ink:#151C21;--muted:#5C6A72;
--faint:#87949C;--line:#DDE3DD;--accent:#17696F;--working:#3C8A4C;--researching:#2A6DA6;
--waiting:#B07C18;--blocked:#C2611C;--error:#B03A2B;--idle:#8A9299;--money:#2C7A4B;
--shadow:0 1px 2px rgba(20,30,35,.06),0 4px 14px rgba(20,30,35,.05);color-scheme:light;}}
@media (prefers-color-scheme:dark){{:root{{--paper:#0D1317;--surface:#151D22;--surface-2:#1C262C;
--ink:#E7ECE8;--muted:#94A1A7;--faint:#6D7B82;--line:#26323A;--accent:#54B6AE;--working:#5CB46B;
--researching:#5B9FD6;--waiting:#D3A03F;--blocked:#E08844;--error:#DE6A59;--idle:#78848B;
--money:#4FB97A;--shadow:0 1px 2px rgba(0,0,0,.4),0 6px 18px rgba(0,0,0,.28);color-scheme:dark;}}}}
*{{box-sizing:border-box}}
html,body{{margin:0;padding:0}}
body{{background:var(--paper);color:var(--ink);font:15px/1.5 "IBM Plex Sans",ui-sans-serif,
system-ui,sans-serif;-webkit-font-smoothing:antialiased;
padding:env(safe-area-inset-top,0) 0 env(safe-area-inset-bottom,0)}}
h1,h2{{font-family:"Bricolage Grotesque","IBM Plex Sans",sans-serif;margin:0;
letter-spacing:-.015em;text-wrap:balance}}
.mono,dd{{font-variant-numeric:tabular-nums}}
.wrap{{max-width:680px;margin:0 auto;padding:0 16px}}
.bar{{position:sticky;top:env(safe-area-inset-top,0);z-index:9;background:var(--surface);
border-bottom:1px solid var(--line)}}
.bar .wrap{{padding-block:10px}}
.top{{display:flex;align-items:baseline;justify-content:space-between;gap:10px}}
.brand{{font-family:"Bricolage Grotesque",sans-serif;font-weight:800;font-size:15px}}
.brand span{{color:var(--accent)}}
.day{{font-size:11px;color:var(--faint);letter-spacing:.06em;text-transform:uppercase;
font-family:"IBM Plex Mono",monospace}}
.figs{{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin:8px 0 0}}
.fig dt{{font-size:10px;letter-spacing:.07em;text-transform:uppercase;color:var(--faint);margin:0}}
.fig dd{{margin:1px 0 0;font-family:"IBM Plex Mono",monospace;font-size:17px;font-weight:600;
line-height:1.1}}
.fig.profit dd{{color:var(--money)}}
.note{{margin-top:6px;font-size:11.5px;color:var(--faint)}}
.banner{{margin:14px 0 0;border:1px solid var(--blocked);border-radius:10px;padding:10px 12px;
background:color-mix(in srgb,var(--blocked) 10%,var(--surface));font-size:13px}}
.banner b{{color:var(--blocked)}}
.room{{background:var(--surface);border:1px solid var(--line);border-radius:12px;margin:12px 0;
box-shadow:var(--shadow);overflow:hidden}}
.room header{{padding:11px 13px 9px;border-bottom:1px solid var(--line)}}
.room h2{{font-size:14px;letter-spacing:.03em;text-transform:uppercase}}
.room header p{{margin:2px 0 0;font-size:12px;color:var(--faint)}}
.person{{display:flex;gap:11px;padding:11px 13px;border-top:1px solid var(--line)}}
.crew .person:first-child{{border-top:0}}
.ava{{position:relative;flex:0 0 42px;width:42px;height:46px}}
.ava svg{{width:42px;height:46px;display:block}}
.dot{{position:absolute;right:-1px;top:-1px;width:11px;height:11px;border-radius:50%;
border:2px solid var(--surface)}}
.pm{{min-width:0;flex:1}}
.pn{{display:flex;align-items:center;gap:7px;flex-wrap:wrap}}
.pn b{{font-family:"Bricolage Grotesque",sans-serif;font-size:14.5px}}
.status{{font-size:10px;letter-spacing:.06em;text-transform:uppercase;font-weight:600;
padding:1px 6px;border-radius:4px}}
.prole{{font-size:11.5px;color:var(--faint)}}
.ptask{{margin:3px 0 0;font-size:12.5px;color:var(--muted)}}
.pruns{{margin-top:4px;font-size:10.5px;color:var(--faint);
font-family:"IBM Plex Mono",monospace}}
.empty{{padding:13px;font-size:12.5px;color:var(--muted);font-style:italic}}
h2.sec{{font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--faint);
margin:20px 0 6px}}
.ev{{display:flex;gap:10px;padding:8px 0;border-bottom:1px solid var(--line)}}
.ev time{{flex:0 0 78px;font-family:"IBM Plex Mono",monospace;font-size:10.5px;color:var(--faint);
padding-top:2px}}
.ev p{{margin:0;font-size:12.5px;color:var(--muted)}}
footer{{padding:20px 0 34px;font-size:11.5px;color:var(--faint);line-height:1.6}}
</style></head><body>
<div class="bar"><div class="wrap">
<div class="top"><div class="brand">LIFE <span>ZERO</span></div>
<div class="day">Day {day}</div></div>
<dl class="figs">{figs}</dl>
<div class="note">{capital} available &middot; {ventures} ventures &middot; {agents} agents &middot;
<b>no revenue has ever been received</b></div>
</div></div>
<div class="wrap">
<div class="banner"><b>{blockline}</b></div>
{office}
<h2 class="sec">Recent activity</h2>
{feed}
<footer>
Generated {generated}. This is a snapshot, not a live feed &mdash; it refreshes when the
daily cycle runs.<br>
<b>Partial view.</b> Strategy, allocation, owner-gate detail, the knowledge base and the
graveyard are deliberately not published here; they live in the private office.
</footer>
</div></body></html>
"""

if __name__ == "__main__":
    main()
