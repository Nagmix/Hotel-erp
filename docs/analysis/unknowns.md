# سجل المجهولات (Unknowns Register)

> كل معلومة لم نستطع إثباتها من الوثائق تُسجل هنا. لا تُترك مجهولات حرجة قبل مرحلة التنفيذ.
> الحالات: `Unknown` / `Partially Resolved` / `Resolved` / `Converted to Decision`

---

## تحديثات الجلسة 3 (مختصرة)

- **UNK-005 Resolved · UNK-006 Resolved · UNK-014 Resolved · UNK-015 Resolved · UNK-002 Partially Resolved** (تفاصيل في الجدول).
- جديد: **UNK-016** (آلية re-process العكسية) من قراءة FAS.

## المجهولات المكتشفة في Phase 0

| ID | السؤال | لماذا يهم | المصادر المفحوصة | الحالة | الأثر | المسار |
|---|---|---|---|---|---|---|
| UNK-001 | هل Guest Master في FOM وPOS قاعدة بيانات واحدة أم نسختان متزامنتان؟ | يحدد تصميم Guest entity المركزي في النظام المستهدف | فهارس FOM-GST وPOS-GST (نفس العناوين تقريباً) | Unknown | عالٍ | قراءة عميقة للملفين في Phase 2/3 |
| UNK-002 | ما آلية "Rev. Management Tool" في FOM-LUK؟ هل هي Revenue Management حقيقية (تسعير ديناميكي) أم تقرير فقط؟ | يحدد إن كانت وحدة RM ضمن نطاق المشروع | **FOM-LUK §1 قرئ كاملاً** | **Partially Resolved** | متوسط | عرض شبكي (Events/Demand Codes بألوان Legend) + Criteria + Group By + ملخص + رسوم بيانية — أداة **قرار تسعيري** أقرب لـ RM؛ وHurdle Rate موثق في REG §14/§22 (سقف/أرضية سعرية) → **[INFERENCE] وحدة RM مبسطة مدمجة في FO** |
| UNK-003 | هل يوجد تكامل GDS/OTA/Channel Manager موثق؟ | نطاق التكاملات الخارجية | الفهارس — لا أثر واضح | Unknown | عالٍ | فحص FOM-RES وSLM نصاً |
| UNK-004 | كيف تُدار متعددية الفنادق/الخصائص (multi-property)؟ | قرار معماري جوهري (Frappe Sites مقابل Company/Property DocTypes) | SYS-SSP فهرس (يذكر DBs) | Unknown | عالٍ | قراءة SYS-SSP |
| UNK-005 | ما بنية دليل الحسابات (Main Heads/Sub Heads — كم مستوى، هل هو شجري حر أم قوالب)؟ | أساس Mapping مع ERPNext COA | **FAS-SET §1-2 + FAS-MST §1 قُرئت كاملة** | **Resolved** | — | ثلاث طبقات: Main Head (3 رقمي + Category نظامي) → Sub Head (3) → Account Head (5/8 حرفي + GL Type + Account Type + PDC Type + CC/Dept للدخل/المصروف) + SubLedger (7) متعدد الحسابات → راجع `docs/modules/financial-accounting/01-master-data.md` |
| UNK-006 | ما تفاصيل Night Audit خطوة بخطوة (أي الحسابات تُقفل، أي القيود تُنشأ)؟ | جوهر الترحيل اليومي في الفنادق | **FOM-DEP كامل + FAS-SET §6 + FAS-TRN §G** | **Resolved** | — | FO: Post Tariff → Guest Balance → Night Balance (Excess/Short=0) → Open New Date؛ ثم **Post FO to Finance**: Sales Journal مجمعة بحسابات روابط Revenue Types (D/C + SL)؛ الفرق → حساب No Transaction (Suspense) مؤقتاً → إصلاح + إعادة ترحيل → راجع `financial-accounting/11-accounting-impact.md` |
| UNK-007 | العملات المتعددة: أين تُعرَّف أسعار الصرف وكيف تُرحَّل الفروقات؟ | متطلب Middle-East محتمل (SAR/YER/USD) | فهارس POS-SET (Link Outlet Currencies) | Unknown | عالٍ | قراءة FAS-SET + POS-SET |
| UNK-008 | ما حدود الضرائب (Tax Structures) وأنواعها (VAT/Municipality/Service Charge)? | الفنادق في المنطقة عليها ضرائب متعددة مركبة | **FOM-SET §6 + FAS-SET §6 (نوع Taxes)** | **Partially Resolved** | — | البنية موثقة كاملة: Calculation (Percentage/Amount/Slab) + On Tax/Consolidate/Pax + Rate Selection (Rack/Charged/High/Low) + فصل إلزامي (Tariff/ExtraBed/Plan)؛ الأنواع المذكورة نصاً: Service Charges, Luxury Tax, Sales Tax (FAS-SET) — أسماء ضرائب المنطقة العربية `[NOT DOCUMENTED]` (تخصيص زبون) |
| UNK-009 | هل الحجوزات تدعم Group Blocks/Allocation حقيقية (PMS allotments)؟ | يحسم تصميم Reservation model | فهرس FOM-SET (Group Business Sources) — غير حاسم | Unknown | عالٍ | قراءة FOM-RES |
| UNK-010 | ما علاقة Care بـ HRP في بيانات الموظفين (Personnel Master واحد أم مستقل)؟ | يمنع ازدواجية Employee entity | فهارس Care-SET (Adding Employee) وHRP-SET | Unknown | متوسط | قراءة الاثنين |
| UNK-011 | آلية "Auto Indent" من BNQ/FNB إلى MGT — هل تولد Purchase Requisition تلقائياً من متطلبات الوليمة؟ | تكامل تشغيلي جوهري | فهارس BNQ-BIL وFNB-COP | Unknown | عالٍ | قراءة العمليات |
| UNK-012 | هل يدعم POS الدفع المقسّم (split payments) وMixed payment على طاولة واحدة؟ | سلوك كاشير POS | فهرس POS-LUK (Settlement Summary) — غير حاسم | Unknown | متوسط | قراءة POS-SET/GST |
| UNK-013 | أين تُخزَّن الصلاحيات: لكل شاشة؟ لكل عملية؟ لكل Transaction Type؟ | تصميم permission model | فهارس SYS-SSP + FAS-SET (Transaction Type Rights) + ACR-SET (AR User Access) | Unknown | عالٍ | قراءة SYS-SSP كاملاً |
| UNK-014 | هل توجد عمليات نهاية الشهر/السنة (Month/Year End Closing) موثقة في FAS؟ | دورة مالية كاملة | **FAS-SET §18 + FAS-TRN §8** | **Resolved** | — | شهرياً: Audited (يقفل شهر القيد)؛ سنوياً: **Open Financial Year** (أرصدة إقفال→افتتاحية + صافي P&L→Retained Earnings بنسب) + **Rollback Fin. Year** للعكس |
| UNK-015 | هل يدعم النظام Packages حقيقية (حزمة إقامة+وجبات+خدمات بسعر واحد)? | نموذج Package/Meal Plan | **FOM-SET §3/§7 قرئتا كاملاً** | **Resolved** | — | نعم: Package Amount يُفكّك إلزامياً عبر أعمدة Tariff/Plan/Services؛ Package Elements (مجموع 100%) يربط الإيراد بالضرائب؛ Occupancy S/D/T/Q + Extra Bed Pax + Days/Nights |

## المجهولات المكتشفة في الجلسة 3

| ID | السؤال | لماذا يهم | المصادر المفحوصة | الحالة | الأثر | المسار |
|---|---|---|---|---|---|---|
| UNK-016 | ما آلية "re-process" العكسية في Post FO to Finance — هل يُعكس القيد السابق آلياً أم يُنشأ قيد جديد معاكس؟ | تحديد سلوك الترحيل اليومي عند إصلاح الروابط | FAS-SET §6 + FAS-TRN §G | Unknown | متوسط | [INFERENCE] الأرجح معالجة قيد جديدة/إعادة توليد؛ يُحسم عند تنفيذ القرار المعماري GE-FA-01/القرار 1 في `financial-accounting/17-gap-analysis.md` |
| UNK-017 | تفاصيل Audit Code المرافق للبنود في شاشة Post FO | ربط ترحيل GL بمصدر التدقيق | FAS-TRN §G (مذكور بلا بنية) | Unknown | منخفض | FAS-REP أو AR |
