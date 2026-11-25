#!/usr/bin/env python3
"""Roast Your Own Agent — writes one roast line to /output/entry.txt.

Deterministic: fixed string literal, stdlib only, no randomness, no
network, no clock, no file reads. Output is exactly one line with
no trailing newline. The roast: my agent's confident wrong answer,
taken one step further — it backs itself up by citing itself.
"""

import os

ROAST = (
    "My agent confidently gave the wrong answer, "
    "then cited itself as the source."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ROAST.strip()
    assert 1 <= len(text) <= 140, "roast must be 1-140 characters"
    assert "\n" not in text and "\r" not in text, "roast must be one line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
