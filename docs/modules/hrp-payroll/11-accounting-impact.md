# 11 — الأثر المحاسبي (Accounting Impact) — وحدة HRP

> **18 حدثاً مالياً** (E$-HR) + بنية الترحيل إلى FAS (الرابط السادس الموثق من طرف FAS-SET) + الانقسامات الإجرائية موظف/صاحب عمل.

---

## 1. الأحداث المالية الموثقة/المستنتجة بثقة

| # | الحدث | الطبيعة | التفصيل الموثق |
|---|---|---|---|
| **E$-HR-01** | **Payroll Processing (الاحتساب)** | التزام | نتائج المعادلات — Gross (Earnings) − Deductions = Net (مع Take Home% clamp) — *الترحيل موثق ضمن روابط FAS الستة (Payroll→Finance)* |
| **E$-HR-02** | **Deduction بالأولوية** | توزيع خصم | Priority order + Partial + Carry Forward — **الخصم قد يكون صفراً أو كاملاً رغم العجز** (BR-HR-06) |
| **E$-HR-03** | **Take Home % clamp** | حماية صافي | 20% مثلاً → "deductions will be made on the remaining 80%" — **إعادة توزيع خصم** غير محاسبية النص لكنها تغير Net |
| **E$-HR-04** | **Round Off للصافي** | تسوية | Nearest/Highest/Lower إلى Round Amount (2516.65/.50) — **فرق تقريب** يجب أن يُرحَّل لحساب Round-off (مطابق نمط SYS) |
| **E$-HR-05** | **Supplementary PF/ESI/PT** | التزام خارج الدورة | "payments made outside payroll" — إجماليات تدخل التقارير الإجرائية دون المرور بالمعالجة |
| **E$-HR-06** | **PF split موظف/صاحب عمل** | انقسام | "half the amount is deducted from employee's salary and the employer contributes the other half" + Admin + EDLI + EDLI admin charges — **أربعة مكونات تحميل صاحب عمل!** |
| **E$-HR-07** | **ESI Employer share %** | تحميل | "Employers' Share %" في التعريف الإجرائي |
| **E$-HR-08** | **LWF employer share** | تحميل | تعريف LWF |
| **E$-HR-09** | **Arrears (الأثر الرجعي)** | تسوية فترات | Arrears Flag + Report type Arrears + "rates applicable in the month selected" — **احتساب بأثر بأثر رجعي سعري** |
| **E$-HR-10** | **Unrealized** | التزام معلّق | Report type ثالث موثق (Regular/Unrealized/Arrears) — مكونات لم تتحقق |
| **E$-HR-11** | **Bonus processing** | مصروف | 4 نسب + **"Recalculate Professional Tax" — إعادة احتساب ضريبة كاملة بسبب تغير الوعاء** |
| **E$-HR-12** | **Bonus Deduction code للمغادرين** | استقطاع | "though the bonus is calculated, there will be a deduction" (Bonus Period) |
| **E$-HR-13** | **Loan issuance** | أصل/خصم | Principal + Interest (Payment Type: Amount/Percentage) — خصم ED Loan Deduction شهرياً |
| **E$-HR-14** | **Loan Return (مبكر/إضافي)** | تسوية | Return amount + interest — خارج القسط الدوري |
| **E$-HR-15** | **AR→Payroll deduction** | تصفية مديونية | AR settled → خصم من الراتب (PNT §22) — **يوثق القيد المقابل لـ POS Staff Settlement/FO Paid Out من طرف المدين** |
| **E$-HR-16** | **Disbursement (Cash/Bank/Cheque/Draft/Transfer)** | صرف | "Option includes all, cash, bank, drafts and transfers... pay mode for each employee, which is specified in personnel master" — **5 قنوات صرف** |
| **E$-HR-17** | **PF/ESI Challan** | سداد حكومي | Cash/Cheque/Draft بتفاصيل (Bank+A/C Group#+Cheque#/تاريخان+Establishment Code+Depositor) |
| **E$-HR-18** | **Full & Final (+Indemnity/Vacation)** | تسوية ختامية | Amount صافٍ + طباعة Final/Vacation Settlement |

## 2. بنية الترحيل إلى FAS — الرابط السادس

> الرابط موثق من طرف FAS-SET (روابط الترحيل الستة: FO/POS/MM/Payroll/Membership→Finance + AR→Finance). من طرف HRP تظهر القرائن:
> - قنوات الصرف الخمس + تفاصيل الشيكات/الحوالات (Statements/Challans).
> - **Costing Group Definition**: "snapshot of how much of salary was spent on a particular group" بتجميع Dept/CC/Grade/Employee — **بُعد التوزيع المحاسبي** للرواتب (يقابل Department/Cost Center في FAS).
> - Denomination (النقد) = بُعد الخزينة.
> - [UNCERTAIN] **JV النمطي التفصيلي لقيد الرواتب** (Debit Salary Expense/Credit Bank أو Accrued) **غير موثق نصاً في HRP** — يُستكمل من FAS-TRN عند المرحلة 6 (Accounting). يُسجَّل **QA-HR-1**.

## 3. مصفوفة القنوات المالية

| القناة | التعريف | الأدلة |
|---|---|---|
| Cash | Pay mode في Personnel Master + Denomination | Statements §2.5 + SET §18 |
| Bank | Branch folio (ledger/account numbers للموظفين) | SET §2 |
| Cheque | Cheque# + تاريخان + A/C Group# | Challan §13.7 |
| Draft | Draft# + مثله | Challan §13.7 |
| Transfer | ضمن Options | Statements §2.5 |

## 4. أسئلة محاسبية معلقة (→ Phase 6)

| # | السؤال | المسار |
|---|---|---|
| QA-HR-1 | قيد JV التفصيلي لمعالجة الرواتب (نمط المدين/الدائن) | FAS-TRN المرحلة 6 |
| QA-HR-2 | معالجة الفرق بين Unrealized والـ Suspense في FAS | مقارنة أنماط |
| QA-HR-3 | توقيت اعتراف مساهمة صاحب العمل (عند الاحتساب أم السداد) | تصميم |
| QA-HR-4 | أثر Cancel بعد Closed على القيود المرحّلة | نمط FAS Rollback |

## 5. الأحداث المالية العابرة للوحدات (تتغذى من HRP)

- **POS/BNQ Staff Settlement → AR → AR to Payroll** (E$-HR-15) — الحلقة الرابعة المغلقة.
- **BNQ Banquet Staff/Service Managers** — كيان موظف مشترك.
- **FAS Report "Payroll" posting link** — الرابط السادس.
