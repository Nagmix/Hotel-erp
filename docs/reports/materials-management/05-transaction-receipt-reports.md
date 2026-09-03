# 05 — المعاملات والاستلام (Transaction & Receipt §4) — MGT-REP (Phase 7)

> §4.1–4.8 = **8 تقارير** — أكبر عائلة فرعية في MGT-REP — مرآة طبقة Transactions (OLTP) كلها.

---

## 1. §4.1 Transaction Checklist — الكشف الشامل لكل الحركات

**الوصف الحرفي:** "view **all types** of Inventory transactions based on postings made through the **Receipt, Issue, Adjustments, Receipt and Issue Returns** Menu Items."

**المعايير (ص13-15):**

| # | المعيار | القيم |
|---|---|---|
| 1 | Date range | — |
| 2 | Store | افتراضياً **كل المخازن** |
| 3 | Item range | — |
| 4 | **Transaction Type** | Receipts / Issue / Adjustments / **Receipt Returns / Issue Return** (خمسة أنواع) |
| 4a | شاشات فرعية تكيّفية | "If you select Receipt or Receipt Returns then select appropriate options **from the displayed screen**" · وكذا Issue · Adjustments · Issue Returns — **شاشة معايير تتبدل حسب النوع** (Adaptive Form) |
| 5 | **Single line space** | "keep space between two rows" — خيار تجميلي |
| 6 | **Remarks** | "if you want to view the **comments of customer**" |

**النقاط البنيوية:**
- **نموذج Adaptive UI موثق**: اختيار نوع المعاملة **يبدّل الشاشة نفسها** (4 شاشات فرعية لكل نوع) — أول توثيق صريح لنموذج "شاشة ديناميكية حسب النوع" في الحزمة.
- **"comments of customer"** — عبارة غريبة في سياق مخزني! (المستلم/الطالب وليس "customer") — **أثر نسخ/لصق من وحدة ضيف** — دليل تحريري عابر للوحدات يوثق دون مستوى تناقض.
- تسمية النوع الخامس "Issue Return" (مفرد Return) مقابل "Receipt Returns" (جمع) — تذبذب صرف تحريري.

## 2. §4.2 Receipt Register — سجل الاستلام بأدوات الترقيم الصفحي

**الوصف الحرفي:** "view Items received from Vendors along with other details... Additional options in the report include **Store Break - To reflect each Store on a new Page, Goods Receipt Note generation, Selective printing by Receipt types, Inclusion/Exclusion or reflection of only Complimentary Items**."

**المعايير (ص17-18):**

| # | المعيار |
|---|---|
| 1 | **Date / Month** + النطاق |
| 2 | Store |
| 3 | **Store Break / GRN generation** |
| 4 | **Vendor / Grr. No** + النطاق |
| 5 | خيارات أخرى |

**النقاط البنيوية:**
- **Store Break = ترقيم صفحي مؤسسي**: "each Store on a new Page" — توزيع الكشوف بين أمينة المخازن بحدود فيزيائية — أول خيار Pagination موثق بوظيفة اجتماعية.
- **GRN generation من داخل Register** — تقرير الاستلام **يولّد مستندات GRN** — الأداة التشغيلية المزدوجة (تقرير + مصدر مستندات).
- **ثلاثية Complimentary الحرفية**: "Inclusion/Exclusion **or reflection of only** Complimentary Items" — ثلاث حالات صريحة (ضمن/استبعد/اعرض فقط المجاني) — أغنى فلتر مجاني في الحزمة (POS Void/Comp ثنائي بلا "only" الصريحة).
- استرجاع بـ**Grr. No** (رقم إيصال الاستلام) — المفتاح التسلسلي للاستلام (يظهر مجدداً في VAT 24.1 بF1).

## 3. §4.3 Capital Goods Receipt — جسر الأصول الرأسمالية

**الوصف الحرفي (كامل!):** "In this report, you can view **VAT report details for the Capital Goods**."

- أصغر وصف في الوحدة (جملة واحدة) لكنه **أثقل جسراً**: البضاعة الرأسمالية المستلمة عبر MGT تحمل تفاصيل VAT — ربط ثلاثي:
  - **MGT-TRN** (استلام أصناف نوع Capital؟)
  - **FAS-FXD** (الأصل الرأسمالي: كود الأصل المرتبط/مجموعة الأصل)
  - **FAS-TRN** (VAT الأصول الرأسمالية — خصم ضريبي مدخلات للأصول).
