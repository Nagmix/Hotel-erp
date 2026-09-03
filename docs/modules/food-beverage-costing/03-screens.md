# 03 — جرد الشاشات (Screens Inventory) — وحدة FNB

> **~25 شاشة** (4 Setup + 9 Operations + 7 Lookups + 13 Reports بمعايناتها) — مع ملاحظة بنائية: كثير من "شاشات" التقارير هي **مولدات نمطية** (معايير + Preview + Generate) تتكرر 13 مرة بنمط واحد، والشاشات الفعلية الغنية تتركز في COP (الجرد/التحويلات) وSET (الوصفة بتاباتها الستة).

---

## 1. شاشات Setup (4 + شاشتان فرعيتان)

| # | الشاشة | العناصر التفاعلية الموثقة | المصدر |
|---|---|---|---|
| S-01 | Costing Start Date | Starting Date · User ID (ro) · Last Updated (ro) · **Audit Date** | SET ص3 |
| S-02 | Costing Link | Cost Type dd · Res Code · Link By (Group/Item) · From/To · Display (All/UnTagged/Tagged) · **Tag Kitchen/Bar** (+Yes) · شبكة Link Item–Kitchen (Group+Item+Kitchen Code قابلة للنقر المزدوج) | SET ص3-5 |
| S-02a | **Defaults** (فرعية) | Available Reports ↔ Required Reports + **Add** | SET ص5-6 |
| S-03 | Sales/Cost Budgets | Month/Year · Sales/Cost · Restaurant/Kitchen · Cost Type (+قائمة Cost Centers بنقر مزدوج) · Session · Sales/Covers · Per Day/Per Month · **Difference** (ro) · شبكة التقويم | SET ص6-9 |
| S-04 | Recipe/Sub Recipe Master | Type dd · Recipe Code (6 رقمي) · Name · Portion + **6 تابات** | SET ص10-13 |
| S-04a | **تفاصيل الوصفة** (فرعية) | Detail view + double-click → المكونات + Recipe Tab (Type/Store/Code/Qty/Process/Yield) + **Cost Analysis** (Restaurant Code/Item Code + شاشة qty/rate) + Production/Preparation/Service/Pictures | SET ص11-13 |

## 2. شاشات Costing Operations (9 + 4 فرعية)

| # | الشاشة | العناصر التفاعلية الموثقة | المصدر |
|---|---|---|---|
| S-05 | Costing Extraction | **Type** (خيارات الاستخراج) · Date Range · **Process** + شاشة تقدم + رسالة اكتمال | COP ص3-4 |
| S-06 | Kitchen Stock | Date · Cost Type · Location · Reference # (3-10) · Stock Type (Adjustment/Physical) · **قائمة المخازن (Pink)** + شبكة (Store/Item/Qty) · F1 · F5(+Yes) · Modify بـDoc# | COP ص5-6 |
| S-07 | Kitchen Opening Stock | Cost Type · Location · Kitchen · Reference # · شبكة (Pink=مستخرج/**Green=رصيد صفري قابل للإدخال**) · **F7/F8** بحث كود/اسم · Stock UOM/Conversion UOM · rate/value auto | COP ص6-9 |
| S-08 | Manual Sales Entry | Criteria (**Consolidated/Item Wise**) · Date · Restaurant · **Supplying Restaurant** · Session · **KOT Type (Standard/NC)** · Menu Type · Kitchen · Guests · Value | COP ص9-11 |
| S-09 | Manual Consumption Entry | Date (auto) · Cost Type · Cost Center · Stores · Item (F1) · UOM (ro!) · Qty · **Value = Qty × Rate** | COP ص11-13 |
| S-10 | Inter Kitchen Transfers | Date · Reference # · From Cost (=To Cost!) · From/To Kitchen · Store · Item · Qty · Remarks + **Transfer Options** | COP ص13-14 |
| S-10a | **Transfer Options** (فرعية) | "Select the type of transfer process" — أنماط التحويل الثلاثة | COP ص13 |
| S-10b | **Value Transfer** (نمط) | Cost range + Kitchen range + عمود **Value** | COP ص14 |
| S-11 | Open/Modifiers Items | Item Type (**POS Modifier/POS Open**) · Restaurant · Date · Cost Type · قائمة (total value/cost/Cost%) + بناء الربط: Type double-click (Store Item/Sub Recipe) · Store · Code · Qty | COP ص15-16 |
| S-12 | Stock Balance Transfer | خيارا **Transfer/Cancel** + **Property** (auto-populate) | COP ص16-17 |
| S-12a | **Cancel** (نمط) | شاشة إلغاء ترحيل الرصيد | COP ص16 |
| S-13 | Auto Indent Creation | Entry Date (+Load) · Selected POS Items (restaurant code + item code + Qty → rate/value auto) | COP ص17-19 |

## 3. شاشات Lookups (7 — نتائج + drill-down)

