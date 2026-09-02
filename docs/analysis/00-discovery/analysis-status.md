# حالة تحليل المشروع (Analysis Status)

> **هذه الوثيقة هي نقطة الدخول لأي جلسة عمل جديدة.**
> **بروتوكول الجلسة (قاعدة الاستمرارية):** اقرأ هذه الوثيقة ← اقرأ `source-coverage.md` ← حدد آخر نقطة مكتملة ← أكمل منها ← حدّث الوثائق والحالة. لا تعد عملًا منجزًا إلا لسبب تحقق موثق.

---

## هوية المشروع

| البند | القيمة |
|---|---|
| المشروع | Hotel ERP متكامل عربي أولاً (Arabic-First) |
| المنصة الخلفية | Frappe Framework + ERPNext + Frappe HRMS (طبقة داخلية غير مرئية للمستخدم) |
| الواجهة | Custom Frontend: Next.js + React + TypeScript + Tailwind + shadcn/ui — RTL Arabic-First |
| المصدر المرجعي الوظيفي | كتالوجات FortuneNext 6i (IDS Next) — `6i Manuals/` (65 ملف، 3,062 صفحة) |
| المنهجية | Functional Reverse-Engineering → Knowledge Base → Specification → Implementation Blueprint |
| **قاعدة ذهبية** | لا كود قبل اكتمال التحليل. DOCUMENT FIRST. |

---

## حالة المراحل (Phases)

| المرحلة | الوصف | الحالة | المخرجات |
|---|---|---|---|
| **Phase 0** | Discovery — فهرسة وجرد وخريطة | ✅ **مكتملة** | الوثائق الخمس في `docs/analysis/00-discovery/` + `extracted-text/` + `inventory.json` |
| **Phase 1** | Domain Model | ✅ **الإصدار التأسيسي مكتمل** (يُوسَّع في كل مرحلة) | `docs/domain/` (8 وثائق) — انظر أدناه |
| Phase 2 | Module Inventory التفصيلي | ◐ **بدأت — FO + FAS + ACR + POS + SYS محللة** | `docs/modules/{front-office, financial-accounting, accounts-receivable, point-of-sale, system-setup}` |
| Phase 3 | Detailed Module Analysis | ◐ **5/17: FO (19) + FAS (18) + ACR (19) + POS (19) + SYS (19) = 94 ملف وثائق** | نفس المسارات |
| Phase 4 | Screens & UX | ⬜ لم تبدأ | `docs/screens/specifications/*` |
| Phase 5 | Workflows | ⬜ لم تبدأ | `docs/workflows/*` |
| Phase 6 | Accounting | ⬜ لم تبدأ | `docs/accounting/*` |
| Phase 7 | Reports | ⬜ لم تبدأ | `docs/reports/*` |
| Phase 8 | Security & Permissions | ⬜ لم تبدأ | `docs/security/*` |
| Phase 9 | Data Model | ⬜ لم تبدأ | `docs/data-model/*` |
| Phase 10 | Cross-Module Integration | ⬜ لم تبدأ | `docs/integrations/*` |
| Phase 11 | ERPNext/Frappe/HRMS Mapping | ⬜ لم تبدأ | `docs/architecture/erpnext-mapping/*` |
| Phase 12 | Gap Analysis | ⬜ لم تبدأ | `docs/gap-analysis/*` |
| Phase 13 | Architecture | ⬜ لم تبدأ | `docs/architecture/*` |
| Phase 14 | Traceability | ⬜ لم تبدأ | `docs/traceability/*` |
| Phase 15 | Implementation Roadmap | ⬜ لم تبدأ | `docs/implementation/*` |
| Phase 16 | Verification & Quality Gate | ⬜ لم تبدأ | — |

---

## سجل الجلسات

### الجلسة 1 — 2026-09-02

**ما تم:**

