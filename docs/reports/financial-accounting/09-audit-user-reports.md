# 09 — التدقيق والتقارير المخصصة والمتفرقات — FAS-REP (Phase 7)

> §33 Audit Trial + §34 User Reports + §22 FA Budget List + Advance Paid Report + Invoice/Payment Check = 5 تقارير ختامية.

---

## 1. §33 Audit Trial Report — **أدق ضبط تدقيقي في الحزمة**

**الوصف:** "processed for a particular financial period. You can view and print **all modifications and deletions done in FA transactions by various users**."

| # | المعيار |
|---|---|
| 1 | Property + FY |
| 2 | **Transaction Date / Updated Date** — "If you select Transaction date the audit report will audit **only those transactions that happened for the first time**. If you select **Updated date, then you can also view those transactions that were modified or deleted**" |
| 3 | Transaction Code |
| 4 | date range |
| 5 | **Modified and/or Deleted** — "view **only** modified **or** deleted transactions" |
| 6 | Ok |

**النقاط البنيوية:**
- **ثنائية توقيت التدقيق**: تاريخ المعاملة (النشأة الأولى) **مقابل** تاريخ التحديث (التعديل/الحذف) — أول فصل صريح بين **زمن الحدث وزمن تغييره** (بما يتجاوز MGT-23 الذي يجمعهما معاً).
- **وصلات Modified/Deleted و/أو** — تحكم مجموعة ثلاثي (معدل فقط/محذوف فقط/كلاهما).
- **"by various users"** — أثر متعدد المستخدمين معلن (توزيع مسؤولية).
- **"Trial" لا "Trail"** — نفس الخطأ الإملائي مثل MGT-23 — **خطأ منسوخ عابر للوحدتين** (دليل سلالة نصية مشتركة بين ملفي REP!).
- عائلة المحذوفات النهائية: **MGT §23 + FAS §2/2(2)/§33** — FN6i تتيح رؤية المحذوفات لكن **بلا استرجاع** (GAP-P موحد).

## 2. §34 User Reports — **منصة P&L المخصصة**

**الوصف:** "generate **customized P&L reports in department wise and consolidation of multiple reports** which are designed using **Create User Report under Setup**."

**المعايير (10 خطوات):**

| # | المعيار |
|---|---|
| 1 | Property |
| 2 | Month & Year |
| 3 | **country currency** من قائمة (عملات دول!) |
| 4 | From/To **Report numbers** (F1) |
| 5 | FY + **Budget type** |
| 6 | **مصفوفة قيمة العرض**: "absolute value / **round off value** / **(-ve) print in bracket** / include opening Balance / **Lakh / Million or Decimal** value" |
| 7 | **Print: Direct أو Excel** |
| 8 | **Load** → التفاصيل |
| 9 | **Tag YES** (double-click) |
| 10 | Ok |