| # | الشاشة | المعايير + العناصر | المصدر |
|---|---|---|---|
| S-14 | Item Recipe Details | Outlet · Cost Type · From/To date · From/To item + **F3 → Recipe details** + double-click drill | LUK ص2-4 |
| S-15 | Recipe Details | Outlet · **Menu Type** · Load · totals (Consumption/Selling Price/Cost%) + double-click + زر **Recipe Master** (إحالة لSET) | LUK ص4-5 |
| S-16 | Non-Chargeable Query | Date · Cost Type · Outlet · **NC Type** (Complimentary/Spoilage/House Consumption) + ملخصات Restaurant/Kitchen/KOT | LUK ص5-7 |
| S-17 | Recipe–Ingredient Details | Recipe Name dd · Date · Item (Help) · KOT Type · Load + زر **Consolidate** | LUK ص7-8 |
| S-18 | Stock Query | From/To · Cost Type · Kitchen · Group output · **Quantity: Stock UOM/Conversion UOM** + print | LUK ص8-11 |
| S-19 | Standard Vs. Actual (Q) | Date range · **Item Range/Group Range** · F1 Store/Item · Print Quantity UOM | LUK ص12-13 |
| S-20 | Profitability Analysis | Date range · Property · Cost Type · **Kitchen/Restaurant** · **Consumption Type (Issue Based/Recipe Based — XOR!)** + **Link Help** + drill ("No Drill Down Available for this Category") | LUK ص13-15 |
| S-20a | **Link Help** (فرعية) | "link the Restaurant/Cost Center and Kitchen" | LUK ص15 |

## 4. شاشات Reports (13 — نمط موحد: معايير → Preview → Generate)

| # | التقرير | المعايير الخاصة | المصدر |
|---|---|---|---|
| S-21 | Recipe Checklist | Recipe/**Sub Recipe** · Restaurant · **Recipe # من-إلى** | REP ص2-3 |
| S-22 | Kitchen Stock Checklist | **نمط: Opening Balance/Adjustment/Physical Stock** · Date range · Cost Type · Cost Center · **By Location/By Item** | REP ص4-6 |
| S-23 | Sales Analysis | Date · Outlet type · Session · items + **يوم/شهر/سنة** + ميزانيات وتباينات | REP ص6-7 |
| S-24 | Kitchen Stock Statement | Date · Cost Type · Kitchen · print quantity + grouping · **day/month/both** | REP ص8-9 |
| S-25 | Stock Sheet | Date · Cost Type · Kitchen · print quantity | REP ص10-13 |
| S-26 | **Missing Recipe List** | Cost Type فقط | REP ص13-14 |
| S-27 | Physical Stock Variance | Date range · Cost Type · Kitchen · **Item/Group range** · UOM (stock/conversion/both) · **All Items/Physical stock items** · ✓ consumption details | REP ص14-17 |
| S-28 | Inter Transfer Checklist | Date range · **Transfer Type (Inter Kitchen/Inter Cost/Value)** · ✓ Item Code Description | REP ص17-19 |
| S-29 | **Cost Report** | **Report Format dd** · Date range · **Forecast** · Cost Type · ✓ **Year to Date/Kitchen Stock Not Required** · **Detail/Summary** | REP ص19-21 |
| S-30 | Standard vs. Actual (R) | Date range · Item/Group range · UOM · **80 أو 132 عموداً** | REP ص22-23 |
| S-31 | Open Item/Modifier (R) | Open/Modifier · Date range · Cost Type · Restaurant · **UOM: Consumption/Issue** | REP ص24-26 |
| S-32 | Print Buffet Information | Date range · Outlet · Session · **اختيار الطابعة** + Print | REP ص26-27 |
| S-33 | Manual Sales/Cons Report | **Manual Sales/Manual Consumption** · Restaurant type · Date range · Cost Type | REP ص27-28 |

## 5. أنماط UI الملاحظة

- **النقر المزدوج أداة تحرير عالمية**: عمود Kitchen Code (SET ص5) · صفوف Green (COP ص8) · عمود Type في Open/Modifiers (COP ص16) · عمودا Status/Action في التقارير (drill-downs) — بعد MNT/TEL يترسخ كنمط مشروع.
- **اللون لغة حالة**: Pink (مخازن متاحة بالجرد + سجلات مستخرجة بالافتتاحي) · Green (رصيد صفري = قابل للإدخال) — ثالث وحدة لونية.
- **مفاتيح الوظائف**: F1 (مساعدة الأصناف — في 7 شاشات) · F3 (قفزة Cost Analysis) · F5 (حذف) · F7/F8 (بحث كود/اسم).
- **Preview قبل Generate** في 12 تقريراً من 13 — بنية شاشة موحدة صارمة.
- **تسلسل إدخال مقنن**: "Enter the quantity... Once all the items are recorded, click Save" + "press F3, the cursor will move to the Cost Analysis Section" — عقلية نموذج ورقي محوسب.
- **عنصر TOC الشاذ**: البند 13 في TOC مكتوب "13.__Manual_Sales_Cons_Report." بشرطات سفلية — أثر تنسيقي خام في الفهرس (GAP-FB-D07-ملحوظة).
