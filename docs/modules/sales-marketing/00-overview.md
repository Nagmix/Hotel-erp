# 00 — نظرة عامة (Overview) — وحدة SLM (Sales & Marketing)

> **وحدة المبيعات والتسويق**: إدارة العلاقة التجارية مع الشركات من **احتمالية (Prospect) → أهداف مستوفاة → تحويل إلى Company Master (شركة CGR)** — مع **مركز مالي ائتماني مدمج داخل Company Profile** (حدود ائتمانية توقف تسويات FO/POS/BNQ!)، ثلاثية توزيع وكلاء (Allocation/Forecast/Release)، مخطط تنفيذي شخصي، و19 تقريراً تسويقياً. المقروء عميقاً كاملاً (الجلسة 11): **SLT (29 ص/10 وظائف) + PRF (42 ص/17 وظيفة) + REP (22 ص/19 تقريراً) + LUK (10 ص/6 استعلامات) = 103 ص كاملة**.

---

## 1. حدود الوحدة

| البند | الوصف الموثق |
|---|---|
| الاسم النظامي | Sales & Marketing — قوائم فرعية: Sales Tracking / Profiles / Reports / Lookups (TOC الملفات الأربعة) |
| الوظيفة الجوهرية | **أربع وظائف طبقية**: (1) Profiles — 17 ماستر تشمل **Company Profile بمركزه المالي الائتماني** + ماسترات الوكلاء + Hotel Profile التسويقي؛ (2) Sales Tracking — 10 وظائف تتبع (احتلال تاريخي، مهرجانات، موازنات، عملاء محتملون، أداة 360°، مكالمات، إعلانات/هدايا، خسائر أعمال، مخطط تنفيذي، تحويل)؛ (3) Reports — 19 تقريراً تسويقياً وإنتاجياً؛ (4) Lookups — 6 استعلامات أسعار وملفات |
| المركز المعماري | **وحدة CRM أمام FO/AR**: تمتلك مخزن العملاء المحتملين الخاص (Prospects منفصل عن Company Master!) + أدوات تتبع مبيعات — وتم **إنشاء/تحديث كيان AR المركزي (Company Profile)** الذي تستهلكه 6 وحدات (FO/S&M/POS/AR/BNQ/MEM نصاً!) |
| نمط التشغيل | دورة استقطاب عند الطلب (مكالمة → متابعة → عرض → عقد/خسارة) + **دورة موازنات سنوية** (Company Budgets → قياس Variance) + إدخال احتلال تاريخي (ما قبل تشغيل PMS) |
| النطاق | شركات CGR ومحتملة · وكلاء سياحة وجولات (تخصيص غرف/توقعات/تواريخ تحرر) · سياسات إلغاء/احتفاظ · خصومات إيراد (menu-type wise!) · مرفقات فندقية · ملف فندق تسويقي مقارن (منافسون/VIP/نزهات!) · مخطط تنفيذي (مواعيد/مهام/نزلاء) · بريد تسويقي جماعي |
| خارج النطاق | حجوزات الغرف نفسها (FO — SLM يوفر الأسعار/التخصيصات فقط) · فوترة AR نفسها (وحدة ACR) · تنفيذ الخصومات (POS/FO عند توليد الفواتير) · صلاحيات مستخدمين موثقة **إطلاقاً** (GAP-SM-D04) |

> ⚠️ **ملاحظة معمارية كبرى:** وحدة SLM هي **سادس بوابة إنشاء/تعديل لكيان AR** في المشروع (بعد AR نفسها + MEMC001 التلقائي) — **Company Profile تحت حوزتها الإدارية** لكن "Information recorded here is used in Front Desk, Sales & Marketing, Point of Sale, Accounts Receivables, Banquets, Conferencing and Membership modules" (PRF ص9-10) — راجع 12-integrations §1.

## 2. جرد الوظائف الموثقة (10 + 17 + 19 + 6 = 52 وظيفة/تقريراً/استعلاماً)

