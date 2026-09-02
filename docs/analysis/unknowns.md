# سجل المجهولات (Unknowns Register)

> كل معلومة لم نستطع إثباتها من الوثائق تُسجل هنا. لا تُترك مجهولات حرجة قبل مرحلة التنفيذ.
> الحالات: `Unknown` / `Partially Resolved` / `Resolved` / `Converted to Decision`

---

## تحديثات الجلسة 4 — POS (مختصرة)

- **UNK-001 Partially Resolved** (قاعدتا ضيوف منفصلتان موثقتان في POS-GST + تشارك انتقائي مع FO — قرار F-POS-2).
- **UNK-007 Partially Resolved** (POS currencies + Round Off لكل عملة + أسعار أجنبية للقوائم؛ تعريف Exchange Entry يبقى).
- **UNK-012 Resolved** (Split 3 طرق + 6 أنماط تسوية + Balance=0 + Resettlement).
- جديد: **UNK-021** (Void KOTs under Billing — مسار غير مقروء) من POS-SET §37.

## تحديثات الجلسة 4 (مختصرة)

- **UNK-013 Partially Resolved** — AR User Access موثق كاملاً (مستخدم × 4 أنواع قيود، افتراضي No) + FAS Transaction Type Rights سابقاً؛ يبقى SYS-SSP للفحص.
- جديد: **UNK-018** (سلوك Black List التشغيلي) و **UNK-019** (تفاعل SOA-AR مع Audited-FAS) من قراءة ACR.

## تحديثات الجلسة 3 (مختصرة)

- **UNK-005 Resolved · UNK-006 Resolved · UNK-014 Resolved · UNK-015 Resolved · UNK-002 Partially Resolved** (تفاصيل في الجدول).
- جديد: **UNK-016** (آلية re-process العكسية) من قراءة FAS.

## المجهولات المكتشفة في Phase 0