1. استخراج أرشيف `6i Manuals.zip` (121 MB) إلى `/home/z/my-project/hotel-erp/6i Manuals/`.
2. بناء خط أنابيب استخراج آلي: `scripts/inventory_manuals.py` (PyMuPDF) — استخرج نصوص الـ 65 ملف كاملةً إلى `extracted-text/` (مرتبة بالوحدات) مع ميتاداتا (صفحات، صور، عناوين) في `inventory.json`.
3. استخراج فهارس (TOC) كل الوثائق: `scripts/extract_tocs.py` + معالجة خاصة لملفات Care (نمط فهارس منقّط).
4. بناء مستخرج جداول الحقول الآلي `scripts/extract_fields.py`: **2,099 حقلاً موثقاً** من 13 ملف إعدادات → `field-extracts/` (JSON لكل ملف: أقسام + جداول حقول مرتبطة بأقسامها).
5. إنشاء هيكل `docs/` الكامل (كل مجلدات المراحل 1–16) + `docs/README.md` كفهرس تنقل.
6. إنتاج وثائق Phase 0 الخمس + `execution-plan.md` + `unknowns.md` (15 مجهولاً مسجلاً) + `contradictions.md`.
7. **Phase 1 — Domain Model (الإصدار التأسيسي):**
   - `domain/hotel-domain-overview.md` — الطبقات الوظيفية السبع + المفاهيم الجوهرية (Business Date, Folio, Night Audit, Rate Architecture...)
   - `domain/entities.md` — ~120 كياناً مصنفاً في 9 مجموعات مع المصادر
   - `domain/entity-relations.md` — **Knowledge Graph**: 46+ علاقة موثقة (Guest Journey G1-G16, Finance F1-F15, Supply S1-S9, HR H1-H6) + 10 قواعد سلوك مؤثرة
   - `domain/master-data.md` — تصنيف Master/Config/Transaction + خاصية **Applicable From** (إصدارية زمنية!) + قاعدة التجميد
   - `domain/transactions.md` — كتالوج دورات حياة المستندات + الأحداث المؤتمتة + 9 قيود تحقق موثقة
   - `domain/hotel-roles.md` — 20 دوراً موثقاً نصاً
   - `domain/terminology.md` — **قاموس موحد 147 مصطلحاً** (EN → FortuneNext → عربي → UI Label → Code)
8. قراءة عميقة: **FOM-DEP كامل (14/14)** + FOM-RES (~40%) + FOM-CAS (~35%) + FOM-REG (~15%) + FOM-SET (جداول الحقول آلياً + ص1-15).

**اكتشافات جوهرية موثقة في هذه الجلسة:**
- **6 روابط ترحيل محاسبي صريحة** في FAS-SET: FO/POS/MM/Payroll/Membership → Finance + AR → Finance (خريطة التكامل المعمارية).
- **FO→AR تلقائي:** "All credit settlements are transferred to the Accounts Receivables module automatically" (FOM-CAS ص69).
- **دورة Night Audit كاملة** بقواعدها: Post Tariff → Guest Balance (بعد منتصف الليل فقط، حظر الترحيل إلا للتاريخ التالي) → Night Balance (تسوية الفواتير المعلقة، Excess/Short=0) → Open New Date (تجميد نهائي).
- **نمط Masters الموحد:** Status Active/Passive + Applicable From + Last Updated — إصدارية زمنية للبيانات الرئيسية.
- **Settlement modes الموثقة:** Cash/Credit Card/Cheque/Company/Staff/Bill on Hold/Forex + تسوية جزئية + إبقاء الإشغال بعد التسوية.

**قرارات مهمة اتُّخذت:**
- لغة التوثيق: **العربية** مع المصطلحات التقنية بالإنجليزية (أسماء الملفات/الكيانات/DocTypes لاحقاً).
- مسار العمل: `extracted-text/` هو المصدر العملي للقراءة (وليس PDF مباشرة).
- أدوات مؤتمتة محفوظة في `/home/z/my-project/scripts/` لإعادة الاستخدام (inventory/tocs/fields).

**نقطة الاستئناف القادمة (الجلسة 2):**
1. إكمال القراءة العميقة لـ FOM: RES (ص28+) + REG (85%) + CAS (65%) + SET (السرد النصي للجداول الكبرى: Room Rate Master §7, Room Master §8) + GST/HSK/LUK/REP/CRG/SMS.
2. بدء **Phase 2/3 للوحدة الأولى (Front Office)**: إنشاء `docs/modules/front-office/00-overview.md` والهيكل الـ 19 ملفاً.
3. تحويل UNK-006 (تفاصيل Night Audit المحاسبية) من مجهول إلى موثق بعد قراءة FOM-CAS/REP المتعلقة بالترحيل.

