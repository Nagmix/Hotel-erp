# 08 — التقارير (Reports) — وحدة POS

> POS-REP (158 ص) **مؤجل للمرحلة 7** (نمط FO/FAS). هنا يُجرد ما ورد في SET/GST/LUK من تقارير ومخرجات موثقة + بنية تعريف تقارير المبيعات المخصصة.

---

## 1. تقارير ومخرجات موثقة في الملفات المقروءة

| ID | التقرير/المخرج | المصدر | الملاحظات |
|---|---|---|---|
| R-POS-01 | **Pending KOTs** (قائمة + إجماليات الكميات والمبالغ) | POS-LUK §1 | قابل للطباعة |
| R-POS-02 | **Pending Bills** | POS-LUK §2 | + التفاصيل بالنقر |
| R-POS-03 | **Table Booking Status** (Reservation # · Covers · Guest · Phone · Special Instruction · Items) | POS-LUK §3 | بتاريخ |
| R-POS-04 | **Settlement Summary** (لكل نمط: cash/credit/cheque/**foreign exchange**/coupon + الصافي) | POS-LUK §5 | بتاريخ وجلسة — مثال موثق: POOLBAR 26-Oct-2010 = Rs. 55,357.00 نقداً |
| R-POS-05 | **Session Statistics** (Receipt Types · Sales Modes · **KOT Audit (Old/New)** · NC KOT · Happy Hours · Void/Comp/BOH · Table Booking · **Menu Movements** · **Average Per Check** · Covers) | POS-LUK §6 | Core/All Sessions |
| R-POS-06 | **Consolidated Sales** (نوع قائمة × تحصيل Cash/Credit) | POS-LUK §7 | لكل منفذ |
| R-POS-07 | **Sales Report** (بتنسيق الأعمدة المخصص من Sales Report Definition) | POS-SET §16 | أعمدة: A/C Group · Taxes · Round Off · Discount · Total Amount · Settlement(s) · Tip(s) |
| R-POS-08 | **DSR — Daily Sales Report** (بتجميعات DSR Session Group ≤3 فئات) | POS-SET §36 | Breakfast/Lunch/Dinner |
| R-POS-09 | **Parameter List** (عرض الإعدادات → IDS Report Engine) | POS-SET §24(2) | Active/All |
| R-POS-10 | **Anniversary List** | POS-GST §5 | معايير بحث موسعة (زيارات/إيراد/تواريخ) |
| R-POS-11 | **Birthday List** (Guest/Spouse DOB) | POS-GST §6 | |
| R-POS-12 | **Repeat Guest List** | POS-GST §9 | منفذ أو الكل |
| R-POS-13 | **Mailing Labels** (عمودان/ثلاثة) | POS-GST §7 | |
| R-POS-14 | **Mailing Letters** (قالب Word + مسار) | POS-GST §8 | |
| R-POS-15 | **Guest Comment Report** (+Print Guest/Company Address) | POS-GST §11 | |
| R-POS-16 | **Guest Comment Analysis** ("Guest Acceptance Audit") | POS-GST §12 | |
| R-POS-17 | مخرجات الطباعة التشغيلية: **KOT · Check/Provisional · NC Bill · Token/Counter** | POS-SET §1 + TS | بنماذج User Defined |
| R-POS-18 | معاينة المصمم + **Match Samples** (مطابقة القوالب) | POS-SET §23 | |

## 2. POS-REP (مؤجل) — الفهرس المكتشف

يُقرأ في المرحلة 7 كاملاً (158 صفحة — أكبر ملف تقارير في الحزمة بعد FOM-REP). مواضعه المتوقعة من فهارس الوحدات الأخرى: مبيعات المنافذ · KOT/Bills · Cashier/Shift · Settlements · Void/Comp · Menu Sales · Tax · DSR · Guest History.

## 3. محرك التقارير (IDS Report Engine)

- مخرجات نمطية: **Display · Spool · Print · Export** (POS-SET §24(2) ص69).
- **IDS Report Designer** (موثق في ACR-RPL §23 وPOS Parameter List) — مصمم تقارير عام.
- أداة طباعة التقارير موثقة في Getting Started (خارج الحزمة — GAP-POS-D03).

## 4. قرارات تصميم التقارير المستنبطة

| القرار | الأساس | المصدر |
|---|---|---|
| Average Per Check صيغة موثقة (Settlement Amount / No. of Bills) | يجب نقلها حرفياً | POS-LUK §6 |
| KOT Audit بثنائية Old/New | نموذج Versioning | POS-LUK §6 |
| **Void/Complimentary شمولية اختيارية لكل تقرير** | "User is advised to list these cautiously" | POS-SET §18 |
| الأعمدة المخصصة لكل منفذ (Sales Report Definition) | 7 أنواع أعمدة نظامية | POS-SET §16 |
| DSR فئات ≤3 | Breakfast/Lunch/Dinner | POS-SET §36 |
