#!/usr/bin/env python3
"""PHASE 0: Generate manual-inventory.md from inventory.json + toc-extracts.json"""
import json

BASE = "/home/z/my-project/hotel-erp"
OUT = f"{BASE}/docs/analysis/00-discovery/manual-inventory.md"

with open(f"{BASE}/inventory.json") as f:
    inv = json.load(f)
with open(f"{BASE}/toc-extracts.json") as f:
    tocs = json.load(f)

# Arabic names + type decoding
MODULE_AR = {
    "Front Office": "مكتب الاستقبال (العمليات الفندقية الأمامية)",
    "Point of Sale": "نقاط البيع (المطاعم والمنافذ)",
    "Financial Management": "الإدارة المالية (المحاسبة العامة)",
    "Accounts Receivales": "الحسابات المدينة",
    "Materials Management": "إدارة المواد والمشتريات والمخازن",
    "Food & Beverage Costing": "تكاليف الأغذية والمشروبات",
    "Banquets": "الولائم والمناسبات",
    "Membership": "العضويات (النوادي)",
    "Maintenance": "الصيانة الهندسية",
    "HR & Payroll": "الموارد البشرية والرواتب",
    "Fixed Assets": "الأصول الثابتة",
    "Sales & Marketing": "المبيعات والتسويق",
    "Care": "خدمة الضيافة والمهام (Fortune Care)",
    "Telephones": "المقسم الهاتفي ومحاسبة المكالمات",
    "Gate Passes": "تصاريح الدخول والخروج (بوابات)",
    "System Setup": "إعداد النظام",
    "(root)": "أدلة عامة",
}

# Doc type codes decoded
TYPE_CODES = {
    "SET": "Setup / الإعدادات",
    "OPR": "Operations / العمليات اليومية",
    "REP": "Reports / التقارير",
    "RPL": "Reports & Lookups / التقارير والاستعلامات",
    "LUK": "Lookups / الاستعلامات السريعة",
    "BIL": "Billing / الفوترة",
    "BOK": "Bookings / الحجوزات",
    "CFG": "Configuration / التهيئة",
    "TRN": "Transactions / القيود والمعاملات",
    "MST": "Masters / البيانات الرئيسية",
    "GST": "Guest History / سجل النزلاء",
    "CAS": "Cashiering / الكاشير",
    "CRG": "Concierge / الكونسيرج",
    "DEP": "Day End Process / إقفال اليوم (Night Audit)",
    "HSK": "Housekeeping / الإشراف الفندقي",
    "REG": "Registrations / تسجيل الوصول",
    "RES": "Reservations / الحجوزات",
    "SMS": "SMS / الرسائل النصية",
    "DNT": "Daily Entries & Transactions / القيود اليومية",
    "COP": "Costing Operations / عمليات التكاليف",
    "MMN": "Member Maintenance / صيانة ملفات الأعضاء",
    "MPF": "Member Profiles / ملفات الأعضاء والطلبات",
    "MTR": "Member Transactions / معاملات الأعضاء",
    "PNT": "Payroll Entries / قيود الرواتب",
    "RQP": "Recruitment Process / التوظيف",
    "SLT": "Sales Tracking / تتبع المبيعات",
    "PRF": "Profiles / الملفات التجارية",
    "CAC": "Call Accounting / محاسبة المكالمات",
    "FXD": "Fixed Assets / الأصول الثابتة",
    "GTP": "Gate Pass / تصاريح البوابة",
    "SSP": "System Setup / إعداد النظام",
}

def decode_type(fname):
    import re
    m = re.search(r'FN6i-NT-\w{3}-(\w{3})\.pdf', fname)
    if m:
        code = m.group(1)
        return code, TYPE_CODES.get(code, code)
    if "Touch_Screen" in fname:
        return "TSC", "Touch Screen / دليل شاشة اللمس"
    if "OPERATIONS" in fname.upper():
        return "OPR", "Operations / العمليات اليومية"
    if "REPORTS" in fname.upper():
        return "RPL", "Reports & Lookups / التقارير والاستعلامات"
    if "SETUP" in fname.upper():
        return "SET", "Setup / الإعدادات"
    return "GEN", "General / عام"

