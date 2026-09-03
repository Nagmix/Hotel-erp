# 00 — نظرة عامة (Overview) — وحدة HR & Payroll (HRP)

> **وحدة إدارة الموارد البشرية والرواتب كاملة**: توظيف → ملفات موظفين → حضور → معادلات أجور بـ 4 أنواع شرائح → معالجة رواتب → صرف إجرائي نقدي/مصرفي → روابط AR→Payroll → تسويات نهائية. المقروء عميقاً كاملاً (الجلسة 8): **HRP-SET (42 ص/21 قسماً) + HRP-PNT (47 ص/24 وظيفة) + HRP-RQP (31 ص/8 وظائف) + HRP-REP (133 ص/19 مجموعة/68 تقريراً) = 253 ص كاملة**.

---

## 1. حدود الوحدة

| البند | الوصف الموثق |
|---|---|
| الاسم النظامي | HR & Payroll — "Payroll Entries is used by Users to create Personnel Master, direct employee entry, change employee info, create rate master definition, attendance entries, leave master, payroll processing etc." (PNT ص2) |
| الوظيفة الجوهرية | **خمس وظائف طبقية**: (1) Setup — البنية المرجعية (بنوك/فروع/درجات/فئات/كودات ED/حضور/إجازات/قوالب رواتب/فترات بداية/فئات تكلفة/فئات نقد/ميزانيات طاقم/تقارير مستخدم)؛ (2) Payroll Entries — دورة الرواتب التشغيلية (ملف الموظف → تعرفة → حضور → معاملات → معالجة → إقفال) + إجازات/مكافآت/قروض/تسوية نهائية؛ (3) Requirement Process — دورة التوظيف الكاملة (طلب → طلبات → فحص → مقابلات → عرض)؛ (4) Reports — 68 تقريراً عبر 19 مجموعة؛ (5) Statutory — المحرك الإجرائي الهندي (PF/ESI/PT/LWF بأرقام النماذج الرسمية) |
| المركز المعماري | **أغنى وحدة "محرك حسابي" في المشروع**: ED Calculation Definition بمعادلات تفاعلية + 4 أنواع شرائح + 4 مصادر احتساب + أولويات خصم + ترحيل جزئي + تكديس تراكمي/شهري + برامج خاصة — لا نظير مباشر في ERPNext القياسي → **محرك أجور مخصص (F-HR-1)** |
| نمط التشغيل | دورة شهرية محكمة: Starting Period (تحدد نطاق الفئة الزمني: يومي/أسبوعي/نصف شهري/شهري) → Attendance (يومي أو واجهة ملف) → Payroll Transactions (متغيرات) → Payroll Processing (احتساب + ACCEPT إدخال تفاعلي) → Closing/Canceling (تجميد) → Disbursement (نقد/بنك/شيك/حوالة) → Reports |
| النطاق | Employee lifecycle كاملاً (Candidate→On Roll→Left مع F&F) · Attendance (يدوي/افتراضي/واجهة جهاز) · ED engine (أرباح/خصومات بكل أنماطها) · Loans (أصل+فوائد+عوائد) · Bonus (استخلاص+معالجة+إقفال) · Leave (مجموعات→تفاصيل→ترحيل للرواتب) · AR deductions · Denomination نقدي · Payroll Audit |
| خارج النطاق | إدارة الدوام/الجداول (لا شيء موثق — خارج الحزمة)؛ تقييم الأداء/KPI (لا شيء)؛ التدريب (لا شيء)؛ الترحيل المحاسبي التفصيلي (الرابط موثق من طرف FAS — انظر 12) |

> ⚠️ **الاكتشاف الحاسم (يوسّع الرسم البياني للمعرفة):** وظيفة **AR to Payroll Transfer** (PNT §22): "If the employee buys something and the amount has to be charged to the payroll, then it goes to the accounts receivable... This information will be transferred to the Payroll so that the relevant amount is deducted from the employee's pay" — **جسر عكسي AR→HRP موثق بالنص** لم يكن مرسوماً في Knowledge Graph (كان الاتجاه الموثق Payroll→Finance فقط). كذلك يوثّق PNT §1 أن Personnel Master يستقبل تلقائياً بيانات المرشح من دورة RQP — **نصف UNK-010 محسوم من الداخل**.

