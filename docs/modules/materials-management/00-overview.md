# 00 — نظرة عامة (Overview) — وحدة Materials Management (MGT)

> **وحدة دورة التوريد والتكلفة الكاملة**: المشتريات → الاستلام → التخزين → الإصدار/الاستهلاك → الجرد والتسويات → الترحيل المالي. المقروء عميقاً كاملاً (الجلسة 6): **MGT-SET (68 ص، 28 قسماً) + MGT-DNT (75 ص، 15 وظيفة Daily Entries) + MGT-LUK (38 ص، 20 استعلاماً)** — إجمالي 181 صفحة. الملف الرابع MGT-REP (112 ص) مؤجل للمرحلة 7 (التقارير) وفق بروتوكول الجلسات.

---

## 1. حدود الوحدة

| البند | الوصف الموثق |
|---|---|
| الاسم النظامي | Materials Management — "The Setup menu item of the Materials Management module explains the various settings that are necessary for the Materials Management module to work efficiently and **in connection with other modules**" (SET ص2) |
| الوظيفة الجوهرية | **أربع وظائف طبقية**: (1) Setup — تعريف المخازن والأصناف والموردين والقوالب والأدوار الضريبية؛ (2) Daily Entries — دورة الطلب والشراء والاستلام والإصدار والتحويل والجرد؛ (3) Lookups — 20 استعلام تشغيلي فوري لحالة الطلبات والمخزون والاستهلاك؛ (4) Reports — مؤجلة (REP) |
| المركز المعماري | **حلقة التوريد المغلقة**: تستهلك من SYS (Cost Centers/Reasons/Tax/UOM/Company Types) وتغذّي FAS (Purchase Journal + روابط الترحيل) وF&B Costing (الاستهلاك والتكلفة المعيارية) — "The cost for the Item Groups is arrived... mainly used with Costing under Foods & Beverages" (SET ص7) |
| نمط التشغيل | مخازن هرمية (Main → Sub؛ Independent منفصل) بتقييم مخزون لكل مخزن (Weighted Average / FIFO)؛ معاملات يومية بتواريخ أعمال مقيدة؛ **عمليات شهر ختامية ثلاث** (Physical Stock → Stock Variance → Process Store Ledger) تجمّد الشهر |
| النطاق | Stores (3 أنواع) · Item Groups/Items/Sub-Codes · Vendors (7 خانات مرمزة) + عقود + تقييم · Indents (Adhoc/Template/Repeat) · Purchase Requisitions بثلاث درجات تفويض · Quotations (دورة 7 وظائف) · PO/SPO/SWO · Receipts (Contract/PO/Direct) · Issues (Direct/Indent) · Returns (Receipt/Issue) · Adjustment · Conversion (Split/Add) · Re-Order · Inter-Store/Sub-Store Transfers · Cost Center Transactions · Physical Stock/Variance/Store Ledger · Budgets · FSN · Purging |
| خارج النطاق | فواتير الموردين المالية وتسديداتها (FAS — Payment Match يستهلك Bill# من هنا فقط)؛ وصفات F&B Costing (وحدة FNB — تستهلك الأصناف والاستهلاك)؛ وثيقة «User Defined Print Forms» التفصيلية (تحيل إلى Getting Started — GAP-SYS-D02)؛ تفاصيل «Module Attributes & INI Settings» (خارج الحزمة — GAP-SYS-D01) |

> ⚠️ **اكتشاف معماري جوهري:** هذه الوحدة تُظهر **أكبر كثافة مفاتيح Module Attributes/INI موثقة** في الأدلة حتى الآن: **INI #39 (طول كود الصنف ≤12) + INI #131 (تشغيل Sub Cost Centre) + INI #245 (Barcode BEV/FB/LQ) + INI #355 (INVPURREQAUTHORISATION — درجات تفويض طلبات الشراء)** و**Module Attributes INV: #3 (إلزام Bill#) + #5 (الاستلام بلا PO) + #6/#7 (تفويض Indent) + #8 (تشغيل SPO) + #13/#14/#298 (تفويض PO)** — يوسّع الجدول التراكمي لمفاتيح الإعداد إلى 25+ مفتاحاً موثقاً بالإحالة.

## 2. جرد الوظائف الموثقة (28 + 15 + 20 = 63 وظيفة)

| الدليل | الوظائف | العدد | المصدر |
|---|---|---|---|
| **MGT-SET** (Setup) | Stores Creation · Item Group Creation · Item Locations · Stores Start Date · Inventory Master · Opening Balance · Vendor Rating · Terms of Payment · Vendor Master · Item Master by Vendor · Vendor Contract Info · Indent Templates · Sub Cost Centre · Variance Cost Centers · Link Cost Centers to Dept · Tax Exemptions · Item Taxes · Define FSN · Define Component · Item Conversion Split · Item Conversions Add · Budget Entry · Foot Notes · Access Rights · Email Access Rights · Indent Purging · Purge PO/SPO · User Defined Print Forms | 28 | TOC SET ص1-2 + المتن |
| **MGT-DNT** (Daily Entries) | Purchase Requisition · Indent Entries · Purchase Order · Standing Purchase Order · Service Work Order · Transactions (Receipt/Issue×2/Returns×2/Adjustment/Conversion×2) · Quotation Analysis (7 وظائف فرعية) · Re-Order Process · Inter Store Requisition · Inter Store Transfer · Sub Store Transfer · Cost Center Transaction · Physical Stock Entry · Stock Variance Updation · Process Store Ledger | 15 (≈24 فرعية) | TOC DNT ص1 + المتن |
| **MGT-LUK** (Lookups) | Requisition Status · Indent Status · Indent Status by Item · Authorization Details · PO Status · PO Status by Vendor · Cancelled & Closed PO · Pending PO · SPO Status · SWO Status · Receipt/Issue by Group · Store Balance by Date · Item Stock Status · Item Stock Balance · Item Balance by Date · Consumption Detail · Group Cons Month Range · Item Stock by CC · Vendor Selection · Spending Pattern | 20 | TOC LUK ص1 + المتن |

## 3. المفاهيم الجوهرية الموثقة

| المفهوم | الدلالة | المصدر |
|---|---|---|
| **تسلسل المخازن الثلاثي** | Main Store ("main division of Stores that can transfer items to Sub-Stores") / Sub Store ("can receive items **only from the Main Store to which it is linked**") / Independent Store ("can receive and issue items directly... does not depend on other Stores") — هيكل توريد صارم أحادي الاتجاه للأعلى | SET §1 ص5 |
| **Rate Calculation (التقييم)** | **Weighted Average**: "Weighted Average = (Closing Balance Value / Closing Quantity)" — بمثال الكاجو الرقمي الكامل (قيمة الافتتاح + الاستلام − الإصدار + مرتجع الإصدار − مرتجع الاستلام ÷ الكميات)؛ **FIFO**: "The items are prioritized to disperse based on their **expiry dates**" — أي FEFO فعلياً في التطبيق الأصلي! | SET §1 ص5-6 |
| **Item Code الإصداري** | "numeric Code up to a maximum of 12 characters as defined in an INI file... setting # 39"؛ "The length of the Item code once specified **cannot be altered** after start of Operation"؛ **Sub Codes** لنفس الصنف بتعبئة وأسعار مختلفة: "An Item, which is purchased / received with different packing and rates, can be entered as Sub Codes under the Main Item Code" — ممكن فقط إذا اختلفت Issue UOM عن Conversion UOM | SET §5 ص10 |
| **أنواع الأصناف الأربعة** | Stockable (مخزن ويصدر) / Non-Stockable (يستلم ويصدر مباشرة إلى Cost Center) / Cash Purchase (شراء نقدي من السوق المفتوح يصدر مباشرة) / Butchery (صنف مخزني بتقييم خاص — التحليل/التقطيع) | SET §5 ص11 |
| **Vendor Code المرکّب** | "seven characters in length. The **first three characters is the Vendor type**, which is defined in the **Company Types option under the Front Desk module**, followed by the four-character user specified code" — **اعتماد توثيقي عبر الوحدات على FO** (نفس عائلة ترميز AR/Company TTT+XXXX!) | SET §9 ص22-23 |
| **تفويض متعدد الطبقات** | PR: Authorization One/Two/Three — "mandatory only if INI Setting 355 'INVPURREQAUTHORISATION=0' is set to '1' for Level One... '2' for Level Two, and '3' for Level Three"؛ "If authorizations are not made, **requisition issues are not allowed**"؛ Indent: Module Attributes #6/#7؛ PO: #13/#14/#298 | DNT §1 ص5 + §2 ص15 + §3 ص21 |
| **DPR (Department Purchase Requisition)** | عند الإصدار ضد Indent ورصيد الصنف **صفر**: "If the item has 'Nil' balance, you can enter the requisition in the 'DPR Qty' field. The DPR recorded here **will be reflected during the Receipt entry**" — **التحويل التلقائي من نقص مخزون إلى طلب شراء** (يحسم جزءاً من UNK-011: قناة Auto-Indent) | DNT §6 Issue (Indent) ص40 |
| **العمليات الشهرية الثلاث** | Physical Stock Entry ("performed as a month end process") → Stock Variance Updation ("excess or short variance is referred as Adjustment Transactions... month end") → Process Store Ledger ("process all the closing operation of monthly transactions... After the Stores Ledger is processed, **update of transactions will not be allowed for the processed months except for the current month**") + Cancel Stores Ledger لفك التجميد | DNT §13-15 ص69-75 |
| **Variance Cost Centers** | "mandatory requirement for **automatic posting of negative (short) variances**" — كل مخزن يحتاج مركز تكلفة/مخزن فرعي مستهدف لترحيل الفروقات السالبة آلياً | SET §14 ص44 |
| **نموذج Bill#/Payment Match** | "The Bill # and Bill date is **mandatory**. It is always recommended... This will be used in the **Payment Match option while making Payment**" (شرط Module Attribute #3) — حلقة الربط مع تسديدات الموردين في FAS | DNT §6 Receipt ص32 |
| **Complimentary Items** | "Items received can be Complimentary or Non-Complimentary. If it is a Complimentary item, **the Rate Plan and Tax Structure will not be applicable**" — استلام مجاني بلا تقييم ضريبي | DNT §6 Receipt ص33 |
| **Stop Purchase / Stop Payment المنطقان** | Stop Purchase (YES = منع الشراء من المورد) مقابل Stop Payment (منطق **معكوس**: "select the option NO... Unless you change this option to YES, the system will **not allow** you to make any payments" — النص الأصلي ملتبس والسلوك الظاهر: الحقل يعمل كمفتاح تفعيل للسماح!) | SET §9 Payment Details ص27-28 |
| **Fixed vs MRP** | في SPO: "FIXED: A price fixed to a particular product, so **cannot enter the discount**. MRP: Maximum retail price, **can enter the discount**" — سياسة خصم ثنائية على مستوى الصنف في أوامر الشراء الدائمة | DNT §4 ص23 |
| **شاشة عمليات ذكية** | شاشة Transactions الرئيسية تعرض دائماً: "pending Indents, expected Receipts (for 7 days), expiring items, items whose stocks are **below minimum level** and Inter Store transfers requisitions" + شريط حالة بعدّاد — **لوحة عمليات يومية مدمجة** (نموذج UX للواجهة الجديدة) | DNT §6 ص31 |

## 4. التفاعلات مع الوحدات (موثقة نصاً)

- **MGT ← SYS:** Cost Centers (Indent Templates "A list of all Cost Center defined under System Setup modules" SET ص41 · Variance CC · Link CC to Dept)؛ Reason Codes ("Reasons are displayed from the Reasons Definition option under System Setup module" DNT ص40)؛ محرك الضرائب الثلاثي (Tax Structure في PO/Item Taxes)؛ UOM؛ Module Attributes (مفاتيح INV) + INI (#39/#131/#245/#355)؛ User Defined Print Forms (تحيل إلى Getting Started).
- **MGT ← FO:** Company Types — "the Vendor type, which is defined in the Company Types option **under the Front Desk module**" (SET ص22) — **نفس عائلة كيانات الشركات/الوكالات التي تغذي AR**.
- **MGT → FAS:** رابط الترحيل MM→Finance الموثق في FAS-SET (الرابط 3 من الست) + Tax Exemptions: "The tax values will be reflected separately during posting and generation of **Purchase Journal to the General Ledger**" (SET ص47) + Bill#/Bill Date → Payment Match + Variance Cost Centers (ترحيل الفروقات) + Vendor Currency/Exc. Rate.
- **MGT → F&B Costing (FNB):** Item Group Type "important for F&B costing module to help pick up the appropriate consumption figures in relevant cost type reports" (SET ص7) + Conversion UOM "where the Sale / Stock and Consumption at the Outlets/Kitchens are in portions. This will be reflected in Food and Beverage Costing" (SET ص10).
- **MGT → POS (Shop Outlet):** "If selected Main/Ind Store is Shop Outlet then the **Outlet Link** will get enable... **Outlet Code and Store code should be same**; and the item can be tagged to **only one shop outlet**" (SET ص15) — جسر مخزن-منفذ للبيع بالتجزئة + Barcode (INI #245 = BEV/FB/LQ) يحمّل تفاصيل الصنف في "Transactions-Receipt entry".
- **MGT → AR (غير مباشر):** Vendor = كيان طرف ثالث مشترك مع Company/Agency (عبر Company Types في FO) — الموردون في FAS/AR يتشاركون بنية الترميز TTT+XXXX.

## 5. أهم الاكتشافات المعمارية (الجلسة 6)

1. **FIFO الأصلي = FEFO وظيفياً:** "The items are prioritized to disperse based on their **expiry dates**" (SET ص6) + في الإصدار: "items will be distributed [in] **ascending order** [of] date" مع Batch Help (DNT §6 ص38) — الإصدار دائماً من أقدم تاريخ استلام/أقرب انتهاء — **قرار تنفيذي للواجهة الجديدة: اعتماد FEFO صريح للأصناف ذات تاريخ صلاحية** (يتوافق مع Batch/Expiry القياسي في ERPNext مع Serial/Batch Bundle).
2. **كثافة مفاتيح الإعداد القصوى (25+ مفتاحاً):** INI #39/#131/#245/#355 + INV MA #3/#5/#6/#7/#8/#13/#14/#298 — الوحدة الأكثر تفعيلاً بالمفاتيح بعد FOM؛ **نموذج التفويض متدرج (0-3) عبر قيمة مفتاح واحد** (INI 355) يختلف عن نمط Yes/No السائد — يدعم تصميم Feature Toggle بحقل **قيمة تعددية** لا ثنائي فقط (تحسين قرار F-SYS-1).
3. **حلقة DPR التلقائية:** Indent → رصيد صفر → DPR Qty → يظهر في Receipt entry آلياً — **أقرب دليل موثق حتى الآن على Auto-Indent** (يحسم جزء UNK-011: القناة موجودة لكن من الإصدار نحو الشراء، وليس من BNQ/FNB نحو المخزن — يبقى اتجاه BNQ غير مؤكد).
4. **التجميد الشهري المتدرج (Three-tier Freeze):** Process Store Ledger يجمد الشهور المعالجة (باستثناء الحالي) + Cancel Stores Ledger لفكه — **نفس عائلة قواعد التجميد في FAS (Open FY/Rollback) وFO (Night Audit Open New Date)** — النمط المعماري الثالث للإغلاقات الدورية بعد Night Audit (يومي) وFinancial Year (سنوي).
5. **Vendor Master أغنى من Supplier القياسي:** 7 عائلات تفاصيل (TDS/Payment/Bank/Contact/Tax/Black-List/Other) + جدول تقويم **"أيام دفع ثابتة"** ("select any 9 days in a month to schedule payments") + 5 شرائح خصم نقدي + شرائح فوائد تأخير + Stop Purchase/Stop Payment — **أغنى من ERPNext Supplier بمرتين** (يحتاج DocType مخصص موسّع فوق Supplier — قرار F-MG-2).
6. **Quotation Cycle كامل من 7 وظائف** (Vendor Evaluation → Invite → Tender Form → Update → Vendor Analysis → Comparison Sheet → Close) — **لا نظير مباشر في ERPNext** (Material Request/Supplier Quotation يغطيان جزءاً فقط) → دورة عطاءات مخصصة (قرار F-MG-5).
7. **Budget بمسارين (Fixed/Apportion):** "If Apportion, then select the Apportion Type... assign budget values automatically to each cost center for each month" + اختصارات لوحة المفاتيح F2 (نسخ سنة مركز) / F4 (لصق لمركز آخر) — يفوق ERPNext Budget القياسي (الذي يوزّع بالتساوي أو يدوياً) بمرونة التوزيع التلقائي بأنماط — **قرار تخصيص F-MG-7**.
8. **تصادم تسمية DNT:** الملف المسماة "Daily Entries" (وليس OPR) في الحزمة؛ القوالب السابقة أشارت إلى MGT-OPR — **الصحيح DNT (Daily Entries)** — حُدّثت الخرائط بناءً عليه.
9. **غنى الاستعلامات التشغيلية:** 20 استعلاماً بالتصفية (Store/CC/Item/Vendor × Date/Month × Status) مع **Drill-down ثلاثي المستوى** في Group Cons Month Range (مجموعة → صنف → شهر → Item Stock Status!) وSpending Pattern (سنة حالية مقابل سابقة → شهر → يوم) — **نموذج جاهز لتصميم صفحات الاستعلام في الواجهة الجديدة**.

## 6. مصادر الوحدة

| الملف | الصفحات | الحالة |
|---|---|---|
| FN6i-NT-MGT-SET.pdf | 68 | **✓ قرئ كاملاً** (28 قسماً + جداول الحقول) |
| FN6i-NT-MGT-DNT.pdf | 75 | **✓ قرئ كاملاً** (15 وظيفة Daily Entries) |
| FN6i-NT-MGT-LUK.pdf | 38 | **✓ قرئ كاملاً** (20 استعلاماً) |
| FN6i-NT-MGT-REP.pdf | 112 | ⬜ مؤجل للمرحلة 7 (التقارير) وفق البروتوكول |
| «Module Attributes & INI Settings» | — | [NOT DOCUMENTED] — GAP-SYS-D01 (إحالات مرقمة داخل MGT هي المصدر) |
| «Getting Started» (User Defined Print Forms) | — | [NOT DOCUMENTED] — GAP-SYS-D02 |
