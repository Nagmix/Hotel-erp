# 15 — تحليل تجربة المستخدم (UX Analysis) — وحدة MEM

> تحليل أنماط التفاعل الموثقة في 133 صفحة — وحدة MEM **الأبسط هيكلاً** بين الوحدات التحليلية (مسطحة القوائم، بلا Lookups شجرة MGT) لكنها **الأغنى تفاعلاً بريدياً وتحريراً داخل التقارير**.

---

## 1. أنماط الإدخال

### 1.1 — التبويبات الكبيرة (Tabbed Forms)
- الطلبات: 4-5 تبويبات لكل من (Address/Work/Birth/Other + Spouse + Children)
- Service Rate: 3 تبويبات شرائح + تأكيد لكل واحدة
- More Details: 5-6 نوافذ عرض
- **نمط شاشة-مقسمة-لمسارات-موازية** بدل المعالجات الطويلة (Wizards) — الوحدة **بلا Wizard موثق واحد** (مقارنة بـ HRP Payroll Processing Accept).

### 1.2 — النقر المزدوج كأداة تحرير أولى
- أعمدة الحالة (Blacklist?/Terminate?/Resigned?) — **تبديل Yes/No بالنقر المزدوج** (MMN)
- تحديث البريد بالنقر المزدوج على العنوان (RPL ص33)
- اختيار السجلات من قوائم المساعدة (Double-click to display)
- **ثقافة DBUI-32 كاملة**: كل خلية قابلة للتحويل بلا شاشة تحرير منفصلة.

### 1.3 — أزرار النسخ
"Click on the appropriate **Copy button to copy the address**" (MPF ص4) — نسخ Register→Local→Mailing — تقليل إعادة الإدخال الثلاثي.

## 2. أنماط التغذية الراجعة

| النمط | المثال | التقييم |
|---|---|---|
| التعبئة التلقائية الظاهرة | Category/Name/Rate عند اختيار الرقم | ممتاز — يقلل الأخطاء |
| سعر الصرف التلقائي | "automatically filled" | ممتاز |
| توليد الأرقام الظاهر | Application# بعد Save | جيد |
| تحذير الفقدان | "data will be lost if not saved" | ضعيف (نصي، بعد فوات الأوان) |
| الرسائل المنعية | From Date ≤ اليوم (MTR ص16) | جيد لكن نادر — **الوحدة قليلة رسائل الخطأ الموثقة** (3 فقط مقابل 5 حرفية في Care!) |

## 3. تفاعل التقارير (سمة مميزة)

- **زر Load** قبل كل استعلام (Membership Summary/Settlement Query/Spending Pattern/Late Fee definition) — فصل صريح بين الفلاتر والنتائج.
- **الفرز بالنقر على الرؤوس**: "sort the records in either ascending or descending order by clicking on the headers" (RPL ص34).
- **الحفر** بالنقر المزدوج (Membership Summary 3 مستويات + Spending Pattern → فاتورة).
- **إخفاء الأعمدة** أزرار فورية (Spending Pattern).
- **رسم بياني مدمج** (Pending Complaints count).
- **إجراء داخل التقرير**: Send Email + تحديث البريد — **التقرير كمساحة عمل تفاعلية** وليس مخرجاً نهائياً — أنضج نمط تقارير في المشروع بعد SYS Dashboard.

## 4. نقاط الألم (Pain Points) المستنتجة

1. **عدد الشاشات لمعاملة واحدة**: دورة الانضمام = 5+ شاشات متتابعة يدوياً (طلب → فحص → مقابلة → تاريخ → تحويل) بلا مؤشر حالة موحد على الشاشة الرئيسية (يُرصد فقط عبر Pending Applications).
2. **القائمة السوداء كنص فقط**: العرض المالي للأعضاء السوداويين في 5 تقارير بثلاثية خيارات — لكن **لا شارة على شاشات الفوترة** (استدلال من غياب التوثيق) — خطر فوترة عضو ممنوع.
3. **السمات الثلاث عشرة في قائمة واحدة**: بلا تجميع منطقي (الهوية/الإيصالات/التسوية/FO) وبتفاعل Yes/No بدائي — قابلة للخطأ (ولهذا توصية اعتماد المدير!).
4. **الإدخال المزدوج للتحويل**: Transfer Membership يعرض تبويبات الطلب مرة أخرى "refer Membership Application" — إعادة تحرير بدل الاستيراد الصامت.
5. **الوفاة بشاشة إتلاف**: اختيار None يحذف كل الأعضاء — **بلا تحذير موثق** قبل التنفيذ.
6. **12 ماستر تهيئة متفرقة**: مسار تهيئة خطي طويل بلا قائمة فحص اكتمال (استنتاج من خريطة 02 §1).

## 5. لوحة الأنماط الذهبية القابلة للنقل (إلى Frappe)

| النمط الأصلي | الترجمة المقترحة |
|---|---|
| خيارات القائمة السوداء الثلاثية (include/exclude/only) | فلتر Report قياسي بثلاث حالات |
| Load + Drill + Sort-by-header | Script Report + رابط فرعي click-through |
| تحديث البريد داخل التقرير | inline-edit في Report View |
| أزرار إخفاء الأعمدة | عمود قابل للإخفاء (client-side) |
| Copy buttons للعناوين | زر "Copy from" في نموذج العنوان |
| AuthPerson + Reason داخل الحدث | حقول إلزامية في transition workflow + تعليق |
| Double-click toggle | checkbox مباشر في Child Table |
| الشريحة الثلاثية في سطر الفاتورة | Customer Group على السطر أو Price List selector |

## 6. البصمة اللفظية (Voice)

نبرة الأدلة **إجرائية مباشرة** (Enter/Select/Click) مع درجة توثيق ميتا منخفضة (لا شرح "لماذا") — لكن 3 مواضع استثنائية تشرح المقصد: "used as reference to **wish the members**" (التسويق!) و"It is important that the **System Administrator certifies**" (الحوكمة) و"offers the flexibility to **withhold, withdraw, or overwrite**" (مرونة الترحيل).
