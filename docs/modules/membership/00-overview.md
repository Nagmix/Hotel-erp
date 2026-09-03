# 00 — نظرة عامة (Overview) — وحدة MEM (Membership)

> **وحدة إدارة العضويات (Club Membership Management)**: دورة حياة عضوية نادي/منتجع كاملة — **طلب (فرد/شركة) → فحص → مقابلة → تحويل → عضوية (فردية/شركة/منتمية لنادٍ متفق معه)** → تجديد/نقل فئة → إنهاء (قائمة سوداء/إنهاء/استقالة/وفاة) — مع **محرك فوترة ثلاثي الشرائح** (عضو/ضيف/عضو متفق معه) و**أربع محركات ترحيل شهرية إلى AR** (اشتراك + مرافق + رسوم سنوية Cover + رسوم تأخير). المقروء عميقاً كاملاً (الجلسة 10): **SET (16 ص/12 قسماً) + MMN (13 ص/7 وظائف) + MPF (30 ص/10 وظائف) + MTR (18 ص/13 وظيفة) + RPL (56 ص/38 تقريراً) = 133 ص كاملة**.

---

## 1. حدود الوحدة

| البند | الوصف الموثق |
|---|---|
| الاسم النظامي | Membership — "The Membership module... explains the various operations from including a new Member to the Member termination" (MPF ص1) |
| الوظيفة الجوهرية | **أربع وظائف طبقية**: (1) Setup — 12 ماستر: فئات العضوية + فحص + أسعار الخدمات (3 شرائح!) + أكواد الإيراد + هيكل الاشتراك + تصنيف الشكاوى + سمات النظام + أسعار ثابتة + أكواد المرافق + رسوم Cover + رسوم التأخير + حقول UDF؛ (2) Member Profiles — دورة الانضمام الكاملة (طلب→فحص→مقابلة→تحويل→عضوية) + النوادي المتفق معها؛ (3) Member Maintenance — 7 عمليات إدارية (عنوان/تجديد/قائمة سوداء/إنهاء/استقالة/وفاة/نقل فئة)؛ (4) Member Transactions — إيصالات + فوترة شهرية + زيارات + شكاوى + فعاليات + **5 محركات ترحيل إلى AR** |
| المركز المعماري | **وحدة إيراد مستقلة بذاتها**: تمتلك مخزن أعضاء خاصاً بها + ماستر أسعار + محرك فوترة + **دفاتر AR مصغرة داخلية** (تقارير Closing Balance/Due/Control مطابقة لعائلة ACR) — وترتبط بـ AR عبر إنشاء شركة تلقائي (MEMC001) وأربع محركات ترحيل، وبـ FO عبر بنيات الضرائب وسمة الربط |
| نمط التشغيل | دورة انضمام عند الطلب + **دورة شهرية مجدولة**: Process Subscription → Process Facility Charges → Cover Charges Posting → Posting Late Charges (كل واحدة تُرحّل لحساب AR للعضو)؛ ثم إيصالات/تسويات يومية للفواتير الخدمية |
| النطاق | عضويات فردية وشركة (بمرشحين nominees) · فحص بمجالس تحقق اختيارية · مقابلات Considered/Rejected/Cancelled · حدود ائتمانية عند التحويل · عائلات الأعضاء (زوج/أبناء/إضافيون بقبول/عضوية مستقلة) · تجديد/نقل فئة · 4 أنواع إنهاء بتتالٍ هابط · إيراد Once/Recurring · فوترة خدمات غير F&B · شكاوى ثنائية الاتجاه · فعاليات الأعضاء · 38 تقريراً |
| خارج النطاق | خدمات F&B (مقصودة صراحة: "used for non-Food and Beverage (F&B) services only" — مسار POS) · فوترة الغرف/الإقامة (FO) · طباعة كروت عضوية (غير موثقة — GAP-ME-D06) · ترحيل GL للقيود (أكواد إيراد موجودة دون حسابات دائن/مدين موثقة — GAP-ME-D02) |

> ⚠️ **ملاحظة معمارية كبرى:** وحدة Membership هي **خامس حلقة إيراد** في المشروع (بعد FO/POS/BNQ/AR) وتغلق نمط "الأعضاء كعملاء AR" — راجع 12-integrations §1.1 (جسر MEMC001) و§1.2 (محركات الترحيل الأربع).

## 2. جرد الوظائف الموثقة (12 + 7 + 10 + 13 + 38 ≈ 80 وظيفة/تقريراً)

