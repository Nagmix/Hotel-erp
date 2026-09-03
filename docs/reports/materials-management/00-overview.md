# 00 — نظرة عامة على طبقة تقارير Materials Management (Phase 7 — 3/4)

> **المصدر:** MGT-REP (112 ص / 1,745 سطر — ثاني أكبر ملف تقارير في الحزمة بعد FOM-REP، وأضخم ملف متبقٍّ بعد اكتمال FO وPOS).
> **الموقع في المشروع:** هذه الطبقة تُكمل — ولا تكرر — `docs/modules/materials-management/08-reports.md` (الذي وثّق التزامات المرحلة 7 + مخرجات LUK العشرين القابلة للطباعة + Print Forms من SET §28).

---

## 1. النطاق والإحصاء

| البند | القيمة |
|---|---|
| ملف المصدر | `FN6i-NT-MGT-REP.txt` (112 ص) |
| أقسام مرقّمة في TOC | **24 رقماً — لكن القسم 6 مرقّم مرتين!** (Item & Vendor List **و** Closing Stock by Type كلاهما "6.") → **C-MR-01** |
| بنود فرعية | 4.1–4.8 (**8** — أكبر عائلة) + 5.1–5.4 (4) + 6.1–6.4 (4) + 9.1–9.4 (4) + 15.1–15.7 (**7** — عائلة الطباعة) + 16.1–16.4 (4) + 18.1–18.4 (4) + 22.1–22.2 (2) + 24.1–24.2 (2) = **39 تقريراً فرعياً** |
| أقسام ورقية (شاشات تصنيف فقط) | 4, 5, 6, 9, 15, 16, 18, 22, 24 = **9 آباء** |
| أقسام مفردة فعلية | 1, 2, 3, 6'(Closing Stock), 7, 8, 10, 11, 12, 13, 14, 17, 19, 20, 21, 23 = **16** |
| إجمالي تقارير الأوراق | **55** (16 + 39) |
| ازدواج موثّق | §6.1 Inventory Item List = **نسخة حرفية من §1** → C-MR-02 · §24.2 Tax Report وصفها **حرفياً مطابق لـ§24.1 VAT Report** → C-MR-03 |
| تقدير التقارير الفريدة | **~53** (55 − ازدواج §6.1 − ازدواج محتمل VAT/Tax) |
| نطق تعريفي | "Reports is a sub-module under Materials Management Module" (REP ص3) — بلا غرض وظيفي موسّع (مقابل تعريف POS الغني بخمس غايات) |
| مدخل القائمة | Materials Management → Reports (ص3) |

**ملاحظة جردية:** عائلات LUK العشرين في `modules/materials-management/09-lookups.md` تتقاطع موضوعياً مع هذه الطبقة (Requisition Status · PO Status · Store Balance by Date · Item Stock · Consumption...) — لكن REP يوثّق **شاشات توليد كاملة بمعايير أوسع** (خصوصاً Store Break وComplimentary triad وR2) بينما LUK كان استعلام سريع بزر Print — التقاطع أعمق من FO/POS لأن MGT وحدة OLTP-First.

## 2. مفارقة الترقيم (C-MR-01) — الخط الأصلي لا الخصومة

على عكس POS (التي وقع فيها §6 فيزيائياً بعد §11 — إدراج لاحق)، مفارقة MGT **اتساقية الترقيم الخاطئ**:

- TOC ص2: `6._Item___Vendor_List` (بند مكسور الترميز بشرطات سفلية!) ثم `6_1..6_4` ثم سطر `6. Closing Stock by Type`.
- الجسم: ص45-46 "6. Item & Vendor List" ثم ص55 "6. Closing Stock by Type" — **القسمان يحملان الرقم 6 في TOC والجسم معاً**.
- النتيجة: كل الأقسام بعد 6' منزاحة منطقياً بواحد (7=One Line Store Balance بينما الترقيم "الصحيح" كان 8) — لكن لا يوجد انزياح فعلي لأن بقية الأقسام تُرقم تسلسلياً حتى 24.

هذا نمط ثالث من عيوب الكتالوغ (بعد انزياح POS الفيزيائي وأشباح FO/POS): **ازدواج رقم قسم بلا إعادة ترقيم لاحقة**.

## 3. العائلات الموضوعية (خريطة الكتالوج)

