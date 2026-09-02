# 08 — التقارير (Reports) — وحدة Materials Management

> **MGT-REP (112 ص) مؤجل بالكامل للمرحلة 7** وفق بروتوكول الجلسات (التقارير تُجمع لكل الوحدات في مرحلة موحدة). هذا الملف يوثق: (1) التقارير المُشار إليها نصاً خارج REP، (2) مخرجات LUK القابلة للطباعة، (3) أشكلة الطباعة المرجعية.

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

## 5. مصير المرحلة 7 (واجبات مؤجلة موثقة)

1. قراءة MGT-REP كاملاً (112 ص — ثاني أكبر REP في الحزمة بعد FOM-REP).
2. فهرسة كل تقرير: الاسم/المعايير/الفلاتر/المخرجات/الطباعة.
3. المطابقة مع قائمة LUK أعلاه (منع الازدواج).
4. ربط FSN/Vendor Analysis/Ledger بالمعايير المالية في FAS-REP.
