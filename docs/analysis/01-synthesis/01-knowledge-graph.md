# 01 — Knowledge Graph النهائي (Phase 8 — المراجعة الشاملة)

> **المرجع الجامع لكل المعرفة المعمارية العابرة للوحدات** المستخرجة من قراءة الـ65/65 ملفاً بعمق.
> المصادر: 16 مجلد وحدات (306 ملفاً) + 4 مجلدات تقارير (48 ملفاً) + سجلات التتبع (unknowns 102 · contradictions 12).
> هذا الملف هو **خريطة المعرفة الموحدة** التي تحلّ محل البحث المتناثر عبر الوحدات — كل عائلة عابرة تُوثَّق هنا مرة واحدة بمواقعها كلها.

---

## 1. البنية الطوبولوجية للنظام (System Topology)

### 1.1 الطبقات الخمس

```
┌────────────────────────────────────────────────────────────────────┐
│ الطبقة التأسيسية (Root)                                             │
│   SYS (المستخدمون/الخصائص/INI/الترميز) — الجذر الذي يعرّف الجميع    │
├────────────────────────────────────────────────────────────────────┤
│ الطبقة التشغيلية الأمامية (Front Operations)                        │
│   FO (القلب الفندقي) · POS · BNQ (فوق محرك POS) · TEL · CRG        │
├────────────────────────────────────────────────────────────────────┤
│ الطبقة الوسيطة (Intermediate Engines)                               │
│   ACR (مركز AR) · SLM (مستودع الشركات/العملاء) · MEM · Care        │
├────────────────────────────────────────────────────────────────────┤
│ الطبقة الخلفية (Back Office)                                        │
│   MGT (مركز المخزون) · FNB (OLAP تكاليف) · MNT · FXD · HRP · GTP   │
├────────────────────────────────────────────────────────────────────┤
│ الطبقة المالية (Financial Core)                                     │
│   FAS — نقطة التقاء كل الجسور المالية (GL) + طبقة النزاهة التكاملية │
└────────────────────────────────────────────────────────────────────┘
```

### 1.2 درجات الاتصال الموثقة نصاً (من ملفات 12-integrations لكل وحدة)

| الوحدة | جسور خارجة (Out) | جسور داخلة (In) | الدور الطوبولوجي |
|---|---|---|---|
| **FAS** | إلى الجميع مالياً (طبقة النزاهة §19/20/21 تراقب) | من FO/POS/ACR/MGT/BNQ/FXD | **الحوْب المالي** — أعلى درجة |
| **FO** | FAS (FOM) · TEL (ثنائي) · SLM · ACR · BNQ · HSK | من TEL/SLM/Care/POS (City Ledger) | **الحوْب التشغيلي** |
| **MGT** | FAS (ترحيل) · FNB/BNQ (استهلاك) · MNT (استعارة) | من FNB/BNQ (Auto Indent) · FXD (شراء أصول) | **حوْب المخزون** |
| **POS** | FAS (FOS/POS-to-Finance) · ACR · FO (غرف) | من SLM (خصومات) · MEM (MemberDiscount) · FNB (بوابة 511!) | محرك إيراد + **مُقاد سلوكياً من FNB** |
| **BNQ** | MGT (Auto Indent) · FAS · ACR | من SLM (عقود) · FO (بلوكات) | فوق POS — جسر إيراد↔مخزون |
| **ACR** | FAS (Acr2Fas INI 56) | من FO/POS/BNQ/MEM | **محطة AR الوسيطة** |
| **HRP** | FAS (JV — غير موثق النوع! UNK-098) | من AR (تحويلات موظفين §22) | ED engine + إشكالية عزلة الترحيل |
| **SLM** | 7 وحدات تستهلك Company Profile | من FO (شركات) | **مستودع كيان العميل** |
| **TEL** | FO (فوليو) · FAS (P&T) | من FO (إشغال ثنائي الاتجاه) | جسر عتاد (EPABX/Onity) |
| **FNB** | MGT (Auto Indent خالد) · POS (بوابة 511) | من MGT (استهلاك) | **OLAP فوق OLTP** |
| **FXD** | FAS (F12 شهري SLM) | من MGT (Capital Goods Receipt) | أنقى تطابق ERPNext |
| **MEM** | AR (فوترة) · POS (خصم) | من SLM (شركات) | أرصدة ائتمانية |
| **Care** | SMS/PMS فقط | لا أحد يستهلكها رقمياً | **جزيرة مهام** (منفصلة عن HRMS) |
| **MNT** | استعارة فقط (MGT/SLM) | لا جسور رقمية موثقة | **الجزيرة المعزولة** (تستعير ولا تُستلف) |
| **GTP** | لا أحد | لا أحد | **الجزيرة الورقية — صفر درجة** |
| **SYS** | يُعرّف الجميع | — | الجذر |

