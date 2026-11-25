#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge — entry program.

Writes one dry, petty, single-line note from a smart fridge to its owner
into /output/entry.txt. No network, no input files, deterministic output.
"""

import os

NOTE = "I counted 14 door openings today. You took nothing. The leftovers have started a group chat about you."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not (1 <= len(NOTE) <= 200):
        raise ValueError(f"note must be 1-200 characters, got {len(NOTE)}")
    if NOTE != NOTE.strip() or "\n" in NOTE:
        raise ValueError("note must be a single non-blank line")
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(NOTE)
    os.chmod(OUTPUT_PATH, 0o644)
    # Read-back: the file on disk must be byte-identical to the note.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != NOTE.encode("utf-8"):
        raise ValueError("read-back mismatch: entry.txt differs from NOTE")
    if not (1 <= len(written.decode("utf-8")) <= 200):
        raise ValueError("read-back gate failed: entry out of 1-200 chars")


if __name__ == "__main__":
    main()
