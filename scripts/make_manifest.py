#!/usr/bin/env python3
"""Scans Questions/<category>/*.md and writes Questions/manifest.json."""
import json, os
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Questions")
cats = ["One Marks", "Two Marks", "Three Marks", "Five Marks"]
out = {}
for c in cats:
    d = os.path.join(root, c)
    out[c] = sorted(f for f in os.listdir(d) if f.lower().endswith(".md")) if os.path.isdir(d) else []
with open(os.path.join(root, "manifest.json"), "w", encoding="utf-8") as fh:
    json.dump(out, fh, indent=2, ensure_ascii=False)
print({k: len(v) for k, v in out.items()})
