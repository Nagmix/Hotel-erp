# 05 — قواعد العمل (Business Rules) — وحدة MNT

> **BR-MN-01..22** — مشتقة حرفياً من النصوص؛ أثقلها: قيود الخلود للماسترات، بوابتا الطباعة ENG، وأزواج الجدولة Rhythm/Lag/Must-Complete-By، والصنف المفتوح 999999999999.

---

## أ) قواعد الترقيم والهوية

### BR-MN-01: رقم الشكوى آلي
- "The complaint number is **auto generated**" (OPR ص3) — لا إدخال يدوي للرقم.
- **الأثر:** الشكوى كيان نظامي لا يدوي — المرجع الخارجي يُدار بحقل Ref. No المنفصل (10 محارف).

### BR-MN-02: رقم PM Schedule آلي مشروط بالاكتمال
- "The PM Schedule # is **auto generated once all the mandatory fields are completed**" (OPR ص22) — الترقيم يتأخر حتى اكتمال الإلزامي (نمط "حفظ نظيف").

### BR-MN-03: Employee # رقمي صرف
- "maximum of **7 numeric characters**" (SET ص14) — الوحيد في الوحدة بقيود رقمية خالصة.

### BR-MN-04: هوية المعدة 8 محارف
- Equipment Code "maximum of 8 alphanumeric characters" + F1 للموجود (OPR ص18).

## ب) قواعد الخلود والسلبية (Immutability + Passive)

### BR-MN-05: ماسترات لا تُحذف — تُخمَت
- الحرفية المتكررة: "Once a ... Code is defined, **it cannot be deleted**. The Status of ... code that is not in use can be **made to Passive**" — تنطبق على: Locations (SET ص4) · Equipment Category (ص6) · Cost Category (ص7) · Shifts (ص9) — **وما بالبقية يُستنتج بالقياس النمطي** (راجع 13).
- Modify متاح دائماً للتفاصيل غير الكودية.

## ج) قواعد الجدولة الوقائية ⭐

### BR-MN-06: التواريخ تُولَّد من الإيقاع
- "The dates are **automatically calculated based on the frequency of service**" (OPR ص21) — الإيقاع (أيام بين خدميتين) هو محرك انتشار التواريخ.

### BR-MN-07: نافذة الإنجاز مقيّدة بالسماحية
- "'Must Complete By'... (**Expected completion date should be less than or equal to the Lag days**)" (OPR ص22) — Lag = حد التأخير المسموح؛ لا يُقبل توقع يتجاوزه.

### BR-MN-08: AMC يسري آلياً إلى الجدولة
- "The **AMC Y/N information will auto populate**" في PM Schedule Master (OPR ص21) من المعدة — مزوّد العقد حاضر بلا إدخال.

## د) قواعد الإسناد المشرفي ⭐

### BR-MN-09: تعريف المشرف
- "used by a **Supervisory User in the Maintenance Department**" (OPR ص22) — توليد Job Orders وظيفة إشرافية (صلاحية ضمنية بلا User Rights موثقة — 07).

### BR-MN-10: الانتقاء NO→YES شرط التوليد
- "Double-click under the **Select column to change the NO option to YES**. **All records tagged as YES indicates that a Job Order has to be generated**" (OPR ص23-24).

### BR-MN-11: اللون يتبع الأولوية فوراً
- "When you assign the priority, **the record will be highlighted in the color that was set for the priority level**" (OPR ص24) — عرض حالي حي، لا لاحق في التقارير.

### BR-MN-12: الإسناد ثنائي الوجهة
- "assign the Priority to the **Employee or the Service Provider (Vendor)**... The respective details of the employee/ service provider appear on the screen" (OPR ص25) — داخلي/خارجي في نفس الجهاز.

## هـ) قواعد الطباعة

### BR-MN-13: بوابة Job Request (ENG#1)
- "The user can **print a job request**, if the **ENG Module Attribute #1 is 'YES'**" (OPR ص4).

### BR-MN-14: بوابة Job Order (ENG#2)
- "You can **print a job Order**, if the **ENG Module Attribute #2 is 'YES'**" (OPR ص26).

### BR-MN-15: صيغة الطباعة من مواصفات المستخدم
- "The print format is **based on the user specifications**" (RPL ص25) — مرجع UDPF — لا قالب نظامي مفروض.

## و) قواعد التنفيذ والتكلفة

### BR-MN-16: مسارات Action Taken الثلاثة
- "Select one of the three options: **By Job Order #, by Complaint # or by PM Schedule #**" (OPR ص6) — نفس شاشات ما بعد التوجيه للثلاثة ("Follow steps 5 to 15").

### BR-MN-17: القيمة تُحسب آلياً من الكمية
- "Enter the **quantity** of the item, **the value will be auto calculated**" (OPR ص13) — سعر الصنف يُجلب (من Inventory) والناتج يُحسب بلا إدخال يدوي.

### BR-MN-18: الصنف المفتوح بشرِكة 999999999999
- "To enter an open item you have to enter **999999999999** in item code field... item name has to be entered manually. **This information will not affect Inventory stores**" (OPR ص13).

### BR-MN-19: الأصناف من المخازن الهندسية المعينة فقط
- العرض عبر F1 "will be picked up from **Inventory stores**" — والسياق: المخازن المعينة في Identify Engg Stores (SET ص17) + الـSpares/Repair Details.

## ز) قواعد الورديات والقراءات

### BR-MN-20: نافذة تعيين الورديات
- "(The date should be a **future date** and the date range should be **within 31 days**)" (OPR ص16) — تخطيط قصير المدى فقط.

### BR-MN-21: الورديات لموظفي الوحدة فقط
- "Shift assignments can be made **only to those employees defined in the Define Employees option in this module**" (OPR ص15) — عزلة المسبار المحلي.

### BR-MN-22: القراءات حصرية بالمعرَّف
- "The readings which are **specified in the Equipment Master** for that particular equipment **only can be entered here**" (OPR ص26) + قراءة Equipment Details List تُبنى "based on the location of the equipment".

---

## جدول التتبع (قاعدة ← مصدر ← أثر)

| القاعدة | المصدر | الأثر عند الإخلال |
|---|---|---|
| BR-01/02 | OPR ص3/ص22 | تسلسل مرجعي مكسور |
| BR-05 | SET ص4/6/7/9 | حذف كيان مستهلك في شكاوى/معدات |
| BR-07 | OPR ص22 | جدولة تتجاوز السماحية — يُرفض |
| BR-10/11/12 | OPR ص23-25 | توليد بلا انتقاء/بلا أولوية/بلا إسناد |
| BR-13/14 | OPR ص4/ص26 | طباعة غير مضمّنة |
| BR-17/18 | OPR ص13 | تضخم مخزني/بلا أثر مخزني (منطقي) |
| BR-20/21 | OPR ص15-16 | رجعية/موظف خارج الماستر — مرفوض |
| BR-22 | OPR ص26 | قراءة دخيلة على الماستر — مرفوضة |