| ID | السؤال | لماذا يهم | المصادر المفحوصة | الحالة | الأثر | المسار |
|---|---|---|---|---|---|---|
| UNK-001 | هل Guest Master في FOM وPOS قاعدة بيانات واحدة أم نسختان متزامنتان؟ | يحدد تصميم Guest entity المركزي في النظام المستهدف | **FOM-GST (قرئ) + POS-GST (قرئ كاملاً)** | **Partially Resolved** | عالٍ | **قاعدتان منفصلتان موثقتان:** POS Guest Master يُفتح باختيار **Outlet أولاً** + كود ضيف آلي خاص (POS-GST §1 ص3-4)؛ خصائصه **تُعرض** فيها تفضيلات FO (ص18) وCard Types من FO (ص10)؛ وGuest Settlement يقرأ ضيوف FO بالغرفة لحظياً (TS ص36). **[INFERENCE]** بنية أصلية = Masterان + تشارك انتقائي؛ الهدف: **كيان واحد** (Customer موحد) بقرار F-POS-2 |
| UNK-002 | ما آلية "Rev. Management Tool" في FOM-LUK؟ هل هي Revenue Management حقيقية (تسعير ديناميكي) أم تقرير فقط؟ | يحدد إن كانت وحدة RM ضمن نطاق المشروع | **FOM-LUK §1 قرئ كاملاً** | **Partially Resolved** | متوسط | عرض شبكي (Events/Demand Codes بألوان Legend) + Criteria + Group By + ملخص + رسوم بيانية — أداة **قرار تسعيري** أقرب لـ RM؛ وHurdle Rate موثق في REG §14/§22 (سقف/أرضية سعرية) → **[INFERENCE] وحدة RM مبسطة مدمجة في FO** |
| UNK-003 | هل يوجد تكامل GDS/OTA/Channel Manager موثق؟ | نطاق التكاملات الخارجية | الفهارس — لا أثر واضح | Unknown | عالٍ | فحص FOM-RES وSLM نصاً |
| UNK-004 | كيف تُدار متعددية الفنادق/الخصائص (multi-property)؟ | قرار معماري جوهري (Frappe Sites مقابل Company/Property DocTypes) | SYS-SSP فهرس (يذكر DBs) | Unknown | عالٍ | قراءة SYS-SSP |
| UNK-005 | ما بنية دليل الحسابات (Main Heads/Sub Heads — كم مستوى، هل هو شجري حر أم قوالب)؟ | أساس Mapping مع ERPNext COA | **FAS-SET §1-2 + FAS-MST §1 قُرئت كاملة** | **Resolved** | — | ثلاث طبقات: Main Head (3 رقمي + Category نظامي) → Sub Head (3) → Account Head (5/8 حرفي + GL Type + Account Type + PDC Type + CC/Dept للدخل/المصروف) + SubLedger (7) متعدد الحسابات → راجع `docs/modules/financial-accounting/01-master-data.md` |
| UNK-006 | ما تفاصيل Night Audit خطوة بخطوة (أي الحسابات تُقفل، أي القيود تُنشأ)؟ | جوهر الترحيل اليومي في الفنادق | **FOM-DEP كامل + FAS-SET §6 + FAS-TRN §G** | **Resolved** | — | FO: Post Tariff → Guest Balance → Night Balance (Excess/Short=0) → Open New Date؛ ثم **Post FO to Finance**: Sales Journal مجمعة بحسابات روابط Revenue Types (D/C + SL)؛ الفرق → حساب No Transaction (Suspense) مؤقتاً → إصلاح + إعادة ترحيل → راجع `financial-accounting/11-accounting-impact.md` |
| UNK-007 | العملات المتعددة: أين تُعرَّف أسعار الصرف وكيف تُرحَّل الفروقات؟ | متطلب Middle-East محتمل (SAR/YER/USD) | **POS-SET §6 + §24 (قرئا) + ACR (سعر الصرف للفاتورة يثبت)** | **Partially Resolved** | عالٍ | POS: Link Outlet Currencies (بشرط Multi Currency=Yes) + Round Off لكل عملة + Menu Master بأسعار Local/Foreign (POS-SET §6/§24)؛ ACR: سعر تاريخ الفاتورة يثبت عند السداد (ACR-OPR §1 ص6)؛ تعريف أسعار الصرف نفسه = **Exchange Entry** (FAS — يقرأ في FAS-REP/Phase 6) |
| UNK-008 | ما حدود الضرائب (Tax Structures) وأنواعها (VAT/Municipality/Service Charge)? | الفنادق في المنطقة عليها ضرائب متعددة مركبة | **FOM-SET §6 + FAS-SET §6 (نوع Taxes)** | **Partially Resolved** | — | البنية موثقة كاملة: Calculation (Percentage/Amount/Slab) + On Tax/Consolidate/Pax + Rate Selection (Rack/Charged/High/Low) + فصل إلزامي (Tariff/ExtraBed/Plan)؛ الأنواع المذكورة نصاً: Service Charges, Luxury Tax, Sales Tax (FAS-SET) — أسماء ضرائب المنطقة العربية `[NOT DOCUMENTED]` (تخصيص زبون) |
| UNK-009 | هل الحجوزات تدعم Group Blocks/Allocation حقيقية (PMS allotments)؟ | يحسم تصميم Reservation model | فهرس FOM-SET (Group Business Sources) — غير حاسم | Unknown | عالٍ | قراءة FOM-RES |
| UNK-010 | ما علاقة Care بـ HRP في بيانات الموظفين (Personnel Master واحد أم مستقل)؟ | يمنع ازدواجية Employee entity | فهارس Care-SET (Adding Employee) وHRP-SET | Unknown | متوسط | قراءة الاثنين |
| UNK-011 | آلية "Auto Indent" من BNQ/FNB إلى MGT — هل تولد Purchase Requisition تلقائياً من متطلبات الوليمة؟ | تكامل تشغيلي جوهري | فهارس BNQ-BIL وFNB-COP | Unknown | عالٍ | قراءة العمليات |
| UNK-012 | هل يدعم POS الدفع المقسّم (split payments) وMixed payment على طاولة واحدة؟ | سلوك كاشير POS | **TS Manual ص28-36 (قرئ)** | **Resolved** | — | **نعم بوضوح:** Split Checks **3 طرق** (Equal/Covers · Item-wise · **Quantity-wise كسري 0.5**) + Link Tables (دمج طاولات بفاتورة واحدة) + Table Suffix؛ والتسويات 6 أنماط (Cash/CC/Cheque/Coupon/Guest/Void) **متسلسلة على الفاتورة** بقاعدة **Balance=0 إلزامية** قبل الحفظ (= mixed payments) + **Resettlement** بوضع آخر — راجع `point-of-sale/04-workflows.md` WF-POS-09/10 |
| UNK-013 | أين تُخزَّن الصلاحيات: لكل شاشة؟ لكل عملية؟ لكل Transaction Type؟ | تصميم permission model | فهارس SYS-SSP + FAS-SET (Transaction Type Rights) + **ACR-SET §4 (AR User Access — قرئ كاملاً)** | **Partially Resolved** | عالٍ | نموذجان موثقان الآن: **AR** = مستخدم × أنواع القيود الأربعة (Debit/Credit/Adjustment/Post — افتراضي No)؛ **FAS** = Transaction Type Rights؛ يبقى فحص SYS-SSP (المظلة) + صلاحيات العمليات الخطرة غير الموثقة (Rollback SOA / Cancel Invoice — GAP-AR-D04) |
| UNK-014 | هل توجد عمليات نهاية الشهر/السنة (Month/Year End Closing) موثقة في FAS؟ | دورة مالية كاملة | **FAS-SET §18 + FAS-TRN §8** | **Resolved** | — | شهرياً: Audited (يقفل شهر القيد)؛ سنوياً: **Open Financial Year** (أرصدة إقفال→افتتاحية + صافي P&L→Retained Earnings بنسب) + **Rollback Fin. Year** للعكس |
| UNK-015 | هل يدعم النظام Packages حقيقية (حزمة إقامة+وجبات+خدمات بسعر واحد)? | نموذج Package/Meal Plan | **FOM-SET §3/§7 قرئتا كاملاً** | **Resolved** | — | نعم: Package Amount يُفكّك إلزامياً عبر أعمدة Tariff/Plan/Services؛ Package Elements (مجموع 100%) يربط الإيراد بالضرائب؛ Occupancy S/D/T/Q + Extra Bed Pax + Days/Nights |

