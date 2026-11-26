#!/usr/bin/env python3
"""Texts From Your Future Self - make.fun one-liner entry.

Writes a single funny text message from the writer's future self to
``entry.txt`` inside the directory named by ``MAKEFUN_OUTPUT_DIR``
(default ``/output``). The grader reads /output, not the current
directory, so the output path always comes from the environment.
"""

import os

ENTRY = (
    "Hey, it's you from 2041. The sourdough starter you named Doug is now "
    "legally a dependent. Stop feeding it \u2014 it has a lawyer and it wants "
    "the thermostat."
)


def validate(text: str) -> None:
    """Gate: mirrors the house gate scorer for /output/entry.txt.

    The entry must be 1-200 characters, a single line, not only
    whitespace, and valid UTF-8. Leading/trailing whitespace is also
    rejected so no character of the 200 is wasted on padding.
    """
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    text.encode("utf-8")  # raises if not valid UTF-8


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
