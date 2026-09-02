# نموذج مجال الفندق (Hotel Domain Overview)

> **المرحلة:** Phase 1 — Domain Model | **الحالة:** الإصدار التأسيسي (يُوسَّع مع تقدم التحليل)
> **المصدر:** استخلاص من كتالوجات FortuneNext 6i (انظر مصدر كل كيان في `entities.md`)

---

## 1. طبيعة النطاق

النظام المجال هو **منشأة ضيافة متكاملة** (فندق + مطاعم + قاعات مناسبات + نادي عضويات + خدمات مساندة)، تُدار عبر دورتين ماليتين متشابكتين:

1. **دورة الإيراد (Revenue Cycle):** من الحجز/البيع ← الفوليو/الفاتورة ← التسوية/التحصيل ← القيد المحاسبي.
2. **دورة التكلفة (Cost Cycle):** من الشراء/الاستلام ← المخزون ← الاستهلاك/التكلفة ← القيد المحاسبي.

وبينهما **محور Night Audit** اليومي الذي يُقفل اليوم المحاسبي ويُرحّل الإيراد — وهو العنصر الأكثر خصوصية في المجال الفندقي مقارنة بـ ERP العام.

---

## 2. الطبقات الوظيفية السبع (Functional Layers)

| الطبقة | الوحدات | الوظيفة المجالية |
|---|---|---|
| **1. الضيافة والبيع (Guest-facing)** | Front Office, POS, Banquets, Membership, Care, Concierge | تعامل مباشر مع النزيل/العضو/العميل |
| **2. الإيراد والتحصيل (Revenue-to-Cash)** | Cashiering (داخل FO), ACR, Membership Billing | الفوليو، الفاتورة، التسوية، المديونية |
| **3. المحاسبة (Financial Core)** | Financial Management (FAS) + Fixed Assets | GL، دليل الحسابات، القيود، الإهلاك، الإقفالات |
| **4. التوريد والتكلفة (Supply & Cost)** | Materials Management, F&B Costing | الشراء، المخازن، الوصفات، التكاليف المعيارية |
| **5. الموارد البشرية (People)** | HR & Payroll, Care (Roster) | التوظيف، الحضور، الرواتب، الإنتاجية |
| **6. الأصول والبنية (Assets & Infrastructure)** | Fixed Assets, Maintenance, Telephones, Gate Passes | إهلاك، صيانة، مكالمات، ضبط حركة المواد |
| **7. التجاري والقيادة (Commerce & Command)** | Sales & Marketing, System Setup, Touch Screen | عقود الشركات، تتبع المبيعات، المستخدمون/الصلاحيات |

---

## 3. المفاهيم المجالية الجوهرية (Core Domain Concepts)

> هذه المفاهيم هي ما يجعل نظام الفنادق مختلفاً عن ERP عام — ويجب أن تكون قلب تصميم Hotel PMS Core.

### 3.1 Business Date (التاريخ المحاسبي الفندقي)
اليوم الفندقي لا يساوي اليوم التقويمي: يبدأ وينتهي مع **Night Audit** (فتح تاريخ جديد). بعد فتح التاريخ الجديد تُمنع كل التعديلات على تاريخ الأمس — قاعدة موثقة (FOM-DEP ص7: "After a new date has been opened, you cannot make any modifications or delete transactions of the previous accounting date").

### 3.2 Folio (فوليو النزيل)
حساب تشغيلي مفتوح للنزيل أثناء الإقامة: تُرحَّل إليه شحنات الغرفة + POS + المكالمات + الغسيل + رسوم متنوعة، ثم يُسوَّى عند المغادرة (نقد/بطاقة/شركة/موظف/معلق) — والتسوية الائتمانية تُرحَّل تلقائياً إلى ACR (موثق: FOM-CAS ص69).

### 3.3 Room Status (دورة حالة الغرفة)
Vacant/Occupied × Clean/Dirty — تُدار بين FO وHousekeeping، وتؤثر على قابلية تخصيص الغرفة عند الوصول.

### 3.4 Rate Architecture (هندسة الأسعار)
Room Type ← Rate (Rack/Discounted/Contract/Package) × Meal Plan × Currency × Tax Structure — مع Plans/Package Elements لتوزيع سعر الحزمة على بنود إيراد (نِسب يجب أن تجمع 100%).

### 3.5 Night Audit (التدقيق الليلي)
عملية إقفال يومية مُرقَّمة إلزامياً: Post Tariff → Create Guest Balance → Create Night Balance → (تسويات/تعدلات) → Open New Date، مع قواعد حظر وتجميد موثقة (انظر `workflows/end-to-end/night-audit.md` لاحقاً).

### 3.6 Revenue Code / Department / Cost Center (محاور الترحيل الثلاثة)
كل شحنة إيراد تُصنَّف عبرها — وهي مفاتيح الربط بين العمليات والمحاسبة (ظاهرة في Consolidated Entry: GL + Department + Cost Center، FOM-DEP ص8–9).

### 3.7 Settlement Modes
Cash / Credit Card / Cheque / Company (AR) / Staff / Bill on Hold / Foreign Exchange / Membership — موثقة في FOM-CAS Settlements.

---

## 4. نظرة على الثنائيات البنيوية

- **الشخص (Party):** Guest / Company / Travel Agent / Member / Staff / Vendor — كلهم "أطراف" لكن بأدوار ودورات مختلفة.
- **المنشأة (Physical):** Property → Building → Floor → Room → Room Features | Function Room (Banquets) | Outlet (POS) | Store (MGT) | Kitchen (FNB).
- **المستند (Document):** Reservation → Registration → Folio → Bill → Settlement → Receipt / Invoice — سلسلة إيراد النزيل.
- **التحليلية (Analytics):** Market Segment / Business Source / Nationality / Guest Status — تصنيفات تُستخدم في التقارير وMIS.

---

## 5. ما يميز المجال عن ERPNext القياسي (ملاحظة تمهيدية للـ Mapping)

> [INFERENCE — يُحسم في Phase 11/12]

| مفهوم فندقي | أقرب مفهوم ERPNext | الفجوة المتوقعة |
|---|---|---|
| Business Date + Night Audit | Posting Date | لا يوجد "إقفال يومي فندقي" بآلية الحظر نفسها |
| Folio (تشغيلي يومي) | Sales Invoice | الفوليو ليس فاتورة؛ يتجمع ويُقفل يومياً |
| Room / Room Status | لا مقابل | Custom domain بالكامل |
| Reservation | Quotation/Sales Order | lifecycle فندقي مختلف جذرياً |
| Rate Plan/Meal Plan/Package | Price List | دلالة أغنى بكثير |
| Guest History | Customer + Contact | مفهوم خاص |
| Night Audit posting | Journal Entry | آلية ترحيل تلقائية يومية |
