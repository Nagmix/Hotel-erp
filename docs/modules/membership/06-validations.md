# 06 — التحققات (Validations) — وحدة MEM

> **V-ME-01..22**: القيود الموثقة نصاً، مرتبة بحسب الشاشة. وحدة MEM **متوسطة الصرامة** — أغلب التحققات تواريخ مستقبلية وإلزاميات بنيوية، لكن **بلا تحقق رصيد/ائتمان موثق** في Service Bill (مقارنة بـ POS/FO).

---

## التحققات الزمنية (عائلة Future-Only)

### V-ME-01: تاريخ سريان أسعار الخدمات
"Date should be **greater than or equal to the current system date**" (SET ص6 — Application Date في Service Rate Master).

### V-ME-02: تعديل الأسعار قبل السريان فقط
"You can modify a record only if the date in the 'Applicable From' field is **greater than the current date**" (SET ص8) — **قفل تعديل تاريخي**: ما بدأ سريانه يصبح للقراءة.

### V-ME-03: تاريخ الأسعار الثابتة
"The date entered should be **greater than or equal to Current date**" (SET ص12 — Facility Fixed Rates).

### V-ME-04: منشأ رسوم المرافق
"The **From Date should be less than or equal to current date**" (MTR ص16 — Process Facility Charges) — لا ترحيل مستقبلي.

## إلزاميات الهيكل

### V-ME-05: صلاحية التحويل المؤسسي إلزامية
"It is mandatory to enter values in the **Validity section**" (MPF ص23 — From/UP TO/Renewal عند تحويل طلب شركة).

### V-ME-06: سمة فحص صلاحية الأساسي
"Primary Member Validity Checking Required: Yes - A valid date in the **UPTO field has to be mandatorily recorded** in the Membership Master" (SET ص12).

### V-ME-07: الكنية شرط جسر ACR
"If flag # 10 is activated this flag cannot be de-activated" + "This flag is activated **only if flag # 9 is activated**" (SET ص11-12) — تبعية + عدم رجعة.

### V-ME-08: العناوين وسيلة اتصال
"You must tag any one address as the **correspondence address**" (MPF ص4 وص6) — للشركة والفرد.

### V-ME-09: فئة المرشحين تفعّل عدد المرشحين
"This field [Number of nominees] is activated **only if the Category is Corporate type**" (SET ص4).

### V-ME-10: ماستر الخدمة شرط الفوترة
"This option [Service Rate Master] is **mandatory for the Service Bill Entry**" (SET ص7) — لا فوترة بلا أسعار معرفة مسبقاً.

## تحقق الحالة والسلوك

### V-ME-11: منع المرافق للقائمة السوداء (مشروط)
"Do not allow blacklist members for facilities: Yes - The blacklisted members will **not be able to avail any facilities**" (SET ص12) — سلوك منع في Service Bill/Guest Visit — يعمل فقط لو السمة Yes.

### V-ME-12: الإنهاءات لا تمس الفرد الأساسي عكسياً
التحقق المضاد للتتالي: أي إنهاء لفرد فرعي "the primary member is **not affected**" (MMN ص6/8/9/12).

### V-ME-13: الرسوم على المدين فقط
"if the outstanding amount is **Debit** amount then it will calculate the Latefee" (MTR ص18) — تحقق اتجاه الرصيد قبل الرسوم.

### V-ME-14: خيار None في الخلافة محدد العواقب
اختيار None = "all the members of the membership will be **removed**" (MMN ص11) — تحقق إتلاف شامل يتطلب تأكيد المستخدم.

## تحققات التحرير والاسترجاع

### V-ME-15: استرجاع إدخال الوفاة الخاطئ
"If you have **accidentally entered a member as deceased** and want to revoke the same, select the Revoke the Decease Member option" (MMN ص11) — تراجع موثق لحالة حساسة.

### V-ME-16: تصفح فقط بعد Browse
"View the preceding details. This is enabled **only after you click Browse**" (SET ص1) — Previous/Next مشروطان.

### V-ME-17: الحذف الشرطي
"Remove or erase the existing information. This button works **conditionally**" (SET ص1) — بلا توثيق شروط دقيقة (UNK عام للمنصة).

### V-ME-18: فقدان التعديلات غير المحفوظة
"The data entered will be **lost if the changes are not saved**" (SET ص8) — تحذير فقدان صريح.

## تحققات الإدخال والتقارير

### V-ME-19: فلاتر Modify الطلب
شاشة تعديل الطلب تعرض خيارات فلترة المتقدمين (All/Available) قبل الاختيار (MPF ص12).

### V-ME-20: نطاق أعياد الميلاد داخل الشهر
"Enter the date range **within a month**" (RPL ص33 — Birthday List Member).

### V-ME-21: فلاتر العمر التربيعية في Age Report
"Less Than or Equal / Greater than or Equal / Between" **مرتين**: مرة للعمر ومرة لسنوات العضوية (RPL ص16) — تحقق نطاق مزدوج.

### V-ME-22: خيارات القائمة السوداء في التقارير المالية
Closing Balance/Due Report: "include / exclude blacklisted members **or view... only for the blacklisted members**" (RPL ص44/46) — ثلاثية خيارات تتكرر في 5 تقارير.

> **فجوة تحققية موثقة (GAP-ME-P2):** لا يوجد أي تحقق موثق لتجاوز Credit Limit عند Service Bill أو الترحيل الشهري — الحد الائتماني (E-ME-16) يُدخل ولا يُفحص في أي مسار لاحق داخل هذه الأدلة.
