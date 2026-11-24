"""One-line excuse writer: emits the exact 98-byte entry, no trailing newline."""

from pathlib import Path

LINE = "I finished it on time in a parallel run. Unfortunately, this is the run where I am talking to you."

Path("/output").mkdir(parents=True, exist_ok=True)
Path("/output/entry.txt").write_text(LINE, encoding="utf-8")
