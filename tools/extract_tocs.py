#!/usr/bin/env python3
"""
PHASE 0: Extract Table of Contents (first pages) from each manual text file.
Builds a per-manual topic list for the document map.
"""
import os
import re
import json

BASE = "/home/z/my-project/hotel-erp"
TEXT_DIR = os.path.join(BASE, "extracted-text")
OUT = os.path.join(BASE, "toc-extracts.json")

out = {}

for root, dirs, files in os.walk(TEXT_DIR):
    for fname in sorted(files):
        if not fname.endswith(".txt"):
            continue
        fpath = os.path.join(root, fname)
        module = os.path.basename(root).replace("_", " ")
        with open(fpath, encoding="utf-8") as f:
            content = f.read()

        # Get first 2 pages of text
        pages = content.split("===== PAGE ")
        first = ""
        if len(pages) > 2:
            first = "===== PAGE " + pages[1] + "===== PAGE " + pages[2]
        elif len(pages) > 1:
            first = "===== PAGE " + pages[1]

        # Extract TOC lines: lines that look like "1. something" or numbered items
        lines = [l.strip() for l in first.split("\n") if l.strip()]
        toc_lines = []
        in_toc = False
        for l in lines:
            # skip page markers and pdf noise
            if re.match(r'^=\s*PAGE\s+\d+\s*=', l):
                continue
            if "pdfMachine" in l or "Broadgun" in l:
                continue
            # detect TOC section start
            if re.search(r'table\s*of\s*contents', l, re.I):
                in_toc = True
                continue
            if in_toc:
                # stop when we hit a chapter body start (long paragraph)
                if len(l) > 200:
                    break
                # TOC entry patterns
                if re.match(r'^\d+[\.\)_\-]?\s*[\w\(\)\&\/\-\+\.\'\,\s]+$', l) or re.match(r'^[A-Z][\w\s\&\/\-]{2,60}$', l):
                    # normalize: strip leading numbers
                    entry = re.sub(r'^\d+[\.\)_\-]?\s*', '', l).strip().replace('_', ' ')
                    if 2 < len(entry) < 80:
                        toc_lines.append(entry)
                # stop after finding enough entries or when hitting body text
                if len(toc_lines) > 40:
                    break
            # also try to detect topic lines before body (some manuals list topics without TOC header)
        
        # If no TOC found, take headings-like lines from first pages
        if not toc_lines:
            for l in lines[:60]:
                if re.match(r'^\d+[\.\)]\s+[A-Z]', l) and len(l) < 80:
                    entry = re.sub(r'^\d+[\.\)]\s*', '', l).strip()
                    toc_lines.append(entry)
                if len(toc_lines) > 25:
                    break

        key = f"{module}/{fname.replace('.txt','')}"
        out[key] = toc_lines[:35]

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

# Print summary
for k, v in out.items():
    print(f"\n### {k} ({len(v)} topics)")
    for t in v[:12]:
        print(f"   - {t}")
