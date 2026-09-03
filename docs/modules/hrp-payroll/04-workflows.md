# 04 — سير العمل (Workflows) — وحدة HRP

> **WF-HR-01..17** موثقة خطوة بخطوة من المتن، مع الشاشة المنفذة والقاعدة الحاكمة في كل خطوة.

---

## WF-HR-01 — دورة الموظف الكاملة (Employee Lifecycle)
1. **(اختياري مسار RQP)** Job Requirements → Applications → Offer accepted (WF-HR-14).
2. **Personnel Master** (S-HR-23): استعراض المرشح المقبول ("Details of the candidate who has accepted the offer will be displayed") → تعديل → Personal Info → Salary method → PF A/C → Save.
3. النظام **يطالب بتعيين Employee#** (رقمي ≤7) → تأكيد.
4. **Rate Master** (S-HR-26): Designation/Grade/Dept/CC/Cal Code + مبالغ ED + Leave Group + PF/VPF.
5. الحالة = **On Roll**.
6. (لاحقاً) Change Employee Status (resigned/retired/terminated + تاريخ + سبب).
7. **Full & Final Settlement** (S-HR-46): Date of Leaving + Status + Indemnity Y/N → Attendance للشهر → Amount → طباعة Final/Vacation.
- *بديل:* Direct Employee Entry (بلا RQP) + **Asset Information** (عهدة).

