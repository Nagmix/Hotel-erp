# 05 — قواعد العمل (Business Rules) — وحدة Materials Management

> BR-MG-01..18 مجموعات القواعد الموثقة نصاً. الوحدة **الأكثر قواعد تقييد هيكلية** (هرمية مخازن + تواريخ أعمال + تجميد دوري).

---

## BR-MG-01 — هرمية المخازن واتجاهات الحركة (القاعدة الدستورية)

**المصدر:** SET §1 ص5.

| القاعدة | النص الموثق |
|---|---|
| Sub Store يستلم **فقط** من Main المرتبط | "A Sub Store **can receive items only from the Main Store to which it is linked**" |
| Independent يستقبل ويصدر مباشرة | "can receive and issue items directly... **does not depend on other Stores or Sub Stores**" |
| Main هو القناة للتحويل للمخازن الفرعية | "Main Store – is a main division of Stores that **can transfer items to Sub-Stores**" |

**+ أعلام الأصناف الاتجاهية** (SET §5 ص12): Issue Allowed / Receipt Allowed / Receipt Return — **بوابات دقيقة على مستوى الصنف×المخزن** فوق الهرمية العامة.

## BR-MG-02 — قواعد التقييم (Valuation)

**المصدر:** SET §1 ص5-6 + DNT Adjustment ص45.

1. طريقة التقييم **تُختار عند إنشاء المخزن** (Weighted Average أو FIFO) — **لكل مخزن على حدة**.
2. **WA:** "Weighted Average = (Closing Balance Value / Closing Quantity)" — كل المعاملات **بما فيها الرصيد الافتتاحي** تقيَّم بها.
3. **FIFO الأصلي = إصدار بأقرب انتهاء (FEFO):** "issue of Items from Store will be prioritized on the basis of the **Expiry Date** of the Goods Receipt" + "The rate / valuation of Items will get reflected depending on the selection of either the **Opening Balance Quantity or Date wise receipt** of goods".
4. **قاعدة دعم Adjustment:** "For Stores defined with FIFO method of valuation, the adjustment methodology **will be supported**" — يوحي بقصور دعم Adjustment في WA [UNCERTAIN: الصياغة تحصر الدعم بـ FIFO].
5. **صيغة القيمة الدورية:** "Opening Value + Receipt Value − Issues + Issue Returns − Receipt Return divided by the Quantities accordingly" (تراكم WA).

## BR-MG-03 — فرادة وترميز الأكواد

