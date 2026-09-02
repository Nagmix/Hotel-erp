# 08 — التقارير (Reports) — وحدة Banquets

> ⚠️ **لا يوجد ملف BNQ-REP في الحزمة الـ 65** (GAP-BQ-D01) — الوحيدة بجانب Touch Screen بلا دليل تقارير مستقل. هذا الملف يجمع كل المخرجات الموثقة **داخل** الملفات الخمسة.

---

## 1. Function Prospectus (البروسبكتوس الوظيفي) — المخرج الرئيسي

| البند | الموثق | المصدر |
|---|---|---|
| البرنامج | Program ID: **FP-NBIDSFP** | SET §16 |
| **ترتيب الطباعة** | "SEQUENCE – This sequence will be followed to **print the Menu Groups** in Function Prospectus" (Menu Group Sequence) | SET §9 ص31 |
| حالة الطباعة | **FP Printed → أزرق** في Availability Chart | LUK §2 ص12 |
| حالة التثبيت | **FP Finalized → بنفسجي** | LUK §2 ص12 |

## 2. نماذج الطباعة الموثقة (Print Forms)

| النموذج | Program ID | المصدر |
|---|---|---|
| Function Prospectus | FP-NBIDSFP | SET §16 |
| Voucher | NB001AD | SET §16 |
| Bill Printing | NB001BL | SET §16 |
| Provisional Bill | NB001PB | SET §16 |
| **أنواع User Defined إضافية** | "Banquet Bill, **Business Event Order**, **Confirmation Letter**, **Cancellation Letter** etc." | SET §17 ص71 |

## 3. إيصالات الودائع (Vouchers — 9 أشكال!)

"Voucher for Cash/Card/Cheque deposit" × **(أصلي + Modified + Deleted)** — أنماط طباعة مستقلة لكل حالة تعديل — **سجل إثبات مالي مطبوع** (BIL §9 ص39-44).

## 4. مخرجات مدمجة في الشاشات

| المخرج | السياق | المصدر |
|---|---|---|
| Purchase-like **Tender/ملخص الإغلاق** | "summary of the transactions made by the cashier for the respective shift" | BIL §5 |
| **Vendor Evaluation** (BNQ لا — راجع MGT) | — | — |
| **Availability Chart/Function Room Availability** (طباعة ضمنية) | استعلامات العرض | LUK |
| Event Calendar (تقويم مطبوع؟) | [NOT DOCUMENTED] | SET §10 |

## 5. واجبات المرحلة 7 (تعويض فجوة المصدر)

1. **لا يمكن** تحليل تقارير BNQ من الحزمة — الخيارات: (أ) جمع المتطلب من Program Types + حقول المطابقة الموثقة هنا، (ب) مراجعة مستندات IDS المتاحة علنياً [خارج النطاق الحالي].
2. تحديد قائمة BEO (Business Event Order) كمواصفة قياسية صناعية (قوائمها الشائعة معروفة قطاعياً) — مع تعليم [INFERENCE] لكل حقل غير مستند.
3. ربط FP بالكيانات الموثقة (Menu Groups Sequence + Items + Tax structures من Print Forms).
