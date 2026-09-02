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
- [سجل المجهولات UNK-001..015](analysis/unknowns.md)
- [سجل التناقضات](analysis/contradictions.md) — (فارغ حتى الآن)

### نموذج المجال (Domain Model) — Phase 1
- [نظرة عامة على مجال الفندق](domain/hotel-domain-overview.md)
- [كيانات المجال (بالمصادر)](domain/entities.md)
- **[شبكة علاقات الكيانات — Knowledge Graph](domain/entity-relations.md)** ⭐
- [Master Data مقابل Transactions](domain/master-data.md)
- [كتالوج المعاملات ودورات الحياة](domain/transactions.md)
- [أدوار المستخدمين الفندقيين](domain/hotel-roles.md)
- **[القاموس الموحد للمصطلحات (عربي/EN)](domain/terminology.md)** ⭐

### الوحدات (Modules) — Phase 2/3 (فارغة — تُملأ بالترتيب: FOM أولاً)
`modules/front-office/` ← `financial-management/` ← `point-of-sale/` ← `accounts-receivable/` ← ...

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
