# 01 — البيانات الرئيسية (Master Data) — وحدة FAS

> المصادر: FAS-MST (كامل) + FAS-SET §1-§2/§12-§14/§19-§20/§25 + FAS-TRN.

---

## 1. Chart of Accounts (الدليل المحاسبي) — FAS-MST §1

**البنية ثلاثية الطبقات:**

| الطبقة | التعريف | الحقول | المصدر |
|---|---|---|---|
| **Main Head** | رؤوس حسب جداول الميزانية/الأرباح | Main Head (3 رقمي فريد)، Account Category (**نظامي: Assets/Liabilities/Income/Expense**)، Name (30)، Short Name (10)؛ **لا يمكن تعديل الرؤوس الأولية المولدة نظامياً** | FAS-SET §1 ص4-5 |
| **Sub Head** | مجموعات تحت رأس رئيسي | Sub Head (3 رقمي فريد)، Name (30)، Short Name (10)، Main Head مرتبط (F1) | FAS-SET §2 ص5-6 |
| **Account Head** | حسابات القيد الفعلية | Account Code (**5 أو 8 حرفي**)، Group Code (=Sub Head)، Name (30، يُقترح آلياً من GL/Dept/CC)، Short Name (**إلزامي**، 20)، Cost Center + Department (**لحسابات الدخل والمصروف فقط**)، Account Type، GL Type، PDC Type، Restrict Journal، Stop Posting، Tax Applicable، Consider as Payable، Activate TDS | FAS-MST §1 ص7-9 |

**الحقول الدلالية في Account Head (نظامية محجوزة):**

| الحقل | القيم الموثقة | الأثر |
|---|---|---|
| **Account Type** | **Client A/C** (عند الترحيل يُحدد Debit أو Credit) · **Payables** (حساب سيطرة الدائنين/الموردين) · **Sub ledger** (محاسبة بأ حسابات فرعية) | FAS-MST §1 ص8 |
| **GL Type** | **CASH / BANK / OTHERS** — "All Cash and Bank Accounts have to be identified... non-Bank/Cash have to be tagged as OTHERS" | FAS-MST §1 ص8 |
| **PDC Type** | **PDC Receivable** (شيكات مؤجلة من المدينين) / **PDC Payable** (للدائنين) | FAS-MST §1 ص8 |
| **Restrict Journal** | Yes/No (افتراضي No) — منع/سماح القيد بنوع Journal | FAS-MST §1 ص8 |
| **Stop Posting** | تعطيل الترحيل للحساب كلياً | FAS-MST §1 ص8 |
| **Tax Applicable** | قابل للضريبة / معفى | FAS-MST §1 ص9 |
| **Consider as Payable** | اعتباره حساب دائن (التزام في الميزانية) | FAS-MST §1 ص9 |
| **Activate TDS** | Yes → تفاصيل Form 16 (العنوان، طبيعة الخصم، رقم حساب الخصم، PAN/GIR) | FAS-MST §1 ص9 |

> **قاعدة Account Code القابلة للتعديل عبر Chart of Accounts List:** يمكن تغيير Group/Name/Currency/Cash Flow Group/Restrict Journal/Stop Posting **أونلاين — لكن ليس إذا كانت هناك معاملات على الحساب** (FAS-LUK §7 ص23).

## 2. Vendor Master (موردون) — FAS-MST §1 (ص9-23)

> حساب مورد كامل بعشر مجموعات تفاصيل:

| المجموعة | الحقول الموثقة |
|---|---|
| **أساسي** | Vendor Code (**7 حرفي: 3 نوع شركة + 4 كود**)، Title، Name، Address، City، State، Country، Zip، Tel/Fax، Email1/2، Vendor Rating، **Black Listed (Yes → مَن وضع + السبب)**، Currency، Category (Company/Non-Company)، TDS Applicable، State (بها/خارجها/أجنبي) |
| **TDS Entry** | طبيعة الدفع (TDS Nature of Payment) + Deduction Account Number + PAN/GIR |
| **Payment Details** | Credit Days، Credit Limit، Advance %، **Stop Purchase** (Yes/No)، Payment Type (**Status أو Last Date**)، Payment Mode (Cash/Cheque/CC/Voucher)، Payment Schedule (**Adhoc/Daily/Fixed — Fixed = اختيار 9 أيام في الشهر من تقويم**)، **Stop Payment** (No يمنع الدفع) |
| **Cash Discount Detail** | **5 شرائح خصم نقدي** بحسب نطاق الأيام (مثال: خلال 5 أيام = 10%) |
| **Interest Detail** | شرائح فوائد التأخير بعد Credit Days (مثال: اليوم 11-15 = 10%) |
| **Bank Details** | BACS، Bank Sorting Code، **Transaction Limit (يومي، 11 رقمي)**، Cheque in favor of |
| **Contact Details** | **حد أقصى شخصان** (Title/Name/Designation/Mobile/Pager) |
| **Tax Details** | Tax Code (F1) + Tax Number (30) + Issue Date + Issue Place — متعدد الصفوف |
| **Other Details** | الحالة التنظيمية (Proprietor/Partner/Directors)، Nature of Business، No of Years، Turnover، ESIC Regn، PAN، Works Contract Tax، Excise، ECC، Cliental Base، Terms of Payment (F1)، Delivery/Packing، Other Costs، Contract Duration، **Short/Late Supply Penalty %**، Warranty، After Sales Service |

