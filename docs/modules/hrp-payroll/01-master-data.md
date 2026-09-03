# 01 — البيانات الرئيسية (Master Data) — وحدة HRP

> جرد الكيانات المرجعية الـ 50 الموثقة في HRP-SET/PNT/RQP مع الحقول والقيود والمصادر. النمط العام: كود قصير (1-10 خانات alphanumeric) + Long Name (30) + Short Name (10) + خاصية Applicable From الإصدارية (نفس عائلة SYS/MGT).

---

## A. المرجعيات المصرفية والهوية

### 1. Bank Definition (SET §1)
| الحقل | القيد/القيمة | ملاحظات |
|---|---|---|
| Bank Code | 3 خانات alphanumeric | F1 للاستعراض — "used extensively across the payroll module" |
| Long Name | 3-30 خانة، إلزامي | اسم البنك |
| Short Name | 3-10 خانات، إلزامي | |
| Address/Email/Contact | عنوان ≥3 خانات إلزامي | + فاكس |

- سلوك: Add/Modify/Delete/Browse حر ("You can modify, delete or browse any records") — **بلا Applicable From** (استثناء لعائلة الإصدارية!).

### 2. Branch Code Definition (SET §2)
| الحقل | القيد/القيمة | ملاحظات |
|---|---|---|
| Applicable From | تاريخ | إصداري |
| Property code | قائمة | |
| Bank Code | F1 | الأب |
| Branch code | إدخال | |
| Long/Short Name | 3-30/3-10 إلزامي | |
| **Folio Required** | Yes → شاشة إدخال "ledger and account numbers... helps the bank to maintain a set of ledger numbers for the employees of each organization" | **ربط أرقام حسابات البنك برواتب الموظفين** |

### 3. Language Definition (SET §3)
| الحقل | القيد |
|---|---|
| Language Code | 1-3 alphanumeric إلزامي |
| Name | 3-30 إلزامي |
| Short Name | 3-10 إلزامي |

- الغرض: "guests might be fluent in many languages... how many languages the employee is familiar with so as to provide better services to the guests" — **غرض خدمة ضيوف لا HR داخلي!**

## B. هيكل التوظيف والتصنيف

### 4. Grade Definition (SET §4)
| الحقل | القيد/القيمة |
|---|---|
| Applicable from | ≥ تاريخ اليوم (افتراضي: اليوم) — **مستقبلي فقط** (عائلة SYS) |
| Grade | كود فريد |
| Long/Short Name | 3-30/3-10 |
| Serial number | ترتيب |
| From amount / To amount | نطاق راتب الدرجة |
| Type | **Percentage/Amount** (نوع العلاوة) |
| Amount | قيمة العلاوة |

- "salary range for which the increment can be calculated" — الدرجة نطاق مالي بعلاوة.

### 5. Category Code Definition (SET §8) — ⭐ العمود الفقري للدورة
| الحقل | القيد/القيمة | الدلالة |
|---|---|---|
| Property code | قائمة | |
| Category code | ≤10 alphanumeric | |
| **Cal Method** | Daily/Monthly/Weekly/Fortnightly | **إيقاع الدورة** |
| Description/Short | 30/10 | Executive مثلاً |
| **Take Home %** | فارغ أو 0-100 | صمام الأمان (BR-HR-07) |
| Work hours | ساعات يوم | يرتبط بـ Hourly Flag |
| Round type | Nearest/Highest/Lower | تقريب Net Pay |
| Round Amount | مثال موثق: 2516.65 + .50 → Nearest=2516.50 / Highest=2517.00 / Lower=2516 | **مطابق حرفياً لـ SYS Round Off** |

### 6. HOD Definition (SET §11)
| الحقل | القيد |
|---|---|
| Applicable from | ≥ اليوم |
| Property + Department code | قوائم |
| HOD code | **رقم موظف** (F1 من قائمة الموظفين!) |

- ربط القسم برئيسه = Employee.

### 7. Staff Budget Definition (SET §19)
| الحقل | الدلالة |
|---|---|
| Property/Category/Department | نطاق |
| Designation | "For eg. You might need more Bell captains" |
| Budget | "number of personnel required" |
| Grades | درجات المعينين |

- يغذي **Staff Cadre Report** (REP §17.11: "list of variance by department and designation wise for the budgets defined").