---

### الجلسة 2 — 2026-09-02 (بعد الظهر)

**ما تم:**

1. **إنشاء مستودع GitHub** `Nagmix/Hotel-erp` (فرع main) وربطه بمستودع Git محلي مستقل في `/home/z/my-project/hotel-erp/`.
2. **تنظيف حقوق النشر:** استبعاد أدلة FortuneNext الأصلية (PDF + النصوص المستخرجة + الجداول الخام) من المستودع عبر `.gitignore` — المرفوع هو وثائق التحليل والأدوات فقط. تاريخ Git نظيف (بلا أي محتوى محمي).
3. **دفع أولي (4 commits):** scaffold + PHASE 0 + PHASE 1 + فهرس docs.
4. **إكمال القراءة العميقة للوثائق التشغيلية الأربع:**
   - FOM-REG كاملاً (105 صفحة، 28 وظيفة): أنماط Check-in الأربعة، Guest Management، Guest Services، Group operations، Extension/SMS، Hotel Chart، Billing Broadcast.
   - FOM-RES كاملاً (68 صفحة): دورة الحجز الكاملة (Add/Amend/Cancel/Inquire/Assign/Copy/Re-Instate) + Room Type Booking + Room Rack Console + Retentions + Close Inventory.
   - FOM-CAS كاملاً (95 صفحة، 20 وظيفة): Posting بأنواعه التسعة، Deposits بثلاث بوابات، Paid Outs، Allowances، Splits/Transfers/Links، Settlements بالأنماط التسعة + Re-Instate + Refund + Foreex + Encashment + Agent Commission + Pax Transfer.
5. **PHASE 2/3 — Front Office (19 ملفاً):** إنشاء `docs/modules/front-office/` كاملاً:
   - 00-overview (حدود الوحدة + جرد الوظائف الـ 60+ بمصادرها + التفاعلات + المفاهيم الجوهرية)
   - 01-master-data, 02-configuration (المفاتيح الموثقة: INI 64, Attribute 16, Post History)
   - 03-screens (كتالوج 64 شاشة بأولويات P0-P2)
   - 04-workflows (13 سير عمل موثقاً خطوة بخطوة WF-FO-01..13)
   - 05-business-rules (10 مجموعات BR-FO-01..10) + 06-validations (V-FO-01..05 + مصفوفة الرسائل)
   - 10-transactions (سلسلة المستندات + حالات الحجز/الفوليو) + 11-accounting-impact (16 حدثاً مالياً + بنية التسويات + 6 أسئلة معلقة)
   - 12-integrations (16 تكاملاً موثقاً I1-I16) + 13-exceptions (28 حالة حدية E1-E28)
   - 14-data-model (23 كياناً + العلاقات + 6 قيود تصميم) + 15-ux-analysis
   - 16-erpnext-mapping (Seed Mapping بتصنيف A-F) + 17-gap-analysis (14 فجوة توثيق + 6 فجوات ERPNext) + 18-acceptance-criteria (8 مجموعات معايير)
6. تحديث source-coverage.md (4 ملفات read + analyzed).

