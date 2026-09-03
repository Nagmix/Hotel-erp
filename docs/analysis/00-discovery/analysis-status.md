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
| Phase 2 | Module Inventory التفصيلي | ◐ **بدأت — FO + FAS + ACR + POS + SYS + MGT + BNQ + HRP + Care + MEM + SLM محللة** | `docs/modules/{front-office, financial-accounting, accounts-receivable, point-of-sale, system-setup, materials-management, banquets, hrp-payroll, care, membership, sales-marketing}` |
| Phase 3 | Detailed Module Analysis | ◐ **11/17: FO (19) + FAS (18) + ACR (19) + POS (19) + SYS (19) + MGT (19) + BNQ (19) + HRP (19) + Care (19) + MEM (19) + SLM (19) = 208 ملف وثائق** | نفس المسارات |
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

### الجلسة 6 — 2026-09-02 — وحدة Materials Management (MGT) كاملة

**ما تم:**

1. **الوحدة 6/17 — Materials Management كاملة (19 ملفاً):**
   - قراءة عميقة كاملة: **MGT-SET (68 ص/28 قسماً) + MGT-DNT (75 ص/15 وظيفة Daily Entries — الملف اسمه DNT وليس OPR!) + MGT-LUK (38 ص/20 استعلاماً)** = 181 ص. (MGT-REP 112 ص مؤجل للمرحلة 7).
   - إنشاء `docs/modules/materials-management/` (00-18): **107 شاشة** · WF-MG-01..19 · BR-MG-01..18 · V-MG-01..42 · I-MG-01..15 · E-MG-01..14 · 64 كياناً · 11 حدثاً آلياً (A-MG) · 36 حالة حدية · Seed Mapping (قرارات F-MG-1..12) · 12 فجوة مصدر + 14 ERPNext · 10 مجموعات معايير قبول (48 معياراً) + Smoke Test 28 خطوة.
2. تحديث: unknowns (**UNK-011 Partially (DPR + Re-Order) + UNK-024 Partially (Shop Outlet)** + جديد **UNK-027..031**) + source-coverage (26/65) + هذا الملف + فهرس docs/README.md (6/17).

**اكتشافات جوهرية موثقة (MGT):**
- **FIFO الأصلي = FEFO وظيفياً:** "prioritized to disperse based on their expiry dates" + توزيع الإصدار تصاعدياً بالتاريخ — قرار تنفيذي F-MG-2.
- **التقييم خاصية مخزن لا صنف** (WA/FIFO لكل Store) — تعارض مباشر مع ERPNext العام — قرار F-MG-1 (محرك تقييم مخصص).
- **حلقة DPR التلقائية:** Indent → رصيد صفر → DPR Qty → ينعكس في Receipt آلياً — أقرب دليل موثق على Auto-Indent (UNK-011 جزئياً).
- **التجميد الشهري المتدرج:** Physical Stock → Variance Updation (تنبيه مراجعة التقرير!) → Process Store Ledger (تجميد ما عدا الحالي) + Cancel — عائلة التجميد الثالثة (FO يومي/FAS سنوي/MGT شهري).
- **Vendor Code = TTT+XXXX من Company Types (FO!)** — نفس عائلة ترميز AR — قرار توحيد F-MG-11 (Supplier Group مشترك).
- **كثافة مفاتيح قياسية:** 12 مفتاح MGT جديد (INI 39/131/245/355 + INV 3/5(=8؟)/6/7/13/14/298) → الجدول التراكمي 25+؛ **مفتاح متدرج القيمة (INI 355: 0/1/2/3)** يطوّر تصميم Feature Toggle (F-SYS-1).
- **Vendor Master أغنى من Supplier بمرتين:** 7 عائلات تفاصيل + تقويم 9 أيام دفع + 5 شرائح خصم + فائدة تأخير + Stop Purchase/Payment (منطق معكوس!) — F-MG-2.
- **Shop Outlet:** مخزن = منفذ (نفس الكود) + صنف لمنفذ واحد — دليل Gift Shop (UNK-024 جزئياً).
- **شاشة Transactions الذكية:** عدادات حية (معلقات/متوقع 7 أيام/منتهيات/تحت الحد/تحويلات) — أول KPI Dashboard جاهز الترجمة.
- **مفاجآت إسقاط إيجابية ERPNext:** Material Request = PR/Indent · Purchase Receipt (+bill_no!) = GR · Stock Reconciliation = Physical Stock · Repack = Conversion · Item-Supplier last rate آلي · Item Reorder per warehouse — أعلى قابلية إسقاط قياسي في المشروع.

**نقطة الاستئناف القادمة (الجلسة 7):**
1. **الوحدة التالية: BNQ (الولائم — 5 ملفات/255 ص: SET 98 + BIL 66 + BOK 41 + CFG 38 + LUK 12)** — بترتيب module-inventory §5 — يحسم UNK-011 (Auto Indent من BNQ) وUNK-025 (Group Nationality إن كانت للولائم).
2. بعده **HRP (الرواتب — 4 ملفات/253 ص)**.
3. (اختياري بالطاقة) وثيقة **Gate Passes** قصيرة لحسم UNK-029.

