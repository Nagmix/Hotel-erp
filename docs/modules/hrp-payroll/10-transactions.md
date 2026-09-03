# 10 — المعاملات وسلاسل المستندات (Transactions) — وحدة HRP

> سلاسل مستندات الدورة الكاملة + حالة كل مستند + دورة الإقفال الفئوية (عائلة التجميد الرابعة).

---

## 1. سلسلة التوظيف (Recruitment Chain)

```
Job Requirement (REQ#)
  └─ Application (APP#) [Status: HR status → HOD Shortlist → Interview Date → Interview Status → Offer]
       └─ Offer Letter (+ Salary Template + ED amounts)
            └─ [Accepted] → Personnel Master (EMP# ≤7) → On Roll
```
- **حالات الطلب:** Application Status (فرز HR) → HOD Status (Short Listed/Not) → Interview Status → Offer Status (+Remarks).
- **حالات الوظيفة:** Closed/Progress/Pending + Authentication date/#.

## 2. سلسلة الموظف (Employee Chain)

```
Personnel/Direct Entry (EMP#) [On Roll]
  ├─ Rate Master (Designation/Grade/Dept/CC + ED amounts + Leave Group + PF/VPF)
  │    └─ [تعديلات] → Emp. Rate Master List "Updated" يرصدها
  ├─ Asset Info (عهدة — Direct Entry فقط)
  ├─ [Status change] (resigned/retired/terminated + date + reason) → [مجمد]
  └─ Full & Final Settlement (DOL + Indemnity Y/N + Attendance + Amount) → Print Final/Vacation
```

## 3. سلسلة الدورة الشهرية (Payroll Cycle Chain)

```
Starting Period (Property+Category+From) → [نافذة]
  ├─ Attendance Entry / Default / Interface (EMP,DATE,CODE,DAYS)
  ├─ Payroll Transaction (EMP+ED+Amount+Remarks [+Tag More])
  ├─ [ACCEPT values وقت المعالجة]
  ▼
Payroll Processing (Property+Category+Order All/Grade/Dept)
  ├─ [احتساب: Equations → Slabs → Priority → Partial/CF → TakeHome% → Round]
  ├─ Payslips (طباعة)
  └─ Salary Abstract/Details (مراجعة)
       ▼
Closing/Canceling Process [Closed | Cancel] (Property+Category+Dept/CC/Grade)
       ▼
Disbursement: Statements (All/Cash/Bank/Drafts/Transfers) + Denomination + Payslip
```

**حالات دورة الرواتب (مستنتجة من الوظائف الموثقة):**
| الحالة | الدخول | الخروج | المصدر |
|---|---|---|---|
| **Open** (قيد معالجة) | Starting Period | Processing | PNT §10 |
| **Processed** | Processing | Closing | PNT §10-11 |
| **Closed** (مجمدة) | Closing | (تقارير فقط) | PNT §11 |
| **Cancelled** (معاد فتحها) | Cancel | إعادة المعالجة | PNT §11 |

## 4. سلاسل فرعية

### 4a. الإجازات
```
Leave Group (INI 220) → Leave Details (Category+Post day)
Leave Master (Prev/Current Opening → Closing auto)
Leave Transaction (تواريخ — F5 كامل/F6 نصف)
Leave Posting to Payroll (Attendance Code موازٍ → "automatically deduct availed leaves")
```

### 4b. المكافآت
```
Bonus Period (Category+Months+Bonus ED+Deduction ED)
Bonus Extraction [Extraction|Cancel] → (gross cutoff)
Bonus Master/Supplementary (تعديلات)
Bonus Processing [Process|Cancel] (+4 نسب + PT recalc + Bypass)
Closing Bonus (إقفال النوع)
```

### 4c. القروض
```
Loan Master (Loan#+Principal+Installments+Interest) [الأصل مقفل]
  ├─ خصم شهري عبر ED Loan Deduction
  ├─ Loan Return (تاريخ/مبلغ/فائدة)
  └─ Modify (تعديل شروط — عبر Return Entry!)
```

### 4d. AR→Payroll
```
AR settled (موظف مدين) → AR to Payroll Transfer (Load → company code link) → خصم دورة تالية
```

### 4e. Supplementary
```
PF/ESI/PT مدفوعات خارج الرواتب (Month/Year + Employee/Non-Employee + تبويبات)
```

## 5. دورة الإقفال — عائلة التجميد الرابعة

| الوحدة | بوابة التجميد | النطاق | القيد الموثق |
|---|---|---|---|
| FO | Night Audit (Open New Date) | يومي | "no postings" أثناء Guest Balance |
| FAS | Open Financial Year/Rollback | سنوي | — |
| MGT | Physical→Variance→Store Ledger | شهري (مخزن) | Cancel آخر فقط |
| **HRP** | **Closing/Canceling** | **فئة+قسم/CC/درجة** | Cancel = إعادة فتح؛ Closed = نهائي |

> ⚠️ **حالة حدية E-HR-24:** الإقفال الحبيبي (قسم دون آخر) يجعل "الفترة" مفهوماً مركباً — عند الإسقاط يجب تمثيل الحالة على مستوى (Period × Category × Org Unit) وليس Period فقط.

## 6. أحداث آلية موثقة (A-HR)

| # | الحدث | المحفّز | المصدر |
|---|---|---|---|
| A-HR-01 | حساب Installment Amount | إدخال Principal+Installments | PNT §20 |
| A-HR-02 | سحب Issue date إلى Processing Date | خارج الشهر | PNT §20 |
| A-HR-03 | Closing auto في Leave Master | إدخال Opening | PNT §13 |
| A-HR-04 | خصم الإجازات المستحقة | Leave Posting + Attendance Code | PNT §15 |
| A-HR-05 | تعبئة بيانات المرشح في Personnel Master | قبول Offer | PNT §1 |
| A-HR-06 | To date محسوبة | From date + Cal Method | SET §9 |
| A-HR-07 | نطاق سنة تلقائي في Prob/Conf report | إدخال تاريخ البدء | REP §1.9 |
| A-HR-08 | سنة كاملة تلقائية في PF Reconciliation | From Month | REP §13.8 |
| A-HR-09 | Min/Max clamp للشريحة | نتيجة خارج النطاق | SET §10 |
| A-HR-10 | fallback عنوان general table في Form 3A | فراغ Register#/Company | REP §13.1 |
