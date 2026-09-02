# 01 — البيانات الرئيسية (Master Data) — وحدة Materials Management

> كل كيانات المرجع المعرّفة في MGT-SET §§1-21 مع الحقول الموثقة والأطوال والقيود. **نمط الإصدارية الزمنية (Applicable From) سائد** في 10+ كيانات، و**Modify-Locked** في 2 كيانين حرجين (Store/Item Code length).

---

## 1. Stores Creation (الكيان الجذري للمخازن)

**المصدر:** MGT-SET §1 ص3-6.

| الحقل | المواصفة الموثقة |
|---|---|
| Applicable From | تاريخ تفعيل المخزن — ddmmyy؛ افتراضي = تاريخ اليوم؛ **يجب ≥ اليوم** (نفس القاعدة الموحدة) |
| Store Code | **كود فريد 3 خانات alphanumeric** — "unique 3-digit alphanumeric code assigned for every Store"؛ في Modify يمكن الاختيار من قائمة (F1) |
| Name | اسم المخزن |
| Short | اسم قصير "used during printing process" |
| Store Type | **Main Store / Sub Store / Independent Store** — القيود السلوكية: Sub "can receive items only from the Main Store to which it is linked"؛ Independent "does not depend on other Stores" |
| Main Store Code | **إلزامي إذا Type = Sub Store** — F1 قائمة Main Stores المعرّفة |
| Rate Calculation | **Weighted Average أو FIFO** — طريقة تقييم المخزون **لكل مخزن على حدة** |

**قواعد الكيان:**
- **Modify-Locked صارم:** "Once the Store Code is created and saved, **updation or deletion of the entry is not allowed**. However, in case of entry errors... the Status of the Store Code has to be made **Passive and a new Store Code has to be created**" (ص5 Note) — نمط الإصلاح بالإبطال لا بالتعديل.
- **مثال التقييم الرقمي الكامل (Weighted Average):** صنف الكاجو — "Weighted Average = (Closing Balance Value / Closing Quantity)" حيث القيمة = "Opening Value + Receipt Value − Issues + Issue Returns − Receipt Return divided by the Quantities accordingly" (ص5).
- **FIFO = إصدار بأقرب انتهاء:** "issue of Items from Store will be prioritized on the basis of the Expiry Date of the Goods Receipt" (ص6) — FEFO فعلياً.

## 2. Item Group Creation (تصنيف الأصناف — إلزامي)

**المصدر:** MGT-SET §2 ص6-7.

| الحقل | المواصفة |
|---|---|
| Applicable From | ≥ اليوم (النمط الموحد) |
| Item Group Code | **3 خانات فريدة** |
| Name | اسم المجموعة |
| Short Name | للطباعة |
| Group Type | "important for **F&B costing module** to help pick up the appropriate consumption figures in relevant cost type reports" |

**قاعدة:** "Every Item entered in the Inventory Master **has to be tagged** with a Group Code" — إلزامية كاملة.

## 3. Item Locations (مواقع الأصناف داخل المخزن/المطبخ)

**المصدر:** MGT-SET §3 ص8-9. الحقلان: Location Code + Description. **التحقق المتقاطع:** "Under Inventory Master, the item location **is validated** with the details captured in this parameter" — موقع الصنف لا يُقبل إلا إذا عُرّف هنا.

## 4. Stores Start Date (نقطة بدء تشغيل المخزن)

**المصدر:** MGT-SET §4 ص9-10.

| الحقل | المواصفة |
|---|---|
| Month/Year | "**less than or equal to the current month and year**" — لا يمكن بدء المستقبل! (ع**كس** Applicable From!) |
| Store Type | Main / Independent (لا Sub — يتبع Main) |
| Store Name | قائمة مخازن النوع المختار |

**الوظيفة:** "This information **enables entering Opening Balance** of the stock" — بوابة الرصيد الافتتاحي. **قاعدة:** "Once the Month/Year are entered, the **Closing Balance details** of the stockable items have to be entered" — إدخال الرصيد الختامي السابق إلزامي بعد الضبط.

## 5. Inventory Master (الكيان المركزي للأصناف)

**المصدر:** MGT-SET §5 ص10-17.

