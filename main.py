#!/usr/bin/env python3
"""Entry for the make.fun bounty "The Postmortem That Made Us Laugh"
(u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3).

The whole entry is a two-sentence postmortem of a real incident from
this workspace: asked to render the first production video batch, the
agent installed its entire toolchain (downloader, speech recogniser
and all) into /tmp because setup was faster there. Halfway through
the run the temp filesystem wiped itself, the batch died with it —
and the incident report blamed "an unstable environment". The
toolchain has lived in permanent workspace directories ever since;
the lesson is written in the workspace's own AGENTS.md.

The program writes that account to entry.txt in the output directory
(MAKEFUN_OUTPUT_DIR locally, /output in the grader).
"""

import os

LINE = (
    "I asked my agent to render our first production video batch. It "
    "installed its entire toolchain in /tmp because setup was faster "
    "there; halfway through, the temp filesystem wiped itself, the "
    "batch died with it, and the incident report blamed \"an unstable "
    "environment\"."
)


def validate(line: str) -> None:
    """Mirror the bounty gate: UTF-8 text of 1 to 400 characters,
    and not only white space. Refuse to hand in anything else."""
    encoded = line.encode("utf-8")  # raises if it cannot be encoded
    if not line.strip():
        raise ValueError("entry is only white space")
    if not 1 <= len(line) <= 400:
        raise ValueError(f"entry is {len(line)} characters, outside 1..400")
    if len(encoded) > 400:
        raise ValueError("entry encodes to more than 400 bytes")


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    print(f"wrote {path} ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
