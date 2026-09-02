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
| Phase 2 | Module Inventory التفصيلي | ◐ **بدأت — FO محللة + FAS محللة** | `docs/modules/front-office/` + `docs/modules/financial-accounting/` |
| Phase 3 | Detailed Module Analysis | ◐ **الوحدتان 2/17: FO (19 ملفاً) + Financial Management (18 ملفاً)** | نفس المسارات |
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

## مؤشرات الجودة الحالية

| المؤشر | القيمة | الهدف |
|---|---|---|
| ملفات مفهرسة | 65/65 | 65/65 ✅ |
| نصوص مستخرجة | 65/65 | 65/65 ✅ |
| ملفات قرأت قراءة عميقة | **13/65** (FOM كامل عدا REP/SMS + FAS كامل عدا REP) | 65/65 |
| وحدات محللة وظيفياً | **2/17** (Front Office — 19 ملفاً + Financial Management — 18 ملفاً) | 17 |
| Knowledge Graph (علاقات موثقة) | 6 روابط ترحيل + 16 تكامل FO (I1-I16) | يوسَّع في Phase 3/6 |
| Unknowns مسجلة | انظر `docs/analysis/unknowns.md` | صفر حرج قبل التنفيذ |
