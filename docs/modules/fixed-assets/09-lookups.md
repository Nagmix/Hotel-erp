# 09 — الاستعلامات (Lookups/Queries) — وحدة FXD

> **3 استعلامات** فقط — أصغر حصيلة استعلامية في وحدة محاسبية (المفاجأة بعد 7 استعلامات FNB): كل مسار التحليل ذهب للتقارير المطبوعة. الاستعلامان الأولان زوج (Details/History) والثالث خاص بالاستبعاد.

---

## الجرد

| # | الاستعلام | المدخلات | المصدر |
|---|---|---|---|
| Q-FX-01 | **Depreciation Details (Q)** | From/To **Financial Year** → Load | "query the depreciation details of **all Assets in the Property** for a given range of Financial Year. Depreciation for each Asset is calculated and displayed based on the **method and rate of depreciation defined in the Depreciation % menu option**" (§12 ص18) |
| Q-FX-02 | **Depreciation History (Q)** | Property + FY (F3) + **Location** + From/To[MMYY] + **From Asset/To Asset** (F1) | "query the depreciation **history** of the fixed assets... for a given range of financial year" (§13 ص18-19) |
| Q-FX-03 | **Disposal History Query** | Property + FY (F3) + **From Date/To Date** + Location + Asset Code (F1) | "query the disposal history of the fixed assets" (§14 ص19-20) |

## التحليل التفاضلي للثلاثي

| البعد | Q-FX-01 | Q-FX-02 | Q-FX-03 |
|---|---|---|---|
| المحور الزمني | **سنوات مالية** (FY range) | **أشهر** (MMYY range) | **أيام** (Date range) |
| الفلترة المكانية | لا (كل الفندق) | Location | Location |
| نطاق الأصول | لا | From/To Asset | أصل واحد (F1) |
| موضوع البيانات | الإهلاك الحسابي | تاريخ الإهلاك | **الاستبعاد** (البيع كذلك؟ "Disposal" فقط في العنوان — بينما المصطلح في Transaction يعني الاستبعاد الفني بلا بيع — [UNCERTAIN] هل يظهر البيع هنا؟) |

## ملاحظات نمطية

| الملاحظة | الدلالة |
|---|---|
| **F3** في كل استعلام مالي | عائلة الاستعلام المالي الموحدة (FAS/HRP) |
| **From/To Asset بF1** | نطاقات الأكواد 12 محرفاً قابلة للقص — الترميز الطبقي يُستغل في القص (5+3 تقاطع) |
| Details (Q) **بلا Property** | يقبل ضمنياً كل الفندق/الفندق الحالي — [NOT DOCUMENTED] سلوك الـProperty في Q-FX-01 |
| لا Drill-Down ولا تصدير Excel | خلافاً لMNT Parameter Listing — استعلامات عرض خالصة |
| لا استعلام "قيمة الأصول اليوم" | الرؤية اللحظية عبر Asset Ledger (R) فقط — ثغرة تشغيلية يومية |
| لا استعلام مكوّنات أصل | مكوّنات الأصل تُرى من Master (browse) فقط |
| History = أثر زمني كامل | مفهوم "الخلود الزمني" للإهلاك (لا تعديل موثق على تاريخ محسوب سوى Rollback الكامل) |

## قرار إعادة البناء

> **D-FX-2:** يُبنى استعلام موحد بمعايير تراكمية (FY/Month/Date × Location × Asset range × نوع الحدث Depn/Disposal/Sale/Component) — Query Report واحد يستبدل الثلاثة ويغلق فجوة "بيع ضمن Disposal History" بجعل نوع الحدث صريحاً.
