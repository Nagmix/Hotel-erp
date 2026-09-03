# 17 — تحليل الفجوات (Gap Analysis) — وحدة HRP

> **11 فجوة مصدر (GAP-HR-D)** + **12 فجوة ERPNext (GAP-HR-E)** — كل فجوة بأثرها ومسار تسويتها.

---

## A. فجوات المصدر (Documentation Gaps)

| # | الفجوة | الدليل | الأثر | التسوية |
|---|---|---|---|---|
| **GAP-HR-D01** | **واجهة الحضور Enterprise Only** | "[Applicable to Fortune Enterprise Only]" (PNT §7) | الفجوة الإصدارية الثالثة (بعد AR Membership hint + POS Module Attributes خارج الحزمة) — وسم قدرات 6i حسب الطبعة | يُوثَّق القدرة كمتغيرة؛ تصميم منصة بـ biometric connector حديث أصلاً |
| **GAP-HR-D02** | لا ملف LUK مستقل | بنية الحزمة (استعلامات ضمن REP §1) | تباين بنية الوحدات | بطاقة موظف موحدة تصميمياً |
| **GAP-HR-D03** | Special Program PYINDSP مغلق | "This code is only for Indian clients" بلا مواصفات | منطق أهلية ESI الشهري غير معلن | يعاد التصميم قاعدة شرائح (F-HR-3) |
| **GAP-HR-D04** | Print Program IDs غير مفصلة | PT/LWF Defn فقط ذكرت | طباعة النماذج مجهولة البنية | طباعة مخصصة جديدة |
| **GAP-HR-D05** | **عقد بائع الحضور** | "intimated... two weeks in advance... confirm in writing directly to IDS Bangalore" | متطلب حوكمة تاريخي — لا قيمة معمارية اليوم | استبدال كامل بواجهة API |
| **GAP-HR-D06** | JV تفصيلي غير موثق في HRP | (راجع 11 QA-HR-1) | القيد النمطي للرواتب | من FAS-TRN في Phase 6 |
| **GAP-HR-D07** | تعريف Non Employee | "Employee/Non Employee or Both" بلا تعريف | نطاق كيان غامض | قرار C-HR-8 |
| **GAP-HR-D08** | تفرد Employee# غير مصرّح | GAP-HR-V01 | قيد بيانات | unique constraint (قياسي) |
| **GAP-HR-D09** | سلوك الشرائح عند الأطراف | E-HR-05/06/07 | محرك حساس | اختبارات وحدة تصممية |
| **GAP-HR-D10** | مواعيد دورة Accept/Pre-run | لا توقيتات موثقة | UX | F-HR-2 |
| **GAP-HR-D11** | Loan ED تعيين إلزامي غير موثق | E-HR-23 | تكامل محرك | قيد تصميمي |

## B. فجوات ERPNext (Platform Gaps)

| # | الفجوة | الأصل | الحل المقترح | الجهد |
|---|---|---|---|---|
| **GAP-HR-E01** | **محرك الشرائح الرباعي** (Normal/Cumulative/Step Over/Eligibility + Min/Max) | SET §10 | ED Slab doctype بأربعة أوضاع + اختبارات بالأمثلة الرقمية الموثقة (500/350/400!) | L |
| **GAP-HR-E02** | **Accumulation الثلاثي** (Month/Cumulative/C-O) | SET §10 | معالج YTD بنقاط تهيئة + مثال SER1/SER2 كاختبار | M |
| **GAP-HR-E03** | **Priority/Partial/Carry Forward للخصومات** | SET §10 | خصائص على Deduction rows + قائمة انتظار ترحيل | M |
| **GAP-HR-E04** | **Take Home %** | SET §8 | قاعدة clamp في المحرك | S |
| **GAP-HR-E05** | **Accept-at-run** | PNT §10 | خطوة wizard | S |
| **GAP-HR-E06** | **AR→Payroll hook** | PNT §22 | event handler + Additional Salary | M |
| **GAP-HR-E07** | **كسر النقد** | SET §18 | تقرير مخصص | S |
| **GAP-HR-E08** | **النماذج الهندية (15 نموذجاً)** | REP §13/§14 | طباعة مخصصة اختيارية لعملاء الهند | M |
| **GAP-HR-E09** | **Bonus الرباعي + PT recalc** | PNT §18 | أداة معالجة مخصصة | M |
| **GAP-HR-E10** | **إقفال حبيبي Dept/CC/Grade** | PNT §11 | حالة على Payroll Entry sub-scope أو إدخال Entries متعددة | M |
| **GAP-HR-E11** | **Denomination + Salary Template preview** | SET §13/§18 | حقول مخصصة | S |
| **GAP-HR-E12** | **تقارير 80/132 + DBF + userId-dotted** | REP عموماً | طباعة A4/HTML + تصدير قياسي | S |

## C. مقارنة جهد التسوية

| الجهد | العدد | أمثلة |
|---|---|---|
| S (صغير < يوم) | 5 | E04/E05/E07/E11/E12 |
| M (متوسط 2-5 أيام) | 5 | E02/E03/E06/E08/E09/E10 |
| L (كبير > أسبوع) | 2 | E01 + F-HR-1 (المحرك) |

## D. قرارات "إصلاح لا استنساخ" (Fix-don't-Clone)

| السلوك الأصلي | القرار | المرجع |
|---|---|---|
| حضور فردي إلزامي | Bulk + import | 15 |
| ACCEPT يوقف المعالجة | pre-run wizard | F-HR-2 |
| كلمات مرور مكشوفة (SYS) | — (سبق) | SYS |
| ملفات 80/132/DBF | A4/XLSX | GAP-HR-E12 |
| حقول هندية ديموغرافية إلزامية الشكل | configurable per country | F-HR-3 |
| INI 220 معكوس | إلغاء — ممكن دائماً | 16 |
