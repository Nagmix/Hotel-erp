# 04 — سير العمل (Workflows) — وحدة Materials Management

> WF-MG-01..19 خطوة بخطوة من المتن. الوحدة **الأغنى بدورات عمليات كاملة** (سلسلة توريد من 8 مراحل + 3 دورات شهر ختامية).

---

## WF-MG-01 — إنشاء مخزن وتفعيله (التأسيس)

**المصدر:** MGT-SET §1 ص3-6 + §4 ص9-10 + §6 ص17-19.

1. Setup → Stores Creation → New.
2. Applicable From (≥ اليوم) + Store Code (3 خانات فريدة) + Name + Short + Store Type (Main/Sub/Independent).
3. إن كان Sub → إلزامي اختيار Main Store Code (F1).
4. اختيار Rate Calculation: **Weighted Average أو FIFO** → Save.
5. Stores Start Date: Month/Year (**≤ الشهر الحالي**) + Type + Store Name → Save.
6. Inventory Master: تعريف الأصناف المربوطة بالمخزن (راجع WF-MG-02).
7. Opening Balance: إدخال الرصيد الختامي السابق (Gr.Date تصاعدياً + Batch/Expiry عند اللزوم + Qty/Rate → Value تلقائي) → Save.

**تحذير التجميد:** الرصيد الافتتاحي **يُقفل نهائياً** بمجرد بدء معاملات المخزن؛ والـ Store Code نفسه لا يُعدَّل ولا يُحذف بعد الحفظ (إصلاح الخطأ = Passive + كود جديد).

## WF-MG-02 — تعريف صنف مخزني كامل

**المصدر:** MGT-SET §5 ص10-17.

1. Inventory Master → New → Item Code (**رقمي ≤12**، فرادى عمومية) + Name + Item Group (إلزامي) + Item Type (Stockable/Non-Stockable/Cash Purchase/Butchery) + Regular + Part # + Issue UOM (**وحدة المحاسبة القياسية**) + Conv Factor UOM (للأجزاء) + Exp.Date/Batch#Mandatory/Consignment/Capital Goods.
2. اختيار Main/Ind. Store(s).
3. **Store-wise Stock Levels:** Min/Max + **Re-order Level** (مولّد طلبات الشراء!) + Re-order Qty + Location (متحقق من Item Locations) + الأعلام: Issue Allowed/Receipt Allowed/Receipt Return.
4. (اختياري) Barcode Link عند INI #245 ∈ {BEV,FB,LQ} — إدخال الباركود → Outlet Link.
5. (Shop Outlet فقط) ربط Outlet Code = Store Code (صنف ↔ منفذ واحد).
6. Sub Codes عند اختلاف التعبئة/الأسعار (شرط: Issue UOM ≠ Conversion UOM).

## WF-MG-03 — طلب شراء قسمي (Purchase Requisition) بتفويض متدرج

**المصدر:** MGT-DNT §1 ص2-11.

