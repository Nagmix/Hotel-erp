# 08 — التقارير (Reports) — وحدة GTP

> **4 مخرجات مطبوعة** (Register + Pending + Print + Report) — "طباعة" هنا وظيفة من الدرجة الأولى (التصريح ورقة أصلاً!)؛ السجل **مرتجع فقط** بنيوياً؛ المعلق **as-on** (وحده بتاريخ لحظي)؛ والجميع يشترك في checkbox 'Include remarks' (اثنان فقط).

---

## الجرد

| # | المخرج | المدخلات الموثقة | النطاق | المصدر |
|---|---|---|---|---|
| R-GP-01 | **Gate Pass Register** | Date range + **checkbox 'Include remarks'** | "all **returnable** Gate Passes issued by **various departments**" — مرتجع فقط! | §4 ص7-8 |
| R-GP-02 | **Pending Gate Passes** | **as-on date** + خيارات Query + **checkbox 'Include remarks'** | "pending Gate Passes register **as on a date**" | §5 ص8-9 |
| R-GP-03 | **Gate Pass Print** | المحور (Date / **Gate Pass #** / **Vendor**) + Date range + Returnable/Non-Returnable + **printer type** | تصاريح انتقائية للطباعة | §6 ص10-11 |
| R-GP-04 | **Gate Pass Report** | خيارات Query (مراكز + Date Range/As-on/GP# Range + النوع) | "transaction details of Gate Passes based on the selection criteria" | §7 ص11-12 |

## التحليل التفاضلي

| البعد | Register | Pending | Print | Report |
|---|---|---|---|---|
| الموضوع | التصاريح المرتجعة الصادرة | غير المكتملة | **إعادة إنتاج ورقة التصريح** | تفاصيل المعاملات |
| الزمن | نطاق | **as-on** (لحظة) | نطاق/محدد | نطاق/as-on/GP# |
| مرشح النوع | مرتجع مفروض | مرتجع مفروض ضمنياً (Pending=مرتجع) | **اختيار صريح** R/NR | اختيار صريح |
| الملاحظات | checkbox | checkbox | — | — |
| الطابعة | مطبوع | مطبوع | **اختيار الطابعة!** | عرض |

## ملاحظات تحليلية

| الملاحظة | الدلالة |
|---|---|
| **الطباعة (R-GP-03) هي جوهر الوحدة** | "to print Gate Passes for selected Date range / Gate Pass / Selected Vendor" — إعادة إنتاج وثيقة البوابة بأثر رجعي/انتقائي (نسخة ثانية لنفس التصريح — **هل يبطل القديم؟** على خلاف Check reprint في TSC الذي يلغي ويولّد رقماً جديداً — [NOT DOCUMENTED]!) |
| Register "by various departments" | تجميع بالأقسام = Cost Centers — القناة التنظيمية الوحيدة تعمل هنا كمجمّع |
| ثنائية الأغراض Query/Report | بنية المعايير نفسها تقريباً (استعلام ص6-7 مقابل تقرير ص11-12) — زوج Q/R كعائلة FXD |
| 'Include remarks' | إظهار نافذة الملاحظات المشروطة (BR-GP-06) في الورق — الشرح الورقي للكمية |
| لا تقرير إحصائي/تحليلي | لا معدلات عودة ولا متوسط زمن — وحدة ضبط لا BI |
| لا أعمدة موصوفة | التوثيق أضأل من وصف الأعمدة — [NOT DOCUMENTED] بنية كل مخرج |

## قرار D-GP-4 (إعادة البناء)

Print: **Status "Printed" موقّع بطابع زمني** لكل نسخة + منع إعادة الطباعة إلا بصلاحية Auditor (سد ثغرة النسخ المزدوجة) · Register/Pending: أصول **Frappe Print Format + Query Report** مباشرة.