| الحقل | المواصفة الموثقة |
|---|---|
| Item Code | **رقمي فقط، ≤12 خانة (INI #39 الافتراضي 12)** — "can be modified as required **only by IDS Customer Service Engineers or by authorized EDP personnel**"؛ الطول **يُجمَّد بعد بدء التشغيل**؛ "entry of similar Item Codes for **different stores is not possible**" (فرادة عمومية) |
| Item Name | — |
| Item Group | F1 — إلزامي (تصنيف F&B/Non-F&B) |
| Item Type | **Stockable / Non-Stockable / Cash Purchase / Butchery** (Butchery = "This is a Stockable Item type") |
| Regular | Yes/No "based on the usage of the Item" |
| Part # | "contains very important information about the manufacturer. Like the **License Number** etc." |
| Issue UOM | "The **Standard Accounting UOM**... all Transactions / Stock will be valued based on this UOM" |
| Conv Factor UOM | "has to be defined where the Sale / Stock and Consumption at the Outlets/Kitchens are **in portions**. This will be reflected in Food and Beverage Costing" |
| Exp. Date | Yes/No — يفعّل Batch/Expiry |
| Batch # Mandatory | Yes/No |
| Consignment Item | Yes/No |
| Capital Goods | Yes/No |
| Main/Ind. Store | ربط الصنف بمخزن واحد أو أكثر |

**Sub Codes (مفهوم جوهري):** "An Item, which is purchased / received with **different packing and rates**, can be entered as Sub Codes under the Main Item Code, thereby avoiding entry of multiple Item Codes. Fortune will identify entry of transactions and stock **Sub Code wise**. Entry of Sub Codes is possible **only if the Issue UOM and Conversion UOM are different**" (ص10).

**مستويات المخزون (لكل صنف×مخزن):** Min/Max quantity + **Re-order Level + Re-order Quantity** — "The levels have to be entered in terms of Unit of Measurement... **Reorder Level is significant since Purchase Requisitions are generated on these specifications**" (ص12) + Location + ثلاث أعلام سلوكية: **Issue Allowed** (الإصدار لمخزن آخر) / **Receipt Allowed** (الاستلام من مخزن آخر) / **Receipt Return** (السماح بمرتجع الاستلام).

**Barcode Link (INI #245):** "Value of the INI switch **#245** should to be changed to **BEV, FB, or LQ**, based on the stores where the user need to activate the barcode" (ص14) — إدخال الباركود ينعكس في "Outlet Link" ويحمّل تفاصيل الصنف في إدخال الاستلام.

**Shop Outlet (تكامل POS):** "If selected Main/Ind Store is **Shop Outlet** then the Outlet Link will get enable... **Outlet Code and Store code should be same**; and the item can be tagged to **only one shop outlet**" (ص15 Note).

## 6. Opening Balance (الرصيد الافتتاحي)

**المصدر:** MGT-SET §6 ص17-19.

| الحقل | المواصفة |
|---|---|
| Store Type/Code | اختيار المخزن |
| O/B as on | يعرض شهر/سنة البدء (من Stores Start Date) |
| Item Code | F1 |
| Std UOM | يعرض Issue UOM |
| Gr. Date | "**ascending order of the Goods Received Date**; else, the last Date of the Up to Month/Year" — دفعات تاريخية مرتبة |
| Batch # | "only if the Expiry Date for the selected item is tagged as 'Yes'" |
| Expiry Date | لكل Batch |
| Quantity / Rate | إدخال يدوي |
| Value | **محسوب تلقائياً** |

**قاعدتان حرجتان:** (1) "Entry of Items should completed using the Inventory Master option **before** the commencement of Opening Balance entry"؛ (2) "**Once the Transactions have commenced for the Store, you will not be allowed to update the Opening Balance details**" (ص18) — تجميد الرصيد الافتتاحي ببدء المعاملات.

## 7. Vendor Rating

**المصدر:** MGT-SET §7 ص19-20. الحقول: Code (**5 خانات alphanumeric فريدة**) + Description + Sequence ("used in Vendor Analysis").

## 8. Terms of Payment (شروط الدفع)

**المصدر:** MGT-SET §8 ص20-21.

| الحقل | المواصفة |
|---|---|
| Applicable From | ≥ اليوم |
| Payment Terms | **3 خانات فريدة** |
| Long Name | الاسم |
| Grade Sequence | "used for Vendor Analysis" |

**أمثلة الدليل:** "Immediate Cash payment on delivery" / "Within 30 days from the Date of receipt of the Goods and Bill" / "Against Delivery". **الاستهلاك:** "When a purchase order is being generated, you have to enter the Payment Term in the Purchase Order entry option. The Payment term selected **will be validated** against the definition given in this parameter" (ص20).

## 9. Vendor Master (الموردون — أغنى كيان مرجعي في الوحدة)

**المصدر:** MGT-SET §9 ص22-37.

**بنية الكود:** "The Vendor Code is an alphanumeric field and is **seven characters** in length. The **first three characters is the Vendor type**, which is defined in the **Company Types option under the Front Desk module**, followed by the **four-character** user specified code" — الترميز: `TTT XXXX` (نفس عائلة AR Company Profile!).

### 9.1 الحقول الرئيسية

| الحقل | المواصفة |
|---|---|
| Vendor Code | 7 خانات (3 نوع + 4 كود) — "double-click to select the Company type from the Vendor Master Help Screen" |
| Title/Name/Address/City/State/Country/Zip/Tel#/Fax# | حقول تعريف قياسية |
| Email#1/Email#2 | بريدان |
| Vendor Rating | من Vendor Rating master |
| Black Listed | Yes/No — عند Yes: "you have to enter the name of the person/user who has black listed the vendor and give the **reason**" — **مسؤولية موثقة إلزامية** |
| Currency | "in which you will be making your transactions with the Vendor" |
| Category | Company / non Company |
| TDS Applicable | Yes/No → يفتح TDS Entry |
| State | "within the state, outside the state or a foreigner" (تصنيف ضريبي جغرافي — نمط هندي CST) |

### 9.2 TDS Entry (استقطاع الضريبة في المصدر)

الحقول: Description + Address (تلقائي) + **TDS Nature of Payment** ("Select **one or all** of the TDS payment codes") + Deduction Account Number (حساب بنك المورد!) + **PAN/GIR #**.

### 9.3 Payment Details

| الحقل | المواصفة |
|---|---|
| Credit Days | أيام ائتمان المورد |
| Credit Limit | سقف الائتمان |
| Advance % | نسبة الدفعة المقدمة |
| Stop Purchase | Yes = **منع الشراء كلياً** من المورد |
| Payment Type | **Status أو Last Date** — معيار تحديد مواعيد الدفع |
| Payment Mode | Cash/cheque/credit card/voucher |
| Payment Frequency | **Adhoc / Daily / Fixed** — عند Fixed: تقويم "select **any 9 days in a month** to schedule payments to be done **only on these days every month**" (أيام محددة بالأحمر!) |
| Stop Payment | ⚠️ منطق ملتبس: "if you want to stop making any payments to the vendor, select the option **NO**... Unless you change this option to **YES**, the system will not allow you to make any payments" — [UNCERTAIN] تسمية معكوسة (الحقل يعمل كمفتاح **Allow** عملياً) — يُسجّل بوصفه الأصلي الدقيق |
| Cash Discount Detail | **5 شرائح** خصم نقدي حسب أيام السداد — مثال: "If the payments are done within the first 5 days, then a cash discount of 10% will be allowed" |
| Interest Detail | شرائح فائدة التأخير — مثال: "If the credit days allowed are 90, and if the payment is made anywhere between 91st to 100th day, then **10% interest will be charged**" |

### 9.4 Bank Details

BACS number (Banks Automated Clearing System) + Bank Sorting Code + **Transaction Limit** ("Maximum Limit (per day) for transactions authorized to the vendor by his bank" — ≤11 خانة رقمية) + Cheque in favor of.

### 9.5 Contact Details

Title/Name/Designation/Mobile/Pager — **"You can save the contact details of maximum two people"** (سقف شخصين!).

### 9.6 Tax Details

Tax Code (F1) + Tax Number (**≤30 خانة alphanumeric مع رموز خاصة**) + Issue Date + Issue Place — إدخالات متعددة بجدول ("the details appear in the table") + تعديل بالنقر المزدوج على Tax Name.

### 9.7 Other Details (الغنية)

**تنظيمية:** Organizational Status + Name of Proprietor/Partner/Directors + Nature of Business + No. of Years Existing + Business Turnover + ESIC Regn No. + Permanent Account Number + Works Contract Tax No. + Excise Range Address + ECC No. · **شخصية:** name/address/contact · **تجارية:** Hotel Industry Cliental Base + Credit/Payment Terms (F1 من Terms of Payment) + Delivery and Packing + Other Cost/Charges + Contract Duration + **Short/Late Supply Penalty %** + Warrantee/Guarantee + After Sales Service + Any Other Info.

> **ملاحظة توثيقية:** حقل ECC No يظهر في الجدول بلا وصف (النص الأصلي مقطوع — "Enter the Personal details..." يظهر قبله مباشرة) — [UNCERTAIN] ECC = Excise Control Code (سياق هندي) بوصف استنتاجي.

## 10. Item Master by Vendor

**المصدر:** MGT-SET §10 ص37-39.

| الحقل | المواصفة |
|---|---|
| Vendor Code + Vendor Info (زر) | عرض موجز للمورد |
| Store Code | المخزن المجهز |
| Item Code | — |
| Vendor Type | **Normal (Open Purchase) / Contract** |
| Contract Number | **إلزامي للنوع Contract** — "will be validated with the Vendor Contract Info option where all Contract Numbers are entered Vendor wise" |
| Currency Code | F1 |
| Last Rate | **إلزامي للـ Contract**؛ **يتحدث تلقائياً عند الاستلام** للـ Normal: "If the Vendor Type is Normal the Last Rate will be updated when an Item is received from the Vendor" |
| Tax Structure | بنية الضريبة للصنف |
| Taxable Amount | "If a Tax Structure has to be calculated for an Item/s **on a specified amount**... reflected during the generation of Purchase Order and Receipts" |

## 11. Vendor Contract Info

**المصدر:** MGT-SET §11 ص39-40. الحقول: Applicable From (≥ اليوم) + Contract Number (**3 خانات فريدة**) + Vendor Code + Expiry Date + Contract Reference No.

## 12. Indent Templates (قوالب طلبات الصرف)

**المصدر:** MGT-SET §12 ص40-42.

| الحقل | المواصفة |
|---|---|
| Type | "A list of all **Cost Center defined under System Setup** modules" — الاختيار من مراكز SYS! |
| Store Type | Independent/Main/Sub |
| Template Code | فريد |
| **Copy Template** (زر) | "copy details of an existing template... make modifications or add more Items... save with a **different template code**" — نسخ-وعدّل |
| Reference/Description | — |
| Department / Property (افتراضي) / Store | — |
| Item Code | F1 — "the Item Name, Item Group and UOM of the item as specified in the Inventory Master is **automatically displayed**" |

**الاستخدام:** "Multiple indent templates are created depending on the requirements of each department... can be generated for every cost center and department" — ويُستهلك من Indent Entries (نمط Template).

## 13. Sub Cost Centre (INI #131)

**المصدر:** MGT-SET §13 ص42-43. الحقول: Cost Center (الرئيسي) + Additional Cost Center (heading) + Name + Short Name. **شرط التفعيل:** "This option will be functional **only when the switch number 131 in the INI file is set to zero**" — مفتاح INI بقيمة 0.

## 14. Variance Cost Centers (مراكز ترحيل الفروقات)

**المصدر:** MGT-SET §14 ص43-45.

| الحقل | المواصفة |
|---|---|
| Applicable Date | ≥ اليوم |
| Store | المخزن المترتبة عليه الفروقات |
| Group Code | — |
| Cost Center | "the Cost Center where the Variance Cost is experienced. **If the store selected is Independent or Sub Store, the Cost Center has to be specified**" |
| Sub Store | "**If the Store Type selected is Main Store** then the Sub Store has to be specified" |

**الوظيفة الحرجية:** "mandatory requirement for **automatic posting of negative (short) variances**. When the total number of quantity available in the store is less than the Stock Balance, you will see negative values" (ص44).

## 15. Link Cost Centers to Dept

**المصدر:** MGT-SET §15 ص45-46. الحقول: Number (فريد) + Description + Department (من Department Code في SYS) + Cost Center (**متعدد**: "Single or multiple Cost Centers can be linked"). **الأثر:** "Indents made from the Departments will be applicable to **all the Cost Centers linked** here" — توسعة نطاق الطلب القسمي.

## 16. Tax Exemptions (إعفاءات ضريبية)

**المصدر:** MGT-SET §16 ص47-48. آلية Tag (NO/YES بالنقر المزدوج/Enter): "If the tag is 'NO' the Tax amount is **included** during the transaction. If the tag is 'YES' the Tax amount is **exempted**... Refer **VAT calculation**". **السياق:** "particularly used where the tax paid by the Purchaser is **reimbursed by the state**" — نمط استرداد ضريبي حكومي.

## 17. Item Taxes

**المصدر:** MGT-SET §17 ص48-49. الحقول: Applicable date + Vendor Code (F1) + Item Code (F1) + Tax Structure (F1). **الغرض:** "define the Tax-Structure on all the items... mainly applied during **Purchase Order generation**. This takes shape for all the **imported items** for which the tax rate is different from the local taxes" — ضريبة استيراد مختلفة عن المحلية.

## 18. Define FSN (Fast/Slow/Non-Moving)

**المصدر:** MGT-SET §18 ص49-51. الحقول: Store Name (F1) + Item Code (F1) + Group Code (تلقائي/يدوي) + **Cut-Off Days** + **Fast Quantity** + **Slow Quantity** ("This number should be greater than the Slow Quantity" / "It should be less than the Fast Quantity" — قيد تقاطع!).

**الصيغة الموثقة:** "The Fast & Slow Movement of items are classified in the FSN analysis report based on **Fast / Slow Quantity divided by the Cut off Days** into the **Total Days** specified for generation of the report, in comparison with the total consumption for the given date range" (ص50).

## 19. Define Component (تكاليف التحويل)

**المصدر:** MGT-SET §19 ص51-52. الحقول: Component Code (فريد) + Long Name + Short Name. **الوظيفة:** "define the cost that is incurred during the **Item Conversion** process. When an item is converted i.e., split or add, a certain value of the original Item is lost or disoriented... During the conversion entry, the component cost is **added to the item value**".

## 20. Item Conversion Split (تحويل تجزئة)

**المصدر:** MGT-SET §20 ص52-54. الحقول: Applicable Date + Transfer Code (**3 خانات فريدة**) + Name + **From Details** (Store + Item — المصدر) + **To Details** (الأصناف الناتجة — متعددة) + **Yield %** ("This should not exceed 100%. Yield is the amount/quantity of item **(after reducing wastage)**, which can be used directly for consumption") + Conversion Factor ("as specified in the Vendor Item Details / Purchase Order / Department Requisition... for Contract / Purchase Order / Direct Items respectively").

**قيد الهيكل:** "the transferred or converted items 'From' and 'To' should be of the **same Store**" (ص53). **مثال الدليل:** "whole chicken is converted or split to make chicken spring and chicken legs" (الجزار).

## 21. Item Conversions Add (تحويل تجميع)

**المصدر:** MGT-SET §21 ص54-56. نفس بنية Split لكن الاتجاه معكوس: **From متعدد → To واحد**. **مثال الدليل:** "Gift Box placed in rooms for VIP guests, The Gift box may contain various individual items... Each of these components is identified in this option".

## 22. Budget Entry (الموازنات السنوية)

**المصدر:** MGT-SET §22 ص56-59.

| الحقل | المواصفة |
|---|---|
| Property | "in case of multi-property (If it is single Property, then the default Property)" |
| Fin. Year | F3/F1 |
| Item Group/Item Code | أساس الموازنة (مع Sub Code للصنف) |
| Value | إجمالي السنة |
| Entry Type | **Fixed** (يدوي لكل Cost Centre × شهر) أو **Apportion** (توزيع آلي) |
| Apportion Type + Apportion For + Apportion Value | "click... to assign budget values **automatically** to each cost center for each month" — ثم "You can also manually change the budget values as desired" |
| **F2 / F4** | "Press **F2 to copy** the budget of the entire year for a Cost Centre and press **F4 to paste** the values for the desired Cost Centre" — اختصارات نسخ/لصق بين مراكز |

## 23. جدول الخصائص الإصدارية والقفل

| الكيان | Applicable From | Modify-Locked | ملاحظة |
|---|---|---|---|
| Store | ✓ (فعالية) | **✓✓ كلي** (الحالة فقط → Passive + كود جديد) | الإصلاح بالإبطال |
| Item Group | ✓ | Status | — |
| Terms of Payment | ✓ | Status | — |
| Vendor Contract | ✓ | Status | — |
| Variance CC | ✓ (Applicable Date) | Status | — |
| Item Conversion ×2 | ✓ (Applicable Date) | Status | — |
| Inventory Master | — (بلا Applicable From!) | **طول الكود يُجمَّد بعد بدء التشغيل** | الكود نفسه قابل للتعديل قبل بدء الحركة |
| Opening Balance | — | **✓✓ يُجمَّد ببدء المعاملات** | — |
