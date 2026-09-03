# 08 — التقارير (Reports) — وحدة Materials Management

> **MGT-REP مكتمل الآن (Phase 7/الجلسة 18)** ووُثّق كاملاً في **[`docs/reports/materials-management/`](../../reports/materials-management/)** — هذا الملف يحتفظ: (1) بالتقارير المُشار إليها نصاً خارج REP، (2) بمخرجات LUK القابلة للطباعة، (3) بأشكلة الطباعة المرجعية، (4) بواجبات المرحلة 7 المنجزة.

---

## 1. تقارير موثقة بالنص خارج REP

| التقرير/المخرج | السياق الموثق | المصدر |
|---|---|---|
| **FSN Analysis Report** | "Classify Items as Fast, Slow and Non-Moving in the FSN analysis report" — الصيغة الكاملة موثقة (BR-MG-18) | SET §18 ص49-50 |
| **Vendor Evaluation (نموذج)** | "An evaluation form is sent to the vendor... Click Print to generate the report. The report will be generated in the following format" — نموذج استبيان قابل للطباعة | DNT §7 ص48-49 |
| **Tender Form** | "This option is used for **print** the Tender form after creating the quotation" — نموذج عطاء رسمي | DNT §7 ص53-55 |
| **Physical Stock Variance Report** | "alerting if the **Physical Stock Variance report has been checked**" — **شرط إجرائي قبل تحديث الفروقات** (يُتحقق أن التقرير روجع!) | DNT §14 ص72 |
| **Stores Ledger** | الغرض المباشر من Process Store Ledger: "to enable the **printing of Stores Ledger**" | DNT §15 ص73 |
| **Purchase Requisition (طباعة/بريد)** | "Print/Email/Print and Mail the Purchase Requisition" | DNT §1 ص7 |
| **Vendor Analysis** | يُبنى على Vendor Rating (Sequence) + Terms (Grade Sequence): "The ratings defined here can be used in the Vendor analysis" | SET §§7-8 |
| **Comparison Sheet** | "view the Comparison list of the Quotations created" — مقارنة عطاءات قابلة للطباعة | DNT §7 ص56 |

## 2-أ. MGT-REP (مكتمل — Phase 7/الجلسة 18)

قُرئ كاملاً (112 ص / 1,745 سطر — 24 رقماً بابل قسما «6» مزدوجاً + 39 فرعياً = 55 ورقة/~53 فريداً) ووُثّق في **[`docs/reports/materials-management/`](../../reports/materials-management/)** (12 ملفاً 00→11 — نظرة عامة · محرك Print-Forms-عبر-FAS · 8 عائلات · مصفوفة تواريخ ببوابات ثلاث جديدة · Mapping F-MR-1..16 + GAP + AC + Smoke 20).

**أهم ما أضافته قراءة REP لهذه الوثيقة (تُستكمل بها الأقسام أعلاه/أدناه):**

| الإضافة | الشاهد | التفصيل |
|---|---|---|
| **Print Forms = FAS-SET §15** (Pgm.ID) — طباعة PO/SPO/GRN معلقة ببرامج لكل عميل | 15.3/15.4/15.6 | `reports/materials-management/04` §1 — القسم 3 أعلاه يتصل الآن بمصدره الرسمي (والتمييز عن SET §28!) |
| **GRN نسخة → Finance للدفع** | 15.6 | المسار المادي الموثق MGT→FAS (قبل أي PJV) |
| **FSN معامل داخل شاشة التقرير** (double-click Days) | §12 | تكامل مع SET §18 أعلاه (BR-MG-18) — من يملك الشاشة؟ UNK-094 |
| **VAT بـassessment year + PJV-Wise** | 24.1 | امتثال هندي استلامي — يقابل PAN (POS) وTDS (FAS القادمة) |
| **Audit Trial يعرض المحذوفات** | §23 | "modified AND deleted" — أوسع مدى تدقيقي في الحزمة |
| **رصيد ثلاثي الحيازة** (مخزن/فرعي/CC) + بوابات زمنية جديدة (الآن-فقط ×2 · بيانات-مقيّد ×1) | 16.x/4.8/17/18.1 | `reports/materials-management/06` + `10` |
| **ABC/FSN/Efficiency** — ثلاثية المنهجيات الكلاسيكية | 11/12/21 | `reports/materials-management/08` — أوراق Pareto/Yield موثقة حرفياً |
| تناقضات ثلاث C-MR-01..03 (قسم 6 مزدوج · 6.1=1 حرفياً · VAT=Tax وصفاً) | TOC/الجسم | `reports/materials-management/00` §2 |

## 2. مخرجات Lookups القابلة للطباعة (زر Print في كل واحد)

كل استعلامات LUK العشرين تنتهي بعرض نتيجة + زر طباعة ("Click Print to take a print of the displayed information" — تتكرر في كل قسم):

**المجموعة التشغيلية (طلبات):** Requisition Status · Indent Status · Indent Status by Item · Authorization Details · PO Status · PO Status by Vendor · Cancelled & Closed PO · Pending PO · SPO Status · SWO Status.

**المجموعة المخزنية:** Receipt/Issue by Group · Store Balance by Date · Item Stock Status · Item Stock Balance · Item Stock Balance (Nil) · Item Balance by Date · Item Stock by CC.

**المجموعة التحليلية:** Consumption Detail · Group Cons Month Range (بتعمق ثلاثي) · Vendor Selection (آخر استلام/سعر) · Spending Pattern (مقارنة سنوية).

## 3. أشكلة الطباعة (Print Forms)

| العنصر | المواصفة |
|---|---|
| Foot Notes (SET §23) | حاشية ثلاثية المناصب لكل فئة تقرير: "Food Cost Report / Purchase Order Print / Vouchers" — Note 1/2/3 |
| User Defined Print Forms (SET §28) | "customize the format of bills, vouchers, slips... column width, page properties" — **يحيل إلى Getting Started (خارج الحزمة — GAP-SYS-D02)** |
| لافتة Short Name | كل مرجع (Store/Group/Terms/CC) يحمل اسماً قصيراً "used during printing process" — **تقليص عرض الأعمدة في المطبوعات** |

## 4. بريد الوحدة (Email Access Rights)

- قوالب بريد **لكل Program Type** في الوحدة (راجع 02-configuration §3) + CC/BCC + قالب افتراضي.
- الاستخدام الموثق: PR "Print and Mail" — **مرشح تضمين التقارير** في الإشعارات.

## 5. مصير المرحلة 7 (واجبات مؤجلة — **منجزة بالجلسة 18**)

1. ~~قراءة MGT-REP كاملاً (112 ص)~~ → **منجز** (1,745 سطراً).
2. ~~فهرسة كل تقرير~~ → **منجز** (55 ورقة/~53 فريداً — `reports/materials-management/00`).
3. ~~المطابقة مع قائمة LUK أعلاه (منع الازدواج)~~ → **منجز** — تقاطعات موثقة (Requisition/PO Status · Store Balance by Date · Item Stock · Consumption) — REP دائماً أوسع معايير (Store Break · ثلاثية Comp · R2).
4. ~~ربط FSN/Vendor Analysis/Ledger بالمعايير المالية في FAS-REP~~ → **منجز جزئياً من جهة MGT** (Print Forms + GRN→Finance + PJV + Capital Goods VAT) — يُستكمل من جهة FAS بعد قراءتها في نفس الجلسة.
