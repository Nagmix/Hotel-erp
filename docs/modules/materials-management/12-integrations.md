# 12 — التكاملات (Integrations) — وحدة Materials Management

> I-MG-01..15 تكاملات موثقة نصاً. MGT **أعقد وحدة تكاملياً بعد FO**: تستهلك مرجعيات SYS/FO وتغذي FAS/FNB/POS — محور دورة التكلفة.

---

## 1. مصفوفة التكامل

| # | التكامل | الاتجاه | النص الموثق | المصدر |
|---|---|---|---|---|
| I-MG-01 | **Cost Centers (SYS → MGT)** | استهلاك | "A list of all Cost Center defined **under System Setup modules** are listed" (Indent Templates) + Link CC to Dept + Variance CC | SET §12 ص41 + §14/§15 |
| I-MG-02 | **Reason Codes (SYS → MGT)** | استهلاك | "Reasons are displayed from the **Reasons Definition option under System Setup module**" (DPR في Issue Indent) | DNT §6 ص40 |
| I-MG-03 | **Company Types (FO → MGT)** | استهلاك جذري | "the Vendor type... defined in the **Company Types option under the Front Desk module**" — بنية كود المورد كلها | SET §9 ص22 |
| I-MG-04 | **محرك الضرائب (SYS → MGT)** | استهلاك | Tax Structure في PO/SPO/Item Taxes/Item Master by Vendor/Misc Tax — كل من SYS الثلاثي (Code/Slab/Structure) | SET §§10/17 + DNT §3/§6 |
| I-MG-05 | **UOM (SYS → MGT)** | استهلاك | Issue UOM "Standard Accounting UOM" + Conv UOM — من قائمة SYS | SET §5 |
| I-MG-06 | **Currencies/Exchange (SYS → MGT)** | استهلاك | Vendor Currency + PO Currency + Receipt Exc.Rate + "Other Cur.Val/Local Value" | SET §9 + DNT §6 |
| I-MG-07 | **Module Attributes/INI (SYS → MGT)** | تحكم سلوكي | INV #3/#5/#6/#7/#8/#13/#14/#298 + INI #39/#131/#245/#355 — **12 مفتاحاً** | SET/DNT مواضع متعددة |
| I-MG-08 | **MGT → FAS (Purchase Journal/GL)** | ترحيل | "tax values... reflected separately during posting and generation of **Purchase Journal to the General Ledger**" + الرابط 3 من الستة في FAS-SET | SET §16 ص47 + FAS-SET |
| I-MG-09 | **MGT → FAS (Payment Match)** | جسر تسديد | "Bill # and Bill date... will be used in the **Payment Match** option while making Payment" | DNT §6 ص32 |
| I-MG-10 | **MGT → FAS (Variance CC)** | ترحيل آلي | "automatic posting of **negative (short) variances**" | SET §14 ص44 |
| I-MG-11 | **MGT → FNB (Item Group Type)** | تصنيف استهلاكي | "Group Type... important for **F&B costing module** to help pick up the appropriate consumption figures in relevant cost type reports" | SET §2 ص7 |
| I-MG-12 | **MGT → FNB (Conv UOM بالأجزاء)** | قياس استهلاك | "where the Sale / Stock and Consumption at the Outlets/Kitchens are **in portions**. This will be reflected in Food and Beverage Costing" | SET §5 ص10 |
| I-MG-13 | **MGT → POS (Shop Outlet/Barcode)** | جسر بيع تجزئة | "If selected Main/Ind Store is **Shop Outlet**... **Outlet Code and Store code should be same**; item tagged to only one shop outlet" + Barcode (INI #245 BEV/FB/LQ) يحمّل الصنف في Receipt | SET §5 ص14-15 |
| I-MG-14 | **Auto-Indent الداخلي (DPR)** | أتمتة داخلية | "If the item has 'Nil' balance... DPR Qty... **will be reflected during the Receipt entry**" | DNT §6 ص40 |
| I-MG-15 | **Departments (SYS → MGT)** | توجيه | "Indents made from the Departments will be applicable to **all the Cost Centers linked** here" + PR Department | SET §15 ص46 |

## 2. سلاسل التكامل المكتملة (Cross-Module Workflows)

### 2.1 سلسلة التكلفة المكتملة (أهم إنجاز توثيقي للجلسة 6)

```
SYS (CC/UOM/Tax) ──► MGT (استلام بالتقييم WA/FIFO)
                          │ إصدار Issue ──► Cost Centers (SYS) ──► FNB Costing (استهلاك×Group Type)
                          │ Adjustment/Variance ──► Variance CC ──► FAS (PJV آلي)
                          └─ Receipt (Bill#) ──► FAS Payment Match ──► تسديد
```

**دلالة:** حلقة "المشتريات → المخزون → الاستهلاك → FAS" الموصوفة في module-inventory §5 (الهدف المعلن للجلسة) **موثقة الآن من طرفيها**.

### 2.2 سلسلة اختيار المورد

```
Vendor Master (بنية FO Company Types!) ──► Item Master by Vendor (Last Rate آلي)
       │                                              │
       ▼                                              ▼
Vendor Rating + Terms (Grade Sequence) ──► Quotation Cycle ──► Comparison ──► PO/SPO
       └── LUK Vendor Selection (آخر استلام/سعر) + Spending Pattern (سنة/سنة)
```

### 2.3 سلسلة الطلب الآلي المزدوجة

```
مسار أ: Re-order Level ──► Re-Order Process (رقم) ──► Update & Generate ──► PR للقسم
مسار ب: Indent بلا رصيد ──► DPR Qty ──► Receipt entry ──► استلام مباشر
كلاهما ينتهي: PO أو Direct Purchase (قرار بشري موثق)
```

## 3. حدود التكامل [NOT DOCUMENTED]

| السؤال | الحالة |
|---|---|
| هل ترحيل MGT→FAS فوري أم دفعة شهرية (مع Ledger)؟ | [NOT DOCUMENTED] — يُحسم في Phase 6 (أنماط الوحدات الأخرى تسمح بالاحتمالين) |
| هل Item Master يُشارك مع FNB Recipes مباشرة (نفس الجدول)؟ | مستنتج قوياً (Conv UOM "reflected in F&B Costing") لكن الوثيقة FNB لم تُقرأ بعد |
| Shop Outlet → هل المبيعات تخفض مخزون MGT مباشرة أم عبر FNB؟ | [UNCERTAIN] — POS وثّق Guest Settlement/فوترة؛ ربط المخزون المنفذ بالمخزن غير موثق في POS-* أو Touch Screen |
| Gate Passes (وحدة مستقلة في الحزمة) ↔ Gate Entry # في Receipt Other Details؟ | [UNCERTAIN] — التسمية المتطابقة قوية؛ وثيقة Gate Passes لم تُقرأ بعد (مرشح تحقق بالجلسة القادمة) |
| Care (مهام) ↔ صلاحيات المخزن؟ | لا إشارة في MGT |

## 4. أثر التكاملات على القاموس الموحد

مصطلحات جديدة تُضاف من MGT إلى domain/terminology.md (المرحلة 1): **GR#/GRR# · Indent · DPR · SPO · SWO · FEFO (كمفهوم FIFO الأصلي) · Yield% · FSN · Variance CC · Complimentary Receipt · Stop Purchase/Payment · Item Master by Vendor · Stores Ledger · Applicable From (تأكيد نمط) · Re-order Level/Quantity · FEFO Batch Help** — 16+ مصطلحاً.
