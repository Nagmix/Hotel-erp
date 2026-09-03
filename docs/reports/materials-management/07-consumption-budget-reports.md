# 07 — الاستهلاك والموازنات (Consumption & Budget) — MGT-REP (Phase 7)

> §5.1–5.4 (+R2 Variant) + §22.1–22.2 = 6 تقارير — "من أين خرجت المادة؟" و"كم كان مسموحاً؟".

---

## 1. §5.1 Cost Center Consumption

**الوصف:** "view Items consumed by Cost Centers, **consolidated or Department**. The report is generated for a range of Items or Group for selected or All Stores."

**المعايير (ص35-36):**

| # | المعيار |
|---|---|
| 1 | Date range |
| 2 | **Consolidated / Cost Center / Department** + اختيار CCs/Departments |
| 3 | Stores |
| 4 | **Item / Group** + النطاق |

**ثلاثية التجميع** (لا ثنائية!): استهلاك مجمّع / حسب CC / حسب Department — Department وCC **ليسا شيئاً واحداً** في معمارية FN6i (Department هيكل تنظيمي من HRP-SYS · CC وحدة تكلفة محاسبية من FAS-TRN) — التقرير يخير بين منظورين محاسبيين مختلفين للاستهلاك.

## 2. §5.2 Cost Center Consumption Summary

**المعايير (ص37-38):** Detail/Summary · CC (افتراضياً الكل) · Store + **Item Group** · **All / Stockable / Direct**.

**النقاط البنيوية:**
- **ثلاثية Stockable/Direct/All** — ثنائية نوع الصنف الأساسية من ماستر SET تصل كفلتر تقرير: هل الاستهلاك من المخزون المُدار (Stockable) أم الشراء المباشر للاستهلاك (Direct)؟ — **سؤال تصنيف تكلفة جوهري**: Direct = مصروف فوري، Stockable = استنزاف أصل جاري.
- يقابل FNB "Standard vs Actual" لكن هنا بلا علاقة بالوصفات — استهلاك مادي خالص.

## 3. §5.3 Group Consumption Month Range

- Stores + Date range + **Consolidated / Cost Center wise** + **Print Options** (ص41).
- "Item Group wise consumption for a specified store and date range" — استهلاك المجموعات عبر نطاق شهور (Month Range في الاسم).

## 4. §5.4 Group Consumption Month Range – **R2** (لاحقة الإصدار الأولى!)

**الوصف (شبه مطابق لـ5.3):** "you can view Item Group wise consumption for a specified store and **month range**. You can generate a consolidated or Cost Center wise report and based on other specifications."

**مقارنة النصين:**

| البند | 5.3 | 5.4 (R2) |
|---|---|---|
| الوصف | "for a specified store and date range" | "for a specified store and month range" |
| التجميع | Consolidated/Cost Center wise | Consolidated/Cost Center wise |
| Print Options | **مذكورة صراحة** | **غير مذكورة** |
| الشاشة | 4 معايير | 3 معايير |

**النقاط البنيوية:**
- **"– R2" لاحقة إصدار تخطيط (Layout Release) في اسم تقرير** — أول مرة في الحزمة يعلن اسم التقرير نفسه أنه **نسخة ثانية من تخطيطه** (R = Release/Report-2) — بعد أن رأينا أشباحاً وتكرارات، هذا **نمط رابع من تعدد النسخ: تقريران متعايشان باختلاف تخطيطي**.
- الفرق التخطيطي الفعلي **غير قابل للتحقق** (تخطيطات الصور غائبة — D06) → **UNK-089**: ما الذي يميز R2؟ (اتجاه العرض؟ أعمدة إضافية؟ إعادة ترتيب؟).
- قرار تحويلي: هل يُدْمَجان (كDiscount Register في POS) أم يُبقيان (كتنسيقي Day Book Format 2 في FAS-REP القادمة!)؟ — FAS يوثق "Day Book (Format 2)" و"Trial Balance Format 2" بنفس النمط → **عائلة لاحقات التخطيط عابرة للوحدات** (R2 هنا / Format 2 هناك).

## 5. §22.1 Budget Actual Consumption

**الوصف:** "view details on the Purchase or **consumption pattern** for items for the **defined financial year**."

**المعايير (ص103):** **Financial Year + Month/Year** · **Purchase / Consumption** (ثنائية البوصلة).

**النقاط البنيوية:**
- **ثنائية Purchase/Consumption** — الموازنة تقاس على **بعدين مختلفين**: ما اشتُري (تدفق نقدي/التزام) وما استُهلك (استنزاف مخزون) — أول موازنة في الحزمة بهذه الثنائية (FNB موازناتها Sales/Cost · FO موازنتها إيرادية).
- **FY + Month** — إسناد سنة مالية (يقابل Budget Master في MGT-SET §… + FAS Budget) — الفترة المحاسبية تحكم فترة الموازنة.
- يقابل FAS-REP §22 "FA Budget List" (موازنة أصول!) — عائلة موازنات متعددة الأنواع عبر الوحدات.

## 6. §22.2 CC Budget Consumption

- "Purchase or consumption pattern **Cost Center wise** for a range of Items/Groups **for the specified period of the current financial year**" — **current FY** فقط (قيد "السنة الجارية" — مقابل 22.1 الذي يقبل FY معرفاً!).
- تناظر عائلي: 5.1 (CC Consumption تفصيلي) ↔ 22.2 (CC Budget مقيّد) — العمود الفقري: CC كوحدة مساءلة استهلاك.

## 7. سلسلة "سؤال الاستهلاك" الكاملة كما كشفتها الوحدة

| السؤال | التقرير | المستوى |
|---|---|---|
| **مَن** استهلك؟ | 5.1/5.2 | CC / Department / Consolidated |
| **ماذا** استُهلك؟ | 5.1/5.3 | Item / Group |
| **من أي نوع** المخزون؟ | 5.2 | Stockable / Direct |
| **متى**؟ | 5.3/5.4 | Month Range (+ R2) |
| **كم كان مسموحاً**؟ | 22.1/22.2 | Budget (Purchase XOR Consumption · FY) |
| **بأي كفاءة** تحوّل؟ | §21 Efficiency (→ 08) | Yield % |

**التجميع:** عائلة الاستهلاك في MGT أدق من FNB في البُعد الكياني (CC/Department/Type) وأبسط منها في البعد المنهجي (لا Standard/Actual ولا Recipes) — الاثنان يلتقيان في "Cost Center Consumption" (FNB: "Actual is arrived based on consumption at cost centers" — نفس الاسم!) — **أسماء متطابقة عبر وحدتين لمفهوم واحد** (يُرجَّح أن FNB تستهلك نفس بيانات MGT).
