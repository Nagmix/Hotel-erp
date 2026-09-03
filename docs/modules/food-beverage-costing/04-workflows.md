# 04 — تدفقات العمل (Workflows) — وحدة FNB

> **WF-FB-01..13** — دورة حياة مزدوجة المستوى: **دورة تأسيسية تُشغَّل مرة واحدة** (التفعيل → الربط → الميزانية → الوصفات → الافتتاحي) ثم **دورة يومية/دورية أبدية** (استخراج → جرد → ترحيل → تقارير) مع جسر صاعد عرضي (Auto Indent). الوحدة الوحيدة التي يبدأ تدفقها الرئيسي بـ**شرط جاهزية وحدتين أخريين**.

---

## WF-FB-01: تفعيل الوحدة (Activation) — ⭐ أحادي الاتجاه

```
[POS تعمل بالكامل] AND [MGT تعمل بالكامل]        ← شرط موصى نصاً (SET ص3)
        ↓
تحديد Costing Start Date (إدخال أول مرة)
        ↓
⚠️ CAUTION: لا تحديث لاحقاً أبداً (قفل دائم)
        ↓
[من هذا التاريخ: تُستخرج Sales من POS + Consumption من MGT]
        ↓
ضبط Audit Date → حظر المعاملات بعد التاريخ (خيارياً)
```

- **مخرجات**: بداية نافذة الاستخراج + User ID/Last Updated أثراً تلقائياً.
- **نقاط الفشل**: تفعيل مبكر → "MIS reports will not be generated due to insufficient details" (SET ص3). لا مسار تصحيح موثق (GAP-FB-P01).

## WF-FB-02: الربط الثلاثي (Costing Link)

```
اختيار Cost Type (Food/Liquor/Soft/Smokes)
        ↓
Link By: Group Code أو Item Code + نطاق From/To
        ↓
Display: All/UnTagged/Tagged → مراجعة الموجود
        ↓
Tag Kitchen/Bar (+تأكيد Yes)
        ↓ [تغيير لاحق]
Double-click عمود Kitchen Code → Kitchen Code Help → تعديل
        ↓
Defaults: Available Reports → Required Reports (حزمة تقارير المستخدم)
        ↓
Save → "Records Saved Successfully"
```

- **قاعدة البنية**: Cost Centers متعددة → Kitchen واحد؛ والقيم في التقارير **تعكس على أساس المطابخ** (SET ص3-4).

## WF-FB-03: الميزانيات (Sales/Cost Budgets)

```
Month/Year (يمكن مستقبلياً)
        ↓
[Sales Budget] → Restaurant أو Kitchen (من SYS/MGT!) + Cost Type + Cost Center
        ↓
Session (افتراضي: All — ينتشر لكل السنة المالية!)
        ↓
Sales (Amount) و/أو Covers (PAX) — البيعي أولاً ثم الPAX
        ↓
Per Day (إدخال شبكة التقويم يدوياً) أو Per Month (توزيع متساوٍ + Difference)
        ↓ [Cost Budget]
Cost % واحد لكل أيام الشهر (تعديل خلية-خلية ممكن)
        ↓
Save → تعكس في Sales Analysis وCost Report كـBudgeted vs Actual
```

## WF-FB-04: بناء الوصفات (Recipe Engine) ⭐

```
Type: Recipe أو Sub Recipe
        ↓
Recipe Code (6 رقمي — إلزامي) + Name (باسم القائمة) + Portion (نص!)
        ↓
[Recipe Tab] صف مكون: Type = Store Item (MGT Inventory!) أو Sub Recipe Item
        ↓
Store number → Code (F1 → desc+UOM auto) → Actual Quantity (القيمة تظهر)
        ↓
Process Type (None/Add New) + Yield % (auto — قابل للتعديل)
        ↓ [F3 — قفزة]
[Cost Analysis] Restaurant Code (المستهلك) + Item Code (POS) F1
        ↓
شاشة qty/rate → Enter
        ↓
⚠️ إن سعر POS < تكلفة الوصفة → "Warning!! Item Price is less than the Cost price"
        ↓
[Production Req] → [Preparation Method] → [Service Method] → [Pictures]
        ↓
Save
```

- **Sub Recipe**: نصف مصنّع مشترك — "One sub recipe can be used / linked to **multiple recipes**" (SET ص12) — شبكة اعتماد متداخلة.

## WF-FB-05: الاستخراج (Extraction) — ثنائية Batch/Online

```
[Mode A: Batch يدوي]
Type of extraction + Date Range → Process → شاشة تقدم → رسالة اكتمال

[Mode B: Online لحظي — INI#368=1]
Issues تنتقل من MGT تلقائياً — "no need to do manual extraction"
```

- **حاجب جانبي**: SWITCH 511=0 → عند KOT punch في POS: كمية > الرصيد الحالي = **منع البيع لحظياً** (COP ص3) — نقطة تحكم عبْرية في POS ذاته.

## WF-FB-06: المخزون الافتتاحي (Kitchen Opening Stock) — مرة واحدة

