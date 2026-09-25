#!/usr/bin/env python3
"""Publish the control plane to Drive, and PROVE the published bytes match.

Why this script exists in this shape
------------------------------------
Drive is an MCP tool, not an HTTP client we hold credentials for, so the only
way to publish is for an agent to put the file's text into a `create_file` call.
That is a hand transcription, and on 2026-09-25 it silently dropped 108 bytes
(KB-107 / INC-003). The old script compared the repo file against a hash it had
written down itself, so it could never have noticed. A check that cannot fail is
not a check.

The fix has two halves, and neither trusts the publisher:

1. SELF-DESCRIBING. `--emit` writes the exact text to publish, carrying a
   `BODY-SHA256:` line in its header. That hash covers every byte BELOW the
   marker line, so it is well defined inside the file itself. Any reader holding
   only the Drive copy -- an operator, the CEO cycle, the Red Team -- can
   recompute it and know whether what they are reading arrived intact. No repo
   access required.

2. OBSERVED. `--verify` takes the bytes actually downloaded back from Drive
   (`download_file_content` returns base64, which is exact, unlike the
   natural-language `read_file_content`) and compares them to the repo. This is
   the only step that has ever looked at the published bytes.

Publishing is therefore: `--emit`, create_file, download_file_content,
`--verify`. A publish that skips the last two steps is not finished, and the
status line says so rather than claiming CURRENT.

Google Drive has no in-place update: republishing creates a NEW file. Superseded
copies are LEFT IN PLACE deliberately -- deletion is permission-gated and buys
nothing, because every operator resolves the control plane by title and
most-recent-modified (KB-105, org/PERMISSION_PREFLIGHT.md).
"""

import argparse
import base64
import hashlib
import json
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE = os.path.join(REPO, "org", "CONTROL_PLANE.md")
STATE = os.path.join(REPO, "state", "control_plane_publish.json")
EMIT = os.path.join(REPO, "state", "control_plane_to_publish.md")
FOLDER_ID = "1HBEz3p2D2EbaLBLr_iH5Ygp-Xtwt8bM0"
TITLE = "LIFE_ZERO_CONTROL_PLANE.md"

MARKER = "BODY-SHA256:"
HEADER = """<!-- PUBLISHED COPY -- integrity header, added by scripts/publish_control_plane.py
     %s %s
     That is the sha256 of every byte below the blank line that follows this
     comment. To check this copy arrived intact, strip everything up to and
     including that blank line and hash the rest. If it does not match, you are
     reading a corrupted transcription -- say so, and do not act on details.
     Source of truth: org/CONTROL_PLANE.md on branch claude/life-zero-runbook-b6qj0t. -->

"""


def sha(b):
    return hashlib.sha256(b).hexdigest()


def body_bytes():
    with open(SOURCE, "rb") as fh:
        return fh.read()


def build():
    """The exact bytes that should exist in Drive."""
    body = body_bytes()
    return (HEADER % (MARKER, sha(body))).encode("utf-8") + body


def split_published(raw):
    """Return (declared_hash, body) from a published copy, or (None, None)."""
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        return None, None
    if MARKER not in text:
        return None, None
    declared = text.split(MARKER, 1)[1].strip().split()[0]
    end = text.find("-->")
    if end == -1:
        return None, None
    after = text[end + 3:]
    # the header is followed by exactly one blank line
    if after.startswith("\n\n"):
        after = after[2:]
    elif after.startswith("\n"):
        after = after[1:]
    return declared, after.encode("utf-8")


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


