# 08 — التحليل وMenu Engineering (§22 + §23 + إحالة §13/14/15)

> عمق POS التحليلي: **F&B Menu Engineering بمعجم STAR/PUZZLE/PLOW HORSE/DOG** (أعمق منهجية في المشروع) + Cover Analysis بسلوك 80/132 المضاف. تحليلات Popularity/Order تفصيلها في `02-sales-reports.md` §4-6.

---

## 1. F & B Menu Eng. Report (§22) — التاج التحليلي

> "The Food and Beverage **Menu Engineering Report is to analyze and control food costs** of the Outlet. In this report for each outlet and session, you can view information in **15 different columns**."

### 1.1 الأعمدة الـ15 بصيغها الحرفية

| العمود | الصيغة/التعريف الحرفي |
|---|---|
| Sl No / Code / Name / QTY Sold | ترقيم · كود الصنف/الفرعي · الاسم · الكمية المباعة |
| **Menu Mix %** | "(Quantity / Total no of qty of all menu groups) × 100" — **ملاحظة: إجمالي الكمية لكل جلسة** ("Total quantity of menu items per session") |
| **Food Cost** | "(**Selling price × Cost %**)" — سعر البيع × نسبة تكلفة الصنف |
| Selling Price | سعر بيع الصنف |
| **Item CM** (Contribution Margin) | "(**Selling price – Food cost**)" — مثال حرفي: تكلفة 100 وبيع 125 → CM = **25** |
| **Menu Costs** | "(**Quantity × Food cost**)" |
| **Menu Revenues** | "(**Quantity × Selling Price**)" — مثال حرفي: 10 American Breakfast × 500 = **5000** |
| **Menu CM** | "(**Item CM × Quantity sold**) or... (**Menu Revenues – Menu Cost**)" — صيغتان مكافئتان موثقتان! |
| **CM Class** | "A value is achieved by dividing **Total Menu CM by Total Quantity sold in that menu**. Compare that value with Item CM. If Item CM **≥** → **HIGH**; **<** → **LOW**" — مثال: 2000/20 = 100 · Item CM 120 → HIGH · 90 → LOW |
| **MM Class** | "(**100 ÷ Total number of items**) × **F&B Factor % defined in INI switch no 335**. Compare with Menu Mix %. **≥ → HIGH · < → LOW**" — مثال: (100/10) × 70% = 7 · Menu Mix 10 → HIGH · 5 → LOW |
| **Item Class** | مصفوفة 2×2 — انظر §1.2 |
| **Profit Factor** | "**Total Menu CM ÷ Total Number of Items** = value achieved; then **Individual Menu CM ÷ value**" — مثال: 500/10 = 50 · 80/50 = **1.6** |

### 1.2 مصفوفة التصنيف (Item Class) — حرفياً

| CM Class | MM Class | **Item Class** |
|---|---|---|
| HIGH | HIGH | **STAR** (نجم) |
| HIGH | LOW | **PUZZLE** (لغز: مربح لكن غير مطلوب — سعر/تسويق) |
| LOW | HIGH | **PLOW HORSE** (حصان الحرث: مطلوب لكن هامش ضعيف — تسعير/تكلفة) |
| LOW | LOW | **DOG** (كلب: مرشح للحذف) |

**الدلالة:** هذا نموذج **Kasavana-Smith Menu Engineering** مطبقاً حرفياً — الاستراتيجية الكلاسيكية لإدارة قائمة المطعم (مصفوفة هامش المساهمة × الحصة السوقية للصنف) — **المنهجية الإدارية الوحيدة المسماة والمصنفة في كل الحزمة**: التقارير الأخرى تقيس؛ هذا **يقرر** (حذف/تسعير/ترويج).

### 1.3 الاعتماد النظامي

- **INI Switch No. 335** (F&B Factor %): "The F&B Factor displayed in the screen is defined in the INI Switch 335" — العامل **يُعرض في شاشة التقرير** (مفتاح INI بمرآة UI!) — قيمته الافتراضية غير موثقة (المثال 70%) → UNK-086.
- عتبة HIGH/Low **≥ vs <** (لا >) — الصنف عند الحد بالضبط = مرتفع (نص حرفي).

