#!/usr/bin/env python3
"""
PHASE 1 tool: Extract field-definition tables from FortuneNext manual text files.
Pattern: "Column/ Fields" + "Description" headers, then alternating field-name / description lines.
Also extracts numbered section headings ("N. Title") as the screen/option catalog.
Outputs: /home/z/my-project/hotel-erp/field-extracts/<module>/<file>.json
"""
import os
import re
import json

BASE = "/home/z/my-project/hotel-erp"
TEXT_DIR = os.path.join(BASE, "extracted-text")
OUT_DIR = os.path.join(BASE, "field-extracts")

# Verbs that typically START a description line
DESC_STARTERS = re.compile(
    r'^(Type|Enter|Select|Double-?click|Click|Press|This|The |Specify|Choose|If |By |'
    r'Mark|Enable|Check|Displays?|Default|Date|Note|From |To |Indicates?|Specifies?|'
    r'Based|Depending|Amount|Value|It |In |On |For |A |An |User|System|Enter the|'
    r'Radio|Combo|Check ?box|Alphanumeric|Numeric|Mandatory|Optional|Auto)', re.I)

# A field-name line: Title Case words, short, no sentence-ending period usually
FIELD_NAME = re.compile(r'^[A-Z][A-Za-z0-9 /&\.\-\(\)%]{2,45}$')

def clean(s):
    return re.sub(r'\s+', ' ', s).strip()

def extract_fields_from_section(text):
    """Parse field tables after 'Column/ Fields' markers."""
    fields = []
    lines = [l.rstrip() for l in text.split('\n')]
    i = 0
    n = len(lines)
    while i < n:
        l = clean(lines[i])
        # find table header
        if re.match(r'^Column/?\s*Fields?$', l, re.I):
            i += 1
            # skip 'Description' and empty
            while i < n and (clean(lines[i]).lower().startswith('description') or not clean(lines[i])):
                i += 1
            # now parse field/desc pairs
            while i < n:
                name_line = clean(lines[i])
                if not name_line:
                    i += 1
                    continue
                # stop conditions: new section, new table header, page break
                if (name_line.startswith('===== PAGE') or
                    re.match(r'^Column/?\s*Fields?$', name_line, re.I) or
                    re.match(r'^\d+\.\s+[A-Z]', name_line) or
                    name_line.lower().startswith('note:') or
                    re.match(r'^To (add|modify|delete|view)', name_line)):
                    break
                # potential field name
                if FIELD_NAME.match(name_line) and not DESC_STARTERS.match(name_line):
                    # avoid pure generic words
                    if name_line.lower() in ('description', 'standards', 'click', 'status', 'user', 'last updated'):
                        i += 1
                        continue
                    fname = name_line
                    i += 1
                    # accumulate description lines
                    desc = []
                    while i < n:
                        d = clean(lines[i])
                        if not d:
                            i += 1
                            continue
                        if d.startswith('===== PAGE') or re.match(r'^Column/?\s*Fields?$', d, re.I):
                            break
                        # next field name?
                        if FIELD_NAME.match(d) and not DESC_STARTERS.match(d):
                            # heuristic: short title-case line that is NOT continuing description
                            if len(d) < 40 and not d.endswith('.'):
                                break
                        if re.match(r'^\d+\.\s+[A-Z]', d) or d.lower().startswith('note:'):
                            break
                        if re.match(r'^To (add|modify|delete|view)', d):
                            break
                        desc.append(d)
                        i += 1
                        # stop after reasonable desc length
                        if sum(len(x) for x in desc) > 600:
                            break
                    fdesc = ' '.join(desc)
                    # only keep if desc looks like a description
                    if fdesc and len(fdesc) > 15:
                        fields.append({"field": fname, "description": fdesc})
                    elif fdesc:
                        fields.append({"field": fname, "description": fdesc})
                else:
                    i += 1
        else:
            i += 1
    return fields


