# 14 — نموذج البيانات (Data Model) — وحدة HRP

> **50 كياناً** موثقاً + العلاقات + قيود التصميم. الأسماء وفقاً للتسمية الأصلية، والإسقاط في 16.

---

## A. ER — المجموعات الخمس

```
┌─ المرجعيات ─────────────────────────────────────────┐
│ BANK ──< BRANCH(folio ledger/accounts)               │
│ LANGUAGE ──< EMPLOYEE_LANGUAGE >── EMPLOYEE          │
└──────────────────────────────────────────────────────┘
┌─ هيكل التوظيف ──────────────────────────────────────┐
│ PROPERTY >── GRADE(from/to/type/amount)              │
│ PROPERTY >── CATEGORY(cal_method/takehome/round/hours)│
│ CATEGORY ──< STARTING_PERIOD(from→to)                │
│ DEPARTMENT >── HOD ── EMPLOYEE                       │
│ PROPERTY/CATEGORY ──< STAFF_BUDGET(designation/budget)│
└──────────────────────────────────────────────────────┘
┌─ محرك الأجور ───────────────────────────────────────┐
│ ED_CODE(type6/printseq/employer#)                    │
│ PROPERTY/CATEGORY >── ED_CALCULATION(cal_code6)      │
│   ├─ flags: arrears/calc_type3/calc_from4/priority/  │
│   │         partial/carryfwd/specific_months/gross   │
│   ├─ SOURCE_DETAILS(acc3/src_ed/subtract)            │
│   ├─ EQUATION(tokens) [testable]                     │
│   ├─< SLAB(from/to/type3/amt/min/max) [4 types]      │
│   └─ special_program(PYINDSP)                        │
│ SALARY_TEMPLATE ──< TEMPLATE_ED(ed_code, amount)     │
└──────────────────────────────────────────────────────┘
┌─ الحضور/الإجازات ────────────────────────────────────┐
│ ATTENDANCE_CODE ──< PROPERTY_ATTENDANCE(5 flags)     │
│ EMPLOYEE ──< ATTENDANCE_ENTRY(code, days/hours)      │
│ LEAVE_GROUP(INI220) ──< LEAVE_DETAILS(category,post) │
│ EMPLOYEE ──< LEAVE_BALANCE(prev/curr→closing)        │
│           ──< LEAVE_TRANSACTION(dates, F5/F6)        │
└──────────────────────────────────────────────────────┘
┌─ المعاملات ──────────────────────────────────────────┐
│ EMPLOYEE ──< RATE_MASTER(ed amounts, leave grp, PF)  │
│ PAYROLL_RUN(category, period, status)                │
│   ├─< PAYSLIP(ed lines, net, rounded)                │
│   ├─ ACCEPT_VALUES(ed, amount)                       │
│ EMPLOYEE ──< PAYROLL_TRANSACTION(ed, amt, remarks)   │
│           ──< SUPPLEMENTARY(pf/esi/pt tabs)          │
│           ──< LOAN(principal, installments, interest)│
│                └─< LOAN_RETURN(amt, interest, modify)│
│ CATEGORY ──< BONUS_PERIOD(months, bonus_ed, ded_ed)  │
│           ──< BONUS_RUN(4 pct, RT PT, bypass)        │
│ EMPLOYEE ──< AR_DEDUCTION_LINK(company code)         │
│           ──< F&F_SETTLEMENT(DOL, indemnity, print)  │
│ JOB_REQ ──< APPLICATION ──< INTERVIEW ──< OFFER      │
│ DENOMINATION(notes/coins values) COSTING_GROUP       │
│ PAYROLL_AUDIT(report, old/new, M/D)                  │
└──────────────────────────────────────────────────────┘
```

## B. جرد الكيانات (50)

