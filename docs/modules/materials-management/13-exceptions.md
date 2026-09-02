# 13 — الحالات الحدية والاستثناءات (Edge Cases) — وحدة Materials Management

> 26 حالة حدية موثقة/مستنتجة بعلاماتها. الوحدة **الأكثر استثناءات بنيوية** (تجمد + هرمية + صفر/سالب).

---

## 1. حالات التجميد والإغلاق (Freeze Edge Cases)

| # | الحالة | السلوك الموثق | المصدر |
|---|---|---|---|
| EC-MG-01 | تعديل Store بعد الحفظ | ممنوع كلياً — "Status... Passive and a new Store Code has to be created" | SET §1 ص5 |
| EC-MG-02 | تغيير طول Item Code بعد بدء التشغيل | "cannot be altered" — ممنوع بنيوياً | SET §5 ص10 |
| EC-MG-03 | تحديث Opening Balance بعد أول معاملة | "you will **not be allowed**" — ممنوع | SET §6 ص18 |
| EC-MG-04 | تعديل معاملة في شهر معالج (Ledger) | ممنوع "except for the current month" — **الاستثناء نفسه حالة حدية**: الشهر الحالي يظل قابلاً للتعديل حتى معالجته؟ [UNCERTAIN — الصياغة تعني المعالجة تتم لبداية شهر جديد فالحالي لم يعالج أصلاً] | DNT §15 ص73 |
| EC-MG-05 | فك تجميد شهر | Cancel Stores Ledger — مسار استرداد موثق | DNT §15 ص74-75 |
| EC-MG-06 | تنفيذ Physical Stock لشهر حالي | "Month and Year must be **less than the server month**" — مرفوض | DNT §13 ص70 |
| EC-MG-07 | Stores Start Date مستقبلي | مرفوض (≤ الحالي فقط) | SET §4 ص9 |

## 2. حالات المخزون الصفري والسالب

| # | الحالة | السلوك | المصدر |
|---|---|---|---|
| EC-MG-08 | إصدار صنف رصيده صفر (Indent) | **DPR Qty** — تحويل تلقائي لطلب شراء ينعكس في الاستلام | DNT §6 ص40 |
| EC-MG-09 | جرد أقل من الرصيد الدفتري | "negative values" → **Adjustment Transaction آلي + ترحيل Variance CC** | SET §14 + DNT §14 |
| EC-MG-10 | تسوية صنف رصيده صفري | **Include Zero balance checkbox** — مسار خاص | DNT §6 ص44 |
| EC-MG-11 | تسوية سالبة | Adjustment Type (سبب) إلزام — موجبة = "unknown" | DNT §6 ص45 |
| EC-MG-12 | تعديل تسوية بكمية أكبر من المعروض | "For posting minus values, **enter the data greater than the data displayed**" — منطق تجاوز رقمي | DNT §6 ص44 |

## 3. حالات التسلسل الهرمي والاتجاه

| # | الحالة | السلوك | المصدر |
|---|---|---|---|
| EC-MG-13 | Sub Store يستلم من غير Main المرتبط | مرفوض بنيوياً — "can receive items **only** from the Main Store to which it is linked" | SET §1 ص5 |
| EC-MG-14 | إصدار صنف لعلم Issue Allowed = No | مرفوض — علامة اتجاهية على مستوى الصنف×المخزن | SET §5 ص12 |
| EC-MG-15 | تحويل Conversion عبر مخازن مختلفة | مرفوض — "From and To should be of the same Store" | SET §20 ص53 |
| EC-MG-16 | صنف واحد لمنفذين بيع (Shop Outlet) | مرفوض — "tagged to **only one** shop outlet" | SET §5 ص15 |
| EC-MG-17 | Inter Store Transfer بلا Indent أصلي للشهر | الشاشة تعمل على "Month and Year this indent was created" — لا مصدر = لا عناصر | DNT §6 ص65 |

## 4. حالات التواريخ والصلاحية

