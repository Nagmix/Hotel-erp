# 02 — الإعدادات (Configuration) — وحدة MNT

> تكوين الوحدة **بلا مفاتيح INI** (الخامسة في العائلة) — يُدار عبر: **عائلة Module Attributes جديدة ENG #1/#2** (بوابات الطباعة) + الارتباطات الانتقائية بمخازن/مراكز تكلفة MGT + الألوان + إعدادات المحطية في مصمم الطباعة.

---

## 1. عائلة Module Attributes — ENG (جديدة كلياً!) ⭐

> أول ظهور لعائلة سمات **ENG** في المشروع (بعد FO Attributes وPOS وغيرها) — وثيقتان فقط ظهرتا منهما:

| السمة | الوظيفة الموثقة | موضع التفعيل | المصدر |
|---|---|---|---|
| **ENG Module Attribute #1 = 'YES'** | طباعة **Job Request** فور تسجيل شكوى: "The user can print a job request, if the ENG Module Attribute #1 is 'YES'" — يظهر حوار Yes/No بعد الحفظ | Register Complaints (بعد الحفظ) | OPR ص4 |
| **ENG Module Attribute #2 = 'YES'** | طباعة **Job Order** فور توليده: "You can print a job Order, if the ENG Module Attribute #2 is 'YES'" — حوار طباعة بعد الإسناد | Job Order Generation (بعد الإسناد) | OPR ص26 |

- **UNK-061:** كم سمة ENG إجمالاً وأين تُعرَّف؟ (الأرجح SYS/SUPERVISOR بنمط Module Attributes الموثق في FO/POS — يُفحص عند SYS-SSP النهائي).
- **الدلالة:** بواباتا طباعة تفصلان مستندين مختلفين — **Job Request** (مطبوع من شكوى خام) و**Job Order** (مطبوع من إسناد مُشرف) — سندانا الورق في دورة الصيانة؛ وغياب #1=NO يعني الشكوى تعيش رقمياً بلا ورقة طلب.

## 2. الارتباطات (فوق الماسترات — راجع 01 §4)

| الإعداد | القيد الموثق | أثر الغياب |
|---|---|---|
| Engg Stores | "A **minimum of one store** has to be selected" (checkbox من Inventory) | لا اختيار أصناف في Equipment Master/Action Taken |
| Engg Cost Centers | "A **minimum of one cost center**" بالمثل | لا Repair Details (الحقل إلزامي في الشاشة) |

## 3. أولويات الألوان

- التكوين عبر **F1 في حقل Color** بـComplaint Priorities — "Select the desired color to **tag it** to the priority".
- لا إعداد إضافي للألوان في أي ملف — يفترض ثبات الاختيار بعد الحفظ (UNK-060 للّوحة).
- الأثر التشغيلي الوحيد الموثق: **تلوين صف السجل** في شاشة إسناد الأولويات (OPR ص24) — لا أثر للألوان في التقارير المطبوعة.

## 4. إعدادات المحطية والطباعة (UDPF)

| الإعداد | المواصفة | المصدر |
|---|---|---|
| Printer Type | Normal Printer / **Slip Printer** (افتراضي Normal) | SET ص21 |
| Stationery Math | مجموع Header+Footer+Body rows = طول المحطية؛ **6 rows = 1 Inch** | SET ص20 |
| Page Continue | "select the format for page continue for the forms that will exceed to more than one page" | SET ص20 |
| Copies / أحرف H×V | عند Match Samples | SET ص20 |
| نوع البرنامج | Bill print · KOT Print · NC Bill Print · Invoice Print (قائمة نوع البرنامج — بصياغة POS!) | SET ص21 |
| التعيين | Description نصي حر ("Debit note" مثالاً) | SET ص21 |

- **ملاحظة معمارية:** القوائم المرجعية للنوع **POS-المحورية** (Bill/KOT/NC) داخل وحدة صيانة — دليل إضافي أن UDPF **أصل Fortune مشترك** يُستدعى من قوائم وحدات متعددة (راجع 12 §6 و15 §5).

## 5. إعدادات مرجعية بلا جسم موثق (رصد)

| العنصر | الحالة | المسار |
|---|---|---|
| Module Attributes ENG الكاملة | سمتان فقط ظهرتا | UNK-061 |
| ألوان الأولوية (اللوحة) | حقل بلا جرد | UNK-060 |
| ماستر Designations (لكود المسمى الوظيفي 3 محارف) | F1 بلا شاشة تعريف في أي ملف MNT | UNK-059 |
| مصدر Vendor / Service Provider | F1 بلا ماستر موثق | UNK-058 |
| مفاتيح INI | **لا شيء** — الخامسة (CARE/MEM/SLM/TEL/MNT) | عائلة موثقة |

## 6. مصفوفة "ماذا لو" التكوينية (موثقة حرفياً)

| القرار | النتيجة الموثقة |
|---|---|
| ENG#1 = NO | لا حوار طباعة بعد تسجيل الشكوى (تسجيل رقمي صرف) |
| ENG#2 = NO | Job Order يُولَّد ويُسند بلا طباعة |
| صفر مخازن مختارة | تكوين غير قابل للحفظ (حد أدنى 1) |
| Long text > المحطية | Print From/To يقصّ الحقل (خصائص F4) |
| حقل الصفحة الأخيرة = True | يظهر مرة واحدة في نهاية مستند متعدد الصفحات (UserId مثالاً) |
