# 08 — التقارير (Reports) — وحدة HRP

> **19 مجموعة / 68 تقريراً** موثقة في HRP-REP (133 ص — أضخم ملف تقارير في الحزمة بعد FO-REP). الأنماط الموحدة: Property+Category+فترة+Order by (Dept/Grade/CC/Emp#) + 80/132 عموداً.

---

## 1. Employee Information (9 تقارير — REP §1)

| # | التقرير | الخصوصية الموثقة |
|---|---|---|
| 1.1 | **Employee Lookup** | تفاصيل موظف بـ Property+Emp# + تنقل Prev/Next — **الـ LUK الوحيد فعلياً** |
| 1.2 | Employee Personal Info | On Roll/Left + Grouping (Grade/DepCode/CC/Emp#) |
| 1.3 | Designation and Salary List | **Fixed أو Earned** ("Earned salary will be calculated on the days he worked") + Consolidated + Skip Rows + Remarks |
| 1.4 | Birthday/Anniversary | Employees/Spouse/Children/All + Both + Order by Date |
| 1.5 | Signature List | عنوان مخصص + **Include Net Pay اختياري!** + Skip Lines |
| 1.6 | Service/Retirement/DOJ | معايير الخدمة/DOJ/DOL/DOB |
| 1.7 | Passport/Visa/Work Permit | **All أو By Date (Expiry!)** — أهلية إقامة |
| 1.8 | Blood Grp/Staff/Place | معلومات طوارئ |
| 1.9 | Prob/Conf/Increment | "The system will calculate one year from the date you enter and auto populates the end date" — نافذة سنة تلقائية + Probationary/Confirmation/Increment Status |

## 2. Payroll Reports (10 — REP §2)

| # | التقرير | الخصوصية |
|---|---|---|
| 2.1 | Salary Abstract | ملخص E/D للجميع + **Report type: Regular/Unrealized/Arrears** + 80/132 |
| 2.2 | Salary Abstract Details | +Summary + **Actual Gross Req./Detailed Paid days** |
| 2.3 | Dept. Payroll Summary | By Department/By Employee |
| 2.4 | Pay Roll Summary | **Print Unrealized Amt** اختياري + sort Dept/Code |
| 2.5 | Statements | **All/Cash/Bank/Drafts/Transfers** (Pay modes!) + Amount/By Master + إجمالي لكل قسم + Grand Total |
| 2.6 | Earnings Reconciliation | **variance between current and previous gross** + % + لكل ED أو Gross فقط + "Print Gross Modified Employees" |
| 2.7 | Consolidate Salary | group/grade/CC/Emp |
| 2.8 | E/D Statement | كود E/D محدد |
| 2.9 | E/D Statement – Month Range | مقارنة شهرية + إجمالي شهري/قسمي/عام |
| 2.10 | Earning Deduction Summary | Summary By options |

## 3-5. Disbursement + Group + Supplementary (REP §3-5)

| التقرير | الخصوصية |
|---|---|
| **Disbursement Statement** | تفاصيل الصرف للفئة والفترة |
| **Group Abstract – Dept/Cost** | snapshot تكلفة القسم + **"Show Bank Payment Separately"** |
| **Supplementary Check List** | **Employee/Non Employee/Both** × **PF/ESI/PT** + Month range |

## 6. Attendance (5 — REP §6)

| التقرير | الخصوصية |
|---|---|
| 6.1 Attendance Check List | **Regular/Arrears/Both** + "Select Fixed Amount" (ذوو الراتب الثابت نفسه) + userId المسجِّل |
| 6.2 Attendance Month Range | **12 شهراً** + **صيغة رياضية للمستخدم**: "(WRK + PL + SL) − (ABS + Calendar days)" — **حاسبة أكواد مخصصة!** |
| 6.3 Attendance Code List | Applicable/List |
| 6.4 Attendance Detailed List | + Double Line Spacing |
| 6.5 Attendance Worksheet | Order + Skip lines |

## 7-11. Transactions + Leave + Payslip (REP §7-11)

| التقرير | الخصوصية |
|---|---|
| Transaction Check List | ED code + **User name من F1** + userId في التقرير — **تتبع مسؤول** |
| Transaction Worksheet | تفصيل المعاملات |
| Leave Transaction List | الإجازات المستحقة |
| **Leave Ledger Report** | أرصدة الإجازات المتاحة |
| **Payslip Printing** | Paymode + Order + **user definition** (قوالب UDR!) |

## 12. Statutory (5 — REP §12)

| التقرير | الخصوصية |
|---|---|
| 12.1 Statutory Report | PF/ESI/LWF/PT + **Merge VPF to EPF (Employee)** + **Merge EPF Difference to EPF (Employer)** + Include Non Employee + تفكيك مساهمات موظف/صاحب عمل |
| 12.2 EPF/ESI/PT Summary | Details/Summary + Dept/CC/Grade |
| 12.3 Gratuity Report | **As on date + ED Code + range of service years + Max Service Years** + On Roll/Left |
| 12.4 PT Exemption List | المعفون من PT |
| 12.5 Number Deduction List | أرقام PF/ESI + Emp Total Required |

## 13. Provident Fund Reports (9! — REP §13)

| النموذج | الخصوصية الموثقة |
|---|---|
| **Form 3A** | **Non Contributing Days (+/- selective!)** + Club VPF/EPF + Register#/Company address (وإلا من general table) + **Create DBF File!** (تصدير دوس!) + Include Non Employee/Summary |
| Form 5 | Address1/2 + Register# اختيارية |
| Form 6A | Merge VPF/EPF × 2 + **بواسطة PF# أو EMP#** |
| Form 9 | بسيط |
| Form 10 | بسيط |
| **Form 12A** | + Bank name |
| **PF Challan** | **3 أنواع دفع**: Cash (Establishment Code+Depositor) / Cheque (Bank+A/C Group#+Cheque#+تاريخان) / Draft (مثل الشيك بـ Draft#) |
| PF Reconciliation | سنة كاملة تلقائية ("It takes a year range") + Register# |
| **E.D.L.I Charge List** | قائمة مشتركي EDLI + Report List selector |

## 14. E.S.I. Reports (6 — REP §14)
Form 3 · Form 5 · Form 7 · Exemption List · **ESI Challan** · **ESIC Reconciliation** (Month range).

## 15. Loan (4 — REP §15)
Checklist (+Loan type) · Statement (All/نوع + Selection + **opening/collection/closing + interest**) · Return Statement (+installments + balance) · Month-wise (+On Roll/Left).

## 16. Bonus (7 — REP §16)
Details List (gross/net) · Cash/Bank Statement · **Slip (+Message بحث نصي: "Performance Bonus"!)** · **Form C** (+Payment Date) · Suppl. Check List · **PT Calculation** (+Total/Subtotal) · **Exgratia Prov. List** (Bonus+Ex gratia+Grand Total).

## 17. Master Reports (11 — REP §17)
Bank Details (Active/List + All/Range) · Grade List (Applicable/List) · HOD List (Active/List + Dept) · Category Code List (+Cal Method) · **Emp. Rate Master List** (All/Updated — "whose salary/cost center/department/grade has been modified"!) · **Standard Rate Master List** (ملف كامل: father's name/DOB/DOJ/basic/HRA/mode/PF#/ESI#/total) · E/D List (All/Selected) · Calculation Defn. List (List/Active) · Salary Template List (Applicable/List + All/Range STP#) · **Employee Paid By Cash** (+Display/Summary) · **Staff Cadre Report** (variance للميزانية!).

## 18-19. UDR + Audit (REP §18-19)
| التقرير | الخصوصية |
|---|---|
| User Defined Report | Report # → Process/Print |
| **Payroll Audit Report** | **Report type dropdown + Modified and/or Deleted + old/new values** — "all employee related records (Report Wise) that have been either modified or deleted" |

---

## أنماط التقارير الموحدة (Report Conventions)

| النمط | القيم | الدلالة |
|---|---|---|
| نطاق الفترة | Date range أو Month range (MM/YY) | ملتزم بـ Starting Period (BR-HR-02) |
| Report type (الرواتب) | **Regular/Unrealized/Arrears** | ثالوث موثق ثلاث مرات (Abstract/Details/Dept Summary + Attendance: Regular/Arrears/Both) |
| Order by | Dept/Grade/Cost Center/Emp# (+A/C# في الإجرائية) | موحد |
| الورق | 80/132 عموداً | محطة Impact قديمة → تُستبدل بـ HTML/A4 |
| تصدير | **Create DBF File** (Form 3A) | **تنسيق دوس!** — يُستبدل CSV/XLSX |
| userId في المخرجات | Check Lists (Attendance/Transaction) | مساءلة — يُستبدل بـ owner/modified_by |
| Include Non Employee | الإجرائية | فئة "غير الموظفين" (متقاعدون/متعاقدون خارج الدورة؟) — [UNCERTAIN] تعريفها الدقيق غير موثق |

## أولويات إعادة البناء

| الأولوية | التقارير | السبب |
|---|---|---|
| P0 | Payslip (قوالب) · Salary Abstract/Details · Statements · Disbursement · Leave Ledger | التشغيل اليومي |
| P1 | Statutory core · Earnings Reconciliation · Attendance Check List · Transaction Check List · Loan Statement · Bonus Details | دورة شهرية |
| P2 | نماذج PF/ESI الرسمية (9+6) · UDR/Audit · Master Lists · مواسمية (Birthday) | إجرائية/دورية |