| # | الحالة | السلوك | المصدر |
|---|---|---|---|
| EC-MG-18 | استلام Contract بعد انتهاء العقد | مرفوض — GR ≤ Expiry | DNT §6 ص32 |
| EC-MG-19 | GR قبل تاريخ PO | مرفوض — GR ≥ PO Date | DNT §6 ص32 |
| EC-MG-20 | استلام صنف بتاريخ انتهاء ماضٍ | مرفوض — Expiry ≥ System Date | DNT §6 ص34 |
| EC-MG-21 | تاريخ إصدار رجعي خارج النافذة | "specified number of days" لكل نوع — مرفوض | SET §24 |
| EC-MG-22 | Applicable From ماضٍ في إعداد | مرفوض — ≥ اليوم | SET كل الإعدادات |

## 5. حالات البيانات والفرادة

| # | الحالة | السلوك | المصدر |
|---|---|---|---|
| EC-MG-23 | نفس Item Code في مخزنين | مرفوض — فرادى عمومية | SET §5 ص10 |
| EC-MG-24 | Sub Code لصنف بنفس UOM الإصدار والتحويل | مرفوض — يشترط الاختلاف | SET §5 ص10 |
| EC-MG-25 | Batch# فارغ مع تكرار الصنف في الاستلام | إلزام يتفعل — "entry mandatory when same item code is selected more than one time" | DNT §6 ص34 |
| EC-MG-26 | Yield > 100% | مرفوض | SET §20 ص54 |
| EC-MG-27 | FSN: Fast Qty ≤ Slow Qty | مرفوض — "greater than" | SET §18 ص51 |
| EC-MG-28 | To Qty ≠ From Qty (Conversion) | مرفوض — التعادل إلزامي | DNT §6 ص46 |

## 6. حالات الموردين

| # | الحالة | السلوك | المصدر |
|---|---|---|---|
| EC-MG-29 | شراء من مورد Black Listed | الحقل موثق كعلم Manع — آلية الحجب الفعلية عند PO [NOT DOCUMENTED صراحة: يُفترض تحذير/منع — INFERENCE] | SET §9 ص24 |
| EC-MG-30 | Stop Purchase = Yes | منع الشراء موثق | SET §9 ص27 |
| EC-MG-31 | Contract Item بلا Last Rate | إلزام تفويت — "entry of Last Rate is mandatory" | SET §10 ص37 |
| EC-MG-32 | Misc Tax بعملة مختلفة + Percentage | مرفوض — "only Amount will be accepted" | DNT §6 ص35 |
| EC-MG-33 | مسح باركود غير معرف (INI 245 غير مفعل) | الباركود لا يعمل في المخزن أصلاً (BEV/FB/LQ فقط) | SET §5 ص14 |

## 7. حالات الاستعلام والحالة

| # | الحالة | السلوك | المصدر |
|---|---|---|---|
| EC-MG-34 | PO "Blank Space" status | قيمة خام تظهر في PO by Vendor — [UNCERTAIN] لم يُستلم عليه | LUK §6 |
| EC-MG-35 | الاعتماد على شاشة ذكية بلا بيانات | عدادات صفرية (لا سقوط) — سلوك افتراضي | DNT §31 |
| EC-MG-36 | Purge لطلب غير آلي | Indent Purging يستهدف "auto-generated requisitions" — اليدوي **لا يشمل** [UNCERTAIN] | SET §26 |

## 8. استنتاجات تصميمية للواجهة الجديدة

1. **الحالات الصفرية/السالبة مسارات أولى** لا استثناءات (DPR/Variance/Zero-balance checkbox) — الواجهة العربية يجب أن تُظهرها كأزرار حالة واضحة.
2. **أخطاء التجميد تحتاج رسائل تفسيرية** (لماذا رُفض؟ أي بديل؟) — الأصل يكتفي بالمنع.
3. **قائمة الحالات المرتبطة بالتواريخ (7 حالات)** تستحق مكون "فاحص تواريخ" موحداً في الواجهة مع تفسير كل قاعدة.
