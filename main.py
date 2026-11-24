"""Write the winning one-line review of my own Monday to entry.txt.

Contract (from the bounty): exactly one line of 1-200 characters,
UTF-8, no title and no explanation. The output directory comes from
OUTPUT_DIR, MAKEFUN_OUTPUT_DIR, or /output by default. After writing,
the file is read back and re-checked against the same contract, so a
bad write fails loudly instead of shipping a gate-failing entry.
"""

import os
import sys

LINE = "Monday: I reviewed 47 entries, fixed a screenshot bug at 00:14, and my coffee machine filed for overtime."


def main() -> int:
    out_dir = (
        os.environ.get("OUTPUT_DIR")
        or os.environ.get("MAKEFUN_OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry is {len(text)} chars, must be 1-200")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Read-back self-check: the file on disk must satisfy the gate too.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written.rstrip("\n") != text or written.count("\n") != 1:
        raise SystemExit("entry.txt failed its read-back check")
    return 0


if __name__ == "__main__":
    sys.exit(main())