## 2. جرد الوظائف الموثقة (21 + 24 + 8 + 68 ≈ 121 وظيفة/تقريراً)

| الدليل | الوظائف | العدد | المصدر |
|---|---|---|---|
| **HRP-SET** (Setup) | Bank Definition · Branch Code Definition (+Folio ledger) · Language Definition · Grade Definition · ED Code Definition · Attendance Code Definition · Property Attendance Definition · Category Code Definition · Define Starting Period · ED Calculation Definition (+Equation+Tables) · HOD Definition · Statutory Deduction Defn. (PF/ESI/PT/LWF) · Define Salary Template · Bonus Period Definition · Leave Group Parameter (INI 220!) · Leave Details Parameter · Costing Group Definition · Denomination Definition · Staff Budget Definition · User Defined Report Definition (+Formula) · User Defined Print Forms · **Payroll User Rights** | 21 (32 فرعية) | TOC SET ص1-2 |
| **HRP-PNT** (Payroll Entries) | Personnel Master · Direct Employee Entry (+Assets) · Change Employee Info · Rate Master Definition · Attendance Entry · Post Default Attendance · Attendance Post Interface (flat file!) · Payroll Transaction (+Tag More) · Supplementary Entries (PF/ESI/PT) · Payroll Processing (ACCEPT!) · Closing/Canceling Process · Change Employee Status · Leave Master · Leave Transaction (F5/F6!) · Leave Posting to Payroll · Bonus Extraction from Pay · Bonus Master/Supplementary · Bonus Processing (4 نسب!) · Closing Bonus · Loan Master · Loan Return Entry · **AR to Payroll Transfer** · Number Deduction Updation (F8) · Full And Final Settlement (+Indemnity) | 24 (34 مع الفرعية) | TOC PNT ص1-2 |
| **HRP-RQP** (Requirement Process) | Job Requirements · Application Details (+Qual/Exp/Ref/Lang/Passport) · Application Status · HOD Status · Interview Date · Interview Status · Offer Letter (+ED details+Template) · Offer Letter Status | 8 (16 مع الفرعية) | TOC RQP ص1 |
| **HRP-REP** (Reports) | Employee Information (9) · Payroll Reports (10) · Disbursement Statement · Group Abstract · Supplementary Check List · Attendance (5) · Transaction Check List/Worksheet · Leave Transaction List/Leave Ledger · Payslip Printing · Statutory (5) · PF Reports (9!) · ESI Reports (6) · Loan (4) · Bonus (7) · Master Reports (11) · User Defined Report · **Payroll Audit Report** | 19 مجموعة / 68 تقريراً | TOC REP ص1-4 |

## 3. المفاهيم الجوهرية الموثقة