**النقاط البنيوية:**
- **مولّد قوائم كاملة من Setup** (Create User Report) — القوائم المخصصة **تُصمم مسبقاً ثم تُشغَّل هنا** (تقريران: مصمم + مشغّل — نفس ثنائية Sales Report Definition في POS).
- **مصفوفة قيمة العرض (6 خيارات!)**: مطلق/مقرّب/**سالب بين قوسين** (محاسبة قانونية!)/مع رصيد افتتاحي/**Lakh/Million** (هندية!)/عشري — **أدق تحكم عرض رقمي في الحزمة**.
- **Direct/Excel** — ثاني Excel موثق (بعد MNT Parameter Listing) — قوائم مالية **تخرج Excel** (نضج إخراجي غير متوقع!).
- **دمج تقارير متعددة** (From/To Report numbers) — تقارير مركبة (Consolidation) — مقابل تعدد الملك (country currency — عملة عرض عالمية).
- **Load/Tag** رابع ظهور (يُفصّل في 01 §4).

## 3. §22 FA Budget List

**الوصف:** "generate a list of budget values defined for a specific financial period. The budgets values are reflected from the **Budget Account Codes option** and can be processed on the basis of **report formats defined in the Create User Reports option**."

- المعايير: Property + FY + **Budget type** — "**Press F1** in the Budget Types option to view a list of budgets defined".
- **موازنات بأنواع** (Budget type بالF1 — قائمة موازنات معرفة!) — عائلة موازنات الحزمة تتوج: FO (إيراد) · FNB (مبيعات/تكلفة) · MGT (شراء/استهلاك) · **FAS (حسابات GL بأنواع!)**.
- **تسلسل مع User Reports**: القائمة تُعرض بصيغ Create User Report — **الرابط الوحيد الموثق بين Budget وUser Report**.

## 4. Advance Paid Report — **ضيوف في قلب المالية**

**الوصف:** "view a report of **all the advances paid by the guests** at the property within a given date range."

- المعايير: Property + F3 FY + date range + Ok.
- **"advances paid by the guests"** — قراءة دقيقة: الإيداعات **المدفوعة من الضيوف** (للفندق) — **FAS يستعلم عن الفوليو من زاوية النقد** — جسر FAS→FO (Deposit) نادر التوثيق (أغلب الجسور باتجاه FAS).
- أبسط تقرير ضيوف في وحدة مالية — "سؤال الخزينة: كم إيداعات الضيوف لدينا؟".

## 5. Invoice / Payment Check

**الوصف:** "generate the **Invoice/Payment Check list report**."

| # | المعيار |
|---|---|
| 1 | Property |
| 2 | F3 FY |
| 3 | **Invoice checklist / Payment checklist** (ثنائية) |
| 4 | date range |
| 5 | Vendor range (F1) |
| 6 | **order by** من خيارات |
| 7 | Ok |

- **كشفان في تقرير واحد**: فواتير الموردين (Invoice) مقابل مدفوعاتها (Payment) — **أداة مطابقة فاتورة↔دفع** (النصف الثاني من Three-Way Match: GRN(MGT) ↔ Invoice ↔ Payment — الآن الثلاثي كامل عبر MGT-10 Supplier Bill + هذا التقرير!).
- **دورة المطابقة الثلاثية الكاملة الموثقة عبر الوحدتين:**
  - **GRN ↔ Receipt** (MGT §4.2/15.6)
  - **Bill ↔ Invoice** (MGT §10 Supplier Bill)
  - **Invoice ↔ Payment** (FAS هذا التقرير)

## 6. جدول العائلة الختامية

| التقرير | الوظيفة | الميزة القصوى |
|---|---|---|
| 33 Audit Trial | تدقيق | **Txn Date XOR Updated Date** + Mod/Del و/أو |
| 34 User Reports | قوائم مخصصة | **مصفوفة قيم 6** + Excel + دمج تقارير |
| 22 FA Budget | موازنات | Budget type بالF1 + صيغ User Report |
| Advance Paid | ضيوف | جسر FO معكوس الاتجاه |
| Invoice/Payment | مطابقة | **إكمال Three-Way Match** |

## 7. الأشباح الختامية (UNK-096 — تُغلق بهما الحزمة)

آخر بندين في TOC (تحت §34) **بلا جسم إطلاقاً**:
1. **IDS Crystal Report Designer** — **شبح متكرر!** نفس الاسم ظهر شبحاً في FOM-REP (UNK-078) — الآن في FAS-REP — **بنود TOC منسوخة عبر قوالب وحدات بلا جسم** — أقوى دليل على قوالب TOC مشتركة المصدر.
2. **Advice / Cheque iDesigner** — iDesigner (بلاحقة i!) مقابل Advice/Cheque Print (§24 العادي) — نسخة "مصمم" من مستند الدفع (تُقابل Print العادي بالمصمم — كما PMSPOL مقابل Police Report العادي في FO).

**مع رصيد عائلة الأشباح الختامي (Phase 7):**
| الوحدة | الشبح الختامي |
|---|---|
| FO | Report Designer + IDS Crystal (UNK-078) |
| POS | KDS §24 (UNK-083) |
| MGT | — (لا شبح ختامياً!) |
| **FAS** | **IDS Crystal + iDesigner (UNK-096)** |

**النمط الغالب:** ملفات REP الكبرى تُغلق ببنود مصممين/أنظمة وعد بلا جسم — **أثمنها IDS Crystal المتكرر** (نفس الاسم في وحدتين = قالب TOC مشترك، والغالب أنه مصمم تقارير Crystal Reports حقيقي ظل وعداً غير موثق).
