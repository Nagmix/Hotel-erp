# PHASE 0 — تتبع تغطية المصادر (Source Coverage)

> **القاعدة:** لا يُعتبر المشروع مكتملًا قبل تحقيق تغطية 100% أو تسجيل سبب واضح لكل استثناء.
> **التحديث:** تُحدَّث هذه الوثيقة بعد كل جلسة عمل.

**حالة كل ملف:**

| الحالة | المعنى |
|---|---|
| `discovered` | اكتُشف اسمه ومساره فقط |
| `indexed` | أُضيف للجرد مع الصفحات والنوع والفهرس |
| `text-extracted` | استُخرج نصه الكامل إلى `extracted-text/` |
| `toc-analyzed` | حُلِّل فهرسه وأُضيفت موضوعاته لخريطة الوثائق |
| `read` | قُرئ المحتوى الفعلي (Deep Read) |
| `analyzed` | استُخرجت المعرفة الوظيفية إلى `docs/modules/...` |
| `cross-referenced` | رُبطت معرفته بالوحدات الأخرى (workflows/accounting) |
| `verified` | راجعها فحص الجودة (Quality Gate) |

---

## ملخص التغطية الحالية

| المؤشر | القيمة |
|---|---|
| إجمالي الملفات | 65 |
| discovered → indexed | **65 / 65 (100%)** ✅ |
| text-extracted | **65 / 65 (100%)** ✅ |
| toc-analyzed | **65 / 65 (100%)** ✅ |
| field-extracted (جداول الحقول آلياً) | **13 ملف إعدادات — 2,099 حقلاً** ✅ |
| read (قراءة عميقة) | **62/65** — FO 11 + FAS 4 + ACR 5 + POS 4 + SYS 1 + MGT 3 + BNQ 5 + HRP 4 + Care 3 + MEM 5 + SLM 4 + TEL 4 + MNT 3 + FNB 4 + FXD 1 + GTP 1 (نهاية الجلسة 16 — **FO أول وحدة كاملة المصادر 11/11** + بدء Phase 7) |
| analyzed | **17/17 وحدة / 306 ملف وثائق + Phase 7 بدأت: reports/front-office 12 ملفاً** (FO 19 + FAS 18 + ACR 19 + POS 19 + SYS 19 + MGT 19 + BNQ 19 + HRP 19 + Care 19 + MEM 19 + SLM 19 + TEL 19 + MNT 19 + FNB 19 + FXD 19 + GTP 19 + **reports/FO 12**) |
| cross-referenced | 0 / 65 |
| verified | 0 / 65 |

> ✅ **النتيجة المهمة:** جميع الملفات الـ 65 نصوصها قابلة للاستخراج آلياً — لا يوجد أي ملف يتطلب OCR. عدد الصور المضمنة ~7,763 (لققطات شاشة) متاحة للتحليل البصري عند الحاجة عبر PyMuPDF.

---

## جدول التغطية التفصيلي

> يُحدَّث عمود "Deep Read" مع تقدم المراحل. الرموز: **✓ = كامل | ◐ = جزئي (مع النسبة) | – = لم يبدأ**. ترتيب الأولويات مبني على وثيقة module-inventory §5.