| الدليل | الوظائف | العدد | المصدر |
|---|---|---|---|
| **MEM-SET** (Setup) | Member Categories (عائلة/مرشحون/مدة/عمر أبناء) · Screening Details (قائمة فحص!) · Service Rate Master (عضو/ضيف/متفق معه) · Membership Revenue Codes (Once/Recurring) · Membership Structure (أسعار لكل فئة) · Complaints Categories · System Attributes (13 سمة!) · Facility Fixed Rates · Membership Facility Codes · Cover Charges (مع إعفاء مسنين) · Late Charge Fee Definition (بنية ضريبية من FO!) · Member UDF | 12 | TOC SET ص1 |
| **MEM-MMN** (Maintenance) | Membership Address Change · Renewal Entry · Members Blacklist/Revoke · Members Termination · Members Resignation · Members Deceased (خلافة!) · Category Transfer | 7 | TOC MMN ص1 |
| **MEM-MPF** (Profiles) | Corporate Applications (مالية الشركات!) · Membership Application (عائلة كاملة) · Application Screening (فحص + بريد!) · Assign Interview Dates · Interview Details (3 حالات) · Transfer Corporate Application (+إيصال!) · Transfer Membership Application (+Credit Limit) · Corporate Master (دخول مباشر) · Membership Master (دخول مباشر) · Affiliated Club Master | 10 | TOC MPF ص1 |
| **MEM-MTR** (Transactions) | Membership Receipt Entry · Revenue/Facility Entry (فوترة شهرية) · Guest Visit Entry (رسوم دخول) · Service Bill Entry (محرك الفوترة) · Register Complaints · Attend Complaints · Event Definition · Process Subscription · Process Facility Charges · Post Subscription to AR (انتقائي!) · ~~Membership Tax Posting~~ (فهرس فقط — جسم مفقود GAP-ME-D01!) · Cover Charges Posting (Process/Cancel) · Posting Late Charges (الشهر السابق!) | 13 | TOC MTR ص1 |
| **MEM-RPL** (Reports & Lookups) | 38 تقريراً/استعلاماً — عائلات: عضوية (انضمام/تجديد/حالة/انتهاء) · تسويق (أعياد ميلاد/بطاقات بريدية/بريد إلكتروني) · مالية AR مصغرة (إقفال/مستحقات/تحكم/سجلات) · تحليل إنفاق (Spending Pattern بحفر!) | 38 | TOC RPL ص1-2 |

## 3. المفاهيم الجوهرية الموثقة

| المفهوم | الدلالة | المصدر |
|---|---|---|
| **شرائح الأسعار الثلاث** | كل خدمة لها 3 جداول أسعار: Member Rates / Guest Rates / **Affiliated Member Rates** — وكل جدول فيه Adult وChildren بأسعار مختلفة + بنية ضريبية — "The rates can be defined for every applicable membership category, with different rates for adults and children" | SET ص6-8 |
| **Once ≠ Recurring** | كود الإيراد Once "will appear in the option Revenue/Facility Entry" بينما Recurring "will NOT appear" — Recurring تُرحّل فقط عبر Process Subscription الدوري — **مفتاح توجيه الفوترة** | SET ص9 |
| **MEMC001 — إنشاء شركة AR تلقائي** | "a company master is automatically created as **MEMC001** where 'C' is the first letter of the Surname" — DAVID S CRAIG → شركة AR باسم MEMC001 — **الجسر المؤتمت الوحيد من نوعه في المشروع** (راجع 12-integrations §1.1) | SET ص12 |
| **التتالي الهابط الموحد** | "If the primary member is blacklisted/terminated/resigned then the additional members, spouse, and children... are **automatically** [affected]. However, if the spouse... are [affected], then the primary member is **not affected**" — قاعدة واحدة عبر 4 وظائف إنهاء (MMN ص6/8/9/12) | MMN ص6-12 |
| **خلافة العضو الأساسي المتوفى** | وفاة Primary تفتح شاشة خلافة: "You have an option to choose additional member, Spouse, or Children as the Primary Member. **If you choose 'None', then all the members of the membership will be removed**" | MMN ص11 |
| **رسوم التأخير بالشهر السابق** | "If you entered Month and year as **January-2011 then it will calculate the Outstanding amount of each member as on last date of December-2010** and if the outstanding amount is Debit amount then it will calculate the Latefee and post it to ACR" — **مثال رقمي موثق** | MTR ص18 |
| **الترحيل الانتقائي** | Post Subscription to AR: "This facility offers the flexibility to **withhold, withdraw, or overwrite** the subscription charges" — إلغاء اختيار عضو = حجب ترحيله | MTR ص17 |
| **فوترة غير F&B حصراً** | Service Bill Entry: "This option is used for **non-Food and Beverage (F&B) services only**" — كل خدمات المطاعم تمر عبر POS | MTR ص7 |
| **رسوم Cover بالإعفاء** | رسوم لكل فئة لكل فترة (شهري/ربعي/نصف سنوي/سنوي) مع خياري "Adjustment Debit to be Consider" و"**Senior Citizen Exemption**" + قيود عمر وسنوات عضوية | SET ص14-15 |
| **سمة الربط بـ FO** | "Link FO to membership: Yes - The Front Office module will be linked... The **Accounting date is picked up by default** in the Service Bill Entry" — FO هو مصدر التاريخ المحاسبي | SET ص12 |
| **إلغاء ترحيل Cover** | Cover Charges Posting بخيارين **Process/Cancel** — ترحيل قابل للإلغاء الشهري (نمط التراجع الموثق في AR) | MTR ص17 |
| **البريد الإلكتروني المدمج** | زر بريد في الفحص ("Click to **email the verification details** to the applicant") + Birthday List ("Click **Send Email** to send birthday wishes") — وحدة العضويات **الأغنى تكاملاً بريدياً** في المشروع | MPF ص18 + RPL ص33 |

