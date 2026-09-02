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
| Phase 2 | Module Inventory التفصيلي | ◐ **بدأت — Front Office محللة** | `docs/modules/front-office/00-overview.md` + هيكل 19 ملفاً كاملاً |
| Phase 3 | Detailed Module Analysis | ◐ **الوحدة 1/17 (Front Office) — 19 ملفاً بمحتوى موثق** | `docs/modules/front-office/` (00→18) |
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

## مؤشرات الجودة الحالية

| المؤشر | القيمة | الهدف |
|---|---|---|
| ملفات مفهرسة | 65/65 | 65/65 ✅ |
| نصوص مستخرجة | 65/65 | 65/65 ✅ |
| ملفات قرأت قراءة عميقة | **5/65** (FOM: DEP+RES+REG+CAS كاملة + SET جزئي) | 65/65 |
| وحدات محللة وظيفياً | **1/17** (Front Office — 19 ملفاً) | 17 |
| Knowledge Graph (علاقات موثقة) | 6 روابط ترحيل + 16 تكامل FO (I1-I16) | يوسَّع في Phase 3/6 |
| Unknowns مسجلة | انظر `docs/analysis/unknowns.md` | صفر حرج قبل التنفيذ |
