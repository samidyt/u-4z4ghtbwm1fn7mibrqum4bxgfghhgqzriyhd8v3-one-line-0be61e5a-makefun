#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry (program/v1).

Writes a single original funny line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt) and prints it to stdout.

Gate (per the bounty kit): /output/entry.txt must be UTF-8 text of
1 to 140 characters, not only whitespace. The program self-checks
that gate before writing and fails loudly instead of handing in
a bad entry.
"""

import os
import sys

LINE = (
    "I asked my smart fridge for life advice. It said: stop opening "
    "me at 2 a.m. looking for answers."
)


def main() -> int:
    text = LINE.strip()
    if not (1 <= len(text) <= 140):
        print(f"gate failed: line is {len(text)} chars, must be 1-140",
              file=sys.stderr)
        return 1
    if not text.strip():
        print("gate failed: line is only whitespace", file=sys.stderr)
        return 1
    if "\n" in text:
        print("gate failed: line must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

    # Round-trip check: what landed on disk must be exactly the line.
    with open(path, "rb") as f:
        if f.read().decode("utf-8") != text:
            print("gate failed: written bytes differ from the line",
                  file=sys.stderr)
            return 1

    # The line itself, on stdout, is the verifiable output.
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