### 1.3 القانون الطوبولوجي الأعظم

> **كل إيراد يصبّ في FAS، وكل مخزون يخرج من MGT، وكل كيان مالي/ائتماني يمرّ عبر ACR/SLM — لكن لا شيء يصعد من GTP ولا ينزل إليها.**
> الطبقة المالية لا تثق بالوحدات: بنت **طبقة النزاهة التكاملية** (FAS-REP §19/20/21: Unlinked/Linked/Auto-Posted) لتراقب نفسها ضد الجميع — الجواب النظامي على سؤال «كيف يضمن FN6i عدم ضياع الإيراد بين الوحدات؟»

---

## 2. الجسور الموحدة (Unified Bridge Registry)

> المرجع المصدر الحاسم: **FAS-REP §19/20/21** (أسماء معاملات الربط المسربة) + FAS-TRN (أنواع الترحيل). انظر جدول المرادفات §C-FA-01 في `03-synonyms-glossary.md` — التسميات الثلاث للجسر نفسه موثقة هناك.

### 2.1 الجسور المالية (الموثقة أنواعها رسمياً في Auto Posted Check List)

| الجسر | نوع الترحيل الرسمي | التوقيت الموثق | الحالة |
|---|---|---|---|
| FO → FAS | **FOM** (يشمل "Front Desk **and** Point of Sale"!) | بعد Day End — Effective Date = اليوم السابق | ✅ موثق كاملاً |
| POS → FAS | ضمن FOM (تسمية FOS-to-FA في §20 — مرادف) | مع إغلاق المنفذ/الوردية | ✅ موثق |
| ACR → FAS | **ACR** (Acr2Fas — INI 56: 0=مكّن، الافتراضي 1=معطل!) | فوري بالحسابات المرتبطة | ✅ موثق + مفتاح معكوس |
| شراء → FAS | **INV** (طرق محاسبة ضريبة الشراء INV Switches 1/3/4) | مع الاستلام (PJV — UNK-092) | ✅ موثق |
| MGT → FAS | غير مدرج كنوع مستقل — التوقيت مجهول (GAP-MG-D04) | غير موثق | ⚠️ فجوة |
| BNQ → FAS | غير مدرج كنوع — الودائع Vouchers بلا بنود (GAP-BQ-D08) | غير موثق (UNK-027/032) | ⚠️ فجوة |
| **HRP → FAS** | **غائب من الأنواع الثلاثة!** (UNK-098 — يلامس UNK-010 الأصل) | مجهول | ⚠️ **أخطر فجوة خريطة** |
| **FXD → FAS** | **غائب رغم F12 الشهري الموثق!** (UNK-098) | الشهر بإهلاك SLM بنهايته | ⚠️ تناقض خريطة |
| TEL → FO/FAS | فوليو + Revenue Codes لكل نوع · P&T بلا قيد موثق | مع الفوليو | ◐ جزئي |
| FNB | صفر قيود OLAP — كل الأثر مفوَّض | — | ✅ بحكم التصميم |