| العائلة | البنود | عدد | ملف التوثيق |
|---|---|---|---|
| محرك التقارير والبنية التحتية | نمط الخطوتين + Printer + **Print Forms عبر FAS** | — (عرضي) | `01-report-engine-infrastructure.md` |
| قوائم الأصناف والموردين والعقود | 1(=6.1), 6.2, 6.3, 6.4 + 9.1–9.4 | 8 | `02-item-vendor-contract-master-reports.md` |
| المشتريات (PR/PO/عطاء/فواتير) | 2, 3, 19, 10 | 4 | `03-procurement-reports.md` |
| عائلة طباعة المستندات | 15.1–15.7 | 7 | `04-document-print-family.md` |
| المعاملات والاستلام | 4.1–4.8 | 8 | `05-transaction-receipt-reports.md` |
| أرصدة المخزون | 6'(Closing), 7, 8 + 16.1–16.4 + 17 | 8 | `06-stock-balance-reports.md` |
| الاستهلاك والموازنات | 5.1–5.4 (+R2) + 22.1–22.2 | 6 | `07-consumption-budget-reports.md` |
| تحليلات المخزون | 11(ABC), 12(FSN), 13, 14, 20, 21(Efficiency) | 6 | `08-inventory-analytics.md` |
| الجرد المادي والدفاتر والتدقيق والضرائب | 18.1–18.4 + 23 + 24.1–24.2 (+4.3 إحالة) | 7 | `09-physical-stock-audit-tax-reports.md` |
| مصفوفة قواعد التواريخ | — (عرضي) | ~21 قاعدة | `10-date-validation-matrix.md` |
| التحويل والفجوات | F-MR-1..16 + GAP + AC | — | `11-erpnext-mapping-gaps.md` |

## 4. أبرز الاكتشافات البنيوية (Session 18)

1. **طباعة PO/SPO/GRN محكومة بمعامل في وحدة أخرى (FAS!)**: حرفياً — "the name of the Purchase Order print program has to be specified in the **Print Forms parameter under the Financial Management module**. The definition of the program name is **mandatory** for printing" (15.3/15.4/15.6) — أول اعتماد تكويني موثق من MGT-REP إلى FAS-SET §15 (Pgm.ID)، وأول كشف صريح أن أشكال الطباعة **برامج مخصصة لكل عميل** ("customized programs are developed for each client... to print either on **pre-printed or plain continuous or cut stationery**") — تفسير جذري لغياب تخطيطات المطبوعات في كل الوحدة.
2. **جسر GRN→المالية الموثق حرفياً** (15.6): "issue an acknowledgement to the Vendor for goods received, and to **forward a copy to the Finance department for making payments accordingly**" — دورة مستندات مدفوعات الموردين: GRN ورقي يُعبر الحدود الوحداتية إلى FAS.
3. **ABC Analysis كاملة** (§11): "% by Store Value/% by Group Value" + "%Cumulative/% Consumption" + صنفا A/B **يعرّفهما المستخدم** (C ضمني = الباقي) — منهجية Pareto مخزنية أصيلة.
4. **FSN Analysis بمعامل يُعرَّف داخل شاشة التقرير** (§12): "Double-click on the **Days column** to view the below screen. Enter the FSN Specifications" — أول إدخال معامل **مدمج في شبكة الاختيار نفسها** (نمط تفاعلي فريد في الحزمة).
5. **Efficiency Report = تحليل العائد/Yield** (§21): FROM/TO (كمية/سعر/قيمة) + التباين + نسبة الكفاءة — "When an Item is split, the quantity or yield of the converted items **can be less than** the quantity of the From Item" — تحليل خسائر التقطيع (جزّارة/مطبخ) من قلب MGT لا FNB.
6. **Audit Trial Report يعرض المحذوفات** (§23): "The user can **include all modified and deleted details** in the report" — مدى تدقيقي يشمل سجلات محذوفة (أوسع من عائلة Audit في FO التي توثق old/new فقط).
7. **Physical Stock Variance مقيدة بالبيانات** (18.1): "generated **only for dates on which the Physical Stocks were entered**" — أول تقرير نطاقه الزمني **بوابة بيانات** لا قاعدة تاريخ.
8. **بوابات "الآن فقط"**: §17 Re-Order Level ("Current System Date" حصراً — بلا معامل تاريخ) و4.8 Opening Balance ("current Month and Year" حصراً) — عائلة as-of-now فريدة في MGT.
9. **لا قنوات إخراج موثقة**: صفر ذكر لـSpool/Export في MGT-REP كله (مقابل القناة الرباعية الموحدة لـFO والخماسية لPOS مع Port ID) — الطباعة والمعاينة فقط — **كسر النمط التصاعدي** بين وحدات المرحلة 7.
10. **R2 Variant** (5.4): "Group Consumption Month Range – R2" — تقرير يحمل **لاحقة إصدار تخطيط** (R2 = Release/تنسيق ثانٍ) بنص شبه مطابق لـ5.3 — أول لاحقة إصدارية في اسم تقرير بالحزمة.
11. **Capital Goods Receipt (4.3)**: تقرير VAT للأصول الرأسمالية المستلمة — نقطة التقاء MGT↔FAS-FXD (بضاعة رأسمالية عبر مخزن→أصل ثابت).
12. **VAT Report بملف امتثال ضريبي** (24.1): شاشة ثانية "Company details for **assessment of a year**" + "Print Sequence **PJV Wise**" + Summary/Details/Both — تقرير امتثال هندي من داخل MGT (PJV مفهوم FAS مؤكد بـ§18 هناك: Pending Receipts for PJV).

