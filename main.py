#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note — a patch note fixing human sleep."""
import os

LINE = "Fixed a bug where humans woke up at 3am to think about an email from 2019."
assert len(LINE) == 74, "entry must be exactly 74 characters"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
