# 03 — تقارير دورة المشتريات — MGT-REP (Phase 7)

> §2 Requisition Status + §3 PO Status + §19 Comparative Statement + §10 Supplier Bill = 4 تقارير — "حالة المستندات" و"تحقق الفواتير" في دورة DPR→PR→PO→GRN→PJV.

---

## 1. §2 Requisition Status — حالة طلبات القسم (DPR)

**الوصف الحرفي:** "the user can view the status of Purchase Requisitions. The user can view the **pending requisition, if the required items have not been received or if they are partially received** and **closed if the items are received completely**."

**مصفوفة الحالة الثلاثية:**

| الحالة | شرطها الدلالي (حرفي) |
|---|---|
| **Pending** | لم تُستلم الأصناف **أو استُلمت جزئياً** — Pending تغطي العدم والجزئية معاً! |
| **Closed** | استلام **كامل** |
| All | الافتراضي: "By default the report will be generated for all requisitions" |

**المعايير (ص7-8):**

| # | المعيار | ملاحظة |
|---|---|---|
| 1 | **Date range / Month range** | ثنائية النطاق الموحدة |
| 2 | Property | تعدد الأملاك |
| 3 | Department | القسم الطالب |
| 4 | **DPR range** + F1 | أرقام طلبات القسم — **F1 lookup** (نفس عائلة مفاتيح البحث FO/POS) |
| 5 | All/Pending/Closed | الافتراضي All |

**النقاط البنيوية:**
- **Partial يبقى Pending** — لا حالة "Partially Received" رابعة (مقابل Closed/Cancelled/Pending في PO Status §3 الذي يملك **أربع** حالات!) — عدم تناظر حالة بين مستندين في نفس الدورة → يُسجل كتفرقة دلالية (تُستكمل في جدول §2/§3 أدناه).
- تقابل LUK: "Requisition Status · Authorization Details" (استعلامات سريعة) — REP يضيف Property/Department/DPR range/F1.

## 2. §3 PO Status Report — حالة أوامر الشراء (4 حالات!)

**الوصف:** "view the status of Purchase Order based on a range of Purchase Order number or for a given date range. The report displays brief details of Purchase Order for Items with the quantity ordered, **quantity received up to date** along with the status of the order i.e. Pending, Closed or Cancelled."

**المعايير (ص10-11):**

| # | المعيار |
|---|---|
| 1 | **By PO / By Vendor** (بعدا التجميع) |
| 2 | PO Date, PO #, **Upto Date** |
| 3 | All / Pending / Closed / **Cancelled** |
| 4 | PO# range (إن اختير By PO) |

**النقاط البنيوية:**
- **كمية مطلوبة × كمية مستلمة حتى تاريخه** — تتبع تقدم التنفيذ (Open Quantity = ordered − received ضمنياً) — تقرير "الفجوة التنفيذية" لأوامر الشراء.
- **حالة رابعة: Cancelled** — موجودة هنا **وغيبة من §2 Requisition** — هل طلبات القسم لا تُلغى أبداً؟ (في LUK وُثق "Cancelled & Closed PO" فقط) → **سؤال حالة DPR المفقودة** يُدرج في UNK-095.
- **Upto Date** — تاريخ قطع (as-of) لحساب "received up to date" — تقرير زمني نقطي.

**جدول عدم التناظر §2/§3:**

| المستند | الحالات الموثقة | Partial | Cancelled |
|---|---|---|---|
| DPR (Requisition §2) | Pending/Closed/All | Pending يبتلعها | **غائبة** |
| PO (§3) | Pending/Closed/Cancelled/All | ضمن "received up to date" | **موجودة** |

## 3. §19 Comparative Statement — مقارنة عطاءات الموردين

**الوصف الحرفي:** "view the comparative analysis of quantity, rate etc between multiple vendors. This report is generated based on **vendor analysis**."

**المعايير (ص100):**

| # | المعيار |
|---|---|
| 1 | **Quotation Month and Year** |
| 2 | Quotation Number — أو double-click للاختيار من قائمة |

**النقاط البنيوية:**
- **تقرير قرار الشراء**: يعرض كميات وأسعار نفس الصنف عبر موردين متعددين من عطاء واحد — أداة اختيار المورد (قبل PO).
- يقابل **Comparison Sheet** في DNT §7 ("view the Comparison list of the Quotations created") — REP/DNT تكرران القدرة من بوابتين (تقرير REP مقابل مخرج DNT) — نفس ظاهرة تعدد البوابات في FO.
- محرك العطاءات: **Purchase Quotations** من MGT-DNT §7 (إنشاء العطاء + Tender Form الطباعة) — هنا التحليل النهائي.
- **Month/Year + Number** — مفتاح استرجاع العطاء — لا نطاق تواريخ حرة (العطاء كائن محدد المرجع).

## 4. §10 Supplier Bill — تحقق فواتير الموردين اليومية

**الوصف الحرفي:** "view and **verify** bills or statements furnished by vendors against **daily and contracted items normally perishables**, supplied to the Hotel on a daily basis for a range of dates."

**المعايير (ص68-69):**

| # | المعيار |
|---|---|
| 1 | Supplier codes range |
| 2 | Date range options + **الشهر** |
| 3 | **Credit Days** option |

**النقاط البنيوية:**
- **كلمة "verify" — البعد الوظيفي الوحيد بالاسم**: التقرير مصمم **للمطابقة** (فواتير المورد ↔ استلامات النظام) — نواة Three-Way Match قبل أن يكون للفهارس اسم.
- **"daily and contracted items normally perishables"** — الاستهداف المعلن: مواد سريعة التلف تُورد يومياً بعقد (الخضار/اللحوم/الألبان) — عائلة عقد Supplies اليومية (Standing Orders) — هنا يقفز الجسر إلى **Standing PO** (15.4) وContract Master (6.4).
- **Credit Days** كمعيار — ربط التحقق بأعمار الذمم (فواتير وصلت أجلها؟) — نافذة على تكامل Dائن مع FAS/AR (وجه المدين في ACR له Night Audit — وجه الدائن هنا له Supplier Bill).
- **العلاقة مع FAS**: فاتورة المورد التي تتحقق هنا هي التي ستدخل PJV (Purchase Journal Voucher) في FAS — نفس دورة GRN (15.6): "forward a copy to the Finance department for making payments".

## 5. خريطة دورة المشتريات كما تكشفت من الطبقة الأربع

```
DPR (طلب قسم) ──§2 Requisition Status──┐
                                        │ (حالة: Pending/Closed فقط!)
Quotation (عطاء) ──§19 Comparative──→ اختيار المورد
                                        │
PR/SWO ──§15.1/15.5 طباعة──→ PO ──§3 PO Status──→ (حالة + Cancelled + qty recd)
                                        │
Standing PO (تعهد يومي) ──§15.4 طباعة──→ GRN (استلام) ──§4.2/§15.6──→ نسخة → FAS للدفع
                                        │
Vendor Bill (يومي/تعهد سريع التلف) ──§10 Supplier Bill (verify)──→ PJV (FAS)
```

**الاكتشاف التجميعي:** الطبقة تقدم **حالة لكل مرحلة من دورة المستندات** (DPR→PO→GRN→Bill) — "مرآة دورة" كاملة — أول وحدة في المرحلة 7 تغطي دورة مستندات كاملة بأربعة تقارير حالة/تحقق متسلسلة.
