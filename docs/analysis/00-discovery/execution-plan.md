# خطة التنفيذ التفصيلية (Execution Plan) — المراحل 1 → 16

> **الأساس:** هذه الخطة تحول منهجية البرومبت الرئيسي إلى خطوات قابلة للتنفيذ جلسةً بعد جلسة، مع نقاط استئناف واضحة (حسب قاعدة الاستمرارية).
> **مقياس الجلسة الواقعية:** قراءة عميقة لـ 150–400 صفحة مصدر + إنتاج وثائقها في كل جلسة. المشروع تقديرياً **8–15 جلسة عمل**.

---

## قواعد عامة إلزامية

1. **مسار القراءة:** `extracted-text/<Module>/<file>.txt` (النص الكامل مقسوم بـ `===== PAGE N =====`).
2. **التوثيق بالإثبات:** كل حقيقة وظيفية مهمة تُوثق بالمصدر: `(المصدر: FN6i-NT-FOM-RES.pdf — صفحة XX)`. غير موثق → `[NOT DOCUMENTED]`. استنتاج → `[INFERENCE]`. غير متأكد → `[UNCERTAIN]`.
3. **قاعدة الذاكرة الدائمة:** كل معرفة تُحفظ في `docs/` فور استخراجها. لا تُترك في ذاكرة الجلسة.
4. **Knowledge Graph تراكمي:** كل علاقة بين كيانين (مثل Reservation→Folio) تُسجل في `docs/domain/entity-relations.md` وتُحدَّث كل جلسة.
5. **Quality Gate بين المراحل:** checklist في نهاية كل مرحلة (اكتمال، اتساق، تتبع، صلاحيات، محاسبة، حالات خاصة) قبل الانتقال.

---

## Phase 1 — Domain Model (الحالية)

**الهدف:** استخراج نموذج مجال فندقي كامل من الوثائق (كيانات، بيانات رئيسية، معاملات، دورات حياة، أدوار، مصطلحات).

**خطوات:**

| # | المهمة | المصادر | المخرج |
|---|---|---|---|
| 1.1 | كيانات Front Office (النواة) | FOM-SET/RES/REG/CAS/DEP | `domain/entities.md` (قسم FO) |
| 1.2 | كيانات الإيراد: POS/BNQ/MEM/TEL | POS-SET, BNQ-CFG/SET, MEM-MPF/SET, TEL-SET | `domain/entities.md` (أقسامها) |
| 1.3 | كيانات التكلفة: MGT/FNB/FXD | MGT-SET, FNB-SET, FAS-FXD | `domain/entities.md` (أقسامها) |
| 1.4 | كيانات الأشخاص: HRP/SLM/Care | HRP-SET, SLM-PRF, Care-SET | `domain/entities.md` (أقسامها) |
| 1.5 | تصنيف Master Data مقابل Transactions | كل ما سبق | `domain/master-data.md` + `domain/transactions.md` |
| 1.6 | دورات حياة الكيانات الرئيسية | RES/REG/CAS/MGT-DNT/MMN | `domain/entity-lifecycles.md` |
| 1.7 | الأدوار (Roles) | SYS-SSP + أدوار وردت في الوثائق | `domain/hotel-roles.md` |
| 1.8 | قاموس المصطلحات التأسيسي | كل الوثائق (تراكمي) | `domain/terminology.md` |
| 1.9 | مخطط علاقات الكيانات (Knowledge Graph) | كل ما سبق | `domain/entity-relations.md` |

**Definition of Done (DoD):** كل كيان له: تعريف، غرض، حقول أساسية (إن وُثقت)، علاقات، دورة حياة، وحدات مستخدمة. لا كيان بلا مصدر.

---

## Phase 2 — Module Inventory التفصيلي

لكل وحدة من الـ 17: إنشاء `docs/modules/<module>/00-overview.md` يتضمن حدود الوحدة، وحداتها الفرعية، قائمة شاشاتها (من الفهارس + النص)، مستخدميها، وتفاعلاتها المعروفة.

**DoD:** 17 ملف overview، كل شاشة مذكورة في الفهارس مسجلة باسمها ومصدرها.

---

## Phase 3 — Detailed Module Analysis (الأثقل)

لكل وحدة (بالترتيب: FOM ← FAS ← POS ← ACR ← MGT ← FNB ← BNQ ← MEM ← HRP ← MNT ← Care ← TEL ← SLM ← FXD ← GTP ← SYS ← TSC):

إنشاء الهيكل القياسي الـ 19 ملفاً في `docs/modules/<module>/`:
`00-overview, 01-master-data, 02-configuration, 03-screens, 04-workflows, 05-business-rules, 06-validations, 07-permissions, 08-reports, 09-lookups, 10-transactions, 11-accounting-impact, 12-integrations, 13-exceptions, 14-data-model, 15-ux-analysis, 16-erpnext-mapping, 17-gap-analysis, 18-acceptance-criteria`.

**إيقاع العمل:** وثيقة مصدر واحدة تُقرأ كاملة ← تُستخرج معارفها إلى الملفات المعنية ← تُعلَّم في coverage.md ← ثم التالية.
**DoD:** لكل شاشة رئيسية: Screen Spec (وفق قالب §7 من البرومبت) في `docs/screens/specifications/`.

---

## Phase 4 — Screens & UX