**قاعدة TDS الاختيارية الموثقة:** اختيار Yes/No في "TDS Applicable" يتطلب **Module Attribute رقم 9 (TDS not Mandatory) = Yes** (FAS-MST §1 ص11).

## 3. Sub Ledger — FAS-MST §1 (ص23-25)

- كود **7 حرفي فريد**، Long Name (40)، Short Name (18).
- يُربط بحساب أو **عدة حسابات** (tag Yes لكل حساب).
- إذا كان الحساب مفعّل TDS=Yes → عند وسم Sub Ledger تظهر شاشة TDS Entry تلقائياً.

## 4. Expense Allocation — FAS-MST §1 (ص25-27)

تخصيص نسب/مبالغ من حسابات للمصاريف المتكررة (هاتف/كهرباء/مياه): Allocation Code (3) + Method (**Absolute Percentage أو Fixed Amount**) + Book Type (**Payments أو Journal**) + Type (Debit/Credit) + Account (+SL) + CC/Dept + Percentage/Amount.

## 5. Statistics Master — FAS-MST §2

- كود 5 حرفي + Name (60) + Short (10) + **Group Code: Rooms (إحصاءات FO) أو Shares (إحصاءات مالية)**.
- **الحسابات المعرفة نظامياً:** Rooms Available · Rooms Sold Single · Rooms Sold Double · Rooms Sold Triple · Number of Guests · Beds Available.
- يُدخل لها قيم دورية عبر Statistics Transaction (FAS-TRN §2) وتُقارن بالميزانيات (Statistics Budget Master).

## 6. Cheque Book Master — FAS-MST §4

- تفعيله: **INI Switch # 504 `FASTRANSAUTOCHEQUENO` = 0**.
- Property + Account + Name + Book Ref + **Book Start Number** + عدد الشيكات + **Minimum Cheques (تنبيه عند بلوغ المتبقي)** + Status (Yes للاستخدام) → الشيكات تولد في grid بحالة open.

## 7. Masters إعداد مساندة — FAS-SET

| Master | الحقول | المصدر |
|---|---|---|
| **TDS Nature of Payment** §12 | Applicable Date، Code (3)، Description (30)، Form 16 Name، Tax Structure (آلي من SYS)، Applicable Form، TDS Section | ص25-26 |
| **TDS Tax Link** §13 | Tax Code (F1) + Account Code + Sub Ledger + **Round Off (none/higher/lower/nearer) + Round Off Amount** | ص26-27 |
| **TDS Defaults** §14 | PAN + TDS Number + TDS Circle + Address + Contact + **Prefix/Suffix لتسلسل الاستمارات** | ص27-28 |
| **Budget Types** §19 | Applicable From (≥ اليوم)، Code (2 رقمي)، Name (30)، Short (15) | ص40-41 |
| **Pre Defined Narration** §20 | Serial (آلي) + Narration (قابلة للتعديل) — تُستدعى بـ F1 أثناء القيد | ص41 |
| **Retained Earning Account** §25 | Financial Year (F3) + A/C Code (**إلزامي — Asset/Liability**) + Percent — **متعدد لتوزيع صافي الربح/الخسارة** | ص47-48 |

## 8. النمط الإصداري

- Applicable From موثق في: TDS Nature (§12) وBudget Types (§19) — بقية ماسترز FAS بلا Applicable From صريح (نمط يختلف عن FO).
- **التجميد بالمعاملات:** تعديل Transaction Type مقيد (راجع `02-configuration.md`)؛ تعديل Account Code ممنوع بعد وجود معاملات.
