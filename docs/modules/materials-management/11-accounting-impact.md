# 11 — الأثر المحاسبي (Accounting Impact) — وحدة Materials Management

> الأحداث المالية الموثقة + الرابط MM→Finance (أحد الروابط الست الموثقة في FAS-SET) + تدفق القيم الضريبية. **ملاحظة منهجية:** الدليل الوظيفي MGT يوثق المشغلات؛ **بنود القيود التفصيلية** موثقة في FAS (Purchase Journal/Book Types) — الإحالات المتبادلة تُربط هنا.

---

## 1. رابط الترحيل المؤسسي (MM → Finance)

**من FAS-SET (مصدر الرابط — راجع financial-accounting/11-accounting-impact.md):** Materials Management من الوحدات الست التي ترحل إلى Finance.

**من MGT (مصدر المشغل):**

| المشغل | النص الموثق | المصدر |
|---|---|---|
| **Tax Exemptions → PJV/GL** | "The tax values will be **reflected separately during posting and generation of Purchase Journal to the General Ledger**" — قيم الإعفاء تظهر **منفصلة** في القيد | SET §16 ص47 |
| **Variance CC (السالب) → ترحيل آلي** | "mandatory requirement for **automatic posting of negative (short) variances**" — عجز الجرد يرحل تلقائياً للمركز المعرف | SET §14 ص44 |
| **Exchange Rate → القيم المحلية** | "If the Currency entered is different from the default currency then the **Exchange Rate is reflected**... Other Cur. Val and Local Value are displayed by default" — عملتان بالقيد (أخرى + محلية) | DNT §6 ص34/35 |

## 2. جدول الأحداث المالية (E-MG-01..14)

| # | الحدث المالي | الطبيعة | الاتجاه/الحساب الموثق | المصدر |
|---|---|---|---|---|
| E-MG-01 | استلام صنف (GR) | قيمة مخزون + التزام موردي | Inventory Dr / Vendor Cr [INFERENCE من Purchase Journal — البنود في FAS-TRN] | DNT §6 |
| E-MG-02 | استلام **Non-Stockable/Cash** | مصروف مباشر | "directly issued to the Cost Center" — القيمة للمركز (لا للمخزن) | SET §5 ص11 |
| E-MG-03 | استلام Complimentary | **بلا قيمة ضريبية** | "the Rate Plan and Tax Structure will not be applicable" | DNT §6 ص33 |
| E-MG-04 | ضريبة شراء (صنف) | التزام ضريبي | "mainly applied during Purchase Order generation... imported items" — Item Taxes | SET §17 ص48 |
| E-MG-05 | **Misc Tax Deduction** (استلام) | ضريبة على مستوى الاستلام | "make the Miscellaneous Tax entry for **the entire receipt**" + قاعدة العملة | DNT §6 ص34-35 |
| E-MG-06 | إعفاء ضريبي | إثبات استرداد | "reflected **separately** during posting" — بند منفصل | SET §16 ص47 |
| E-MG-07 | إصدار (Issue) | تحويل تكلفة | Store → Cost Center (قيمة بتقييم المخزن) | DNT §6 |
| E-MG-08 | Receipt Return | عكس التزام/مخزون | عكس جزئي/كلي على GRR | DNT §6 |
| E-MG-09 | Issue Return | تخفيض مصروف | CC → Store | DNT §6 |
| E-MG-10 | Adjustment (±) | تسوية قيمة | **السالب → Variance CC آلياً** | SET §14 + DNT §6 |
| E-MG-11 | Conversion (Split/Add) | إعادة تقييم داخلي | "component cost is **added to the item value**" + ضياع Yield | SET §19/20 |
| E-MG-12 | **Stock Variance Updation** | تسوية جرد آلية | "excess or short variance... **Adjustment Transactions**" (فائض وعجز) | DNT §14 |
| E-MG-13 | Consolidate Discount (PO) | خصم كمي | "select the percentage option and enter the percentage of amount that can be given as discount" | DNT §3 ص17 |
| E-MG-14 | Bill# → Payment Match | **جسر التسديد** | "will be used in the **Payment Match option while making Payment**" — مطابقة الفواتير في FAS | DNT §6 ص32 |

## 3. التقييم كأساس محاسبي (Valuation → Posting)

1. **WA:** "Weighted Average = (Closing Balance Value / Closing Quantity)" — **سعر الإصدار يعاد حسابه مع كل حركة** (مثال الكاجو الرقمي: صيغة القيمة الدورية موثقة) — القيود تتبع السعر الجاري.
2. **FIFO/FEFO:** "The rate / valuation of Items will get reflected depending on the selection of either the **Opening Balance Quantity or Date wise receipt**" — كل إصدار **يستهلك دفعات محددة بتواريخها وأسعارها** (Batch Help يوزع الفعلي).
3. **أثر منطقي [INFERENCE]:** قيمة قيود الإصدار تختلف بين المخازن (WA vs FIFO) **لنفس الصنف** — التقييم **خاصية مخزن لا صنف** (قرار نمذجة حرج — F-MG-1).

## 4. حلقة الموردين المالية (Vendor Financial Loop)

```
Vendor Master (Credit Days/Limit/Advance%/خصم 5 شرائح/فائدة)
        │
        ▼
PO/SPO (Payment Term محقق من Terms of Payment) ── Misc Tax
        │
        ▼
Receipt (Bill#/Bill Date إلزام عند INV #3 + Currency/Exc.Rate)
        │
        ▼
[FAS] Payment Match بالفاتورة ──► تسديد (Cash/Cheque/CC/Voucher)
        │
        ├── خصم نقدي (ضمن أيام الشرائح: "within the first 5 days... 10%")
        └── فائدة تأخير ("91st to 100th day... 10% interest") [موثقة في Master
            كسلوك اتفاقي — آلية الحساب المالية في FAS: NOT DOCUMENTED هنا]
```

**عناصر الحلقة المالية الموثقة في MGT فقط:** Credit Days · Credit Limit · Advance % · Stop Payment · 9 أيام دفع ثابتة · 5 شرائح خصم · شرائح فائدة · TDS Applicable (مع Deduction Account Number + PAN/GIR) · Currency.

## 5. مواضع [NOT DOCUMENTED] المحاسبية (تُحسم من FAS/FNB)

| البند | الحالة |
|---|---|
| بنود القيود Debit/Credit للاستلام/الإصدار | في FAS-TRN (Book Types) — مرجع متبادل |
| توقيت الترحيل (فوري/دفعة/شهري) | [NOT DOCUMENTED في MGT] — نمط FO/POS دفعات مقابل AR فوري يترك الاحتمالين؛ **يُحسم في Phase 6** |
| قيد Conversion بدقة (ضياع Yield كخسارة؟) | [UNCERTAIN] — "certain value of the original Item is lost or disoriented" يوثق المفهوم لا القيد |
| آلية فوائد التأخير الحسابية | موثقة كمفهوم في Vendor Master؛ الحساب [NOT DOCUMENTED] |
| ترحيل Cash Purchase | "purchased from the open market for cash and directly issued" — قيد نقدي مباشر [INFERENCE] |
