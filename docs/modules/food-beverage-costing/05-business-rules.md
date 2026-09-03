# 05 — قواعد العمل (Business Rules) — وحدة FNB

> **BR-FB-01..25** — أثقل عائلة قواعد "قراءة" في المشروع (المحاسبة هنا قرارات تحليلية لا قيود)، وأبرزها: بوابة التفعيل الأحادية · انتشار الجلسة سنة مالية كاملة · علاقة POS↔Recipe باتجاه واحد · **الحاجب اللحظي على KOT** · خلود Auto Indent · XOR منهجي التكلفة.

---

## أ) قواعد التفعيل والربط

### BR-FB-01: بوابة أحادية الاتجاه ⭐
"Once the Start Date is entered, **updating the same will not be allowed**" (SET ص3) — أقوى قفل تعديل في المشروع: ليس Passive-state ولا modify-locked بل **قفل كتابة كامل على حقل واحد إلى الأبد**.

### BR-FB-02: شرط جاهزية الوحدتين
"only when **both the Point of Sale and Materials Management modules are fully operational**, the Costing Start Date should be specified" (SET ص3) — توصية موثقة بوصفها شرط صحة المخرجات (وإلا MIS ناقص).

### BR-FB-03: تكديس مراكز التكلفة على المطبخ
"**Multiple Cost Centers can be linked to a single kitchen**" (SET ص3) — علاقة N:1 صريحة؛ عكسها غير موثق.

### BR-FB-04: Sales Tag يميّز الإيرادية
"A provision for **Sales Tag** is provided for identification of **Revenue and Non Revenue Outlets** in the Cost Reports" (SET ص3) — ثنائية تصنيف المنافذ في كل تقارير التكلفة.

### BR-FB-05: المطابخ محور الانعكاس
"**All sales / cost values in the Cost Reports will be reflected based on Kitchens**" (SET ص4) — وحدة القياس التقريري = المطبخ (ليس المطعم ولا مركز التكلفة!).

### BR-FB-06: To Cost يرصد From Cost
"Select the From Cost. **The To Cost will reflect the same option** selected under From Cost" (COP ص14) — سلوك انعكاس حقل في التحويلات البينية (منع عدم التطابق؟ أم قيد إدخال؟).

## ب) قواعد الميزانيات

### BR-FB-07: انتشار الجلسة على السنة المالية ⭐
"Once budget of a particular month / year is defined for any specific or All sessions, **the same holds good for the rest of the months in the Financial year**... uniformity... if the option for **March 2007** is selected as 'All' then the option by default remains the same for **any other month in the year 2007**" (SET ص8) — انتشار إعدادي قسري عبر سنة كاملة (بلا نمط مقابل في المشروع).

### BR-FB-08: تسلسل البيع ثم الPAX
"For entering **both**, you have to define **Sales Budget figures first, followed by the Covers Budget**" (SET ص8-9) — ترتيب إلزامي موثق.

### BR-FB-09: التوزيع المتساوي + عداد الانحراف
"If Per Month option is selected, the Amount or Covers specified will get **equally distributed**" + "If some changes are made to the figures distributed, the **Difference is reflected**" (SET ص9) — عداد مراقبة يدوي حي.

### BR-FB-10: إشارة التباين معكوسة الحدس المحاسبي
"If the **Actual Cost Percentage... is greater than the Budgeted Percentage**, then the Variance will reflect as **minus** and if... **lesser**... as **plus**" (SET ص6) — التباين من منظور الربحية (تجاوز التكلفة = سالب) — موثق حرفياً لمنع الالتباس عند إعادة البناء.

### BR-FB-11: نسبة التكلفة تنطبق على كل أيام الشهر
"The Percentage entered in this option is **applicable to all the days of the month**" (SET ص8) — شبكة قابلة للتعديل لكن قيمة أولية شمولية.

## ج) قواعد الوصفات

### BR-FB-12: POS Item → وصفة واحدة فقط
"POS Item can tag for **only one Recipe**" (SET ص12) — 1:1 من طرف الصنف.