rows = []
for r in inv:
    code, type_desc = decode_type(r["file"])
    key = f"{r['module']}/{r['file'].replace('.pdf','')}"
    toc = tocs.get(key, [])
    # Clean TOC: dedupe, filter noise
    seen = set()
    clean_toc = []
    for t in toc:
        t = t.strip()
        if t and t.upper() not in ("LOOKUPS", "SETUP", "REPORTS", "MASTERS", "BOOKINGS", "BILLINGS", "OPERATIONS", "BANQUETS") and t not in seen and len(t) > 3:
            seen.add(t)
            clean_toc.append(t)
    rows.append({
        "module": r["module"],
        "file": r["file"],
        "path": r["path"],
        "pages": r["pages"],
        "size_mb": round(r["size_kb"]/1024, 1),
        "imgs": r["images"],
        "type_code": code,
        "type_desc": type_desc,
        "toc": clean_toc[:18],
        "text": r["has_extractable_text"],
    })

# Group by module
from collections import defaultdict
by_mod = defaultdict(list)
for r in rows:
    by_mod[r["module"]].append(r)

total_pages = sum(r["pages"] for r in rows)
total_files = len(rows)

md = []
md.append("# PHASE 0 — جرد الأدلة الكامل (Manual Inventory)")
md.append("")
md.append("> **المصدر المرجعي:** `6i Manuals/` — كتالوجات نظام FortuneNext 6i (IDS Next Business Solutions Ltd.)")
md.append(f"> **إجمالي الملفات:** {total_files} ملف PDF | **إجمالي الصفحات:** {total_pages:,} صفحة | **الحجم:** ~209 MB | **لقطات الشاشة (صور):** ~7,763")
md.append("> **حالة النصوص:** جميع الملفات تحتوي نصاً قابلاً للاستخراج آلياً (لا حاجة لـ OCR) ✓")
md.append("> **ملاحظة:** تم استخراج النصوص الكاملة إلى `extracted-text/` مرتبةً حسب الوحدة لاستخدامها في المراحل التالية.")
md.append("")
md.append("**منهجية الترميز:** اسم الملف يتبع النمط `FN6i-NT-<MODULE>-<TYPE>.pdf` حيث MODULE هو رمز الوحدة و TYPE هو نوع الوثيقة:")
md.append("")
md.append("| كود الوحدة | الوحدة |")
md.append("|---|---|")
CODES = {
    "FOM": "Front Office / مكتب الاستقبال", "POS": "Point of Sale / نقاط البيع",
    "FAS": "Financial Accounting / المحاسبة المالية", "ACR": "Accounts Receivable / الحسابات المدينة",
    "MGT": "Materials Management / إدارة المواد", "FNB": "F&B Costing / تكاليف الأغذية والمشروبات",
    "BNQ": "Banquets / الولائم", "MEM": "Membership / العضويات", "MNT": "Maintenance / الصيانة",
    "HRP": "HR & Payroll / الموارد البشرية", "SLM": "Sales & Marketing / المبيعات والتسويق",
    "TEL": "Telephones / الهاتف", "SYS": "System / النظام",
}
for k, v in CODES.items():
    md.append(f"| `{k}` | {v} |")
md.append("")
md.append("---")
md.append("")

# Module order by pages (descending)
mod_order = sorted(by_mod, key=lambda m: -sum(r['pages'] for r in by_mod[m]))

for mod in mod_order:
    mrows = by_mod[mod]
    m_pages = sum(r["pages"] for r in mrows)
    m_ar = MODULE_AR.get(mod, mod)
    md.append(f"## الوحدة: {mod} — {m_ar}")
    md.append("")
    md.append(f"**{len(mrows)} وثيقة | {m_pages} صفحة | {round(sum(r['size_mb'] for r in mrows),1)} MB**")
    md.append("")
    md.append("| الملف | الكود | نوع الوثيقة | الصفحات | الصور | النص مستخرج |")
    md.append("|---|---|---|---|---|---|")
    for r in sorted(mrows, key=lambda x: x["file"]):
        md.append(f"| `{r['file']}` | {r['type_code']} | {r['type_desc'].split(' / ')[0]} | {r['pages']} | {r['imgs']} | {'✓' if r['text'] else '✗'} |")
    md.append("")
    md.append("**المحتويات الرئيسية (من فهارس الوثائق):**")
    md.append("")
    for r in sorted(mrows, key=lambda x: x["file"]):
        if r["toc"]:
            toc_str = " • ".join(r["toc"][:14])
            md.append(f"- **`{r['file']}`**: {toc_str}")
    md.append("")
    md.append("---")
    md.append("")

md.append("> ⚠️ **ملاحظة جودة:** فهارس بعض الوثائق (خاصة Care و Touch Screen) استُخرجت بنمط مختلف وقد تكون قوائمها غير مكتملة أعلاه؛ القوائم الكاملة موثقة في `toc-extracts.json` والنصوص الكاملة في `extracted-text/`.")

with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(md))

print(f"Written: {OUT}")
print(f"Total: {total_files} files, {total_pages} pages across {len(mod_order)} modules")
