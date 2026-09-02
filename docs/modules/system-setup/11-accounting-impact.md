# 11 — الأثر المحاسبي (Accounting Impact) — وحدة System Setup

> SYS **لا يرحّل قيوداً** — لكنه **يؤسس ثلاثة أركان محاسبية**: (1) أسعار الصرف التي يثبّتها AR؛ (2) محرك الضرائب الذي يحسب FO/POS/BQT/Purchase؛ (3) Round-off الذي يعدّل فاتورة الخروج. + Floor Limits كبوابات تسوية.

---

## 1. الأحداث المالية المؤثرة (8)

| ID | الحدث | الأثر المحاسبي | المصدر |
|---|---|---|---|
| E-FIN-SYS-01 | تعريف Round Off للخصيص | **تقريب مبلغ فاتورة الضيف عند Check-out**: None/Nearer/Higher/Lower × Round Amount — الفرق يظهر في الفاتورة النهائية (يحتاج حساب Round-off إجمالي في الفاتورة) | ص42-45 |
| E-FIN-SYS-02 | إدخال Exchange Rate (حتى 4 لكل عملة) | **السعر الساري زمنياً** الذي يثبّت عليه AR عند سداد الفواتير — "exchange rate of the bill date... pinned at settlement" (ACR-OPR) — منع Book Profit/Loss | ص69-71 |
| E-FIN-SYS-03 | Standard Rate للعملة | "valuation is based on that standard rate" — أساس التقييم (افتراضي 1) | ص64 |
| E-FIN-SYS-04 | Division/Multiplication Method | طريقة التحويل (5000÷49 مقابل 5000×49) — تحدد قيمة المكافئ المحلي لكل مبلغ أجنبي | ص65-66 |
| E-FIN-SYS-05 | Tax Code + Applicable To | تحدد أي وحدات (FO/POS/BQT/Purchase) تحسب هذه الضريبة — بوابة الظهور الحسابي | ص71-73 |
| E-FIN-SYS-06 | Tax Slab (Cumulative Y/N) | **طريقة الحساب نفسها** تختلف: 26.25 مقابل 18.75 لنفس المبلغ (مثال الدليل) — فرق مادي في القيد | ص76-77 |
| E-FIN-SYS-07 | Tax Structure: On Value/Discounted/**On Tax** | وعاء الضريبة: خصم يخفض الوعاء؛ On Tax = **ضريبة فوق ضريبة** (تسلسل مكدس) — يحدد الشحنة النهائية | ص81-83 |
| E-FIN-SYS-08 | Credit Card Floor Limit | "validates the set limit credit limit during settlement of Room, POS and Banquet bills" — **حاجز تفويض قبل القيد** | ص93-94 |

## 2. علاقة Round-off بالوحدات (خريطة الوظيفة)

- **Property-level (SYS)**: التقريب هنا للفاتورة النهائية عند Check-out.
- **POS per-currency Round Off** (POS-SET §6): التقريب في منافذ البيع — **كيان مستقل** لكن نفس النمط.
- كلاهما يحتاج حساب `Round-off` كمبلغ فرعي ظاهر في الفاتورة (متطلب تقارير/طباعة).

## 3. علاقة محرك الضرائب بالوحدات (الاستهلاك)

| الهدف | يستهلك | ملاحظات |
|---|---|---|
| Front Office | Tax Code (Applicable To=FO) + Slab/Structure (Module=Front Office) | تقاطع مع Rate Architecture (فصل Tariff/ExtraBed/Plan الضريبي الموثق في FOM-SET §6) |
| Point of Sale | Code (Applicable To=POS) + Structure (Module=Restaurant/Room Service) | + Taxcode Mapping الشهيرة الفارغة (GAP-POS-D01) |
| Banquets | Code (Applicable To=Banquet) + Structure (Module=Banquets) | — |
| Purchase | Code (Applicable To=Purchase) + Structure (Module=Purchase) | تقاطع مع INV Switches (طرق ضريبة الشراء الموثقة في FAS بأمثلة) |
| Laundry / Laundry (S) | Slab/Structure فقط | — |

## 4. أثر كشف كلمة المرور/الصلاحيات على المحاسبة (غير مباشر)

- صلاحيات Add/Modify/Delete على عناصر **Transaction** = قدرة تعديل القيود — الصلاحيات المظلية بوابة مالية.
- AR User Access (أنواع القيود الأربعة) — منع المستخدم من Credit/Adjustment يمنع تلاعب القيود — **طبقة تحكم مالي**.

## 5. أسئلة معلقة (QA)

| ID | السؤال | الحالة |
|---|---|---|
| QA-SYS-1 | هل Round-off يرحَّل لحساب مستقل (Round-off Gain/Loss) أم يندمج في الإيراد؟ | [NOT DOCUMENTED] — الدليل يعرض أثره على "guest bill" فقط؛ مصير الفرق في القيود غير موثق — يُطرح على FAS links عند التحقق النهائي |
| QA-SYS-2 | من يستهلك Decimal Length في القيود (Bank/Cash rounding)؟ | [NOT DOCUMENTED] — موثق كعرض فقط |
| QA-SYS-3 | عند 4 أسعار صرف: أيها يسري للتسوية النقدية الفورية (POS) مقابل تثبيت تاريخ الفاتورة (AR)? | [UNCERTAIN] — AR موثق (تاريخ الفاتورة)؛ POS يستخدم ساري اللحظة [INFERENCE] |
| QA-SYS-4 | هل Floor Limit يمنع التسوية أم يستوجب تفويضاً فقط؟ | [UNCERTAIN] — "validates" فقط؛ السلوك عند التجاوز [NOT DOCUMENTED] (يُربط بمصير UNK-018 سلوك التفويض) |