def cmd_emit():
    payload = build()
    os.makedirs(os.path.dirname(EMIT), exist_ok=True)
    with open(EMIT, "wb") as fh:
        fh.write(payload)
    print("WROTE %s (%d bytes)" % (EMIT, len(payload)))
    print("body sha256: %s" % sha(body_bytes()))
    print("")
    print("Publish it, then verify -- both steps, or the publish is not finished:")
    print("  1. create_file  title=%s" % TITLE)
    print("                  parentId=%s" % FOLDER_ID)
    print("                  contentMimeType=text/plain")
    print("                  disableConversionToGoogleType=true")
    print("                  textContent=<the ENTIRE contents of %s>" % os.path.basename(EMIT))
    print("  2. download_file_content fileId=<new id>   (base64 -- exact)")
    print("  3. python3 scripts/publish_control_plane.py --verify-size <fileSize from the")
    print("       create_file result> --published <new id>")
    print("     (fileSize is the Drive API's own count, not a transcription. A mismatch means")
    print("      the transcription was lossy -- republish rather than record it.)")
    return 0


def cmd_verify_size(reported, file_id):
    """Compare the Drive API's own fileSize against the bytes we emitted.

    HONEST LIMITS. This is the strongest check available without transcribing
    24 KB of base64 back into a shell heredoc -- which would reintroduce exactly
    the hand-transcription error this whole mechanism exists to catch, and could
    only ever produce false alarms, never false passes.

    fileSize comes from the Drive API, not from an agent retyping anything, so it
    is an independent observation. Equal length is NECESSARY but NOT SUFFICIENT
    for byte-identity: it catches the failure that actually happened (KB-107's
    silent 108-byte drift) and any truncation, but not a same-length substitution.

    The sufficient check is a READER recomputing BODY-SHA256 from the Drive copy.
    That is cheap for any agent that opens the file, because it already has the
    text. Which is why the header is there, and why this records the status as
    "size+header" rather than claiming a byte-identity nobody observed.
    """
    expected = len(build())
    print("emitted bytes    : %d" % expected)
    print("Drive fileSize   : %d" % reported)
    if reported != expected:
        print("FAIL: %+d bytes of drift. The transcription was lossy -- republish."
              % (reported - expected))
        print("      Do NOT record this copy as current.")
        return 1
    state = load_state()
    state.update({"file_id": file_id, "sha256": sha(body_bytes()),
                  "byte_identity_verified": "size+header",
                  "body_sha256": sha(body_bytes()),
                  "note": "Length verified against the Drive API's own fileSize (%d bytes),"
                          " and the published copy carries a BODY-SHA256 header any reader can"
                          " recompute. Equal length is necessary, not sufficient -- a reader"
                          " checking the header is the sufficient test. See KB-107 / INC-003."
                          % expected})
    save_state(state)
    print("LENGTH VERIFIED against the Drive API, and the copy carries its own BODY-SHA256.")
    print("  Sufficient check remains: a reader recomputes the header hash. Not a claim of")
    print("  byte-identity -- status recorded as size+header, not true.")
    print("RECORDED: %s" % file_id)
    return 0


def cmd_verify(b64_path, file_id):
    with open(b64_path, "rb") as fh:
        raw = fh.read().strip()
    try:
        got = base64.b64decode(raw, validate=True)
    except Exception:
        got = raw  # already decoded
    declared, body = split_published(got)
    expect = sha(body_bytes())

    if declared is None:
        print("FAIL: the published copy carries no %s header." % MARKER)
        print("      It was not produced by --emit. Republish from --emit output.")
        return 1
    ok_self = declared == sha(body)
    ok_repo = sha(body) == expect
    print("declared in file : %s" % declared[:16])
    print("recomputed body  : %s" % sha(body)[:16])
    print("repo             : %s" % expect[:16])
    if ok_self and ok_repo:
        print("VERIFIED: the published bytes match the repo, and the file attests to itself.")
        state = load_state()
        state.update({"file_id": file_id, "sha256": expect,
                      "byte_identity_verified": True,
                      "note": "Verified by downloading the published bytes and comparing"
                              " to org/CONTROL_PLANE.md. See KB-107 / INC-003."})
        save_state(state)
        print("RECORDED: %s (byte_identity_verified=true)" % file_id)
        return 0
    if not ok_self:
        print("FAIL: the copy does not match its OWN declared hash -- the transcription")
        print("      was corrupted in transit. Republish; do not record it.")
    if not ok_repo:
        print("FAIL: the copy is internally consistent but is not the current repo file.")
        print("      %d bytes published vs %d in repo." % (len(body), len(body_bytes())))
    return 1