| الكيان | القاعدة | المصدر |
|---|---|---|
| Store Code | 3 خانات alphanumeric فريدة — **لا تعديل ولا حذف بعد الحفظ** (الحالة → Passive + كود بديل) | SET §1 ص5 |
| Item Code | رقمي ≤12 (INI #39)؛ **فرادى عبر كل المخازن** ("entry of similar Item Codes for different stores is not possible")؛ **طول الكود يُجمَّد بعد بدء التشغيل**؛ تعديل الطول = "IDS Customer Service Engineers or authorized EDP personnel" فقط | SET §5 ص10 |
| Item Group Code | 3 خانات فريدة — إلزامية الربط لكل صنف | SET §2 ص6-7 |
| Vendor Code | 7 خانات = **3 نوع (من Company Types/FO) + 4 كود مستخدم** | SET §9 ص22-23 |
| Contract Number | 3 خانات فريدة لكل مورد عقد | SET §11 ص39 |
| Vendor Rating / Terms / Transfer Code | 5 / 3 / 3 خانات فريدة | SET §§7/8/20 |

## BR-MG-04 — قواعد التواريخ (Date Logic) — أغنى مصفوفة زمنية

| المعاملة | القاعدة | المصدر |
|---|---|---|
| Applicable From (كل الإعدادات تقريباً) | **≥ اليوم** (إصدارية مستقبلية) | SET §§1/2/8/11/14/17/20/21 |
| Stores Start Date | **≤ الشهر/السنة الحالية** (اتجاه معاكس — تاريخي!) | SET §4 ص9 |
| GR Date (Contract) | **≤ تاريخ انتهاء العقد** | DNT §6 ص32 |
| GR Date (PO) | **≥ تاريخ الـ PO** | DNT §6 ص32 |
| GR Date (Direct) | **≥ تاريخ الطلب** | DNT §6 ص32 |
| Expiry Date (استلام) | **≥ تاريخ النظام** | DNT §6 ص34 |
| Issue Date (Indent) | **≥ تاريخ النظام الحالي** | DNT §6 ص39 |
| Physical Stock Date | **Month/Year < شهر الخادم** | DNT §13 ص70 |
| Process Store Ledger | "enabled **after the beginning of a new month**" | DNT §15 ص73 |
| Backdate Trn. Access | **نافذة أيام محددة لكل مستخدم×نوع معاملة** | SET §24 ص64-65 |

## BR-MG-05 — تفويض متعدد المستويات (سلسلة 1→2→3)

**المصدر:** DNT §1 ص5-7 + §2 ص15 + §3 ص21.

1. **PR:** INI 355 = 1/2/3 → إلزام مستوى/مستويين/ثلاثة — "If authorizations are not made, **requisition issues are not allowed**".
2. **تسلسل صارم:** "Level one authorization... is **mandatory before receiving the Level 2 authorization**".
3. **Indent:** INV #6/#7 (مستويان). **PO:** INV #13/#14/#298 (ثلاثة).
4. **Authorization Details (Lookup):** تتبع تفويضات PO/PR/Indent — **تدقيق جاهز**.

## BR-MG-06 — قواعد الاستلام والفاتورة (Receipt/Bill)

1. **الاستلام بلا أمر:** مسموح (Direct) فقط عند INV #5 = Yes.
2. **Bill#/Bill Date إلزام عند INV #3** — "always recommended... will be used in the **Payment Match** option while making Payment" (DNT ص32).
3. **Batch# عند التكرار:** "entry mandatory when **same item code is selected more than one time**" (DNT ص34).
4. **Complimentary:** بلا Rate Plan وTax Structure (DNT ص33).
5. **Currency مختلفة → Exchange Rate يظهر** تلقائياً (DNT ص34).
6. **Misc Tax بقاعدة العملة:** "If the Currency is **equal to** the currency entered in the Main screen, then the **Percentage or Amount** can be specified. Else, **only Amount** will be accepted" (DNT ص35).
7. **Cost Center يُستخدم فقط** للـ Non-Stockable/Cash Purchase؛ Sub Store يُعرض فقط إذا كان المخزن Main؛ وكلاهما **يُعطَّل** للـ Non-Stockable (DNT ص34).

## BR-MG-07 — قواعد الإصدار (Issue)

1. **المعروض للإصدار:** الرصيد "as on the system date".
2. **التوزيع التصاعدي:** "with date in ascending order, the items will be distributed" + Batch Help للتعديل اللحظي (DNT ص38) — **FEFO تطبيقياً**.
3. **الإصدار ضد Indent يتبع التفويض:** "issue of items that are recorded in the indent entry. Issue of items is **based on authorized indents** from the Departments" (DNT ص38).
4. **DPR عند الصفر:** "If the item has 'Nil' balance, you can enter the requisition in the 'DPR Qty' field" → "reflected during the Receipt entry" (DNT ص40).

## BR-MG-08 — التحويلات: مساران بعدد الأطراف

1. **Inter Store Transfer:** يتطلب **Month/Year لإنشاء الـ Indent** — يعمل على أصناف الطلب القديم ("Enter the Month and Year this indent was created") (DNT ص65).
2. **Sub Store Transfer:** sub→sub مباشر بمرجع وتوازن تلقائي (DNT ص65-66).
3. **Conversion:** **To Qty = From Qty** إلزام ("The quantity specified in the To Items Details should be **equal to** the quantity specified in From Items Details") + **Yield ≤ 100%** (SET §54) + **نفس المخزن** (SET §53).

## BR-MG-09 — التجميد الشهري المتدرج (Three-tier Month Freeze)

**المصدر:** DNT §15 ص73-75.

1. **الإقفال:** Process Store Ledger بعد بداية شهر جديد → طباعة Stores Ledger متاحة.
2. **الحظر:** "update of transactions will **not be allowed** for the processed months **except for the current month**".
3. **الاستثناء:** Cancel Stores Ledger → إعادة فتح للتصحيح → إعادة المعالجة.

> **عائلة التجميد المعمارية:** Night Audit (يومي/FO) · Store Ledger (شهري/MGT) · Financial Year (سنوي/FAS) — ثلاث مستويات إغلاق بنفس فلسفة "فتح جديد = تجميد سابق + مسار إلغاء".

## BR-MG-10 — الرصيد الافتتاحي والبدء

1. **ترتيب الإلزام:** Inventory Master **قبل** Opening Balance (SET ص18).
2. **التجميد النهائي:** "Once the Transactions have commenced for the Store, you will **not be allowed** to update the Opening Balance details" (SET ص18).
3. **Gr.Date:** تصاعدياً أو آخر يوم في "Up to Month/Year" (SET ص18).
4. **تعريف البدء يلزم بملء الرصيد:** "Once the Month/Year are entered, the **Closing Balance details** of the stockable items have to be entered" (SET ص9).

## BR-MG-11 — إعادة الطلب (Re-Order)

1. **الشرط الرقمي:** الرصيد **≤ Re-order Level** المعرف في Inventory Master (DNT §8 ص57).
2. **تسلسل المعالجة:** Process (رقم) → Update & Generate → "posted to a Department" — **قرار الشراء يبقى قسمياً** (PO أو Direct).
3. **الأداة التوليدية:** "Reorder Level is significant since **Purchase Requisitions are generated on these specifications**" (SET ص12).

## BR-MG-12 — الجرد والفروقات (Audit/Variance)

1. **Variance Cost Centers إلزامية** لترحيل السالب: "mandatory requirement for **automatic posting of negative (short) variances**" (SET §44).
2. **الفائض/العجز → Adjustment Transactions** آلياً (DNT §72).
3. **تنبيه التحقق البشري:** "alerting if the **Physical Stock Variance report has been checked**" قبل التحديث (DNT §72) — **نقطة ضبط جودة إجرائية**.
4. **Adjustment السالب يبرر السب** (Adjustment Type)؛ الموجيب = "unknown" (DNT ص45).

## BR-MG-13 — قواعد الموردين التجارية

1. **Black Listed:** يلزم اسم المُدرِج + السبب (SET ص24) — **مسؤولية موثقة**.
2. **Stop Purchase = Yes:** منع الشراء كلياً (SET §9 ص27).
3. **Stop Payment** [⚠️ منطق معكوس موثق]: "if you want to stop making any payments to the vendor, select the option **NO**... Unless you change this option to **YES**, the system will **not allow** you to make any payments" (SET §28) — [UNCERTAIN]: النص متناقض التسمية/السلوك؛ التسجيل الحرفي مع علامة مراجعة للتنفيذ (يُفهم عملياً كـ Allow-Payment).
4. **Contract Vendor:** Contract# إلزامي (متحقق من Vendor Contract Info) + Last Rate إلزامي؛ **Normal Vendor:** "the **last Rate** at which the Item was purchased... will get updated" تلقائياً عند الاستلام (SET §37).
5. **عتبة السداد:** Credit Days + Credit Limit + **5 شرائح خصم** + شرائح فائدة (مثال موثق: 90 يوم ائتمان؛ 91-100 يوم → 10% فائدة) (SET §27-29).

## BR-MG-14 — التقييم الضريبي الشرائي

1. **Tax Exemptions:** YES = إعفاء من حساب الضريبة (VAT) — "tax paid by the Purchaser is **reimbursed by the state**" (SET §47).
2. **Item Taxes:** ضريبة استيراد مختلفة عن المحلية — "for all the imported items for which the tax rate is different from the local taxes" (SET §48).
3. **القيم تنعكس في Purchase Journal:** "The tax values will be **reflected separately** during posting and generation of Purchase Journal to the General Ledger" (SET §47).

## BR-MG-15 — الموازنات (Budget)

1. الأساس: **Item Group أو Item Code** لسنة مالية لكل Property.
2. **Fixed** يدوي أو **Apportion** آلي بنمط توزيع + "You can also manually change the budget values" (SET §58-59).
3. **F2/F4** نسخ/لصق بين مراكز التكلفة (SET ص59).

## BR-MG-16 — التطهير (Purging) الانتقائي

1. **Indent Purging:** يستهدف "**auto-generated requisitions**" تحديداً بحد أيام/تاريخ (SET §67).
2. **Purge PO/SPO:** نطاق تاريخ → قائمة → **checkbox انتقائي** → تنفيذ (SET §67-68).

## BR-MG-17 — الصلاحيات الرباعية البُعد

**المصدر:** SET §24 ص61-65. مستخدم × {مخزن · وظيفة · قسم/CC · **نافذة أيام رجعية لكل نوع معاملة**} — الأبعاد الثلاثة الأولى معيارية؛ **الرابع فريد في المشروع كله**.

## BR-MG-18 — FSN (التحليل الحركي)

"Fast & Slow Movement... based on **Fast / Slow Quantity divided by the Cut off Days** into the **Total Days** specified for generation of the report, in comparison with the **total consumption** for the given date range" + قيد تقاطع: Fast Qty **>** Slow Qty (SET §50-51).