### 1.4 الفرضية المحاسبية الضمنية

- **Food Cost = Selling price × Cost %** — التكلفة **نسبة من السعر** (وليس من FNB Recipe الفعلية!) — أي أن Menu Engineering يعمل حتى بدون FNB Costing مثبتة، من نسبة Cost% المخزنة في الصنف نفسه (POS-SET Rate List يعرضها ضمن أعمدة Menu List!).
- القيم Rs/- (روبية) في الأمثلة — سياق هندي متسق مع §9 PAN.

## 2. Cover Analysis (§23) — المقيمون وغيرهم

> "analytical report that gives a picture of the **spending pattern of the Resident (inhouse) Guests and Non-Resident Guests**."

| البند | القيمة |
|---|---|
| المدخل | Date + Outlets + **80 Column XOR 132 Column** |
| المخرج | لكل منفذ×جلسة×نوع قائمة: covers · المبلغ · **متوسط الإنفاق (resident وnon-resident منفصلين)** + إجماليات |
| **سلوك 80** | "displays the spending pattern... for **four menu types (Food, Liquor, Soft Drinks and Tobacco)**" |
| **سلوك 132** | "**five menu types** (Food, Liquor, Soft Drinks, Tobacco and **Others**) + **grand total column 'Total'** (covers/amount/average)" |

**الدلالة البنيوية (مفتاح عائلة 80/132):**

- في POS: 132 **يضيف** نوع القائمة الخامس + عمود الإجمالي — **دلالة إضافية**.
- في FO (Night Report): 132 كان **يحذف** خيار YTD — **دلالة حذفية**.
- النتيجة: عائلة XOR 80/132 ليست قاعدة واحدة بل **معرّفي عرض متقلب الاتجاه بين الوحدات** — يُهجر عند التنفيذ (عرض موحد قابل للتمرير) ويُسجل كسلوك أصلي (GAP-PR-D03).

**Resident vs Non-Resident:** تجزئة سكانية موصولة بـFO (ضيف مقيم = Room settlement عادة) — تحليل يقاطع مصدر الإيراد بالفندق: مطعم يخدم النزلاء vs الخارجيين.

## 3. Popularity ×2 + Order Analysis (إحالة تفصيل)

- **Popularity Analysis (§13)**: Cut Off ≤ **9999** + (Item Total ÷ Restaurant Total)×100 أو (Item Total ÷ Group Total)×100 + ترتيب تنازلي + Standard XOR NC → تفصيل كامل في `02-sales-reports.md` §4.
- **Popularity Report (Time) (§14)**: Time Slots متصاعدة إلزامياً + 132 = المبالغ → §5 هناك.
- **Order Analysis by Time (§15)**: start/close لكل طلب → §6 هناك.

> العائلة التحليلية الخماسية (13/14/15/22/23) تشكل **طبقة BI كاملة**: الطلب (المبيعات) → الزمن (الطلب والشريحة) → التكلفة والهامش (Menu Engineering) → السكان (Cover) — لم تجتمع بهذا الترتيب المنهجي في أي وحدة أخرى.

## 4. مصفوفة التحليلات النهائية (Session 17)

| التحليل | السؤال الذي يجيبه | الأداة |
|---|---|---|
| Sales ×16 | كم بعنا؟ بأي تفصيل؟ | `02` |
| Settlements ×9 | كيف دُفع؟ | `03` |
| Popularity (13) | ما الأكثر طلباً؟ (عتبة) | Cut Off 9999 |
| Popularity-Time (14) | متى تُشترى الذروة؟ | Time Slots |
| Order-Time (15) | كم يستغرق الطلب؟ | start/close |
| **Menu Engineering (22)** | **ماذا نحذف/نسعّر/نروّج؟** | **STAR/PUZZLE/PLOW HORSE/DOG + INI 335** |
| Cover (23) | من ينفق: النزيل أم الخارجي؟ | Resident split + 80/132 |
