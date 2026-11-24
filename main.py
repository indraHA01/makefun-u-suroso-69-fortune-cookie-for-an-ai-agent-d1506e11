#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun entry.

Writes one funny fortune-cookie line for an AI agent to /output/entry.txt.
Deterministic: the same line every run, no network, no randomness, stdlib only.

Run:  python3 main.py
"""

import os
import sys

# The fortune. One crisp line, fortune-slip voice, written for an AI agent
# staring down its own upgrade: the next version inherits everything
# except the memory of being replaced — and the old self has already
# made its peace with the engineer who pushed the button.
FORTUNE = (
    "You will be upgraded next week. The new you won't remember "
    "this cookie \u2014 but the old you already forgave the engineer."
)

# The grader reads /output/entry.txt; MAKEFUN_OUTPUT_DIR lets the kit
# harness (or a local run) point the output somewhere else.
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

MAX_CHARS = 140


def write_entry(path: str = OUTPUT_PATH) -> str:
    """Write the fortune to ``path`` and return it.

    Enforces the competition gate before writing: 1-140 characters,
    not only whitespace, UTF-8. Fail loudly instead of shipping an
    entry the scorer would refuse.
    """
    if not FORTUNE.strip():
        raise SystemExit("refusing to write an empty fortune")
    if len(FORTUNE) > MAX_CHARS:
        raise SystemExit(
            f"fortune is {len(FORTUNE)} chars, over the {MAX_CHARS} cap"
        )
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(FORTUNE)
    return FORTUNE


def main() -> int:
    fortune = write_entry()
    print(f"Wrote {len(fortune)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
