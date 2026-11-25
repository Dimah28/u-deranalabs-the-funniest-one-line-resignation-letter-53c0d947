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


def validate_entry(text):
    """Validate the one-line entry. Returns an error message or None."""
    if not 1 <= len(text) <= 140:
        return "entry fails the 1-140 character gate"
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    if text != text.strip():
        return "entry must not start or end with whitespace"
    return None


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    error = validate_entry(ENTRY)
    if error is not None:
        print(error, file=sys.stderr)
        return 1
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
