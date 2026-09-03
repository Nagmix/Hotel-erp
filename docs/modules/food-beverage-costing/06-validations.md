# 06 — قيود الإدخال والتحقق (Validations) — وحدة FNB

> **V-FB-01..15** — قيود قليلة نسبياً مقارنة بحجم الوحدة (أغلب الصرامة في التقارير معايير فرض اختيار لا تحقق منطقي)، لكنها تحتوي **أغرب قيد كتابة في المشروع** (حقل يُقفل للأبد) و**أصعب قيد تشغيلي** (منع بيع لحظي في POS بقرار من FNB).

---

## أ) قيود التفعيل والتواريخ

### V-FB-01: عدم قابلية تحرير تاريخ البدء
"You will not be able to **edit the date** appearing in this field **once it is created**" (SET ص3) — تحقق من نوع "الحالة النهائية للحقل" (تحرير ممنوع مطلقاً).

### V-FB-02: Audit Date كحاجز معاملات
"the user can enter the date **beyond which the transactions are not allowed**" (SET ص3) — سقف زمني للكتابة.

### V-FB-03: تاريخ الاستهلاك الافتراضي قابل للتغيير
"The current date is displayed automatically when you click Add. **Change the date as required**" (COP ص12) — افتراض اليوم بلا قفل (مقابل قيود السجلات المحاسبية في FO/AR!) — الوحدة التحليلية متساهلة زمنياً.

## ب) قيود الأكواد والمراجع

### V-FB-04: Recipe Code — 6 رقمي إلزامي
"It can be **six numeric characters** long. This is a **mandatory field**" (SET ص10) — أضيق كود في الوحدة.

### V-FB-05: Reference # — 10 أبجدي-رقمي بحد أدنى 3
"You can enter maximum of **10 alphanumeric characters and minimum of 3**" (Kitchen Stock — COP ص5؛ يُفترض نفس العائلة في الافتتاحي/التحويلات بلا أطوال موثقة هناك).

### V-FB-06: UOM مقفل من الماستر
"The Unit Of Measurement is **fixed. You will not be able to edit this field**. This data is defined in the Master Entry in **Material Management**" (COP ص12) — قفل كتابة باسم وحدة أخرى (نمط الاستعارة الصارم).

## ج) قيود المخزون والكميات

### V-FB-07: منع البيع فوق الرصيد (SWITCH 511=0) ⭐
"Items **cannot be sold**, if the **quantity is greater than the current stock**" عند KOT punch (COP ص3) — تحقق لحظي قابل للتفعيل على POS — **القيد الوحيد في المشروع الذي يمنع واقعة بيع في وحدة أخرى**.

### V-FB-08: إدخال الكمية على الصفوف الخضراء فقط
"Double-click on the **Zero Balance (Green) records** to enter the Quantity" (COP ص8) — قناة إدخال مقيدة بلون الحالة.

### V-FB-09: السعر يدوي فقط عند غيابه
"It will allow to enter the rate of the items **which do not have rates**" (COP ص8) — rate auto-populate إلا الناقص.

## د) قيود المعايير والتقارير

### V-FB-10: XOR الربحية
Issue Based → **لا Restaurant** · Recipe Based → **لا Kitchen** (LUK ص14) — قيد فرض اختيار على مستوى واجهة المعايير.

### V-FB-11: تفاصيل الوصفة تحتاج وصفة
"If the recipe is **not defined, then you cannot view the details**" (LUK ص5) — منع عرض بلا مصدر.

### V-FB-12: نطاقات From/To إلزامية الاستخدام
"Enter the **range** of the Group Code or the Item Code" (SET ص5) + "Enter the item range in the FROM item and TO item fields" (LUK ص3) + "Item Range or Group Range... enter the respective ranges" (REP ص22) — نمط نطاقات موحد في كل المعايير.

### V-FB-13: NC Query يحتاج NC Type
"Select the **NC Type** (They can be Complimentary, Spoilage or for House Consumption etc.)" (LUK ص6) — قائمة مفتوحة بـ"etc." (UNK-066).

## هـ) قيود دورة الحياة

### V-FB-14: Auto Indent — لا تعديل ولا حذف
"Once the indent is generated, **it will not be allowed to modify or delete**" (COP ص19) — حصانة مزدوجة منذ الولادة.

### V-FB-15: تعديل الجرد بـDoc# والحذف بتأكيد
"To modify any records, click Modify... **Select the Doc #** of the record you want to modify" + "If you want to Delete any record... press **F5**... confirmation message, click **Yes**" (COP ص6) — تعديل موجّه بالرقم + حذف بتأكيد صريح.

---

## ملاحظة تحليلية

- **غياب تحقق التاريخ في الجرد/المبيعات اليدوية** مقارنة بقيود "نفس الشهر"/"≤ اليوم الحالي" في TEL/POS — الوحدة تفترض الثقة التشغيلية أو تقبل التأخير التحليلي (الجرد retrospective بطبيعته).
- **لا رسالة خطأ واحدة موثقة رفضاً** في 76 صفحة — أقرب للأعلى (المشترك مع MNT: فقر رسائل)، بينما التحذيران الوحيدان: "Warning!! Item Price is less than the Cost price" (SET ص12) و"No Drill Down Available" (LUK ص15).
- أغلب "التحقق" هنا **قيد فرض على واجهة المعايير** (XOR/نطاقات/أنماط) — عقلية "مولد تقارير" لا "نموذج معاملات".