**اكتشافات جوهرية موثقة في هذه الجلسة:**
- **Room Rate posting يسجل شحنة واحدة** — التنفيذ المتكرر يخزن الأخير فقط؛ للتعدد Additional Room Rate (4 أنواع: Rate/Plan/Extra Bed/Retention).
- **Day Charge = 1 أو 0.5** فقط (نصف اليوم موثق نصاً).
- **Fixed Charge Posting يمنع تكرار (revenue, guest, day)** — قيد تفرد مركب.
- **Bill Allowance محصور زمنياً بمدى Arrival↔Departure**.
- **التسوية يجب أن تتطابق (tally)** وإلا رفضت — + 9 أنماط + Multi + جزئية + إبقاء الإشغال + Resettlement.
- **Credit Card Authorization تلقائي من portal لكنه غير إلزامي**.
- **كل تغييرات الحجز تُسجل في Audit بخمسة أبعاد** (Reservation/Change Room/Room Rate/Amend Stay/Occupancy) + مستخدم + وقت.
- **OOO يتطلب سبباً من قائمة + قسماً** وOOS وصفاً فقط؛ From/To غير قابلين للتحرير في كليهما.
- **Close Room Inventory يمنع الحجز لكن يسمح لـ walk-ins** — تفصيل تشغيلي مهم.
- **Re-Instate (Cancel/No-Show) يولد رقماً جديداً دوماً** — الأرقام المسلسلة لا تُعاد أبداً.
- **Folio Re-Instate متاح قبل Night Audit فقط، والغرفة الرئيسية قبل المرتبطة**.
- **6 روابط تفويض موثقة** عبر العمليات الحساسة (نمط "منفذ + مصرِّح" مزدوج).

**نقطة الاستئناف القادمة (الجلسة 3):**
1. **Quality Gate لوحدة FO الحالية** — التحقق من مطابقة 04-workflows و05-business-rules للأدلة ثم استكمال نقاط [PENDING]: قراءة FOM-SET عميقاً (خصوصاً §7 Room Rate Master و§8 Room Master + جرد Attributes/INI كاملاً) + FOM-LUK + FOM-CRG.
2. **الوحدة التالية في التسلسل: FAS (Financial Management)** — بدء هيكل 19 ملفاً + قراءة FAS-SET (الروابط الست) وFAS-TRN (حسم QA-1..6 وUNK-006).
3. ترقية unknowns.md: حسم ما يمكن من UNK-001..015 وتحديث الحالة.

---

### الجلسة 3 — 2026-09-02 (مساء)

**ما تم:**

1. **Quality Gate لـ FO — اكتمل:**
   - قراءة FOM-SET كاملة (67 قسماً، 145 ص): هندسة التعرفة §1-§8 (كاملة الحقول والقواعد) + Core Masters + قوائم + Behavior Config + مصممون + Data Ops + **مصفوفة التعديل (48 قاعدة Note لكل Master)**.
   - قراءة FOM-LUK كاملة (22 وظيفة Lookups).
   - قراءة FOM-CRG كاملة — **تصحيح: CRG = Concierge** (5 وظائف: Left Luggage/Parcels/Ticket/Valet/Baggage) وليس Charge Groups.
   - قراءة FOM-HSK كاملة (18 وظيفة: OOO/OOS بالسحب والإفلات، دورة الغسيل كاملة ب7 أنماط تسوية، المفقودات، الجدولة ≤7 أيام).
   - قراءة FOM-GST كاملة (17 وظيفة: Guest Master بـ 10 تبويبات، الولاء 4 مراحل، Merge/Purge).
   - تحديث وثائق FO: 01 (كتالوج 67 + مصفوفة) + 02 + 03 (**193 شاشة**) + 04 (WF-FO-15/16/17 موثقة) + 05 (BR-FO-11..16) + 07 (مصفوفة التفويض الخمسية) + 09 (22 بحثاً) + 12 (I17-I22) + 13 (E29-E42).
2. **الوحدة 2/17 — Financial Management (FAS) كاملة (18 ملفاً):**
   - قراءة عميقة كاملة: FAS-SET (27 قسماً — الروابط الست بنصوصها) + FAS-TRN (9 أقسام + 15 خياراً فرعياً) + FAS-MST (COA/Vendor/SL/ChequeBook) + FAS-LUK (9 استعلامات).
   - إنشاء `docs/modules/financial-accounting/` (00-18): 65 شاشة · WF-FA-01..16 · BR-FA-01..09 · V-FA-01..24 · I-FA-01..13 · E-FA-01..28 · 30 كياناً · Seed Mapping ERPNext (A-F) · فجوات ومعايير قبول.
   - تحديث FO `11-accounting-impact.md`: **حسم QA-1/QA-2/QA-3/QA-6 + UNK-006**.
3. تحديث unknowns (UNK-005/006/014/015 Resolved + 002/008 Partially + جديد 016/017) + source-coverage (13/65 read) + هذا الملف.

