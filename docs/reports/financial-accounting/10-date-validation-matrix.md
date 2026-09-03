# 10 — مصفوفة قواعد التواريخ — FAS-REP (Phase 7)

> ~22 قاعدة على 46 تقريراً — **عائلة past-only الصريحة** + قيود FY/Month-bound + **أرباع TDS**.

---

## 1. البوابات الصريحة الجديدة في FAS

| البوابة | التقرير | النص الحرفي |
|---|---|---|
| **تاريخ ≤ تاريخ النظام** | TB Format 2 (§9) + TB الرابع | "Date entered should be **less than or equal to the Current System Date**" |
| **شهر ≤ شهر النظام** | TB Format 2 + الرابع | "month and year that is **less than or equal to the Current System Month**" |
| **Cut Off ≤ الجاري** | Balance Confirmation (§14) | "Cut Off Date... **less than or equal to the Current System Date**" |
| **تاريخ ≤ الجاري** | Pending Receipts for PJV (§18) | "Date entered should be **less than or equal to the Current System Date**" |
| **داخل الشهر/السنة المحددين** | Advice/Cheque (§24) | "Date entered should be **within specified Month / Year**" — month-bound على سلسلة 11 خطوة! |
| **داخل السنة المالية** | PDC Check List (§32) | "From date should be **within the financial year specified**" |

**ملاحظة بنيوية:** FAS تجمع **أكبر كثافة قيود past-only صريحة** (4 مواضع حرفية!) — عكس MGT (قيود "الجاري حصراً") وPOS (نادر) — **القيد الزمني المالي ماضويّ بحت**.

## 2. المصفوفة الكاملة

| # | التقرير | القاعدة |
|---|---|---|
| 1 | 1 CoA List | بلا تاريخ (ماستر) |
| 2 | 2 Transaction Checklist | date range (ضمن FY بF3) |
| 3 | 2(2) TC | Doc# + خيارات |
| 4 | 3 Ledger Opening Balance | **شهر محدد = شهر بدء FAS** |
| 5 | 4 Day Book | "particular date or date range" |
| 6 | 4 Day Book F2 | (بالمثال — بلا قاعدة صريحة) |
| 7 | 4 Cash/Bank Book | FY + From/To |
| 8 | 5 Ledger Balance | FY + Date range |
| 9 | 6 General Ledger | FY + **Month range** (شهور لا تواريخ!) |
| 10 | 7 P&L | **Month & Year** |
| 11 | 7 PL by CC/Dept | Month & Year (أعمدة Month/YTD/PrevYr/Total) |
| 12 | 8 Balance Sheet | Month & Year |
| 13 | 9 TB (الأصل) | **Date أو Month & Year** |
| 14 | 9 TB F2 | **Date ≤ SysDate · Month ≤ SysMonth** + XOR 0/132 |
| 15 | 9 TB (3.3) | كF2 (إحالة ذاتية) |
| 16 | 9 TB (رابع) | Date/Month&Year + قيود ≤ نفسها |
| 17 | 10 Creditors Outstanding | **As On / Month / Date** ثلاثية |
| 18 | 11 Purchase Tax Register | date range |
| 19 | 12 Purchase Register | date range |
| 20 | 13 Expense Register | FY + date range + **Above مبلغ** |
| 21 | 14 Balance Confirmation | **Cut Off ≤ SysDate** |
| 22 | 15 Debit Note Print | Date أو Debit Note + نطاق |
| 23 | 16 CDN List | date range |
| 24 | 17 Detail Register | FY + date range + Minimum Amount |
| 25 | 18 Pending PJV | **Date ≤ SysDate** + Print Seq ثلاثي |
| 26 | 19/20 Unlinked/Linked | بلا نطاق (فحص هيكلي) |
| 27 | 21 Auto Posted | date range + 80/132 |
| 28 | 22 FA Budget List | FY + Budget type |
| 29 | 23 Bank Rec | **Realized Date range** أو **As on** |
| 30 | 24 Advice/Cheque | Month & Year + **داخل الشهر** + Normal/Repeat |
| 31 | 25 Voucher Print | Month & Year + Date أو Doc No |
| 32 | TDS Details | **MMYY** + FY |
| 33 | Invoice/Payment Check | date range |
| 34 | Advance Paid | date range |
| 35 | 26 Form 16A | date range + **Run Date** + **أرباع ×4** |
| 36 | 27 Form 26J | **Certificate No range** (F1) |
| 37 | 28 Form 27 | **Challan No + Challan Date** |
| 38 | 29 Form 26A | Challan No + Date |
| 39 | 30/31 Forms 26C/26K | date range |
| 40 | 32 PDC List | **From داخل FY** |
| 41 | 33 Audit Trial | **Txn Date XOR Updated Date** + range |
| 42 | 34 User Reports | Month & Year |
| 43 | Bank Payment | date range |

## 3. مقارنة أنماط البوابات — الخلاصة النهائية للمرحلة 7

| النمط | FO | POS | MGT | **FAS** |
|---|---|---|---|---|
| Date range | ✓ | ✓ | ✓ | ✓ |
| Date XOR Month | نادر | نادر | **9 تقارير** | TB ×4 (Date/Month&Year) |
| Month & Year (قائمة شهرية) | Budget | — | Budget | **قوائم P&L/BS/Advice/User ×8!** |
| **past-only صريح** | ضمني | 1 | — | **4 حرفية!** |
| **داخل FY** | — | — | 2 (Budget) | **PDC** |
| month-bound | ~15 | ~25 | 1 | **Advice (ضمن M/Y)** |
| future-only | عدة | 1 | **0** | **0** |
| current-only | عائلة | — | 2 | — (لكن **Opening=شهر بدء FAS**) |
| data-gated | — | — | 1 (18.1) | — |
| **مداخل غير تاريخية** | DDMMYY | — | N-أيام/Cut-off/Credit | **MMYY · Challan · Certificate · أرباع · Above/Minimum** |

**الاستنتاجات الختامية:**
1. **FAS = أكثر الوحدات "محاسبية الزمن"**: الشهر وحدة القياس (قوائم شهرية ×8) والماضي قيد صارم (×4) والسنة المالية إطار (FY بF3 في 15+ موضعاً).
2. **مفاتيح استرجاع غير تاريخية**: Challan/Certificate/Ack-Quarters — **النظام الضريبي يسترجع بأرقامه الرسمية** لا بالتاريخ (تقرير = نموذج قانوني مفتاحه رقمه).
3. **أربع وحدات = أربع فلسفات زمنية**: FO (ضيف-حاضر/مستقبلي) · POS (وردية-شهر) · MGT (مخزون-ماضٍ وجرد) · FAS (فترة-إقفال).

## 4. عتبات غير تاريخية قابلة للاختبار (تُختبر في AC)

- **Above/Minimum Amount** (13/17): عتبة مبلغية.
- **Height 11/12 IN** (16A): عتبة ورقية قانونية.
- **أرباع ×4** (16A Ack): زمن TDS الربع سنوي.
- **Run Date** (16A): تاريخ توليد النموذج (منفصل عن نطاق البيانات!) — أول فصل موثق بين **تاريخ التقرير وتاريخ بياناته**.
