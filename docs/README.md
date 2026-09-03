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

### الوحدات (Modules) — Phase 2/3 (14/17 محللة)

**1. Front Office (مكتملة — 19 ملفاً):** [`modules/front-office/`](modules/front-office/) — ابدأ بـ [`00-overview.md`](modules/front-office/00-overview.md) · ⭐ النواة المحاسبية: [`11-accounting-impact.md`](modules/front-office/11-accounting-impact.md) · الجرد: [`03-screens.md`](modules/front-office/03-screens.md) (193 شاشة) · القواعد: [`05-business-rules.md`](modules/front-office/05-business-rules.md) (BR-FO-01..16)

**2. Financial Management (مكتملة — 18 ملفاً):** [`modules/financial-accounting/`](modules/financial-accounting/) — ابدأ بـ [`00-overview.md`](modules/financial-accounting/00-overview.md) · ⭐ **النواة المعمارية للترحيل:** [`11-accounting-impact.md`](modules/financial-accounting/11-accounting-impact.md) (الروابط الست + قواعد Book Types + أمثلة بالأرقام) · القواعد: [`02-configuration.md`](modules/financial-accounting/02-configuration.md) · السير: [`04-workflows.md`](modules/financial-accounting/04-workflows.md) (WF-FA-01..16)

**3. Accounts Receivable (مكتملة — 19 ملفاً):** [`modules/accounts-receivable/`](modules/accounts-receivable/) — ابدأ بـ [`00-overview.md`](modules/accounts-receivable/00-overview.md) · ⭐ **الإقفال الشهري وسلسلة القفل الثلاثية:** [`10-transactions.md`](modules/accounts-receivable/10-transactions.md) (SOA/Rollback/Untagging) + [`11-accounting-impact.md`](modules/accounts-receivable/11-accounting-impact.md) (الترحيل التفاعلي عند الحفظ + INI المعكوسة) · القواعد: [`05-business-rules.md`](modules/accounts-receivable/05-business-rules.md) (BR-AR-01..14) · الحالات: [`13-exceptions.md`](modules/accounts-receivable/13-exceptions.md) (E-AR-01..30)

**4. Point of Sale (مكتملة — 19 ملفاً):** [`modules/point-of-sale/`](modules/point-of-sale/) — ابدأ بـ [`00-overview.md`](modules/point-of-sale/00-overview.md) · ⭐ **العمليات اليومية:** [`04-workflows.md`](modules/point-of-sale/04-workflows.md) (WF-POS-01..16: Shift/KOT/Check/Split/Settlement/Close) + [`11-accounting-impact.md`](modules/point-of-sale/11-accounting-impact.md) (التسويات الست + Guest→AR/FO) · الحالات: [`13-exceptions.md`](modules/point-of-sale/13-exceptions.md) (E-POS-01..30) · UX: [`15-ux-analysis.md`](modules/point-of-sale/15-ux-analysis.md) (دليل Touch Screen — أساس الواجهة الجديدة)

**5. System Setup (مكتملة — 19 ملفاً):** [`modules/system-setup/`](modules/system-setup/) — ابدأ بـ [`00-overview.md`](modules/system-setup/00-overview.md) · ⭐ **نموذج الصلاحيات الرباعي (يحسم UNK-013):** [`07-permissions.md`](modules/system-setup/07-permissions.md) · ⭐ **المرجعيات المشتركة + محرك الضرائب الثلاثي:** [`01-master-data.md`](modules/system-setup/01-master-data.md) (Code→Slab→Structure بأمثلة رقمية) · القرارات: [`16-erpnext-mapping.md`](modules/system-setup/16-erpnext-mapping.md) (F-SYS-1..12 — **Property=Company يحسم UNK-004**) · الفجوات: [`17-gap-analysis.md`](modules/system-setup/17-gap-analysis.md) (GAP-SYS-D01: وثيقة INI خارج الحزمة — يحسم UNK-022)