## 4. التفاعلات مع الوحدات (موثقة نصاً)

- **MEM → AR (جسران!):** (1) إنشاء شركة ACR تلقائي عند حفظ Membership Master (سمة #10، مثال MEMC001)؛ (2) أربع محركات ترحيل: Process Subscription/Process Facility/Cover/Late Charges — كلها "posted to the relevant members AR account".
- **MEM ← FO:** بنيات الضرائب "available in the **Front office module**" لرسوم التأخير (SET ص15) + سمة Link FO تملأ تاريخ المحاسبة آلياً في Service Bill (SET ص12).
- **MEM × POS:** حدود واضحة — الفوترة غير F&B فقط (MTR ص7)؛ لا مسار موثق لفوترة عضو POS من هذه الوحدة (GAP-ME-D04).
- **MEM × BNQ (تشابه بلا جسر):** Event Definition (قاعة/وقت/ضيف شرف) تكرر مفاهيم حجز BNQ دون أي ربط موثق (GAP-ME-D03).
- **MEM → البريد الإلكتروني:** بريد التحقق + أمنيات أعياد الميلاد (مزوّد غير موثق).
- **MEM × العملات:** الإيصالات بعملات متعددة مع Currency Rate "automatically filled" + هيكل الاشتراك بعملة وسعر صرف تلقائي (MPF ص3/MTR ص3/SET ص10).

## 5. أهم الاكتشافات المعمارية (الجلسة 10)

1. **جسر AR المؤتمت الفريد:** MEMC001 — إنشاء شركة AR من حرف اسم العائلة عند الحفظ، مع **قيد لا رجعة فيه** (سمة #10 لا تُلغى بعد التفعيل!) — لا نظير لهذا النمط في 9 وحدات سابقة (قرار F-ME-9).
2. **خمس محركات ترحيل لا واحدة:** Subscription + Facility + Cover + Late + (Tax Posting المفقودة جسمها!) — أغنى وحدة ترحيلاً دورياً إلى AR بعد BNQ؛ كلها بمثال رقمي واحد موثق (Late) وبعضها قابل للإلغاء (Cover Process/Cancel).
3. **دفاتر AR مصغرة مدمجة:** 15 تقريراً مالياً (Closing Balance/Due/Control/Receipt Register/Credit Card Register/Transaction Check List...) يستغني بها العضويات عن الانتقال لوحدة ACR — نمط "وحدة بميزان مستقل".
4. **عائلة سمات النظام (13 سمة) بدل INI:** وحدة MEM لا تستخدم INI keys إطلاقاً — سمات Yes/No داخل System Attributes مع **عائلة استدعاء رباعية** (استدعاء إيصال من 4 شاشات حفظ مختلفة!) + تبعية #10←#9 + عدم قابلية عكس #10.
5. **ثلاث شرائح عملاء كاملة:** Member/Guest/Affiliated — الأ Affiliated مصدرها Affiliated Club Master (نوادي متفق معها بصورة!) — ترجمة Frappe طبيعية: Price Lists أو Customer Groups (F-ME-4).
6. **فجوة توثيق حرفية:** Membership Tax Posting مذكورة في فهرس MTR (#11) **وجسمها غير موجود في النص إطلاقاً** — أول حالة فهرس-بلا-جسم في 43 ملفاً مقروءاً (GAP-ME-D01 → UNK-045).