## C. محرك الأجور (ED Engine)

### 8. ED Code Definition (SET §5) — ⭐⭐
| الحقل | القيد/القيمة | ملاحظات |
|---|---|---|
| ED Code | 1-3 alphanumeric | |
| Name/Short name | 3-30/3-10 | |
| **ED type (6)** | Earning · Regular Deduction · Loan Deduction · Number Deduction · Temporary · Cumulative YTD | التعريفات الموثقة: Earning=Basic+OT+Bonus+Travel+Medical؛ Regular=Professional Tax؛ Loan=سداد شهري؛ **Number=PF/ESI/LIC "A reference number is assigned... Fortune refers to these deductions with that number"**؛ Temporary="dummy XYZ calculation; this will not affect the salary"؛ Cumulative YTD="Cumulative PF / Income Tax for a Year to Date" |
| Print sequence | ترتيب في payslip — **قاعدة التبادل**: "print sequence assigned to an earning code can be assigned to a deduction code... But... a print sequence assigned to a code categorized under a one-deduction type cannot be assigned to another deduction type" (BR-HR-09) |
| **Employer number** | "Each company will have a PF, ESI number" — للخصومات المشتركة: "half the amount is deducted from employee's salary and the employer contributes the other half" | **بنية صاحب عمل/موظف مزدوجة** |

### 9. ED Calculation Definition (SET §10) — ⭐⭐⭐ الأغنى
الرأس:
| الحقل | القيم | الدلالة |
|---|---|---|
| Applicable from / Property / Category / Calc. Method (auto) / Cal Code (6 خانات فريد + F1) / Description / **Copy button** (نسخ تعريف ED آخر!) | | |
| **Arrears Flag** | Yes/No | "employee is having arrear days for the previous month and it has to be used for salary computation" — الأجور بأثر بأسعار "the month selected" |
| **Calculation Type (3)** | Payroll (يطبع في Payslip — wages يُضاف وإلا يُخصم) / **Annual** ("Bonus is given only once in a year") / **Temporary** (وسيط: مثال موثق: بدل تعريف المعادلة الكاملة تُعرّف (worked+paid+sick)/total ثم Basic × Temporary) | |
| **Calculate From (4)** | **None** (معادلة/XY مثل HRA% من Basic) / **Master** (من Rate Master: مثال Basic المثبت × أيام/إجمالي حسب Cal Method) / **Accept** (قيمة من المستخدم وقت المعالجة لكل الفئة — مثال FDA + شرط "employee should be present for at least one day"!) / **Transaction** (مبالغ Payroll Transaction — "positive or negative" للتعديلات!) | |
| **Priority Number** | خصومات فقط | "order in which deductions are made... If you specify this number as 1... Fortune deducts this amount first" + **F3 لإعادة الترتيب** ("Press F3 to change Priority Order") |
| **Partial Deduction** | Yes/No (خصومات) | مثال موثق: Earnings 1500 / Deductions 1700 → Yes="the entire 1700 is deducted" (!) / No="no amount is deducted" — **سلوك قطعي بين الطرفين** |
| **Carry Forward** | Yes/No (خصومات) | Yes="carried forward and deducted as a priority" / No="required to keep track of the outstanding amount and manually deduct it" |
| **Specific Months** | Yes → منتقي شهور | مثال موثق: Feb/May/Aug/Nov |
| **Gross Amount** | Yes/No | "first equation... is for a Gross Amount... If Yes then the Gross Amount will return to the tables, otherwise Gross Amount does not get updated in Gross Tables" |
| **Special Program ID** | مثال موثق: **PYINDSP** — "This code is only for Indian clients" — يفحص أهلية ESI الشهرية | **خطاف برنامج خارجي في التعريف!** |

Source Details (بعد اختيار الشهور):
| الحقل | القيم | مثال موثق (SER1/SER2!) |
|---|---|---|
| **Accumulation Type** | Month / Cumulative / **Cumulative C/O** | Month: 5% × 1000 = 50 لكل شهر؛ Cumulative: "basic amount for January also gets accumulated... 5% × 2000 = 100"؛ **C/O**: "PF YTD must be printed but not initialized as long as the employee is with the organization. But Income tax must be initialized every financial Year" |
| **Source ED Code** | ED آخر | SER2 يعتمد SER1 |
| **Subtract Flag** | Yes/No | مثال: SER2 التراكمي = 200(SER1 حتى مارس) − 150 = **50.00** |

