# 10 — المعاملات ودورات الحياة (Transactions) — وحدة Materials Management

> دورات حياة كل مستندات الوحدة + الأحداث المؤتمتة الموثقة + الأرقام التسلسلية المولدة.

---

## 1. دورة الحياة الكبرى (سلسلة التوريد)

```
[Auto: Re-Order / DPR]      [يدوي]
        │                      │
        ▼                      ▼
   Purchase Requisition ──(تفويض 1→2→3 عند INI 355)──► Closed
        │
        ▼ (اختياري)
   Quotation Cycle (Invite → Tender → Update → Analysis → Comparison → Close)
        │
        ▼
   PO ──(تفويض عند INV 13/14/298)──► Closed        SPO (دائم: نطاق صلاحية) ──► Closed
   SWO (خدمات) ──► Processed/Cancelled/Closed
        │
        ▼
   Receipt (Contract/PO/Direct) ── Bill# ──► [FAS: Payment Match]
        │
        ▼ (إصدار)
   Issue (Direct / Indent) ──► Cost Centers ──► [FNB: الاستهلاك]
        │                                   └─► [POS: Shop Outlet]
        ├──► Receipt Return (إلى المورد)
        ├──► Issue Return (من المركز للمخزن)
        ├──► Adjustment (± Qty/Value)
        ├──► Conversion Split/Add (Butchery/تصنيع)
        ├──► Inter Store / Sub Store / CC Transfer
        ▼ [شهري]
   Physical Stock ──► Stock Variance Updation ──► Process Store Ledger (تجميد)
```

## 2. جدول دورات الحياة التفصيلي

| المستند | الإنشاء | الأرقام | الحالات الموثقة | الإغلاق/الإلغاء |
|---|---|---|---|---|
| **Purchase Requisition** | يدوي أو **آلي** (Re-Order/DPR) | Request # (تلقائي) | Pending/Closed/All + Received | Close (Manual نطاق/Automatic تاريخ) — Delete column = Yes |
| **Indent** | يدوي Adhoc/Template/Repeat Request | **Indent# بعد الحفظ** | Pending/Closed/**Deleted**/All | Close Indent (اختيار أصناف) |
| **Quotation** | Invite Quotation → **رقم** | Quotation # | مفتوح → Closed | Close Quotation + **Reason** |
| **PO** | يدوي (زر Requisitions يدمج PR!) | **PO # عند التوليد** | Pending/Closed/Cancelled + **Blank** | إغلاق/إلغاء موثقان في LUK 5/7 |
| **SPO** | يدوي (SPO# تلقائي) | SPO# | مفتوح/Closed (بصلاحية نطاق تاريخ) | Close SPO |
| **SWO** | يدوي → **رقم SWO** | SWO# | **Closed/Cancelled/Processed/All** | Cancel (+Reason+تأكيد) أو Close (+Reason) |
| **Receipt** | Contract/PO/Direct — GR# | GR# (+GRR للمرتجع) | محقق ضد النوع | Receipt Return (كلي/جزئي) |
| **Issue** | Direct/Indent — Doc# تلقائي | Doc Number | فوري (ضد رصيد) | Issue Return |
| **Adjustment** | يدوي | Adjustment# (≥3 حروف) | فوري ± | — |
| **Conversion** | من Master محدد | Transfer Code (Master) + Ref# | فوري | — |
| **Re-Order** | آلي عند ≤ Reorder Level | **Process Number** | Processed → Posted | — |
| **Store Ledger** | شهري | — | المعالج (مجمد) | **Cancel Stores Ledger** لفك التجميد |

## 3. الأحداث المؤتمتة الموثقة (Automation Events)

| # | الحدث | المحفّز | الأثر | المصدر |
|---|---|---|---|---|
| A-MG-01 | توليد PR من Re-order | "Stock Balance equal to or below the Re-Order level" | إدراج في Re-Order Process برقم معالجة → Update → **نشر requisition إلى القسم** | DNT §8 ص57-59 |
| A-MG-02 | **DPR من نقص الإصدار** | رصيد الصنف **Nil** أثناء Issue (Indent) | "The DPR recorded here will be **reflected during the Receipt entry**" | DNT §6 ص40 |
| A-MG-03 | تحديث Last Rate للمورد Normal | "when an Item is received from the Vendor" | تحديث Vendor Item Master + "Details" | SET §10 ص37 |
| A-MG-04 | تحميل تفاصيل الصنف بالباركود | مسح الباركود في Receipt | "Item Details will be loaded in Transactions-Receipt entry" | SET §5 Barcode ص17 |
| A-MG-05 | توزيع الإصدار Batch-wise تصاعدي | إدخال كمية الإصدار | توزيع آلي على الدفعات (Batch Help للتعديل) | DNT §6 ص38 |
| A-MG-06 | حساب Value تلقائي | Qty × Rate | في كل شاشة (OB/Receipt/Issue/Transfer) | SET §6 + DNT §6 |
| A-MG-07 | حساب Exc.Rate + Local Value | عملة مختلفة | عرض تلقائي | DNT §6 ص34 |
| A-MG-08 | تقييد الإصدار بالتفويض | محاولة إصدار PR غير مفوض | "requisition issues are **not allowed**" | DNT §1 ص5 |
| A-MG-09 | **توليد Adjustment Transactions** | Stock Variance Updation | "The excess or short variance is referred as Adjustment Transactions" + ترحيل السالب إلى Variance CC | DNT §14 ص72 + SET §14 |
| A-MG-10 | تجميد الشهور المعالجة | Process Store Ledger | حظر التحديث "except for the current month" | DNT §15 ص73 |
| A-MG-11 | توزيع الموازنة آلياً | Budget Entry = Apportion | "assign budget values **automatically** to each cost center for each month" | SET §22 ص58-59 |

## 4. الأرقام التسلسلية المولدة (Numbering)

| الرقم | المولد | اللحظة |
|---|---|---|
| Request # (PR) | النظام | عند الإدخال (يتاح للتعديل في Modify فقط) |
| Indent # | النظام | "displays with an Indent number entry" بعد الحفظ |
| PO # | النظام | "to generate the Purchase Order number" (نهاية WF) |
| SPO # | النظام | "generated automatically when a PO is created" |
| SWO # | النظام | عند التوليد |
| Quotation # | النظام | "to generate a quotation number" |
| GR # / GRR # | النظام | Receipt / Receipt Return |
| Doc Number (Issue) | النظام | "This field is automatically generated" |
| Process Number (Re-Order) | النظام | عند المعالجة |

> **قاعدة:** كل مستندات الوحدة **مرقمة آلياً** — لا إدخال رقم يدوي موثق واحد (باستثناء Ref# المرجعية اليدوية القصيرة 3-10 خانات).

## 5. الطوابع الزمنية وسير الأعمال

- **Business Date مصدر التحقق:** تواريخ GR/Issue/Physical كلها تقارن "system date"/"server month" — نفس عائلة Business Date في FO (لكن هنا **تاريخ النظام/الخادم** حرفياً — [UNCERTAIN] هل يتقدم مع Night Audit؟ لا توثيق مباشر في MGT — يُفترض ربطه بعملية الإقفال الشهري لا اليومي).
- **التأريخ الرجعي منظّم:** نافذة أيام لكل نوع معاملة (V-MG-38) — ليس ممنوعاً مطلقاً بل **مقنناً**.
- **الشهر المالي للمخزن مستقل عن السنة المالية** (Stores Start Date بالشهر + Ledger شهري) — دورة إغلاق أدق من FAS.