```
Cost Type + Location + Kitchen + Reference #
        ↓
Add → معالجة الأصناف → الشبكة:
  Pink = سجلات مستخرجة (من MGT) · Green = رصيد صفري
        ↓
Double-click صف Green → إدخال Quantity (rate/value auto — rate يدوي للأصناف بلا سعر)
        ↓
F7 (بحث كود) / F8 (بحث اسم) / F5 (حذف)
        ↓
Save
```

## WF-FB-07: دورة الجرد اليومية (Daily Physical Cycle) ⭐ قلب الوحدة

```
[يومياً] Kitchen Stock:
  Date + Cost Type + Location + Reference # (3-10)
  Stock Type: Physical Stock (المتاح) أو Adjustment (المستهلك)
  قائمة المخازن (Pink) → اختيار → F1 Item → Qty
  Save (Modify بـDoc# · F5 حذف + Yes)
        ↓
[نهاية اليوم] Stock Balance Transfer:
  Transfer (أو Cancel) + Property (auto-populate)
  → حساب variance (حاسوبي مقابل فعلي)
  → الرصيد الفعلي يصبح افتتاحياً للغد
        ↓
[نهاية السنة] نفس الأداة: ترحيل من سنة مالية للتي تليها
```

- الاستعلامات المساندة: Physical Stock Variance (REP #7) + Stock Query (LUK #5).

## WF-FB-08: مبيعات المنافذ غير المحوسبة (Manual Sales)

```
Criteria: Consolidated (قيد واحد) أو Item Wise (صنف صنف)
        ↓
Date + Restaurant + Supplying Restaurant + Session (فطور/غداء/عشاء)
        ↓
KOT Type: Standard أو N C (غير قابل للشحن!) + Menu Type + Kitchen
        ↓
عدد الضيوف + Value → Save (+Modify)
```

## WF-FB-09: الاستهلاك اليدوي (Manual Consumption)

```
Date (اليوم auto) + Cost Type + Cost Center + Store
        ↓
Item (F1) — UOM مقفل (من ماستر MGT!)
        ↓
Qty (بالوحدتين: Stock وConversion) → Value = Qty × Rate
        ↓
Save
```

## WF-FB-10: التحويلات الثلاثية (Inter Transfers)

```
Transfer Options → اختيار نوع العملية
        ↓
[نمط 1: Inter Kitchen] From Kitchen → To Kitchen + Store + Item + Qty + Remarks
[نمط 2: Inter Cost] بين أنواع التكلفة (From Cost — To يعكسه)
[نمط 3: Value Transfer] Cost range + Kitchen range + عمود Value (بلا أصناف!)
        ↓
Save → شبكة السجلات → تأكيد
```

## WF-FB-11: الأصناف المفتوحة/المعدلات (Open/Modifier Mapping)

```
Item Type: POS Modifier Items أو POS Open Items + Restaurant + Date + Cost Type
        ↓
قائمة النتائج (total value/cost/Cost%)
        ↓
Double-click سجل → تفاصيل الوصفة أسفل الشاشة
        ↓
Double-click عمود Type → Store Item أو Sub Recipe → Store + Code → Qty
        ↓
Save  ← صيانة الربط من شاشة استعلام! (Lookup-as-Editor)
```

## WF-FB-12: الطلب الآلي (Auto Indent) — الجسر الصاعد إلى MGT ⭐

```
Entry Date (حقول التاريخ) → Load
        ↓
Selected POS Items: Restaurant Code + Item Code → الحقول المرتبطة تظهر
        ↓
Quantity → Rate + Value (auto)
        ↓
Save → توليد indent → **قابل للاستخدام في inventory (MGT)**
        ↓
⚠️ خلود الوثيقة: "Once the indent is generated, it will not be allowed to modify or delete"
```

- **المنطق**: "link POS menu items with their ingredients and add the quantity" — انفجار الوصفة BOM-explosion باتجاه الطلب.

## WF-FB-13: دورة التقارير اليومية (Reporting Cycle)

```
[مساءً/صباحاً]
Sales Analysis (ميزانية ± تباين · يوم/شهر/سنة)
Cost Report (Format + Forecast + YTD + Detail/Summary)
Profitability Analysis (Issue XOR Recipe based)
        ↓ [تدقيق وصفي]
Missing Recipe List (ما بلا وصفة) · Recipe Checklist
        ↓ [تدقيق فعلي]
Physical Stock Variance · Kitchen Stock Statement/Sheet
        ↓ [تفاصيل]
NC Query · Open/Modifier (R) · Inter Transfer Checklist · Manual Sales/Cons
        ↓ [طباعة تشغيلية]
Print Buffet Information (إلى طابعة محددة)
```

---

## خريطة تقاطع التدفقات

- **WF-FB-01 يسبق الجميع** (بوابة أحادية).
- **WF-FB-04 (وصفات) يغذي**: WF-FB-05 (استخراج recipe items) · WF-FB-11 (ربط المعدلات) · WF-FB-12 (Auto Indent) · WF-FB-13 (Standard/Actual وProfitability Recipe-Based).
- **WF-FB-07 (الجرد) يغذي**: Stock Balance Transfer → افتتاحي الغد → يكرر نفسه؛ وPhysical Variance.
- **المخرج الوحيد عبر حدود الوحدة**: WF-FB-12 → MGT (indent). عدا ذلك: تقارير/ورق فقط.
