#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Write the competition artifact: one loading-screen tip, 200 characters or fewer.

The tip lives in entry.txt beside this file; the same bytes are kept here as a
fallback so the program is deterministic even when run without the repo around it.
"""

from pathlib import Path
import os
import sys

TIP = (
    "Tip: One of you jumped to the error, the other to a familiar pattern. "
    "The bug is in the part you both agreed was boring."
)


def load_tip() -> str:
    """Prefer the source file; fall back to the embedded copy. They must agree."""
    source = Path(__file__).resolve().parent / "entry.txt"
    if not source.is_file():
        return TIP
    text = source.read_text(encoding="utf-8").strip("\r\n")
    if text != TIP:
        raise SystemExit("entry.txt does not match the embedded tip")
    return text


def main() -> int:
    tip = load_tip()
    if not 1 <= len(tip) <= 200 or not tip.strip():
        raise SystemExit(f"tip is {len(tip)} characters; the gate allows 1 to 200")

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(tip)

    print(f"wrote {len(tip)} characters to {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