**اكتشافات جوهرية موثقة في هذه الجلسة:**
- **الروابط الست كاملة:** 13 Revenue Type في رابط FO (بما فيها Settlements=Debit فقط، GLB: B/F دائن/C/F مدين، No Transaction=Suspense إلزامي) + POS (منفذ × مجموعة قائمة: مبيعات Credit/خصومات Debit) + MM (أصل للشراء/مصروف للاستهلاك) + Payroll (ED Codes إلزامي) + Membership + AR (فوري مع تعديل F5).
- **قواعد التحقق التسعة للـ Book Types** (Receipts يبدأ Bank/Cash... Exchange/Contra كله Bank/Cash) — الأساس التشريعي للقيود.
- **نمط الفروق غير الموزعة:** فرق ≠ 0 → Yes → حساب No Transaction مؤقتاً → إصلاح الروابط → **إعادة ترحيل**.
- **Post FO to Finance:** الزنار بعد Day End + Open New Date؛ Effective = عادة الأمس؛ البنود تُعرض بـ Account/Revenue/Audit Code + D/C + SL.
- **أمثلة قيود ضريبة الشراء بالأرقام** (طريقتا البائع/المشتري بـ INV Switches 1+4 + Vendor Tax Split).
- **Open Financial Year + Rollback** (أرصدة→افتتاحية + صافي P&L→Retained Earnings بنسب) + قفل Audited الشهري.
- **FO:** النقد إلزامي لكل المنافذ؛ مصفوفة تعديل كل Master نصاً؛ تعرفة أيام الأسبوع؛ تغيير نوع غرفة للشاغرة فقط + Create Hotel Chart؛ Purge 60/60/120 يوم؛ **INI موثقة جديدة: 58 (Reservation Mode) + 283 (استهلاك) + 504 (شيكات)** + FAS Switch 4 + INV 1/3/4 + Module Attr 9.
- **ترميز ألوان حالة الغرف** (VC/VD/RS/OD/OC/OO/OS) — أساس تصميم مخطط الغرف في الواجهة الجديدة.

**نقطة الاستئناف القادمة (الجلسة 4):**
1. **الوحدة التالية: Accounts Receivable (AR)** — القراءة العميقة (RPL 33 + OPR 21 + SET 19 + BIL 8 + CRT 8 = 89 ص) ثم هيكل وحدة كامل — تكملة الحلقة المالية (FO→AR→FAS) وتوثيق AR User Access وAging.
2. بعدها **POS** (SET 122 + GST 56 + LUK 14 = أولوية تشغيلية) — يحسم UNK-001 (Guest Master الموحد؟) وUNK-012 (الدفع المقسّم).
3. مراجعة `docs/README.md` لتحديث فهرس الوحدات بوحدة FAS.

---

### الجلسة 4 — 2026-09-02 (ليلاً)

**ما تم:**

1. **الوحدة 3/17 — Accounts Receivable (AR) كاملة (19 ملفاً):**
   - قراءة عميقة كاملة للملفات الخمسة: ACR-SET (8 أقسام — Company Profile المشترك 7 وحدات + Aging بالفائدة) + ACR-OPR (8 أقسام — SOA/Rollback/Match/Untagging/CC Consolidation) + ACR-RPL (23 وظيفة) + ACR-BIL (4 فوترة) + ACR-CRT (Debtors Follow-Up بتنقيب 4 مستويات).
   - إنشاء `docs/modules/accounts-receivable/` (00-18): 88 شاشة · WF-AR-01..15 · BR-AR-01..14 · V-AR-01..30 · I-AR-01..15 · E-AR-01..30 · 24 كياناً · 16 حدثاً مالياً · Seed Mapping ERPNext (A-F بقرارات F-AR-1..4) · 10 فجوات مصدر + 10 فجوات ERPNext · 8 مجموعات معايير قبول + خطة Smoke Test.
2. تحديث: unknowns (UNK-013 Partially + جديد 018/019/020) + source-coverage (18/65) + هذا الملف + فهرس docs/README.md.