| # | الكيان | المفتاح | الحقول الجوهرية | المصدر |
|---|---|---|---|---|
| 1 | Bank | code(3) | names/address | SET §1 |
| 2 | Branch | prop+bank+code | folio_required, ledger/accounts | SET §2 |
| 3 | Language | code(1-3) | name | SET §3 |
| 4 | Grade | code | from/to amount, type, amount, serial | SET §4 |
| 5 | ED Code | code(1-3) | type(6), print_seq, employer_no | SET §5 |
| 6 | Attendance Code | code(1-3) | name | SET §6 |
| 7 | Property Attendance | prop+code | leave/paid/hourly/wrkday | SET §7 |
| 8 | Category | prop+code(10) | cal_method, takehome%, hours, round type/amt | SET §8 |
| 9 | Starting Period | prop+cat | from, to(computed), cal_method | SET §9 |
| 10 | ED Calculation | prop+cat+cal_code(6) | 12+ حقلاً (BR-HR-05/06) | SET §10 |
| 11 | Source Details | calc | acc_type(3), src_ed, subtract | SET §10 |
| 12 | Equation | calc | tokens | SET §10 |
| 13 | Slab Row | calc+seq | from/to, type(3), amount, min, max, slab_type(4) | SET §10 |
| 14 | HOD | prop+dept | employee_no | SET §11 |
| 15 | Statutory PF Def | prop | pf/fpf/vpf codes, %, pension, admin, edli×2 | SET §12 |
| 16 | Statutory ESI Def | prop | code, employer_share, % | SET §12 |
| 17 | Statutory PT Def | prop | code, print_pgm | SET §12 |
| 18 | Statutory LWF Def | prop | code, employer_share, print_pgm | SET §12 |
| 19 | Salary Template | #≤10 | description, serial | SET §13 |
| 20 | Template ED | template+ed | amount | SET §13 |
| 21 | Bonus Period | prop+cat | months, bonus_ed, deduction_ed | SET §14 |
| 22 | Leave Group | prop+grp | dates | SET §15 |
| 23 | Leave Details | prop+cat+grp | from/to, post_day | SET §16 |
| 24 | Costing Group | prop+mm/yy | group_type(4), code | SET §17 |
| 25 | Denomination | prop+cat+curr | conversion, notes[], coins[] | SET §18 |
| 26 | Staff Budget | prop+cat+dept | designation, budget, grades | SET §19 |
| 27 | UDR Definition | report# auto | paper(80/132), headers, cols, formula | SET §20 |
| 28 | Print Form Project | name | layout rows (6=1"), toolbox, logo | SET §21 |
| 29 | Payroll User Rights | user×category | yes | SET §23 |
| 30 | Employee | emp#(7N) | status, personal, salary method, pf_ac, assets | PNT §1-2 |
| 31 | Rate Master | emp+date | designation/grade/dept/cc/cal, ED amounts, leave grp, PF/VPF | PNT §4 |
| 32 | Attendance Entry | emp+date+code | days(5,2) | PNT §5 |
| 33 | Attendance Interface File | filename | EMP/DATE/CODE/DAYS | PNT §7 |
| 34 | Payroll Transaction | emp+ed+date | amount, remarks | PNT §8 |
| 35 | Supplementary | emp+month | pf/esi/pt amounts + days paid | PNT §9 |
| 36 | Payroll Run | prop+cat+period | order, status(Closed/Cancel) | PNT §10-11 |
| 37 | Accept Value | run+ed | amount | PNT §10 |
| 38 | Payslip | run+emp | ED lines, gross, net(rounded) | PNT §10/REP §11 |
| 39 | Leave Balance | emp+year | prev/curr opening, closing | PNT §13 |
| 40 | Leave Transaction | emp+date | type(F5/F6) | PNT §14 |
| 41 | Bonus Extraction | prop+cat | cutoff gross | PNT §16 |
| 42 | Bonus Run | prop+cat | 4 pct, round, RT_PT, bypass[] | PNT §18 |
| 43 | Loan | emp+loan# | principal, installments, inst_amt, interest type/amt | PNT §20 |
| 44 | Loan Return | loan+date | return amt, interest, modify terms | PNT §21 |
| 45 | AR Deduction Link | emp+company code | transfer state | PNT §22 |
| 46 | F&F Settlement | emp | DOL, status, indemnity, attendance, amount, print type | PNT §24 |
| 47 | Job Requirement | job code | type, requisition, status, auth | RQP §1 |
| 48 | Application | app# | بيانات المرشح + 5 مجموعات | RQP §2 |
| 49 | Interview / Offer | app# | dates/status/offer+template | RQP §5-8 |
| 50 | Payroll Audit Record | report+date | old/new values, M/D flag | REP §19 |

## C. قيود تصميم النموذج (Design Constraints)

| # | القيد | الأثر |
|---|---|---|
| C-HR-1 | **الإيقاع لكل فئة:** Payroll Run ليست شهرية عموماً — الفترة تابع Category | الجدولة: تشغيل متعدد متزامن |
| C-HR-2 | **الإقفال الحبيبي:** حالة (Period × Category × Dept/CC/Grade) | مصفوفة حالة معقدة |
| C-HR-3 | **ED التعريفات إصدارية (Applicable From)** بلا نهاية موثقة | temporal versioning |
| C-HR-4 | **المعادلات مخزنة كبنود (tokens)** قابلة للاختبار | Formula DSL + sandbox |
| C-HR-5 | **الشرائح نوع/Min/Max** — أربع عائلات حسابية مختلفة | محرك واحد بأربعة أوضاع |
| C-HR-6 | **Employee# ≤7 أرقام** | يعاد ترقيمه في المنصة الجديدة (recode map) |
| C-HR-7 | **أرقام PF/ESI مرجع خصم (Number Deduction)** | حقل مرجع على مستوى الموظف×ED |
| C-HR-8 | **Non Employee** فئة بملف أقل (Supplementary فقط) | نطاق كيان موسّع أو كيان مستقل |

## D. التطبيع مقابل الكيانات المرجعية العابرة

| الكيان المشترك | الوحدات المشاركة | القرار |
|---|---|---|
| Employee | HRP + SYS (User؟) + BNQ (Staff) + FO/POS (Staff settlement) | **كيان Employee واحد مركزي** مع تمثيلات |
| Department/Cost Center | HRP + MGT + FAS + FO | من FAS المرجع |
| Bank/Branch | HRP + FAS (ChequeBook) | موحّد |
| Property | كل الوحدات | SYS Company |
