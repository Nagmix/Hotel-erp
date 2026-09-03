# 16 — الموائمة مع ERPNext/Frappe (ERPNext Mapping) — وحدة FNB

> **F-FB-1..12** — من **أمضى تواءمات المشروع بنيوياً**: المحرك الوصفي يقع حرفياً على **BOM** (الوصفة = BOM · Sub Recipe = BOM متداخل/نصف مصنّع · انفجار المكونات = BOM Explosion · Auto Indent = Material Request من BOM!)، والجرد على **Stock Reconciliation/Stock Entry**، والموازنة على **Budget**. الأصول المخصصة تتركز في **محرك الاستخراج/التكلفة والتقارير التحليلية**. التقدير: **~6 أصول مخصصة / 4-5 أسابيع**.

---

## 1. الخريطة العامة

| مكون FNB | الأصل Frappe/ERPNext | الحالة | القرار |
|---|---|---|---|
| Recipe (رأس+مكونات+Process+Yield) | **BOM** (+ Operations للProcess!) | ✅✅ جاهز قوي | F-FB-1 |
| Sub Recipe | **BOM متداخل (sub-assembly BOM)** | ✅✅ جاهز قوي | F-FB-1 |
| Recipe↔POS Item (N:1) | BOM-for-Item (+ حقل link للقائمة) | ✅ جاهز بنمط | F-FB-2 |
| Kitchen Stock (يومي فعلي) | **Stock Reconciliation** | ✅✅ جاهز قوي | F-FB-3 |
| Kitchen Opening Stock | Stock Reconciliation (افتتاحي) / Stock Ledger | ✅ جاهز | F-FB-3 |
| Stock Balance Transfer (يومي/سنوي) | Reconciliation دوري مجدول (scheduler) | ✅ جاهز | F-FB-3 |
| Inter Kitchen/Cost/Value Transfer | **Stock Entry Material Transfer** (+ نمط قيمي مخصص) | ✅✅ / 🔧 | F-FB-4 |
| Manual Consumption | **Stock Entry Material Issue** (إلى Cost Center) | ✅✅ جاهز قوي | F-FB-5 |
| Manual Sales (غير محوسب) | **POS Invoice** offline / Sales Invoice | ✅ جاهز بنمط | F-FB-6 |
| Auto Indent | **Material Request** (+ توليد من BOM — أصلية!) | ✅✅ جاهز قوي | F-FB-7 |
| Sales/Cost Budgets | **Budget** (Cost Center/Monthly) | ✅ جاهز بنمط | F-FB-8 |
| Costing Start Date | **Accounting Fiscal/بداية Stock Ledger** + قرارات تشغيل | 🔧 مخصص | F-FB-9 |
| Costing Extraction (Batch/Online) | Scheduled Jobs + Hooks | 🔧 مخصص ⭐ | F-FB-10 |
| حاجب KOT (SWITCH 511) | Validation على POS Invoice | 🔧 مخصص | F-FB-11 |
| 13 تقريراً + 7 استعلامات | Script Reports/Dashboards | 🔧 مخصص | F-FB-12 |
| Costing Link (Res↔Kitchen↔CC) | Warehouse/Store structure + Cost Centers | ✅ بنمط | F-FB-2 |

## 2. القرارات التفصيلية

### F-FB-1: Recipe = BOM ⭐⭐ (أثقل قرار — يسقط الوحدة كلها على أصل ناضج)
- **BOM** يمنح: items[] بكميات (Actual Quantity!) · **Process = Routing/Operations** (العملية "None/Add New" = Workstation/Operation اختياري!) · **Yield** (حقل أصلي في BOM!) · is_active/is_default · **تكلفة الوحدة محسوبة آلياً** (Valuation BOM) = Cost per Portion.
- **Sub Recipe = BOM-for-sub-assembly-item**: "One sub recipe can be linked to multiple recipes" = sub-assembly BOM يُستهلك في BOMs متعددة بكميات مختلفة — **حرفياً نمط Manufacturing القياسي**.
- امتدادات مخصصة: `portion_qty/portion_uom` (Portion "2 vegetable rolls" → رقم+وصف!) · تابات نصية (Production Req/Preparation/Service = حقول Text طويلة) · **Pictures** = جدول مرفقات لكل بند أو doctype-image.
- **Cost Analysis = BOM Costing + Price List**: COST % = BOM cost / Price × 100 → **حقل محسوب Dashboard**؛ والتحذير "Item Price less than Cost" = تحقق on_validate مع رسالة التحذير الأصلية نفسها.

### F-FB-2: عالم المطابخ = Warehouses + Cost Centers
- Kitchen (ماستر MGT المستعار) = **Warehouse**؛ مراكز التكلفة = **Cost Centers** الحقيقية؛ المطاعم = منافذ POS (SYS Setup Outlet).
- **Costing Link**: جدول ربط `Warehouse-Kitchen ↔ Cost Center ↔ POS Outlet` بحقل **sales_tag** (Revenue/Non-Revenue) — "All values reflected based on Kitchens" = تجميع التقارير على Warehouse.
- Link By (Group/Item) = تخصيص على Item Group أو Item.

### F-FB-3: دورة الجرد = Stock Reconciliation (تطابق قوي جداً) ⭐
- Kitchen Stock اليومي (Physical) = **Stock Reconciliation** (يعيّن الرصيد الفعلي ويحسب الفرق آلياً!) — عبارتهم "variances between computer stock and physical stock... would become the opening balance for the next day" = سلوك Reconciliation حرفياً.
- Adjustment = Reconciliation بأسلوب Delؤta أو Stock Entry Adjustment.
- **الافتتاحي (Pink/Green)**: Reconciliation الافتتاح الأول (Green = بند صفري بلا valuation — يدخل القيمة يدوياً "rate of items which do not have rates" = القناة الأصلية ذاتها!).
- **السنوي**: Reconciliation نهاية FY أو مجرد استمرارية Stock Ledger (تلقائية في ERPNext — الخيار الأنظف).