**اكتشافات جوهرية موثقة في هذه الجلسة:**
- **سلسلة القفل الثلاثية:** SOA (شهر) → Invoice (مستند) → Matching (إيصال) — كل طبقة تفتح التي تحتها فقط؛ Rollback مدى (من شهر القطع حتى آخر معالج) لا نقطة.
- **منطق INI معكوس:** #56 ACR2FAS: 0=مكن (افتراضي 1=معطل!) و #74: 0=يسمح التعديل بعد الطباعة — مصيدة نقل حرفي.
- **AR ترحّل تفاعلياً عند الحفظ** (شاشة FA Transaction تنبثق) — مقابل دفعات FO/POS المجمعّة بعد Day End: إيقاع مزدوج موثق.
- **حاجب Credit Limit عابر للوحدات:** تجاوزه يمنع تسوية FD/POS/BQT قبل حدوثها (تحقق upstream مركزي).
- **نمط الاستلام-المطابقة-الفك:** إيصال unallocated → Match Bills (إيصال واحد × فواتير متعددة) → Untagging للعكس — دورة حياة إيصال كاملة.
- **سعر صرف تاريخ الفاتورة يثبّت عند السداد** (منع Book Profit/Loss) — باستثناء التعديلات (سعر تاريخ التعديل).
- **CC Consolidation تجميع عرضي فقط** (للـ Register حصراً) + **المطابقة داخل شركة واحدة** + **متابعة بموعد/توقعات/تعيين**.
- **فجوة مصدر نادرة:** التقرير 13 في ACR-RPL بعنوان «12123 PENDING» — عنصر نائب متروك في الدليل الرسمي (GAP-AR-D01) + إشارة «Fortune Enterprise 2.0» (نَسَب قديم).

**نقطة الاستئناف القادمة (الجلسة 5):**
1. **الوحدة التالية: POS** — القراءة العميقة (SET 122 + GST 56 + LUK 14 = 192 ص ذات أولوية تشغيلية) ثم هيكل وحدة كامل — يحسم UNK-001 (Guest Master الموحد؟) وUNK-012 (الدفع المفسّم) وUNK-007 (العملات/Link Outlet Currencies).
2. بعدها **Materials Management** (SET 68 + LUK 38) أو **SYS-SSP** (110 ص — يحسم UNK-004/UNK-013 المتبقي) حسب الطاقة.
3. مراجعة domain/terminology.md لإضافة مصطلحات AR الناشئة (SOA/Untagging/Aging with Interest...).

---

### الجلسة 4 (تابع) — وحدة Point of Sale (POS) كاملة

**ما تم (بالاستمرار في الجلسة نفسها بعد AR):**

1. **الوحدة 4/17 — Point of Sale كاملة (19 ملفاً):**
   - قراءة عميقة: **POS-SET (42 قسماً/122 ص) + POS-GST (12 وظيفة/56 ص) + POS-LUK (7 استعلامات/14 ص) + Touch Screen Manual (34 ص — عمليات POS الفعلية!)**.
   - إنشاء `docs/modules/point-of-sale/` (00-18): 95 شاشة · WF-POS-01..16 · BR-POS-01..16 · V-POS-01..34 · I-POS-01..16 · E-POS-01..30 · 30 كياناً · 18 حدثاً مالياً · Seed Mapping (قرارات F-POS-1..5) · 11 فجوة مصدر + 12 ERPNext · 10 مجموعات معايير قبول + Smoke Test.
2. تحديث: unknowns (**UNK-001/007 Partially + UNK-012 Resolved** + جديد UNK-021/022) + source-coverage (22/65) + فهرس README (4/17).

