# 14 — نموذج البيانات (Data Model) — وحدة Materials Management

> **34 كياناً** للوحدة + علاقاتها الداخلية والخارجية. التسمية: E-MG-**. الأنواع: Master (M) / Transaction (T) / Config (C) / Lookup-Like (Q).

---

## 1. كيانات الإعداد (Master/Config)

| الكود | الكيان | النوع | المفتاح | أهم الحقول | المصدر |
|---|---|---|---|---|---|
| E-MG-01 | **Store** | M | StoreCode (3 حروف-أرقام فريد) | Name·Short·**StoreType (Main/Sub/Independent)**·MainStoreCode·**RateCalc (WA/FIFO)**·ApplicableFrom·Status | SET §1 |
| E-MG-02 | **ItemGroup** | M | GroupCode (3) | Name·Short·**GroupType (FNB linkage!)**·ApplicableFrom | SET §2 |
| E-MG-03 | **ItemLocation** | M | LocationCode | Description — متحقق منه في Inventory | SET §3 |
| E-MG-04 | **StoreStart** | C | Store+Month/Year | تاريخ البدء — يفتح OB | SET §4 |
| E-MG-05 | **Item** | M | ItemCode (رقمي ≤12 **فريد عمومياً**) | Name·Group·**ItemType (Stockable/NonStock/Cash/Butchery)**·Regular·Part#·IssueUOM·ConvUOM·ExpDate?·BatchMandatory?·Consignment?·CapitalGoods? | SET §5 |
| E-MG-06 | **ItemSubCode** | M | ItemCode+SubCode | تعبئة/أسعار مختلفة — شرط UOM مختلفة | SET §5 |
| E-MG-07 | **ItemStockLevel** (صنف×مخزن) | M | Item+Store | Min/Max·**ReorderLevel·ReorderQty**·Location·IssueAllowed?·ReceiptAllowed?·ReceiptReturn? | SET §5 |
| E-MG-08 | **BarcodeLink** | M | Item (+Outlet) | Barcode — INI 245 | SET §5 |
| E-MG-09 | **OpeningBalance** | T(تأسيسي) | Store+Item(+Batch) | GrDate·Batch#·Expiry·Qty·Rate·Value | SET §6 |
| E-MG-10 | **VendorRating** | M | Code (5) | Description·Sequence | SET §7 |
| E-MG-11 | **TermsOfPayment** | M | Code (3) | LongName·GradeSequence·ApplicableFrom | SET §8 |
| E-MG-12 | **Vendor** | M | VendorCode (**7 = 3 Type(FO)+4 User**) | 26 حقلاً رئيسياً + 7 عائلات فرعية | SET §9 |
| E-MG-13 | VendorTDSEntry | M | Vendor | TDSNatureOfPayment (متعدد)·DeductionAccountNumber·PAN/GIR | SET §9 |
| E-MG-14 | VendorPaymentDetails | M | Vendor | CreditDays·CreditLimit·Advance%·StopPurchase·PaymentType·PaymentMode·Frequency(**FixedDays≤9!**)·StopPayment·5 DiscountSlabs·InterestSlabs | SET §9 |
| E-MG-15 | VendorBankDetails | M | Vendor | BACS·SortingCode·TransactionLimit(≤11)·ChequeFavorOf | SET §9 |
| E-MG-16 | VendorContact (≤2) | M | Vendor+Seq | Title·Name·Designation·Mobile·Pager | SET §9 |
| E-MG-17 | VendorTaxDetail | M | Vendor+TaxCode | TaxNumber(≤30)·IssueDate·IssuePlace | SET §9 |
| E-MG-18 | VendorOtherDetails | M | Vendor | 20 حقلاً تنظيمياً/تجارياً + Penalty%·Warranty | SET §9 |
| E-MG-19 | **VendorItem** (Item Master by Vendor) | M | Vendor+Store+Item | **VendorType (Normal/Contract)**·ContractNumber·Currency·LastRate (آلي للـ Normal)·TaxStructure·TaxableAmount | SET §10 |
| E-MG-20 | **VendorContract** | M | ContractNumber (3) | VendorCode·ExpiryDate·Ref·ApplicableFrom | SET §11 |
| E-MG-21 | **IndentTemplate** | M | TemplateCode | Type(CC)·StoreType·Dept·Store·Items[] + CopyTemplate | SET §12 |
| E-MG-22 | SubCostCentre | M | CC+Name | AdditionalCC — INI 131 | SET §13 |
| E-MG-23 | **VarianceCostCenter** | C | Store(+Sub/CC) | GroupCode·CC — **هدف ترحيل العجز** | SET §14 |
| E-MG-24 | DeptCostCenterLink | C | Number | Dept→CCs[] | SET §15 |
| E-MG-25 | TaxExemption | C | (TaxCode) | Tag Yes/No | SET §16 |
| E-MG-26 | ItemTax | C | Vendor+Item+TaxStructure | ApplicableDate — ضريبة استيراد | SET §17 |
| E-MG-27 | **FSNRule** | C | Store+Item | CutOffDays·FastQty·SlowQty | SET §18 |
| E-MG-28 | Component | M | ComponentCode | أسماء — تكلفة التحويل | SET §19 |
| E-MG-29 | **ConversionSplit** | M | TransferCode (3) | From(Item)→To(Items)·**Yield≤100**·ConvFactor | SET §20 |
| E-MG-30 | **ConversionAdd** | M | TransferCode (3) | From(Items)→To(Item) | SET §21 |
| E-MG-31 | **Budget** | C | Property+FinYear+Group/Item | Value·EntryType(Fixed/Apportion)·CC×Month grid | SET §22 |
| E-MG-32 | FootNote | C | Type+Note# | Designation — 3 مستويات | SET §23 |
| E-MG-33 | MGTAccessRights | C | User×{Store/Option/CC/BackdateType} | 4 أبعاد | SET §24 |
| E-MG-34 | EmailAccess+Template | C | User/Group·Module+ProgramType | CC/BCC·DefaultTemplate | SET §25 |

