# 09 — الاستعلامات (Lookups) — وحدة SLM

> **6 استعلامات موثقة** في SLM-LUK (10 ص). نمط الوحدة: **استعلامات عرض صرفة (read-only)** بدون أي عملية تعديل — كلها تخدم مكتب المبيعات عند التفاوض والهاتف.

---

## L-SM-01 — Browse Company

| البند | الموثق |
|---|---|
| الغرض | "browse company **contact details** based on selective criteria" |
| المعايير | "such as **Watch List, Holding Company, Sales Executive** etc…" — مع **sub-selection criteria** لتضييق الاختيار |
| مثال موثق | **Credit Limit range**: "Enter the range of Credit Limit and a list of Companies is displayed whose credit limit lies between the range specified" — استعلام ائتماني ميداني! |

> **دلالة:** البحث بالمدى الائتماني = أداة ميدانية لمدير المبيعات/التحصيل قبل مكالمة (من تجاوز حدَّه؟).

## L-SM-02 — View Rate Structures

| البند | الموثق |
|---|---|
| الغرض | عرض **rack وnon-rack** معاً لتاريخ |
| المدخلات | Date · Property · Room Type · Plan · **Currency (محلية وأجنبية!)** |
| التفاعل | "On selecting the **non-rack** rate structures, the Company option will be enabled. Click to view the **Companies linked** to the selected non-rack rate type" — من يشتري بنفس السلة السعرية |

## L-SM-03 — Company Rates — Datewise

| البند | الموثق |
|---|---|
| الغرض | "view a detailed **tariff chart** for a given company highlighting in **multiple currency**" |
| المصدر | "pre-defined for a company in the **Rate Master option** and are linked to the Company using **Link Rates to Company** option. **Discount applicable, if any, is also reflected**" |
| المدخلات | Property · Company · Date · Room Type/Plan/Currency · **Rate Type: Non Rack أو Package** |
| التنقل | أزرار Browse عبر: **Room Types · Plan types · Currency Types · Companies** |

## L-SM-04 — Browse Hotel Profile

| البند | الموثق |
|---|---|
| الغرض | عرض ملف الفندق التسويقي "based on the hotel attributes defined in Hotel Profile option" |
| **نقطة الاستدعاء الموثقة** | "This information can be **browsed from Room Booking screen**!" — الاستعلام الوحيد في الوحدة الموثق استدعاؤه من **شاشة FO** (أداة بيع أمام النزيل/الشركة!) |
| السلوك | "By default, the Hotel Profile of the Hotel listed at the top will be displayed" + زر Clear + اختيار Property |

> ⚠️ **أثر معماري:** هذه نقطة البيع الذهبي — بيانات Outlets/Banquets/Picnic Spots تُعرض لموظف الحجز لبيع خدمات الفندق — جسر **SLM→FO عرضي** (جسر عكسي نادر الاتجاه!).

## L-SM-05 — Company Package Rates

| البند | الموثق |
|---|---|
| الغرض | "package rates of the all the Companies as defined in the system" |
| المدخلات | Property · Company (F1) · **Package # (F1)** |
| المحتوى | "rates are displayed **day wise** for **occupancy type, extra adult and child pax** and other details" — تفصيل باكس إضافي/طفل يومياً |

## L-SM-06 — Company Rates (Query)

| البند | الموثق |
|---|---|
| الغرض | استعلام أسعار الشركة من زاويتي البحث |
| المدخلات | **Search By: Company Name / Company Code** → Enter → "The **Rate ID and its description** will be displayed" |
| التعمق | اختيار → **Room Rate Master – Help screen**: "displays the **rate applicability, plan type and Currency details**" → double-click = "detailed rates for different room types" |
| ⚠️ أثر توثيقي خام | النص يتضمن "**BELOW SCREENSHOTS ARE REQUIRED**" (ص9) — بقايا مسودة في الدليل الأصلي (GAP-SM-D05) |

---

## الخلاصة المعمارية

- **الرشح الموحد:** L-02/03/05/06 كلها زوايا لذات الموضوع (أسعار الشركة) — بِنية، تاريخ، باقات، سريع — نمط "بحث متعدد المداخل" لذات البيانات.
- **لا عمليات كتابة في الاستعلامات** — سلوك read-only صارم.
- **الجسور:** L-01 (Credit Limit → AR)، L-04 (**Room Booking → FO**)، L-02/03/06 (Rate Master → FO).
- **الأثر البيعي الميداني:** أربعة من الستة استعلامات = أدوات طاولة مفاوضات (أسعار+عملات+خصم+حد ائتماني) — SLM توظف استعلاماتها للتحويل البيعي لا للإدارة.