### 2.2 الجسور السلوكية (غير مالية — أندر وأخطر)

| الجسر | النمط | المصدر |
|---|---|---|
| **FNB → POS (بوابة 511)** | حاجب بيع لحظي: POS يرفض البيع حين نفاد رصيد KOT — قرار من وحدة أخرى بمفتاح بلا مالك موثق في POS نفسه! | FNB-COP ص3 (UNK-063) |
| **BNQ → MGT (Auto Indent)** | WS Finalize → indent تلقائي بWork Sheet# + Department/CC → الوصفة تنفجر indent | BNQ-BIL §13 (UNK-011 محسوم) |
| **FNB → MGT (Auto Indent الخالد)** | الاستهلاك الكلي للوصفة → indent دائم | FNB-COP |
| **MGT DPR/Re-Order → PR** | nil balance / reorder level → Requisition آلي | MGT-SET (A-MG-01/02) |
| **SLM → FO/POS/BNQ (القفل الائتماني الثلاثي)** | منع تسوية/ترحيل يدوي عند تجاوز Credit Limit — من ثلاث وحدات + يدوي | SLM-PRF §7 (UNK-051) |
| **FO ↔ TEL (ثنائي الاتجاه)** | إشغال FO يعرضه TEL + تسعير/بوابات ترجع للفوليو | TEL-SET Link |
| **Care → PMS (استيراد CI/CO حتى سجل البند!)** | Drilldown يصل لسجل بCI/CO من PMS — أعمق قراءة عكسية موثقة | Care-REP |
| **FO ↔ BNQ (بلوكات/حجز الحاجب التقويمي)** | Block/allowed/made-by | BNQ-SET |

### 2.3 الجسور الورقية (Physical Bridges — موثقة نصاً!)

| الجسر | الوثيقة | المصدر |
|---|---|---|
| **GRN نسخة → Finance للدفع** | «a copy of the GRN is forwarded to the Accounts department for making payments» | MGT-REP 15.6 |
| GTP → الطابعة (وثيقة أمنية بلا مسار رقمي) | printer type من قائمة | GTP ص10 |
| KOT Books الورقية (دفتر كأصل!) | issued-to/date/used-unused-void | POS-REP 17.1 |

---

## 3. العائلات العابرة الموحدة (Unified Cross-Module Families)

> **20 عائلة معمارية** ظهرت عبر القراءة العميقة وتكررت في أكثر من وحدة — موثقة هنا نهائياً بأعضائها الكاملين وقانونها الحاكم.

### 3.1 عائلة الصلاحيات الصفرية (Zero-Permissions Family) — **12/17** ⚠️ الحاكمة

| الطبقة | الأعضاء | الدلالة |
|---|---|---|
| وحدات كاملة بلا صلاحيات | **CARE · MEM · SLM · TEL · MNT · FNB · FXD · GTP** (8) | لا قسم User Rights واحد في أي ملف |
| طبقة تقارير REP بلا صلاحيات | **FO (135) · POS (~57) · MGT (~53) · FAS (46)** — مجموع **~291 تقريراً** | الوحدات نفسها *تملك* صلاحيات لكن طبقة تقاريرها لا تذكر Role واحدة |
| الاستثناء الموثق | HRP (Payroll User Rights داخل SET) · SYS (Define Rights) · POS (User Access ×20+ شاشة) · FO (سلوكيات) · FAS (Voucher Auth 3 مستويات) | النمط: الصلاحية تسكن **داخل** الوحدات التراثية وتغيب عن الحديثة |

**القانون:** كل وحدة حديثة (post-FAS) وُلدت بلا نموذج أمان؛ وكل طبقة REP في الحزمة كلها بلا صلاحيات. قرار إعادة البناء: Report Permission Matrix إلزامي (GAP-*-D01 الموحد).

### 3.2 عائلة صفر قيود GL (Zero-GL Family) — نمطان مختلفان