def cmd_selftest():
    """Prove the verifier fails on a corrupted copy. Lesson 4: inject the fault."""
    good = build()
    bad = good.replace(b"CURRENT OBJECTIVE", b"CURRENT OBJECTIVE ", 1)
    if bad == good:
        print("SELFTEST INCONCLUSIVE: could not inject a fault"); return 1
    d_g, b_g = split_published(good)
    d_b, b_b = split_published(bad)
    clean_ok = (d_g == sha(b_g))
    dirty_caught = (d_b != sha(b_b))
    print("clean copy accepted : %s" % clean_ok)
    print("1-byte corruption caught: %s" % dirty_caught)
    if clean_ok and dirty_caught:
        print("SELFTEST PASS -- the guard was proven by injecting the fault, not by clean data.")
        return 0
    print("SELFTEST FAIL"); return 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--emit", action="store_true", help="write the exact bytes to publish")
    ap.add_argument("--verify", metavar="B64_FILE", help="downloaded bytes to check")
    ap.add_argument("--published", metavar="FILE_ID", help="the new Drive file id")
    ap.add_argument("--verify-size", type=int, metavar="N",
                    help="fileSize reported by the Drive API for the new file")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if not os.path.exists(SOURCE):
        sys.exit("FAIL: %s does not exist" % SOURCE)
    if args.selftest:
        return cmd_selftest()
    if args.emit:
        return cmd_emit()
    if args.verify_size is not None:
        if not args.published:
            sys.exit("FAIL: --verify-size needs --published <file id>")
        return cmd_verify_size(args.verify_size, args.published)
    if args.verify:
        if not args.published:
            sys.exit("FAIL: --verify needs --published <file id>")
        return cmd_verify(args.verify, args.published)

    current = sha(body_bytes())
    state = load_state()
    if state.get("sha256") == current:
        mode = state.get("byte_identity_verified")
        if mode is True:
            print("CURRENT AND BYTE-VERIFIED (body sha256 %s)." % current[:12])
            print("Drive file id: %s" % state.get("file_id"))
            print("The published bytes were downloaded and compared. Nothing to do.")
            return 0
        if mode == "size+header":
            print("CURRENT, LENGTH-VERIFIED (body sha256 %s)." % current[:12])
            print("Drive file id: %s" % state.get("file_id"))
            print("  The Drive API's own fileSize matched the emitted byte count, and the")
            print("  published copy carries a BODY-SHA256 header. Equal length is necessary,")
            print("  not sufficient. Any reader of the Drive copy should recompute that header")
            print("  hash -- that is the sufficient test, and it is cheap for whoever is")
            print("  already reading the file. See KB-107.")
            return 0
        print("CONTENT CURRENT, BYTE-IDENTITY UNVERIFIED (body sha256 %s)." % current[:12])
        print("  %s" % state.get("note", "no note recorded"))
        print("  Finish it: --emit, publish, download, --verify.")
        print("Drive file id: %s" % state.get("file_id"))
        return 0
    print("STALE: org/CONTROL_PLANE.md has changed since the last publish.")
    print("  published : %s" % ((state.get("sha256") or "(never)")[:12]))
    print("  current   : %s" % current[:12])
    print("  superseded: %s" % state.get("file_id", "(unknown)"))
    print("")
    print("Run: python3 scripts/publish_control_plane.py --emit")
    print("")
    print("Do NOT trash the superseded copy. Deletion is permission-gated and buys")
    print("nothing -- readers take the most recently modified copy (KB-105).")
    return 1


if __name__ == "__main__":
    sys.exit(main())
