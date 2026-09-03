# 00 — نظرة عامة (Overview) — وحدة MNT (Maintenance Management)

> **إدارة الصيانة**: من تسجيل شكوى أي قسم لأي غرفة أو موقع حتى **إغلاق العمل بتحليل تكلفة** — بمحرك صيانة وقائية ثنائي المستوى (PM Master بإيقاع أيامي + Lag ثم PM Entry بتواريخ محسوبة آلياً)، وتوليد **Job Orders** لأولويات **ملونة** تُسلَّم لموظف أو مزوّد خارجي، وسجل معدات بأربع شاشات فرعية (AMC/قطع غيار/قراءات قياسية/ملاحظات)، وجدول ورديات فنيين بنسخ خلايا/صفوف. **صفر قيود GL** — التكاليف تُسجَّل للتحليل فقط. المقروء عميقاً كاملاً (الجلسة 13): **SET (24 ص/12 قسماً) + OPR (28 ص/8 وظائف) + RPL (29 ص/15 تقريراً/استعلاماً) = 81 ص كاملة**.

---

## 1. حدود الوحدة

| البند | الوصف الموثق |
|---|---|
| الاسم النظامي | Maintenance Management — قوائم فرعية: **Setup / Operations / Reports & Lookups** (TOC الملفات الثلاثة) |
| الوظيفة الجوهرية | **أربع وظائف طبقية**: (1) Setup — 12 ماستراً تهيوياً (مواقع بلا غرف! · فئات معدات · فئات تكلفة · ورديات · أنواع خدمة Overhauling/Decarburizing/Lubrication · **إيقاعات خدمة بالأيام** · مهارات · **موظفو هندسة محليون** · أولويات شكاوى **بألوان** · **ربط مخازن ومراكز تكلفة من Inventory** · مصمم طباعة عام)؛ (2) Operations — 8 وظائف (تسجيل شكاوى · Action Taken بثلاثة مسارات · تعيين ورديات · Equipment Master · PM Master/Entry · توليد Job Orders · قراءات معدات)؛ (3) Reports — 15 تقريراً + **استعلام تفاعلي يغيّر الحالة (Complaint Status Q)** + محرك طباعة + **تصدير بارامترات كل الوحدات إلى Excel!** |
| المركز المعماري | **وحدة عمليات هندسية نقية بلا لمسة مالية**: الحلقة الوحيدة في المشروع التي تُوثّق دورة صيانة كاملة (شكوى/PM ← أولوية ← إسناد ← تنفيذ ← تكلفة تحليلية) — وتتغذى من Inventory (مخازن/مراكز تكلفة/أصناف قطع غيار) **دون أن تُصدر أي قيد أو إذن صرف مخزني موثق** (GAP) |
| نمط التشغيل | **مدفوع بأحداث** (شكوى تُسجَّل أو جدول PM يحين) + **دورة إشرافية يدوية** (Supervisory User ينتقي/يولّد/يسند/يطبع) + روتين ورديات وتقاطعات قراءات |
| النطاق | شكاوى أي قسم لأي غرفة/موقع · نوع Common/**Repeated** · مراجع خارجية 10 محارف · معدات بكود 8 محارف + مصنّع/طراز/مسلسل/تاريخ تركيب + **قيمة وعملة** · **AMC (عقد صيانة سنوي) بمزوّد وتاريخ انتهاء** · قطع غيار بمخزن وصنف وكمية ومزوّد و**Lead Time** · قراءات قياسية **Min/Max بـUOM** · PM بأنواع/إيقاعات/تأخير Lag/مهام · **Must Complete By ≤ Lag** · Job Orders بانتقاء NO→YES وأولوية ملونة · إسناد **لموظف أو مزوّد** · Action Taken بثلاثة مسارات + تحليل تكلفة + تفاصيل إصلاح بأصناف Inventory · **صنف مفتوح 999999999999** · ورديات مستقبلية ≤31 يوماً · مصمم طباعة بمحطية (6 صفوف = 1 بوصة) |
| خارج النطاق | أي قيد GL أو Revenue Code (التكلفة تحليلية فقط — راجع 11) · خصم مخزون موثق لقطع الغيار المستهلكة (لا إذن صرف! — GAP-MN-P3) · جسر الأصول الثابتة (قيمة المعدة لا تُقيَّد في FAS — GAP-MN-D05) · سنترال الموظفين (لا جسر HRP — **مخزن موظفين محلي خامس!**) · إشعارات/تصعيد آلي للشكاوى العاجلة |

> ⚠️ **ثلاث ملاحظات معمارية كبرى:** (1) **اللون أداة سير عمل** — كل أولوية شكوى تُعرَّف بلون، ويُبرز سجل Job Order بلون أولويته عند الإسناد — أقدم تجربة "لوحة كانبان بصرية" في المشروع قبل Kanban. (2) **مخزن موظفين هندسي خامس** (Employee # رقمي 7 خانات بلا جسر HRP — عائلة UNK-038 تتسع للمرة الخامسة) — الفنيون يُدارون محلياً في MNT رغم وجود HRP كاملة! (3) **صفر مفاتيح INI** (الخامسة بعد CARE/MEM/SLM/TEL) — السلوك يُدار عبر **عائلة Module Attributes جديدة: ENG #1 (طباعة طلب عمل عند تسجيل شكوى) و ENG #2 (طباعة Job Order عند توليده)**.

## 2. جرد الوظائف الموثقة (12 + 8 + 15 = 35 وظيفة/تقريراً/استعلاماً)

| الدليل | الوظائف | العدد | المصدر |
|---|---|---|---|
| **MNT-SET** (Setup) | Define Locations (6 محارف، بلا غرف!) · Equipment Category · Cost Category · Define Shifts (بترتيب) · Service Types · **Service Rhythms (بالأيام!)** · Define Skills · **Define Employees (رقمي 7!)** · **Complaint Priorities (بألوان!)** · Identify Engg Store(s) (من Inventory — حد أدنى 1) · Identify Engg Cost Center (من Inventory — حد أدنى 1) · **User Defined Print Forms (مصمم عام بمحطية)** | 12 | TOC SET ص1 |
| **MNT-OPR** (Operations) | Register Complaints (رقم آلي + Common/Repeated + ENG#1) · Action Taken (3 مسارات + تحليل تكلفة + تفاصيل إصلاح + **999999999999**) · Assign Shifts (مستقبلي ≤31 + F2/F3) · Equipment Master (4 شاشات فرعية) · PM Schedule Master (بـLag) · PM Schedule Entry (تواريخ آلية + Must-Complete-By ≤ Lag) · **Job Order Generation (ألوان + موظف/مزوّد + ENG#2)** · Equipment Reading Entry (بالقراءات المعرفة فقط) | 8 | TOC OPR ص1 |
| **MNT-RPL** (Reports & Lookups) | Complaints List · Duty Chart · **Complaint Status (Q) — استعلام تفاعلي يغيّر الحالة!** · Equipment Wise Complaints · Location Wise Complaints · Action Taken Report · Employee Wise Action Taken · Equipment Details List (بمعيار AMC!) · PM Schedule List · Resolution Time Report · Job Order Report · Spares and Cost Report · **Job/Complaint Print Engine** · Equipment Readings List · **Parameter Listing (كل بارامترات كل الوحدات → MS-Excel!)** | 15 | TOC RPL ص1 |

## 3. المفاهيم الجوهرية الموثقة

| المفهوم | الدلالة | المصدر |
|---|---|---|
| **الموقع (Location)** | "various Locations (**Other than rooms**) in the Property where equipments are placed example, **Lobby, Restaurants, various Departments, Kitchens**" — الموقع مكمّل لغرفة FO في كل اختيارات المعدات/الشكاوى/التقارير (نمط ثنائي Room-أو-Location متكرر 6 مرات) | SET ص3 |
| **إيقاع الخدمة (Service Rhythm)** | "the frequency at which different services are carried out, example **Daily, Weekly, Monthly, Annually**. The frequency has to be defined in terms of **'number of days'**" — و"No of Days between **two consecutive service rhythms**" — قلب حساب جدولة PM | SET ص11-12 |
| **أيام السماح (Lag Days)** | "Enter the number of days the selected service type **can lag (delay) for**" — سماحية تأخير الخدمة الوقائية، تُقيد صارماً بـ"Must Complete By": "(**Expected completion date should be less than or equal to the Lag days**)" — نافذة المرونة الوحيدة في الجدولة | OPR ص21-22 |
| **الأولوية الملونة** | "Each priority can have a **particular color**" + عند إسناد الأولوية في Job Order Generation: "**the record will be highlighted in the color that was set for the priority level**" — اللون حالة بصرية للسجل وليس زينة | SET ص15-16 + OPR ص24 |
| **الصنف المفتوح 999999999999** | "To enter an open item you have to enter **999999999999** in item code field. For the open items, the item name has to be entered manually. **This information will not affect Inventory stores**" — شرِكة هروب من Inventory (12 تسعة — أطول من 9999999999 في TEL باثنتين!) | OPR ص13 |
| **Common / Repeated** | نوع الشكوى عند التسجيل — ثنائية الشكوى العادية مقابل **المتكررة** (تتبع الأعطال المعاودة — بلا عرض لتاريخ التكرار — GAP-MN-P4) | OPR ص3 |
| **AMC** | "AMC (Annual Maintenance Contract) information is required or not. If required, then select the **vendor name, enter the expiry date**" — عقد صيانة سنوي مرتبط بالمعدة، **يُلتقط آلياً (auto populate)** في PM Schedule Master | OPR ص18 + ص21 |
| **القراءات القياسية** | "information relating to the **minimum and maximum UOM**" في Equipment Master، وقراءة المعدة "The readings which are **specified in the Equipment Master** for that particular equipment **only** can be entered" — قائمة قراءات مقيدة بالماستر **بلا إنذار تجاوز Min/Max موثق!** (GAP-MN-P5) | OPR ص19 + ص26 |
| **مخازن ومراكز تكلفة الهندسة** | "Select from the list of all stores defined in the **Inventory module**... A minimum of one store has to be selected" + Cost Centers بالمثل — كلاهما "defined in Fortune using the **Store code Definition / cost center code Definition option under the Customize sub module of the Material Management module**" — جسر MGT صريح مرتين | SET ص17-18 |
| **مستخدم إشرافي** | "This option is used by a **Supervisory User in the Maintenance Department** to prioritize and allocate the complaints/PM Tasks to different employees **based on their skills and availability**" — الدور الإشرافي الوحيد المسمّى في الوحدة | OPR ص22 |

## 4. الإحصاءات المقروءة

| المؤشر | القيمة |
|---|---|
| صفحات مقروءة عميقاً | 81 (SET 24 + OPR 28 + RPL 29) |
| وظائف/تقارير/استعلامات موثقة | 35 |
| شاشات رئيسية + فرعية | ~35 (راجع 03) |
| قواعد عمل موثقة | BR-MN-01..22 (راجع 05) |
| قيود إدخال موثقة | V-MN-01..20 (راجع 06) |
| قيود GL | **صفر** — التكلفة تحليلية (راجع 11) |
| عائلة Module Attributes | **ENG #1/#2** (جديدة — راجع 02) |
| مجهولات جديدة | UNK-058..062 (راجع تحليل الفجوات 17) |

## 5. موقعها في خريطة المشروع

- **قبلها:** FO (1) → FAS (2) → ACR (3) → POS (4) → SYS (5) → MGT (6) → BNQ (7) → HRP (8) → Care (9) → MEM (10) → SLM (11) → TEL (12) → **MNT (13 — هذه الوحدة)**.
- **علاقاتها الواردة:** MGT (مخازن + مراكز تكلفة + أصناف قطع الغيار) · مصدر Vendor غير موثق (UNK-058) · FO (غرف الشكاوى — ضمنياً) · SYS (ENG Attributes).
- **علاقاتها الصادرة:** لا شيء مالي؛ Parameter Listing يقرأ بارامترات "various modules" (استعلام عابر).
- **بعدها:** FNB (4 ملفات/76 ص) ← الجلسة 14.
