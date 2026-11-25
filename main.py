#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh — entry program.

DRAFT -> REVISED: the draft line was

    "My smart fridge pushed a firmware update and now the ice maker
    won't work."

Three real improvements in the revision below:

1. "pushed a firmware update" became "updated its firmware
   overnight" — the update happens while you sleep, so the betrayal
   is discovered in the morning instead of announced; "overnight"
   also drops the redundant "smart", since firmware implies it.
2. "won't work" became "holds my ice hostage until I accept its
   terms and conditions" — the punchline now shows the exact absurd
   mechanism (an appliance demanding a legal agreement before it
   will make ice) instead of a flat failure, and the surprise turn
   lands at the end of the line.
3. "My smart fridge" became "My fridge" — one word shorter, and
   every remaining word earns its place inside the 200 character
   limit; the joke stays specific to a smart fridge (firmware,
   ice maker, terms and conditions) without saying "smart".

The final line is 125 characters, one line, no trailing newline.
The program writes it to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output). Python 3 standard library only, deterministic.
"""

import os

ENTRY = "My fridge updated its firmware overnight, and now the ice maker holds my ice hostage until I accept its terms and conditions."

assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
assert ENTRY == ENTRY.strip(), "entry must have no leading/trailing whitespace"
assert ENTRY.strip(), "entry must not be only whitespace"

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
