# 17 — تحليل الفجوات (Gap Analysis) — وحدة TEL

> **GAP-TE-D01..D07 (توثيق) + GAP-TE-P01..P05 (عملية/وظيفة)** — من بينها **وظيفة SMS مقدَّمة-بلا-جسم** (ثانية في المشروع بعد Membership Tax Posting!) وتناقض Others (نسبة/مبلغ) وازدواج مصطلح Transfer/Extension.

---

## أ) فجوات التوثيق (Documentation Gaps)

### GAP-TE-D01: SMS المعيارية — وظيفة مقدَّمة بلا جسم ⭐
- الموقع: مقدمة CAC (ص2): "used by Users to... setup extension passwords and **record and save standard SMSs to be sent to the guests on various occasions like checkins, anniversaries etc.**"
- الدليل: **TOC CAC = 4 وظائف فقط** (Activate/Deactivate · Error · Transfer · Password) — لا قسم SMS في أي ملف من الأربعة
- الحالة: ثاني "مقدمة-بلا-جسم" في المشروع (بعد MEM Membership Tax Posting = فهرس-بلا-جسم) — **UNK-054**
- المعالجة: البحث في إصدارات أحدث؛ وإلا تُستكمل كقالب رسائل تلقائية عند CI (نمط متسق مع 2-Way)

### GAP-TE-D02: لا خريطة GL للإيراد الهاتفي
- Revenue Codes لكل نوع + Government Tax Structure دون أي حساب مدين/دائن مسمى
- P&T (تكلفة المزوّد) بلا أي مسار قيد/فاتورة موثق داخل الوحدة
- (عائلة الفجوة العامة — المرحلة 8 GL Mapping)

### GAP-TE-D03: صلاحيات غير موثقة (رابعة)
- لا قسم User Rights في أي ملف (بعد CARE/SLM/MEM) — والاستثناءات مواضع استنتاجية
- الأخطر: **إعادة الترحيل فعل مالي بلا ضابط موثق** (أي مستخدم لشاشة Error يرحّل للفوليو) + لا قيد على تعديل/حذف الشراكات الحساسة (LCA/9999999999)

### GAP-TE-D04: تناقض حقل Others — نسبة أم مبلغ؟
- SET ص5: الحقل ضمن Calculation % (نسبة، طول 3، منطق 100/150/200%) لكن النص: "If the Hotel decides to charge a certain **minimum amount**... **specify the amount in this field**"
- نسبة لا تستطيع تمثيل "حد أدنى للمكالمات المجانية نوعياً" (مثال: 60c كحد أدنى لا يُكتب كنسبة)
- المعالجة: D-TE — حقلان منفصلان (others_pct + others_min_amount) أو توثيق الأصل

### GAP-TE-D05: مسار SPL غير معرّف
- List All Calls يعرض نوع **SPL** ("calls to Special numbers like Toll Free") — لا ماستر تعريف SPL ولا ذكر له في Call Identifier (Local/STD/IDD/others) ولا في Calculation%
- مصير SPL في التسعير: يُستنتق Others؟ غير موثق — **مرشّح UNK-057**

### GAP-TE-D06: قدرات 2-Way بلا وظائف
- "activate / de-activate the phones, **voice mails, wake-up calls and room status**" — لا شاشة/قائمة لأي منها في الوحدة:
  - Wake-up Calls: وظيفة مشهورة فندقياً — غائبة كلياً
  - Voice Mail: إدارة بلا واجهة
  - Room Status من الهاتف: قناة housekeeping ذائعة الصيت في العصر — لا أثر
- المعالجة: تُوثق كنطاق عتاد للتكامل فقط

### GAP-TE-D07: لا مفاتيح INI (الثالثة)
- CARE/MEM/SLM/TEL — أربع وحدات بلا INI؛ TEL تحديداً تملك **إحالة Module Attributes وحيدة** (عرض المدة) — النمط: إعدادات الوحدات الحديثة تتوزع بين property.ini وModule Attributes وSingleton داخلي
- (يعمّق سؤال GAP-SYS-D01: مركزية التهيئة)

## ب) فجوات العملية (Process/Functional Gaps)

### GAP-TE-P01: السباق بلا معالجة آلية (pending-folio)
- Room vacant error موثقة بأصلها (group check-in) لكن الحل يدوي بحت: انتظار تصحيح FO ثم Repost يدوي — **لا طابور auto-retry** عند تسجيل الوصول لاحقاً
- الخطر: نسيان السجلات = إيراد ضائع صامت (Unbilled List هو الكاشف الوحيد!)

### GAP-TE-P02: Address Book ملكية غير معلنة
- "create **your own** Yellow Pages" — هل خاص بالمستخدم أم مشترك؟ من يرى دفتر من؟ لا User-ownership موثقة
- المعالجة: Owner field + مشاركة اختيارية

### GAP-TE-P03: لا أرشفة/احتفاظ لسجلات المكالمات
- أعلى جدول تراكمي في الفندق (300-1000/يوم) بلا سياسة Retention/أرشفة/ضغط موثقة

### GAP-TE-P04: لا تداخل زمني مُدار للشرائح
- From/To Time لكل سجل بلا فحص تداخل مع سجل آخر بنفس الكود — سيناريو التصادم غير المعالج (13-exceptions §و)

### GAP-TE-P05: كلمة المرور بلا إدارة دورة
- إنشاء عند التسجيل + انتهاء بالمغادرة — **لا تغيير ولا استعادة ولا إبطال فوري** (نزيل شكا من تسريب؟ إجراء غير موجود)
- ولا توليد تلقائي موثق (من يختار الرقم؟ الموظف — عنصر بشري في مفتاح الاتصال!)

## ج) مصفوفة الأولويات

| الفجوة | الخطورة | المرحلة المقترحة |
|---|---|---|
| D01 SMS الشبح | متوسطة | بحث → قرار (نمط Notification) |
| D02 GL | عالية (مشتركة) | المرحلة 8 |
| D03 الصلاحيات | **عالية** | فورية عند إعادة البناء (P-TE-1) |
| D04 Others | متوسطة | قرار D-TE فوري |
| D05 SPL | متوسطة | UNK-057 ثم قرار |
| D06 قدرات 2-Way | منخفضة (توثيق) | نطاق تكامل |
| D07 INI | منخفضة | مشتركة |
| P01 السباق | **عالية** | طابور retry في F-TE-8 |
| P02 الملكية | منخفضة | Owner field |
| P03 Retention | متوسطة | سياسة زمنية |
| P04 التداخل | متوسطة | validate زمني |
| P05 كلمة المرور | متوسطة | إدارة أدوار |

## د) مقارنة عابرة (فجوات الوحدات الحديثة)

| الوحدة | بلا INI | بلا صلاحيات | شبح وظيفي | خلود سجلات |
|---|---|---|---|---|
| CARE | ✓ | (نمط SYS) | — | (الرسائل) |
| MEM | ✓ | — | ✓ (Tax Posting) | Rate Master |
| SLM | ✓ | ✓ | — | — |
| **TEL** | ✓ | ✓ | **✓ (SMS)** | **Slabs** |
- **نمط واضح:** الوحدات اللاحقة (الجيل الأحدث من Fortune 6i) أخف توثيقاً للصلاحيات/INI وأكثر اعتماداً على أدوار/سمات داخلية — عكس نواة FO/POS/FAS الغنية بمفاتيح INI وUser Rights.