| الدليل | الوظائف | العدد | المصدر |
|---|---|---|---|
| **SLM-SLT** (Sales Tracking) | Daily Occupancy Entry (تاريخي!) · F&B Promotion Entry · Company Budgets · Prospect Entry · Sales Manager Tool (أداة 360°!) · Daily Sales Call · Entertainment/Gift Entry · Business Loss Entry · Executive Planner (محمي كلمة مرور!) · Transfer Prospects | 10 | TOC SLT ص1 |
| **SLM-PRF** (Profiles) | Sales Office · Sales Executives · Collection Executives · Bookers Master · Revenue Discount Master · Hotel Amenities · **Company Profile** (مركز AR!) · Update Company Profile (تحديث جماعي!) · Link Rates to Company · Retention Policy · Cancellation Policy · Agent Allocation · Agent Forecast · Agent Release Dates · Sales Call Types · Map Users/Sales Exec · Hotel Profile (تسويقي شامل!) | 17 | TOC PRF ص1-2 |
| **SLM-REP** (Reports) | Business Lost · Market Share Analysis (منافسون!) · Sales Call · Follow-up/Schedule · Birthday/Anniversary · Watch List Companies · Sales Performance (Budget) · Allocation List · Forecast List · Company List · Company Labels · Company Letters (بريد Outlook!) · E-Mail ID List · Company Productivity · Company Contribution Datewise · Company Contribution · Company Sales · Company Prod. Variance · Sales Performance Report | 19 | TOC REP ص1-2 |
| **SLM-LUK** (Lookups) | Browse Company · View Rate Structures · Company Rates-Datewise · Browse Hotel Profile · Company Package Rates · Company Rates (Query) | 6 | TOC LUK ص1 |

## 3. المفاهيم الجوهرية الموثقة