## 2. كيانات المعاملات (Transactions)

| الكود | الكيان | المفتاح/الترقيم | الحالات | المصدر |
|---|---|---|---|---|
| E-MG-35 | **PurchaseRequisition** | Request# (آلي) | Pending/Closed(+Received) | DNT §1 |
| E-MG-36 | PRItem | PR+Item | Qty·CurrentStock·Packing·Weight·RequiredDate·Brand·Remarks | DNT §1 |
| E-MG-37 | **PRAuthorization** | PR+Level(1-3) | Authorizer·تاريخ — INI 355 | DNT §1 |
| E-MG-38 | **Indent** | Indent# (آلي) | Pending/Closed/Deleted · نمط (Adhoc/Template/Repeat) | DNT §2 |
| E-MG-39 | IndentItem | Indent+Item+**CC** | Qty per CC (أعمدة!)·Rate | DNT §2 |
| E-MG-40 | **Quotation** | Quotation# (آلي) | مفتوح/Closed(+Reason) | DNT §7 |
| E-MG-41 | QuotationItem | Quotation+Item | ItemSpec·Suppliers[] | DNT §7 |
| E-MG-42 | **PurchaseOrder** | PO# (آلي) | Pending/Closed/Cancelled | DNT §3 |
| E-MG-43 | POItem | PO+Item | Qty·Rate·DeliveryDate·Place·PaymentTerm | DNT §3 |
| E-MG-44 | POtherDetails | PO | ComStatement·Project·Location·PriceBasis·DeliveryPeriod·Guarantee·Inspection·PenaltyDelay·Conditions | DNT §3 |
| E-MG-45 | POMiscTax | PO | Tax·Currency·Type·Factor | DNT §3 |
| E-MG-46 | **StandingPO** | SPO# (آلي) | صلاحية نطاق تاريخ · ItemRate **Fixed/MRP** | DNT §4 |
| E-MG-47 | **ServiceWorkOrder** | SWO# (آلي) | Closed/Cancelled/Processed | DNT §5 |
| E-MG-48 | **Receipt** | GR# (+GRR للمرتجع) | نوع (Contract/PO/Direct)·DS#·**Bill#/BillDate**·ExcRate | DNT §6 |
| E-MG-49 | ReceiptItem | GR+Item(+Batch) | Complimentary?·ConvFactor·POUOM·Batch·Expiry·Weight·Qty·Currency/Tax/Rate/Value·CC·SubStore | DNT §6 |
| E-MG-50 | ReceiptMiscTax | GR | Tax·Currency·Type·Factor·OtherCurVal·LocalVal | DNT §6 |
| E-MG-51 | ReceiptOtherDetails | GR | GateReceipt#·GateEntry#·Location·RejectedReport#·ModeOfTransport·**Images[]** | DNT §6 |
| E-MG-52 | **Issue** | Doc# (آلي) | Direct/Indent | DNT §6 |
| E-MG-53 | IssueItem | Issue+Item+**Batch** | Qty (توزيع تصاعدي)·Rate·Value·CC · **DPRQty عند الصفر** | DNT §6 |
| E-MG-54 | **ReceiptReturn** | Ref# (3 حرفي) | GRR-driven | DNT §6 |
| E-MG-55 | **IssueReturn** | — (Store+Indent 3-10) | GRR/Batch-driven | DNT §6 |
| E-MG-56 | **Adjustment** | Adjustment# (≥3) | ± Qty/Value·IncludeZero·AdjustmentType (سالب) | DNT §6 |
| E-MG-57 | **ConversionTxn** (Split/Add) | Ref# (≤10) | TransferCode·Yield·ComponentCost | DNT §6 |
| E-MG-58 | **ReOrderProcess** | Process# (آلي) | Processed→Posted | DNT §8 |
| E-MG-59 | InterStoreRequisition | — | +StockLocator/SaleHistory أدوات | DNT §9 |
| E-MG-60 | **InterStoreTransfer / SubStoreTransfer** | — | From/To·Month/Year (Inter)·TransferQty | DNT §§10-11 |
| E-MG-61 | CostCenterTransaction | — | CC Start Date·Physical Stock CC·Source→Target | DNT §12 |
| E-MG-62 | **PhysicalStockEntry** | — | مساران (Independent/Main-Sub Group)·Variance | DNT §13 |
| E-MG-63 | **StockVariance** | — | Adjustment Transactions الناتجة | DNT §14 |
| E-MG-64 | **StoreLedger** | Store+Month | المعالج — تجميد | DNT §15 |