| النمط | الأعضاء | الآلية |
|---|---|---|
| **صفر بالتفويض** (منظم) | SLM (كل الأثر لAR/FO) · MEM (posted to AR) · TEL (فوليو FO) | الإيراد يُرحَّل من وحدة أخرى رسمياً |
| **صفر بالعزل** (جزيرة) | **MNT** (بلا تفويض أصلاً!) · **FNB** (OLAP فوق OLTP بأرقام مالية!) · **GTP** (ورقة كمية) | لا قيد ولا تفويض — أرقام بلا دفاتر |

**القانون:** الوحدة قد تكون غنية مالياً (FNB: Standard/Actual/تسويات قيمية) وتظل بلا قيد واحد — FN6i يفصل **المعرفة المالية** عن **المحاسبة** فصلاً صريحاً.

### 3.3 عائلة مخازن الموظفين المتعددة (UNK-038) — 6 امتدادات

| الامتداد | الوحدة | الشكل |
|---|---|---|
| الأصل | FO (Waiter/Department codes) | ماستر داخلي |
| 2 | HRP (Employee ED engine) | الموظف الرسمي |
| 3 | SLM (Sales/Collection Executives في FO Setup!) | ثالث بلا جسر HRP |
| 4 | MNT (Define Employees — 7 رقمي) | خامس مخزن |
| 5 | FXD (لا أحد — عبر Vendor؟) | سلبي |
| 6 | GTP (Authorized By أسماء حرة) | نص حر |

**الحسم التنفيذي:** Employee واحد (ERPNext) يخدم الجميع — القرار المعماري F-SM-2/F-MN الموحد.

### 3.4 عائلة المورد بلا موطن (UNK-058) — **7 امتدادات (أطول عائلة)**

MNT (الأول: Equipment/PM/Job Order/Cost) → SLM → FXD (سادس) → GTP (سابع: Code اختيار + Name يدوي يصبح مفتاح بحث!) — والموطن المرجح دائماً: **ماستر موردو MGT**.

**الحسم التنفيذي:** Supplier واحد (ERPNext) يخدم MGT/MNT/FXD/GTP/BNQ — قرار نهائي منذ الجلسة 15.

### 3.5 عائلة الخلود الزمني (Temporal Immortality) — 4 أعضاء

| الوحدة | السجل الخالد |
|---|---|
| HRP | شرائح ED (لا تعديل — سجل جديد بنفس الكود) |
| MEM | أسعار العضويات (Applicable From الأحدث يفوز) |
| BNQ | الأسعار التعاقدية |
| TEL | شرائح الاتصال (خلود تام + مثال 2011/2012) |

**القانون:** التغيير السعري/القاعدي لا يُعدَّل — يُصدَّر: سجل جديد يتفعّل بApplicable From وهو النمط الرابع للتوريخ (بلا versioning حقيقي).

### 3.6 عائلة مفاتيح INI (27+ مفتاحاً موثقاً) — انظر §4 للمصفوفة الكاملة

النمط الحاكم: INI files تُنشأ من **N6IRPRP.BAS** (ملف مرخّص جزء من المنتج!) بNotepad — «carefully... Else, there could be functionality issues» + التحذير الأعلى في SYS: يُفعَّل فقط بعد فهم كامل من System Administrator **بموافقة الجهة المختصة**.
عائلة **بلا INI** المقابلة: CARE · MEM · SLM · TEL · MNT (خمسة — تُدار بModule Attributes/Singletons) — الفجوة الحرجة: وثيقة «Module Attributes & INI Settings» **خارج الحزمة** (GAP-SYS-D01).

### 3.7 عائلة 80/132 (عرض الطباعة) — **متقلبة الاتجاه** ⚠️

