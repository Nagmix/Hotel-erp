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
- [سجل المجهولات UNK-001..102](analysis/unknowns.md)
- [سجل التناقضات (12)](analysis/contradictions.md)

### التجميع النهائي (Synthesis) — Phase 8
- ⭐⭐ **[فهرس التجميع](analysis/01-synthesis/README.md)** — نقطة الدخول للمعرفة الموحدة بعد إغلاق 65/65
- **[Knowledge Graph النهائي](analysis/01-synthesis/01-knowledge-graph.md)** — الطوبولوجيا (طبقات 5 + درجات اتصال) + الجسور الموحدة (مالية/سلوكية/ورقية) + **20 عائلة عابرة** + مصفوفة INI/MA الكاملة (27 مفتاحاً) + **8 قوانين معمارية (L1-L8)** + نقاط الالتفاف الحرجة
- **[مصفوفة القرارات المجمعة](analysis/01-synthesis/02-decision-matrix.md)** — ~128 قرار D/E من 20 وحدة + **العشرة P0 الحرجة** + 8 مجموعات موضوعية + ترتيب الحسم
- **[جدول المرادفات والمعجم الموحد](analysis/01-synthesis/03-synonyms-glossary.md)** — حل C-FA-01 (جسر بثلاثة أسماء) + معجم ADQ/ADC/POT + قاموس اختصارات الحزمة + الأنماط الدلالية
- **[خريطة إغلاق المجهولات](analysis/01-synthesis/04-unknowns-closure-map.md)** — تدقيق 102: 55 قراراً · 30 استنتاجاً · 12 ميدانياً · 5 تسقط — بجدولة زمنية

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

