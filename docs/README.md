# فهرس قاعدة المعرفة (Knowledge Base Index)

> **مشروع:** Hotel ERP عربي أولاً — مبني على Frappe/ERPNext/HRMS + Frontend مخصص
> **المصدر المرجعي:** FortuneNext 6i Manuals (`6i Manuals/` — 65 ملف، 3,062 صفحة)
> **بروتوكول الجلسة الجديدة:** اقرأ `docs/analysis/00-discovery/analysis-status.md` ← `docs/analysis/source-coverage.md` ← أكمل من آخر نقطة.

---

## خريطة الوثائق

### التحليل والحالة (Analysis & Status)
- [خطة التنفيذ الكاملة للمراحل 1→16](analysis/00-discovery/execution-plan.md)
- [حالة المشروع — نقطة الدخول](analysis/00-discovery/analysis-status.md)
- [جرد الأدلة الـ 65](analysis/00-discovery/manual-inventory.md)
- [جرد الوحدات الـ 17](analysis/00-discovery/module-inventory.md)
- [خريطة الوثائق والتكاملات](analysis/00-discovery/document-map.md)
- [تتبع التغطية](analysis/source-coverage.md)
- [سجل المجهولات UNK-001..022](analysis/unknowns.md)
- [سجل التناقضات](analysis/contradictions.md) — (فارغ حتى الآن)

### نموذج المجال (Domain Model) — Phase 1
- [نظرة عامة على مجال الفندق](domain/hotel-domain-overview.md)
- [كيانات المجال (بالمصادر)](domain/entities.md)
- **[شبكة علاقات الكيانات — Knowledge Graph](domain/entity-relations.md)** ⭐
- [Master Data مقابل Transactions](domain/master-data.md)
- [كتالوج المعاملات ودورات الحياة](domain/transactions.md)
- [أدوار المستخدمين الفندقيين](domain/hotel-roles.md)
- **[القاموس الموحد للمصطلحات (عربي/EN)](domain/terminology.md)** ⭐

### الوحدات (Modules) — Phase 2/3 (5/17 محللة)

**1. Front Office (مكتملة — 19 ملفاً):** [`modules/front-office/`](modules/front-office/) — ابدأ بـ [`00-overview.md`](modules/front-office/00-overview.md) · ⭐ النواة المحاسبية: [`11-accounting-impact.md`](modules/front-office/11-accounting-impact.md) · الجرد: [`03-screens.md`](modules/front-office/03-screens.md) (193 شاشة) · القواعد: [`05-business-rules.md`](modules/front-office/05-business-rules.md) (BR-FO-01..16)

**2. Financial Management (مكتملة — 18 ملفاً):** [`modules/financial-accounting/`](modules/financial-accounting/) — ابدأ بـ [`00-overview.md`](modules/financial-accounting/00-overview.md) · ⭐ **النواة المعمارية للترحيل:** [`11-accounting-impact.md`](modules/financial-accounting/11-accounting-impact.md) (الروابط الست + قواعد Book Types + أمثلة بالأرقام) · القواعد: [`02-configuration.md`](modules/financial-accounting/02-configuration.md) · السير: [`04-workflows.md`](modules/financial-accounting/04-workflows.md) (WF-FA-01..16)

**3. Accounts Receivable (مكتملة — 19 ملفاً):** [`modules/accounts-receivable/`](modules/accounts-receivable/) — ابدأ بـ [`00-overview.md`](modules/accounts-receivable/00-overview.md) · ⭐ **الإقفال الشهري وسلسلة القفل الثلاثية:** [`10-transactions.md`](modules/accounts-receivable/10-transactions.md) (SOA/Rollback/Untagging) + [`11-accounting-impact.md`](modules/accounts-receivable/11-accounting-impact.md) (الترحيل التفاعلي عند الحفظ + INI المعكوسة) · القواعد: [`05-business-rules.md`](modules/accounts-receivable/05-business-rules.md) (BR-AR-01..14) · الحالات: [`13-exceptions.md`](modules/accounts-receivable/13-exceptions.md) (E-AR-01..30)