## 3. العلاقات الجوهرية (Relations)

```
Store 1──1 RateCalc (WA|FIFO)                    [التقييم خاصية مخزن]
Store 1──* ItemStockLevel *──1 Item               [الأعلام الاتجاهية]
Store 1──* SubStore (Self-Ref: MainStoreCode)     [الهرمية]
Item *──1 ItemGroup ──GroupType──► FNB
Item 1──* SubCode (شرط UOM)
Item *──* Vendor (عبر VendorItem: Normal/Contract + LastRate)
Vendor *──1 CompanyType (FO!)
Vendor 1──* {TDS·Payment(+5 slabs)·Bank·Contact(≤2)·Tax·Other}
Contract 1──* VendorItem (Contract#)
IndentTemplate ──► CC (SYS) + Dept + Items[]
PR ──(Auth 1→2→3)──► PO ──(GR Date ≥ PO Date)──► Receipt ──Bill#──► FAS PaymentMatch
SPO ──(GR ≤ Contract Expiry)──► Receipt (نوع Contract)
Indent ──► Issue ──(Nil balance)──► DPR ──► Receipt (Direct)
Receipt(GRR) ──► ReceiptReturn
Issue ──► IssueReturn (GRR/Batch matching)
PhysicalStock ──► StockVariance ──(سالب)──► VarianceCC ──► FAS
Store+Month ──► StoreLedger (freeze/cancel)
```

## 4. كيانات مشتركة عبر الوحدات (تُحسم ملكيتها في Phase 9)

| الكيان | مالك موثق | مستهلكون |
|---|---|---|
| Company Type | FO (نص MGT) | MGT (Vendor) + AR (Company Profile TTT+XXXX نفس البنية!) |
| Cost Center | SYS | MGT (كل شيء) + FAS + FNB |
| Reason Code | SYS (فلاتر 9 وحدات تشمل Purchase) | MGT DPR + POS + FAS |
| Tax Code/Slab/Structure | SYS | MGT + FO + POS + BNQ |
| UOM | SYS | MGT + POS + FNB |

## 5. تقديرات الحجم والنمذجة

- **34 + 30 = 64 كياناً موثقاً** (الضخم: Vendor بـ 7 عائلات؛ Receipt بـ 4 كيانات تابعة).
- **نمط الانفجار الشرائي:** GR واحد = Receipt + Items(±Batch) + MiscTax + OtherDetails + Images — **5 كيانات** لحدث واحد.
- **الترقيم الآلي الكامل** (10 مسارات مرقمة) — ن Naming Series متعددة في Frappe.
- الحقول الصريحة الطول/الصيغة: **21 حقلاً** (راجع 06-validations) — تُنقل كقيود Char/Length في DocTypes.
