# 05 — قواعد العمل (Business Rules) — وحدة SLM

> **20 قاعدة موثقة** BR-SM-01..20 — مرتبة بالأثر. القاعدة #1 (القفل الائتماني الثلاثي) أعنف قاعدة مالية عابرة للوحدات في المشروع كله.

---

## القواعد المالية (الأثر الأعلى)

### BR-SM-01 — القفل الائتماني الثلاثي + اليدوي 🔴
> "If the current bill and/or the amount receivable exceed the specified **credit limit**, settlement of the **Front Desk, Point of Sale or Banquet bill or manual posting of the bill is not allowed**." — PRF §7 (ص13)

- الشرط: (الفاتورة الحالية +/أو المديونية) > الحد.
- الأثر: **منع التسوية في 3 وحدات + منع الترحيل اليدوي** — Q: هل المنع عند التوليد أم التسوية الائتمانية فقط؟ النص يقول settlement — (قرار تصميمي عند التنفيذ D-SM-2).

### BR-SM-02 — الفائدة على تجاوز أيام الائتمان
> "Interest % — percentage of interest applicable on bills **that exceed the specified credit days**" — PRF §7.
(لا آلية احتساب/ترحيل فائدة موثقة — GAP-SM-P1).

### BR-SM-03 — عمولات الوكلاء وشركات البطاقات
> "Commission % — normally applicable to **travel companies or agents and credit card companies**" — PRF §7. (الاحتساب/الدفع خارج التوثيق — يُربط بدورة ACR).

### BR-SM-04 — Bypass Invoice
> Yes/No "if you want to generate an invoice to the account" — مستوى حساب AR (PRF §7).

## قواعد هوية العميل وبنيته

### BR-SM-05 — بنية كود الشركة 3+4
> "alphanumeric values of character length up to 7. The **first three characters is the guest/company type**, predefined using **Company Types under Front Office Setup**. The next four characters can be a combination of alphanumeric" — PRF §7.

### BR-SM-06 — التوليد الآلي عند تحويل Prospect
> "**COM** for companies, **TAG** for travel agents, **AIR** for airlines... next character = starting letter of company name. **The system checks the last serial number for the company type and automatically generates the next number**" — SLT §10.
- المسلسل **لكل (نوع + حرف)** — لا لكل نوع فقط! (دقة مهمة للنمذجة).

### BR-SM-07 — استثناء Prospects من الموازنات
> "It is important to note that **potential companies are not included** in this budget" — SLT §3 (CGR فقط).

### BR-SM-08 — قائمة المراقبة بتاريخ قطع
> Watch List + To Date: "if you require the room occupancy and business received information... **up to a specified date**" — PRF §7. + التقرير بخياري Include **Compliment**/Include **Houseguest** (REP §6).

### BR-SM-09 — القائمة السوداء تستوجب سبباً ومصرّحاً
> "If you set the option to Yes, then press Enter key to **enter the reason and the name of the person who authorized** the blacklist" — PRF §7. (العرض: Modify mode فقط).

## قواعد الوكلاء والتوزيع

### BR-SM-10 — تفعيل cutoff بجعل INI #41 = '0' (مقلوب!)
> "To activate the cutoff days validation during Reservation, Setting # 41 in the .INI file needs to be activated **by setting it to '0'**" — PRF §14.

### BR-SM-11 — Week/Day Access بسمة FO رقم 8
> "The Week Access column is **dependent on the Module Attribute # 8 for Reservations**: NO → week access screen... YES → **day access** screen" — PRF §12.

### BR-SM-12 — تطابق التوقع مع التخصيص
> "Forecast information that are entered here **should match with the allocation information created for the same company**" — PRF §13 (قاعدة مطابقة موصى بها — درجة الإلزام غير مقيدة).

### BR-SM-13 — From Date التخصيص = تاريخ المحاسبة
> "By default, the **Accounting date will be picked as From Date** and can be edited" — PRF §12. (نمط تاريخ المحاسبة FO المألوف!)

