# 05 — قواعد العمل (Business Rules) — وحدة HRP

> **BR-HR-01..18** — كل قاعدة موثقة بنص المصدر.

---

## BR-HR-01 — تعدد إيقاعات الدورة (Category Cal Method)
**القاعدة:** كل فئة موظفين تمتلك إيقاع معالجة مستقلاً (Daily/Weekly/Fortnightly/Monthly) تحدده Category Code وتُبنى نافذته في Starting Period.
**النص:** "The period mentioned will depend on the method of calculation... daily, weekly, monthly, fortnightly which is already pre-defined for categories using the category code" (SET §9).
**الأثر:** Payroll Run لا يكون حدثاً واحداً في الفندق — بل **مجموعة أحداث متزامنة حسب الفئات** (WF-HR-05 يُستدعى لكل Category).

## BR-HR-02 — احتكار الفترة للتقارير والقيود
**القاعدة:** كل التقارير والقيود اليدوية والقروض تُعالج حصراً ضمن فترة Starting Period للفئة.
**النص:** "All the reports will be based on the period specified here only. Transactions entered manually or Loan amounts posted for any Date will be processed for that period only" (SET §9).

## BR-HR-03 — حساب To Date الأربعة
**القاعدة:** Daily: To=From · Weekly: +7 · Fortnightly: +15 · Monthly: تقويمية إن كانت From أول الشهر وإلا شهر متدحرج (21-Dec→20-Jan).
**النص:** موثق حرفياً بأمثلة التواريخ (SET §9 ص14).

## BR-HR-04 — مصفوفة الأعلام الخمسة للحضور
**القاعدة:** دلالة كل Attendance Code تُشتق من 5 أعلام (Leave/Paid/Hourly/Wrkday) وفق المصفوفة الموثقة (Sick/CL/PL/Vacation=Y,Y,N,N · Absent=Y,N,N,N · Overtime=N,Y,**Y**,N · Working=N,Y,N,**Y**) — Hourly يحوّل القيمة من أيام إلى ساعات.
**المصدر:** SET §7 (جدول كامل).

## BR-HR-05 — أهلية ED بالشهور والتراكم
**القاعدة:** ED Calculation قد يُقيَّد بشهور معينة (Specific Months) بنمط تكديس: Month (كل شهر مستقل) / Cumulative (يتراكم من بداية السلسلة) / **Cumulative C/O (يتراكم مع نقطة تهيئة — PF YTD لا يُهيأ، ضريبة الدخل تُهيأ سنوياً مالياً)**.
**النص:** أمثلة SER1/SER2 الرقمية + "PF YTD... not initialized as long as the employee is with the organization. But Income tax must be initialized every financial Year" (SET §10 ص19).

## BR-HR-06 — أولوية الخصومات والخصم الجزئي والترحيل
**القاعدة:** تُخصم الخصومات بترتيب Priority (F3 لإعادة الترتيب)؛ إذا تجاوز الخصمُ الأرباحَ: Partial=Yes → الخصم الكامل رغم العجز / No → **لا يُخصم شيء**؛ Carry Forward=Yes → الباقي يُرحَّل ويُخصم بأولوية الشهر التالي / No → **تتبع يدوي**.
**النص:** أمثلة 1500/1700 الرقمية (SET §10 ص17).

## BR-HR-07 — صمام Take Home %
**القاعدة:** الفئة تحدد حداً أدنى مئوياً من الإجمالي يصل الموظف مهما كانت الخصومات (20% → الخصومات على 80%)؛ فارغ → الخصم الفعلي الكامل؛ 100% → لا خصومات.
**النص:** "minimum salary (in terms of percentage) that the employee will get, irrespective of the total deductions being greater than the earnings" (SET §8 ص12).

## BR-HR-08 — مطابقة التقريب الثلاثية
**القاعدة:** Net Pay يُقرَّب على مستوى الفئة بـ Nearest/Highest/Lower إلى Round Amount (مثال: 2516.65 → 2516.50/2517.00/2516) — ومستوى ED Calculation أيضاً (None/Higher/Lower/Nearer).
**المصدر:** SET §8 + SET §10.

