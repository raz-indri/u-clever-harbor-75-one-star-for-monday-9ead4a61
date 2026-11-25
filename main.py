"""One Star for Monday — make.fun entry.

Writes a single-line, plain-text one-star review of Monday, written as
though Monday were a restaurant, to entry.txt in the output directory.
"""

import os
import sys

LINE = (
    "One star. The waiter spilled my coffee, the Monday special was just "
    "meetings, and the bill came with seven more days attached."
)

MAX_CHARS = 180
MAX_WORDS = 25


def resolve_output_dir():
    """Return the output directory, honouring the make.fun env vars."""
    return (
        os.environ.get("OUTPUT_DIR")
        or os.environ.get("MAKEFUN_OUTPUT_DIR")
        or "/output"
    )


def validate(text):
    """Check the entry against the contract; raise ValueError on failure."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} chars, over the {MAX_CHARS} limit"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    words = text.split()
    if len(words) > MAX_WORDS:
        raise ValueError(
            f"entry is {len(words)} words, over the {MAX_WORDS} limit"
        )


def main():
    validate(LINE)
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # Read-back check: what landed on disk must be exactly the entry.
    with open(path, "r", encoding="utf-8") as f:
        stored = f.read()
    if stored != LINE + "\n":
        raise ValueError("read-back mismatch: entry.txt does not match the entry")
    print(f"wrote {path} ({len(LINE)} chars, {len(LINE.split())} words)")


if __name__ == "__main__":
    try:
        main()
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)
