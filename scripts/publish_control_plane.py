#!/usr/bin/env python3
"""Tell the CEO cycle whether the Drive copy of the control plane is stale.

Google Drive has no in-place content update: republishing creates a NEW file and
the old one must be trashed. That makes the file id unstable, so every operator
prompt resolves the control plane by TITLE and most-recent-modified instead.

This script cannot call Drive itself -- Drive is an MCP tool, not an HTTP client
we hold credentials for. It does the part that can be automated: decide whether a
republish is owed, and print the exact steps. After publishing, record it with
`--published <new_file_id>` so the next run can tell stale from current.
"""

import argparse
import hashlib
import json
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE = os.path.join(REPO, "org", "CONTROL_PLANE.md")
STATE = os.path.join(REPO, "state", "control_plane_publish.json")
FOLDER_ID = "1HBEz3p2D2EbaLBLr_iH5Ygp-Xtwt8bM0"
TITLE = "LIFE_ZERO_CONTROL_PLANE.md"


def digest(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def load_state():
    try:
        with open(STATE, encoding="utf-8") as fh:
            return json.load(fh)
    except FileNotFoundError:
        return {}


def save_state(state):
    os.makedirs(os.path.dirname(STATE), exist_ok=True)
    with open(STATE, "w", encoding="utf-8") as fh:
        json.dump(state, fh, indent=2, sort_keys=True)
        fh.write("\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--published", metavar="FILE_ID",
                    help="record that this file id now holds the current content")
    args = ap.parse_args()

    if not os.path.exists(SOURCE):
        sys.exit("FAIL: %s does not exist" % SOURCE)

    current = digest(SOURCE)
    state = load_state()

    if args.published:
        previous = state.get("file_id")
        state.update({"file_id": args.published, "sha256": current})
        save_state(state)
        print("RECORDED: %s now holds the current control plane (sha256 %s)"
              % (args.published, current[:12]))
        if previous and previous != args.published:
            print("REMINDER: trash the superseded file %s -- two copies in the"
                  " folder and the operators may read the wrong one." % previous)
        return 0

    published_hash = state.get("sha256")
    file_id = state.get("file_id", "(unknown -- search the folder by title)")

    if published_hash == current:
        print("CURRENT: the Drive copy matches org/CONTROL_PLANE.md (sha256 %s)."
              % current[:12])
        print("Drive file id: %s" % file_id)
        print("Nothing to do.")
        return 0

    print("STALE: org/CONTROL_PLANE.md has changed since the last publish.")
    print("  published sha256: %s" % (published_hash[:12] if published_hash else "(never published)"))
    print("  current   sha256: %s" % current[:12])
    print("  superseded file : %s" % file_id)
    print("")
    print("Republish it now, in this order:")
    print("  1. create_file  title=%s" % TITLE)
    print("                  parentId=%s" % FOLDER_ID)
    print("                  contentMimeType=text/plain")
    print("                  disableConversionToGoogleType=true")
    print("                  textContent=<the full contents of org/CONTROL_PLANE.md>")
    print("  2. trash_file   fileId=%s" % file_id)
    print("  3. python3 scripts/publish_control_plane.py --published <new file id>")
    print("")
    print("The id changing is expected -- operator prompts resolve the file by")
    print("title and most-recent-modified. Two copies in the folder is the failure.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