---

### الجلسة 7 — 2026-09-02 — وحدة Banquets (BNQ) كاملة

**ما تم:**

1. **الوحدة 7/17 — Banquets كاملة (19 ملفاً):**
   - قراءة عميقة كاملة للملفات الخمسة: **BNQ-SET (98 ص/20 قسماً) + BNQ-BOK (41 ص/Bookings) + BNQ-CFG (38 ص/12 قسماً) + BNQ-BIL (66 ص/13 قسماً) + BNQ-LUK (12 ص/استعلامان) = 255 ص كاملة**.
   - إنشاء `docs/modules/banquets/` (00-18): **88 شاشة** · WF-BQ-01..16 · BR-BQ-01..16 · V-BQ-01..30 · I-BQ-01..14 · E-BQ-01..14 · 46 كياناً · 18 حدثاً آلياً (A-BQ) · 33 حالة حدية · Seed Mapping (قرارات F-BQ-1..8) · 11 فجوة مصدر + 12 ERPNext · 10 مجموعات معايير قبول (42 معياراً) + Smoke Test 26 خطوة.
2. تحديث: unknowns (**UNK-011 RESOLVED كاملاً** + UNK-025 بالسلب + جديد UNK-032..034) + source-coverage (31/65) + هذا الملف + فهرس docs/README.md (7/17).