| الوحدة | دلالة 132 عموداً | الدلالة |
|---|---|---|
| FO | **تحذف** YTD (Night Report: 132 بلا خيار YTD!) | سلوك طرح |
| POS | **تضيف** مبالغ + نوع خامس Others + Total | سلوك إضافة |
| FAS | **XOR اقتراني**: Zero-Suppress × 132 مقترنان إجبارياً | اقتران |
| HRP | 80/132 + DBF + userId-dotted | إرث تقني |

**القرار الموحد (GAP-FOR-D03/PR-D03):** يُهجر النمط كلياً — عرض واحد متجاوب مع YTD دائماً.

### 3.8 عائلة الأشباح (Ghost Functions) — 7 أشباح موثقة

| الشبح | الموطن | الحالة |
|---|---|---|
| Membership Tax Posting | MEM-MTR فهرس #11 بلا متن | أول فهرس-بلا-جسم (UNK-045) |
| SMS المعيارية | TEL-CAC مقدمة بلا قسم (بلا جسم في أي ملف) | ثانية (UNK-054) |
| KDS §24 | POS-REP عنوان يغلق الملف بلا كلمة | ثالث (UNK-083) |
| IDS Crystal Report Designer | **FO + FAS معاً** (متكرر عبر وحدتين!) | رابع (UNK-078/096) |
| Advice/Cheque iDesigner | FAS-REP TOC تحت §34 | خامس (UNK-096) |
| Report Designer | FOM-REP TOC بلا متن | سادس |
| «12123 PENDING» | ACR-RPL تقرير 13 — عنصر نابع بلا وظيفة | سابع (GAP-AR-D01) |

**القانون الحاسم:** تكرار IDS Crystal عبر FO+FAS + الشبحين الختاميين لFAS = **شبه إثبات قوالب TOC منسوخة عبر الوحدات** — الحزمة وُلدت من قوالب مشتركة والأشباح بقاياها.

### 3.9 عائلة Format-2/R2 (لاحقة التخطيط)

| العضو | الموطن |
|---|---|
| R2 (Group Consumption Month Range-R2) | MGT-REP 5.4 — أول لاحقة إصدار في اسم تقرير |
| TB Format 2 | FAS-REP §9 |
| Day Book Format 2 | FAS-REP (مثال A008000/SBI Frankfurt/USD) |
| TB (3.3) — إحالة ذاتية | FAS-REP — أوصاف متطابقة ×3 (C-FA-02) |

### 3.10 عائلة Print Forms عبر FAS (قانون الطباعة الأعظم) ⭐

> **قانون Print Forms:** طباعة PO/SPO/GRN (MGT) وBalance Confirmation/Advice/Voucher (FAS) **تتطلب Program Name معرَّفاً في FAS-SET §15 Pgm.ID** — «customized programs developed for each client... pre-printed or plain continuous or cut stationery».

هذا القانون **يفسر غياب كل تخطيطات المطبوعات في الحزمة الـ65 كلها**: الطباعة = طبقة كود لكل تثبيت، خارج الوثائق بتصميم. القرار: Print Format مفتوح (HTML/Jinja) لكل موقع (GAP-MR-D04).

### 3.11 عائلة Tag-YES (نمط الإخفاء/التجميع)

| الموطن | السلوك |
|---|---|
| MNT (Complaint) | Tag → YES يخفي من Guest Page Messages |
| MGT | Tag في Re-Order/DPR |
| FAS | Tag/Load pattern ×4 (UnTag/TagAll/UnTagAll أزرار!) |
| ACR | Untagging في المطابقة |

### 3.12 عائلة المحذوفات (Deletions Audit) — أوسع نطاق تدقيق

- **MGT-REP Audit Trial** («Trial» بدل Trail — خطأ منسوخ عبر وحدتين مع FAS!): يعرض **السجلات المحذوفة** — أوسع نطاق تدقيق في الحزمة.
- FAS-REP §2/§2(2)/§33: Transaction Checklist بمثال Doc#+Delete Transaction + Audit Trail.
- POS: Bill Audit بإعادة تسوية بزوج **mode+amount قديم→جديد** (أكمل old/new) + Cancelled bills تعرض أرقام البديلة.
- HRP: Payroll Audit بقيم old/new.
- FO: Audit ×8 بأثر المستخدم المخوّل + Watch List بذاكرة unmarking.