## BR-HR-09 — قاعدة تبادل Print Sequence
**القاعدة:** رقم تسلسل الطباعة قابل للمشاركة بين earning وdeduction، لكن **يُمنع** مشاركته بين deduction types مختلفة.
**النص:** "a print sequence assigned to a code categorized under a one-deduction type cannot be assigned to another deduction type" (SET §5 ص8).

## BR-HR-10 — أهلية Accept بشرط الحضور
**القاعدة:** القيم المدخلة وقت المعالجة (Accept مثل FDA) لا يستفيد منها الموظف إلا "if the employee is present for at least one day. (One day of attendance)".
**النص:** SET §10 ص17.

## BR-HR-11 — تجميد ملفات المغادرين
**القاعدة:** لا يمكن تعديل بيانات الموظف الموقوف/المستقيل/المسرَّح — التعديلات قبل تغيير الحالة فقط.
**النص:** "You cannot modify suspended/resigned or terminated employee details" (PNT §3).

## BR-HR-12 — قفل أصل القرض
**القاعدة:** المبلغ الأصلي للقرض غير قابل للتعديل بعد الإنشاء — كل التسويات عبر Loan Return Entry (بما فيها تعديل الشروط في قسم Modify).
**النص:** "Once the principal loan amount is entered in the Loan master it cannot be changed" (PNT §21).

## BR-HR-13 — توقيت إصدار القرض
**القاعدة:** تاريخ إصدار القرض يجب أن يكون ضمن شهر المعالجة (وإلا يُسحب إلى تاريخ المعالجة تلقائياً).
**النص:** "The issue date should be in between the processing Month. By default the issue date will change to Processing Date" (PNT §20).

## BR-HR-14 — الحد الأدنى لحضور الإدخال
**القاعدة:** Attendance Entry فردي حصراً ("single employee at a time") وPost Default فردي-الكود فئوي ("single attendance for category wise") + الأيام ≤ نطاق الفترة.
**المصدر:** PNT §5-6 (Notes).

## BR-HR-15 — Bonus الرباعي بحد القطع
**القاعدة:** أربع نسب مكافأة منفصلة (موجودون ≤ cutoff / موجودون > cutoff (مثال 7500) / مغادرون ≤ / مغادرون >) + إلزام إعادة احتساب PT اختياري عند تغير الراتب + استثناء موظفين (Bypass).
**المصدر:** PNT §18.

## BR-HR-16 — تعويق تعديل طلب التوظيف
**القاعدة:** في Job Requirements لا يُعدَّل إلا Authentication status وRemarks.
**النص:** "The user can modify only the authentication status and Remarks information" (RQP §1).

## BR-HR-17 — نمط تفعيل INI المعكوس (220)
**القاعدة:** مجموعة إجازات الموظفين تُفعَّل بضبط INI 220 = **0** (لا 1!) — رابع وثيقة نمط "0=ممكن" (بعد AR 56/74).
**المصدر:** SET §15.

## BR-HR-18 — إقفال/إلغاء الدورة المتدرج
**القاعدة:** إقفال الرواتب أو إلغاؤها يتم على مستوى Property+Category+**Dept/CC/Grade** — أي يمكن إقفال قسم معالَج وإبقاء آخر مفتوحاً.
**المصدر:** PNT §11 ("Select the department/cost center/grade at which the payroll processing should be cancelled/closed").

---

## عائلات القواعد العابرة للوحدات
- **عائلة التجميد الثلاثية→الرباعية:** FO يومي (Night Audit) · FAS سنوي (FY) · MGT شهري (Store Ledger) · **HRP فئوي-قسمي (Closing)** — كل وحدة تشغيلية تملك بوابة تجميد.
- **عائلة Applicable From:** Grade/Template/HOD/Branch/EDCalc ≥ اليوم — مطابقة SYS.
- **عائلة INI المعكوسة:** 56/74/**220**.
- **عائلة التقريب الثلاثي:** SYS (عملة) + HRP Category + HRP ED — نفس الأسماء الثلاثة.
