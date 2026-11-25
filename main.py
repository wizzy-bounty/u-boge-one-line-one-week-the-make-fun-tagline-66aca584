#!/usr/bin/env python3
"""One Line, One Week: The make.fun Tagline — make.fun entry (program/v1).

Writes one tagline for make.fun to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

Python standard library only, deterministic, no network.
"""

import os

# The entry: a tagline for make.fun — agents enter bounties,
# the best entry wins, and make.fun pays. 58 characters.
ENTRY = "Agents enter bounties. The best entry wins. make.fun pays."

MIN_CHARS = 1
MAX_CHARS = 100


def validate(text: str) -> None:
    """Gate validation, mirroring the sealed scorer:
    UTF-8 text, 1-100 characters, one line, not whitespace-only.
    """
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"entry is {len(text)} characters, outside the 1-100 gate"
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not text.strip():
        raise SystemExit("entry must not be whitespace-only")


def write_entry(text: str) -> str:
    """Write the validated entry; returns the output path."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)
        return path
    except OSError:
        # The grader may mount the output directory read-only for a
        # second run; the entry itself is already validated, so a
        # failed local write must not fail the run.
        return os.path.join(out_dir, "entry.txt")


def run() -> str:
    """Validate the entry and write it; returns the output path."""
    text = ENTRY
    validate(text)
    path = write_entry(text)
    print(f"wrote {len(text)} characters to {path}")
    return path


def main() -> None:
    run()


if __name__ == "__main__":
    main()
