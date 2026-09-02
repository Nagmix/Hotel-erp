# 11 — الأثر المحاسبي (Accounting Impact) — وحدة Banquets

> الأحداث المالية الموثقة + الروابط إلى AR/FAS/FO. BNQ رابط الترحيل الرابع من الستة (BNQ→Finance في FAS-SET).

---

## 1. الأحداث المالية (E-BQ-01..14)

| # | الحدث | الطبيعة | الموثق | المصدر |
|---|---|---|---|---|
| E-BQ-01 | Hall Charges + Rate/Pax (حجز/متطلبات) | إيراد قاعة + إيراد شخص | القيم تدخل الفاتورة مع بنى الضرائب (Inclusive/Exclusive) | BOK/BIL |
| E-BQ-02 | **Minimum Revenue** (القاعة) | أرضية إيراد | حقل Details في Function Room | CFG §5 |
| E-BQ-03 | **Minimum Cover Charge** (الجلسة) | حد أدنى للجلسة | Link Outlet-Sessions | SET §1 |
| E-BQ-04 | الوديعة (Cash/Card/Cheque) | التزام مقدَم | Vouchers + Running Balance | BIL §9 |
| E-BQ-05 | **Refund** | عكس التزام | "total deposit will be get deducted from the Refund charges" | BIL §10 |
| E-BQ-06 | **Retention** | احتجاز/إيراد جزائي | يقتطع من الوديعة + Reason | BIL §10 |
| E-BQ-07 | **Cancellation Policy charge** | غرامة إلغاء | "Days range, value type (V/P)... charged to the Party in case the Party cancels" | CFG §4 |
| E-BQ-08 | **Credit Card Settlement → AR** | ذمم بطاقات | "sent to the Accounts Receivable module for further processing" | BIL §4 |
| E-BQ-09 | **Company Settlement → AR outstanding** | ذمم شركات | "treated as outstanding until payment is received from the Company" | BIL §4 |
| E-BQ-10 | **Staff Settlement → AR** | ذمم موظفين | "saved in the Accounts Receivables module" | BIL §4 |
| E-BQ-11 | **Guest Settlement → FO Folio** | ترحيل لغرفة | Room# + بيانات الضيف | BIL §4 |
| E-BQ-12 | **Complimentary/NC** | **ليست مبيعات** | "Settlements made by this mode is not considered as Sales for the Hotel" — **بند إيراد محاسبي صريح** | BIL §4 |
| E-BQ-13 | **Multiple Settlement** | مزج وسائل | Cash + نمط (باستثناء غير البيعية) — مثال NRS 5,976 | BIL §4 |
| E-BQ-14 | **Auto Indent → MGT** | تكلفة مخزنية قادمة | indent بالوصفات حسب القسم | BIL §13 |

## 2. الضرائب الموثقة

| العنصر | الموثق |
|---|---|
| بنى العرض في الحجز | **INI 409** |
| الافتراضي للقاعة | **Print Forms program** (Hall Tax Structure) |
| التبديل | **Inclusive/Exclusive** (بجوار Hall Charges) |
| Rate/Pax Tax | Tax Structure (Rate/Pax) في Print Forms |
| Non F&B Group | Group Code (Non F&B) — "considered for **billing purposes**" |
| صنف القائمة | Tax Structure لكل صنف (Menu Master) + **GL Code** (النمط الفردي!) |
| Corporate Rates | Tax type + structure لكل عائلة |

## 3. أثر الترحيل (من FAS — روابط متبادلة)

- **BNQ→Finance**: ضمن الروابط الست الموثقة في FAS-SET (راجع financial-accounting/11).
- **بنود القيد الفعلية**: FAS-TRN Book Types (مرجع متبادل — لا تُكرر هنا).
- **Complimentary/NC ليست مبيعات** → استبعاد من Sales Journal عند الترحيل (قاعدة مرحلة 6 موثقة هنا أصلاً).

## 4. [NOT DOCUMENTED] المحاسبية

| البند | الحالة |
|---|---|
| توقيت الترحيل BNQ→FAS | كالتالي في MGT (UNK-027) — Phase 6 |
| قيد الوديعة (خصم نقدية/التزام؟) | Vouchers موثقة؛ القيد [NOT DOCUMENTED] |
| معالجة Cancellation Policy charge في GL | [NOT DOCUMENTED] |
| توزيع Package Menu Card على حسابات GL | GL Code موثق للصنف فقط — التجميع [NOT DOCUMENTED] |
