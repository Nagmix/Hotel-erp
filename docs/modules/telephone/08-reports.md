# 08 — التقارير (Reports) — وحدة TEL

> **8 تقارير (REP — 20 ص)** — عائلتان: **تشغيلية** (List All Calls / Extension Wise / Call Summary / Transferred / Unbilled / Guest List) و**مرجعية** (Print Telephone Bill + Telephone Master List بثلاثة أنماط). كل التقارير تعرض منظور **P&T Charge مقابل Guest Charge** + خيار Include Taxes.

---

## 1. List All Calls ⭐ (الأغنى خيارات)

| البند | المواصفات |
|---|---|
| الغرض | "a list of all calls made from the Property" |
| المجمّعات | **Date Range** (≤ Current Date + **within the same month**) · **Time Range** (فقط عند From=To!) — مثال الدليل: "From 10th Oct 2010 to 10th Oct 2010... time slot from 10 am to night 23 pm" |
| أنواع المكالمات | All / IDD / **SPL** / STD / Local — تعريفات الدليل الحرفية: "IDD = International · **SPL = calls to Special numbers like Toll Free** · STD = National · Local = within the State/Province" |
| المواضع | Rooms and Extensions / Only Rooms / Only Extensions (امتدادات الأقسام) |
| منظور الأثر | **P&T Charge أو Guest Charge** |
| الخيارات | Include Taxes |
| الفرز | Order By: **Extension # / Date & Time / Trunk Line Date & Time** — "Trunk Line is the Service Provider's line" |
| التوليد | معاينة (شاشة) ثم Print |

## 2. Print Telephone Bill (فاكورة النزيل)

| البند | المواصفات |
|---|---|
| الغرض | "prints details about telephone calls from a particular extension in a room or department" |
| التاريخ | For the Date (≤ **Accounting Date**) — افتراضي اليوم |
| النطاق | All Rooms أو Specific Rooms (Room# F1) |
| الخيارات | Include Taxes · **Round Sec (60)** — "round off the seconds" |
| تجميع الطباعة | **Room # wise أو Registration # wise** |
| الأعمدة | "Called number, Place, Time, Duration, call amount, tax amount, **net amount**" لكل مكالمة |
| ملاحظة العرض | "The call duration is printed in **seconds by default**. If you want... in **minutes**, then change the settings in **Module Attributes** (Refer CHAPTER SUPERVISOR under MODULE SYSTEM SETUP)" — إعداد عرض خارجي |

## 3. Call Summary by Department

| البند | المواصفات |
|---|---|
| الغرض | "calls made from the various departments... for a given date range within a month" |
| المجمّعات | Date Range (نفس الشهر) · All/Specific Departments (F1 — الاسم تلقائي) |
| الخيارات | التوليد بمعاينة ثم طباعة |

## 4. Transferred Call List

| البند | المواصفات |
|---|---|
| الغرض | "all calls that were transferred using the transfer call option... between rooms and departments extensions" |
| التاريخ | Date (≤ Accounting Date) |
| الفلاتر | **Extn to Extn / Extn to Room / All** |
| الخيارات | Include Taxes |

## 5. Extension Wise All Calls

| البند | المواصفات |
|---|---|
| الغرض | "print/view a list of extension wise calls" |
| النطاق | All Extension / **Guest Extension** (نزلاء فقط) / **Other Extension** (أقسام) |
| المقياس | **Date Range Wise أو Extension Range Wise** (From/To امتداد بF1) |
| الفلاتر | Call types (checkboxes) · P&T/Guest · Include Tax |
| تنسيقات | **Page Skip By Extension** (صفحة جديدة لكل امتداد!) · **Summary wise Extension** (ملخص لكل امتداد) |

## 6. Telephone Master List (مرجعي ثلاثي الأنماط) ⭐

| النمط | المُدخل | الناتج |
|---|---|---|
| **Extension** | Extension type (قائمة) | "entire list of extension numbers, extension types and the **charges applicable for each call type**" |
| **Area Code** | Country (قائمة) | "all the area codes for all the Countries... the slab types applicable for each area and the **maximum and minimum call charges**" |
| **Rate List** | Slab + Currency (قائمتان) | "different types of rate slabs, call charges from the **service provider and the Property** for different time periods and the **currencies** applicable" |

- **الدلالة:** مرجع تسعيري مطبوع كامل — وثيقة تدقيق/تسليم الورديات.

## 7. Unbilled Call List ⭐ (حوكمة الفوترة)

| البند | المواصفات |
|---|---|
| الغرض | "All calls that were **not posted to room folios** are printed in this report" |
| التاريخ | Date (≤ Accounting Date) — افتراضي اليوم |
| الخيارات | Include Taxes |
| العلاقة | قرين استعلام LUK §1 (View Unbilled Calls) لكن **بلا فلتر Error Type** — التقرير يسرد والاستعلام يشخّص |

## 8. Guest List

| البند | المواصفات |
|---|---|
| الغرض | "in-house Guests list... for the current date" (تاريخ تلقائي) |
| الفرز | **By Name أو By Room** |
| الخيارات | "Print All Room / **Billing Instruction** / **Floorwise**" |

## 9. الجرد التقاطعي

| الخاصية | التقارير |
|---|---|
| قيد نفس الشهر | List All Calls · Call Summary · Extension Wise (Date Range) |
| قيد ≤ Accounting Date | Print Bill · Transferred · Unbilled |
| P&T/Guest | List All · Extension Wise · Room Calls Query (LUK) |
| Include Taxes | List All · Print Bill · Transferred · Extension Wise · Unbilled |
| معاينة ثم طباعة | كل التقارير الثمانية (نمط شاشة → Print) |
| F1 Help | Rooms (Print Bill) · Departments (Summary) · Extensions (Extension Wise) |
| افتراض التاريخ | اليوم (Print Bill/Unbilled/Guest) — Accounting (استعلام LUK) |

## 10. ثغرات التقارير

| الثغرة | التفصيل |
|---|---|
| لا فلترة Error Type في Unbilled REP | الاستعلام LUK يملكها والتقرير لا — عكس المعتاد (التقرير أفقر من الاستعلام!) |
| Guest List للتاريخ الجاري فقط | "for the current date" — تاريخ تلقائي غير قابل للتغيير الموثق |
| لا تجميع Revenue Code | لا تقرير إيراد هاتفي تراكمي (يُنتظر من FAS/FO أو غير موجود) |
| لا كشف P&P للمزوّد | ثنائية P&T موجودة كأعمدة لا كتقرير مصروف مقدم الخدمة |
| SPL بلا مسار ماستر | يظهر في List All Calls كنوع — وقيده في Calculation% Others غير موثق (GAP-TE-D05) |