**4. Point of Sale (مكتملة — 19 ملفاً):** [`modules/point-of-sale/`](modules/point-of-sale/) — ابدأ بـ [`00-overview.md`](modules/point-of-sale/00-overview.md) · ⭐ **العمليات اليومية:** [`04-workflows.md`](modules/point-of-sale/04-workflows.md) (WF-POS-01..16: Shift/KOT/Check/Split/Settlement/Close) + [`11-accounting-impact.md`](modules/point-of-sale/11-accounting-impact.md) (التسويات الست + Guest→AR/FO) · الحالات: [`13-exceptions.md`](modules/point-of-sale/13-exceptions.md) (E-POS-01..30) · UX: [`15-ux-analysis.md`](modules/point-of-sale/15-ux-analysis.md) (دليل Touch Screen — أساس الواجهة الجديدة)

**5. System Setup (مكتملة — 19 ملفاً):** [`modules/system-setup/`](modules/system-setup/) — ابدأ بـ [`00-overview.md`](modules/system-setup/00-overview.md) · ⭐ **نموذج الصلاحيات الرباعي (يحسم UNK-013):** [`07-permissions.md`](modules/system-setup/07-permissions.md) · ⭐ **المرجعيات المشتركة + محرك الضرائب الثلاثي:** [`01-master-data.md`](modules/system-setup/01-master-data.md) (Code→Slab→Structure بأمثلة رقمية) · القرارات: [`16-erpnext-mapping.md`](modules/system-setup/16-erpnext-mapping.md) (F-SYS-1..12 — **Property=Company يحسم UNK-004**) · الفجوات: [`17-gap-analysis.md`](modules/system-setup/17-gap-analysis.md) (GAP-SYS-D01: وثيقة INI خارج الحزمة — يحسم UNK-022)

**التالي بالترتيب:** `materials-management/` (MGT — يحسم جزء UNK-011 Auto Indent) ← `banquets/` ← `hr-payroll/` ← ... (راجع `analysis/00-discovery/analysis-status.md` §نقطة الاستئناف)

### العمليات (Workflows) — Phase 5
`workflows/module-workflows/` + `workflows/end-to-end/`

### الشاشات (Screens) — Phase 4
`screens/screen-catalog.md` + `screens/specifications/`

### المحاسبة (Accounting) — Phase 6
`accounting/` — قواعد الترحيل الست الموثقة موجودة حالياً في `domain/entity-relations.md §3.2`

### التقارير/الأمان/نموذج البيانات/التكاملات/UX/التعريب
`reports/` `security/` `data-model/` `integrations/` `ux/` `localization/`

### المعمارية (Architecture) — Phase 11/13
`architecture/erpnext-mapping/` + `architecture/hotel-pms-core/` + `architecture/system-architecture/` + `architecture/frontend-backend/`

### الفجوات/التتبع/القرارات/التنفيذ — Phase 12/14/15
`gap-analysis/` `traceability/` `decisions/` `implementation/`

---

## أدوات التحليل المؤتمتة (Reusable)

| الأداة | الموقع | الوظيفة |
|---|---|---|
| `inventory_manuals.py` | `/home/z/my-project/scripts/` | استخراج نصوص الـ 65 PDF + ميتاداتا |
| `extract_tocs.py` | نفسه | استخراج فهارس الوثائق |
| `extract_fields.py` | نفسه | استخراج جداول الحقول (2,099 حقلاً → `field-extracts/`) |
| `extracted-text/` | `/home/z/my-project/hotel-erp/` | النصوص الكاملة مقسمة بصفحات PDF |
| `field-extracts/` | نفسه | الحقول الموثقة لكل شاشة إعداد |

## ملاحظات إرشادية لكل جلسة قادمة

1. لغة التوثيق: عربية + مصطلحات تقنية إنجليزية. المصدر يُذكر دائماً.
2. علامات الإثبات: `[NOT DOCUMENTED]` `[INFERENCE]` `[UNCERTAIN]` — إلزامية.
3. كل علاقة/مصطلح جديد يُضاف لـ `entity-relations.md` و`terminology.md` فوراً.
4. تحديث `source-coverage.md` (أعمدة deep-read/analyzed) و`analysis-status.md` (سجل الجلسة) في نهاية كل جلسة.
