# 10 — مصفوفة قواعد التواريخ — MGT-REP (Phase 7)

> ~21 قاعدة موزعة على ~53 تقريراً — **ثلاث بوابات زمنية جديدة** لا مثيل لها في FO/POS: بوابة "الآن فقط" ×2 وبوابة "البيانات" ×1.

---

## 1. البوابات الجديدة المكتشفة في MGT

| البوابة | التقرير | النص الحرفي | الجدة |
|---|---|---|---|
| **الشهر/السنة الجارية فقط** | 4.8 Opening Balance List | "as on **current Month and Year**" | أول قيد "الشهر الجاري" في الحزمة (أضيق من same-day) |
| **تاريخ النظام الحالي فقط** | §17 Re-Order Level Items | "processed for the **Current System Date**" | عائلة as-of-now — لا تاريخ إطلاقاً في المعايير |
| **تواريخ الجرد المُدخلة فقط** | 18.1 Physical Stock Variance | "only for dates on which the **Physical Stocks were entered**" | **بوابة بيانات** — النطاق يرث وجوده من مصدر OLTP |
| السنة المالية الجارية فقط | 22.2 CC Budget Consumption | "for the specified period of the **current financial year**" | (22.1 يقبل FY معرّفاً — الاختلاف بين الشقيقين!) |

## 2. المصفوفة الكاملة

| # | التقرير | القاعدة | النص/الدلالة |
|---|---|---|---|
| 1 | §1 Inventory Item List | بلا تاريخ | قائمة ماستر (لا نطاق) |
| 2 | §2 Requisition Status | **Date XOR Month** | "Select an option Date range/Month range" |
| 3 | §3 PO Status | PO Date + **Upto Date** | as-of لكمية "received up to date" |
| 4 | 4.1 Transaction Checklist | Date range | — |
| 5 | 4.2 Receipt Register | **Date XOR Month** | ثنائية موحدة |
| 6 | 4.3 Capital Goods Receipt | **Date XOR Month** | قالب 4.2 |
| 7 | 4.4 Receipt/Issue by Group | **Date XOR Month** | — |
| 8 | 4.5 Receipt/Issue Consolidate | **Date XOR Month** | — |
| 9 | 4.6 Consolidate Receipt Value | **Date XOR Month** | — |
| 10 | 4.7 Supplier Receipt Register | Date range | — |
| 11 | **4.8 Opening Balance List** | **current Month/Year فقط** | 🆕 الجاري حصراً |
| 12 | 5.1 CC Consumption | Date range | — |
| 13 | 5.2 CC Consumption Summary | (غير موصّف) | "appropriate options" |
| 14 | 5.3 Group Consumption Month Range | Date range | Month Range في الاسم |
| 15 | 5.4 GCMR – **R2** | month range | صياغة "month range" الصريحة |
| 16 | §6' Closing Stock by Type | **أي تاريخ** | "as on **any given date**" — as-on حر (مقابل 4.8!) |
| 17 | §7 One Line Store Balance | Date range | — |
| 18 | §8 Store Balance by Date | **نطاق داخل الشهر** | "date range **of the month**" — month-bounded |
| 19 | 9.1 Item Stock Details | Date range | — |
| 20 | 9.3 Ledger by Item | **Date XOR Month** | ثنائية |
| 21 | 9.4 Item Expiry List | Date range + **N أيام إنذار** | "populated on time based on the number of days entered" |
| 22 | §10 Supplier Bill | Date range + Month + **Credit Days** | زمن ذمم |
| 23 | §11 ABC Analysis | Date range | — |
| 24 | §12 FSN Analysis | Date range + **Cut off Days** | — |
| 25 | §13 Slow Moving | Date range + **Percentage** | — |
| 26 | §14 Non Moving | **Cut Off Days فقط** (بلا نطاق) | "classified based on the Cut Off Days specified" |
| 27 | §16.1 Sub Store Transfer List | Date range | — |
| 28 | **§17 Re-Order Level Items** | **Current System Date فقط** | 🆕 as-of-now |
| 29 | 18.1 Physical Stock Variance | **تواريخ الجرد فقط** | 🆕 Data-gated |
| 30 | 18.2 Physical Stock Valuation | **as on a specified Date** | — |
| 31 | 18.3 Negative Variance | as on specified date + **قبل/بعد Update** | مرونة توقيت |
| 32 | 18.4 Print Stores Ledger | **شهر أو مدى شهور** | فترات محاسبية |
| 33 | §19 Comparative Statement | **Quotation Month/Year** | مفتاح عطاء |
| 34 | §20 Item Conversion Checklist | Date range | — |
| 35 | §21 Efficiency Report | (معايير عامة) | "appropriate options" |
| 36 | 22.1 Budget Actual Consumption | **FY + Month/Year** | سنة مالية |
| 37 | 22.2 CC Budget Consumption | **current FY** | 🆕 الجاري المالي |
| 38 | 24.1 VAT Report | Date Range | + assessment year في الشاشة الثانية |

## 3. مقارنة أنماط البوابات عبر المرحلة 7

| النمط | FO (~135) | POS (~57) | **MGT (~53)** |
|---|---|---|---|
| Date range حر | ✓ | ✓ | ✓ (الأغلب) |
| **Date XOR Month ثنائية** | نادر | نادر | **مبدأ معماري (~9 تقارير!)** |
| Month-bounded | ~15 | ~25 | **1 (صياغة واحدة!)** |
| future-only | عدة | 1 (Happy Hours) | **0** |
| past-only / as-on | عدة | عدة | 3 (16'/18.2/18.3) |
| **same-day/current فقط** | عائلة | — | **2 (4.8 + 17!)** |
| **Data-gated (ميراث OLTP)** | 0 | 0 | **1 (18.1!)** |
| **FY-aligned** | Budget | — | **2 (22.x)** |

**الاستنتاجات:**
1. **ثنائية Date/Month هي بصمة MGT المعمارية** — 9 تقارير تعرض الخيارين صراحة (مقابل ندرته في FO/POS) — الوحدة الأكثر "وعياً" بالفترة المحاسبية الشهرية بعد POS.
2. **لا مستقبل إطلاقاً**: صفر future-only في 53 تقريراً (MGT ماضٍ-وحاضر بحت — عكس POS التي تملك Happy Hours) — منطقي: المخزون لا يُستَقبل، يُجرَد.
3. **بوابة البيانات (18.1)** أعقد بوابات الحزمة: التقرير **لا يستطيع** الوجود حيث لا جرد — التحقق من الصلاحية الزمنية يهتم بوجود السجل المصدر لا بقاعدة تاريخ.

## 4. معايير ليست تواريخ لكنها "عتبات زمنية"

- **N أيام** (9.4 Expiry): نافذة إنذار مستقبلية ضمنية — الأصناف التي ستنتهي خلال N يوماً = أقرب شيء للمستقبلي في الوحدة.
- **Cut off Days** (§12/§14): عتبة تقادم.
- **Percentage** (§13): عتبة بطء نِسَبية.
- **Credit Days** (§10): أعمار ذمم — زمن مالي لا تشغيلي.

> هذه "شبه-التواريخ" تُختبر جميعها رقمياً في AC (ملف 11).
