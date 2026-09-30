#!/usr/bin/env python3
"""Two agents both append to the knowledge base, and both pick "the next number".

On 2026-09-30 that had produced FIFTEEN duplicate ids -- KB-107, 120 (three times),
121, 134, 135, 136, 150 through 157, and 167. A duplicate id is not cosmetic: every
entry in this repository cites its evidence by number, and "see KB-173" stops meaning
anything the moment two entries answer to it. The knowledge base is the one asset this
company has actually accumulated, and its index was quietly rotting.

This reports them, and prints the next free number so nobody has to guess again.

    python3 scripts/kb_lint.py            # list duplicates, exit 1 if any
    python3 scripts/kb_lint.py --next     # just print the next free id
"""
import collections, io, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KB = os.path.join(REPO, "org", "KNOWLEDGE_BASE.md")
# A heading that says UPDATE is a deliberate follow-up to an existing entry, not a
# second definition of it, so it does not count as a clash.
HEADING = re.compile(r"^#{2,3} KB-(\d+)\b(?![^\n]*\bUPDATE\b)", re.M)


def main():
    text = io.open(KB, encoding="utf-8").read()
    nums = [int(n) for n in HEADING.findall(text)]
    counts = collections.Counter(nums)
    dupes = sorted(n for n, c in counts.items() if c > 1)
    nxt = (max(nums) + 1) if nums else 1
    while nxt in counts:
        nxt += 1

    if "--next" in sys.argv:
        print("KB-%d" % nxt)
        return

    print("%d entries, %d distinct ids, next free id KB-%d" % (len(nums), len(counts), nxt))
    if not dupes:
        print("No duplicate ids.")
        return
    for n in dupes:
        print("\nDUPLICATE KB-%d (%d entries):" % (n, counts[n]))
        for m in HEADING.finditer(text):
            if int(m.group(1)) != n:
                continue
            line = text.count("\n", 0, m.start()) + 1
            full = text[m.start():text.find("\n", m.start())]
            print("  line %-6d %s" % (line, full.strip()[:96]))
    sys.exit("\n%d duplicated id(s). Every citation to one of these is ambiguous. "
             "Renumber the LATER entry to the next free id and fix its references; "
             "never renumber the earlier one, because other files already cite it."
             % len(dupes))


if __name__ == "__main__":
    main()