### F-FB-4: التحويلات = Stock Entry Material Transfer
- Inter Kitchen = Transfer بين Warehouses (نمط 1:1 كامل).
- **Value Transfer** (نمط قيمي بلا أصناف): **لا مقابل مخزني** — يُبنى **Journal Entry تحليلي بين Cost Centers** أو أداة إعادة توزيع مخصصة (GAP يُرفع قراراً: توزيع تحليلي على مركز تكلفة، بلا لمس المخزون — مطابق للفلسفة الأصلية!).

### F-FB-5: Manual Consumption = Material Issue
- Stock Entry → Material Issue: من Warehouse إلى Cost Center (ERPNext يدعم "Issue to Cost Center/Maintenance" حرفياً) — والكمية بوحدتي UOM = **UOM Conversion** الأصلية (Stock UOM/Conversion UOM = نمط ERPNext القياسي).

### F-FB-6: Manual Sales = POS Invoice
- منفذ غير محوسب = **POS Invoice offline** بحقل `is_manual_fb_entry`، بنمط Consolidated (بند واحد إجمالي) أو Item-wise؛ جلسات/قوائم/KOT بحقول مخصصة على القائمة؛ **NC KOT = وضع غير محصَّل** (POS Invoice بلا دفع = ممتاز أصلاً).

### F-FB-7: Auto Indent = Material Request ⭐ (الحل الأنيق للخلود)
- **Material Request** أصلاً: قابل للتوليد من BOM (get_item_details/BOM explosion) — نفس "link POS menu items with their ingredients"!
- **كسر الخلود بأمان**: الأصل "not allowed to modify or delete" يُستبدل بدورة Draft→Submitted→(Cancel قبل Receipt) — قرار D-FB-3 موثق في 17/P03: الأمان الوظيفي نفسه (لا تعديل بعد التقديم) بلا فخ الخطأ الخالد.

### F-FB-8: Budgets = Budget
- Budget على Cost Center (شهر/سنة) بأهداف قابلة للتوزيع الشهري؛ **Covers/PAX = حقل مخصص** `custom_pax_target`؛ Cost Budget % = موازنة تكلفة بنسبة — **Budget Variance Report أصلي** يحل نصف Sales Analysis.

### F-FB-9: Costing Start Date = قرار تشغيلي
- لا Singleton أصلي — يُبنى **Singleton doctype** (نمط "Accounts Settings"): `fb_costing_start_date` بقفل كتابة بعد الحفظ (validate: رفض أي update لحقل التاريخ — يحاكي CAUTION الأصلية حرفياً) + شرط POS/MGT جاهزين = checklist تشغيلي (راجع AC-01).

### F-FB-10: Extraction Engine (الأصل المخصص الأول) ⭐
- **Batch**: Scheduled Job ( nightly) يجمع: POS Invoices (مبيعات) + Stock Entries issues (استهلاك) → جداول تحليلية مجمعة.
- **Online (INI#368)**: hooks on_submit (POS Invoice/Stock Entry) تكتب فورياً.
- **التوازي الدلالي**: INI#368 = اختيار Batch/Event-driven — قرار معماري Frappe مجاني (كلاهما متاح).

### F-FB-11: حاجب KOT = Validation hook
- تحقق on_submit/save لPOS Invoice: مجموع الكمية > رصيد Warehouse الحالي → رفض (رسالة الخطأ تُصمم — الأصل صامت!) — **السويتش يصبح Feature Flag** (System Settings).

### F-FB-12: 20 مخرجاً تحليلياً
- **Script Reports** (13 تقريراً) + **Queries/Dashboard** (7 استعلامات): Sales Analysis/Cost Report/Profitability/Standard-vs-Actual = تقارير QuerryScript مع drill-down HTML (راجع UX).
- **Missing Recipe List = تقرير Items-for-POS بلا BOM** (أصل قابل للتنفيذ فوراً!) · **Recipe Checklist = BOM listing** · **Buffet = Print Format بتوجيه طابعة**.
- الـStandard vs Actual = **BOM Cost (theoretical) vs Stock Consumption (actual)** — كلاهما موجود أصلاً في ERPNext (BOM cost + Stock Ledger) — أبعدُ نقطة قوة في الموائمة.

## 3. الملخص التنفيذي

| المحور | التقييم |
|---|---|
| أصل مجاني كبير | BOM (وصفات كاملة بنصف مصنّع وYield وProcess وتكلفة) + Stock Reconciliation (دورة الجرد) + Material Request (indent) + Budget (موازنة) |
| أصول مخصصة (~6) | 1) Extraction/Sync engine (batch+online) 2) Singleton تفعيل + Feature Flag 511 3) Costing Link/analytic Warehouse-CC model 4) تقارير التكلفة (Cost Report/Sales Analysis/Profitability/SvA) 5) Value Transfer (توزيع تحليلي) 6) NC Query/Open-Modifier mapping |
| الجهد | **~4-5 أسابيع** (التقارير أثقل بند) |
| المخاطر | غياب جلسات/قوائم حسب النمط الأصلي في POS invoices → حقول مخصصة؛ تعدد UOM في التقارير = انتباه تحويل |
| المكسب غير المتوقع | **Manufacturing في قلب الفندق**: BOM/Routing/Workstation تعطي Process Type وProduction Requirement مجاناً — والمطبخ مصنعاً فعلياً |