- الشاشة والمعايير **مطابقة لـReceipt Register** (Date/Month + Store + Vendor/Grr. + خيارات) — قالب سجل الاستلام بمرشح نوع رأسمالي.
- يوثّق أن دورة الأصل تبدأ **من بوابة المخزن** (استلام رأسمالي → تفعيل أصل) — أعمق مما وثق modules/fixed-assets وحده (بوابة FA Start Date هناك = نقطة بدء الاحتساب، وهنا = نقطة الدخول المادي).

## 4. §4.4 Receipt/Issue by Group

- "consolidated figure of the Issues and Receipts are displayed" لكل **Item Group** + نطاق تاريخ.
- فلتر **Open Items** (تضمين الأصناف المفتوحة).
- مبسّط: Group × (Receipts/Issues) × Period — البوابة التحليلية الأولى قبل 4.5.

## 5. §4.5 Receipt/Issue Consolidate

- **خياران حصريان**: "Group wise Value" **أو** "item Consolidation required" — تجميع بالقيمة حسب المجموعة أو بالصنف.
- + Open Items checkbox.
- 4.4/4.5 ثنائية (by Group التفصيلي / Consolidate المجمّع) — نفس عائلة LUK "Receipt/Issue by Group".

## 6. §4.6 Consolidate Receipt Value

**الوصف:** "view a list of Consolidated Receipts for the specified Store or for all Stores. The user can sort the report based on **Vendor Name or Vendor Code**."

- **نمطا انتقاء المخزن**: "either select **all and choose the stores** or you can select **Range and enter a range of Stores Codes**" — إما (الكل ثم انتقاء) أو (نطاق أكواد) — نمطا UI موثقان صراحة لاختيار مجموعة مخازن (يظهر مجدداً في 24.1 VAT بAll/Range).
- **فرز بمفتاح اسم المورد أو كوده** — القيمة الاستلامية مجمّعة لكل مورد (الوجه المورد-مح-centric للقيمة).
- خطأ ترقيم خطوات: من 4 تقفز إلى 6 (بلا خطوة 5 — ص29).

## 7. §4.7 Supplier Receipt Register

- "receipt details processed for a selected range of **suppliers** for all or for selected Stores" — **Item wise / Group wise**.
- مقارنة بـ4.2 (Receipt Register): 4.2 = استلام حسب المخزن/GRN (عام) · 4.7 = استلام **حسب المورد** (تفصيلي بالنطاق) — ثنائية المحور: مخزن-مح مقابل مورد-مح.

## 8. §4.8 Opening Balance List — بوابة "الشهر الجاري"

**الوصف الحرفي:** "view the Opening Balance of each item available in the selected Store **as on current Month and Year**."

- **قيد "الآن"**: الرصيد الافتتاحي **للشهر/السنة الجارية حصراً** — لا معامل تاريخ حر إطلاقاً — أضيق نطاق زمني في الوحدة (يقابل §6' Closing Stock الذي يقبل "any given date" — ثنائية: افتتاحي=الآن / ختامي=أي تاريخ!).
- معايير أصلية: Store فقط (أبسط شاشة في الوحدة: معيار واحد!).
- الجسر: Opening Balance لكل شهر = ناتج ترحيل "Stock Balance Transfer" اليومي (FNB-COP: "becomes opening balance for next day") هنا بصيغة شهرية.

## 9. جدول العائلة

| # | التقرير | المحور | الميزة الفريدة |
|---|---|---|---|
| 4.1 | Transaction Checklist | النوع (5 أنواع) | **Adaptive UI** + "customer comments" |
| 4.2 | Receipt Register | المخزن/GRN | **Store Break + GRN gen + ثلاثية Comp** |
| 4.3 | Capital Goods Receipt | **رأسمالي** | جسر FXD/FAS VAT |
| 4.4 | R/I by Group | المجموعة | Consolidated + Open |
| 4.5 | R/I Consolidate | تجميع | **Group-Value XOR item-Consolidation** |
| 4.6 | Consolidate Receipt Value | المورد | **All/Range نمطا الانتقاء** + فرز Name/Code |
| 4.7 | Supplier Receipt Register | المورد | Item/Group wise |
| 4.8 | Opening Balance List | الشهر الجاري | **current Month/Year فقط** |

**الاكتشاف التجميعي للعائلة:** §4 يغطي الاستلام من **5 زوايا محاور مختلفة** (النوع/المخزن/الرأسمالي/المجموعة/المورد) + الافتتاحي — تعدد الزوايا المنهجي أوسع من أي عائلة في FO/POS (التي كانت محاورها زمنية/فندقية غالباً) — MGT تحلل نفس البيانات بمحاور **كيانية** متعددة.
