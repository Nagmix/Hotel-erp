# 09 — مصفوفة قواعد التواريخ والأعمدة (FOM-REP)

> ~25 قاعدة تاريخ صريحة + قواعد تنسيق الأعمدة — أغلى مصفوفة تحقق في طبقة التقارير بالمشروع. كل قاعدة بنص حرفي من الدليل.

---

## 1. قواعد اتجاه الزمن (Future / Past)

| التقرير | القاعدة الحرفية | الصنف |
|---|---|---|
| Expected Arrivals 80/132 (12/13) | "should be a **future date only** because we are generating the report for expected arrivals" | future-only |
| GH Arrivals (17) | "greater than the **accounting date**" | future-strict |
| Arrivals for the Day (16) | "less than the **accounting date**" | past-only |
| Reprint Voucher (9) | "≤ current date" | past-inclusive |
| Arrivals Date Range (71) | "≤ **server date**" (لفظ الخادم!) | past-server |
| Group Wise Checkout (69) | "≤ **server date** and within the same month" | past-server + month |

**الملاحظة الاصطلاحية**: الدليل يستعمل **ثلاث ساعات مرجعية**: accounting date (الغالبية) · current date (13 موضعاً) · **server date** (69/71 فقط) — التقارير المالية الصرفة تميل لـaccounting date والحدود الزمنية للنظام لـserver date. توحي بأن accounting date قابلة للتأخر عن ساعة الخادم (Night Audit لم يُقفل) → قرينة على Design النافذة الليلية.

## 2. قيود النطاق الرقمية (فجوة قصوى)

| التقرير | القيد |
|---|---|
| Tips Statement (84) | "date difference should **not be greater than 31 days**" |
| Plan Forecast (52) | "date range **cannot exceed more than 30 days**" |
| Mat./Forecast Rev. (131) | "maximum **10 days only**" |
| Mat./Forecast Room (132) | "maximum **31 days only**" |

**السلم النافذي**: 10 ← 30/31 — عتبات مرتبطة بحجم البيانات المتوقع (حجوزات يومية كثيفة الكثافة vs إشغال).

## 3. قيود "نفس الشهر/السنة" (Month-Boundary)

| التقرير | القيد |
|---|---|
| Guest Visit by Nation (48) | "< accounting date" + same month+year |
| Foreigners Verification (50) | same month |
| Reopen Folio (31.6) | "≤ accounting date and **within the same year and month**" |
| Change Room Type (31.8) | "≤ current date and within the **same Month and Year**" |
| Misc. Sales Register (80) | "The month and Year should be the same for From and To Dates" |
| Bill Summary (85) | "< current date" + same month |
| Settlement Summary (86) | same month |
| Tax Report (93) | "< accounting date" + same month+year |
| Consolidated Tax Register (94) | "within the same month and ≤ accounting date" |
| CC Encashment (96) | same month |
| Group Revenue (134) | "within the same month and ≤ accounting date" |
| Laundry Sales by Item (113.1) | "within the same month and ≤ accounting date" |
| Tourist Arrivals (70) | "≤ Current Month and Year" |
| Foreign Exchange Summary (88) | "≤ current month and year" |
| Reprint FO Bill (92) | "≤ Current Month/Year" |

**التفسير البنيوي**: التقارير المرتبطة بدورة الإقفال الليلي/الشهري (ضريبة/تسوية/فواتير) حبيسة الشهر — **مؤشر قوي على أن الإقفال الشهري data-retention boundary فعلي** (الأرشفة/الإجماليات تُحسب شهرياً). أي reproduction حديث يقرر: هل يرفع القيد أم يحاكيه؟ (يُنصح برفعه مع فهرسة، مع الإبقاء على تنبيه).

## 4. قواعد التواريخ القِيَمية الخاصة

| التقرير | القاعدة |
|---|---|
| Re-Confirm Bookings (4) | Re-confirm date "≥ the accounting date" |
| Operational Report (1) | "To Date should be greater than the From Date **[Current Date]**" |
| Wakeup Call List (32) / Pickup-Drop (20) / Guest Trace (26) | "≥ current date" |
| Departure Slip (68.4) / Expected Departures (68.2) | "≥ accounting date" (68.4 صريح "greater than **or equal**") |
| Checkout for the day (68.1) / Early Departures (68.3) | "≤ accounting date" |
| Room Status Audit (31.2) | "> accounting date" (مستقبلي لأنه تدقيق تغييرات وامضة؟ — لفظ الدليل حرفياً) |
| Room Transfer Audit (31.4) / Foreign Exchange List (87) | "≤ accounting date" |
| Night Report (102) / Guest Ledger Balance (99) / Oneline GL (101) | "≤ accounting date" |
| Occupancy Statistics (66) | تاريخ حر (أي يوم) |
| Guest Telephone Bill (79) | Month/Year آلي من الغرفة |

## 5. قواعد أعمدة الطباعة (80/132 + XOR)

| التقرير | الصيغة |
|---|---|
| Night Report (102) | **80** = يوم + شهر (+ خيار **Year to Date**) · **132** = يوم + شهر + **سنة** (وخيار YTD **معطّل**) — "If option 80 Column is selected, you get the option to select 'Year to Date', and if 132 Column is selected, then the 'Year to Date' option will be **deactivated**" |
| User Defined Report (104) | **Print Net Values** يقفل 80 و132 (XOR ثلاثي: "then the other two options are deactivated") · 80 = يوم+شهر · 132 = +سنة + "current year and **previous year**" |
| Expected Arrivals (12/13) | 80: One Line + FIT/Group Break Up · 132: **Likes/Dislikes + Guest Status Summary + Booker Info Only** |
| Settlement Summary (86) | **Print 132** كـcheckbox |
| Occupancy Statistics (66) | **132 Column** كخيار |
| FO Budget Report (106) | 80 = يوم+شهر أو يوم+سنة · 132 = يشمل السنوي |
| HRP-REP المقابل | 80/132 في Salary Abstract — نمط الحزمة العام |

**المنطق التاريخي**: 80/132 = عرضا الورق التسلسلي القديم (Dot-matrix). الدليل يربط **محتوى أعمال بالصيغة** (132 يحمل أعباء سنوية أعرض!) — عند التنفيذ تُهجر الصيغتان لصالح HTML Print Format واحد متجاوب، مع حفظ الاختلاف الدلالي (YTD يظهر دائماً).

## 6. قواعد إدخال أخرى قابلة للتحقق

- Cut Off Amount (77): "only in numbers **without any special characters**" — numeric strict.
- Shift times (89): "should be entered in **24 Hour format**".
- Guest Details في Lost & Found (111): "**Atleast one field should be entered**" — required-any-of validation.
- Copies في Pre-Reg Card (22): رقم نسخ موجب.
- From/To Company (73): "enter the company code **range** in the From and To fields" — مدى أكواد.

## 7. جدول الملخص التنفيذي (للتحويل إلى فحوصات)

| عائلة القاعدة | العدد | القرار الموصى به عند التنفيذ |
|---|---|---|
| future-only / future-strict | 6 تقارير | Validation مع رسالة تشرح السبب (كالدليل) |
| past-only / past-inclusive | 9 | Validation |
| month-boundary | 15 | **رفع القيد** + فهرسة زمنية + تنبيه تجاوز (backward-compatible) |
| window caps (10/30/31) | 4 | رفع مع pagination |
| XOR أعمدة/خيارات | 3 (102/104/8) | UI يعكس القفل بصرياً |
| مرجع زمني | accounting vs current vs server | **توحيد على Posting Date + Today** مع إبقاء مفهوم قفل Night Audit |
