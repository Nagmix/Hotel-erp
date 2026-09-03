# 13 — الاستثناءات والحالات الخاصة (Exceptions) — وحدة SLM

> **الحالات الشاذة والسلوكيات الموثقة خارج المسار السعيد** — E-SM-01..18. الوحدة غنية بالاستثناءات "السلبية" (أشياء لا يمكن عملها) أكثر من الإيجابية — نمط CRM الواقي لبياناته.

---

## 1. استثناءات المستودعين (Prospect/Company)

| ID | الاستثناء | النص/الدلالة | المصدر |
|---|---|---|---|
| E-SM-01 | **Prospect خارج الموازنات** | "potential companies are **not included** in this budget" — القيد الأصرح: التخطيط للـCGR فقط | SLT §3 |
| E-SM-02 | **تحويل أحادي الاتجاه** | لا وظيفة معكوسة (شركة → prospect) موثقة — التخرج نهائي | SLT §10 |
| E-SM-03 | **اسم Prospect من مستودع الشركات!** | Prospect Entry: "Enter the name of the company **or press F1 to get the list of all the company names**" — الاسم يبدأ من Company Master رغم أن Prospect مستودع منفصل! (غرابة نمذجة أصلية — يُحتمل أن F1 للتحقق من عدم التكرار) | SLT §4 |
| E-SM-04 | **كود مولد قابل للتحرير** | "Enter the **New Company Code** and click" — النظام يقترح (TTT+حرف+مسلسل) والمستخدم قد يعدّله — خطر تصادم يدوي (V-SM-3 يعالجه إلزامياً بإعادة البناء) | SLT §10 |
| E-SM-05 | **General Information للقراءة فقط** | "You **cannot modify any fields**" — تعديل بيانات الأداة يتم من Prospect Entry نفسه | SLT ص10 |

## 2. استثناءات الحماية (Planner/Blacklist)

| ID | الاستثناء | النص | المصدر |
|---|---|---|---|
| E-SM-06 | **شاشة دخول مستقلة داخل التطبيق** | Executive Planner: "Enter the user id and password" — sub-session كاملة بـlogout صريح "logs out the user that is logged into the Executive Planner" | SLT §9 |
| E-SM-07 | **المخطط حكر على المربوطين** | "executed **only by sales executives who have been mapped** to a user id" — غير المربوط خارج التغطية كلياً (حتى لو موظف مبيعات!) | SLT §9 |
| E-SM-08 | **Blacklist view في Modify فقط** | "This option is available **only in Modify mode**" — شاشة التفاصيل السادسة تظهر بعد الحفظ لا قبله | PRF ص15 |
| E-SM-09 | **Company Profile معدل من نافذتين** | Sales Manager Tool: أزرار Add/Edit Company "For more information, refer Company Profile **under Accounts Receivables Setup**" — النص يحيل الوظيفة لوصف **AR** رغم أن الشاشة موثقة في PRF! (تضارب ملكية توثيقي — انظر 17 §تناقضات) | SLT ص10 |

## 3. استثناءات التواريخ والبيانات التاريخية

| ID | الاستثناء | النص | المصدر |
|---|---|---|---|
| E-SM-10 | **إدخال ما قبل التشغيل** | Daily Occupancy: "backdated... **before IDS PMS went live**" — نافذة إدخال تاريخياً مغلقة بطبيعتها بعد الترحيل الزمني | SLT §1 |
| E-SM-11 | **تخصيص وكيل يبدأ من تاريخ المحاسبة** | "By default, the Accounting date **will be picked** as From Date and can be edited" — غير قابل لأن يكون تاريخاً ماضياً افتراضياً | PRF §12 |
| E-SM-12 | **From date التحرر مولد آلياً** | "'From date' is **auto generated based on the start date**" — المستخدم لا يملك حرية تقسيم المدد من الصفر | PRF §14 |

## 4. استثناءات التقارير (قيود صارمة)

| ID | الاستثناء | الدلالة | المصدر |
|---|---|---|---|
| E-SM-13 | **Market Share: شهر واحد حصراً** | "month and year... To Date should be **equal** to... From Date" — لا مقارنة ربعية/سنوية ممكنة | REP §2 |
| E-SM-14 | **Sales Performance: 31 يوماً** | نافذة شهرية قصوى لتقرير الأداء (بينما نظيره Budget بلا قيد) | REP §19 |
| E-SM-15 | **Contribution Datewise: نفس الشهر** | تقرير يومي-داخل-شهر لا عابر للشهور | REP §15 |
| E-SM-16 | **تقريران بنفس التعريف** | Sales Performance (Budget) وSales Performance Report — مقدمة حرفية متطابقة تقريباً (REP ص8-9 vs ص21-22) | REP §7/§19 |

## 5. استثناءات البيئة والصيغ

| ID | الاستثناء | النص | المصدر |
|---|---|---|---|
| E-SM-17 | **BMP فقط للصور** | "You can upload **only bmp files**" — قيد صيغة صريح | PRF §17 |
| E-SM-18 | **ddmmyy صيغة الخصم** | تنسيق تاريخ غير قياسي موثق صراحة | PRF §5 |
| E-SM-19 | **"BELOW SCREENSHOTS ARE REQUIRED"** | نص خام من مسودة الدليل بقي في LUK ص9 — أثر توثيقي أصلي (قابل للإسقاط في إعادة البناء) | LUK §6 |
| E-SM-20 | **Pager # حقل حي** | HODs في Hotel Profile: "Residence #, Mobile #, **Pager #**" — أثر عصر تقني (1990s-2000s) | PRF §34 |

## 6. الاستثناءات البنيوية الكبرى (خلاصة)

1. **غياب التراجع كلياً** (E-02/E-04 + 10 §6): لا عكس تحويل، لا إلغاء تخصيص/توقع، لا استرجاع موازنة — الوحدة **أحادية الاتجاه** في كل معاملاتها تقريباً.
2. **تضارب ملكية Company Profile** (E-09): SLM-PRF يوثق الشاشة كاملة، وSLM-SLT يحيلها لـ"Accounts Receivables Setup" — تشهد أن الأصل التاريخي للشاشة كان AR ثم استضافته SLM (أو العكس) — قرار إعادة البناء: ملكية واحدة (Customer) وواجهتان.
3. **التقسيم الزمني الغريب للتقارير** (E-13/14/15): قيود شهر/سنة/31 يوم تعكس حدود استعلامات محرك قديم (يُفك القيد في إعادة البناء بلا خسارة وظيفية — R-SM-5).
