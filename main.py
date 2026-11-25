#!/usr/bin/env python3
"""One Star for Monday — make.fun entry.

Writes a single-line one-star review of Monday, written as if Monday
were a restaurant, to $MAKEFUN_OUTPUT_DIR/entry.txt.
Gate: 1-180 chars, at most 25 words, one line, plain text.
"""

import os
import sys

LINE = "One star. The menu lists Friday under dessert, four days away, and the waiter already charged me for it."

MAX_CHARS = 180
MAX_WORDS = 25


def output_path() -> str:
    """Output file, resolved from the environment, never the CWD."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    if not (1 <= len(LINE) <= MAX_CHARS):
        print(f"entry is {len(LINE)} chars, gate is 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if len(LINE.split()) > MAX_WORDS:
        print(f"entry is {len(LINE.split())} words, gate is at most {MAX_WORDS}", file=sys.stderr)
        return 1
    if "\n" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    path = output_path()
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
