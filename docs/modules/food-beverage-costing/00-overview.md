# 00 — نظرة عامة (Overview) — وحدة FNB (Food & Beverage Costing)

> **تكاليف الطعام والشراب**: **العقل التحليلي لربحية المطاعم** — تستخرج المبيعات من POS والاستهلاك من Materials Management، وتضيف **المحرك الوصفاتي النظري** (Recipe/Sub Recipe بتكلفة الحصة ومقارنة السعر)، **وجرد المطابخ اليومي** (فعلي مقابل حاسوبي → عجز/فائض → رصيد افتتاحي للغد)، **والميزانيات** (بيعية بالقيمة/PAX وتكلفية بالنسبة المئوية) — ثم تنتج تقارير Sales Analysis وCost Report وProfitability Analysis وStandard vs Actual. **صفر قيود GL** — وحدة MIS خالصة بأضخم تدفق وارد في المشروع. المقروء عميقاً كاملاً (الجلسة 14): **SET (14 ص/4 أقسام) + COP (19 ص/9 وظائف) + LUK (15 ص/7 استعلامات) + REP (28 ص/13 تقريراً) = 76 ص كاملة**.

---

## 1. حدود الوحدة

| البند | الوصف الموثق |
|---|---|
| الاسم النظامي | Food & Beverage Costing — قوائم فرعية: **Setup / Costing Operations / Lookups / Reports** (TOC الملفات الأربعة) |
| الوظيفة الجوهرية | **خمس وظائف طبقية**: (1) Setup — 4 أقسام (تاريخ بدء التكلفة **بوابة تفعيل أحادية الاتجاه** · ربط مطعم↔مطبخ↔مركز تكلفة · ميزانيات بيع/تكلفة · ماستر الوصفات)؛ (2) Costing Operations — 9 وظائف (استخراج ETL · جرد مطابخ · مخزون افتتاحي · **مبيعات غير محوسبة** · استهلاك يدوي · تحويلات ثلاثية · أصناف مفتوحة/معدلات · ترحيل أرصدة · **طلب آلي وصفي**)؛ (3) Lookups — 7 استعلامات تحليلية؛ (4) Reports — 13 تقريراً (أثقل حصيلة تقارير لكل صفحة مقروءة في المشروع) |
| المركز المعماري | **وحدة MIS تحليلية نقية**: النص الحرفي — "Sales and Consumption details **will get extracted** from the Point of Sales and Materials Management modules **for generation of Sales and Cost MIS Reports**" — أضخم مستهلك وارد للبيانات التشغيلية (POS + MGT كاملين) وأكبر منتج تقارير إدارية، **بلا قيد GL واحد ولا Revenue Code واحد** في 76 صفحة (مقابل TEL التي وحدت كل نوع برقم إيراد!) |
| نمط التشغيل | **دفعات ليلية/دورية** (Costing Extraction بتاريخ من-إلى) **أو لحظي** (INI#368 ONLINEFBCOSTING) + **جرد يومي يدوي** (Kitchen Stock) + **حاجب لحظي على POS نفسه** (SWITCH 511: كمية > الرصيد الحالي → لا بيع عند KOT punch!) + استعلامات آنية |
| النطاق | مطاعم/منافذ POS كلها · 4 أنواع تكلفة (**Food / Liquor / Soft Drinks / Smokes-Tobacco**) · مطابخ MGT · مراكز التكلفة · وصفات 6 أرقام بنِصف مصنّع قابل للمشاركة · جلسات (فطور/غداء/عشاء) · أنواع KOT (Standard/**NC**) · أنواع NC (مجاني/تلف/استهلاك داخلي) · ميزانيات شهرية بالتقويم اليومي · مخزون فعلي/تسوية · تحويلات قيمة/مطبخ/نوع تكلفة · طلب آلي من الوصفات إلى MGT · 13 تقريراً + 7 استعلامات بأعمدة 80/132 |
| خارج النطاق | أي قيد GL أو Revenue Code (راجع 11) · فواتير أو تسويات (المبيعات تُحصَّل في POS/FO — هنا تحليل فقط) · إدارة أصناف أو مخازن (ملك MGT — FNB تستهلك وتطلب فقط) · موظفون/صلاحيات موثقة (لا ذكر واحد!) · بطاقات تكلفة إصدارية مؤرخة (لا Applicable From للوصفات — عائلة الخلود الزمني غائبة!) |

> ⚠️ **أربع ملاحظات معمارية كبرى:** (1) **بوابة التفعيل أحادية الاتجاه** — "CAUTION: Once the Start Date is entered, **updating the same will not be allowed**" + شرط أهلية تشغيلية صريح (POS وMGT يعملان أولاً وإلا "MIS reports will not be generated due to insufficient details") — أشد باب دخول وحدة صرامة في المشروع. (2) **حاجب POS مُدار من سياق FNB** — SWITCH 511 (autodeductionliqsale=0) يجعل **كبس KOT نفسه** يتحقق من الرصيد الحالي ويمنع البيع — سلوك وحدة أخرى يُضبط من هنا! (3) **المعادلة المالية الوحيدة موثقة مرتين بصيغ متقاطعة** — COST % = Cost per Portion / PRICE × 100 في SET، وVariance Sign (فعلي > ميزانية → سالب) في SET أيضاً — كل المحاسبة هنا نسب ومقارنات. (4) **تناقض تسمية Standard/Actual بين LUK وREP** — الأقواس في كلا الملفين تقول (Consumption)/(Recipe) لكن متن REP يحسم: Standard = الوصفة، Actual = الاستهلاك في مراكز التكلفة (راجع 13 + سجل التناقضات).

## 2. جرد الوظائف الموثقة (4 + 9 + 7 + 13 = 33 وظيفة/تقريراً/استعلاماً)

| الدليل | الوظائف | العدد | المصدر |
|---|---|---|---|
| **FNB-SET** (Setup) | Costing Start Date · Costing Link (+Defaults) · Sales/Cost Budgets · Recipe/Sub Recipe Master (6 تابات) | 4 | TOC SET ص1 |
| **FNB-COP** (Costing Operations) | Costing Extraction (INI#368 + SWITCH 511) · Kitchen Stock · Kitchen Opening Stock · Manual Sales Entry · Manual Consumption Entry · Inter Kitchen Transfers (3 أنماط) · Open/Modifiers Items · Stock Balance Transfer (يومي + سنوي!) · Auto Indent Creation (إلى MGT) | 9 | TOC COP ص1 |
| **FNB-LUK** (Lookups) | Item Recipe Details · Recipe Details · Non-Chargeable Query · Recipe–Ingredient Details (+Consolidate) · Stock Query · Standard Vs. Actual (Q) · Profitability Analysis (+Link Help + Drill-Down) | 7 | TOC LUK ص1 |
| **FNB-REP** (Reports) | Recipe Checklist · Kitchen Stock Checklist · Sales Analysis (ميزانية ± تباين، يوم/شهر/سنة) · Kitchen Stock Statement · Stock Sheet · **Missing Recipe List** · Physical Stock Variance · Inter Transfer Checklist · **Cost Report (Forecast + YTD + Detail/Summary)** · Standard vs. Actual (R) (80/132 عموداً) · Open Item/Modifier (R) · Print Buffet Information (بطابعة) · Manual Sales/Cons Report | 13 | TOC REP ص1 |

## 3. المفاهيم الجوهرية الموثقة

| المفهوم | الدلالة | المصدر |
|---|---|---|
| **Costing Start Date** | "a mandatory parameter... for **activating** the food and beverage-costing module. Based on the date specified here, the Sales and Consumption details **will get extracted**... CAUTION: Once the Start Date is entered, **updating the same will not be allowed**" + Audit Date "the date beyond which the transactions are not allowed" — بند واحد بقفل دائم + قفل تاريخي | SET ص3 |
| **Costing Link** | "Links between **Restaurant, Kitchen and Cost Centers**... Multiple Cost Centers can be linked to a **single kitchen**... provision for **Sales Tag** is provided for identification of **Revenue and Non Revenue Outlets** in the Cost Reports. **All sales / cost values in the Cost Reports will be reflected based on Kitchens**" — المطبخ هو محور التقارير وليس المطعم! | SET ص3-4 |
| **Recipe / Sub Recipe** | Sub Recipe = "frequently used sub recipes / **semi finished items**... **One sub recipe can be used / linked to multiple recipes** and the quantity of use varies based on the recipe requirement" — نصف المصنّع القابل للمشاركة (نمط BOM متداخل) | SET ص12 |
| **ربط POS↔Recipe** | "POS Item can tag for **only one Recipe**... **One Recipe can tag to Multiple Res Codes and for multiple POS Items**" + تحذير "Warning!! Item Price is less than the Cost price" — علاقة N:1 من طرف الصنف | SET ص12 |
| **COST %** | "COST % = **Cost per Portion / PRICE × 100**" — المعادلة الوحيدة المسطرة حرفياً؛ ومقابلها التمويلي "Variance will reflect as **minus**" إذا "Actual Cost Percentage calculated is **greater than** the Budgeted" | SET ص12 + ص6 |
| **الاستخراج المزدوج النمط** | Batch: "extract the data from Sales, Consumption and recipe items" بتاريخ من-إلى · Online: "368,ONLINEFBCOSTING=1. **Online transfer of Issues from inventory to costing**... If INI is activated **no need to do manual extraction** for inventory issued items" | COP ص3-4 |
| **حاجب KOT اللحظي** | "SWITCH 511, autodeductionliqsale; if this switch is set to 0, in real time during **Current stock balance will be checked KOT punch. Items cannot be sold, if the quantity is greater than the current stock**" — فحص مخزون عند البيع ذاته (الاسم يوحي بالخمر والسلوك عام! — UNK-063) | COP ص3 |
| **العالمان المخزونيان** | حاسوبي (issues من MGT عبر الاستخراج) مقابل فعلي: "Kitchen Stock... the **physical stock present at the kitchen is recorded** for a date... normally on **daily basis**" ثم "This option will arrive at **variances between computer stock and physical stock** so that physical stock recorded **would become the opening balance for the next day**" + "used to transfer from **One financial Year to next financial year**" | COP ص5 + ص16 |
| **Pink/Green** | "Records highlighted in **pink are Extracted records and green are zero balance records**" (الافتتاحي) · "Available stores list... will be highlighted in **Pink color**" (الجرد) — اللغة اللونية الثالثة بعد MNT/POS | COP ص8 + ص5 |
| **Stock UOM / Conversion UOM** | "Stock UOM: The unit of measurement for the **stock stored**. Conversion UOM: The unit of measurement of the item **to be dispensed**" + "It will allow to enter quantity in **both the UOM's**" — ثنائية التخزين والصرف في كل الكميات | COP ص8 + ص13 |
| **ثلاثية التحويل** | "inter kitchen transfers, **transfers between cost types** or transfer of **consolidated value** between two cost centers/kitchens" — البند الثالث بلا صنف أصلاً: "you have to enter the **Value under the Value column**... and save" | COP ص13-14 |
| **Auto Indent** | "link **POS menu items with their ingredients** and add the quantity to the created items... created indent can be used in **inventory**. Once the indent is generated, **it will not be allowed to modify or delete**" — جسر FNB→MGT الصاعد الوحيد + خلود الوثيقة | COP ص17 + ص19 |
| **ثنائية منهج التكلفة** | "Recipe based method of Costing" مقابل "Issue Based" (الاستهلاك الفعلي) — وتتقاطع صارماً في Profitability: "if you select the option **Issue Based then you cannot select the Restaurant**... **Recipe Based then you cannot select the option Kitchen**" | SET ص10 + LUK ص14 |
| **Standard vs Actual** | متن REP حاسم: "**Standard consumption is based on recipe details. Actual is arrived based on consumption at cost centers**" — النظري وصفي والفعلي استهلاكي (والأقواس في كلا TOC العنوانين معكوسة — تناقض مسجل) | REP ص22 |

## 4. الإحصاءات المقروءة

| المؤشر | القيمة |
|---|---|
| صفحات مقروءة عميقاً | 76 (SET 14 + COP 19 + LUK 15 + REP 28) |
| وظائف/تقارير/استعلامات موثقة | 33 (4 + 9 + 7 + 13) |
| شاشات رئيسية + فرعية | ~25 (راجع 03) |
| قواعد عمل موثقة | BR-FB-01..25 (راجع 05) |
| قيود إدخال موثقة | V-FB-01..15 (راجع 06) |
| قيود GL | **صفر** — MIS خالص (راجع 11) |
| مفاتيح INI/Switches | **#368 ONLINEFBCOSTING + #511 autodeductionliqsale** (أول وحدة بعد عائلة الخمسة بلا INI تعود بمفتاحين!) |
| مجهولات جديدة | UNK-063..067 (راجع 17) |

## 5. موقعها في خريطة المشروع

- **قبلها:** FO (1) → FAS (2) → ACR (3) → POS (4) → SYS (5) → MGT (6) → BNQ (7) → HRP (8) → Care (9) → MEM (10) → SLM (11) → TEL (12) → MNT (13) → **FNB (14 — هذه الوحدة)**.
- **علاقاتها الواردة:** POS (مبيعات/KOT/جلسات/أصناف قوائم/معدلات) · MGT (استهلاك/issues + مطابخ + أصناف Inventory Master + مخازن) · SYS (منافذ Setup Outlet + INI) — **أضخم وحدة استهلاكاً لبيانات الوحدتين التشغيليتين الكبريين**.
- **علاقاتها الصادرة:** **Auto Indent → MGT** (الجسر الصاعد الوحيد — طلبات شراء وصفية) · لا شيء مالي إطلاقاً · تقارير ورقية/Excel.