**15. Fixed Assets (مكتملة — 19 ملفاً):** [`modules/fixed-assets/`](modules/fixed-assets/) — ابدأ بـ [`00-overview.md`](modules/fixed-assets/00-overview.md) · ⭐ **أول وحدة موجبة القيود كاملة المواصفة بعد FAS (البند F12):** [`11-accounting-impact.md`](modules/fixed-assets/11-accounting-impact.md) (الربط الرباعي BS×2/PL×2 لكل Sub Group + ترحيل شهري **بتاريخ نهاية الشهر وSLM حصراً** بينما يُحسب WDV ولا يُرحَّل!) + [`12-integrations.md`](modules/fixed-assets/12-integrations.md) (I-FX-01..09 — جسر F12 + تقاطع كياني صامت مع MNT: Equipment≠Asset) · ⭐ **كود آلي 12=5+3+4 من FIMSHTBL + بوابة أحادية property-wise ثالثة:** [`01-master-data.md`](modules/fixed-assets/01-master-data.md) + [`02-configuration.md`](modules/fixed-assets/02-configuration.md) (INI#475 يقرر المنهج) · ⭐ **أزرق = غير مربوط + تعطيل P&L عند التساوي + Gain/Loss آلي بأمثلة الدليل الرقمية (£75,000/40% WDV):** [`05-business-rules.md`](modules/fixed-assets/05-business-rules.md) + [`13-exceptions.md`](modules/fixed-assets/13-exceptions.md) · **أنقى تطابق ERPNext في المشروع (Asset/Category Accounts/SLM+WDV أصلية — ~4 أصول/2-3 أسابيع):** [`16-erpnext-mapping.md`](modules/fixed-assets/16-erpnext-mapping.md) (F-FX-1..11 — توحيد MNT+FXD على Asset واحد!) · صلاحيات صفرية سابعة (الأخطر — وحدة ترحيلية): [`07-permissions.md`](modules/fixed-assets/07-permissions.md) · الفجوات: [`17-gap-analysis.md`](modules/fixed-assets/17-gap-analysis.md) (**Rollback بلا معكوس GL — UNK-071 قصوى** + UNK-068..073)

**16. Gate Passes (مكتملة — 19 ملفاً):** [`modules/gate-passes/`](modules/gate-passes/) — ابدأ بـ [`00-overview.md`](modules/gate-passes/00-overview.md) · ⭐ **أضأف دليل في المشروع (13 ص) بثلاث "أوائل مطلقة": لا ماسترات داخلية · لا User/Last Updated · صفر درجة اتصال (الجزيرة الورقية):** [`00-overview.md`](modules/gate-passes/00-overview.md) + [`12-integrations.md`](modules/gate-passes/12-integrations.md) (I-GP-01..06 — ختام عائلة UNK-058 بالامتداد السابع: Vendor Code/Name منفصلان!) · ⭐ **الاستلام الجزئي بأغنى وصف + الاسترجاث ثلاثي المفاتيح (GP#/Vendor/Ref#):** [`10-transactions.md`](modules/gate-passes/10-transactions.md) + [`04-workflows.md`](modules/gate-passes/04-workflows.md) (WF-GP-01..07 — دورة العودة والدورة المتجمدة) · ⭐ **ثنائية Returnable تنظّم كل شيء + السجل للمرتجع فقط + المعلق as-on:** [`05-business-rules.md`](modules/gate-passes/05-business-rules.md) (BR-GP-01..12) + [`08-reports.md`](modules/gate-passes/08-reports.md) · **"Asset Issue Gate Pass" بقايا تسمية تحقيقية (E-GP-01):** [`13-exceptions.md`](modules/gate-passes/13-exceptions.md) (دورة متجمدة + إعادة طباعة بلا إبطال!) · أرخص تحويل (~3 أصول/1-2 أسبوع): [`16-erpnext-mapping.md`](modules/gate-passes/16-erpnext-mapping.md) (F-GP-1..8) · الفجوات: [`17-gap-analysis.md`](modules/gate-passes/17-gap-analysis.md) (UNK-074..077)

---

## 🎯 اكتمال الـ17/17 وحدة (الجلسة 15 — 2026-09-04)

> **كل الوحدات موثقة الآن**: 1.FO · 2.FAS · 3.ACR · 4.POS (+TSC داخلها) · 5.SYS · 6.MGT · 7.BNQ · 8.HRP · 9.Care · 10.MEM · 11.SLM · 12.TEL · 13.MNT · 14.FNB · 15.FXD · 16.GTP = **306 ملفات وثائق** في `docs/modules/` + عائلات عابرة (UNK-001..077 · 16 جسر F-link · تناقض C-FB-01).
> **التالي (المرحلة 7+):** التقارير المؤجلة (FOM-REP 120 ص · MGT-REP 112 ص · FAS-REP 64 ص · POS-REP 158 ص...) ← ثم المراجعة الشاملة + cross-referencing + Knowledge Graph النهائي (Phase 8+).

---

## 🚀 المرحلة 7 — طبقة التقارير (Phase 7 Reports) — بدأت الجلسة 16

### Front Office Reports + SMS (مكتمل — 12 ملفاً — الجلسة 16)

**[`reports/front-office/`](reports/front-office/)** — المصادر: FOM-REP (120 ص — أضخم ملف تقارير: ~135 تقريراً + 28 فرعياً) + FOM-SMS (14 ص) — **FO أول وحدة كاملة المصادر 11/11**:

- **[نظرة عامة + إحصاء الكتالوج](reports/front-office/00-overview.md)** — العائلات الـ9 + الجسور + أبرز 10 اكتشافات
- ⭐ **[محرك التقارير والبنية التحتية](reports/front-office/01-report-engine-infrastructure.md)** — قناة الإخراج الرباعية الموحدة (Display/Spool/Print/Export) + Program IDs (FOMRR15) + **INI Switch 63** (أول مفتاح playlist) + **PMSPOL.INI→POL.SPC** (ثالث بنية ملفية مسربة) + بوابات الإعداد العابرة (SYS+FO Setup) + أنماط التفاعل الثمانية
- **[الحجوزات والوصول](reports/front-office/02-reservation-arrival-reports.md)** (§1-23) — Cut Off/No Show revenue/Turn Away + future-only الحرفية
- ⭐ **[الأمن والامتثال النظامي](reports/front-office/03-security-statutory-reports.md)** — خريطة الامتثال الهندية: الشرطة (Police/C-Form/Watch List بذاكرة unmarking) + **RBI (RLM)** + IT + Tax FO×POS + Scanty Baggage
- **[الإشغال والتدقيق](reports/front-office/04-occupancy-inhouse-audit.md)** (§24-50) — **مجموعة Audit ×8** (old/new + المستخدم المخوّل) + Reopen Folio + Dummy/Feature/CGR
- **[الأسعار والتوقعات والمغادرة](reports/front-office/05-rates-plans-forecast-departures.md)** (§51-71) — **Hurdle Rate موثقة** + "This mandatory report" + تبعية ترحيل التعرفة + رموز AP/BB/EP/MAP
- **[المالية ودفاتر القيود](reports/front-office/06-financial-ledger-reports.md)** (§72-106) — **صيغة Room Balance الحرفية** + معجم ADQ/ADC/ADV/POT + Cashier بالورديات + **XOR 80/132 المعكوس** + Budget بسعر صرف قابل للتحرير
- **[الدعم التشغيلي](reports/front-office/07-operations-support.md)** (§107-114) — Sequence Print + مطابقة FO↔HK + HK Consumption (12 معياراً) + Lost & Found 7 زوايا
- **[MIS والتحليل](reports/front-office/08-mis-analytics.md)** (§115-135) — الأبعاد الأربعة + Lakhs + **Materialized/Forecast** + ETL دفعي (Manager Report Creation بذاكرة)
- ⭐ **[مصفوفة قواعد التواريخ](reports/front-office/09-date-validation-matrix.md)** — **~25 قاعدة حرفية** (future/past/month-boundary×15/نوافذ 10-30-31) + مراجع الزمن الثلاثة (accounting/current/server)
- **[تنبيهات SMS](reports/front-office/10-sms-alerts.md)** — 8 خدمات بمحتوى الرسائل حرفياً + **Checkout قبل ساعة** + Department Checkout Alert + **"Fortune Next Enterprise 2.0"** (C-FO-02)
- **[التحويل والفجوات](reports/front-office/11-erpnext-mapping-gaps.md)** — F-FOR-1..14 (~8-10 أصول/5-7 أسابيع) + GAP-FOR-D01..D07/P01..P05 + UNK-078..082 + AC + Smoke 18 خطوة

### Point of Sale Reports (مكتمل — 12 ملفاً — الجلسة 17)

**[`reports/point-of-sale/`](reports/point-of-sale/)** — المصدر: POS-REP (158 ص / 3,898 سطر — أضخم ملف REP متبقٍّ: 59 بنداً/~57 فريداً) — **POS ثاني وحدة كاملة المصادر 4/4**:

- **[نظرة عامة + مفارقة الترتيب الفيزيائي](reports/point-of-sale/00-overview.md)** — 24 قسماً + 42 فرعياً + جسور الوحدات + أبرز 12 اكتشافاً + §6 واقعة فيزيائياً بعد §11
- ⭐ **[محرك التقارير والبنية التحتية](reports/point-of-sale/01-report-engine-infrastructure.md)** — **مصفوفة POS Report Options (أول Config-per-Report في المشروع)** + Invariant Void/Comp ×25 تكراراً + قنوات الإخراج + **Port ID** (خامسة خاصة بPOS) + بوابات الإعداد (DSR Session Group/INI 137/335)
- **[تقارير المبيعات](reports/point-of-sale/02-sales-reports.md)** (§1.1-1.16) — **DS Report 8×11 بAmount+%** + عمود التنبؤ العامي "Where are we headed with this average?" + علامات (V)/(C) + تعريف Credit الحرفي
- **[التسوية والتحصيل](reports/point-of-sale/03-settlement-collection-reports.md)** (§2-5) — **Cancelled bills تعرض أرقام البديلة** + **Closed Shifts only** + نطاق أرقام فواتير الوردية + معجم أنماط التسوية الكامل (Staff/others/City Ledger)
- **[الخصومات وNC والتوصيل](reports/point-of-sale/04-discount-nc-delivery-reports.md)** (§6/11/7/12) — **Discount Register المزدوج (C-POS-01)** + سلسلة الخصم الرباعية + مسؤول السماح + عتبة 7 منافذ→132 + Customer Id مولد آلياً
- ⭐ **[الضرائب والامتثال الهندي](reports/point-of-sale/05-tax-statutory-reports.md)** (§16+§9) — **Pivot أعمدة من نسب الضرائب** + تعريف **City Ledger** الحرفي + **PAN بSwitch 137** ("applicable only for Indian Government") + ثلاثية Non-Taxable/Exemption/Breakup
- **[تدقيق KOT والفواتير](reports/point-of-sale/06-audit-reports.md)** (§17) — **Bill Audit بزوج mode+amount قديم→جديد** (أكمل old/new) + KOT Audit بسبب الحذف + **KOT Books الورقية** + عبور الشهور للتدقيق فقط
- **[قوائم الماستر](reports/point-of-sale/07-menu-master-lists.md)** (§18-21) — Rate List بطاقة صنف كاملة (NC%!) + **Happy Hours المستقبلي الوحيد** + TS Modifier ماستر مستقل
- ⭐ **[التحليل وMenu Engineering](reports/point-of-sale/08-analytics-menu-engineering.md)** (§22/23) — **مصفوفة STAR/PUZZLE/PLOW HORSE/DOG بـ15 عموداً وصيغ حرفية** (نموذج Kasavana-Smith كاملاً — أعمق منهجية في المشروع) + INI 335 + Cover Analysis بسلوك **80/132 المعكوس عن FO**
- **[الولاء وإعادة الطباعة وKDS](reports/point-of-sale/09-loyalty-pan-reprint-kds.md)** (§8/10/24) — وضع Month&Year للمنسية + Help ديناميكي + **KDS §24 شبح ختامي** (UNK-083)
- ⭐ **[مصفوفة قواعد التواريخ](reports/point-of-sale/10-date-validation-matrix.md)** — ~20 قاعدة: **POS ماضوية شبه كاملة** (مستقبلي واحد!) + نوافذ 7/30 + عتبات منافذ 7/8 + مقارنة مع مصفوفة FO
- **[التحويل والفجوات](reports/point-of-sale/11-erpnext-mapping-gaps.md)** — F-PR-1..15 (~7-9 أصول/5-6 أسابيع) + GAP-PR-D01..D07/P01..P05 + UNK-083..088 + C-POS-01..03 + AC-PR-01..15 + Smoke 20 خطوة

**التالي (ختام المرحلة 7):** ~~MGT-REP (112 ص) → FAS-REP (64 ص)~~ — **✅ منجز بالجلسة 18 — 65/65 والحزمة مغلقة** → ثم المراجعة الشاملة (Phase 8+)

### Materials Management Reports (مكتمل — 12 ملفاً — الجلسة 18)

**[`reports/materials-management/`](reports/materials-management/)** — المصدر: MGT-REP (112 ص/1,745 سطر — 55 ورقة/~53 فريداً) — **MGT ثالث وحدة كاملة المصادر 4/4**:

- **[نظرة عامة + مفارقة الترقيم](reports/materials-management/00-overview.md)** — القسم 6 مرقّم مرتين (C-MR-01) + أبرز 12 اكتشافاً + جسور الوحدات
- ⭐ **[محرك التقارير](reports/materials-management/01-report-engine-infrastructure.md)** — **قانون Print Forms عبر FAS** (طباعة PO/SPO/GRN بـPgm.ID في FAS-SET §15 — برامج لكل عميل بثلاثية الورق!) + **صفر قنوات إلكترونية** (شذوذ عن FO/POS) + فعل Load
- **[قوائم الأصناف/الموردين/العقود](reports/materials-management/02-item-vendor-contract-master-reports.md)** — Vendor List بخمسة مناظر×ثلاث تفاصيل + **Black List** + Item Expiry بإنذار N-أيام
- **[تقارير دورة المشتريات](reports/materials-management/03-procurement-reports.md)** — حالة DPR/PO (عدم تناظر Cancelled!) + **Supplier Bill بـverify** (نواة Three-Way Match) + Comparative للعطاءات
- ⭐ **[عائلة طباعة المستندات](reports/materials-management/04-document-print-family.md)** — 7 مستندات + **GRN نسخة → Finance للدفع** + Indent بتنسيقين وAuthorization choice
- **[المعاملات والاستلام §4](reports/materials-management/05-transaction-receipt-reports.md)** — أكبر عائلة (8) بـ**Adaptive UI** + Store Break + ثلاثية Complimentary + **Capital Goods Receipt** (جسر FXD)
- **[أرصدة المخزون](reports/materials-management/06-stock-balance-reports.md)** — **رصيد ثلاثي الحيازة** (مخزن/فرعي/CC) + Re-Order **بـCurrent Date فقط** + Load
- **[الاستهلاك والموازنات](reports/materials-management/07-consumption-budget-reports.md)** — ثلاثية Consolidated/CC/Department + **R2 أول لاحقة إصدار** (UNK-089) + Budget بثنائية Purchase/Consumption
- ⭐ **[تحليلات المخزون](reports/materials-management/08-inventory-analytics.md)** — **ABC (Pareto) بعتبتي A/B من المستخدم** + FSN بمعامل داخل الشاشة (double-click Days) + **Efficiency/Yield FROM/TO** — ثلاثية المنهجيات الكلاسيكية
- **[الجرد المادي والتدقيق والضرائب](reports/materials-management/09-physical-stock-audit-tax-reports.md)** — **Variance ببوابة بيانات** (تواريخ الجرد فقط!) + **Audit Trial بالمحذوفات** + VAT بـassessment year وPJV-Wise
- ⭐ **[مصفوفة قواعد التواريخ](reports/materials-management/10-date-validation-matrix.md)** — **ثلاث بوابات جديدة**: current-only ×2 · **data-gated** · Date XOR Month كـ9 تقارير
- **[التحويل والفجوات](reports/materials-management/11-erpnext-mapping-gaps.md)** — F-MR-1..16 (~4-6 أصول/3-4 أسابيع — **أنسب وحدات المرحلة للتحويل**: ABC/FSN/Stock Ledger/Reconciliation native) + GAP + UNK-089..095 + C-MR-01..03 + AC ×15 + Smoke 20

### Financial Management Reports (مكتمل — 12 ملفاً — الجلسة 18 — **خاتمة الحزمة 65/65**)

**[`reports/financial-accounting/`](reports/financial-accounting/)** — المصدر: FAS-REP (64 ص/858 سطر — 46 تقريراً + **شبحان ختاميان**) — **FAS رابع وحدة كاملة المصادر 5/5 — آخر ملف في الحزمة**:

- **[نظرة عامة](reports/financial-accounting/00-overview.md)** — 48 بنداً + القوانين الخمسة الكبرى + **شبحا الختام (IDS Crystal متكرر مع FO! + iDesigner)**
- ⭐ **[محرك التقارير](reports/financial-accounting/01-report-engine-infrastructure.md)** — **5 قنوات إخراج** (Print/Email/Spool بملف/Excel/132) + **مسار Email بـOutlook+Broadgun PDF** + Print Forms بنمطي تسجيل + Tag/Load ×4
- **[دليل الحسابات واليوميات](reports/financial-accounting/02-chart-ledger-daybooks.md)** — اليوميات ×3 + **مثال A008000/SBI Frankfurt/USD الحرفي** (Contra) + كشف المحذوفات من TC
- **[الأرصدة والدفاتر](reports/financial-accounting/03-ledger-balance-gl.md)** — GL بأربعة مناظير + Detail Register **بمؤشر تكيّفي** وعتبة مبلغ
- **[القوائم المالية](reports/financial-accounting/04-financial-statements.md)** — **PL بأربع فترات (Month/YTD/PrevYear/Total)** + **TB ×4 بـXOR 0×132 أول اقتران إجباري** + past-only ×4 + شجرة CoA (Sub group/Sub Head)
- **[سجلات الدائنين والمشتريات](reports/financial-accounting/05-creditors-purchase-registers.md)** — Ageing الدائنين + Expense بعتبة Above + **قصة Contract Debit كاملة بـwaive amount**
- ⭐⭐ **[طبقة النزاهة التكاملية](reports/financial-accounting/06-integration-link-reports.md)** — **أهم 4 تقارير في المرحلة 7**: Unlinked/Linked Account Codes + Auto Posted — **أسماء معاملات الربط الأربعة المسربة + أنواع الترحيل FOM/ACR/INV (بلا HRP! — UNK-098 يلامس UNK-010 الأصل)** + PJV (Regular/Service)
- **[المصرفية والشيكات](reports/financial-accounting/07-banking-cheques-pdc.md)** — Bank Rec (Realized/Unrealized برصيد كشف يدوي) + Advice/Cheque بـ**Normal/Repeat وTagAll** + PDC Rec/Pay + طابعة افتراضية محطية
- ⭐ **[جناح TDS الهندي](reports/financial-accounting/08-tds-statutory-forms.md)** — **16A بأرباع ×4 + New/Reprint + Height 11/12 IN + 26J=ملحق 16A للعوائد + Challan** — أضخم كتلة امتثال في الحزمة
- **[التدقيق والتقارير المخصصة](reports/financial-accounting/09-audit-user-reports.md)** — Audit بـ**Txn Date XOR Updated Date** + User Reports بمصفوفة قيم ست (**(-ve) بين قوسين · Lakh/Million**) + Excel + Invoice/Payment يُكمل **Three-Way Match**
- ⭐ **[مصفوفة قواعد التواريخ](reports/financial-accounting/10-date-validation-matrix.md)** — **past-only ×4 حرفية** + قيود FY/Month-bound + مفاتيح استرجاع غير تاريخية (Challan/Certificate/أرباع)
- **[التحويل والفجوات](reports/financial-accounting/11-erpnext-mapping-gaps.md)** — F-FA-1..16 (~5-7 أصول/3-4 أسابيع — قوائم/دفاتر/TB/AP-ageing/Bank-Rec/TDS **native**) + قرار معماري D12 (من «احفظ ثم نبّه» إلى «اربط ثم احفظ») + UNK-096..102 + C-FA-01..03 + AC ×15 + Smoke 20

---

## 🎯 خاتمة المشروع القرائي — 65/65 (الجلسة 18 — 2026-09-04)

> **كل ملفات الحزمة الـ65 مقروءة عميقاً**: 17/17 وحدة (306 ملف وثائق في `modules/`) + 4 وحدات REP كاملة (48 ملفاً في `reports/` — FO ~135 · POS ~57 · MGT ~53 · FAS 46 = ~291 تقريراً) = **354 ملفاً** · **102 مجهول** (UNK-001..102) · **12 تناقضاً** (C-FB-01 · C-FO-01/02 · C-POS-01..03 · C-MR-01..03 · C-FA-01..03).
> **أكبر خلاصات المرحلة 7:** هوية سوق هندية مكتملة (PAN/TDS ×7/C-Form/RLM/assessment/Lakhs) · طبقة النزاهة التكاملية (FAS) كجواب نظامي لسؤال الجسور · Print Forms = كود لكل عميل (تفسير غياب المطبوعات) · عائلات عابرة مؤكدة (80/132 باتجاهين · Format-2/R2 · Tag-YES · أشباح IDS ×2 · محذوفات ×4) · **~291 تقريراً بلا صلاحية واحدة**.
> **التالي (المرحلة 9): بدء التنفيذ على ERPNext** — بوابة الدخول: `analysis/01-synthesis/04-unknowns-closure-map.md` §6 (تفعيل P0-1..P0-10 ثم الوحدات بترتيب أنقى التواءم: FXD → GTP → FNB/Recipe → MNT).

---

## 🧩 المرحلة 8 — التجميع النهائي (الجلسة 19 — 2026-09-04)

> **المعرفة المركزية الموحدة جاهزة**: `analysis/01-synthesis/` (5 ملفات) — Knowledge Graph النهائي (20 عائلة عابرة + 8 قوانين L1-L8 + مصفوفة INI 27 مفتاحاً) + مصفوفة ~128 قراراً مجمّعاً (العشرة P0) + جدول المرادفات (حل C-FA-01) + خريطة إغلاق 102 مجهول (لا واحد بلا مسار إغلاق).
> **أبرز خامات التجميع:** قانون الربط-قبل-الحفظ (L1/D12 يقلب save-then-warn) · قانون الطباعة-لكل-عميل (L2 يفسر غياب كل المطبوعات) · القالب المشترك (L8 — شبه إثبات قوالب TOC منسوخة عبر الوحدات من أشباح IDS ×2) · العائلات الأطول: المورد بلا موطن (UNK-058 ×7 امتدادات) والمخازن الموظفية (UNK-038 ×6) والصلاحيات الصفرية (12/17) · الجسر السلوكي العكسي الوحيد (FNB يقود POS بمفتاح 511) · GRN الورقي إلى Finance (جسر مادي موثق نصاً).

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
