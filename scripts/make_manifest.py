#!/usr/bin/env python3
"""Scans Questions/<category>/*.md and writes Questions/manifest.json
(file name, 'Chapter:' and 'Paper:' value of every question).
If a file has no 'Paper:' line, the paper is taken from the file name
(Mar2024-Q05.md -> Mar2024)."""
import json, os, re
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Questions")
cats = ["One Marks", "Two Marks", "Three Marks", "Four Marks", "Five Marks"]
def field(name):
    return re.compile(r"^[ \t]*(?:\*\*)?%s(?:\*\*)?[ \t]*:(?:\*\*)?[ \t]*(.+?)[ \t]*$" % name, re.I | re.M)
CH, PA = field("Chapter"), field("Paper")
out = {}
for c in cats:
    d = os.path.join(root, c)
    items = []
    if os.path.isdir(d):
        for f in sorted(os.listdir(d)):
            if not f.lower().endswith(".md"):
                continue
            with open(os.path.join(d, f), encoding="utf-8-sig") as fh:
                t = fh.read()
            ch, pa = CH.search(t), PA.search(t)
            paper = pa.group(1).replace("*", "").strip() if pa else re.sub(r"[-_ ]*Q\d+.*$", "", f[:-3], flags=re.I)
            items.append({"file": f,
                          "chapter": ch.group(1).replace("*", "").strip() if ch else "Other",
                          "paper": paper or "Other"})
    out[c] = items
with open(os.path.join(root, "manifest.json"), "w", encoding="utf-8") as fh:
    json.dump(out, fh, indent=2, ensure_ascii=False)
print({k: len(v) for k, v in out.items()})
