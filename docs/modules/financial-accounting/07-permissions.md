# 07 — الصلاحيات (Permissions) — وحدة FAS

> الموثق نصاً في FAS-SET/FAS-TRN/FAS-MST. المصفوفة الشاملة (SYS-SSP) في Phase 8.

---

## 1. Transaction Type Rights (FAS-SET §5 ص11-12)

- **النطاق:** Property + **User ID** (F1) → جدول أكواد المعاملات → **Tag = YES** يمنح الوصول؛ **Select All** للكل.
- **الدلالة:** صلاحية استخدام كود معاملة (نوع قيد) — تتحكم بمن يستطيع إدخال Receipts/Payments/Journals...

## 2. Voucher Authorization (FAS-TRN §9 ص45)

- **"authorization levels that a user may need to process a voucher"**.
- **نطاق تاريخي** لكل تفويض (صلاحية مؤقتة بالمدة).
- **ثلاثة مستويات: Level 1 / Level 2 / Level 3** — تدرج اعتماد القسائم.

## 3. صلاحيات موثقة ضمنية

| السلوك | المصدر |
|---|---|
| تعديل الحساب المرتبط في قيد AR (F5) — قبل الحفظ فقط | FAS-SET §11 |
| **Day Book (Q) يسمح بتعديل المعاملة مباشرة** (drill-down → تعديل → Confirm → Save) | FAS-LUK §2 |
| تغيير Cost Center في رابط POS مسموح | FAS-SET §7 |
| Vendor Black Listed يسجل **مَن** أدرجه والسبب | FAS-MST §1 |

## 4. الفجوة

`[PENDING]` مصفوفة SYS-SSP الكاملة (أدوار × وظائف × خصائص) + علاقتها بمستويات Voucher Authorization — تُبنى في `docs/security/` (Phase 8).
