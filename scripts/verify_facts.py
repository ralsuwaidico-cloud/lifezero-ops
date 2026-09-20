#!/usr/bin/env python3
"""Fail if any artefact states a fee rate or tax figure that data/facts.json says is wrong.

Written the day after this happened for real. The UAE listing's feature list told buyers Small
Business Relief covers "periods ending on/before 31 Dec 2026". Ministerial Decision 131 of 2026
extended that window to 2029; the workbook was corrected on 2026-09-10 and so was the paragraph
immediately AFTER the bullet in the same description - and the bullet itself stayed wrong on a
live product page for nine days.

The reason it survived is structural rather than careless. The workbook has build assertions
pinning its numbers. The listing copy, the storefront articles and the owner-queue drafts have
nothing, so every restatement of a fact drifts on its own schedule. A number that appears in
four places needs one home and a check, not four careful authors.

This deliberately does NOT try to refactor every artefact to read from facts.json - that is a
large change with real risk to live copy for no extra safety. It checks for CONTRADICTION, which
is the failure that actually occurred: an artefact stating the superseded value. Historical
narration is allowed ("extended from 31 Dec 2026", "used to end", "raised from 5%"), because
saying what a rate used to be is how you show your work. `allowed_context` in facts.json lists
those phrases per fact, matched within 80 characters either side.

One rule was tried and removed the same hour: excusing a contradiction whenever the CURRENT value
appeared nearby. It silenced a false positive on the LinkedIn draft, and in exchange it stopped
catching a stale fee row - which almost always sits inches from the correct number, in the same
table, in the same sentence. It excused exactly the case worth catching. Narration words are
per-fact and explicit; proximity is neither.

Exit 0 = no artefact contradicts a canonical fact. Non-zero = listed, with file and line.
Run: python3 scripts/verify_facts.py
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
FACTS = ROOT / "data" / "facts.json"
WINDOW = 80


def main():
    if not FACTS.exists():
        print("verify_facts: no data/facts.json, nothing to check")
        return 0
    doc = json.loads(FACTS.read_text())
    problems, checked_files, checked_facts = [], set(), 0

    for fact in doc.get("facts", []):
        checked_facts += 1
        allowed = [a.lower() for a in fact.get("allowed_context", [])]
        for pattern in fact.get("scope", []):
            for f in sorted(ROOT.glob(pattern)):
                if not f.is_file():
                    continue
                checked_files.add(f)
                try:
                    text = f.read_text()
                except (UnicodeDecodeError, OSError):
                    continue
                low = text.lower()
                for bad in fact.get("contradicts", []):
                    start = 0
                    while True:
                        i = low.find(bad.lower(), start)
                        if i == -1:
                            break
                        start = i + 1
                        context = low[max(0, i - WINDOW):i + len(bad) + WINDOW]
                        if any(a in context for a in allowed):
                            continue  # narrating the old value, not claiming it
                        line = text.count("\n", 0, i) + 1
                        rel = f.relative_to(ROOT)
                        problems.append(
                            f"{rel}:{line} states {bad!r}, but data/facts.json says "
                            f"{fact['id']} is {fact['value']!r} "
                            f"({fact['source']}, checked {fact['checked']})")

    for p in problems:
        print("WRONG:", p)
    if not problems:
        print(f"verify_facts: {checked_facts} canonical fact(s) checked across "
              f"{len(checked_files)} file(s), no contradictions")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