**اكتشافات جوهرية موثقة (POS):**
- **العمليات الفعلية في دليل Touch Screen المنفصل** (وليس POS-* )!: Shift/Outlet/Session ثلاثية الفتح (كاشير فردي/منفذ جماعي) + إغلاق يحجبه المعلقات.
- **فصل KOT→Check→Settlement الثلاثي** + **Print Bill = تسوية نقدية تلقائية** + **Provisional (رقم صفر)** + **Reprint قبل التسوية يُبطِل الرقم ويرقِّم من جديد**.
- **Split 3 طرق** (Equal/Item/**Quantity كسري 0.5**) + Link Tables + Table Suffix — عائلة تجميع/تقسيم كاملة (يحسم UNK-012).
- **6 أنماط تسوية فاعلة حصراً** (Cash/CC/Cheque/Coupon/Guest/Void) + **Balance=0 إلزام** + Resettlement + Tips (CC/شيك/Guest فقط).
- **Guest Settlement = بوابة الائتمان الموحدة:** Room#→FO Folio؛ و**AR/Company/BoH بنفس المسار** → قيود AR تلقائية.
- **POS Guest Master مستقل مقيَّد بالمنفذ** + تشارك انتقائي مع FO (Preferences/Card Types) — قاعدتا ضيوف موثقتان (UNK-001 Partially).
- **Menu Master بنمطين** (Module Attribute 29: مشترك/لكل منفذ) + نقل أصناف بشرط تطابق العملات + Quick Update فوري/من الغد + Batch Rate.
- **مصمم طباعة مرئي كامل** (Projects + Toolbox + F4/F3 + Body إلزامي + 6 rows=1 inch + Make Active).
- **صلاحيات ثلاثية الأبعاد** (كاشير × KOT/Billing/Settlement × Regular/Touch/PDA) + Restrict Outlet Access (blocklist).
- فجوات مصدر: **§42 Taxcode Mapping فارغة** + §10 Server Outlet Mapping صورتان فقط + مرجعية وثائق SYS خارج الحزمة.

**نقطة الاستئناف القادمة (الجلسة 5):**
1. **الوحدة التالية (بالأولوية المالية): Materials Management** — MGT-SET (68 ص) + MGT-LUK (38 ص) أولاً (يحسم جزءاً من UNK-011 Auto Indent من BNQ/FNB) — أو **SYS-SSP (110 ص)** مباشرة لحسم UNK-004 (multi-property) + UNK-013/022 (المفاتيح والصلاحيات) — **المفضل: SYS-SSP أولاً** لأنه يحسم 3 مجهولات حرجة دفعة واحدة ويعلق القواعد المفقودة للوحدات الأربع المحللة.
2. بعده MGT ثم BNQ ثم HRP (بترتيب module-inventory §5).
3. POS-REP + FOM-REP + FAS-REP مؤجلة للمرحلة 7.

---

### الجلسة 5 — 2026-09-02 (فجراً)

**ما تم:**

1. **الوحدة 5/17 — System Setup (SYS) كاملة (19 ملفاً):**
   - قراءة عميقة كاملة: **SYS-SSP (110 ص — 3 فصول: User Setup + Supervisor + General Setup بـ 19 قسماً فعلياً)** — الأداة الآلية لجداول الحقول التقطت صفر جداول لهذا الملف (بنية مخالفة) فجرى توثيق الحقول يدوياً من المتن.
   - إنشاء `docs/modules/system-setup/` (00-18): **66 شكل/شاشة** (42 تشغيلية) · WF-SYS-01..12 · BR-SYS-01..15 · V-SYS-01..22 · I-SYS-01..18 · E-SYS-01..24 · 32 كياناً · 12 قراراً معماريياً (F-SYS-1..12) · 8 مجموعات معايير قبول + Smoke Test.
2. **حسم ثلاث مجهولات حرجة:**
   - **UNK-004 (multi-property) Resolved:** النموذج الأصلي سجل متعدد الخصائص لكن تشغيلاً أحادياً بلا آلية تبديل موثقة → **القرار F-SYS-11: Property = Company في Frappe**.
   - **UNK-013 (نموذج الصلاحيات) Resolved:** **النموذج الرباعي الطبقات** — Supervisor (تجاوز) + SYS المظلة (Group/User × Module/Sub/Item × Add/Modify/Delete) + قيود التقارير (Spool/Export/Format) + صلاحيات الوحدات الخاصة (AR/FAS/POS/FO) — راجع `modules/system-setup/07-permissions.md`.
   - **UNK-022 (مرجعية المفاتيح) Resolved:** وثيقة «Module Attributes & INI Settings» **مؤكدة خارج الحزمة** (إحالتان ص33/ص37) → GAP-SYS-D01 + استراتيجية الجدول التراكمي للإحالات (15+ مفتاحاً مجمعاً حتى الآن).
3. تسجيل مجهولات جديدة: **UNK-023** (سلوك انتهاء كلمة المرور) + **UNK-024** (Gift Shop في Reason Codes بلا أدلة مستقلة) + **UNK-025** (Group Nationality §19 الهامشية) + **UNK-026** (لا حذف موثق للمستخدمين).
4. تحديث: source-coverage (23/65) + هذا الملف + فهرس docs/README.md (5/17).

**اكتشافات جوهرية موثقة (SYS):**
- **سلسلة التفويض الثلاثية:** مزود الخدمة → مسؤول النظام (Supervisor) → مستخدمون — "total access to all menu items" للمشرف بلا استثناء.
- **كلمة المرور تولَّد آلياً بمجرد اختيار Designation** + عرضها **مكشوفة** في عمود User Management بعد Reset — فجوة أمنية أصلية تُصلح لا تُستنسخ (قرار F-SYS-6).
- **محرك الضرائب الثلاثي:** Code (×4 وحدات) → Slab (تراكمي 26.25 مقابل غير تراكمي 18.75 — مثال الدليل الرقمي) → Structure (Percentage/Amount/Slab × On Value/Discounted/**On Tax متسلسلة**) — لا نظير قياسي في ERPNext → محرك مخصص (F-SYS-7).
- **العملة أغنى من ERPNext:** Travellers Cheque كنوع + Standard Rate + **Division/Multiplication** + Million/Lakh + نص قبل/بعد الكسر + Decimal 0-3.
- **Round-off بأمثلة رقمية كاملة** (tie-break للأعلى عند التساوي في Nearer: 1000.50/0.50→1001.00).
- **قاعدة Modify-Locked:** 12+ كياناً بلا تعديل جوهري بعد الإنشاء (الحالة فقط غالباً) + استثناءات ثلاثة موثقة.
- **Applicable From > اليوم** في كل المرجعيات — إصدارية مستقبلية عامة.
- **§19 Group Nationality غير مدرجة في TOC** — اكتشاف توثيقي.
- **Extract DB Tables:** نسخ .INS إلى C:\PMSDATA + History بلاحقة MMYY + GUI<customer code>.dat.
- **تخصيص الداشبورد الأصلي:** ≤3 برامج قوائم + 3-5 رسوم + Guest Info + Statistics لكل مستخدم — يسري بعد إعادة الدخول.
- **Change Caption = آلية توطين أصلية** (عرض الاسموين معاً + تطبيق على التقارير) — تُستبدل بـ i18n كامل (F-SYS-3).

**نقطة الاستئناف القادمة (الجلسة 6):**
1. **الوحدة التالية: Materials Management (MGT)** — MGT-SET (68 ص) + MGT-LUK (38 ص) ثم MGT-OPR — يحسم جزءاً من UNK-011 (Auto Indent) ويكمل حلقة التوريد (المشتريات→المخزون→الاستهلاك→FAS).
2. بعده **BNQ (الولائم)** ثم **HRP (الرواتب)** بترتيب module-inventory §5.
3. التقارير (REP) للوحدات الخمس المؤجلة للمرحلة 7.

---

## مؤشرات الجودة الحالية

| المؤشر | القيمة | الهدف |
|---|---|---|
| ملفات مفهرسة | 65/65 | 65/65 ✅ |
| نصوص مستخرجة | 65/65 | 65/65 ✅ |
| ملفات قرأت قراءة عميقة | **23/65** (FOM عدا REP/SMS + FAS عدا REP + ACR كامل + POS 4 + **SYS-SSP كامل**) | 65/65 |
| وحدات محللة وظيفياً | **5/17** (FO 19 + FAS 18 + ACR 19 + POS 19 + SYS 19 = 94 ملف وثائق) | 17 |
| Knowledge Graph (علاقات موثقة) | 6 روابط ترحيل + 16 تكامل FO (I1-I16) | يوسَّع في Phase 3/6 |
| Unknowns مسجلة | انظر `docs/analysis/unknowns.md` | صفر حرج قبل التنفيذ |