| المفهوم | الدلالة | المصدر |
|---|---|---|
| **CGR vs Potential** | "all Hotels try to get as many companies to join the ranks of Common Guaranteed Revenue (CGR) companies... The Hotel sets certain targets for each company... **Until the company fulfils the Hotel's requirements, it is known as Potential Company**" — ثنائية الوجود: مخزن Prospects منفصل عن Company Master، والتحويل مشروط باستيفاء الأهداف | SLT ص7 |
| **Transfer Prospects (التخرج)** | "Double-click on 'No' in the To Company Profile column to **post selected potential companies to the Company Master**... If these targets are met then they are posted... after which it is considered as a CGR company" — بوابة ترقية موثقة بشاشة مخصصة | SLT ص27-28 |
| **توليد كود الشركة التلقائي** | "The first three characters stand for type of company such as **COM for companies, TAG for travel agents, AIR for airlines**... the next character stands for the starting letter of the company name. **The system checks the last serial number for the company type and automatically generates the next number**" — آلية serial auto-increment لكل نوع+حرف | SLT ص28 |
| **بنية كود Company** | "This field supports alphanumeric values of character length up to 7. The first three characters is the guest/company type, which is predefined using **Company Types under Front Office Setup**. The next four characters can be a combination of alphanumeric" — 3 نوع + 4 حر | PRF ص10 |
| **الحد الائتماني الحاجب** | "If the current bill and/or the amount receivable exceed the specified credit limit, **settlement of the Front Desk, Point of Sale or Banquet bill or manual posting of the bill is not allowed**" — قفل صريح ثلاثي الوحدات + الإدخال اليدوي! | PRF ص13 |
| **Sales Manager Tool (CRM 360°)** | 10 عروض: General Information (للقراءة فقط — بيانات Prospect) · Sales Activity · Entertainment · Negotiated Rates · Amenities · Reservations (مع Cancelled وNo Show + Show Past Reservation) · In-house Guests · Revenue (شهرية برؤوس إيراد!) · **Receivables (cutoff = Accounting date!)** · Guest Visits — + **Hotel Position** (توفّر بأنواع الغرف → Hourly → Next day → Detailed → Yearly مع خيار Over Booking!) | SLT ص9-16 |
| **ثلاثية الوكلاء** | **Agent Allocation** (غرف مخصصة + نسبة حجز فائقة + أيام تأكيد + Week/Day Access بتبعية **Module Attribute #8**!) + **Agent Forecast** ("may be considered as confirmed... should match with the allocation") + **Agent Release Dates** (cutoff days متعددة → برنامج الحجز "prompts you to assign the rooms requested as **Inside or Outside allocation**") | PRF §12-14 |
| **Revenue Discount Master** | خصم نسبة لكل كود إيراد، و"F&B revenue code, percentage discount can be tagged **menu type wise (FOOD, LIQUOR, SOFTDRINKS, TOBACCO and OTHERS)**" — يُفعّل عند "generation of Bills in F&B outlets and various transaction entries" | PRF §5 |
| **Watch List** | "This option is specified if you require the room occupancy and business received information of a guest/company account **up to a specified date**" + تقرير بخياري Include Compliment/Houseguest | PRF ص10 + REP §6 |
| **Executive Planner** | "password protected and can be executed only by sales executives who have been **mapped to a user id using the Map User Id option**" + "Option can be extended to **all users by changing property.ini flag 239**" — 3 مناطق: Appointments (فرز بـCompany Name/zip/City/State + إعادة جدولة/إلغاء/تحويل لمندوب آخر!) · Things To Do (7am-8pm، Important/Normal) · In-house Guest | SLT §9 |
| **Hotel Profile التنافسي** | "define information related to the default Hotel and **groups of hotels within the Property or any other Hotel(s) information on which a comparative study has to be done**" — 10 كتل: HODs · Outlets (Dress Code/Smoking/Chef!) · Rooms + مواسم أسعار · Banquets · CGR · VIP visits · **Picnic Spots**! · صورة (BMP فقط!) · معلومات عامة (حرارة/مسافات/أجرة) | PRF §17 |
| **Market Share (ذكاء منافسين)** | "displays **room occupancy information of other competing Hotels**... based on the comparative room sales entry" + قيد "month and year entered in the To Date field should be **equal to the month and year of the From Date**" — شاشة إدخال البيانات المقارنة غير موثقة (GAP-SM-D01) | REP §2 |
| **الاحتلال التاريخي** | "record the **backdated** room occupancy information for all Properties (same or different Groups) **before IDS PMS went on live**... this helps in generating MIS reports for entire Financial Year" — إدخال ما قبل التشغيل | SLT §1 |

## 4. التفاعلات مع الوحدات (موثقة نصاً)

- **SLM → AR (الجسر الأعمق):** Company Profile يحمل كل شروط الائتمان (Bypass Invoice/Allow Credit/Credit Days/Invoice Currency/Interest %/Credit Limit/Commission %/Collection Executive) + عرض Receivables في Sales Manager Tool بتاريخ قطع = Accounting date + Transfer Prospects يُنشئ سجلات Company Master.
- **SLM ← FO (توأمة إعدادات):** Company Types + Sales Office + Sales Executives + Collection Executives + Bookers Types كلها "under Front Office Setup" (نفس البيانات!) + Rate Structures تُستهلك في حجوزات FO + Retention تُحصّل عبر "Retention-Cancel/No show option **under front office**" + تخصيصات الوكلاء تستدعي "reservation program prompts" + Amenities "highlighted when a reservation is being made".
- **SLM → POS:** خصومات الإيراد "applicable during the generation of Bills in **F&B outlets**" + حد الائتمان يوقف تسويات POS.
- **SLM → BNQ:** Company Profile "used in... **Banquets**" + حد الائتمان يوقف تسوية فواتير البنوك.
- **SLM → MEM:** Company Profile "used in... **Membership**" (شركات العضويات).
- **SLM → SYS:** Map Users/Sales Exec يربط بـ"User Setup **under System Setup**" + مفاتيح INI رقم 239 و41.
- **SLM ↔ البريد الخارجي:** Company Letters عبر "**Microsoft outlook** as E-Mail with attachments" — التكامل الخارجي الموثق الوحيد في الوحدة.
- **SLM ↔ HRP (غياب!):** Sales Executives وCollection Executives يُعرّفون في FO Setup **لا في HRP** — ثالث مخزن موظفين (راجع UNK-038).

## 5. أهم الاكتشافات المعمارية (الجلسة 11)

1. **مركز الائتمان في غير وحدة الائتمان:** شروط AR المالية الكاملة تسكن Company Profile داخل SLM — والقفل الائتماني ثلاثي الوحدات (FO/POS/BNQ + manual posting) — أقوى تأثير مالي موثق لوحدة "غير مالية".
2. **دورة Prospect→CGR بمستودعين:** Prospects ليست سجلات مؤقتة بل ماستر كامل (CEO/holding/competitors/turnover/Frequent Travelers!) والتحويل وظيفة مخصصة بتوليد كود آلي (TTT+حرف+مسلسل لكل نوع!) — تطابق شبه حرفي لدورة Lead→Customer في ERPNext (F-SM-1).
3. **مفتاحا INI جديدان:** **#239** (تعميم المخطط التنفيذي لكل المستخدمين) و**#41 = '0'** لتفعيل تحقق cutoff في الحجوزات — العائلة المقلوبة (الصفر يُفعّل! — انضمام لعائلة 56/74/220) + **Module Attribute #8** يقلب شاشة Week Access↔Day Access.
4. **SaaS تسويقي مبكر:** Birthday/Anniversary + Company Letters (بريد جماعي بمرفقات عبر Outlook + منطق CEO→بريد الشركة vs بريد جهات الاتصال) + Company Labels (2/3 أعمدة) + E-Mail ID List — قناة تسويق كاملة قبل عصر CRM الحديث.
5. **فندقية "الدراسة المقارنة":** Hotel Profile يتسع لفنادق المنافسين (ل Market Share) وكتل Picnic Spots/VIP/Outlets بمعلومات عرضية غنية (Dress Code/Smoking/Chef/View) — محتوى تسويقي فوق-تشغيلي.
6. **فجوة صلاحيات كاملة:** لا قسم User Rights في أي من الملفات الأربعة — الوحدة الوحيدة بعد 44 ملفاً بلا أي صلاحيات موثقة (GAP-SM-D04).