## 5. علاقة هذه الطبقة بالوحدات الأخرى

| الجسر | الاتجاه | الشاهد |
|---|---|---|
| MGT → **FAS** | **تكويني (أول من نوعه)** | Print Forms parameter (15.3/15.4/15.6 → FAS-SET §15 Pgm.ID) + GRN copy → Finance للدفع (15.6) + PJV Wise (24.1 → FAS-REP §18) |
| MGT → FAS/FXD | أصول | Capital Goods Receipt (4.3) — بضاعة رأسمالية من الاستلام المخزني |
| MGT → MGT-SET | معاملي | FSN "Define FSN parameter" (§12 ← SET §18) + Foot Notes الثلاثية (SET §23: "Purchase Order Print"!) |
| MGT → FNB | تحليلي | Efficiency Report (§21) يحلل عائد التحويلات التي تنفذها FNB-COP (Inter Kitchen Transfers/Conversions) |
| MGT → MNT | تشغيلي | أصناف قطع الغيار في Item Master — Item Stock Levels يخدم Re-order صيانة |
| MGT → AR/FAS | فواتير | Supplier Bill (§10) — تحقق فواتير الموردين (وجه الدائنين من ACR المدينين) |
| MGT → HRP | زهيد | لا موظفين في 112 ص إلا ضمن Audit Trial (أثر المستخدم الضمني) — نمط الجزيرة التشغيلية |

## 6. ملاحظات الجرد (MGT-REP)

- **أكبر عائلة قوائم طباعة**: 7 مستندات تُطبع (PR/Indent/PO/Standing PO/SWO/GRN/Transactions) — MGT الوحدة الوحيدة التي تملك "عائلة إعادة إصدار مستندات" كاملة (POS لديها فاتورة واحدة، FO لديها Registration Card).
- **Print Indent بتنسيقين** (15.2): Indent Format مقابل **Contract Format** — ثنائية تحول العقد إلى مستند تشغيلي.
- **أعمق تفاعل مع مفاتيح الاختيار**: Vendor List (6.3) يقدم **5 مناظير** (standard/payment/bank/contract/tax) × 3 تفاصيل (Regular/Black List/Last Updated) × 2 ترتيب (Code/Name).
- **"Sun Cost Center Checklist"** (ص90): خطأ مطبعي متكرر (Sun بدل Sub) — يوثق دون مستوى التناقض.
- **أخطاء ترقيم خطوات**: 5.1 (الخطوة بعد 4 تُرقّم "3" مجدداً) و4.6 (تقفز من 4 إلى 6) — عائلة أخطاء تحريرية ثالثة بعد C-POS-02/03.
- **كل تخطيطات التقارير غائبة**: كل عبارة "The report will be generated in the following format:" يعقبها فراغ (صور غير مستخرجة) — على عكس FO/POS التي سربت أعمدة وصيغاً نصياً — **فجوة D06 الحاكمة لهذه الطبقة**.
