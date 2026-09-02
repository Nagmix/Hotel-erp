# 13 — الحالات الحدية والاستثناءات (Exceptions) — وحدة System Setup

> E-SYS-01..24 — حالات حواف التشغيل الموثقة أو المستنتجة بأدلة.

---

| ID | الحالة | السلوك/المخاطرة | المصدر/النوع |
|---|---|---|---|
| E-SYS-01 | مستخدم Supervisor غادر الفندق | **لا أحد غير Supervisor يصل لكل القوائم** — مخطط استرداد غير موثق (من يعيد تعيين supervisor آخر؟) | [NOT DOCUMENTED] — استنتاج من بنية التفويض |
| E-SYS-02 | نسيان كلمة المرور + المشرف غير متاح | لا مسار استرداد ذاتي — دائرة مقفلة | [NOT DOCUMENTED] |
| E-SYS-03 | انتهاء صلاحية كلمة المرور أثناء التشغيل | السلوك (حظر؟ إلزام تغيير؟) غير موثق | **UNK-023** |
| E-SYS-04 | محاولة تعديل كيان مقيد (مثل Department Name) | **الرفض بالتصميم** — "modify the status only" — إنشاء كود جديد + Passive للقديم هو المسار الوحيد | Notes Ch3 |
| E-SYS-05 | حذف مرجع مستهلك (Department مستعمل في POS outlet) | غير موثق — الحذف أصلاً "conditional"؛ والأصل نمط تعطيل | [NOT DOCUMENTED] |
| E-SYS-06 | 5 أسعار صرف لعملة واحدة | رفض/استبدال؟ — القيد 4 موثق بلا سلوك تجاوز | ص70 + [UNCERTAIN] |
| E-SYS-07 | إدخال تاريخ Applicable ماضٍ | "must enter a date greater than the current date" — الرفض موثق بالوصف (سلوك الإدخال) | كل Ch3 |
| E-SYS-08 | تعطيل (Passive) عملة عليها فواتير AR مفتوحة | الفواتير الموجودة تحتفظ بسعرها المثبت — لكن التسويات الجديدة؟ | [UNCERTAIN] — من تقاطع ACR |
| E-SYS-09 | تعديل Division Method لعملة نشطة | **مسموح!** (الاستثناء الثالث) — تغيّر نتيجة كل تحويل لاحق: 5000 USD من 245,000 إلى 102 بالمثال الحرفي — **مخاطرة محاسبية** | ص69 |
| E-SYS-10 | ضريبة On Tax تشير لبندها نفسه (Tax# = نفسه) | التسلسل الذاتي — لا تحقق موثق ضد المرجع الدائري | [NOT DOCUMENTED] |
| E-SYS-11 | Slab بأول Amount From ≠ 0 أو فجوة بين الشرائح | "starts with zero followed by..." آلي — لكن القيمة اليدوية الثانية قابلة للتداخل؟ | [UNCERTAIN] |
| E-SYS-12 | تعديل Guest Comment 1-25 | **ممنوع نظامياً** — استطلاعات الضيوف التاريخية محمية | ص84-85 |
| E-SYS-13 | Round Amount = 0 أو قيمة شاذة | يُقبل رقمياً — التقريب قد يصبح لا-أثر أو مدمراً | [NOT DOCUMENTED] |
| E-SYS-14 | Nearer عند كسر يساوي المقدار بالضبط (0.50/0.50) | **يرفع للأعلى** (مثال الدليل: 1000.50/0.50→1001.00) — قاعدة Tie-break موثقة ضمنياً بالأمثلة | ص45 |
| E-SYS-15 | Program ID > 7 خانات أو منفذ طابعة خطأ | رفض طولي فقط — الطابعة المعنية قد تكون غير موصولة | [NOT DOCUMENTED] |
| E-SYS-16 | Print Bill Message بـ To Date ماضٍ | الرسالة تفنى — من يُنظف السجلات؟ | [NOT DOCUMENTED] |
| E-SYS-17 | Excel/Open Calc غير مثبتين والمستخدم مقيَّد بهما | التقرير يفشل عند الإخراج — التحقق خارج النظام | ص19 |
| E-SYS-18 | INI محرر بملف نصي خارجي بشكل خاطئ | "there could be **functionality issues** with the Fortune PMS product" — **فساد سلوكي بلا شبكة أمان** | ص37 |
| E-SYS-19 | Extract DB Tables: Delete | "permanently deletes all tables that have been extracted" — حذف نهائي بدون تأكيد مزدوج موثق | ص36 |
| E-SYS-20 | GUI<customer code>.dat اسمه خاطئ | "The filename created in the application folder must contain the customer code" — وإلا فشل الاستخراج | ص34-35 |
| E-SYS-21 | تخصيص Dashboard ثم ترقية النظام | Menu Programs المرتبطة بعناصر أُزيلت؟ | [NOT DOCUMENTED] |
| E-SYS-22 | تعطيل Group مستخدمها نشط | سلوك تفعيل عضوية المجموعة على الصلاحيات غير موثق | [NOT DOCUMENTED] |
| E-SYS-23 | Reason Codes تحتاج "Gift Shop" وقد لا تملك منافذ | بند قائمة بلا وظيفة — هدر UI | ص61 [UNCERTAIN] |
| E-SYS-24 | مجموعة Group بلا مستخدمين | مرجع شبح — List Users Access يعرضها | [INFERENCE] |

---

## الحالات ذات الأثر المعماري على البنية الجديدة

1. **E-SYS-01/02 (قفل المشرف):** البنية الجديدة **توجب** مسار استرداد (Frappe Administrator مستقل عن تطبيق الفندق) — قرار F-SYS-10.
2. **E-SYS-09 (تعديل Division Method):** يترجم إلى **تحذير تأثير** + منع التبديل مع وجود أرصدة أجنبية مفتوحة.
3. **E-SYS-18 (تحرير INI):** يُستأصل جذرياً بقرار F-SYS-2 (Feature Toggle بديل INI) — أقوى مبرر للاستبدال.
4. **E-SYS-19 (Delete نهائي):** حذف نسخ الاستخراج — يختفي مع استبدال Extract بـ Backup قياسي.
5. **E-SYS-14 (Tie-break):** يُحسم في الترجمة: `round(x, nearest, half-up)`.