1. Daily Entries → Purchase Requisition → New.
2. Request # (تلقائي) + Request Date + Reference + Property + Department + Authorized By + Remarks + Store.
3. الأصناف: Item Code (F1) → UOM تلقائي + Quantity + Current Stock + Packing/Weight (من Master) + Required Date + Brand + Item Remarks → Save → تظهر في الجدول.
4. **التفويض (عند INI 355 ∈ {1,2,3}):** Authorization One → Two → Three **تسلسلياً** ("Level one authorization... is **mandatory before** receiving the Level 2") — بلا تفويض: "requisition issues are not allowed".
5. طباعة/بريد: "Print/Email/Print and Mail the Purchase Requisition".
6. **الإغلاق:** Close → Manual (نطاق PR#) أو Automatic (تاريخي) → تحديد إدخالات (Delete column = Yes) → Close.

## WF-MG-04 — طلب صرف داخلي (Indent)

**المصدر:** MGT-DNT §2 ص11-15 + SET §12.

1. Indent Entries → New.
2. Type (الموقع) + Store Type + النمط: **Adhoc** (يدوي) / **Template** (من Indent Templates) / **Repeat Request** (نسخ طلب سابق).
3. Date + Reference (F1) + Department + Authorized By + Property.
4. اختيار Cost Centers (متعددة — "shown column wise") → Enter.
5. الشبكة: Store + Item (F1) → UOM/Rate تلقائي + الكميات **لكل CC عمودياً** → رجوع → Save → **رقم Indent**.
6. (تفويض عند INV #6/#7 = Yes) — نفس آلية WF-MG-03.
7. **Close Indent** → اختيار الأصناف → Close.

## WF-MG-05 — دورة العطاءات (Quotation Cycle — 7 وظائف)

**المصدر:** MGT-DNT §7 ص48-57.

1. **Vendor Evaluation:** نطاق موردين → توليد تقرير نموذج التقييم (يُعبأ من المورد).
2. **Invite Quotation:** Quotation Date + Ref + **Cut-off + Expiry** → عرض Indent details → تأكيد → **Item Spec** (مواصفة الصنف) → اختيار Suppliers (نقر مزدوج) → توليد **رقم العطاء**.
3. **Tender Form:** إدخال/اختيار رقم العطاء → عرض Date/Ref/العطاءات تلقائياً → **طباعة**.
4. **Update Quotation:** تسجيل عروض الموردين المستلمة.
5. **Vendor Analysis:** "select Suppliers for Updated Quotations".
6. **Comparison Sheet:** قائمة مقارنة العروض.
7. **Close Quotation:** رقم + Reason → Confirm.

## WF-MG-06 — إنشاء أمر شراء (Purchase Order)

**المصدر:** MGT-DNT §3 ص15-21.

1. Purchase Order → New.
2. Consolidate Discount (None/Percentage+قيمة) + Vendor (F1) + Date + Reference + Currency.
3. الأصناف (Item Master Help → Enter) + Quantity → شاشة Rate → Save → الصف في الجدول.
4. Payment Term + Delivery Date + Place + Remarks + Reason.
5. أزرار مساندة: Vendor Contact Details · **Requisitions** ("select from the already created Purchase requisitions to the existing PO" — دمج PR→PO!) · **Copy PO** · **Add Image** · **Other Details**.
6. Other Details: Com.Statement# + Project/Package + Location Code (F1) + Price Basis + Delivery Period + Guarantee/Warranty + Inspection of Mat. (Y/N) + **Penalty of delay** + Other Condition.
7. Misc Tax: Tax (F1) + Currency + Type (Percentage/Amount) + Factor.
8. Save → **توليد رقم PO**.
9. (تفويض عند INV #13/#14/#298) — نفس النمط.

## WF-MG-07 — أمر شراء دائم (Standing Purchase Order)

**المصدر:** MGT-DNT §4 ص21-25.

**شرط التفعيل:** INV Switch #8/Serial 5 "In Receipt / PO Indent is not mandatory" = Yes.
1. SPO → New (SPO# تلقائي) → Vendor (بحث بالاسم/الكود) + **نطاق صلاحية التاريخ** + Location + Payment Term + Remarks.
2. الشبكة (نقر مزدوج): Store + Item + Specification + Currency + **Item Rate: Fixed أو MRP** (Fixed: لا خصم؛ MRP: خصم مسموح) + Tax Structure → Save → **رقم SPO**.
3. Close SPO عند الانتهاء.

## WF-MG-08 — أمر عمل خدمي (Service Work Order)

**المصدر:** MGT-DNT §5 ص25-30.

1. SWO → New → Vendor (F1) + SWO Date + Reference + Currency → Vendor Details.
2. الأصناف (Item Master Help) + Quantity + Rate → Save.
3. Payment Terms + Delivery Date/At + Remarks + Reason → Save → **رقم SWO**.
4. Preview متاح. **الإلغاء:** SWO# + Reason → Confirm (رسالة تأكيد). **الإغلاق:** SWO# → Details → Reason → Close.

## WF-MG-09 — استلام بضاعة (Receipt — الأنماط الثلاثة)

**المصدر:** MGT-DNT §6 Receipt ص31-37.

1. Transactions → Receipt.
2. اختيار النمط: **Contract** (SPO# — يعرض المورد تلقائياً) / **Purchase Order** (PO# — كذلك) / **Direct** (اختيار Vendor يدوياً؛ شرط INV #5).
3. GR# + GR Date (التحقق: Contract ≤ انتهاء العقد؛ PO ≥ تاريخ PO؛ Direct ≥ تاريخ الطلب) + **DS#/DS Date** (سند التسليم) + **Bill#/Bill Date** (إلزام عند INV #3 — للـ Payment Match!).
4. الأصناف (نقر مزدوج على الصفوف): **Complimentary** (بلا Rate/Tax) · Item Code حسب النمط (Contract: أصناف العقد·PO: أصناف الأمر·Direct: كل أصناف المخزن) + Conversion Factor + P.O UOM + **Batch#** (إلزام عند تكرار الصنف!) + Expiry (**≥ تاريخ النظام**) + Unit Weight (Kg) + Quantity + Currency/Tax/Rate/Value (تلقائي للعقد/PO؛ يدوي للـ Direct + **Exchange Rate** عند عملة أجنبية) + Cost Center (**للـ Non-Stockable/Cash فقط**) + Sub Store (للـ Main).
5. **Mis Tax Ded** (ضريبة على مستوى الاستلام كاملاً): Tax code + Currency (قاعدة: **نفس عملة الشاشة → Percentage أو Amount؛ عملة مختلفة → Amount فقط**) + Type + Factor → Other Cur.Val/Local Value تلقائي.
6. **Other Details:** Gate Receipt Record #/Date + Gate Entry #/Date + Location + **Rejected Report #/Date** + Mode of Transport.
7. Add Image (delivery challan) + **View Entries** (معاينة قبل الحفظ) → Save.

## WF-MG-10 — إصدار مباشر (Issue Direct)

**المصدر:** DNT §6 Issue (Direct) ص37-38.

1. Transactions → Issue (Direct) → Doc Number (تلقائي) + Indent# (3 خانات) + Store + Issue Date.
2. Item (F1) → "The total quantity available in the store as on the system date will be shown" → إدخال الكمية.
3. **Batch Help:** "with date in **ascending order**, the items will be distributed" — توزيع الدفعات بتاريخ تصاعدي/أقرب انتهاء + تعديل لحظي للكميات.
4. Rate/Value محسوبان + Cost Center → Save.

## WF-MG-11 — إصدار ضد طلب (Issue Indent) + قناة DPR

**المصدر:** DNT §6 Issue (Indent) ص38-40.

1. Issue Date (**≥ تاريخ النظام**) + Indent# (F1) → عرض Department/Authorized By/Property/CC من الطلب.
2. اختيار الطلب → Enter → **الشبكة:** CC + Store + Item + UOM + Total Indent Qty + Balance + Issued Qty + **الرصيد Batch-wise**.
3. إدخال Issue Qty مع اختيار الـ Batch.
4. **عند رصيد صفر:** "If the item has 'Nil' balance, you can enter the requisition in the **'DPR Qty' field**. The DPR recorded here **will be reflected during the Receipt entry**" — توليد طلب شراء قسمي تلقائي المنعكس!
5. Reason (من Reasons Definition في SYS) عند اللزوم → Confirm → Save.

## WF-MG-12 — المرتجعات (Receipt Return / Issue Return)

**المصدر:** DNT §6 ص40-43.

**Receipt Return (إلى المورد):** Ref# (**3 خانات حرفية**) + Store + Date + Vendor + **GRR#** (F1 → يعرض تلقائياً: GRR Date/DC#/DC Date/Bill#/Bill Date/Item/UOM/Rate/Value/Batch#/Expiry/Currency/Exc.Rate) + Quantity + Remarks → Save. الأسباب الموثقة: "excess receipt, poor quality of Items, spoilage".

**Issue Return (من مركز التكلفة إلى المخزن):** Store + Indent# (**3-10 alphanumeric**) + Issue Return Date + Item (F1 → CC/GRR#/GRR Date/Batch#/Expiry/Quantity تلقائي) + Quantity + Rate/Value + Remark. الأسباب: "Spoilage/Poor Quality/Excess Issue/Not Requested Items". **المنطق:** "handled based on the GRR Date / Batch wise data captured during posting of issue items".

## WF-MG-13 — تسوية مخزنية (Adjustment)

**المصدر:** DNT §6 Adjustment ص43-45.

1. Adjustment By: **Quantity أو Value** — "both towards **plus and minus**".
2. Store + Adjustment# (≥3 alphanumeric) + Adjustment Date + **Include Zero balance** (checkbox لذوات الرصيد الصفري).
3. Item (F1) → GRR#/GRR Date/Batch#/Expiry + **Closing Balance (Qty/Rate/Value)** تلقائي.
4. Adjustment Quantity/Rate/Value (حقلان قابلان للإدخال).
5. **عند السالب:** Adjustment Type (السبب) يتفعل — "will remain **unknown** by default if any positive adjustments done".
6. Authorized By + Remarks → Save. **قيود الدعم:** "Only for those items whose stock balance is maintained and Good Receipts for stock is maintained" + "For Stores defined with **FIFO** method of valuation, the adjustment methodology will be supported".

## WF-MG-14 — التحويلات الداخلية (Inter-Store / Sub-Store / CC)

**المصدر:** DNT §§9-12 ص57-69.

**Inter Store Requisition:** Store + Date + Item Groups → **Load Stock Details** → Reference + Authorized By → Save + **F3 Stock Locator / F7 Sale History** (شهر→يوم، سنة حالية مقابل سابقة).

**Inter Store Transfer:** From Store + To Store + Date + Month/Year الإنشاء → Load → اختيار الأصناف + Transfer Qty → Save.

**Sub Store Transfer:** Date + Reference# + From/To Sub Stores + Item + Quantity (Balance تلقائي) + UOM + Rate/Value + Remarks → Save.

**Cost Center Transaction:** CC Start Date (إن لم يوجد) → Physical Stock Entry CC (CC/Room + Item + Qty → Variance view) → Source CC/Room → Target CC/Room + Item (Closing Balance تلقائي) + Qty + Description → Save.

## WF-MG-15 — إعادة الطلب الآلية (Re-Order Process)

**المصدر:** DNT §8 ص57-60.

1. Re-Order Process → Store + نطاق Item Groups → **Process** → **رقم معالجة** ("The following screen is displayed with the Process number").
2. **Update & Generate:** Request# (F1 — يعمل فقط بعد Re-Order entry) + From/To Item Group → Load → **Update** → "All processed and updated requisitions will be **posted to a Department** for reflection in Purchase Reflection".
3. القسم يقرر: "placement of order with the Vendor or they might do a Direct Purchase".

**المحفّز:** "all the items whose Stock Balance is **equal to or below** the Re-Order level as specified in the Inventory Master".

## WF-MG-16 — التحويل التصنيعي (Conversion Split/Add)

**المصدر:** DNT §6 Conversion ص45-47 + SET §§20-21.

**Split (واحد → متعدد):** Date + Transfer Code (F1) + Reference# (≤10) → From (Store+Item) → To (الأصناف الناتجة من Master) + **Yield %** + Conversion Factor → Component Cost (من Define Component — "the user have to incur the operation cost") → **التحقق: To Qty = From Qty** → Save.

**Add (متعدد → واحد):** Date + Transfer Code + Reference + **Proceed** (يفعّل From) → From (المكونات — نقر مزدوج يعرض Batch) + Component Cost → To (الناتج) + Quantity/Balance → Save.

## WF-MG-17 — الجرد الفعلي (Physical Stock Entry)

**المصدر:** DNT §13 ص69-72.

**المسار A (Independent):** Store → New → Date (**Month/Year يجب < شهر الخادم!**) → Item (F1 → Name/Quantity) → Quantity (→ Batch Help للتأكيد + Value تلقائي) → **Load** → **Variance** (Physical مقابل Balance) → Save.

**المسار B (Main/Sub):** Store → Date → **Group Code** (F1) → Load (Stock/Rate/Value/**Variance** للأصناف في المجموعة).

**الغرض:** "Normally... only when there is a **variance** of item between Physical Stock and Stock Balance... also performed as a **month end process**".

## WF-MG-18 — تحديث الفروقات (Stock Variance Updation)

**المصدر:** DNT §14 ص72-73.

1. Store Variance Updation → Store → Update.
2. **تنبيه إجرائي:** "The following screen is displayed alerting if the **Physical Stock Variance report has been checked**" → متابعة → "message that the updation was done successfully".
3. الأثر: "The excess or short variance is referred as **Adjustment Transactions**" — توليد معاملات تسوية آلي + الترحيل لمركز التباين (Variance CC) للسالب.

## WF-MG-19 — إقفال دفتر المخزن (Process Store Ledger)

**المصدر:** DNT §15 ص73-75.

1. Process Store Ledger → Process → Store → تنفيذ.
2. **الأثر:** "enabled after the beginning of a new month to enable the printing of **Stores Ledger**. After the Stores Ledger is processed, **update of transactions will not be allowed for the processed months except for the current month**".
3. **فك التجميد:** Cancel Stores Ledger → Store → تنفيذ (ثم إعادة المعالجة بعد التصحيح).

**السلسلة الشهرية الكاملة:** WF-MG-17 → WF-MG-18 → WF-MG-19 (جرد → تسوية → إقفال) — "also performed as a month end process" تتكرر نصاً في الثلاثة.