**Equation Builder**: 4 أعمدة (ED Codes / Attendance / Operators / Numbers) + **Test Equation button** — مثال Basic: `BASIC Amount x Worked days / Total number of days in the month`.

**Table Details (الشرائح 4 أنواع)**:
| النوع | المنطق | المثال الرقمي الموثق (2500) |
|---|---|---|
| From/To Amount + Type (Amount/Percentage/Rate) + Amount + Min/Max clamp | | |
| **Normal** | شريحة واحدة مطبقة كاملة | 2500 → شريحة 3 → 20% = **500.00** |
| **Cumulative** | تقسيم عبر الشرائح | 1000×10% + 1000×15% + 500×20% = **350** |
| **Step Over** | "selects the slab which **precedes** the actual slab... remaining amount... next slab" | 2000×15% + 500×20% = **400** |
| **Eligibility Check** | Type=Eligible/Not Eligible — **تعطيل Amount/Min/Max** | ESI: ≤6500 Eligible / >6500 Not — "ESI slabs are set as per the government norms" |

### 10. Rate Master Definition (PNT §4) — تعرفة الموظف
الحقول: Date + Property + Employee# (+**Copy button** لنسخ بنية تعرفة) + Show Details + Address · **Designation/Grade#/Department Code/Cost Center/Calculation Method/Calculation Code** · شبكة ED Codes للفئة مع المبالغ · **Leave Group** · **PF Calculation Yes/No + VPF Calculation + Amount** · قسم Salary Breakup بإجمالي يمين الشاشة.

### 11. Define Salary Template (SET §13) — قوالب ما قبل التعيين
| الحقل | القيد |
|---|---|
| Applicable from | ≥ اليوم |
| Property | |
| Salary Template # | ≤10 خانات |
| Description + Serial (auto) | |
| ED code + Name (auto) + **Amount** | "starting salary that the candidate will be offered based on the position for which the candidate is being interviewed" |

- الغرض: "At the time of the interview the HR needs this option to select a fixed salary that is applicable to all candidates... templates that can be posted to Payroll after the selection is made. The details specified within the template can be changed at a later date" — **قالب عرض وظيفي**.

### 12. Statutory Deduction Definition (SET §12) — 4 تبويبات إجرائية
| التبويب | الحقول الموثقة |
|---|---|
| **Provident Fund** | Applicable from + PF code + **FPF EDCODE** (Family Pension) + **VPF code** (Voluntary) + Minimum pensionable gross + Pension % + Round off + Calculating % + **Administrative charges + E.D.L.I. charges + EDLI admin charges** ("as per government rules") |
| **ESI** | ESI code + **Employers' Share %** + Round off amount/type + ESI % |
| **Professional Tax** | code + **Print Program Id** |
| **Labour Welfare Fund** | code + Employers' share + Print Program ID |

## D. الحضور والإجازات

### 13. Attendance Code Definition (SET §6)
| الحقل | القيد |
|---|---|
| Attendance code | **"1 or 3 digit code"** |
| Name/Short name | 10 خانات للأقصى |

### 14. Property Attendance Definition (SET §7) — ⭐ المصفوفة الحاكمة
| الحقل | الدلالة |
|---|---|
| Property + Attendance Code (F1) + Leave Code Y/N + Consider Pay Days Y/N + Hourly Flag Y/N + Is It Wrkday Y/N | |

**المصفوفة الموثقة حرفياً (BR-HR-04):**
| Attendance Code | Leave | Paid | Hourly | Wrkday |
|---|---|---|---|---|
| Sick/Casual/Privilege/Vacation | YES | YES | NO | NO |
| Absent/Loss of Pay | YES | NO | NO | NO |
| Overtime | NO | YES | **YES** | NO |
| Working/Present | NO | YES | NO | **YES** |

- Hourly Flag: "YES... calculate the value as number of **hours**... NO... as number of **days**, as fed in the Attendance entry".

### 15. Leave Group Parameter (SET §15)
Property + Group code (F1) + Start/End Date — **التفعيل: INI 220 = 0** — "define eligibility of Leave for a particular group... executive group can avail 12 leaves per year and... managers group can avail 10".

