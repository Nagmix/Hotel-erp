# 06 — أرصدة المخزون (Stock Balance) — MGT-REP (Phase 7)

> §6' Closing Stock by Type + §7 One Line Store Balance + §8 Store Balance by Date + §16.1–16.4 Sub Store & CC + §17 Re-Order Level Items = 8 تقارير.

---

## 1. §6' Closing Stock by Type (القسم "6" الثاني — C-MR-01)

**الوصف الحرفي:** "view the Closing Stock details of the Items in a Store **as on any given date**. You can view the report by the order of Item Code or Item Name, **include batch balance, zero balance** etc."

**المعايير (ص55-56):**

| # | المعيار | القيم |
|---|---|---|
| 1 | Date | **any given date** — رصيد as-of حر |
| 2 | Stores | قائمة |
| 3 | Item Type | افتراضياً الكل |
| 4 | **Sequence** | **Item Code / Group Code** |
| 5 | **Order By** | **By Item Code / By Item Name** |

**النقاط البنيوية:**
- **ثنائية مستويي الفرز**: Sequence (Code/Group) **ثم** Order By (Code/Name) — فرزان تسلسليان مستقلان (المجموعة ثم داخلها بالاسم مثلاً) — أدق تحكم فرز موثق في تقارير MGT.
- **batch balance** — تضمين رصيد الدفعات (تقاطع مع §9.4 Expiry: البضاعة = دفعات بصلاحيات).
- **zero balance** — إظهار/إخفاء عديمي الرصيد.
- يقابل LUK: "Item Stock Balance" و"Item Stock Balance (Nil)" — الـNil موجود كاستعلام مستقل بينما هنا Checkbox!
- **بوابة زمنية حرة** تقابل قيد §4.8 (current only): الافتتاحي مقيد بالجاري والختامي حر — ثنائية المفارقة (الوثيقة موثقة في 00 §4.8).

## 2. §7 One Line Store Balance

**الوصف:** "view the balance of the items available in the Stores for a **give date range**."

- سطر واحد لكل صنف (One Line = تكثيف) + نطاق تاريخ + Group (افتراضياً الكل).
- الفرق الدلالي عن §6': §7 **نطاق فترة** (تتبع حركة الرصيد عبرها) بينما §6' **نقطة زمنية** (as-on) — ثنائية as-on/as-range.

## 3. §8 Store Balance by Date — اليومية المجمعة

**الوصف الحرفي:** "view date wise **consolidated summary** of the balances of the transactions (Receipts, Issues, Adjustments etc) **for a given date range of the month**."

- **تجميع حسب اليوم** (Date-wise) لحركات المخزن — "يومية المخزن".
- **قيد "of the month"**: "for a given date range **of the month**" — النطاق **داخل شهر واحد** (month-bounded) — يقابل عائلة same-month في POS (~25 تقريراً) لكن هنا بجملة واحدة فقط.
- يقابل LUK: "Store Balance by Date" و"Item Balance by Date" (استعلامان) — REP يوثق نسخة التقرير الكاملة.

## 4. §16 عائلة المخازن الفرعية ومراكز التكلفة (Sub Store & CC)

### 16.1 Sub Store Transfer List
- "list of transactions made through the sub-store. A report containing the **transferred items within the sub stores**" (ص90).
- **ثلاثة مفاتيح مخازن**: Main Store + **Sub Store** + Transaction Type + Item list (افتراضياً الكل) + Date range.
- يعكس معمارية **المخزن الرئيسي → مخازن فرعية** (MGT-SET Sub Store Master) — التوزيع الداخلي.

### 16.2 Receipt Return to Sub Store
- "items that have the **receipt returned to the sub-store**" — مرتجع الاستلام مستهدف المخزن الفرعي (بمعايير عامة — أضعف وصف في العائلة).

### 16.3 Sub Cost Center Checklist
- "details of all transactions **for each sub cost centers tagged to appropriate cost center**" — البنية الهرمية: CC أم ↔ Sub-CC (بنية ماستر MGT-SET) — كل حركات مراكز التكلفة الفرعية **موسومة بأمها**.
- **خطأ مطبعي صارخ**: في صديد مقدمة §16 (ص90): "**Sun** Cost Center Checklist" (الشمس بدل الفرعي!) — يوثق كأثر تحريري دون مستوى تناقض.

### 16.4 CC Item Stock Details
- "stock details of all the items **at a specific cost center**" — الرصيد **عند مركز التكلفة** (بضاعة في حوزة قسم!) — مهم: المخزون ليس في المخازن فقط — القسم يحمل رصيداً (Bar/Maison…) — يقابل LUK "Item Stock by CC".

**الاكتشاف العائلي:** رصيد المادة يتوزع على **ثلاثة مستويات حيازة**: المخزن (§6'/7/8) → المخزن الفرعي (16.1/16.2) → **مركز التكلفة/القسم (16.4)** — نموذج توزيع جرد ثلاثي الطبقات (طابور التوزيع المادي للبضاعة).

## 5. §17 Re-Order Level Items — إنذار إعادة الطلب (as-of-now)

**الوصف الحرفي:** "view a list of all Items whose closing stock is **less than the Re-order Level**. The re-order level is specified for each Item in the Inventory Items menu option. The report is processed **for the Current System Date** and for a specific Store. The report can be generated based on Item Wise or Group wise."

**النقاط البنيوية:**
- **المعادلة الضمنية**: `closing_stock(system_date) < re_order_level` → إنذار.
- **قيد "الآن" الثاني في الوحدة**: "Current System Date" حصراً — لا تاريخ حر — تقرير **لوحة حالة** لا أرشيف (يقابل عائلة same-day في FO).
- **الفعل "Load"**: "click **Load** to view the below screen" — يجلب الحالة اللحظية (UNK تفاعل: ثالث فعل إخراجي).
- البوابة التكاملية: الناتج الطبيعي = **Auto Indent/PR** (MGT-DNT: Indent Creation) — طبقة التقارير تكتشف الحاجة وDNT ينفذها — يقابل FNB "Auto Indent Creation" (لكن هنا يدوي الطور).

## 6. جدول العائلة

| التقرير | البوابة الزمنية | مستوى الحيازة | الميزة |
|---|---|---|---|
| 6' Closing Stock by Type | **أي تاريخ (حر)** | مخزن | **فرزان + Batch/Zero** |
| 7 One Line Store Balance | نطاق | مخزن | سطر/صنف |
| 8 Store Balance by Date | **نطاق داخل شهر** | مخزن | يومية مجمعة |
| 16.1 Sub Store Transfer List | نطاق | مخزن فرعي | ثلاثي Main/Sub/Type |
| 16.2 Receipt Return to Sub Store | — | مخزن فرعي | مرتجع مستهدف |
| 16.3 Sub Cost Center Checklist | — | **CC فرعي** | وسم CC الأم |
| 16.4 CC Item Stock Details | — | **CC** | رصيد القسم |
| 17 Re-Order Level Items | **Current System Date فقط** | مخزن | `<` re-order + Load |

**التجميع النهائي للعائلة:** ثلاث بوابات زمنية (حر/نطاق-شهر/الآن-فقط) × ثلاثة مستويات حيازة (مخزن/فرعي/CC) — مصفوفة 3×3 غير مكتملة الأركان لكنها أوسع "فضاء رصيد" في الحزمة (FO رصيدها: Folio فقط · POS: الوردية فقط).