| المفهوم | الدلالة | المصدر |
|---|---|---|
| **ED Code (أنماط 6)** | Earning / Regular Deduction / **Loan Deduction** / **Number Deduction** (PF/ESI/LIC برقم مرجعي!) / **Temporary** (حساب وسيط لا يطبع!) / **Cumulative YTD** (PF/ضريبة تراكمية سنوياً) — أوسع تصنيف مكونات أجر في المشروع | SET §5 ص7-8 |
| **ED Calculation (المحرك)** | 3 أنواع حساب (Payroll يطبع/Annual سنوي/Temporary وسيط) × 4 مصادر (None معادلة/Master من Rate Master/**Accept إدخال وقت المعالجة!**/Transaction متغير) + Priority/F3 إعادة ترتيب + Partial Deduction + Carry Forward + Specific Months + Accumulation (Month/Cumulative/**Cumulative C/O** بالتهيئة!) + Source ED + Subtract Flag + Gross Amount + Special Program (PYINDSP!) | SET §10 ص14-23 |
| **شرائح 4 أنواع بأمثلة رقمية** | Normal (شريحة واحدة 2500→20%=500) · **Cumulative** (1000×10%+1000×15%+500×20%=350!) · **Step Over** (الشريحة السابقة كاملة ثم الباقي: 2000×15%+500×20%=400!) · **Eligibility Check** (ESI: ≤6500 مؤهل/>6500 غير مؤهل — عتبة أهلية!) + Min/Max clamp لكل شريحة | SET §10 ص22-24 |
| **Take Home %** | "minimum salary (in terms of percentage) that the employee will get, **irrespective of the total deductions being greater than the earnings**" — 20%→الخصومات على 80% فقط؛ فارغ→الخصم الفعلي الكامل — **صمام أمان اجتماعي** على مستوى الفئة | SET §8 ص12 |
| **Starting Period** | تحدد فترة معالجة كل فئة: Daily (To=From) / Weekly (+7) / Fortnightly (+15) / Monthly (تقويمي إذا From بداية شهر، وإلا 21-Dec→20-Jan!) — "All the reports will be based on the period specified here only" + أول إقلاع: "The system will take the date range from next month onwards" | SET §9 ص13-14 |
| **واجهة الحضور الخارجية** | Flat Line Sequential file: `EMP#(7), DATE(8), CODE(3), DAYS(5,2)` مفصولة بفواصل → `PMS\Interface\PYATYYMM.DAT` — مع أيام عشرية (.5!) وساعات OVT (Hourly Flag) — **[Applicable to Fortune Enterprise Only]** فجوة إصدارية | PNT §7 ص16-18 |
| **ACCEPT التفاعلي** | أثناء Payroll Processing تظهر شاشة ED codes ذات Calculate From=Accept لإدخال مبالغ "applicable to all the employees under the specified category" (مثل FDA) — **إدخال بيانات وقت التشغيل الحسابي** | PNT §10 ص26-27 + SET §10 |
| **Bonus الرباعي** | 4 نسب: Ext. Bon. % (موجودون ≤ حد القطع) / Ext. Exg. % (موجودون > 7500!) / Left Bon. % / Left Exg. % + **Recalculate Professional Tax** (لأن الراتب يتغير بالمكافأة!) + Bypass Employees | PNT §18 ص33-34 |
| **قفل أصل القرض** | "Once the principal loan amount is entered in the Loan master it **cannot be changed**, so all the adjustments are done through this option" (Return Entry) — قيد سلامة مالية | PNT §21 ص36 |
| **Payroll Audit** | "list of all employee related records (Report Wise) that have been either **modified or deleted**... view the **old and new values**" — تقرير تدقيق تغييرات بقيم قبل/بعد — **أداة رقابة نادرة في المشروع** | REP §19 ص132-133 |

## 4. التفاعلات مع الوحدات (موثقة نصاً)

- **HRP → FAS (رابط الترحيل السادس):** موثق من طرف FAS-SET (روابط الترحيل الستة) — صرف الرواتب (Cash/Bank/Cheque/Draft/Transfer من Statements §2.5 + PF/ESI Challans بتفاصيل بنكية) وتوزيع التكاليف (Costing Group → Department/Cost Center).
- **HRP ← AR (جسر عكسي جديد):** "AR to Payroll Transfer" (PNT §22) — استيراد خصومات موظفين من الذمم مع ربط company code بالموظف — **يستكمل العائلة العكسية AR→(FO/POS/BNQ/HRP)**.
- **HRP ← RQP (داخلي):** Personnel Master "considers only those details that are recorded in the human resource module. Details of the candidate who has accepted the offer will be displayed" — التوظيف يغذي ملف الموظف آلياً (+ Salary Template عند العرض: "template that is applicable to the candidate").
- **HRP ← SYS:** Property codes (كل الشاشات) · Round Off (أنواع الثلاثة متطابقة!) · User setup (Payroll User Rights يمنح per-Category) · Print Forms infrastructure.
- **HRP ← أجهزة الحضور:** flat file من مزوّد خارجي (مواصفات vendor contract: "Any change... will be intimated... at least two weeks in advance").
- **HRP → البنوك:** Branch Code Definition بـ Folio Required (ledger/account numbers للموظفين!) + Disbursement + PF/ESI Challan (Cash/Cheque/Draft بتفاصيل A/C Group#/Cheque#).
- **HRP ↔ BNQ/POS/FO:** موظفو الخدمات (Banquet Staff/Service Managers في BNQ) يُدار ملفهم هنا؛ خصم مطاعم الموظفين يظهر في POS Staff Settlement → AR → AR to Payroll Transfer (الحلقة المغلقة!).

## 5. أهم الاكتشافات المعمارية (الجلسة 8)

1. **محرك ED المعادلاتي الفريد:** 6 أنماط ED × 3 أنواع حساب × 4 مصادر × 4 شرائح × تراكم 3 أنماط × أولوية/جزئية/ترحيل — **قرار F-HR-1: بناء Salary Structure Engine مخصص فوق Frappe HRMS** (معادلات Python-side + جداول شرائح) بدل الاعتماد على Salary Component القياسي.
2. **AR→Payroll موثق:** الجسر العكسي للخصومات يرسم **الحلقة الرابعة المغلقة** (POS/BNQ Staff consumption → AR → HRP deduction → Net Pay) — تحديث Knowledge Graph مطلوب.
3. **الرصيد الإجرائي الهندي كامل:** PF (بـ FPF/VPF/EDLI + Admin charges!) + ESI (Form 3/5/7 + Employer share) + PT (شرائح) + LWF — **9 نماذج PF رسمية (3A/5/6A/9/10/12A/Challan/Reconciliation/EDLI) قابلة للطباعة** — قرار F-HR-3: إبقاؤها طباعة مخصصة قابلة للتهيئة جغرافياً.
4. **Accept-at-Processing:** نمط إدخال قيم وقت المعالجة (FDA/Service Charge) — يتطلب تصميم Payroll Run wizard بحقول ديناميكية (F-HR-2).
5. **Take Home % كصمام أمان:** منطق خصم غير موجود في ERPNext (F-HR-5).
6. **فئات النقد (Denomination):** تقرير كسر النقد للصرف النقدي بقيم تنازلية — غير موجود في ERPNext (F-HR-8).
7. **INI 220 منطق معكوس مرة أخرى:** "To activate this parameter the INI Switch No. 220 should be set to **0**" — عائلة INI المعكوسة تتوسع (56/74/220).
8. **Payroll Audit بقيم قبل/بعد:** نمط versioning مسبق — يُستبدل بـ Versioning/Activity Log في Frappe (F-HR-10).
9. **Personnel Master رقم 7 خانات:** "EMP # can be numeric values of maximum 7 digits" — قيد طول التوظيف.
10. **F&F Settlement بمسار مطبوع ثلاثي:** Final/Vacation Settlement + Indemnity Calculation اختياري — يطابق Full and Final Statement في Frappe HRMS (F-HR-9 — إسقاط مباشر!).

## 6. هيكل الوثائق (19 ملفاً)

| # | الملف | المحتوى |
|---|---|---|
| 00 | نظرة عامة | هذه الوثيقة |
| 01 | Master Data | 50 كياناً بملفها |
| 02 | Configuration | مفاتيح + إعدادات (INI 220 + بنية Statutory) |
| 03 | Screens | 79 شاشة تشغيلية + 68 تقريراً بأولويات |
| 04 | Workflows | WF-HR-01..17 |
| 05 | Business Rules | BR-HR-01..18 |
| 06 | Validations | V-HR-01..30 + مصفوفة رسائل |
| 07 | Permissions | Payroll User Rights + مصفوفة الأدوار |
| 08 | Reports | 19 مجموعة/68 تقريراً مفهرسة |
| 09 | Lookups | Employee Lookup + استعلامات التشغيل |
| 10 | Transactions | سلاسل المستندات + دورة الإقفال |
| 11 | Accounting Impact | 18 حدثاً مالياً + جسر FAS |
| 12 | Integrations | I-HR-01..16 |
| 13 | Exceptions | E-HR-01..30 حالات حدية |
| 14 | Data Model | الكيانات والعلاقات |
| 15 | UX Analysis | أنماط الشاشات والإدخال |
| 16 | ERPNext Mapping | F-HR-1..12 + Seed Mapping |
| 17 | Gap Analysis | فجوات المصدر + فجوات ERPNext |
| 18 | Acceptance Criteria | 10 مجموعات + Smoke Test |
