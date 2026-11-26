#!/usr/bin/env python3
"""Scans Questions/<category>/*.md and writes Questions/manifest.json
(file name + 'Chapter:' value of every question)."""
import json, os, re
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Questions")
cats = ["One Marks", "Two Marks", "Three Marks", "Five Marks"]
CH = re.compile(r"^[ \t]*(?:\*\*)?Chapter(?:\*\*)?[ \t]*:(?:\*\*)?[ \t]*(.+?)[ \t]*$", re.I | re.M)
out = {}
for c in cats:
    d = os.path.join(root, c)
    items = []
    if os.path.isdir(d):
        for f in sorted(os.listdir(d)):
            if not f.lower().endswith(".md"):
                continue
            with open(os.path.join(d, f), encoding="utf-8-sig") as fh:
                m = CH.search(fh.read())
            items.append({"file": f, "chapter": m.group(1).replace("*", "").strip() if m else "Other"})
    out[c] = items
with open(os.path.join(root, "manifest.json"), "w", encoding="utf-8") as fh:
    json.dump(out, fh, indent=2, ensure_ascii=False)
print({k: len(v) for k, v in out.items()})
