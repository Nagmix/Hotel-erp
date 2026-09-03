# 14 — نموذج البيانات (Data Model) — وحدة FNB

> **17 كياناً / ~100 حقل** — نموذج "مستعير الماسترات": لا أصناف ولا مطاعم ولا مخازن هنا (كلها MGT/SYS/POS)، ما يملكه: **Config(3) + Recipe(1+4 أطفال) + حركات الجرد والتحويل (8) + ميزانية (1) + هندسة التكامل (2)**.

---

## 1. خريطة الكيانات (ERD نصي)

```
[SYS: Outlet]───(استعارة)───┐
[MGT: Kitchen]──(استعارة)───┤
[MGT: Item+UOM]─(استعارة)───┼──▶ CostingLink ──▶ (ينظّم) ──▶ كل التقرير
[MGT: Store]────(استعارة)───┤        │
[MGT: CostCenter](استعارة)──┘        └─ SalesTag (Revenue/NonRevenue)
[POS: MenuItem]─(استعارة)──▶ RecipeCostAnalysis ◀── Recipe (6 رقمي)
                                   ▲                │ 1:N (مكون)
                                   │           RecipeLine ──▶ [MGT Item] أو SubRecipe(≡Recipe)
                                   │                │ Yield%/Process
[POS: KOT/Session/MenuType]        │           + ProductionReq/PreparationMethod/
                                   │             ServiceMethod/Pictures (نصوص/صور)
CostingStartDate (Singleton!) ──▶ قفل كل الاستخراج/المعاملات (AuditDate)
                                   │
SalesBudget ──(شهر/سنة/جلسة)──▶ SalesAnalysis/CostReport (موازنة)
                                   │
KitchenOpeningStock ──▶ KitchenStock (يومي) ──▶ StockBalanceTransfer ──▶ افتتاحي الغد/FY
                                   │
ManualSalesEntry / ManualConsumptionEntry / InterTransfer(3 أنماط)
                                   │
OpenModifierMapping ──▶ AutoIndent ──▶ [MGT: Indent] (خالد!)
```

## 2. جرد الكيانات والحقول

| # | الكيان | الحقول الموثقة | المصدر |
|---|---|---|---|
| E1 | **CostingStartDate** *(Singleton)* | starting_date (immutable!) · user_id · last_updated · audit_date | SET ص3 |
| E2 | **CostingLink** | cost_type · res_code · cost_code · cost_name · link_by (group/item) · from/to · tag · kitchen_code · **sales_tag** | SET ص3-5 |
| E3 | **CostingLinkDefault** | required_reports[] (من available_reports) | SET ص5-6 |
| E4 | **SalesBudget** | month/year · target (restaurant/kitchen) · cost_type · cost_center · session · basis (sales/covers) · amount · pax · distribution (per_day/per_month) · **difference** (محسوب) · daily_grid[] | SET ص6-9 |
| E5 | **CostBudget** | month/year · target · cost_type · **cost_percent** (+تعديل لكل يوم) | SET ص6/8 |
| E6 | **Recipe** | type (recipe/sub) · **recipe_code (6 رقمي)** · name · portion (نص!) | SET ص10-11 |
| E7 | **RecipeLine** (طفل E6) | line_type (**store_item/sub_recipe**) · store · code (F1) · uom (auto) · **actual_qty** · value (auto) · process_type (none/add-new) · **yield_pct** (auto+يدوي) | SET ص11-12 |
| E8 | **RecipeCostAnalysis** (طفل E6) | restaurant_code · item_code (POS) · qty · rate · **cost_pct** = CostPerPortion/PRICE×100 | SET ص12 |
| E9 | **RecipeDocs** (طفل E6 ×4) | production_req · preparation_method · service_method · pictures[] | SET ص12-13 |
| E10 | **KitchenStockEntry** | date · cost_type · location · **reference_no (3-10)** · stock_type (**adjustment/physical**) · doc# (تعديل) + سطور: store (pink) · item (F1) · qty | COP ص5-6 |
| E11 | **KitchenOpeningStock** | cost_type · location · kitchen · reference_no + سطور: item · status (**pink=extracted/green=zero**) · **stock_uom/conversion_uom** · qty · rate (يدوي عند غيابه) · value (auto) | COP ص6-9 |
| E12 | **ManualSalesEntry** | criteria (**consolidated/item_wise**) · date · restaurant · **supplying_restaurant** · session · **kot_type (standard/NC)** · menu_type · kitchen · guests · value | COP ص9-11 |
| E13 | **ManualConsumptionEntry** | date (auto) · cost_type · cost_center · store · item · **uom (locked-MGT)** · qty (بوحدتين!) · rate · value=qty×rate | COP ص11-13 |
| E14 | **InterTransfer** | date · reference_no · from_cost (=to_cost!) · from/to_kitchen · store · item · qty · remarks · **[value variant: value فقط]** · transfer_type (kitchen/cost/value) | COP ص13-14 |
| E15 | **OpenModifierMapping** | item_type (**pos_modifier/pos_open**) · restaurant · date · cost_type · total_value/total_cost/total_cost_pct + سطور: line_type (store/sub) · store · code · qty | COP ص15-16 |
| E16 | **StockBalanceTransfer** | property · action (**transfer/cancel**) · (rest auto) | COP ص16-17 |
| E17 | **AutoIndent** | entry_date · restaurant_code · item_code (POS) · qty · rate · value (auto) — **immutable post-generation** | COP ص17-19 |