### BR-SM-14 — حجز Inside/Outside عند التحرر
> "Based on the cutoff days the **reservation program prompts** you to assign the rooms requested as **Inside or Outside allocation**" — PRF §14.

### BR-SM-15 — نسبة الحجز الفائقة
> "percentage of rooms that can be booked **above and over the number of rooms allocated**" — PRF §12 (Over-book %).

## قواعد التتبع والمخطط

### BR-SM-16 — المخطط التنفيذي محمي بربط هوية
> "password protected and can be executed **only by sales executives who have been mapped to a user id** using the Map User Id option" + التعميم بـINI #239 — SLT §9.

### BR-SM-17 — تحويل الموعد يوثق السبب
> Reschedule/Cancel/Transfer للمواعيد — كل إجراء يستوجب **reason** (وTransfer يحدد المندوب الجديد) — SLT §9.

### BR-SM-18 — ساعات المهام 7am–8pm بتصنيفين
> "Hourly schedules **from 7.am to 8.pm**... classified as **important and Normal**" + إمكانية وسم "completed" — SLT §9.

## قواعد الخصومات والسياسات

### BR-SM-19 — خصم إيراد بفعالية مؤرخة menu-wise
> Active Date "current date or a date **greater than** the current date" + Expiry Date + **خصم منفصل لكل Menu Type (FOOD/LIQUOR/SOFTDRINKS/TOBACCO/OTHERS) في F&B** — PRF §5.

### BR-SM-20 — سياسات الاحتفاظ/الإلغاء نسب من السعر المتفق
> Retention: "% of Room rate **agreed by the Hotel to the Company**" تُحصّل عبر FO "Retention-Cancel/No show" — PRF §10.
> Cancellation: مدى From Day/To Day **مقارنةً بتاريخ الإلغاء قبل الوصول** + نسبة — PRF §11.

## قواعد التقارير (قيود معالجة)

| # | القاعدة | المصدر |
|---|---|---|
| BR-SM-21 | Market Share: "month and year entered in the To Date **should be equal to** month/year of From Date" (شهر واحد!) | REP §2 |
| BR-SM-22 | Sales Call Report: "date entered should be **within the specified month**" | REP §3 |
| BR-SM-23 | Follow-up/Schedule: المدى "should be **within the specified year**" | REP §4 |
| BR-SM-24 | Sales Performance Report: "date range should **not exceed 31 days**" | REP §19 |
| BR-SM-25 | Business Lost/Productivity/Contribution: To ≤ تاريخ اليوم | REP §1/§14/§15 |
| BR-SM-26 | Company Contribution Datewise: "should be **within the same month of the year**" | REP §15 |
| BR-SM-27 | Birthday/Anniversary: مدى MM/YY | REP §5 |
| BR-SM-28 | Prod. Variance: "month range ≤ current month of the year" | REP §18 |

## قواعد العرض (استهلاك بيانات)

| # | القاعدة | المصدر |
|---|---|---|
| BR-SM-29 | عرض Receivables في أداة المدير: **cutoff = Accounting date** | SLT ص13 |
| BR-SM-30 | عروض Sales Activity/Entertainment/Guest Visits: افتراضياً **الشهر السابق** | SLT ص11/13 |
| BR-SM-31 | General Information في أداة المدير: **قراءة فقط** (مصدرها Prospect Entry) | SLT ص10 |
| BR-SM-32 | تصفية CGR في Daily Sales Call عبر checkbox (مستودع Company Master) | SLT ص16 |
| BR-SM-33 | Outlook كقناة Company Letters: **CEO → بريد الشركة · designation آخر → قائمة جهات الاتصال** | REP §12 |
| BR-SM-34 | صور الفندق: **BMP فقط** | PRF §17 |

> **الإحصاء النهائي: 34 قاعدة موثقة** (20 كبرى + 14 قيد معالجة/عرض) — أعلى كثافة قواعد في وحدة CRM-طابع في المشروع.
