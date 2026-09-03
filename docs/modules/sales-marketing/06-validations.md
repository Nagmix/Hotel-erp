# 06 — التحققات (Validations) — وحدة SLM

> **28 تحقيراً موثقاً** V-SM-01..28 — مصدرها الصياغات الحرفية "should/shall/needs to/must" في الملفات الأربعة. توزيع مميز: كثافة تحققات **قيود المعالجة في التقارير** (نمط تواريخ صارم) + تحققات هوية الكود والتواريخ الفعالة.

---

## 1. تحققات الهوية والترميز

| ID | التحقق | النص/الدلالة | المصدر |
|---|---|---|---|
| V-SM-01 | كود الشركة ≤ 7 خانات alphanumeric | "supports alphanumeric values of character length up to 7" | PRF §7 |
| V-SM-02 | أول 3 خانات = نوع من Company Types (FO) | "predefined using Company Types under Front Office Setup" | PRF §7 |
| V-SM-03 | توليد المسلسل: **آخر مسلسل لنفس (نوع+حرف)** | "The system checks the last serial number for the company type and automatically generates the next number" | SLT §10 |
| V-SM-04 | كود Amenities فريد | "Enter a **unique code** in the Amenities field" | PRF §6 |
| V-SM-05 | Discount ID رقمي ≤ 4 خانات | "This field supports **numeric values** of character length up to **4**" | PRF §5 |
| V-SM-06 | كود Hotel Profile ≤ 3 خانات alphanumeric | "supports alphanumeric values of character length up to three" | PRF §17 |

## 2. تحققات التواريخ والفعالية

| ID | التحقق | النص | المصدر |
|---|---|---|---|
| V-SM-07 | تاريخ تفعيل الخصم ≥ اليوم (ddmmyy) | "Enter the **current date or a date greater than the current date** to activate" | PRF §5 |
| V-SM-08 | Business Lost: To ≤ تاريخ اليوم | "To Date entered should be **less than or equal to current date**" | REP §1 |
| V-SM-09 | Market Share: To شهر/سنة = From شهر/سنة | "month and year entered in the To Date field **should be equal** to the month and year of the From Date" | REP §2 |
| V-SM-10 | Sales Call: التواريخ داخل شهر واحد | "The date entered should be **within the specified month**" | REP §3 |
| V-SM-11 | Follow-up/Schedule: المدى داخل سنة واحدة | "date range should be **within the specified year**" | REP §4 |
| V-SM-12 | Sales Performance: المدى ≤ 31 يوماً | "date range should **not exceed 31days**" | REP §19 |
| V-SM-13 | Company Productivity/Contribution: المدى < اليوم | "should be **lesser than the current date**" | REP §14/§15 |
| V-SM-14 | Contribution Datewise: داخل نفس الشهر | "should be **within the same month of the year**" | REP §15 |
| V-SM-15 | Sales Performance (Budget): To ≤ اليوم | REP §7 | REP §7 |
| V-SM-16 | Prod. Variance: الشهر ≤ الشهر الحالي | "month range entered should be **lesser than or equal to the current month**" | REP §18 |

## 3. تحقيات الائتمان والمالية (من Company Profile)

| ID | التحقق | الدلالة | المصدر |
|---|---|---|---|
| V-SM-17 | تجاوز الحد الائتماني ⇒ منع تسوية FO/POS/BNQ + منع الترحيل اليدوي | القفل الثلاثي اليدوي (راجع BR-SM-01) | PRF §7 |
| V-SM-18 | Credit Days مشروطة بـAllow Credit = Yes | "Enter the number of credit days **if you have selected Yes** to Allow Credit" | PRF §7 |
| V-SM-19 | سجل القائمة السوداء يستوجب سبباً ومصرّحاً | reason + authorizer قبل التفعيل | PRF §7 |

## 4. تحققات التبعية الهيكلية

| ID | التحقق | النص | المصدر |
|---|---|---|---|
| V-SM-20 | تفعيل تحقق Cutoff يتطلب INI #41 = '0' | "needs to be activated by setting it to '0'" | PRF §14 |
| V-SM-21 | وضع Week/Day Access يتبع Module Attribute #8 | تحقق شرطي مزدوج القيمة | PRF §12 |
| V-SM-22 | دخول المخطط التنفيذي يتطلب ربط User↔Executive | "can be executed only by sales executives who have been **mapped** to a user id" | SLT §9 |
| V-SM-23 | تعديل Revenue Discount "with validations as applicable" | "Information created here can be edited/deleted **with validations as applicable**" — غير مفصلة! (GAP-SM-D03) | PRF §5 |
| V-SM-24 | Forecast ينبغي أن يطابق Allocation | "should match with the allocation information" — درجة إلزام غير محسومة | PRF §13 |
| V-SM-25 | بيانات General Information للأداة: **لا تعدَّل من الأداة** | "You cannot modify any fields" | SLT ص10 |

## 5. تحقيات الإدخال التاريخي والصور

| ID | التحقق | النص | المصدر |
|---|---|---|---|
| V-SM-26 | Daily Occupancy: إدخال backdated **قبل تشغيل PMS** | "record the backdated room occupancy information... **before IDS PMS went on live**" — نطاق زمني مقيد بطبيعة البيان | SLT §1 |
| V-SM-27 | صيغة تاريخ الخصم ddmmyy | "The date format is ddmmyy" — تنسيق إلزامي | PRF §5 |
| V-SM-28 | صورة الفندق: BMP فقط | "You can upload only bmp files" | PRF §17 |

---

## 6. ملاحظات تحققية للنمذجة (قرارات إعادة البناء)

1. **D-SM-1:** عائلة قيود التاريخ في التقارير (V-08..V-16) نمط "شهر/سنة/31 يوم" — تُترجم server-side query validators في Frappe (فلاتر تقرير قياسية).
2. **D-SM-2:** نقطة تفعيل V-SM-17 (عند توليد الفاتورة؟ عند تسوية ائتمانية؟ عند ترحيل يدوي؟) — النص يجمع "settlement... or manual posting" — يُقرر مرة واحدة في طبقة Customer credit balance API مشتركة لـFO/POS/BNQ.
3. **D-SM-3:** V-SM-03 (مسلسل لكل نوع+حرف) يفترض فهرس فريد مركب (type_prefix, letter, serial) — يمنع التصادم عند التحويل المتزامن.
4. **D-SM-4:** V-SM-24 (تطابق forecast=allocation) يُنفذ تحذيراً (warning) لا قفلاً — النص توصية "should" وليس "must".