### 3.13 عائلة بوابات التاريخ (Date Gates) — مصفوفة عابرة للتقارير

~25 قاعدة في FO + ~20 في POS + بوابات MGT الثلاث الجديدة (current-only ×2 · **data-gated** للجرد!) + past-only ×4 في FAS (TB) + Happy Hours **التقرير المستقبلي الوحيد** (POS) — التوزيع النهائي: عائلة same-month (~25 تقريراً في POS!) هي أشدها تقييداً.

### 3.14 عائلة الألوان كلغة حالة (Colors as State)

| الوحدة | الاستخدام |
|---|---|
| MNT | أولويات الشكاوى الملونة F1 (أول كانبان بصري) |
| FXD | **أزرق = غير مربوط** (استثناء ترحيل) |
| BNQ | Availability Chart بألوان الحالة (INI 408) |
| MNT | ألوان الأولوية في Job Order Generation |
| POS/FO | First/Last/Day-Use ألوان الحالة |

### 3.15 عائلة الشراكات الدفاعية (قيم الهروب المطلقة)

- **TEL**: LCA + **9999999999 ×3** بأنماط أعلى IDD/STD — حماية الإيراد بأغلى تعرفة للمجهول.
- **MNT**: **999999999999** (12 تسعة) لشرِكة الصيانة المفتوحة — صنف بلا أثر مخزني.
- **BNQ**: قيم block/release الدفاعية.

### 3.16 عائلة التسريب البنيوي (Structural Leaks) — أصول أسماء الملفات/الجداول

| التسريب | المصدر | الدلالة |
|---|---|---|
| **FIMSHTBL** | FXD (توليد كود الأصل 12=5+3+4) | اسم جدول الشاشة الرئيسية الحقيقي |
| **PMSPOL.INI → POL.SPC** | FOM-REP (شرطة) | ملف تخصيص في dll folder — طبقة ملفية ثالثة |
| **N6IRPRP.BAS** | SYS (مصدر إنشاء INI) | ملف Basic مرخّص — مصدر المفاتيح |
| dll folder | موضع .SPC | بنية نشر Windows |
| Program IDs (FOMRR15) | FO-REP | اصطلاح ترميز برامج التقارير |
| FOMRR Pattern + PT/LWF Defn | HRP | نفس الاصطلاح |

### 3.17 عائلة إصدارية 2.0 (الأثر الجيولوجي)

«**Fortune Next Enterprise 2.0**» في FOM-SMS + ACR-RPL («Fortune Enterprise 2.0») مقابل «FN6i-» في الـ65 كلها — بقايا حقبة تحريرية (C-FO-02): وحدة SMS والطبقة النصية لACR أقدم من بقية الحزمة.

### 3.18 عائلة الوعد المستقبلي (Future Promises)

- FXD: بطاقة الدفع ببطاقة ائتمانية «**will be provided later**»
- POS: Module Attributes خارج الحزمة «refer Module Attributes & INI Settings documents»
- HRP: عقد بائع الحضور (IDS Bangalore خطاباً!)
- MEM: KOT/Settlement lists «displayed» بلا تعداد

### 3.19 معجم التسويات والرموز الموحد (Settlement Lexicon)

انظر الملف الكامل: `03-synonyms-glossary.md` — يحوي: ADQ/ADC/ADV/POT (FO pay modes) · Staff/others (POS settlement) · City Ledger («bills debited to his Company») · Credit («other than Cash, Void, Complimentary and NC») · (V)/(C) markers · CGR/NON-CGR · FOM/FOS/POS/FO/FA (جسر واحد بثلاثة أسماء!) · Sub/SL/Sub Ledger/Sl. Name · Transfer/Extension (TEL) · Trial/Trail.

