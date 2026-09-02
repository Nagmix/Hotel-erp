#!/usr/bin/env python3
"""
PHASE 0 — DISCOVERY: Inventory all FortuneNext 6i manuals.
- Walks all PDFs in "6i Manuals/"
- Extracts metadata (pages, title, TOC)
- Extracts full text to extracted-text/ (per module)
- Builds a JSON + Markdown inventory
"""
import os
import json
import fitz  # PyMuPDF

BASE = "/home/z/my-project/hotel-erp"
MANUALS = os.path.join(BASE, "6i Manuals")
OUT_TEXT = os.path.join(BASE, "extracted-text")
OUT_JSON = os.path.join(BASE, "inventory.json")

os.makedirs(OUT_TEXT, exist_ok=True)

results = []

for root, dirs, files in os.walk(MANUALS):
    for fname in sorted(files):
        if not fname.lower().endswith(".pdf"):
            continue
        fpath = os.path.join(root, fname)
        rel_path = os.path.relpath(fpath, BASE)
        module = os.path.basename(root) if os.path.basename(root) != "6i Manuals" else "(root)"

        try:
            doc = fitz.open(fpath)
            n_pages = doc.page_count
            meta = doc.metadata or {}
            title = (meta.get("title") or "").strip()

            # TOC
            toc = doc.get_toc()
            toc_titles = [t[1] for t in toc[:60]]

            # Extract full text
            text_parts = []
            has_text = False
            img_count = 0
            for pno in range(doc.page_count):
                page = doc[pno]
                t = page.get_text("text")
                text_parts.append(f"\n\n===== PAGE {pno+1} =====\n\n{t}")
                if len(t.strip()) > 50:
                    has_text = True
                img_count += len(page.get_images(full=True))
            full_text = "".join(text_parts)

            # Save extracted text per module
            mod_dir = os.path.join(OUT_TEXT, module.replace(" ", "_"))
            os.makedirs(mod_dir, exist_ok=True)
            txt_name = fname.replace(".pdf", ".txt")
            with open(os.path.join(mod_dir, txt_name), "w", encoding="utf-8") as f:
                f.write(full_text)

            # First pages sample for classification (content summary)
            first_pages = full_text[:3000].replace("\n", " | ")

            results.append({
                "file": fname,
                "path": rel_path,
                "module": module,
                "size_kb": round(os.path.getsize(fpath) / 1024),
                "pages": n_pages,
                "pdf_title": title,
                "has_extractable_text": has_text,
                "images": img_count,
                "toc_count": len(toc),
                "toc_titles": toc_titles,
                "sample": first_pages[:1500],
            })
            doc.close()
            print(f"OK  [{module}] {fname} — {n_pages} pages, text={has_text}, imgs={img_count}")
        except Exception as e:
            results.append({
                "file": fname,
                "path": rel_path,
                "module": module,
                "error": str(e),
            })
            print(f"ERR [{module}] {fname} — {e}")

with open(OUT_JSON, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

total_pages = sum(r.get("pages", 0) for r in results)
print(f"\n=== TOTAL: {len(results)} files, {total_pages} pages ===")
print(f"Inventory JSON: {OUT_JSON}")
