# 03 — كتالوج الشاشات (Screens Catalog) — وحدة HRP

> **79 شاشة تشغيلية** (SET 29 + PNT 34 + RQP 16) + **68 تقريراً** (REP — تفصيلها في 08-reports). الأولويات وفق الأثر على الإسقاط إلى ERPNext.

---

## A. Setup (29 شاشة)

| # | الشاشة | المصدر | الأولوية | ملاحظات UX |
|---|---|---|---|---|
| S-HR-01 | Bank Definition | SET §1 | P2 | نمط CRUD بسيط + F1 |
| S-HR-02 | Branch Code Definition (+Folio ledger sub) | SET §2 | P2 | شاشة شرطية عند Folio=Yes |
| S-HR-03 | Language Definition | SET §3 | P2 | |
| S-HR-04 | Grade Definition | SET §4 | P1 | From/To + Type/Amount |
| S-HR-05 | ED Code Definition | SET §5 | **P0** | محرك الأجور |
| S-HR-06 | Attendance Code Definition | SET §6 | P1 | |
| S-HR-07 | Property Attendance Definition | SET §7 | **P0** | مصفوفة 5 أعلام |
| S-HR-08 | Category Code Definition | SET §8 | **P0** | Cal Method + Take Home% + Round |
| S-HR-09 | Define Starting Period (+Preview) | SET §9 | **P0** | نافذة الدورة |
| S-HR-10 | ED Calculation Definition | SET §10 | **P0** | ⭐ الأغنى — انظر الشجرة أدناه |
| S-HR-10a | → Select Months | SET §10 ص18 | P0 | منتقي شهور |
| S-HR-10b | → Source Details | SET §10 ص18-20 | P0 | Accumulation + Source ED + Subtract |
| S-HR-10c | → Calculate Equation (+Test) | SET §10 ص21 | **P0** | ⭐ معادلة تفاعلية |
| S-HR-10d | → Table Details (Slabs) | SET §10 ص22-24 | **P0** | ⭐ 4 أنواع |
| S-HR-11 | HOD Definition | SET §11 | P1 | F1 موظفون |
| S-HR-12 | Statutory Deduction Defn. (4 tabs) | SET §12 | P1 | PF/ESI/PT/LWF |
| S-HR-13 | Define Salary Template | SET §13 | P1 | قالب عرض |
| S-HR-14 | Bonus Period Definition | SET §14 | P1 | |
| S-HR-15 | Leave Group Parameter | SET §15 | P1 | INI 220 |
| S-HR-16 | Leave Details Parameter | SET §16 | P1 | Post day |
| S-HR-17 | Costing Group Definition | SET §17 | P2 | |
| S-HR-18 | Denomination Definition | SET §18 | P2 | قيم تنازلية |
| S-HR-19 | Staff Budget Definition | SET §19 | P2 | |
| S-HR-20 | User Defined Report Definition | SET §20 | P2 | Formula + Check |
| S-HR-20a | → Create Formula | SET §20 ص37 | P2 | |
| S-HR-21 | User Defined Print Forms | SET §21 | P2 | مصمم طباعة (F4 Property!) |
| S-HR-22 | Payroll User Rights | SET §23 | **P0** | أمن فئوي |

## B. Payroll Entries (34 شاشة)