## WF-HR-02 — تهيئة محرك الأجور (ED Engine Setup)
1. ED Code Definition (النمط 6 + Print seq + Employer#).
2. ED Calculation Definition: Applicable/Property/Category → Cal Code (**Copy** إن وجد مثيل) → Arrears Flag → Calculation Type (3) → Calculate From (4).
3. إن كان خصماً: Priority + Partial Deduction + Carry Forward.
4. Specific Months؟ → منتقي الشهور → Source Details (Accumulation: Month/Cumulative/C-O + Source ED + Subtract).
5. **Equation** (ED Codes × Attendance × Operators × Numbers) → **Test Equation** → OK.
6. جدولي؟ → Table Type (Normal/Cumulative/Step Over/Eligibility) + الشرائح (From/To/Type/Amount/Min/Max) → Confirm لكل شريحة → Go Back → Save.

## WF-HR-03 — إقلاع الدورة الشهرية (Period Bootstrap)
1. Category Code (Cal Method + Take Home% + Round) — مرة واحدة.
2. **Define Starting Period**: Property + Category + From date → To date محسوبة (BR-HR-05) → **Preview** للتحقق.
3. أول تشغيل فقط: "The system will take the date range from next month onwards".
4. كل دورة: Attendance + Transactions تُقيَّد ضمن "that period only".

## WF-HR-04 — الحضور الشهري (Attendance Cycle)
1. يدوياً: **Attendance Entry** (موظف واحد): Property → Employee → Attendance type → الأيام لكل كود → Confirm → Save.
2. أو جملة: **Post Default Attendance** (فئة + كود + أيام ≤ نطاق التاريخ) — "single attendance for category wise".
3. أو خارجياً: **Attendance Post Interface** (فئة → Read من `PYATYYMM.DAT`) — مواصفات الملف: EMP(7),DATE(8),CODE(3),DAYS(5,2) بفواصل.
4. الأعلام تفسّر الأيام عبر **مصفوفة Property Attendance** (BR-HR-04) — Hourly=OVT بالساعات.

## WF-HR-05 — معالجة الرواتب (Payroll Processing) — ⭐ سيد الدورة
1. Property + **Category** + ترتيب المعالجة (**All/Grade/Department**).
2. **Process** → أثناء الاحتساب: شاشة **ACCEPT** (كل ED ذي Calculate From=Accept — إدخال المبلغ للفئة كلها).
3. المحرك ينفذ: المعادلات بالأولوية → الشرائح → Take Home% clamp → التقريب (Round type/Amount).
4. المراجعة: Salary Abstract / Abstract Details / Transaction Check List.
5. تصحيحات: Payroll Transaction إضافية أو Attendance تعديل — **داخل الفترة فقط**.
6. **Closing/Canceling Process**: Cancel (إعادة فتح) أو **Closed** (تجميد نهائي) — على مستوى Property+Category+Dept/CC/Grade.

## WF-HR-06 — الصرف (Disbursement)
1. بعد Closed: **Statements** (REP §2.5): Property + Category + فترة + **Option: All/Cash/Bank/Drafts/Transfers** (من Pay mode في Personnel Master) + Amount/By Master + Order by (Dept/Grade/CC/Emp/Ac#).
2. نقداً: **Denomination** statement (كسر النقد من Definition SET §18).
3. بنكياً: Branch folio (ledger/account numbers) + كشوف.
4. **Payslip Printing**: Paymode + Order + user definition.

## WF-HR-07 — الإجازات (Leave Cycle)
1. Leave Group Parameter (INI 220=0) + Leave Details (فئة + Post day).
2. **Leave Master**: Previous/Current Opening → Closing auto.
3. **Leave Transaction**: F5 يوم كامل / F6 نصف يوم على التواريخ.
4. **Leave Posting to Payroll**: Property + Category + **Attendance Code** (نوع اليوم الموازي) → "automatically deduct availed leaves".

## WF-HR-08 — المكافآت (Bonus Cycle)
1. Bonus Period Definition (فئة + Start/End Month + Bonus ED + Deduction code للمغادرين!).
2. **Bonus Extraction from Pay**: Extraction/Cancel — استخلاص الإجمالي "the cutoff amount to calculate the bonus".
3. تصحيحات: Bonus Master/Supplementary (Gross/Bonus/Pay mode).
4. **Bonus Processing**: Bonus Process/Cancel + Round + **4 نسب** (Ext Bon %/Ext Exg %/Left Bon %/Left Exg %) + **Recalculate PT** + Bypass Employees.
5. **Closing Bonus** (إقفال النوع).
6. تقارير: Details/Cash-Bank/Slip/Form-C/Suppl/PT Calc/Exgratia.

## WF-HR-09 — القروض (Loan Cycle)
1. **Loan Master**: Property + Employee + ED Code + Loan# + **Principal + Installments** (القسط auto) + Interest (Type/Amt-%).
2. الخصم الشهري يمر عبر ED type=Loan Deduction بأولويته.
3. عوائد مبكرة/إضافية: **Loan Return Entry** (تاريخ/مبلغ/فائدة) — **الأصل مقفل**.
4. تعديل شروط: قسم Modify في Return Entry.
5. تقارير: Checklist/Statement/Return/Month-wise.

## WF-HR-10 — خصومات AR (AR to Payroll Transfer) — ⭐
1. موظف يشتري (POS Staff Settlement / FO Paid Out) → **AR** (مديونية موظف).
2. **AR to Payroll Transfer**: Category → **Load** (استعراض السجلات) → عرض ED Code (زر).
3. ربط **company code** بالموظف (double-click) → تظهر على سجله.
4. Save → يصبح خصماً في دورة الرواتب التالية.

## WF-HR-11 — التوظيف (Recruitment)
1. HOD يرسل طلباً → **Job Requirements**: Job Code/Description/Type (Contract/Regular/Temporary) + Property + Dept + Requisition (date/#/period/description — "Permanent" أو عدد الأشهر!) + Mode of Advert + Status (Closed/Progress/Pending) + Authentication date/# + Remarks.
2. **Application Details**: Job Code + بيانات المرشح الكاملة (هوية + عنوانان + 5 مجموعات).
3. **Application Status**: HR فرز ("scrutinizes each application, shortlists those applications fitting the job description") → الحالة.
4. **HOD Status**: Short Listed / Not Short Listed.
5. **Interview Date**: إسناد التواريخ.
6. **Interview Status**: لجنة المقابلات تحدّث.
7. **Offer Letter**: التفاصيل + **Salary Template (F1)** + Earn/Dedu codes + المبالغ + Confirm.
8. **Offer Letter Status**: رد المرشح + Remarks.
9. (قبول) → **Personnel Master** (WF-HR-01 خطوة 2).

## WF-HR-12 — التعديلات الضخمة (Bulk Maintenance)
- **Number Deduction Updation**: جدول كل الموظفين — تعديل PF/CIT/ESI أرقام جملة + **F8** معلومات إضافية — "instead of making changes to each employee in the change info screen".
- **Post Default Attendance** (فئة).
- Change Employee Info (فردي).

## WF-HR-13 — المدخلات الإجرائية الخارجية (Supplementary)
1. مدفوعات PF/ESI/PT خارج الرواتب → **Supplementary Entries**: Property + **Employee or Non Employee** + Month/Year + Employee#.
2. تبويبات: PF (Days Paid + Gross + PF + VPF) → ESI (Days/Gross/ESI) → PT (Gross/PT) → Save.
3. التقارير: Supplementary Check List (REP §5).

## WF-HR-14 — التسوية النهائية (Full & Final)
1. الموظف مغادر → S-HR-46.
2. Date of Leaving + Status + **Indemnity Calculation Y/N**.
3. Attendance entry للشهر الأخير (شاشة داخلية).
4. Amount (المستحق الصافي) → OK.
5. Print → **Final Settlement أو Vacation Settlement** → توليد التقرير.

## WF-HR-15 — التدقيق (Audit)
1. **Payroll Audit Report**: Report type + Property + فترة + Modified/Deleted.
2. استعراض old/new values لكل سجل معدّل/محذوف.

## WF-HR-16 — قالب الراتب في المقابلة (Offer-time Salary)
1. Define Salary Template (ED codes + مبالغ البداية).
2. عند Offer Letter: **F1 على Salary Template** → ربط القالب بالمرشح + تعديل المبالغ.
3. عند التعيين: "templates that can be posted to Payroll after the selection is made".

## WF-HR-17 — تقرير معرّف ذاتياً (UDR)
1. User Defined Report Definition: Report # auto + Name + Paper (80/132) + Headers (L/C/R) + أعمدة من Tool Box + **Formula** (+ Check) + Column Detail + Break & Sort.
2. User Defined Report (REP §18): Report # → Print.

---

## مصفوفة الاعتماد (Dependency Matrix)

| WF | يعتمد على | يغذّي |
|---|---|---|
| 01 الموظف | RQP (11) أو مباشر | 05/07/08/09/14 |
| 02 محرك ED | ED Codes (S-05) | 05 |
| 03 الإقلاع | Category | كل الدورة |
| 04 الحضور | 03 + مصفوفة الأعلام | 05 |
| 05 المعالجة | 02+03+04+Transactions | 06+11 |
| 06 الصرف | 05 Closed | FAS (ترحيل) |
| 07 الإجازات | INI 220 + Leave Setup | 04/05 |
| 08 المكافآت | Bonus Period + 05 | 11 (PT recalc) |
| 09 القروض | ED Loan type | 05 |
| 10 AR Transfer | AR settled | 05 |
| 11 التوظيف | Job Req | 01 |
| 14 التسوية | 01 (Left) | AR/Bank (صرف نهائي) |