### 16. Leave Details Parameter (SET §16)
Property + Category + Group code + From/To Date + **Post day** ("posting monthly or otherwise") — "If they have not availed any leave that was entitled to them the previous year, it can be carried forward".

## E. الفترات والتكلفة والصرف

### 17. Define Starting Period (SET §9) — ⚡ قلب الدورة
Property + Category + Calculation Method + **Preview button** ("details of Periods for different categories") + From date → To date محسوبة:
- Daily: To=From ("Daily Wages")
- Weekly: +7 أيام
- Fortnightly: +15 يوماً
- Monthly: تقويمية إن بدأت بأول شهر (01-Jan→31-Jan)، وإلا **21-Dec-2010→20-Jan-2011**
- "Transactions entered manually or Loan amounts posted for any Date will be processed for that period only" + إقلاع أول: "The system will take the date range from next month onwards".

### 18. Costing Group Definition (SET §17)
Property + Date MM/YY + **Department/Cost center/Grade/Employee (نوع التجميع)** + Group code + Long Name + اختيار من اليمين — "snapshot of how much of salary was spent on a particular group".

### 19. Denomination Definition (SET §18)
Property + Category + **Currency** (روبية/دولار) + Conversion + **Notes/Coins labels سياقية** + **Values تنازلية** ("descending order starting from the highest value") — "The system usually checks for the first value and calculates accordingly to provide the denomination statement, which lists the net pay of employees, split denomination wise" — **للنقد فقط**.

## F. الموظف والمرشح (كيانات PNT/RQP)

### 20. Personnel Master / Employee (PNT §1-2) — ⭐
- مسار مزدوج: من RQP (candidate accepted) أو **Direct Employee Entry** ("details of existing employees... or when a candidate is taken into job without going through the Recruitment process").
- شاشات فرعية: Personal Information · Salary calculation method · **Account numbers (PF A/C!)** · **Asset Information** (Direct فقط — أصول عهدة الموظف!).
- **Employee# = numeric ≤7 خانات** يُعيَّن عند الحفظ بمطالبة ("The system will prompt you to assign an employee number").
- الحالة: On Roll افتراضياً → Change Employee Status (resigned/retired/terminated + effective date + reason).
- القيد: "You cannot modify suspended/resigned or terminated employee details" (BR-HR-11).

### 21. Candidate/Application (RQP §2)
الحقول: Job Code (الأب) + Complete name + DOB + Birth Place + Father's Name + Gender + Marital Status + Nationality + Religion + **Caste and Classification (SC/ST/OBC!)** + Residential/Permanent Address + **Qualification + Experience + Reference + Language + Passport** (5 مجموعات فرعية).

### 22. Loan Master (PNT §20)
Property + Employee# + **ED Code** (F1) + Issue date (تلقائي — "should be in between the processing Month... will change to Processing Date") + Loan number + **Principal Amount + No of installments (→ Installment Amount auto)** + **Interest: Payment Type / Amount-Percentage / Amount** — **الأصل غير قابل للتعديل بعدها**.

### 23. Full & Final Settlement (PNT §24)
Date of Leaving + Status + **Indemnity Calculation Y/N** + Attendance entry للشهر + Amount + **نوعا الطباعة: Final Settlement / Vacation Settlement**.

## G. سجل التدقيق

### 24. Payroll Audit Records (REP §19)
Report type + Property + Date range + **Audit types: Modified and/or Deleted** + Old/New values — "employee related records (Report Wise)".

---

## خلاصة القيود العابرة للوحدات
- **عائلة Applicable From:** Grade/Salary Template/HOD/Branch/ED Calculation (≥ اليوم) — تتطابق مع نمط SYS (مستقبلي فقط)؛ **استثناء Bank Definition** بلا إصدارية.
- **عائلة Long/Short Name:** (3-30/3-10) موحدة عبر البنك/الفرع/اللغة/الدرجة/الفئة/ED.
- **الكودات القصيرة:** Bank 3 · Language 1-3 · ED 1-3 · Attendance 1-3 · Category ≤10 · Salary Template ≤10 · Cal Code 6 · EMP# 7 numeric.
- **Round Off الثلاثي** (Nearest/Highest/Lower) مطابق لنمط SYS بأمثلة رقمية متطابقة البنية (2516.65).
