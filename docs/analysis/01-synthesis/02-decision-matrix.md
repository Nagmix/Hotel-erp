# 02 — مصفوفة القرارات المجمعة (Consolidated Decision Matrix)

> **كل قرارات GAP-D/E عبر 16 وحدة + 4 وحدات تقارير** مجمّعة في مصفوفة واحدة — الغاية: رؤية القرار الواحد الذي يتكرر، والقرار العابر الذي يحسم عائلة كاملة، وأولويات ما يُحسم أولاً عند التنفيذ.
> الترقيم الأصلي محفوظ (GAP-XX-D##) — هذا الملف **فهرس القرارات** وليس بديل ملفات الوحدات (التفاصيل الكاملة في 17-gap-analysis لكل وحدة).

---

## 1. الإحصاء البنيوي

| النطاق | الوحدات | قرار D | قرار E (ERPNext) | قرار P (تشغيل) |
|---|---|---|---|---|
| الوحدات | 16 | ~100 | ~40 | ~60 |
| وحدات التقارير (Phase 7) | 4 | 28 | — | 20 |
| **الإجمالي** | **20 وحدة تحليلية** | **~128** | **~40** | **~80** |

> ملاحظة تدوينية: FO وFAS (الجلسات 1-3) استعملتا ترميز G/GE قبل استقرار اصطلاح GAP-XX-D — موحَّدتان هنا تحت نفس المظلة.

---

## 2. القرارات الحرجة P0 (تصنع أو تكسر التحويل)

> العشرة التي بلا حسمها لا يبدأ تنفيذ جاد — كلها عابرة للوحدات.

| # | القرار | المصدر القراري | الأثر عند التأجيل |
|---|---|---|---|
| **P0-1** | **Customer Credit Gate موحدة**: نقطة فحص واحدة تستدعيها FO/POS/BNQ/يدوي عند Credit Limit | UNK-051 → D-SM-2/F-SM-4 | قفل لا يعمل أو يعمل بأربع سلوكيات مختلفة |
| **P0-2** | **خريطة الترحيل الآلي الشاملة**: Journal origin أوسع من FOM/ACR/INV — يشمل HRP (رواتب) وFXD (F12) وMGT وBNQ | UNK-098 → GAP-FA-D04 | إيرادات تُرحَّل وأخرى تضيع (سيناريو FN6i الأصلي!) |
| **P0-3** | **Vendor واحد + Employee واحد**: Supplier يخدم MGT/MNT/FXD/GTP/BNQ · Employee يخدم FO/HRP/SLM/MNT/GTP | UNK-058 (امتدادات ×7) + UNK-038 (×6) | انفجار علاقات مرجعية في 11 وحدة |
| **P0-4** | **Report Permission Matrix إلزامية لكل طبقة REP** (~291 تقريراً بلا صلاحية عبر 4 وحدات + 8 وحدات بلا صلاحيات) | GAP-FOR/PR/MR/FA-D01 (القرار الموحد) | أمن فراغ على الشرطة/الضرائب/GL/TDS |
| **P0-5** | **Cancel-with-reversal إلزامي** لكل Rollback/حذف مؤثر على GL (أخطرها FXD) | UNK-071 → GAP-FX-D03 | دفاتر تحسب قيوداً محذوفة |
| **P0-6** | **بوابة 511 كاملة المواصفة**: أي رصيد يُفحص (FNB أم MGT) + سلوك رفض POS + قيمة افتراضية | UNK-063 → GAP-FB-D06 | حاجب بيع إما غائب أو يخنق البيع |
| **P0-7** | **Print Format مفتوح لكل موقع** بدل Pgm.ID لكل عميل | GAP-MR-D04/UNK-091 (قانون L2) | 6 تقارير موقوفة + كل المطبوعات بلا تخطيط |
| **P0-8** | **مركزية التكوين**: وثيقة Module Attributes & INI خارج الحزمة — تُعوَّض بجمع المرقمة (27 INI + 7 عائلات MA) في System Settings واحدة بدلالات إيجابية | GAP-SYS-D01 + GAP-TE-D07/ME-D05 | سلوكيات خفية بلا مالك |
| **P0-9** | **التقييم المخزني خاصية مخزن** (custom_rate_calc لكل Warehouse — WA حسابي أو FIFO/FEFO) | F-MG-1 (أصل التعارض مع ERPNext global) | تعارض مباشر مع نموذج التقييم الموحد |
| **P0-10** | **متعددية Property داخل قيد واحد** (Dimension + Company) | GAP-AR-E09 (القرار المعماري الأب) | كل القيود إما تنفجر أو تُبنى مرتين |

---

## 3. المصفوفة الكاملة حسب الموضوع

### 3.1 الصلاحيات والأمان (Permissions & Security) — 15 قراراً

| ID | الوحدة | القرار (مختصر) |
|---|---|---|
| GAP-CA-D01(P1) | Care | انفصال HRMS → Employee موحد + Checkin = Attendance حقيقية |
| GAP-SM-D04 | SLM | لا قسم صلاحيات إطلاقاً → P-SM-1..5 (أدوار مصممة) |
| GAP-TE-D03 | TEL | إعادة الترحيل فعل مالي بلا ضابط → صلاحية Operator+Authorizer |
| GAP-MN-D01 | MNT | Complaint Status يعدّل بلا ضابط → أدوار مستنتجة تعتمد |
| GAP-FB-D01 | FNB | Audit Date/Start Date/511/Auto Indent أفعال قفل بلا مالك |
| GAP-ME-D01(+P) | MEM | Membership Tax Posting شبح → يُستكمل Notification/لا شيء |
| GAP-FX-D06 | FXD | لا صلاحيات في وحدة ترحيلية (الأخطر) → أدوار ثلاثة |
| GAP-AR-D04 | AR | Rollback SOA/Cancel Invoice بلا تقييد → أدوار صريحة |
| GAP-POS-D05 | POS | افتراضي Allow/Deny لUser Access → قرار Deny default |
| GAP-GP-D02 | GTP | إعادة طباعة بلا إبطال → Status Printed بطابع + Auditor |
| GAP-FOR-D01 | FO-REP | 135 تقريراً بلا صلاحية → Matrix إلزامية |
| GAP-PR-D01 | POS-REP | ~57 بلا صلاحية → Matrix |
| GAP-MR-D01 | MGT-REP | ~53 بلا صلاحية → Matrix |
| GAP-FA-D01 | FAS-REP | 46 بلا صلاحية (Audit+TDS+GL!) → Matrix صارمة |
| GE-FA-05/FAS | FAS | Voucher Authorization ثلاث مستويات بلا تفصيل → تعريف أدوار المستويات |

### 3.2 المحاسبة وGL (Accounting) — 14 قراراً

| ID | الوحدة | القرار |
|---|---|---|
| G-FA-01/02 | FAS | قيود Tips (POS/AR) + Complimentary محاسبياً → قرارا قيمة صفر/مصروف |
| GAP-AR-D09 | AR | فائدة Aging بلا ترحيل → Dunning مع قيد |
| GAP-MG-D04 | MGT | توقيت MM→FAS (فوري/دفعة) → نمط دفعة + قرار |
| GAP-MG-D08 | MGT | فوائد تأخير المورد (شرائح 91-100 يوم=10%) → محرك FAS أم SLM؟ |
| GAP-MG-D11 | MGT | مصير Complimentary في الدفاتر → قيمة صفر قراراً |
| GAP-BQ-D08 | BNQ | قيد الوديعة/الغرامات → Payment Entry + Penalties |
| GAP-BQ-D07 | BNQ | توقيت BNQ→FAS → UNK-027/032 قرار دفعة |
| GAP-HR-D06 | HRP | JV التفصيلي → من FAS-TRN (Phase 6 حلّها) |
| GAP-TE-D02 | TEL | لا خريطة GL هاتفية → Revenue Codes من FO/FAS |
| GAP-MN-D02 | MNT | تكاليف جزيرة → MIS خالص أم Expense عند عتبة |
| GAP-FB-D02 | FNB | لا إقفال تحليلي → Audit Date + Period Closing للتقارير |
| GAP-ME-D02 | MEM | لا خريطة GL → عبر AR (مفوَّض) |
| GAP-FA-D04 | FAS-REP | HRP/FXD غائبان من Auto-Posted → origin أوسع (P0-2) |
| GE-FA-01 | FAS | undistributed→Suspense + re-process → تحقق مسبق (أفضل من الأصل) |

### 3.3 الكتالوغ والتكرارات (Catalog & Duplication) — 12 قراراً

| ID | الوحدة | القرار |
|---|---|---|
| GAP-AR-D01 | AR | «12123 PENDING» معلق → يوثق ميدانياً إن ظهر |
| GAP-BQ-D03 | BNQ | قوائم KOT-28/Settlement-15 → تستكمل من POS User Access |
| GAP-MR-D02 | MGT-REP | §1≡6.1 حرفياً + VAT≡Tax + قسم 6 مزدوج → دمج إلزامي (C-MR-01/02/03) |
| GAP-FA-D03 | FAS-REP | TB الثلاثة المتطابقة → تقرير واحد بوضعيات عرض (C-FA-02) |
| GAP-PR-D05 | POS-REP | Discount Register مزدوج → دمج §12 + مرشح §6.1 (C-POS-01) |
| GAP-MR-D05 | MGT-REP | R2 Variant → دمج/إبقاء (UNK-089) |
| GAP-HR-D02 | HRP | لا ملف LUK → بطاقة موظف موحدة |
| GAP-FA-D02 | FAS-REP | شبحا IDS Crystal+iDesigner → Report Builder (قانون القالب L8) |
| GAP-FOR-D04 | FO-REP | Report Designer + IDS Crystal → Report Builder مفتوح |
| GAP-PR-D04 | POS-REP | KDS §24 شبح → KOT Display عند الحاجة (F-PR-15) |
| GAP-TE-D01 | TEL | SMS المعيارية شبح → Notification قالب عند CI/ذكرى |
| GAP-ME-D01 | MEM | Membership Tax Posting شبح → يوثق كأثر بلا بناء |

### 3.4 الطباعة والإخراج (Print & Output) — 10 قرارات

| ID | الوحدة | القرار |
|---|---|---|
| GAP-AR-D02 | AR | Print Form Designer يحيل لGetting Started (خارج الحزمة) → Print Format Builder |
| GAP-POS-D03 | POS | Print Report Options من Getting Started → Print Format |
| GAP-ME-D06 | MEM | كروت العضوية بلا شاشة → Print Format تصميم جديد |
| GAP-HR-D04 | HRP | Print Program IDs بلا بنية → طباعة مخصصة |
| GAP-FOR-D05 | FO-REP | Export بلا صيغة → XLSX/CSV قراراً |
| GAP-FOR-D06 | FO-REP | تحرير INI/ملفات على الخادم لمستخدم أعمال → Print Format من الواجهة |
| GAP-FOR-D07 | FO-REP | الطباعة الفيزيائية قناة أولى → رقمنة العرض |
| GAP-FA-D06 | FAS-REP | مسار Outlook+Broadgun+PDF-أحمر → بريد خادم قياسي |
| GAP-FA-D07 | FAS-REP | ورق 11/12 IN hard-coded → Print Format مخصص |
| GAP-MR-D06 | MGT-REP | كل التخطيطات غائبة → أعمدة تُستكمل تصميماً |

### 3.5 التواريخ والأرشفة (Dates & Archiving) — 8 قرارات

| ID | الوحدة | القرار |
|---|---|---|
| GAP-FOR-D02 | FO-REP | month-boundary ×15 → نطاق حر + افتراضات |
| GAP-PR-D02 | POS-REP | same-month ×25 → نطاق حر |
| GAP-FOR-D03/PR-D03 | FO+POS | XOR 80/132 المعكوس → يُهجر (YTD دائماً) |
| GAP-SYS-D04 | SYS | انتهاء كلمة المرور → سياسة صريحة (UNK-023) |
| GAP-SYS-D05 | SYS | قيد سعر الصرف الرابع → سلوك رفض/استبدال |
| GAP-FB-P01 | FNB | بوابة تفعيل بلا طريق رجعة → Singleton + قرار إدارة |
| GAP-FX-P01 | FXD | لا تصحيح Start Date → نفس النمط |
| GAP-ME-D03 | MEM | Event بلا جسر BNQ → تحقق توفر القاعة (UNK-046) |

### 3.6 التكاملات والجسور (Integrations) — 12 قراراً

| ID | الوحدة | القرار |
|---|---|---|
| GAP-CA-D01 | Care | لا فوترة للمهام → المرشح FO Folio |
| GAP-CA-D04 | Care | IVR صندوق أسود → قناة حديثة |
| GAP-CA-D05 | Care | بوابة SMS بلا مواصفة → Gateway مركزي (UNK-082 عائلة) |
| GAP-MN-D05 | MNT | لا جسر Equipment↔FXD → Asset موحد |
| GAP-GP-D04 | GTP | الجسر المخزني الغائب (material transfers نصاً!) → ربط اختياري |
| GAP-ME-D04 | MEM | فوترة عضو F&B → POS-side (حُسم في POS المقروء) |
| GAP-POS-D08 | POS | تسلسل Close↔DayEnd↔Post → قرار ترتيب صريح |
| GAP-POS-D06/D07 | POS | Guest Settlement لغرفة غير موجودة + إدخال CC يدوي → تحقق + خيار بصلاحية |
| GAP-SM-D01 | SLM | مصدر Market Share (comparative entry غير موجود!) → تصميم شاشة (UNK-049) |
| GAP-SM-D07 | SLM | ملكية Company Profile المزدوجة (SLM vs ACR) → Customer واحد |
| GAP-MG-D09 | MGT | مورد Black List بلا قيد PO → تحقق |
| GAP-TE-D06 | TEL | 2-Way بلا وظائف (wake-up/voice mail) → قرار نطاق |

### 3.7 التكوين والمفاتيح (Configuration) — 10 قرارات

| ID | الوحدة | القرار |
|---|---|---|
| GAP-SYS-D01 ⭐ | SYS | وثيقة MA&INI خارج الحزمة → جمع المرقمة (مصفوفة KG §4) |
| GAP-SYS-D02/D03 | SYS | Getting Started غائب + §19 هامشية → توثيق بديل |
| GAP-MG-D01 | MGT | تعارض ترقيم SPO (8 أم 5) → بالاسم النصي |
| GAP-MG-D02 | MGT | Stop Payment معكوس التسمية → تسمية عربية صريحة |
| GAP-TE-D04 | TEL | Others نسبة أم مبلغ → حقلان منفصلان |
| GAP-TE-D05 | TEL | SPL بلا ماستر → قرار تصنيف |
| GAP-FB-D07 | FNB | قوائم NC/Session/Menu/KOT بلا مالك → ماسترات POS/SYS |
| GAP-BQ-D04 | BNQ | INI 346 بلا دلالة → حقل صريح |
| GAP-HR-D03 | HRP | PYINDSP مغلق (هنود فقط) → قاعدة شرائح ESI |
| GAP-MN-D07 | MNT | ENG ناقصة (2/؟) → فهرسة كاملة عند SYS النهائي |

### 3.8 كيانات مرجعية وجودة بيانات (Reference & Data Quality) — 9 قرارات

| ID | الوحدة | القرار |
|---|---|---|
| GAP-MN-D04 | MNT | Vendor غائب (UNK-058 الأول) → Supplier موحد |
| GAP-FX-D05 | FXD | نفس العائلة سادساً → نفس الحسم |
| GAP-GP-D03 | GTP | انفصال Vendor Code/Name → fetch آلي |
| GAP-MN-D03 | MNT | Status خيارات صورية → الثلاثي المستنتج (P/W/C) |
| GAP-HR-D07/D08 | HRP | Non Employee غامض + تفرد Employee# → تعريف + unique |
| GAP-ME-D07 | MEM | تفرد رقم العضوية اليدوي → unique constraint |
| GAP-GP-D05 | GTP | لا قاعدة إغلاق اكتمال → اكتمال تراكمي محسوب |
| GAP-BQ-D05/D06 | BNQ | Coupons مزج + تعديل Function Room → قواعد صريحة |
| GAP-SYS-D06/D07 | SYS | حقول ميتة (Card File/Conversion Id) + لا حذف مستخدم → حذف/تعطيل+أرشفة |

---

## 4. جدول المرجع السريع (Quick Reference)

| الوحدة | ملف القرارات | النطاق |
|---|---|---|
| FO | modules/front-office/17 | G-1..G-14 + GE-FO |
| POS | modules/point-of-sale/17 | GAP-POS-D01..D11 |
| FAS | modules/financial-accounting/17 | G-FA-01..08 + GE-FA-01..06 |
| ACR | modules/accounts-receivable/17 | GAP-AR-D01..D10 + E01..E10 |
| MGT | modules/materials-management/17 | GAP-MG-D01..D12 |
| BNQ | modules/banquets/17 | GAP-BQ-D01..D11 |
| HRP | modules/hrp-payroll/17 | GAP-HR-D01..D11 + E01..E12 |
| SLM | modules/sales-marketing/17 | GAP-SM-D01..D07 |
| MEM | modules/membership/17 | GAP-ME-D01..D07 |
| TEL | modules/telephone/17 | GAP-TE-D01..D07 |
| MNT | modules/maintenance/17 | GAP-MN-D01..D07 |
| FNB | modules/food-beverage-costing/17 | GAP-FB-D01..D07 |
| FXD | modules/fixed-assets/17 | GAP-FX-D01..D06 |
| GTP | modules/gate-passes/17 | GAP-GP-D01..D05 |
| Care | modules/care/17 | GAP-CA-D01..D07 |
| SYS | modules/system-setup/17 | GAP-SYS-D01..D08 |
| FO-REP | reports/front-office/11 | GAP-FOR-D01..D07 |
| POS-REP | reports/point-of-sale/11 | GAP-PR-D01..D07 |
| MGT-REP | reports/materials-management/11 | GAP-MR-D01..D07 |
| FAS-REP | reports/financial-accounting/11 | GAP-FA-D01..D07 |

---

## 5. القرارات ذات الأولوية في الحسم (Closing Order)

> ترتيب الحسم المقترح عند بدء التنفيذ (Phase 9+):

1. **P0-10 ← P0-3 ← P0-2**: البنية (Property multi + الكيانات + خريطة الترحيل) — لا يُبنى شيء قبلها.
2. **P0-4 + P0-5**: الأمان (Matrix + reversal) — قبل أي بيانات حقيقية.
3. **P0-9 + P0-6**: محرك المخزون + البوابة — قبل تحويل MGT/FNB/POS.
4. **P0-1 + P0-7 + P0-8**: قنوات العمل (Credit Gate + Print + Config) — قبل FO/BNQ.
5. بعدها تُحسم قرارات الوحدات بترتيب أنقى التواءم أولاً (FXD → GTP → FNB/Recipe → MNT/Issue) كمسارات إثبات المفهوم.
