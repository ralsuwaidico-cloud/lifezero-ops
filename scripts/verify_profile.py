#!/usr/bin/env python3
"""Verify the Gumroad seller profile matches its source in growth/profile/.

The seller name and bio are the storefront root - the page every product links to and the
first thing a visitor reads about who made these. The bio sat EMPTY from 2026-09-10 to
2026-09-15 and nothing noticed, because nothing was looking: verify_live checks products,
verify_pages checks storefront pages, and the profile belonged to neither.

Standing rule on this project since the tags incident of 2026-09-09: a field pushed to the
store is a field something checks, the same day. This is that check for the profile.

Exit 0 = matches. Non-zero = drift, listed.
"""
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PROFILE = ROOT / "growth" / "profile"
FIELDS = {"bio": "bio.txt", "name": "name.txt"}


def live_user():
    p = subprocess.run(["gumroad", "user", "--json", "--no-input", "--non-interactive"],
                       capture_output=True, text=True)
    if p.returncode != 0 or not p.stdout.strip():
        return None
    try:
        return json.loads(p.stdout).get("user")
    except json.JSONDecodeError:
        return None


def main():
    if not PROFILE.is_dir():
        print("verify_profile: no growth/profile/ directory, nothing to check")
        return 0
    u = live_user()
    if u is None:
        print("DRIFT: could not read the live profile")
        return 1

    problems = []
    checked = 0
    for field, fname in FIELDS.items():
        f = PROFILE / fname
        if not f.exists():
            continue
        want, got = f.read_text().strip(), (u.get(field) or "").strip()
        if not got:
            problems.append(f"{field} is EMPTY on the live profile - the storefront root says "
                            f"nothing about who made these")
        elif got != want:
            problems.append(f"{field} differs from growth/profile/{fname} "
                            f"({len(got)} chars live vs {len(want)} local)")
        else:
            checked += 1

    for p in problems:
        print("DRIFT:", p)
    if not problems:
        print(f"verify_profile: {checked} profile field(s) match their source")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