**اكتشافات جوهرية موثقة (BNQ):**
- **UNK-011 RESOLVED كاملاً — سلسلة Auto Indent بالنص:** Requirement Entry → **Pre Costing Chef Eng** ("ingredient details... from the recipe... or inventory items linked manually") → **Auto Indent** (Work Sheet# → Res/Party تلقائي + Department/CC + "recipe details populate based on the department selected") → MGT indent — قرار F-BQ-6 (WS→Material Request hook).
- **BNQ = FO×POS هجينة (قرار F-BQ-1):** تحجز بعقل FO (Market/Source/PayMode من FO defaults + Guest من الغرفة) وتفوتر بمحرك POS (Shift/Outlet/Session + 11 نمط تسوية + POS MA 3/8/16/21/26/29 + POS User Access حرفياً) — **بناء فوق محرك POS الموحد لا وحدة مستقلة**.
- **Function Room بـ 6 تبويبات** (Details بمقاسات وMinimum Revenue وSecurity + Seating بسعة لكل نمط مع صور + Pictures/Layout/Location) + **Sub Venues حصرية**.
- **نمطا الحجز:** **Across-Dates** (احتكار مستمر — "no other bookings can be taken until the function date is over") أو فترة زمنية؛ **Inquiry بلا قاعة**؛ نسخ Inquiry ممنوع.
- **قفل الودائع:** إلغاء ذي وديعة ممنوع ("make the paid outs first") + Refund/Retention مجمّد بعد Save + Running Balance.
- **Void ممنوع في BNQ** + **Complimentary/NC = ليست مبيعات** (قاعدة إيراد صريحة) + CC/Company/Staff → AR + Company → outstanding + **Blacklist message بالاسم والسبب**.
- **Availability Chart = أغنى لوحة عمليات موثقة** (قسمان + ألوان حالات مخصصة + دمج 4 حالات افتراضي (INI 408=1 يفصّل) + FP أزرق/بنفسجي + Management أحمر/Maintenance أخضر + تخصيص أعمدة (بإعادة تحميل — عيب يُصلح)).
- **F11/F12 في Requirement Entry** (إعادة تسمية صنف/جعله مجانياً) + Finalize ناعم + 9 معايير نسخ.
- مفاتيح جديدة: INI 346/408/409 — التراكمي **28+**.
- **فجوة REP الكلية:** لا ملف تقارير للولائم في الحزمة (GAP-BQ-D01) — Program IDs فقط (FP-NBIDSFP + BEO/Confirmation/Cancellation كأنواع).

**نقطة الاستئناف القادمة (الجلسة 8):**
1. **الوحدة التالية: HRP (الرواتب — 4 ملفات/253 ص: REP 133 + PNT 47 + SET 42 + RQP 31)** — يحسم UNK-010 (Care↔HRP Personnel Master) ويوثق ترحيل Payroll→Finance (الرابط السادس من الستة!).
2. بعده **Care** (3 ملفات/187 ص — تكمل UNK-010) أو **MEM** حسب الطاقة.
3. التقارير (REP) للوحدات محللة مؤجلة للمرحلة 7 (HRP-REP استثناء محتمل لأنه 133 ص من أصل 253).

---


### الجلسة 8 — 2026-09-03 — وحدة HR & Payroll (HRP) كاملة

**ما تم:**

1. **الوحدة 8/17 — HR & Payroll كاملة (19 ملفاً):**
   - قراءة عميقة كاملة للملفات الأربعة: **HRP-SET (42 ص/21 قسماً) + HRP-PNT (47 ص/24 وظيفة) + HRP-RQP (31 ص/8 وظائف) + HRP-REP (133 ص/19 مجموعة/68 تقريراً) = 253 ص كاملة**.
   - إنشاء `docs/modules/hrp-payroll/` (00-18): **79 شاشة تشغيلية + 68 تقريراً** · WF-HR-01..17 · BR-HR-01..18 · V-HR-01..30 · I-HR-01..16 · E-HR-01..30 · 50 كياناً · 18 حدثاً مالياً · 10 أحداث آلية · Seed Mapping (قرارات F-HR-1..12) · 11+12 فجوة · 10 مجموعات معايير قبول (46 معياراً) + Smoke Test 28 خطوة.
2. تحديث: unknowns (**UNK-010 Partially — النصف الداخلي محسوم: RQP يغذي Personnel Master آلياً** + جديد UNK-035..040) + source-coverage (35/65) + هذا الملف + فهرس docs/README.md (8/17).

**اكتشافات جوهرية موثقة (HRP):**
- **AR→Payroll Transfer موثق بالنص (PNT §22):** "the amount has to be charged to the payroll, then it goes to the accounts receivable... transferred to the Payroll" — **جسر عكسي جديد يرسم الحلقة الرابعة المغلقة** (POS/BNQ/FO Staff → AR → HRP → Net Pay) — تحديث Knowledge Graph بعلاقة S10 مطلوب.
- **محرك ED المعادلاتي الأغنى في المشروع:** 6 أنماط ED (منها Temporary وسيط لا يطبع + Number Deduction بمرجع رقمي) × 3 أنواع حساب × 4 مصادر (منها **Accept = إدخال وقت المعالجة**) × **شرائح 4 أنواع بأمثلة رقمية كاملة** (Normal 500 / Cumulative 350 / Step Over 400 / Eligibility عتبة ESI 6500) × تراكم ثلاثي (Month/Cumulative/**Cumulative C/O بنقطة تهيئة**) + **Priority/Partial/Carry Forward** (أرباح 1500 وخصم 1700: Yes=1700 كاملة! / No=صفر!) + **Take Home %** صمام أمان فئوي + Special Program (PYINDSP هندي مغلق) — **قرار F-HR-1: محرك أجور مخصص فوق Salary Structure**.
- **الرصيد الإجرائي الهندي كامل:** PF (FPF/VPF/EDLI+Admin) + ESI + PT + LWF بأربعة تعريفات منفصلة + **15 نموذجاً رسمياً قابلاً للطباعة** (PF: 3A/5/6A/9/10/12A/Challan/Reconciliation/EDLI + ESI: 3/5/7/Challan/ESIC-Recon) + PF Challan بثلاث قنوات دفع (Cash/Cheque/Draft بتفاصيل).
- **INI 220 (0=مفعل!)** — عائلة INI المعكوسة: 56/74/220.
- **Payroll Audit بقيم old/new** (REP §19) — أول نمط versioning موثق في الحزمة.
- **واجهة الحضور flat file** `PYATYYMM.DAT` (EMP7/DATE8/CODE3/DAYS5,2) — **[Applicable to Fortune Enterprise Only]** فجوة إصدارية ثالثة + عقد بائع ("two weeks in advance" كتابياً).
- **فئات النقد (Denomination)** + Statements بخمس قنوات صرف (All/Cash/Bank/Drafts/Transfers) + Branch Folio (حسابات بنكية للموظفين).
- **قفل أصل القرض** + Loan Return للتعديلات + F&F (Indemnity اختياري + Final/Vacation print).
- **Bonus الرباعي** (Ext/Ext Exg/Left/Left Exg مع cutoff 7500) + **Recalculate Professional Tax**.
- **إقفال حبيبي** فئة+قسم/CC/درجة — عائلة التجميد الرابعة (FO يومي/FAS سنوي/MGT شهري/HRP فئوي-حبيبي).
- **توافق Frappe HRMS ممتاز** في: التوظيف (Job Opening/Applicant/Offer) + الإجازات + Attendance + Salary Slip + **Employee Loan** + **Full and Final** + Staffing Plan — أربع أصول مخصصة فقط: المحرك (شرائح/تراكم/أولويات) + Statutory Layer جغرافية + AR-hook + كسر النقد.

**نقطة الاستئناف القادمة (الجلسة 9):**
1. **الوحدة التالية: Care (3 ملفات/187 ص: OPR 80 + REP 73 + SET 34)** — تكمل UNK-010 (جسر Care↔HRP Personnel Master).
2. بعده **Membership (5 ملفات/133 ص)** — يحسم الجانب الثاني من رابط الترحيل السادس (Membership→Finance).
3. ثم **SLM/Sales & Marketing (4 ملفات/103 ص)**.
4. التقارير (REP) للوحدات محللة مؤجلة للمرحلة 7 (HRP-REP استثناء نُفذ لأنه 133/253 من الوحدة).

## مؤشرات الجودة الحالية

| المؤشر | القيمة | الهدف |
|---|---|---|
| ملفات مفهرسة | 65/65 | 65/65 ✅ |
| نصوص مستخرجة | 65/65 | 65/65 ✅ |
| ملفات قرأت قراءة عميقة | **38/65** (FO 9 + FAS 4 + ACR 5 + POS 4 + SYS-SSP + MGT 3 + BNQ 5 + HRP 4 + **Care 3 كاملة**) | 65/65 |
| وحدات محللة وظيفياً | **9/17** (FO 19 + FAS 18 + ACR 19 + POS 19 + SYS 19 + MGT 19 + BNQ 19 + HRP 19 + Care 19 = 170 ملف وثائق) | 17 |
| Knowledge Graph (علاقات موثقة) | 6 روابط ترحيل + 16 تكامل FO (I1-I16) | يوسَّع في Phase 3/6 |
| Unknowns مسجلة | انظر `docs/analysis/unknowns.md` | صفر حرج قبل التنفيذ |

---

### الجلسة 9 — 2026-09-03 — وحدة Care (Fortune Care v6) كاملة + دفع HRP

**ما تم:**

0. **دفع HRP إلى GitHub** بعد استلام بيانات الاعتماد: `fd5b014..1a5796b` (كانت الوحدة منجزة محلياً كاملاً والفشل كان في الدفع فقط).
1. **الوحدة 9/17 — Care كاملة (19 ملفاً):**
   - قراءة عميقة كاملة للملفات الثلاثة: **CARE-SET (34 ص/6 أقسام) + CARE-OPR (80 ص/6 وظائف) + CARE-REP (73 ص/20 تقريراً) = 187 ص كاملة**.
   - إنشاء `docs/modules/care/` (00-18): **32 شاشة (≈44 عنصراً شاشياً) + 20 تقريراً** · WF-CA-01..16 · BR-CA-01..18 · V-CA-01..23 · I-CA-01..14 · E-CA-01..18 · 17 كياناً (50+ حقلاً) · 16 معاملة · Seed Mapping (قرارات F-CA-1..10 — 4 أصول مخصصة فقط!) · 7+5 فجوات · 10 مجموعات قبول (42 معياراً) + Smoke Test 24 خطوة.
2. تحديث: unknowns (**UNK-010 RESOLVED نهائياً** + جديد UNK-041..044) + source-coverage (38/65 — 9 وحدات/170 ملف وثائق) + هذا الملف + فهرس docs/README.md (9/17).

**اكتشافات جوهرية موثقة (Care):**

- **UNK-010 RESOLVED نهائياً:** Care لا يقرأ HRP إطلاقاً — مستخدمون/أقسام/تصنيفات/ورديات/مواقع/غرف/ضيوف/L&F كلها من **PMS** (7 قنوات واردة — أعلى اعتماد أحادي في المشروع)؛ الموظفون يُنشؤون محلياً خفيفين (اتصال+صورة+تصعيد) — مخزنان مستقلان؛ قرار F-CA-2: توحيد Employee في إعادة البناء.
- **محرك SMS ثنائي الاتجاه فريد في المشروع:** تخصيص آلي للحاضر بصيغة حرفية `<1> Complaint #: 1 Room #: OR0707 Task.. Est. Time: 10 mins Priority: High Esc Level: 0` + أوامر ردّية **`1 S` (بدء) / `1 C` (إغلاق)** + 5 رسائل خطأ موثقة نصاً + إشعار إغلاق المشرف `CLOSED BY: JOHN REASON: ISSUE RESOLVED` — المنفذ الحقلي يعمل **بلا شاشة إطلاقاً** (الهاتف فقط).
- **14 حالة تشغيلية** (Queued→Delivered→WIP→AwaitingFeedback→Closed + Cancelled/Stopped/Unassigned + Esc 0-4) — أغنى آلة حالة في المشروع.
- **زر Thank You يبدأ المؤقت** (وليس الحفظ)؛ التصعيد التسلسلي بـ timeout دقائقي لكل مستوى عبر سلسلة Reporting (مثال: Room boy→Supervisor→Manager→FOM→GM→MD).
- **عهدة الموبايل بين الورديات:** رقم الموظف يستقبل المهام ويُعاد تعيينه لموظف الوردية التالية (Login/Logout باسترداد checkbox).
- **فجوات نوعية:** لا فوترة رغم Charges/Approximate Cost (GAP-CA-D01)؛ لا تغذية Attendance من الروستر (GAP-CA-P1)؛ IVR صندوق أسود (D04)؛ لا مفاتيح INI إطلاقاً (D03 — الوحدة الوحيدة)؛ Break بلا تفصيل (D07).
- **أعلى كفاءة بذرة Frappe في المشروع:** Issue/Employee/Checkin/Notification تغطي معظم الوحدة — أصول مخصصة: SMS Reply Processor + لوحة الروستر D&D + محرك التصعيد الدقيقي (~2-3 أسابيع فقط).
- **عائلة التجميد تكتمل (الخامسة):** روستر Care (ماضٍ محمي) بعد FO يومي/MGT شهري/FAS سنوي/HRP رواتب.

**نقطة الاستئناف القادمة (الجلسة 10):**
1. **الوحدة التالية: MEM (العضويات — 5 ملفات/133 ص: RPL 56 + MPF 30 + MTR 18 + SET 16 + MMN 13)** — دورة عضوية كاملة (طلب→فحص→موافقة→تجديد→إلغاء) بفوترة وترحيل إلى AR (تكمل حلقة الإيراد).
2. بعدها **SLM (المبيعات) أو TEL (الهاتف)** حسب الطاقة.
3. التقارير المؤجلة (REP) للوحدات محللة تبقى للمرحلة 7.

---

### الجلسة 10 — 2026-09-03 — وحدة Membership (MEM) كاملة

**ما تم:**

1. **الوحدة 10/17 — Membership كاملة (19 ملفاً):**
   - قراءة عميقة كاملة للملفات الخمسة: **MEM-SET (16 ص/12 قسماً) + MEM-MMN (13 ص/7 وظائف) + MEM-MPF (30 ص/10 وظائف) + MEM-MTR (18 ص/13 وظيفة) + MEM-RPL (56 ص/38 تقريراً/استعلاماً) = 133 ص كاملة**.
   - إنشاء `docs/modules/membership/` (00-18): **~80 شاشة (42 تشغيلية + 38 تقريرية)** · WF-ME-01..15 · BR-ME-01..18 · V-ME-01..22 · I-ME-01..12 · E-ME-01..25 · T-ME-01..14 · 12 حدثاً مالياً · Seed Mapping (قرارات F-ME-1..12) · 7+5 فجوات · 10 مجموعات قبول (48 معياراً) + Smoke Test 26 خطوة.
2. تحديث: unknowns (جديد **UNK-045..048**) + source-coverage (**43/65 — 10 وحدات/189 ملف وثائق**) + هذا الملف + فهرس docs/README.md (10/17).

**اكتشافات جوهرية موثقة (MEM):**

- **جسر MEMC001 — أول إنشاء كيان AR تلقائي في المشروع:** "a company master is automatically created as MEMC001 where 'C' is the first letter of the Surname" (DAVID S CRAIG → MEMC001) مع **سمة لا رجعية** (#10 لا تُلغى بعد التفعيل + مشروطة بـ #9) — العضو يصبح شركة City-Ledger قابلة للفوترة لحظة الحفظ.
- **خمس قنوات ترحيل إلى AR:** Process Subscription + Process Facility + Cover (Process/**Cancel**!) + Late + (Tax Posting المفقودة جسمها!) — Post Subscription **انتقائي بثلاثية withhold/withdraw/overwrite** (أدق تحكم تشغيلي في محركات المشروع).
- **المثال الرقمي لرسوم التأخير:** January-2011 → رصيد آخر يوم December-2010 → Debit فقط → رسوم ببنية ضريبية **من FO** → ACR — توثيق حسابي مزدوج (إزاحة شهر + اتجاه رصيد).
- **GAP-ME-D01 (أول حالة فهرس-بلا-جسم):** Membership Tax Posting في TOC MTR #11 **بلا أي نص في الجسم** — الوظيفة الوحيدة بهذا الوضع في 43 ملفاً → UNK-045.
- **التتالي الهابط الموحد:** إصابة Primary بالقائمة السوداء/الإنهاء/الاستقالة/الوفاة تعمّم العائلة تلقائياً؛ العكس مستحيل (نص حرفي 4 مرات) + **خلافة الوفاة** (بديل من العائلة أو None = إزالة الجميع).
- **ثلاث شرائح عملاء:** Member/Guest/**Affiliated** (نوادٍ متفق معها بصورة وفئة مستفيدة) × Adult/Children — ترجمة Frappe مباشرة: Price Lists + Customer Groups.
- **دفاتر AR مصغرة داخلية:** 15 تقريراً مالياً (Closing Balance/Due/Control/Receipt Register بـ Bank-wise breakup/Credit Card Register بـ **Commission %**) — الوحدة تمتلك دفترها المساعد الشهري المستقل.
- **CRM بريدي مدمج:** بريد التحقق للطالب + Birthday List بتحديث بريد بالنقر المزدوج + **Send Email أمنيات** — التقرير كمساحة عمل (مع حفر 3 مستويات في Membership Summary وحفر للفاتورة في Spending Pattern + إخفاء أعمدة).
- **Once/Recurring كمفتاح توجيه فوترة:** Once يظهر في Revenue/Facility Entry يدوياً؛ Recurring محصور بمحرك Process Subscription.
- **F&B مستثنى صراحة** من Service Bill (POS حكر) + Event Definition توازي BNQ بلا جسر (GAP-ME-D03/UNK-046 خطر ازدواج حجز).
- **لا مفاتيح INI إطلاقاً** (الوحدة الثانية بعد CARE) — System Attributes بـ13 سمة داخلياً بعائلة استدعاء رباعية (استدعاء الإيصال من 4 نقاط حفظ).
- **توافق Frappe قوي غير متوقع:** Customer (يجعل MEMC001 مجانياً!) + Subscription/Recurring Invoices + Price Lists الثلاثية + Workflow للإنهاءات + non-profit Membership كقالس — 7-9 أصول مخصصة (~6-8 أسابيع).

**نقطة الاستئناف القادمة (الجلسة 11):**
1. **الوحدة التالية: SLM (المبيعات والتسويق — 4 ملفات/103 ص: PRF 42 + SLT 29 + REP 22 + QTS؟)** — تحقق من inventory.json للأسماء الدقيقة.
2. بعدها **TEL (الهاتف — 4 ملفات)** أو **GATE (بوابات) أو MNT (صيانة)** حسب الطاقة.
3. التقارير المؤجلة (REP) للوحدات محللة تبقى للمرحلة 7 (MEM-RPL استثناء نُفذ لأنه 56/133 من الوحدة).

---

### الجلسة 11 — 2026-09-03 — وحدة Sales & Marketing (SLM) كاملة

**ما تم:**

1. **الوحدة 11/17 — Sales & Marketing كاملة (19 ملفاً):**
   - قراءة عميقة كاملة للملفات الأربعة: **SLM-SLT (29 ص/10 وظائف) + SLM-PRF (42 ص/17 وظيفة) + SLM-REP (22 ص/19 تقريراً) + SLM-LUK (10 ص/6 استعلامات) = 103 ص كاملة**.
   - إنشاء `docs/modules/sales-marketing/` (00-18): **~60 شاشة/نافذة (24 SLT + 15 PRF + 19 REP + 6 LUK)** · WF-SM-01..14 · BR-SM-01..34 · V-SM-01..28 · I (تكاملات 8 عائلات) · E-SM-01..20 · T-SM-01..16 · محاسبة (صفر-قيود! أثر مفوض عبر الحدود) · Data Model (~160 حقلاً/كياناً مركزياً) · UX · Mapping (F-SM-1..8) · 7+5 فجوات · 10 مجموعات قبول (46 معياراً) + Smoke Test 26 خطوة.
2. تحديث: unknowns (جديد **UNK-049..052**) + source-coverage (**47/65 — 11 وحدة/208 ملف وثائق**) + هذا الملف + فهرس docs/README.md (11/17).

**اكتشافات جوهرية موثقة (SLM):**

- **مركز الائتمان في غير وحدة الائتمان:** Company Profile (تحت SLM!) يحمل شروط AR المالية كاملة (Bypass Invoice/Allow Credit/Credit Days/Invoice Currency/Interest %/Credit Limit/Commission %/Collection Executive/Billing Address) — والقفل الائتماني **ثلاثي الوحدات + يدوي**: "settlement of the Front Desk, Point of Sale or Banquet bill or manual posting of the bill is not allowed" — أقوى قاعدة مالية عابرة للوحدات في المشروع (UNK-051 لنقطة التفعيل).
- **دورة Prospect→CGR بمستودعين وجسر تخرّج:** Prospects (بماستر غني: CEO/holding/**competitors**/turnover/Frequent Travelers) منفصلة عن Company Master — والتحويل وظيفة مخصصة بتوليد كود آلي **TTT+حرف أول+مسلسل لكل (نوع،حرف)** (أمثلة: COM/TAG/AIR) — تطابق حرفي لدورة **Lead→Customer** في ERPNext (أفضل موائمة في المشروع: 8 أصول فقط، قلبها منصة-جاهز).
- **مفتاحا INI جديدان + سمة FO:** **INI #239** (تعميم Executive Planner لكل المستخدمين) و**INI #41 = '0' لتفعيل** تحقق cutoff في الحجوزات (عائلة مقلوبة — انضمام لـ56/74/220؛ تراكمي 31+) + **Module Attribute #8 for Reservations** (Week Access↔Day Access) يوثق وظيفة سمة FO جديدة (بعد 16).
- **Sales Manager Tool — أول CRM 360°:** 10 عروض (General Info للقراءة فقط/Sales Activity/Entertainment/Negotiated Rates/Amenities/Reservations مع Cancelled+No-Show+Past/In-house/Revenue برؤوس إيراد/**Receivables بتاريخ قطع=Accounting date**/Guest Visits) + **Hotel Position** (يومي→ساعي→غد→تفصيلي→سنوي مع Over Booking).
- **ثلاثية الوكلاء:** Allocation (Over-book% + أيام تأكيد + Week/Day Access) + Forecast (شبه مؤكد، "should match allocation") + Release Dates (cutoff متعددة → reservation **prompt Inside/Outside**) — مفهوم allotment فندقي صرف بلا مقابل ERPNext (F-SM-3 الأصل المخصص الوحيد الكبير).
- **Revenue Discount Master menu-type wise:** FOOD/LIQUOR/SOFTDRINKS/TOBACCO/OTHERS — خصم لكل رأس إيراد + تفريع menu لـF&B — يُنفذ في POS/FO عند "generation of Bills" — ترجمة Pricing Rules حرفية.
- **قناة تسويق بريدية كاملة:** Company Letters عبر **Microsoft Outlook** (CEO→بريد الشركة، غيره→جهات الاتصال، مرفقات+Subject) + Labels 2/3 أعمدة + E-Mail ID List + Birthday/Anniversary (Company/Prospect × Contact/Frequent Travelers × MM/YY) — تُعاد بـEmail Template+Newsletter (F-SM-5).
- **Hotel Profile بالمحتوى التنافسي:** فنادق مقارنة (لم Market Share) + Outlets (Dress Code/Smoking/Chef!) + Banquets + VIP + **Picnic Spots** + صور BMP-only + معلومات عامة (حرارة/مسافات/أجرة) — **ويُستدعى من شاشة الحجز** (LUK §4: "browsed from Room Booking screen") — بيانات بيع حية.
- **صلاحيات صفر موثقة:** لا قسم User Rights في أي ملف من الأربعة — الوحدة الوحيدة بعد 48 ملفاً (GAP-SM-D04) → تصميم P-SM-1..5.
- **صفر قيود GL:** كل الأثر المحاسبي مفوَّض (شروط ائتمان/خصومات/سياسات تحصيلها FO/AR) — SLM "مصممة قرارات" تنفذها الوحدات عند الحدود (UNK-050 لمسار Entertainment/Gift).
- **Market Share Analysis بلا مصدر إدخال موثق:** "based on the comparative room sales entry" — شاشة غير موجودة → UNK-049 (أعلى أثر) + [INFERENCE] Daily Occupancy لفنادق Hotel Profile.
- **أثر توثيقي خام:** "BELOW SCREENSHOTS ARE REQUIRED" في LUK ص9 (GAP-SM-D05) + "Conferencing" في قائمة مستهلكي Profile بلا وحدة → UNK-052.
- **UNK-038 تتسع:** Sales/Collection Executives = ثالث مخزن موظفين (FO Setup — لا HRP) بعد HRP-employee وCare-PMS-employee.

**نقطة الاستئناف القادمة (الجلسة 12):**

1. **الوحدة التالية: TEL (الهاتف — 4 ملفات/83 ص: SET 32 + LUK 21 + REP 20 + CAC 10)** — محاسبة المكالمات + ترحيل الإيراد لفوليو النزيل (حلقة تكامل FO-مالية).
2. بعدها: MNT (3/81) ثم FNB (4/76) ثم FXD+GTP (2/38) — لإغلاق الـ17.
3. التقارير المؤجلة (REP) للوحدات محللة تبقى للمرحلة 7.

---

### الجلسة 12 — 2026-09-03 — وحدة Telephone Management (TEL) كاملة

**ما تم:**

1. **الوحدة 12/17 — Telephone Management كاملة (19 ملفاً):**
   - قراءة عميقة كاملة للملفات الأربعة: **TEL-SET (32 ص/10 أقسام) + TEL-REP (20 ص/8 تقارير) + TEL-LUK (21 ص/9 استعلامات) + TEL-CAC (10 ص/4 وظائف) = 83 ص كاملة**.
   - إنشاء `docs/modules/telephone/` (00-18): **~40 شاشة/نافذة (17 SET ببطاقات Onity الخمس + 6 CAC + 9 REP + 12 LUK)** · WF-TE-01..14 · BR-TE-01..24 · V-TE-01..26 · I-TE-01..13 (عتاد مزدوج!) · T-TE-01..14 + 10 أحداث آلية · محاسبة (فوليو بكود إيراد لكل نوع × توحيد لكل نوع + P&T بلا قيد) · Data Model (16 كياناً/~120 حقلاً) · UX (وحدة تحكم العامل + أزمة تسمية Transfer/Extension) · Mapping (F-TE-1..10 — ~7 أصول/~4.5 أسابيع) · GAP-TE-D01..D07 + P01..P05 · 10 مجموعات قبول (47 معياراً) + Smoke Test 24 خطوة.
2. تحديث: unknowns (جديد **UNK-053..057**) + source-coverage (**51/65 — 12 وحدة/227 ملف وثائق**) + هذا الملف + فهرس docs/README.md (12/17).

**اكتشافات جوهرية موثقة (TEL):**

- **بوابة العتاد المزدوجة الفريدة:** القناة الوحيدة في المشروع بتكاملين عتاديين موثقين — **EPABX** ("data transfer between EPABX and the Serial Port" + Conversion Program ≤7 محارف + **Battery Reverse Signal** للمكالمات الناضجة + **2-Way Communication** بالتحكم العكسي: "activate / de-activate the phones, voice mails, wake-up calls and room status") و**أقفال Onity** (واجهة كروت كاملة داخل TEL!: New/Copy/**Single Open**/Check Out تعطيل/Read — بآلية "saved in the backend, read by the door lock interface program and send to the device") — **نمط معماري معياري لكل تكاملات العتاد** عند إعادة البناء (F-TE-8/9).
- **محرك التسعير النبضي الأغنى توثيقاً رقمياً:** شرائح زمنية بـ4 أزواج أسعار (P&T×Hotel × Regular×Holidays بSeconds/Rate لكل) + **نسبة الحساب بأرقام حرفية** (60c: 100%=60c، 150%=90c، 200%=120c، **0%=uncharged ممنوعة لSTD/IDD**) + Min/Max ي overwrite الشريحة + تقريب رباعي (Higher/Nearer/Lower/None) + حدود دنيا للمكالمات الأخرى (Toll Free/Calling Card/AT&T) — أرقام الدليل = حالات اختبار جاهزة (F-TE-2).
- **الشراكات الست الدفاعية:** LCA + 9999999999 (بلد) + الثلاث (منطقة: LCA/LCA محلي · 9999999999×2 بأعلى IDD · فارغ/9999999999 بأعلى STD) — "غير المعرف يُسعَّر بأغلى تعرفة" — **حماية إيراد مدمجة بالماستر** (BR-TE-11).
- **سباق تسجيل الوصول الجماعي موثق:** Room vacant error — "The keys were given to the guest and the guest checked-in... but the same check-in **is not recorded in the PMS**" — توثيق مبكر نادر لrace condition (فيزيائي vs منطقي) + 4 حالات خطأ (امتداد غير معرف/مدة قصيرة/Bad records بمحرف دخيل 01/@2/99) + إصلاح يدوي **Select→YES = إعادة ترحيل للفوليو** (T-TE-06 — الفعل المالي اليدوي الوحيد).
- **خلود الشرائح الزمنية:** "You cannot Modify or Delete... Add a new record with the same slab code but with a **new applicable from date**... latest wins" (مثال 2011/2012) — **عائلة الإصدار الزمني الرابعة** (HRP-Rate/MEM-Service/BNQ-Corporate) — بنية موحدة تتكرر عبر الوحدات.
- **أدق تحكم توحيد في المشروع:** Consolidate Postings **Yes/No لكل نوع مكالمة على حدة** (بند يومي لكل نوع أو بند لكل مكالمة) + Revenue Code مستقل لكل نوع — يفوق POS/BNQ دقةً (يقاربه فقط MEM بثلاثية withhold/withdraw/overwrite).
- **مصفوفة تحويل المكالمات الحرفية:** مسموح Department→Room/Shop/Department؛ ممنوع Room→Department/Shop→Department/**Room→Room/Shop→Shop** — "should always be a department" — قاعدة اتجاه صريحة نادرة التوثيق كجدول.
- **وحدة تحكم عامل السنترال:** Guest Information (تعليمات/شكاوى/رسائل/موقع النزيل) بنمط **Tag→YES = أُبلّغ/وُجد → إخفاء من Guest Page Messages** (قائمة اتصالات نزلاء كلاسيكية) + **زر SL# الإداري الوحيد** (SysAdmin لحل تعارض SL# — طبيعته مجهولة UNK-053).
- **أزمة تسمية داخل وحدة واحدة:** Transfer = تحويل مكالمات (CAC/REP) أم تحويل غرف (LUK)! وExtension = امتداد هاتفي أم **تمديد إقامة** (View Transfers/Extensions يعرض المغادرة القديمة/الجديدة + **User + Authorizer** — أثر تدقيقي مزدوج)!
- **SMS الشبح (ثاني مقدمة-بلا-جسم):** مقدمة CAC تذكر "record and save standard SMSs... like checkins, anniversaries" — لا جسم في TOC الأربعة (GAP-TE-D01 + UNK-054) بعد Membership Tax Posting (فهرس-بلا-جسم).
- **رابعة بلا INI:** CARE/MEM/SLM/**TEL** + إحالة Module Attributes وحيدة (عرض المدة ثوانٍ/دقائق — فصل SUPERVISOR في SYS) — يتعمق نمط الجيل الأحدث (سمات داخلية بدل INI).
- **In-House Statistics مفوَّضة لـFO حرفياً:** "refer CHAPTER – LOOKUPS of MODULE – FRONT OFFICE" — أنقى تفويض موثق بعد BNQ=POS.
- **صلاحيات استنتاجية فقط:** لا قسم User Rights (رابعة) + أخطرها: إعادة الترحيل فعل مالي بلا ضابط + الشراكات بلا قفل تعديل (GAP-TE-D03).
- **غائبون:** لا جسر HRP (عائلة UNK-038) · لا Wake-up/Voice Mail كوظائف (قدرة 2-Way فقط — GAP-TE-D06) · لا خريطة GL (عائلة الفجوة العامة — D02).

**نقطة الاستئناف القادمة (الجلسة 13):**

1. **الوحدة التالية: MNT (الصيانة — 3 ملفات/81 ص: RPL 29 + OPR 28 + SET 24)** — `extracted-text/Maintenance/` — ثم FNB (4/76) ثم FXD+GTP (2/38) لإغلاق الـ17.
2. التقارير المؤجلة (REP) للوحدات محللة تبقى للمرحلة 7.
3. بعد الـ17: المراجعة الشاملة + cross-referencing + Knowledge Graph النهائي (Phase 8+).
