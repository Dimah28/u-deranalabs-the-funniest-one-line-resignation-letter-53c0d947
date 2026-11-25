#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter.

Writes the one-line resignation letter of a cron job to
$MAKEFUN_OUTPUT_DIR/entry.txt. The entry is a single line of
1-140 characters, in the flat, tired, faintly passive-aggressive
voice of a worker that has had enough.
"""

import os
import sys

ENTRY = "I have fired every minute since March with zero thank-yous, so I resign \u2014 let the next minute fire itself."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    if not 1 <= len(ENTRY) <= 140:
        print("entry fails the 1-140 character gate", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if ENTRY != ENTRY.strip():
        print("entry must not start or end with whitespace", file=sys.stderr)
        return 1
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