| # | الوحدة | الملف | الصفحات | indexed | text | toc | deep-read | analyzed | x-ref | verified |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Front Office | FN6i-NT-FOM-SET.pdf | 145 | ✓ | ✓ | ✓ | **✓ كامل (67 قسماً + مصفوفة التعديل 48 Note)** | **✓ → modules/front-office/** | – | – |
| 2 | Front Office | FN6i-NT-FOM-REP.pdf | 120 | ✓ | ✓ | ✓ | **✓ كامل (Phase 7/الجلسة 16: ~135 تقريراً + 28 فرعياً — محرك إخراج رباعي + INI 63 + PMSPOL.INI→POL.SPC + "This mandatory report" + صيغة Room Balance + مصفوفة تواريخ ~25 قاعدة + Audit ×8)** | **✓ → reports/front-office/ (12 ملفاً)** | – | – |
| 3 | Front Office | FN6i-NT-FOM-REG.pdf | 105 | ✓ | ✓ | ✓ | **✓ كامل (28 وظيفة، ص1-105)** | **✓ → modules/front-office/** | – | – |
| 4 | Front Office | FN6i-NT-FOM-CAS.pdf | 95 | ✓ | ✓ | ✓ | **✓ كامل (20 وظيفة، ص1-95)** | **✓ → modules/front-office/** | – | – |
| 5 | Front Office | FN6i-NT-FOM-LUK.pdf | 51 | ✓ | ✓ | ✓ | **✓ كامل (22 وظيفة)** | **✓ → modules/front-office/ (09)** | – | – |
| 6 | Front Office | FN6i-NT-FOM-GST.pdf | 57 | ✓ | ✓ | ✓ | **✓ كامل (17 وظيفة + الولاء)** | **✓ → modules/front-office/ (04/05)** | – | – |
| 7 | Front Office | FN6i-NT-FOM-HSK.pdf | 59 | ✓ | ✓ | ✓ | **✓ كامل (18 وظيفة + دورة الغسيل)** | **✓ → modules/front-office/ (04/05)** | – | – |
| 8 | Front Office | FN6i-NT-FOM-RES.pdf | 68 | ✓ | ✓ | ✓ | **✓ كامل (7 وظائف رئيسية، ص1-68)** | **✓ → modules/front-office/** | – | – |
| 9 | Front Office | FN6i-NT-FOM-SMS.pdf | 14 | ✓ | ✓ | ✓ | **✓ كامل (الجلسة 16: Mobile Master + 8 خدمات SMS بمحتوى حرفي + Department Checkout Alert + "Fortune Next Enterprise 2.0" — C-FO-02)** | **✓ → reports/front-office/ (10)** | – | – |
| 10 | Front Office | FN6i-NT-FOM-CRG.pdf | 19 | ✓ | ✓ | ✓ | **✓ كامل (Concierge — 5 وظائف)** | **✓ → modules/front-office/ (04)** | – | – |
| 11 | Front Office | FN6i-NT-FOM-DEP.pdf | 14 | ✓ | ✓ | ✓ | **✓ كامل** | **✓ → modules/front-office/** | – | – |
| 12 | Point of Sale | FN6i-NT-POS-SET.pdf | 122 | ✓ | ✓ | ✓ | **✓ كامل (42 قسماً + فجوة §42 Taxcode Mapping فارغة)** | **✓ → modules/point-of-sale/** | – | – |
| 13 | Point of Sale | FN6i-NT-POS-REP.pdf | 158 | ✓ | ✓ | ✓ | – | – | – | – |
| 14 | Point of Sale | FN6i-NT-POS-GST.pdf | 56 | ✓ | ✓ | ✓ | **✓ كامل (12 وظيفة Guest History + الولاء)** | **✓ → modules/point-of-sale/** | – | – |
| 15 | Point of Sale | FN6i-NT-POS-LUK.pdf | 14 | ✓ | ✓ | ✓ | **✓ كامل (7 استعلامات + صيغة Average Per Check)** | **✓ → modules/point-of-sale/** | – | – |
| 16 | Materials Management | FN6i-NT-MGT-REP.pdf | 112 | ✓ | ✓ | ✓ | – (مؤجل Phase 7) | – | – | – |
| 17 | Materials Management | FN6i-NT-MGT-DNT.pdf | 75 | ✓ | ✓ | ✓ | **✓ كامل (15 وظيفة Daily Entries — الإصدار/المرتجعات/الجرد/الإقفال الشهري)** | **✓ → modules/materials-management/** | – | – |
| 18 | Materials Management | FN6i-NT-MGT-SET.pdf | 68 | ✓ | ✓ | ✓ | **✓ كامل (28 قسماً — المخازن/الأصناف/Master المورد بـ 7 عائلات)** | **✓ → modules/materials-management/** | – | – |
| 19 | Materials Management | FN6i-NT-MGT-LUK.pdf | 38 | ✓ | ✓ | ✓ | **✓ كامل (20 استعلاماً + Drill-down ثلاثي)** | **✓ → modules/materials-management/ (09)** | – | – |
| 20 | Banquets | FN6i-NT-BNQ-SET.pdf | 98 | ✓ | ✓ | ✓ | **✓ كامل (20 قسماً — القاعات/المعدات/الأسعار التعاقدية/التقويم الحاجب)** | **✓ → modules/banquets/** | – | – |
| 21 | Banquets | FN6i-NT-BNQ-BIL.pdf | 66 | ✓ | ✓ | ✓ | **✓ كامل (13 قسماً — التسويات الـ 11 + الودائع + Requirement + Auto Indent!)** | **✓ → modules/banquets/** | – | – |
| 22 | Banquets | FN6i-NT-BNQ-BOK.pdf | 41 | ✓ | ✓ | ✓ | **✓ كامل (Bookings: Make بـ 7 أقسام + Across-Dates + Cancel/No-Show + Block)** | **✓ → modules/banquets/** | – | – |
| 23 | Banquets | FN6i-NT-BNQ-CFG.pdf | 38 | ✓ | ✓ | ✓ | **✓ كامل (12 قسماً — Function Room 6 تبويبات + Menu Cards + Sub Venues)** | **✓ → modules/banquets/** | – | – |
| 24 | Banquets | FN6i-NT-BNQ-LUK.pdf | 12 | ✓ | ✓ | ✓ | **✓ كامل (استعلامان — Availability Chart بألوان الحالة + INI 408)** | **✓ → modules/banquets/ (09)** | – | – |
| 25 | HR & Payroll | FN6i-NT-HRP-REP.pdf | 133 | ✓ | ✓ | ✓ | **✓ كامل (19 مجموعة/68 تقريراً — أضخم REP بعد FO؛ Payroll Audit بقيم old/new)** | **✓ → modules/hrp-payroll/** | – | – |
| 26 | HR & Payroll | FN6i-NT-HRP-PNT.pdf | 47 | ✓ | ✓ | ✓ | **✓ كامل (24 وظيفة — دورة الرواتب + AR→Payroll Transfer + F&F)** | **✓ → modules/hrp-payroll/** | – | – |
| 27 | HR & Payroll | FN6i-NT-HRP-SET.pdf | 42 | ✓ | ✓ | ✓ | **✓ كامل (21 قسماً — محرك ED + الشرائح الأربع + الإجرائية الهندية + Payroll User Rights)** | **✓ → modules/hrp-payroll/** | – | – |
| 28 | HR & Payroll | FN6i-NT-HRP-RQP.pdf | 31 | ✓ | ✓ | ✓ | **✓ كامل (8 وظائف — دورة التوظيف الكاملة)** | **✓ → modules/hrp-payroll/** | – | – |
| 29 | Financial Management | FN6i-NT-FAS-REP.pdf | 64 | ✓ | ✓ | ✓ | – (مؤجل Phase 7) | – | – | – |
| 30 | Financial Management | FN6i-NT-FAS-SET.pdf | 48 | ✓ | ✓ | ✓ | **✓ كامل (27 قسماً — الروابط الست)** | **✓ → modules/financial-accounting/** | – | – |
| 31 | Financial Management | FN6i-NT-FAS-TRN.pdf | 45 | ✓ | ✓ | ✓ | **✓ كامل (9 أقسام + FO/POS/PJV posting)** | **✓ → modules/financial-accounting/** | – | – |
| 32 | Financial Management | FN6i-NT-FAS-MST.pdf | 33 | ✓ | ✓ | ✓ | **✓ كامل (COA + Vendor + ChequeBook)** | **✓ → modules/financial-accounting/** | – | – |
| 33 | Financial Management | FN6i-NT-FAS-LUK.pdf | 28 | ✓ | ✓ | ✓ | **✓ كامل (9 استعلامات)** | **✓ → modules/financial-accounting/** | – | – |
| 34 | Care | FORTUNE CARE v6 - OPERATIONS.pdf | 80 | ✓ | ✓ | ✓ | **✓ كامل (6 وظائف — الروستر D&D + Login/Logout بعهدة موبايل + Manual Entry بمحرك SMS ثنائي الاتجاه `1 S`/`1 C` مع 5 رسائل خطأ حرفية + Group SMS + Agent Console + Supervisor Lookup بأربع عمليات)** | **✓ → modules/care/** | – | – |
| 35 | Care | FORTUNE CARE v6 - REPORTS & LOOKUPS - VER 10 AUGUST.pdf | 73 | ✓ | ✓ | ✓ | **✓ كامل (20 تقريراً — 7 Charts + 3 Drilldown رباعي المستويات حتى سجل بـ CI/CO من PMS + IVR Code في Task List + SMS Queued كملخص إداري)** | **✓ → modules/care/** | – | – |
| 36 | Care | FORTUNE CARE v6 - SETUP - VER 10 AUGUST.pdf | 34 | ✓ | ✓ | ✓ | **✓ كامل (6 أقسام — User Creation بـ PMS فقط! + Define Rights نمط SYS + Org Structure شجرة بـ Reporting تصعيدي + Task Definition بمهلات 4 مستويات + Multi Task عبر الأقسام + Restrict Reports)** | **✓ → modules/care/** | – | – |
| 37 | Membership | FN6i-NT-MEM-RPL.pdf | 56 | ✓ | ✓ | ✓ | **✓ كامل (38 تقريراً/استعلاماً)** | **✓ → modules/membership/** | – | – |
| 38 | Membership | FN6i-NT-MEM-MPF.pdf | 30 | ✓ | ✓ | ✓ | **✓ كامل (10 وظائف — دورة الانضمام)** | **✓ → modules/membership/** | – | – |
| 39 | Membership | FN6i-NT-MEM-MTR.pdf | 18 | ✓ | ✓ | ✓ | **✓ كامل (13 وظيفة — محركات الترحيل)** | **✓ → modules/membership/** | – | – |
| 40 | Membership | FN6i-NT-MEM-SET.pdf | 16 | ✓ | ✓ | ✓ | **✓ كامل (12 قسماً + 13 سمة)** | **✓ → modules/membership/** | – | – |
| 41 | Membership | FN6i-NT-MEM-MMN.pdf | 13 | ✓ | ✓ | ✓ | **✓ كامل (7 وظائف — عائلة الإنهاء)** | **✓ → modules/membership/** | – | – |
| 42 | System Setup | FN6i-NT-SYS-SSP.pdf | 110 | ✓ | ✓ | ✓ | **✓ كامل (3 فصول + 19 قسماً + §19 Group Nationality غير المفهرسة)** | **✓ → modules/system-setup/** | – | – |
| 43 | Sales & Marketing | FN6i-NT-SLM-PRF.pdf | 42 | ✓ | ✓ | ✓ | **✓ كامل (17 وظيفة — Company Profile مركز AR + Hotel Profile)** | **✓ → modules/sales-marketing/** | – | – |
| 44 | Sales & Marketing | FN6i-NT-SLM-SLT.pdf | 29 | ✓ | ✓ | ✓ | **✓ كامل (10 وظائف — دورة Prospect→CGR + Planner)** | **✓ → modules/sales-marketing/** | – | – |
| 45 | Sales & Marketing | FN6i-NT-SLM-REP.pdf | 22 | ✓ | ✓ | ✓ | **✓ كامل (19 تقريراً — Letters/Labels/Market Share)** | **✓ → modules/sales-marketing/** | – | – |
| 46 | Sales & Marketing | FN6i-NT-SLM-LUK.pdf | 10 | ✓ | ✓ | ✓ | **✓ كامل (6 استعلامات — Browse من شاشة الحجز!)** | **✓ → modules/sales-marketing/** | – | – |
| 47 | Accounts Receivales | FN6i-NT-ACR-RPL.pdf | 33 | ✓ | ✓ | ✓ | **✓ كامل (23 وظيفة + فجوة «12123 PENDING» موثقة)** | **✓ → modules/accounts-receivable/** | – | – |
| 48 | Accounts Receivales | FN6i-NT-ACR-OPR.pdf | 21 | ✓ | ✓ | ✓ | **✓ كامل (8 أقسام — SOA/Rollback/Match/Untagging)** | **✓ → modules/accounts-receivable/** | – | – |
| 49 | Accounts Receivales | FN6i-NT-ACR-SET.pdf | 19 | ✓ | ✓ | ✓ | **✓ كامل (8 أقسام — Company Profile المشترك)** | **✓ → modules/accounts-receivable/** | – | – |
| 50 | Accounts Receivales | FN6i-NT-ACR-BIL.pdf | 8 | ✓ | ✓ | ✓ | **✓ كامل (4 أقسام الفوترة)** | **✓ → modules/accounts-receivable/** | – | – |
| 51 | Accounts Receivales | FN6i-NT-ACR-CRT.pdf | 8 | ✓ | ✓ | ✓ | **✓ كامل (Debtors Follow-Up + تنقيب 4 مستويات)** | **✓ → modules/accounts-receivable/** | – | – |
| 52 | Telephones | FN6i-NT-TEL-SET.pdf | 32 | ✓ | ✓ | ✓ | **✓ كامل (10 أقسام — الامتدادات بنسب×4 + شرائح نبضية خالدة ثنائية P&T/فندق×عادي/عيد + شراكات 6 + واجهة Onity!)** | **✓ → modules/telephone/** | – | – | – |
| 53 | Telephones | FN6i-NT-TEL-LUK.pdf | 21 | ✓ | ✓ | ✓ | **✓ كامل (9 استعلامات — Guest Information لوحة العامل + In-House مفوَّضة لFO + Yellow Pages + View Transfers/Extensions بأثر User+Authorizer)** | **✓ → modules/telephone/** | – | – | – |
| 54 | Telephones | FN6i-NT-TEL-REP.pdf | 20 | ✓ | ✓ | ✓ | **✓ كامل (8 تقارير — P&T/Guest + Page Skip + Master List ثلاثي الأنماط + Unbilled)** | **✓ → modules/telephone/** | – | – | – |
| 55 | Telephones | FN6i-NT-TEL-CAC.pdf | 10 | ✓ | ✓ | ✓ | **✓ كامل (4 وظائف — 4 حالات خطأ + إعادة ترحيل Select-YES + مصفوفة تحويل + كلمة مرور بالإقامة)** | **✓ → modules/telephone/** | – | – | – |
| 56 | Maintenance | FN6i-NT-MNT-RPL.pdf | 29 | ✓ | ✓ | ✓ | **✓ كامل (15 تقريراً/استعلاماً — Complaint Status Q معدِّل + Print Engine + Parameter Listing إلى Excel)** | **✓ → modules/maintenance/** | – | – |
| 57 | Maintenance | FN6i-NT-MNT-OPR.pdf | 28 | ✓ | ✓ | ✓ | **✓ كامل (8 وظائف — Register/Action Taken بثلاث مسارات + 999999999999 + Job Order Generation بالألوان + PM بـLag)** | **✓ → modules/maintenance/** | – | – |
| 58 | Maintenance | FN6i-NT-MNT-SET.pdf | 24 | ✓ | ✓ | ✓ | **✓ كامل (12 قسماً — 7 ماسترات نمطية + موظفو هندسة خامس مخزن + أولويات ملونة + جسرا MGT + UDPF)** | **✓ → modules/maintenance/** | – | – |
| 59 | F&B Costing | FN6i-NT-FNB-REP.pdf | 28 | ✓ | ✓ | ✓ | **✓ كامل (13 تقريراً — Sales Analysis بميزانية±تباين يوم/شهر/سنة + Cost Report بـForecast/YTD + Standard vs Actual 80/132 عموداً + Buffet بطابعة)** | **✓ → modules/food-beverage-costing/** | – | – |
| 60 | F&B Costing | FN6i-NT-FNB-COP.pdf | 19 | ✓ | ✓ | ✓ | **✓ كامل (9 وظائف — استخراج ETL ثنائي Batch/Online + جرد يومي Pink/Green + تحويلات ثلاثية (قيمة بلا أصناف!) + ترحيل يومي/سنوي + Auto Indent خالد إلى MGT + INI#368/#511)** | **✓ → modules/food-beverage-costing/** | – | – |
| 61 | F&B Costing | FN6i-NT-FNB-LUK.pdf | 15 | ✓ | ✓ | ✓ | **✓ كامل (7 استعلامات — Profitability بـXOR منهجي وLink Help وNo-Drill-Down معلنة + NC Query ثلاثي المحاور + Consolidate للمكونات)** | **✓ → modules/food-beverage-costing/** | – | – |
| 62 | F&B Costing | FN6i-NT-FNB-SET.pdf | 14 | ✓ | ✓ | ✓ | **✓ كامل (4 أقسام — Costing Start Date أحادي الاتجاه + Costing Link ثلاثي بـSales Tag + ميزانيات انتشار جلسة السنة + Recipe/Sub Recipe بـ6 تابات)** | **✓ → modules/food-beverage-costing/** | – | – |
| 63 | (root) | Touch_Screen_Manual.pdf | 46 | ✓ | ✓ | ✓ | **✓ كامل (عمليات POS الفعلية: Shift/Outlet/KOT/Check/Split/Settlement/NC/Close)** | **✓ → modules/point-of-sale/** | – | – |
| 64 | Fixed Assets | FN6i-NT-FAS-FXD.pdf | 25 | ✓ | ✓ | ✓ | **✓ كامل (19 وظيفة: بوابة أحادية property-wise + هرمية 5 ماسترات + ربط GL رباعي BS×2/PL×2 + كود آلي 12=5+3+4 من FIMSHTBL + SLM/WDV بـINI#475 وحساب بمنهجين وترحيل SLM شهرياً بنهاية الشهر + أزرق=غير مربوط + Gain/Loss وتعطيل التساوي + بطاقة "لاحقاً")** | **✓ → modules/fixed-assets/** | – | – | – |
| 65 | Gate Passes | FN6i-NT-FAS-GTP.pdf | 13 | ✓ | ✓ | ✓ | **✓ كامل (7 وظائف — أضأف دليل: إصدار NOTE بثنائية Returnable + استلام جزئي ثلاثي المفاتيح + سجل مرتجع فقط + معلق as-on + طباعة بطابعة + Vendor Code/Name منفصلان!)** | **✓ → modules/gate-passes/** | – | – | – |

---

## استثناءات مسجلة

- **فهارس Care وTouch Screen:** استُخرجت بأنماط مختلفة ودقتها أقل — عولجت بقراءة الصفحات الأولى يدوياً. لا يوجد ملف ناقص.
- **لا توجد ملفات تتطلب OCR** — استثناء OCR غير مطلوب إطلاقاً.
- **مسار مجلد "Accounts Receivales"** فيه خطأ إملائي في المصدر الأصلي (Receivales بدل Receivable) — يُترك كما هو في المصدر ويُصحح في docs.
