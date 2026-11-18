#!/usr/bin/env python3
"""Entry program for make.fun's news-image-20261118 bounty.

The image that sums up Wednesday 18 November 2026's world news — a
newspaper front page drawn with Python and PIL — lives in entry.png
beside this file. The program copies it to the output directory as
entry.png, byte for byte, so both grader runs write identical bytes.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
/output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(source, os.path.join(out_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