## المجهولات المكتشفة في الجلسة 3

| ID | السؤال | لماذا يهم | المصادر المفحوصة | الحالة | الأثر | المسار |
|---|---|---|---|---|---|---|
| UNK-016 | ما آلية "re-process" العكسية في Post FO to Finance — هل يُعكس القيد السابق آلياً أم يُنشأ قيد جديد معاكس؟ | تحديد سلوك الترحيل اليومي عند إصلاح الروابط | FAS-SET §6 + FAS-TRN §G | Unknown | متوسط | [INFERENCE] الأرجح معالجة قيد جديدة/إعادة توليد؛ يُحسم عند تنفيذ القرار المعماري GE-FA-01/القرار 1 في `financial-accounting/17-gap-analysis.md` |
| UNK-017 | تفاصيل Audit Code المرافق للبنود في شاشة Post FO | ربط ترحيل GL بمصدر التدقيق | FAS-TRN §G (مذكور بلا بنية) | Unknown | منخفض | FAS-REP أو AR |

## المجهولات المكتشفة في الجلسة 4 (من ACR)

| ID | السؤال | لماذا يهم | المصادر المفحوصة | الحالة | الأثر | المسار |
|---|---|---|---|---|---|---|
| UNK-018 | ما السلوك التشغيلي لـ Black List؟ هل يمنع التسوية الائتمانية تلقائياً أم وصم عرضي فقط؟ | سلوك تحكم ائتماني حاسم | ACR-SET §5 ص12 (الوصم فقط موثق) | Unknown | متوسط | `[INFERENCE]` الأرجح المنع؛ يُحسم عند التنفيذ (GAP-AR-D03) |
| UNK-019 | ما ترتيب/تفاعل الإقفال: SOA (AR) مقابل Audited (FAS) لنفس الشهر؟ | دورة إقفال مالية موحدة | ACR-OPR §7 + FAS-SET §18 | Unknown | عالٍ | قرار معماري (E-AR-17) — يُطرح في Phase 6/13 |
| UNK-020 | هل قيود Opening Balance تُرحَّل إلى GL؟ (لا ذكر لشاشة FA في ACR-SET §2) | سلامة أرصدة التأسيس | ACR-SET §2 | Unknown | متوسط | فحص سلوكي عند التنفيذ (QA-AR-3) |
| UNK-021 | ما وظيفة/بنية Void KOTs تحت Billing (يُذكر شرطاً لـ Purge KOT Books)؟ | دورة KOT الكاملة | POS-SET §37 ص109 (اسم فقط) | Unknown | منخفض | قراءة POS-REP (المرحلة 7) أو قسم Billing غير المقروء |
| UNK-022 | أرقام Module Attributes/INI الكاملة لوحدة POS (الموثق: 6/29/32 + INI 404) — المرجع "Module Attributes & INI Settings documents" خارج حزمة 65؟ | مفاتيح سلوكية | POS-SET §15 ص45 + §24 + §41 | Unknown | عالٍ | قراءة SYS-SSP (110 ص) — تحسم مع UNK-004/013 |
