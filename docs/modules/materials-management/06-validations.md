# 06 — قواعد التحقق (Validations) — وحدة Materials Management

> V-MG-01..30 تحققات موثقة نصاً (الحقل + القاعدة + لحظة التطبيق). مرتبة بحسب دورة الحياة.

---

## 1. تحققات الإعداد والمرجعيات

| # | التحقق | النص/الشرط | المصدر |
|---|---|---|---|
| V-MG-01 | Applicable From المستقبلي | "Enter the current date or **a date greater than the current**" — في Store/ItemGroup/Terms/Contract/VarianceCC/ItemTaxes/Conversion | SET §§1/2/8/11/14/17/20/21 |
| V-MG-02 | فرادة Store Code | "unique 3-digit alphanumeric code assigned for **every** Store" | SET §1 |
| V-MG-03 | Main Store Code إلزامي للـ Sub | "If the Store Type defined is a **Sub Store**, then it is **necessary** to define its Main Store" | SET §1 ص5 |
| V-MG-04 | Rate Calculation إلزامي | "has to be specified for the defined Store" — اختيار من {WA, FIFO} | SET §1 |
| V-MG-05 | حظر تعديل/حذف Store | "Once the Store Code is created and saved, **updation or deletion... is not allowed**" | SET §1 ص5 Note |
| V-MG-06 | Stores Start Date ≤ الحالي | "Month and year entered should be **less than or equal to** the current month and year" | SET §4 ص9 |
| V-MG-07 | Item Group إلزامي للصنف | "Every Item... **has to be tagged** with a Group Code" | SET §2 ص6 |
| V-MG-08 | Item Code رقمي فقط | "This field supports only **numeric** characters" | SET §5 ص11 |
| V-MG-09 | طول Item Code | "≤12 characters as defined in an INI file (#39)... **cannot be altered** after start of Operation" | SET §5 ص10 |
| V-MG-10 | فرادة Item Code عمومياً | "entry of similar Item Codes for **different stores is not possible**" | SET §5 ص10 |
| V-MG-11 | Sub Code شرطه UOM | "Entry of Sub Codes is possible **only if the Issue UOM and Conversion UOM are different**" | SET §5 ص10 |
| V-MG-12 | Item Location متحقق | "the item location **is validated** with the details captured in this parameter" | SET §3 ص8 |
| V-MG-13 | Vendor Code بنية 7 | "Vendor code should be of 7 characters in length. The first 3 characters should be of company type followed by the vendor code" | SET §9 ص23 |
| V-MG-14 | سقف 2 للـ Contact | "You can save the contact details of **maximum two people**" | SET §9 ص31-32 |
| V-MG-15 | Tax Number ≤30 | "alphanumeric values and special characters of length **up to 30**" | SET §9 ص33 |
| V-MG-16 | Transaction Limit ≤11 رقمي | "This field supports maximum **11 numeric** values" | SET §9 ص31 |
| V-MG-17 | Contract# إلزام للـ Contract Vendor | "receipt of Contract Items are based on the rate entered in this option... validated against the Vendor Contract Info" | SET §10 ص37 |
| V-MG-18 | FSN تقاطع الكميات | Fast Quantity "should be **greater than** the Slow Quantity" | SET §18 ص51 |
| V-MG-19 | Yield ≤100% | "This should **not exceed 100%**" | SET §20 ص54 |
| V-MG-20 | تحويل داخل مخزن واحد | "the transferred or converted items 'From' and 'To' should be of the **same Store**" | SET §20 ص53 |

## 2. تحققات المعاملات اليومية