def extract_sections(text):
    """Extract numbered section headings: '1. Room Types' etc."""
    sections = []
    for m in re.finditer(r'^\s*(\d{1,3})[\.\)]\s+([A-Z][A-Za-z0-9 &/\-\.\(\)]{2,60})\s*$', text, re.M):
        num = int(m.group(1))
        title = clean(m.group(2))
        if title.lower() not in ('click', 'note'):
            sections.append({"num": num, "title": title})
    # dedupe by (num,title)
    seen = set()
    out = []
    for s in sections:
        key = (s['num'], s['title'].lower())
        if key not in seen:
            seen.add(key)
            out.append(s)
    return out


def split_pages(text):
    parts = re.split(r'===== PAGE (\d+) =====', text)
    pages = {}
    for i in range(1, len(parts) - 1, 2):
        pages[int(parts[i])] = parts[i+1]
    return pages


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    summary = {}
    for root, dirs, files in os.walk(TEXT_DIR):
        for fname in sorted(files):
            if not fname.endswith('.txt'):
                continue
            module = os.path.basename(root).replace('_', ' ')
            fpath = os.path.join(root, fname)
            with open(fpath, encoding='utf-8') as f:
                text = f.read()
            pages = split_pages(text)
            # process page by page, tracking sections
            fields = extract_fields_from_section(text)
            sections = extract_sections(text)

            # Map fields to the nearest preceding section title
            # simple approach: find positions of section titles and table starts in text
            sec_positions = []
            for m in re.finditer(r'^\s*(\d{1,3})[\.\)]\s+([A-Z][A-Za-z0-9 &/\-\.\(\)]{2,60})\s*$', text, re.M):
                sec_positions.append((m.start(), clean(m.group(2))))
            tab_positions = [m.start() for m in re.finditer(r'^Column/?\s*Fields?\s*$', text, re.M)]

            # rebuild fields with context
            enriched = []
            lines = text.split('\n')
            pos = 0
            line_positions = []
            for l in lines:
                line_positions.append(pos)
                pos += len(l) + 1

            # For each "Column/ Fields" occurrence, get nearest section title above
            for tm in re.finditer(r'^Column/?\s*Fields?\s*$', text, re.M):
                start = tm.start()
                sec_title = None
                for sp, st in sec_positions:
                    if sp < start:
                        sec_title = st
                    else:
                        break
                # find the page number for this position
                pg = 1
                for pnum, ptext in pages.items():
                    if ptext and text.find(ptext[:200]) != -1:
                        pass
                chunk = text[start:start+3000]
                enriched.append({
                    "section": sec_title,
                    "offset": start,
                    "fields_raw": extract_fields_from_section(text[start:start+6000]),
                })

            out = {
                "module": module,
                "file": fname.replace('.txt', '.pdf'),
                "sections": sections,
                "field_tables": enriched,
            }
            mod_dir = os.path.join(OUT_DIR, module.replace(' ', '_'))
            os.makedirs(mod_dir, exist_ok=True)
            with open(os.path.join(mod_dir, fname.replace('.txt', '.json')), 'w', encoding='utf-8') as f:
                json.dump(out, f, ensure_ascii=False, indent=1)

            n_fields = sum(len(t['fields_raw']) for t in enriched)
            key = f"{module}/{fname.replace('.txt','')}"
            summary[key] = {"sections": len(sections), "tables": len(enriched), "fields": n_fields}

    with open(os.path.join(OUT_DIR, "_summary.json"), 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    print(f"{'File':<58} {'Sections':>8} {'Tables':>7} {'Fields':>7}")
    print('-' * 85)
    tot_f = 0
    for k, v in sorted(summary.items()):
        print(f"{k:<58} {v['sections']:>8} {v['tables']:>7} {v['fields']:>7}")
        tot_f += v['fields']
    print('-' * 85)
    print(f"TOTAL FIELDS EXTRACTED: {tot_f}")

if __name__ == '__main__':
    main()
