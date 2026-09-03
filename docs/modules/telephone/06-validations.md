# 06 — التحققات (Validations) — وحدة TEL

> **V-TE-01..26** — تحققات إدخال موثقة بالأطوال والقيود الحرفية (امتداد 6 · نسبة 3 · دولة 10 · بطاقة 10 · برنامج تحويل 7 · كلمة مرور 10 خانات) + **قيود تواريخ صارمة متدرجة** (أكبر من تاريخ المحاسبة / أصغر أو يساوي / نفس الشهر) + قيود تشغيلية (غرف مشغولة، قسم المصدر).

---

## أ) تحققات الحقول (أطوال وأنماط)

| ID | الحقل | القاعدة الموثقة | المصدر |
|---|---|---|---|
| V-TE-01 | Extension # | "numeric values of character length up to **6**" | SET ص4 |
| V-TE-02 | Calculation % (الأربعة) | "numeric values of character length up to **3**" | SET ص4 |
| V-TE-03 | Extension Name | "alphanumeric values and special characters of length up to **30**" — اختياري | SET ص5 |
| V-TE-04 | Extension Type | قائمة محصورة: **Phone / Fax** | SET ص5 |
| V-TE-05 | Equipment Code / Location Details | اختياريان — "you can save the details without this information" | SET ص5 |
| V-TE-06 | EPABX Prefix | "a **single** alphabet/digit code" — اختياري | SET ص16 |
| V-TE-07 | Conversion Program | "alphanumeric values of character length up to **7**" | SET ص16-17 |
| V-TE-08 | Country Code | "alphanumeric values of character length up to **10**" | SET ص22 |
| V-TE-09 | Country Name | "up to **30**" | SET ص22 |
| V-TE-10 | Area Code / Area Name | "**10** / **30**" | SET ص24 |
| V-TE-11 | Slab Name | "up to **30**" | SET ص19 |
| V-TE-12 | Extension Password | "only numbers and maximum of **10 digits**" | CAC ص9 |
| V-TE-13 | Address Book: Main Category | "mandatory... alphanumeric of **15** characters" | LUK ص16 |
| V-TE-14 | Address Book: Sub Category | "optional... **15**" | LUK ص16 |
| V-TE-15 | Address Book: Prefix/Name | "**10 / 45**" | LUK ص16 |
| V-TE-16 | Address Book: Address/City/State/Phone/Fax | "**100 / 30 / 30 / 30 / 30**" | LUK ص16-17 |
| V-TE-17 | Address Book: Pager/Email/Cellular/Remarks | "**20 / 30 / 20 / 200**" | LUK ص17 |
| V-TE-18 | Call Identifier Code | "The code is the **initial portion of the called number**" (بادئة) | SET ص31 |

## ب) تحققات التواريخ (متدرجة بثلاث درجات) ⭐

| ID | السياق | القاعدة | الدرجة |
|---|---|---|---|
| V-TE-19 | Holiday Table | "should be **greater than the accounting date**" — ddmmyy | مستقبلي صارم |
| V-TE-20 | Time-Rate Slabs (Applicable From) | "must enter a date **greater than the current date** to activate the setting active for a future date" + لا اختيار شريحة "created **on the same date**" | مستقبلي + عبور |
| V-TE-21 | Print Telephone Bill / Transferred List / Unbilled / Error | "less than or **equal to the Accounting Date**" | تاريخ محاسبي |
| V-TE-22 | List All Calls / Call Summary / Extension Wise | "less than or equal to the **Current Date** and **within the same month**" | تاريخ نظامي + شهر واحد |
| V-TE-23 | View Transfers/Extensions | "less than or equal to the **Current date**" | تاريخ نظامي |

- **قاعدة الوقت المشروطة:** "If you select only one date (Enter the same date in the From and To Date fields)... then you will have an option to enter the time range, **else this option is not applicable**" (List All Calls) — نطاق زمني ليوم واحد فقط.

## ج) تحققات تشغيلية (علاقات)

| ID | القاعدة | المصدر |
|---|---|---|
| V-TE-24 | كلمة المرور للغرف: "The user can select **only occupied rooms** from the Room numbers list" | CAC ص8 |
| V-TE-25 | تحويل المكالمات: From Extension "has to be a **department extension number only**" — "The application does not allow... from a room or a shop" | CAC ص6-7 |
| V-TE-26 | إعادة ترحيل الأخطاء: تتطلب تحويل Select إلى YES يدوياً (نقر مزدوج) قبل الحفظ | CAC ص6 |

## د) تحققات ضمنية (من سلوك الواجهات)

| السلوك | الاستدلال الموثق |
|---|---|
| انتقال المؤشر الذكي | "If you selected the Extension 'Room', then the cursor will move to the Room # field" — فرض تسلسل الإدخال حسب النوع (SET ص4) |
| Day تلقائي | "Automatically displays the day of the date" في Holiday Table (SET ص10) |
| Today Date تلقائي | "This is the system date auto populated" في كرت الباب (SET ص28) |
| التواريخ التلقائية | "The Accounting Date and the System Date will be auto populated" في Error (CAC ص5) + "By default, the current date will be displayed" (REP ص6، ص18) + "By default the Accounting Date" (LUK ص3) |
| From Time تلقائي | "This is system generated. By default it is, 00.00" (SET ص19) |
| Department Name تلقائي | "the respective department's name will appear in the Department Name field" (REP ص9) |
| Location تلقائي | "The Location details of the extension number specified will populate" (CAC ص9) |
| الجدول المزدوج بالأعطال | لا قيد يمنع الحفظ — الحقول الاختيارية الموثقة تُحفظ فارغة (SET ص5) |
| قيود القوائم | كل F1 Browse (امتدادات/غرف/أقسام/عملات/شرائح/Reg#) يفرض اختياراً من المعرف فقط — لا إدخال حر للمفاتيح الخارجية |

## هـ) حدود غير موثقة (فجوات تحقق)

| الموضع | الوضع |
|---|---|
| تفرّد Extension # | غير مصرح — يُفترض (مفتاح) لكن لا نص |
| تناقض Min/Max | لا تحقق أن Minimum ≤ Maximum في Area Codes |
| تناقض Others (مبلغ/نسبة) | GAP-TE-D04 — الحقل % لكن وصفه كمبلغ أدنى |
| نطاق Round Amount | لا قيد موجبية/حدود |
| صلاحية كلمة المرور | لا تعقيد (أرقام فقط!) — معيار أمني بدائي موثق |
| تكرار كود الشراكة | لا منع موثق من حذف LCA/9999999999 الحساسة! |
