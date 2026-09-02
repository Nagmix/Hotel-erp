# Hotel ERP — مشروع نظام إدارة فندقي متكامل (عربي أولاً)

> **هندسة عكسية وظيفية** لنظام FortuneNext 6i الفندقي (IDS Next) → بناء ERP فندقي متكامل عربي بالكامل (Arabic-First + RTL-First) فوق منصة **Frappe Framework + ERPNext + Frappe HRMS** مع واجهة مستخدم مخصصة بالكامل (**Next.js + React + TypeScript + Tailwind CSS + shadcn/ui**).

---

## 🎯 هوية المشروع

| البند | القيمة |
|---|---|
| **الهدف** | ERP فندقي متكامل يغطي 17 وحدة وظيفية (Front Office, POS, Finance, HR, Membership, Banquets, Materials, Maintenance...) |
| **اللغة** | عربي أولاً — RTL من التصميم الأساسي، وليس ترجمة لاحقة |
| **الشفافية للمعمارية** | ERPNext Desk ليس الواجهة — المستخدم النهائي لا يعرف أن الخلفية Frappe/ERPNext |
| **المرجع الوظيفي** | كتالوجات FortuneNext 6i (65 ملف / ~3,062 صفحة) — تُحلَّل وظيفياً (Business Requirements فقط) دون نسخ أي كود أو تصميم |
| **المرحلة الحالية** | التحليل والتوثيق والهندسة — **لا برمجة قبل اكتمال التحليل** (DOCUMENT FIRST) |

## 📂 هيكل المستودع

```
docs/                    ← قاعدة المعرفة (المنتج الأساسي الحالي)
├── analysis/            ← Phase 0: فهرسة المصادر + التغطية + المجهولات + التناقضات
├── domain/              ← Phase 1: نموذج المجال (كيانات، علاقات، مصطلحات، أدوار)
├── modules/             ← Phase 2-3: تحليل تفصيلي لكل وحدة (هيكل 19 ملفاً لكل وحدة)
├── workflows/  screens/  accounting/  reports/  security/  data-model/
├── integrations/  ux/  localization/  architecture/  gap-analysis/
└── traceability/  decisions/  implementation/
tools/                   ← سكربتات استخراج وفهرسة الأدلة (Python)
inventory.json           ← فهارس الميتاداتا (أسماء الملفات/الصفحات) — بدون محتوى محمي
```

> ⚠️ **ملاحظة قانونية:** أدلة FortuneNext 6i الأصلية (PDF) ونصوصها المستخرجة ملكية لشركة IDS Next ومحمية بحقوق النشر، لذا **لا تُرفع إلى هذا المستودع**. هذا المستودع يحتوي على وثائق التحليل والهندسة (متطلبات الأعمال المستخلصة) وأدواتنا البرمجية فقط.

## 📖 نقطة البداية للقراءة

1. [`docs/analysis/00-discovery/analysis-status.md`](docs/analysis/00-discovery/analysis-status.md) — حالة المشروع ونقطة الاستئناف (ابدأ هنا دائماً)
2. [`docs/analysis/00-discovery/execution-plan.md`](docs/analysis/00-discovery/execution-plan.md) — خطة التنفيذ التفصيلية (المراحل 1-16)
3. [`docs/domain/hotel-domain-overview.md`](docs/domain/hotel-domain-overview.md) — نظرة عامة على مجال الفندقة المكتشف
4. [`docs/domain/terminology.md`](docs/domain/terminology.md) — القاموس الموحد (EN ↔ FortuneNext ↔ عربي ↔ UI Label ↔ Code)

## 🔄 بروتوكول الاستمرارية (Session Protocol)

الوثائق هي الذاكرة الدائمة للمشروع. كل جلسة عمل:
اقرأ `analysis-status.md` ← `source-coverage.md` ← حدّد آخر نقطة مكتملة ← أكمل منها ← حدّث الحالة. لا يُعاد عمل منجز إلا لسبب موثق.

## 🧭 المنهجية

- **Evidence-Based Analysis** — كل معلومة موثقة بمصدرها (ملف/قسم/صفحة). المسموح: `[UNCERTAIN]` / `[NOT DOCUMENTED]` / `[INFERENCE]`
- **Quality Gate** بين كل مرحلة والتي تليها — لا انتقال قبل استيفاء معايير الخروج
- **Knowledge Graph** وظيفي — علاقات وتبعيات موثقة بين الوحدات
- **Mapping إلى ERPNext** بتصنيف A-F (موجود مباشرة → يُبنى من الصفر)

---

*آخر تحديث للحالة: انظر `docs/analysis/00-discovery/analysis-status.md`*