### BR-FB-13: وصفة → مطاعم وأصناف POS متعددة
"One Recipe can tag to **Multiple Res Codes and for multiple POS Items**" (SET ص12) — 1:N من طرف الوصفة (مع BR-FB-12: علاقة N:1 كلية).

### BR-FB-14: تحذير التسعير الخاسر (غير حاجب)
"If the selected POS item **Rate is Less than Recipe COST**, then it will display warning message saying **'Warning!! Item Price is less than the Cost price'**" (SET ص12) — إنذار فقط؛ البيع بسعر أقل مسموح.

### BR-FB-15: معادلة COST %
"**COST % = Cost per Portion / PRICE × 100**" (SET ص12) — المعادلة المسطرة الوحيدة في الوحدة.

### BR-FB-16: إلزامية الوصفات شرطية بالمنهج
"Defining of Recipe Items is **mandatory only if the Recipe based method of Costing is followed**" (SET ص10) — المنهج يحدد إلزامية الماستر.

### BR-FB-17: نصف المصنّع مشترك متغير الكمية
"One sub recipe can be used / linked to **multiple recipes** and the **quantity of use varies** based on the recipe requirement" (SET ص12).

## د) قواعد الاستخراج والتدفق

### BR-FB-18: ثنائية Batch/Online ⭐
INI#368=1 → "**Online transfer of Issues** from inventory to costing... **no need to do manual extraction** for inventory issued items" (COP ص3) — استراتيجية ETL قابلة للتبديل.

### BR-FB-19: الحاجب اللحظي على KOT ⭐⭐ (الأخطر عبْرياً)
"SWITCH 511, autodeductionliqsale; if this switch is set to **0**, in real time during **Current stock balance will be checked KOT punch. Items cannot be sold, if the quantity is greater than the current stock**" (COP ص3) — قاعدة **موزعة التنفيذ**: تُقرر في FNB وتُنفَّذ في POS لحظة البيع. (اسم المفتاح يوحي بالخمر والنص عام — UNK-063).

## هـ) قواعد المخزون والجرد

### BR-FB-20: دلالتا Stock Type
"**Adjustment**: Enter the amount of stock **the user has consumed**. **Physical Stock**: Enter the amount of **physical stock available**" (COP ص5) — عالمان للجرد اليومي.

### BR-FB-21: الافتتاحي — Pink مستخرج/Green قابل للإدخال
"Records highlighted in **pink are Extracted records and green are zero balance records**. Double-click on the Zero Balance (Green) records to enter the Quantity" + "It will allow to enter the rate of the items **which do not have rates**" (COP ص8) — بنية دمج MGT-مع-يدوي.

### BR-FB-22: الكمية بالوحدتين
"It will allow to enter quantity in **both the UOM's i.e. Stock and Conversion UOM**" (COP ص13) — ثنائية UOM حاضرة في الاستهلاك (وأصل التعريف ص8).

### BR-FB-23: دورة الترحيل اليومي/السنوي
"This option will arrive at **variances between computer stock and physical stock** so that physical stock recorded would become **the opening balance for the next day**... used to transfer from **One financial Year to next financial year**" (COP ص16) — أداة واحدة ببعدين زمنيين (يومي وسنوي!).

## و) قواعد الطلب والاستعلام

### BR-FB-24: خلود Auto Indent
"Once the indent is generated, **it will not be allowed to modify or delete**" (COP ص19) — الوثيقة الوليدة مكتملة الحصانة فوراً (أقوى من modify-locked: قفل كامل منذ اللحظة صفر).

### BR-FB-25: XOR منهج التكلفة في الربحية ⭐
"if you select the option **Issue Based then you cannot select the Restaurant** option. If you select the option **Recipe Based then you cannot select the option Kitchen**" (LUK ص14) — المنهج الاستهلاكي يُقرأ بلا مطاعم والوصفي بلا مطابخ — قيد معايير دلالي فريد.

### BR-FB-26: نهاية التنقيب المعلنة
"If there are not further details, you get the message **'No Drill Down Available for this Category'**" (LUK ص15) — رسالة حدود الاستعلام (نهاية شجرة التنقيب معلنة للمستخدم — نادرة اللطف!).