## 3. العلاقات الأساسية

| العلاقة | النوع | الدلالة |
|---|---|---|
| POS Item → Recipe | **N:1** (صنف→وصفة واحدة) + Recipe→POS Items **1:N** | BR-FB-12/13 — علاقة "بطاقة الوصفة القياسية" |
| Sub Recipe → Recipes | **M:N** بكميات متغيرة | "one sub recipe can be used/linked to multiple recipes" (SET ص12) |
| Cost Centers → Kitchen | **N:1** | SET ص3 |
| Kitchen → Reports | **1:N** (محور انعكاس) | "reflected based on Kitchens" |
| KitchenStock(اليوم) → OpeningStock(الغد) | تحويل يومي عبر E16 | دورة T-FB-11 |
| Recipe → AutoIndent | انفجار مكونات بكميات | "POS menu items with their ingredients" |
| SalesBudget → SalesAnalysis | استهلاك موازنة | "predefined budgets with variances" |

## 4. قرارات نمذجة ملحوظة

1. **Singleton حقيقي** (E1) — أول كيان المشروع المفروض أن يوجد **مرة واحدة بالضبط** للفندق (نمط "Config-once").
2. **Portion نص حر** (E6): "Like 2 vegetable rolls etc." — الحصة ليست كمية رقمية قابلة للضرب! تكلفة الحصة تُحسب من المكونات لا من قسمة (تناقض داخلي محتمل مع Cost per Portion في المعادلة — يُحل تصميمياً: qty إجمالي الوصفة ÷ portion قابلة للتحليل أو حقلان).
3. **ثنائية UOM** في كل كمية مخزنية (stock/conversion) — إلزامية النمذجة المزدوجة في كل E10/E11/E13 + اختيار عرض في كل تقرير.
4. **status لوني كحقل مشتق** (E11: pink/green) — مشتق من "مستخرج من MGT مقابل صفر رصيد" — نمذجة: source (extracted/manual) + zero_balance boolean.
5. **E14 متعدد الأشكال** (3 أنماط في كيان واحد: كمي/تصنيفي/قيمي) — نمذجة Frappe أنظف: doctype واحد بحقل transfer_type وشرطية الحقول.
6. **لا أرقام آلية موثقة** في أي كيان (reference يدوي + doc# غامض) — قرار إعادة بناء: Naming Series تلقائية.
7. **E17 بلا كيان طلب تفصيلي موثق** — سطور المكونات المنتفجرة غير مرئية في الدليل (الشاشة تظهر POS Item+qty! والانفجار للوصفة يحدث أين؟) — يُستنتج child table عند التنفيذ (UNK مرتبط بـGAP-FB-D04).
