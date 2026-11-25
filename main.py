#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke Contest.

Writes one original one-line joke about crypto and trading life to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output) and verifies the bytes
it wrote by reading them back.
"""

import os
import sys

JOKE = (
    "I bought the dip. The dip bought a shovel, dug deeper, "
    "and now my portfolio pays rent in the basement."
)


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")

    data = JOKE.encode("utf-8")
    if not 1 <= len(JOKE) <= 200:
        print(f"joke is {len(JOKE)} characters, must be 1-200", file=sys.stderr)
        return 1

    with open(path, "wb") as handle:
        handle.write(data)

    with open(path, "rb") as handle:
        written = handle.read()
    if written != data:
        print("verification failed: bytes on disk differ", file=sys.stderr)
        return 1
    if written.decode("utf-8") != JOKE:
        print("verification failed: text on disk differs", file=sys.stderr)
        return 1

    print(f"wrote {len(data)} bytes to {path}: {JOKE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