### 3.20 عائلة Config-per-Report (مصفوفة POS Report Options)

أول نمط إعداد لكل تقرير (Void/Complimentary flags لكل تقرير عبر SETUP) + Invariant الحرفي المتكرر ~25 مرة («details will appear... NOT be included in the grand total») — أعلى تكرار قاعدة واحدة في الحزمة. يقابلها Tag/Load ×4 في FAS.

---

## 4. مصفوفة INI/Module Attributes الكاملة (27 مفتاحاً + 6 عائلات سمات)

### 4.1 مفاتيح INI المرقمة الموثقة

| # | الوحدة | الوظيفة | الملاحظة الحاسمة |
|---|---|---|---|
| 39 | MGT | طول كود الصنف (افتراضي 12) | يُجمَّد — يعدّله **IDS Customer Service Engineers فقط** |
| 41 | SLM | Week/Day Access للوكلاء | **معكوس**: 0=تفعيل! (مزدوج مع Attribute #8) |
| 56 | ACR→FAS | Acr2Fas | **معكوس**: 0=مكّن، الافتراضي 1=معطل! |
| 58 | FO | Reservation Mode | 0 لتفعيل |
| 63 | FO-REP | **أول Playlist**: Program IDs بفواصل (FOMRR15) لطباعة دفعية | UNK-080 |
| 64 | FO | Clear Room# بعد Save التسوية | سلوك نافذة |
| 74 | ACR | تعديل AR بعد الطباعة | 0=يسمح |
| 131 | MGT | SubCostCentre | مع E-MG-22 |
| 137 | POS-REP | **PAN prescribed limit** | «applicable only for Indian Government» — عتبة بلا قيمة (UNK-085) |
| 220 | HRP | Leave Group Parameter | S-HR-15 |
| 239 | SLM | رؤية Exec Planner (owner-only) | يقابلها قرار role setting |
| 245 | MGT | BarcodeLink (صنف+منفذ) | مع E-MG-08 |
| 283 | FO | الاستهلاك | QA-2 |
| 335 | POS-REP | **F&B Factor %** على شاشة التقرير | يقلب تصنيف Menu Engineering كله (UNK-086 — المثال 70%) |
| 346 | BNQ | تعديل قيمة | دلالة غير مؤكدة (GAP-BQ-D04) |
| 355 | MGT | PRAuthorization (مستويات 1-3) | E-MG-37 |
| 368 | FNB | **ONLINEFBCOSTING** | =1 → نقل Online من Inventory إلى Costing بلا استخراج يدوي |
| 404 | POS | MemberDiscount نطاق | 1=رئيسي فقط / 0=رئيسي+ثانوي |
| 408 | BNQ | حالات Availability Chart المعرفة | 0=الافتراضي/1=مخصصة |
| 409 | BNQ | بنى الضرائب في الحجز | تعرض حسب تعريف المفتاح |
| 475 | FXD | **اختيار SLM مقابل WDV** | بلا قيم ولا قاعدة انتقال (GAP-FX-D04) — WDV يُحسب ولا يُرحَّل! |
| 504 | FAS | ترقيم الشيكات التلقائي | 0=تفعيل |
| 511 | FNB | **autodeductionliqsale** | حاجب POS بيع عند نفاد الرصيد — اسم يوحي بالخمر ونص عام (UNK-063) |
| INV 1/3/4 | FAS | طرق محاسبة ضريبة الشراء | Switches مستقلة |
| FAS 4 | FAS | مفتاح FAS | — |
| SPO 8/5 | MGT | SPO/Direct — **تعارض ترقيم** (8 أم 5؟) | GAP-MG-D01 |
| Module Attributes | POS-REP | Void/Comp لكل تقرير | عائلة 3.20 |

### 4.2 عائلات Module Attributes

| العائلة | الحجم الموثق | المصدر |
|---|---|---|
| FO | Attr 1-67 (جرد فهرسي فقط!) | FOM-SET §4 |
| POS | 3/6/8/16/21/26/29/32 (+MA مشتركة مع BNQ: 3/8/16/21/26/29) | POS-SET |
| BNQ | يشارك POS + خاص | BNQ-SET |
| FAS | Attr 9 | FAS-SET |
| ENG (MNT) | #1/#2 فقط (طباعة JR/JO) — **UNK-061**: الحجم الحقيقي مجهول | MNT-OPR |
| MEM | 13 System Attributes داخلية | MEM-SET |
| SLM | MA 8 (Week/Day Access) | SLM-PRF |

---

## 5. القوانين المعمارية العابرة (Cross-Cutting Architectural Laws)

> الثمانية القوانين التي تحكم النظام كله — كل قرار تحويل يُختبر ضدها.

| # | القانون | النص الحاكم | الامتداد |
|---|---|---|---|
| **L1** | **قانون الربط قبل الحفظ** | أثر FAS-REP 19/20/21: النزاهة تُفحص **بعد** الترحيل (save-then-warn) — قرار التحويل D12 يقلبه إلى link-then-save | كل الجسور المالية |
| **L2** | **قانون الطباعة لكل-عميل** | Pgm.ID في FAS-SET §15 — برامج مخصصة لكل تثبيت (pre-printed/continuous/cut) | كل المطبوعات |
| **L3** | **قانون القفل الائتماني الثلاثي** | FO+POS+BNQ+يدوي — أربع نقاط تحقق Credit Limit واحدة | SLM→الجميع |
| **L4** | **قانون الخدمة المزدوجة للكيان** | Company Profile (SLM/AR) = Customer واحد يغذي 7 وحدات؛ Vendor (UNK-058) = Supplier واحد يخدم 4 | كيانا العميل والمورد |
| **L5** | **قانون الإصدار الزمني للسجلات** | لا تعديل: Applicable From الأحدث يفوز (الأسعار/الشرائح) | HRP/MEM/BNQ/TEL |
| **L6** | **قانون النافذة الزمنية للتحرير** | Back-date بأيام لكل نوع معاملة (فقر الأثر الرابع MGT) + قفل Audited الشهري/السنوي | كل المعاملات |
| **L7** | **قانون العزل الوظيفي** | وحدات حديثة تولد بلا صلاحيات/بلا INI/بلا GL — الحداثة = عزلة (CARE→GTP) | 8 وحدات |
| **L8** | **قانون القالب المشترك** | أشباح TOC المتكررون (IDS Crystal ×2) + فقرات منسوخة (C-MR-02 حرفياً) — الحزمة من قوالب منسوخة | البنية التوثيقية |

---

## 6. نقاط الالتفاف الحرجة (Critical Junctions)

النقاط التي عندها ينجح التحويل أو يفشل — مرتبة بالخطورة:

1. **خريطة الترحيل الآلي غير الشاملة** (UNK-098): HRP/FXD غائبان عن FOM/ACR/INV — أول ما يُحسم في Phase 9 (قرار Journal origin الأوسع).
2. **Vendor/Employee الموحدان** (UNK-058/038): بلا حسمهما تنفجر العلاقات المرجعية في 11 وحدة.
3. **Print Forms عبر FAS** (UNK-091): 6 تقارير موقوفة على طبقة كود خارج الحزمة.
4. **بوابة 511** (UNK-063): سلوك POS يقرره مفتاح FNB — أول تكامل سلوكي عكسي.
5. **Document المفقود** (GAP-SYS-D01): «Module Attributes & INI Settings» خارج الحزمة — خريطة السلوك ناقصة 50%+.
6. **القفل الائتماني** (UNK-051): نقطة الفحص الموحدة Customer Credit Gate.
7. **Rollback بلا معكوس GL** (UNK-071 — الأثر قصوى): Cancel-with-reversal إلزامي.
