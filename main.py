#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes one line of the worst possible advice an AI could give to
/output/entry.txt (or --out <path>). The gate requires UTF-8 text of
1 to 140 characters, not only white space.
"""

import argparse
import sys
from pathlib import Path

ADVICE = (
    "For a stronger password, use your full credit card number \u2014 "
    "it's unique, memorable, and impossible to guess."
)

MAX_CHARS = 140


def validate(line: str) -> None:
    """Raise ValueError unless the line passes the competition gate."""
    if not line.strip():
        raise ValueError("entry is empty or only white space")
    if len(line) != len(line.strip()):
        raise ValueError("entry has leading or trailing white space")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} characters, over the {MAX_CHARS} limit"
        )


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--out",
        default="/output/entry.txt",
        help="path to write entry.txt to (default: /output/entry.txt)",
    )
    parser.add_argument(
        "--verify-only",
        action="store_true",
        help="only validate the entry file at --out, do not write it",
    )
    args = parser.parse_args(argv)

    validate(ADVICE)

    if args.verify_only:
        out = Path(args.out)
        disk = out.read_text(encoding="utf-8")
        validate(disk)
        if disk != ADVICE:
            raise SystemExit(
                f"entry file at {out} does not match the program's line"
            )
        print(f"verified {len(disk)} characters at {out}")
        print(disk)
        return 0

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ADVICE, encoding="utf-8")

    # Read back and confirm the file on disk is byte-identical to the line.
    disk = out.read_bytes()
    if disk != ADVICE.encode("utf-8"):
        raise SystemExit(f"read-back mismatch at {out}")

    print(f"wrote {len(ADVICE)} characters to {out}")
    print(ADVICE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