- تجميع `docs/screens/screen-catalog.md` من كل الوثائق.
- مواصفات الشاشات الكاملة (Fields/Actions/State/Rules/Side Effects) للشاشات الجوهرية (~40–60 شاشة تقديرياً).
- تحليل UX: information architecture + تقسيم Desktop/Tablet/Mobile/POS-Touch من سلوك الاستخدام الموثق (مثلاً Touch Screen Manual = مرجع POS اللمسي).
- مخرجات `docs/ux/`: navigation-model, screen-groups, device-matrix, rtl-arabic-ux-guidelines.

## Phase 5 — Workflows

- `docs/workflows/module-workflows/` لكل عملية داخلية.
- `docs/workflows/end-to-end/` للعمليات العابرة للوحدات — **يُبنى من الروابط المكتشفة في document-map.md §1–6**: Guest Journey، Night Audit، POS→GL، Procure-to-Pay، Banquet، Membership، Payroll، Maintenance.
- لكل workflow: Happy Path + Alternative + Exception + محاسبة + أثر على الوحدات.

## Phase 6 — Accounting (حرجة)

- من FAS-SET (الروابط الست) + FAS-TRN + كل وثائق "Impact" في الوحدات.
- `docs/accounting/`: posting-rules لكل وحدة، folio-accounting، night-audit-accounting، دورة AR، إلخ.
- **قاعدة صارمة:** لا قيد محاسبي يُخترع. غير موجود → `[NOT DOCUMENTED]` + Unknown.

## Phase 7 — Reports

- كتالوج كل التقارير (~15 وثيقة REP/RPL ≈ 900 صفحة): الاسم، الغرض، المرشحات، الأعمدة، المصدر، الصلاحيات.

## Phase 8 — Security & Permissions

- من SYS-SSP + Transaction Type Rights (FAS) + AR User Access + Care Rights: `roles.md`, `permissions.md`, `role-capability-matrix.md`, `segregation-of-duties.md`.

## Phase 9 — Data Model

- `docs/data-model/`: entities/relationships/lifecycle + نماذج خاصة (room-model, guest-model, folio-model, inventory-model, multi-property, multi-currency).

## Phase 10 — Cross-Module Integration

- `docs/integrations/`: توثيق كل نقاط التكامل (الروابط الست + TEL posting + POS→folio + Auto Indent + Post Subscription to AR...) كعقود تدفق بيانات.

## Phase 11 — ERPNext/Frappe/HRMS Mapping

- لكل وظيفة: `FortuneNext Function → ERPNext Capability → Fit Level (A–F) → Implementation Strategy`.
- مقارنة **semantics** (lifecycle/accounting/permissions) لا أسماء المستندات فقط (قاعدة §16).

## Phase 12 — Gap Analysis

- لكل فجوة: requirement/source/ERPNext capability/gap/severity/solution/complexity/dependencies.

## Phase 13 — Architecture

- `docs/architecture/system-architecture/` (حدود النظام، Frappe Apps، Custom Apps، الوظائف المجدولة مثل Night Audit) + `hotel-pms-core/` (حدود PMS الخاصة بنا) + `frontend-backend/` (API contracts، authentication، realtime، background jobs).

## Phase 14 — Traceability

- مصفوفات: Manual→Module→Feature→Screen→Rule→Entity→Mapping→Task→Test.

## Phase 15 — Implementation Roadmap

- `docs/implementation/`: roadmap، epics، features قابلة للتحويل لمهام coding agents، dependencies، milestones، testing-strategy.

## Phase 16 — Verification & Quality Gate

- مراجعة نهائية شاملة + مصفوفة قبول + إغلاق كل Unknowns أو تحويلها لقرارات موثقة.

---

## ترتيب الوحدات القياسي (للمراحل 3–11)

```
1. FOM  Front Office        (11 وثيقة، 747 ص)   — نواة PMS
2. FAS  Financial Mgmt      (5 وثائق، 218 ص)    — المحور المحاسبي
3. POS  Point of Sale       (4، 350 ص)
4. ACR  Accounts Receivable (5، 89 ص)
5. MGT  Materials Mgmt      (4، 293 ص)
6. FNB  F&B Costing         (4، 76 ص)
7. BNQ  Banquets            (5، 255 ص)
8. MEM  Membership          (5، 133 ص)
9. HRP  HR & Payroll        (4، 253 ص)
10. MNT Maintenance         (3، 81 ص)
11. CARE Fortune Care       (3، 187 ص)
12. TEL  Telephones         (4، 83 ص)
13. SLM  Sales & Marketing  (4، 103 ص)
14. FXD  Fixed Assets       (1، 25 ص)
15. GTP  Gate Passes        (1، 13 ص)
16. SYS  System Setup       (1، 110 ص)
17. TSC  Touch Screen       (1، 46 ص)
```

---

## إدارة المخاطر

| الخطر | الاحتمال | الأثر | التخفيف |
|---|---|---|---|
| ضياع السياق بين الجلسات | متوسط | عالٍ | analysis-status.md + coverage.md + worklog.md قبل/بعد كل جلسة |
| اختلاق معلومات غير موثقة | متوسط | عالٍ جداً | قاعدة الإثبات بالمصدر + علامات [INFERENCE]/[NOT DOCUMENTED] |
| تكرار عمل منجز | منخفض | متوسط | علامات deep-read/analyzed في coverage.md |
| غرق في تفاصيل شاشة واحدة | متوسط | متوسط | قاعدة: الشاشة تُوثق بمستواها الموثق في المصدر فقط |
| فقدان العلاقات العابرة للوحدات | متوسط | عالٍ | entity-relations.md تراكمي + تحديثه كل جلسة |