| # | الشاشة | المصدر | الأولوية | ملاحظات |
|---|---|---|---|---|
| S-HR-23 | Personnel Master (search→record) | PNT §1 | **P0** | من RQP |
| S-HR-23a | → Personal Information | PNT §1 ص5 | P0 | |
| S-HR-23b | → Salary calculation method | PNT §1 ص6 | **P0** | |
| S-HR-23c | → Account numbers (PF A/C) | PNT §1 ص7 | P0 | |
| S-HR-24 | Direct Employee Entry (+Asset Info sub) | PNT §2 | P0 | عهدة أصول! |
| S-HR-25 | Change Employee Info (search) | PNT §3 | P0 | قيد الحالات |
| S-HR-26 | Rate Master Definition (+Show Details+Address+Copy) | PNT §4 | **P0** | ⭐ |
| S-HR-27 | Attendance Entry | PNT §5 | **P0** | موظف واحد فقط! |
| S-HR-28 | Post Default Attendance | PNT §6 | P1 | فئوي |
| S-HR-29 | Attendance Post Interface | PNT §7 | P1 | Enterprise Only |
| S-HR-30 | Payroll Transaction (ED-wise/Category-wise + Tag More) | PNT §8 | **P0** | F2 copy/F3 paste |
| S-HR-31 | Supplementary Entries (PF/ESI/PT tabs) | PNT §9 | P1 | خارج الرواتب |
| S-HR-32 | **Payroll Processing** (+ACCEPT screen) | PNT §10 | **P0** | ⭐ سيد الوحدة |
| S-HR-33 | Closing/Canceling Process | PNT §11 | **P0** | Cancel/Closed |
| S-HR-34 | Change Employee Status | PNT §12 | P0 | |
| S-HR-35 | Leave Master (Opening balances) | PNT §13 | P1 | Closing auto |
| S-HR-36 | Leave Transaction (F5/F6!) | PNT §14 | P1 | يوم كامل/نصف |
| S-HR-37 | Leave Posting to Payroll | PNT §15 | P1 | |
| S-HR-38 | Bonus Extraction from Pay | PNT §16 | P1 | Extraction/Cancel |
| S-HR-39 | Bonus Master/Supplementary | PNT §17 | P1 | |
| S-HR-40 | Bonus Processing (4 نسب + RT PT) | PNT §18 | P1 | ⭐ |
| S-HR-41 | Closing Bonus | PNT §19 | P1 | |
| S-HR-42 | Loan Master | PNT §20 | P1 | أصل مقفل |
| S-HR-43 | Loan Return Entry (Return+Modify) | PNT §21 | P1 | |
| S-HR-44 | **AR to Payroll Transfer** (+company code link) | PNT §22 | **P0** | ⭐ جسر AR |
| S-HR-45 | Number Deduction Updation (F8) | PNT §23 | P1 | شاشة جملة |
| S-HR-46 | **Full And Final Settlement** (+Attendance+Amount+Print) | PNT §24 | **P0** | Indemnity |

## C. Requirement Process (16 شاشة)

| # | الشاشة | المصدر | الأولوية |
|---|---|---|---|
| S-HR-47 | Job Requirements | RQP §1 | P1 |
| S-HR-48 | Application Details | RQP §2 | P1 |
| S-HR-48a | → Qualification / Experience / Reference / Language / Passport (5 subs) | RQP §2 ص6-10 | P1 |
| S-HR-49 | Application Status | RQP §3 | P1 |
| S-HR-50 | HOD Status | RQP §4 | P1 |
| S-HR-51 | Interview Date (+Add details) | RQP §5 | P1 |
| S-HR-52 | Interview Status | RQP §6 | P1 |
| S-HR-53 | Offer Letter (+ED details + Salary Template F1) | RQP §7 | **P0** |
| S-HR-54 | Offer Letter Status (+additional info) | RQP §8 | P1 |

## D. أنماط UX الموثقة

| النمط | الدليل | الدلالة التصميمية |
|---|---|---|
| **شاشة إدخال وقت المعالجة (ACCEPT)** | PNT §10: "While the processing is happening, you will get the following screen with a list of ED codes, where you can enter the amount" | Wizard step ديناميكي في Payroll Run |
| **اختصارات لوحة مفاتيح كثيفة** | F1 (استعراض) في كل مكان · F2 copy/F3 paste (Transaction) · **F3 تغيير أولوية الخصومات** · F5/F6 إجازة كاملة/نصف · **F8 معلومات إضافية** (Number Deduction) · **F4 خصائص الحقل** (Print Forms) | خريطة اختصارات تُصمم RTL |
| **مصفوفة أعلام 5×ن** | Property Attendance | جدول قرارات قابل للإسقاط |
| **Test Equation** | Equation builder | تحقق فوري قبل الحفظ — يُستبدل بـ formula validator |
| **Preview button** | Starting Period | معاينة الفترات قبل الحفظ |
| **Copy button** | ED Calculation + Rate Master | استنساخ التعريفات — نمط ERPNext القياسي |
| **شاشة مطالبة تعيين الرقم** | PNT §1: "The system will prompt you to assign an employee number" | auto-suggest numbering |
| **قيد "موظف واحد"** | Attendance Entry: "The user will be allowed to enter Attendance for single employee at a time" | ⚠️ يُستبدل بـ bulk entry + import |