| # | التحقق | النص/الشرط | المصدر |
|---|---|---|---|
| V-MG-21 | GR Date مقابل نوع الاستلام | Contract: ≤ انتهاء العقد · PO: ≥ تاريخ PO · Direct: ≥ تاريخ الطلب | DNT §6 ص32 |
| V-MG-22 | Bill#/Date إلزام مشروط | "mandatory only if Serial # 3... is set to YES in module Attributes" | DNT §6 ص32 |
| V-MG-23 | Batch# عند تكرار الصنف | "entry **mandatory** when same item code is selected more than one time" | DNT §6 ص34 |
| V-MG-24 | Expiry ≥ النظام | "Date entered should be **equal to or greater than the system date**" | DNT §6 ص34 |
| V-MG-25 | Misc Tax — قاعدة العملة | نفس عملة الشاشة → Pct/Amount؛ عملة أخرى → **Amount فقط** | DNT §6 ص35 |
| V-MG-26 | Issue Date ≥ النظام | "Date entered should be **equal to or greater than the current system date**" (Issue Indent) | DNT §6 ص39 |
| V-MG-27 | Issue Return Indent# صيغة | "alphanumeric values, a **minimum of three** characters and **maximum of 10**" | DNT §6 ص42-43 |
| V-MG-28 | Adjustment# صيغة | "It accepts a **minimum of 3 alphanumeric** characters" | DNT §6 ص44 |
| V-MG-29 | Reference# (تحويل) | "Maximum of **10 alphanumeric** characters" | DNT §6 ص46/47 |
| V-MG-30 | To Qty = From Qty (Conversion) | "The quantity specified in the To Items Details should be **equal to** the quantity specified in From Items Details" | DNT §6 ص46 Note |

## 3. تحققات الحوكمة والدورية

| # | التحقق | النص/الشرط | المصدر |
|---|---|---|---|
| V-MG-31 | PR Issue محجوب بلا تفويض | "If authorizations are not made, **requisition issues are not allowed**" | DNT §1 ص5 |
| V-MG-32 | تفويض تسلسلي | "Level one... is **mandatory before** receiving the Level 2 authorization" | DNT §1 ص7 |
| V-MG-33 | Direct Receipt مشروط | INV #5 "In Receipt / PO Indent is not mandatory" = Yes | DNT §6 ص31 |
| V-MG-34 | SPO مشروط | "To activate SPO, Switch #8... set" (Serial 5 = Yes) | DNT §4 ص21 |
| V-MG-35 | Physical Stock < الخادم | "Month and Year must be **less than the server month and year**" | DNT §13 ص70 |
| V-MG-36 | حظر تحديث الشهور المعالجة | "update of transactions will **not be allowed** for the processed months **except for the current month**" | DNT §15 ص73 |
| V-MG-37 | حظر Opening Balance بعد المعاملات | "Once the Transactions have commenced... you will **not be allowed** to update the Opening Balance" | SET §6 ص18 |
| V-MG-38 | نافذة التأريخ الرجعي | "access to different types of Transaction **for a specified number of days**" — لكل مستخدم | SET §24 ص64-65 |
| V-MG-39 | Sub Cost Centre مشروط | INI #131 = 0 | SET §13 ص42 |
| V-MG-40 | Barcode مشروط | INI #245 ∈ {BEV, FB, LQ} | SET §5 ص14 |
| V-MG-41 | Shop Outlet 1:1 | "Outlet Code and Store code should be **same**; and the item can be tagged to **only one** shop outlet" | SET §5 ص15 |
| V-MG-42 | Adjustment Type للسالب فقط | "will remain **unknown** by default if any positive adjustments done" | DNT §6 ص45 |

## 4. مصفوفة التحقق ضد أنواع الأصناف

| الموقف | Stockable | Non-Stockable | Cash Purchase | Butchery |
|---|---|---|---|---|
| رصيد مخزني + Opening Balance | ✓ | ✗ ("stockable Items for a given store") | ✗ | ✓ (سلوك Stockable) |
| Cost Center في الاستلام | ✗ | ✓ | ✓ | ✗ |
| Sub Store في الاستلام | ✓ (إذا Main) | ✗ (معطل) | — | ✓ |
| Receipt Return | ✓ ("return **Stockable** type of items") | ✗ | ✗ | ✓ |
| Adjustment | ✓ (مع GRR) | — | — | ✓ |
| تحويل/تقطيع | — | — | — | ✓ (الحالة النموذجية) |

> **ملاحظة تنفيذية:** هذه المصفوفة تُشتق من نصوص متفرقة (SET §5/6 + DNT §6) — الخلايا الفارغة [NOT DOCUMENTED] صراحة وتُستكمل من FNB لاحقاً.
