#!/usr/bin/env python3
"""The Funniest Out-of-Office — make.fun entry.

Writes the one-line out-of-office auto-reply to /output/entry.txt.
The competition gate requires UTF-8 text of 1-140 characters, not only
whitespace, so the program refuses to write anything outside that gate.
"""

import os

LINE = (
    "Out of office: my replacement has been trained, briefed, "
    "and has already quit."
)


def main() -> None:
    line = LINE.strip()
    if not line or len(line) > 140:
        raise SystemExit(f"entry must be 1-140 chars, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    # The grader sandbox provides /output, but create it when it is
    # missing so the program also runs cleanly anywhere else.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    # Round-trip check: what the grader reads must be exactly this line.
    back = open("/output/entry.txt", encoding="utf-8").read().rstrip("\n")
    if back != line:
        raise SystemExit("round-trip mismatch")
    print(f"wrote {len(line)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