**6. Materials Management (مكتملة — 19 ملفاً):** [`modules/materials-management/`](modules/materials-management/) — ابدأ بـ [`00-overview.md`](modules/materials-management/00-overview.md) · ⭐ **دورة التوريد الكاملة + الإقفال الشهري:** [`04-workflows.md`](modules/materials-management/04-workflows.md) (WF-MG-01..19: PR→PO→GR→Issue→Physical→Variance→Ledger) · ⭐ **القواعد الدستورية:** [`05-business-rules.md`](modules/materials-management/05-business-rules.md) (BR-MG-01..18: هرمية المخازن + WA/FIFO لكل مخزن + قواعد التواريخ العشر) · التقييم المحاسبي: [`11-accounting-impact.md`](modules/materials-management/11-accounting-impact.md) (MM→FAS + Bill#→Payment Match) · القرارات: [`16-erpnext-mapping.md`](modules/materials-management/16-erpnext-mapping.md) (F-MG-1..12 — ⭐ **محرك التقييم لكل مخزن F-MG-1 + FEFO F-MG-2** — أعلى قابلية إسقاط قياسي: Material Request/Purchase Receipt/Stock Reconciliation/Repack)

**7. Banquets (مكتملة — 19 ملفاً):** [`modules/banquets/`](modules/banquets/) — ابدأ بـ [`00-overview.md`](modules/banquets/00-overview.md) · ⭐ **حسم UNK-011 كاملاً — سلسلة Auto Indent:** [`12-integrations.md`](modules/banquets/12-integrations.md) §2.2 (Requirement→Pre Costing→Auto Indent→MGT) + [`04-workflows.md`](modules/banquets/04-workflows.md) (WF-BQ-08..10) · ⭐ **الوحدة الهجينة FO×POS (قرار F-BQ-1):** [`16-erpnext-mapping.md`](modules/banquets/16-erpnext-mapping.md) (BNQ فوق محرك POS) · دورة الحجز والودائع: [`05-business-rules.md`](modules/banquets/05-business-rules.md) (BR-BQ-01..16 — Across-Dates + قفل الودائع + ليست مبيعات) · لوحة العمليات: [`09-lookups.md`](modules/banquets/09-lookups.md) (Availability Chart — أعلى مكون ترجمة Frontend)

**8. HR & Payroll (مكتملة — 19 ملفاً):** [`modules/hrp-payroll/`](modules/hrp-payroll/) — ابدأ بـ [`00-overview.md`](modules/hrp-payroll/00-overview.md) · ⭐ **محرك الأجور المعادلاتي (قرار F-HR-1):** [`01-master-data.md`](modules/hrp-payroll/01-master-data.md) (ED Calculation: 6 أنماط × 3 حساب × 4 مصادر × **شرائح 4 أنواع بأمثلة رقمية 500/350/400** + Priority/Partial/CarryForward) + [`16-erpnext-mapping.md`](modules/hrp-payroll/16-erpnext-mapping.md) (أربعة أصول مخصصة فقط) · ⭐ **جسر AR→Payroll (الحلقة الرابعة المغلقة):** [`12-integrations.md`](modules/hrp-payroll/12-integrations.md) (I-HR-01 — يوسع Knowledge Graph بعلاقة S10) · قواعد الخصم القطعية: [`05-business-rules.md`](modules/hrp-payroll/05-business-rules.md) (BR-HR-06/07 — أرباح 1500/خصم 1700: Yes=كامل! No=صفر!) · التقارير: [`08-reports.md`](modules/hrp-payroll/08-reports.md) (68 تقريراً/19 مجموعة — 15 نموذجاً هندياً رسمياً + Payroll Audit بقيم old/new)

**9. Care (مكتملة — 19 ملفاً):** [`modules/care/`](modules/care/) — ابدأ بـ [`00-overview.md`](modules/care/00-overview.md) · ⭐ **UNK-010 محسوم نهائياً (مخزنان مستقلان + 7 قنوات PMS):** [`12-integrations.md`](modules/care/12-integrations.md) (I-CA-01..06 — Care وحدة ساتلية PMS-centric بلا أي جسر إلى HRP!) · ⭐ **محرك SMS ثنائي الاتجاه الفريد (`1 S`/`1 C` + 5 رسائل خطأ حرفية + 14 حالة):** [`04-workflows.md`](modules/care/04-workflows.md) (WF-CA-04/05 — المنفذ الحقلي بلا شاشة!) + [`13-exceptions.md`](modules/care/13-exceptions.md) (جدول الأخطاء↔ردود النظام) · الهيكل والتصعيد: [`01-master-data.md`](modules/care/01-master-data.md) (سلسلة Reporting: Room boy→…→MD بمهلات دقائق) · أعلى كفاءة بذرة Frappe: [`16-erpnext-mapping.md`](modules/care/16-erpnext-mapping.md) (F-CA-1..10 — 4 أصول مخصصة فقط ~2-3 أسابيع)

**10. Membership (مكتملة — 19 ملفاً):** [`modules/membership/`](modules/membership/) — ابدأ بـ [`00-overview.md`](modules/membership/00-overview.md) · ⭐ **جسر MEMC001 (أول إنشاء كيان AR تلقائي) + 5 محركات ترحيل:** [`12-integrations.md`](modules/membership/12-integrations.md) (I-ME-01/02 — شركة ACR من حرف اسم العائلة بلا رجعة! + Subscription/Facility/Cover/Late الانتقائي بثلاثية withhold/withdraw/overwrite) · ⭐ **دورة الانضمام الرباعية + الإنهاء المتتالي:** [`04-workflows.md`](modules/membership/04-workflows.md) (WF-ME-02..07 — طلب→فحص→مقابلة→تحويل/خلافة الوفاة بنمط None) + [`05-business-rules.md`](modules/membership/05-business-rules.md) (BR-ME-08 — التتالي الهابط الحرفي ×4) · المثال الرقمي لرسوم التأخير (يناير→ديسمبر) والفوترة الثلاثية الشرائح: [`11-accounting-impact.md`](modules/membership/11-accounting-impact.md) · **أول فجوة فهرس-بلا-جسم (Tax Posting):** [`17-gap-analysis.md`](modules/membership/17-gap-analysis.md) (GAP-ME-D01/UNK-045) · التقارير كمساحة عمل (حفر 3 مستويات + بريد): [`09-lookups.md`](modules/membership/09-lookups.md)

**11. Sales & Marketing (مكتملة — 19 ملفاً):** [`modules/sales-marketing/`](modules/sales-marketing/) — ابدأ بـ [`00-overview.md`](modules/sales-marketing/00-overview.md) · ⭐ **مركز الائتمان داخل وحدة تسويقية (القفل الثلاثي FO/POS/BNQ+يدوي):** [`05-business-rules.md`](modules/sales-marketing/05-business-rules.md) (BR-SM-01 + `11-accounting-impact.md` — صفر قيود GL: كل الأثر مفوَّض عبر الحدود!) · ⭐ **دورة Prospect→CGR بتوليد كود آلي TTT+حرف+مسلسل:** [`04-workflows.md`](modules/sales-marketing/04-workflows.md) (WF-SM-01 — تطابق Lead→Customer الحرفي) + [`12-integrations.md`](modules/sales-marketing/12-integrations.md) (جسر Company Profile لسبع وحدات نصاً + INI جديدان 239/41-المقلوب + Module Attribute #8) · **أول CRM 360°:** [`03-screens.md`](modules/sales-marketing/03-screens.md) (Sales Manager Tool بعشرة عروض + Hotel Position) · **الصلاحيات الصفرية (GAP-SM-D04):** [`07-permissions.md`](modules/sales-marketing/07-permissions.md) (P-SM-1..5) · **أفضل موائمة ERPNext في المشروع:** [`16-erpnext-mapping.md`](modules/sales-marketing/16-erpnext-mapping.md) (F-SM-1..8 — 8 أصول فقط، قلب CRM منصة-جاهز)

**12. Telephone Management (مكتملة — 19 ملفاً):** [`modules/telephone/`](modules/telephone/) — ابدأ بـ [`00-overview.md`](modules/telephone/00-overview.md) · ⭐ **بوابة العتاد المزدوجة الفريدة (EPABX Serial + أقفال Onity):** [`12-integrations.md`](modules/telephone/12-integrations.md) (I-TE-01..13 — نمط «حفظ خلفي → برنامج وسيط → جهاز» المعياري لكل تكاملات العتاد + 2-Way التحكم العكسي بالهواتف/المنبهات/حالة الغرفة!) · ⭐ **محرك التسعير النبضي الكامل (النص الوحيد بأرقام حرفية قابلة للاختبار):** [`05-business-rules.md`](modules/telephone/05-business-rules.md) (BR-TE-01..24 — 60c×100/150/200% + 0% الممنوعة لSTD/IDD + الشراكات الست بأغلى تعرفة) + [`13-exceptions.md`](modules/telephone/13-exceptions.md) (**سباق تسجيل الوصول الجماعي** الموثق: مفاتيح بلا PMS! + 4 حالات خطأ + ازدواج Transfer/Extension) · خلود الشرائح الزمنية: [`01-master-data.md`](modules/telephone/01-master-data.md) (لا تعديل — أحدث Applicable From يفوز، مثال 2011/2012) · وحدة تحكم العامل: [`09-lookups.md`](modules/telephone/09-lookups.md) (Guest Information بأزرار التعليمات/الشكاوى/الرسائل/الموقع + Tag-YES + زر SL# الإداري) · إعادة الترحيل المالي: [`10-transactions.md`](modules/telephone/10-transactions.md) (T-TE-06 Select→YES) · SMS الشبح: [`17-gap-analysis.md`](modules/telephone/17-gap-analysis.md) (GAP-TE-D01 + UNK-054)

**13. Maintenance (مكتملة — 19 ملفاً):** [`modules/maintenance/`](modules/maintenance/) — ابدأ بـ [`00-overview.md`](modules/maintenance/00-overview.md) · ⭐ **اللون أداة سير عمل + جهاز الإسناد المشرفي (NO→YES × أولوية × موظف/مزوّد):** [`04-workflows.md`](modules/maintenance/04-workflows.md) (WF-MN-01..13 — دورات الشكوى/الوقائية/القراءات/الورديات تتقاطع عند Job Order Generation) + [`05-business-rules.md`](modules/maintenance/05-business-rules.md) (BR-MN-01..22 — بوابتا ENG#1/#2 + Must-Complete-By ≤ Lag) · ⭐ **شرِكة الهروب الأطول (صنف مفتوح 999999999999 — 12 تسعة!):** [`13-exceptions.md`](modules/maintenance/13-exceptions.md) (بلا أثر مخزني + خمود الماسترات + استعلام يُحرّر) · ⭐ **أفضل تواءم تشغيلي (يضاهي SLM/Care):** [`16-erpnext-mapping.md`](modules/maintenance/16-erpnext-mapping.md) (F-MN-1..12 — Issue + Asset Maintenance + **Asset Repair بحل P3 جذرياً عبر Stock Entry!** + Shift Assignment — ~6 أصول/3-4 أسابيع) · ⭐ **صفر قيود GL بنمط «الجزيرة المعزولة» (بلا تفويض حتى):** [`11-accounting-impact.md`](modules/maintenance/11-accounting-impact.md) · جسر MGT الاستعاري (مخازن/مراكز/أصناف): [`12-integrations.md`](modules/maintenance/12-integrations.md) (I-MN-01..12 — مخزن الموظفين **الخامس** + Parameter Listing العابر للوحدات إلى Excel!) · الاستعلام المعدِّل: [`09-lookups.md`](modules/maintenance/09-lookups.md) (Complaint Status Q + Job Order Help رباعي المعايير) · الفجوات: [`17-gap-analysis.md`](modules/maintenance/17-gap-analysis.md) (**P3 استهلاك بلا خصم مخزني — الأخطر** + P1..P5 كلها تُغلق بأصول Frappe مجانية تقريباً)

**14. Food & Beverage Costing (مكتملة — 19 ملفاً):** [`modules/food-beverage-costing/`](modules/food-beverage-costing/) — ابدأ بـ [`00-overview.md`](modules/food-beverage-costing/00-overview.md) · ⭐ **Recipe = BOM حرفياً (أنقى سقوط وحدة على أصول ERPNext):** [`16-erpnext-mapping.md`](modules/food-beverage-costing/16-erpnext-mapping.md) (F-FB-1..12 — **Sub Recipe = نصف مصنّع متداخل + Yield% + Process≈Routing** + Stock Reconciliation للجرد + Material Request للAuto Indent + Budget للموازنة — ~6 أصول/~4-5 أسابيع) · ⭐ **بوابة التفعيل الأحادية + الحاجب اللحظي العكسي (SWITCH 511 يمنع البيع في POS ذاته!):** [`05-business-rules.md`](modules/food-beverage-costing/05-business-rules.md) (BR-FB-01..26 — قفل دائم لStart Date + INI#368 Batch/Online + COST% بالمعادلة الحرفية) + [`02-configuration.md`](modules/food-beverage-costing/02-configuration.md) · ⭐ **دورة الجرد اليومي/السنوي (فعلي↔حاسوبي → افتتاحي الغد):** [`04-workflows.md`](modules/food-beverage-costing/04-workflows.md) (WF-FB-01..13 — التأسيس لمرة ثم الدورة الأبدية + Auto Indent الخالد إلى MGT) + [`10-transactions.md`](modules/food-beverage-costing/10-transactions.md) (T-FB-01..14 — التحول الثلاثي بتحويل قيمي **بلا أصناف**) · ⭐ **صفر قيود GL بأنقاء OLAP فوق OLTP:** [`11-accounting-impact.md`](modules/food-beverage-costing/11-accounting-impact.md) · ⭐ **أول تناقض داخلي مسجل (C-FB-01 — أقواس Standard/Actual المعكوسة):** [`13-exceptions.md`](modules/food-beverage-costing/13-exceptions.md) + [`09-lookups.md`](modules/food-beverage-costing/09-lookups.md) (XOR المنهجي + No-Drill-Down معلنة + Lookup-as-Editor للمعدلات) · 13 تقريراً بـForecast/YTD/80-132 عموداً: [`08-reports.md`](modules/food-beverage-costing/08-reports.md) · الفجوات: [`17-gap-analysis.md`](modules/food-beverage-costing/17-gap-analysis.md) (سادسة بلا صلاحيات + بوابة بلا إنعاش + Auto Indent خالد — UNK-063..067)

**التالي بالترتيب:** `fixed-assets + gate-passes` (FXD 25 + GTP 13 — **إغلاق الـ17/17**) ← ثم المراجعة الشاملة (راجع `analysis/00-discovery/analysis-status.md` §نقطة الاستئناف)

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
