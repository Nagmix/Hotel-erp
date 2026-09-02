# سجل المجهولات (Unknowns Register)

> كل معلومة لم نستطع إثباتها من الوثائق تُسجل هنا. لا تُترك مجهولات حرجة قبل مرحلة التنفيذ.
> الحالات: `Unknown` / `Partially Resolved` / `Resolved` / `Converted to Decision`

---

## تحديثات الجلسة 6 — Materials Management (MGT-SET/DNT/LUK قُرئت كاملة)

- **UNK-011 Partially Resolved** (Auto-Indent: قناة **DPR** موثقة داخل MGT — "If the item has 'Nil' balance... DPR Qty... will be reflected during the Receipt entry" + Re-Order Process الآلي؛ **يبقى اتجاه BNQ/FNB→MGT غير موثق** — يفحص عند قراءة BNQ/FNB).
- **UNK-024 Partially Resolved** (دليل Gift Shop يقوى: MGT يوثق **Shop Outlet** كنوع مخزن مربوط بمنفذ بيع "Outlet Code and Store code should be same" + Barcode INI 245 — يرجّح أن Gift Shop = مخزن+منفذ POS لا وحدة مستقلة؛ يبقى [UNCERTAIN] حتى POS-REP/BNQ).
- جديد من قراءة MGT: **UNK-027** (توقيت ترحيل MM→FAS: فوري/دفعة/شهري) + **UNK-028** (مالك كيان Company Types: FO أم SYS؟) + **UNK-029** (ارتباط Gate Entry# في Receipt بوحدة Gate Passes) + **UNK-030** (هل ترتبط مبيعات Shop Outlet بمخزون MGT مباشرة؟) + **UNK-031** (دلالة حالة "Blank Space" في PO by Vendor).
- الجدول التراكمي لمفاتيح الإعداد يوسَّع إلى **25+ مفتاحاً** (إضافة INI 39/131/245/355 + INV 3/5(=8?)/6/7/13/14/298 — مع GAP-MG-D01 تعارض ترقيم SPO).

## تحديثات الجلسة 5 — System Setup (SYS-SSP قُرئ كاملاً)

- **UNK-004 Resolved** (multi-property: نموذج بيانات متعدد الخصائص + Property=Company قرار F-SYS-11).
- **UNK-013 Resolved** (نموذج الصلاحيات الرباعي الطبقات موثق كاملاً من SYS-SSP Ch1 + دمجه مع صلاحيات الوحدات).
- **UNK-022 Resolved** (مرجع «Module Attributes & INI Settings» مؤكد وجوده **خارج الحزمة** — إحالتان صريحتان ص33/ص37 — GAP-SYS-D01؛ الاستراتيجية: جمع الإحالات المرقمة من كل وحدة).
- جديد: **UNK-023** (سلوك انتهاء كلمة المرور) + **UNK-024** (وحدة Gift Shop المذكورة في Reason Codes بلا أدلة مستقلة) + **UNK-025** (وظيفة Group Nationality §19 الهامشية) من قراءة SYS.

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
| UNK-004 | كيف تُدار متعددية الفنادق/الخصائص (multi-property)؟ | قرار معماري جوهري (Frappe Sites مقابل Company/Property DocTypes) | **SYS-SSP قُرئ كاملاً (خصوصاً §Ch3/1 + Introduction)** | **Resolved** | — | النموذج الأصلي: **Property Codes سجل متعدد** ("A property can be a Hotel, a Resort... Food Court, Hotel Management School" ص41) لكن **تشغيلاً أحادياً**: FO Defaults يختار قيمة افتراضية واحدة، ولا آلية موثقة لتبديل خاصية التشغيل أو مشاركة البيانات. **القرار F-SYS-11:** Property = Company في Frappe (شركات متعددة بموقع واحد) + User Permissions للعزل — راجع `modules/system-setup/16-erpnext-mapping.md` |
| UNK-005 | ما بنية دليل الحسابات (Main Heads/Sub Heads — كم مستوى، هل هو شجري حر أم قوالب)؟ | أساس Mapping مع ERPNext COA | **FAS-SET §1-2 + FAS-MST §1 قُرئت كاملة** | **Resolved** | — | ثلاث طبقات: Main Head (3 رقمي + Category نظامي) → Sub Head (3) → Account Head (5/8 حرفي + GL Type + Account Type + PDC Type + CC/Dept للدخل/المصروف) + SubLedger (7) متعدد الحسابات → راجع `docs/modules/financial-accounting/01-master-data.md` |
| UNK-006 | ما تفاصيل Night Audit خطوة بخطوة (أي الحسابات تُقفل، أي القيود تُنشأ)؟ | جوهر الترحيل اليومي في الفنادق | **FOM-DEP كامل + FAS-SET §6 + FAS-TRN §G** | **Resolved** | — | FO: Post Tariff → Guest Balance → Night Balance (Excess/Short=0) → Open New Date؛ ثم **Post FO to Finance**: Sales Journal مجمعة بحسابات روابط Revenue Types (D/C + SL)؛ الفرق → حساب No Transaction (Suspense) مؤقتاً → إصلاح + إعادة ترحيل → راجع `financial-accounting/11-accounting-impact.md` |
| UNK-007 | العملات المتعددة: أين تُعرَّف أسعار الصرف وكيف تُرحَّل الفروقات؟ | متطلب Middle-East محتمل (SAR/YER/USD) | **POS-SET §6 + §24 (قرئا) + ACR (سعر الصرف للفاتورة يثبت)** | **Partially Resolved** | عالٍ | POS: Link Outlet Currencies (بشرط Multi Currency=Yes) + Round Off لكل عملة + Menu Master بأسعار Local/Foreign (POS-SET §6/§24)؛ ACR: سعر تاريخ الفاتورة يثبت عند السداد (ACR-OPR §1 ص6)؛ تعريف أسعار الصرف نفسه = **Exchange Entry** (FAS — يقرأ في FAS-REP/Phase 6) |
| UNK-008 | ما حدود الضرائب (Tax Structures) وأنواعها (VAT/Municipality/Service Charge)? | الفنادق في المنطقة عليها ضرائب متعددة مركبة | **FOM-SET §6 + FAS-SET §6 (نوع Taxes)** | **Partially Resolved** | — | البنية موثقة كاملة: Calculation (Percentage/Amount/Slab) + On Tax/Consolidate/Pax + Rate Selection (Rack/Charged/High/Low) + فصل إلزامي (Tariff/ExtraBed/Plan)؛ الأنواع المذكورة نصاً: Service Charges, Luxury Tax, Sales Tax (FAS-SET) — أسماء ضرائب المنطقة العربية `[NOT DOCUMENTED]` (تخصيص زبون) |
| UNK-009 | هل الحجوزات تدعم Group Blocks/Allocation حقيقية (PMS allotments)؟ | يحسم تصميم Reservation model | فهرس FOM-SET (Group Business Sources) — غير حاسم | Unknown | عالٍ | قراءة FOM-RES |
| UNK-010 | ما علاقة Care بـ HRP في بيانات الموظفين (Personnel Master واحد أم مستقل)؟ | يمنع ازدواجية Employee entity | فهارس Care-SET (Adding Employee) وHRP-SET | Unknown | متوسط | قراءة الاثنين |
| UNK-011 | آلية "Auto Indent" من BNQ/FNB إلى MGT — هل تولد Purchase Requisition تلقائياً من متطلبات الوليمة؟ | تكامل تشغيلي جوهري | **MGT-DNT قُرئ كاملاً (§6 DPR + §8 Re-Order)** | **Partially Resolved** | عالٍ | **قناتان موثقتان داخل MGT:** (1) **DPR**: عند إصدار ضد Indent برصيد Nil → "enter the requisition in the DPR Qty field... will be reflected during the Receipt entry" (DNT ص40)؛ (2) **Re-Order Process** الآلي عند ≤ Reorder Level → PR للقسم. **يبقى اتجاه BNQ/FNB→MGT [NOT DOCUMENTED]** — يفحص عند قراءة BNQ-BIL/FNB-COP |
| UNK-012 | هل يدعم POS الدفع المقسّم (split payments) وMixed payment على طاولة واحدة؟ | سلوك كاشير POS | **TS Manual ص28-36 (قرئ)** | **Resolved** | — | **نعم بوضوح:** Split Checks **3 طرق** (Equal/Covers · Item-wise · **Quantity-wise كسري 0.5**) + Link Tables (دمج طاولات بفاتورة واحدة) + Table Suffix؛ والتسويات 6 أنماط (Cash/CC/Cheque/Coupon/Guest/Void) **متسلسلة على الفاتورة** بقاعدة **Balance=0 إلزامية** قبل الحفظ (= mixed payments) + **Resettlement** بوضع آخر — راجع `point-of-sale/04-workflows.md` WF-POS-09/10 |
| UNK-013 | أين تُخزَّن الصلاحيات: لكل شاشة؟ لكل عملية؟ لكل Transaction Type؟ | تصميم permission model | **SYS-SSP Ch1 قُرئ كاملاً + ACR-SET §4 + FAS-SET + POS-SET** | **Resolved** | — | **النموذج الرباعي الطبقات موثق:** (1) SYS المظلة: Supervisor=تجاوز كامل · Group/User × Main/Sub Module × بند قائمة × **Add/Modify/Delete** (لعناصر Settings/Transaction/Master المؤهلة فقط) · قيود التقارير Spool/Export/Format · تخصيص الداشبورد؛ (2) صلاحيات خاصة لكل وحدة: AR (أنواع قيود) · FAS (Transaction Types) · POS (3D كاشير×عمل×وضع + حجب منافذ) · FO (تفويض مزدوج). SYS يمنح الوصول للقائمة والوحدة تحكم بدقة العمليات داخلها — راجع `modules/system-setup/07-permissions.md` + قرارات F-SYS-8/9 |
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
| UNK-022 | أرقام Module Attributes/INI الكاملة (الموثق مبعثراً: FO Attr 1-67 · POS 6/29/32 · INI 56/58/64/74/283/404/504 · FAS Sw4 · INV 1/3/4) — المرجع «Module Attributes & INI Settings» خارج حزمة 65؟ | مفاتيح سلوكية | **SYS-SSP قُرئ كاملاً — إحالتان صريحتان ص33/ص37 للوثيقة الغائبة** | **Resolved** | — | **مؤكد: المرجع خارج الحزمة (GAP-SYS-D01)** — لا توجد خريطة كاملة؛ الاستراتيجية المعتمدة: **جدول تراكمي للإحالات المرقمة** يُغذّى من قراءة كل وحدة (الحالي: 15+ مفتاحاً) — راجع `modules/system-setup/02-configuration.md` §2 |


## المجهولات المكتشفة في الجلسة 5 (من SYS-SSP)

| ID | السؤال | لماذا يهم | المصادر المفحوصة | الحالة | الأثر | المسار |
|---|---|---|---|---|---|---|
| UNK-023 | ما سلوك النظام عند انتهاء صلاحية كلمة المرور (Password Expires)؟ حظر؟ إلزام تغيير؟ | تجربة مستخدم + سياسة أمنية | SYS-SSP Ch1 §1 (الحقل موثق) + Ch2 §6 (إدارة) | Unknown | متوسط | [NOT DOCUMENTED] — يُغلق بقرار تصميمي في AC-1 (إلزام تغيير عند أول دخول) |
| UNK-024 | ما «Gift Shop» المذكورة كوحدة هدف في Reason Codes (9 وحدات)؟ وحدة مستقلة بلا أدلة أم منافذ POS؟ | نطاق الوحدات في البنية المستهدفة | SYS-SSP Ch3 §6 ص61 | Unknown | منخفض | قراءة BNQ/MEM أو إسقاطها كمنافذ POS — [UNCERTAIN] |
| UNK-025 | ما وظيفة «Group Nationality» (§19 — غير مدرجة في TOC، صفحة ونصف هامشية)؟ | قد تكون جنسيات جماعية للولائم/المجموعات | SYS-SSP Ch3 §19 ص108-109 | Unknown | منخفض | [UNCERTAIN] — فحص تقاطعها عند قراءة BNQ/FOM-GST |
| UNK-026 | هل يُحذف المستخدم مادياً أم تعطيله فقط (لا حذف موثق في SYS-SSP)؟ | خصوصية البيانات + نموذج المستخدم | SYS-SSP Ch1/Ch2 كامل | Unknown | منخفض | [INFERENCE] تعطيل فقط — يُقرر في تصميم User lifecycle |

## المجهولات المكتشفة في الجلسة 6 (من MGT)

| ID | السؤال | لماذا يهم | المصادر المفحوصة | الحالة | الأثر | المسار |
|---|---|---|---|---|---|---|
| UNK-027 | ما توقيت ترحيل MM→FAS (فوري عند كل معاملة / دفعة يومية / مع الإقفال الشهري Ledger)؟ | جوهر دورة القيود الشرائية | MGT كامل (رابط الترحيل موثق دون توقيت — GAP-MG-D04) + FAS-TRN | Unknown | **عالٍ** | يُحسم في Phase 6 (أنماط FO/POS دفعات مقابل AR فوري تسمح بالاحتمالين) |
| UNK-028 | من يملك تعريف Company Types: FO (نص MGT ص22) أم SYS؟ (بنية Vendor Code TTT+XXXX كلها تعتمد عليه) | توحيد كيان الترميز مع AR | MGT-SET §9 + (SYS-SSP لا يذكره) + FO | Unknown | عالٍ | Phase 11 مع AR mapping — مرشح: Supplier Group مشترك (F-MG-11) |
| UNK-029 | هل Gate Receipt/Gate Entry# في Receipt Other Details ترتبط بوحدة Gate Passes المستقلة في الحزمة؟ | تكامل استلام-بوابة | MGT-DNT §6 (الحقول) + فهرس Gate_Passes غير المقروء | Unknown | متوسط | قراءة وثيقة Gate Passes (جلسة قادمة) |
| UNK-030 | هل مبيعات Shop Outlet (POS) تخفض مخزون MGT مباشرة (Item-Level) أم عبر مقاصة FNB؟ | نموذج تكامل البيع التجزيء | MGT-SET §5 (الربط موثق 1:1) + POS-* (لا ذكر) | Unknown | متوسط | قراءة FNB-COP أو POS-REP — [INFERENCE] الربط الهيكلي موجود بلا مسار مخزوني موثق |
| UNK-031 | ما دلالة حالة «Blank Space» في PO Status by Vendor؟ | دقة تفسير حالات PO | MGT-LUK §6 ص13 | Unknown | منخفض | [INFERENCE] على الأرجح PO بلا أي استلام/حركة — يُطابق Pending عند التنفيذ |
