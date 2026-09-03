# 07 — الصلاحيات (Permissions) — وحدة HRP

> نموذج الصلاحيات في HRP: **Payroll User Rights الفئوي** فوق النموذج الرباعي العام (SYS) — طبقة خامسة فريدة: **نطاق بيانات على مستوى فئة الموظفين**.

---

## 1. Payroll User Rights (SET §23) — ⭐ الموثق الوحيد داخل الوحدة

| البند | الموثق |
|---|---|
| المانح | "the **supervisor-user** can grant access rights" — قناة Supervisor (الطبقة 1 من نموذج SYS) |
| الممنوح | "different User ids" — اختيار من قائمة User IDs (double-click) |
| **نطاق المنح** | "to different **employee groups**" = Categories — **Row-level security بمعايير فئوية** |
| آلية الاستخدام | "Double click in the Option column corresponding to **Category** which the user wants to give rights (the column then appears **YES**)" — تفعيل عمودي |
| الحفظ | Save |

**الدلالة المعمارية:** هذا هو الوحيد الموثق في الحزمة الذي يمنح **وصولاً شرطياً بالبيانات** (فئة الموظفين) لا بالوظائف فقط — يتقاطع مع:
- نموذج SYS الرباعي (Supervisor→Admin→User→ACL لكل قائمة).
- تقييد التقارير في SYS (report restrictions).

## 2. مصفوفة الأدوار التشغيلية المستنتجة من المتن

| الدور | الوصول الموثق/المستنتج | المصدر |
|---|---|---|
| **Supervisor-User** | منح Payroll Rights + الإعدادات كلها | SET §23 + طبيعة Setup |
| **HR Department** | RQP كاملاً (فرز الطلبات: "HR department scrutinizes") + Personnel Master + Leave | RQP §3 + PNT |
| **HOD** | Job Requirements (طلب تعيين) + HOD Status (قائمة المرشحين) | RQP §1/§4 + SET §11 |
| **Interview Panel** | Interview Status حصراً | RQP §6 |
| **Payroll Officer** | Attendance/Transaction/Processing/Closing/Statements | PNT عموماً |
| **Employee (self-service)** | ❌ لا وجود موثق — Payslip Printing موظف-عدة فقط | REP §11 |
| **Auditor** | Payroll Audit Report (Modified/Deleted بقيم old/new) | REP §19 |

## 3. حساسيات الصلاحيات (Risk Register)

| الحساسية | السبب | القرار |
|---|---|---|
| **ACCEPT وقت المعالجة** | إدخال مبالغ تُطبَّق على فئة كاملة | تقييد دور Payroll Officer + تسجيل audit |
| **Change Employee Status** | يفتح/يغلق التسوية النهائية | موافقة ثنائية مستحسنة (غير موثقة) |
| **Closing/Canceling** | تجميد/إلغاء دورة مالية | صلاحية مستقلة عالية |
| **Payroll Audit** | يكشف تعديلات تاريخية | دور Auditor |
| **Number Deduction Updation** | تعديل أرقام PF/ESI جملة | صلاحية محدودة |
| **Print sequence + ED engine** | يعيد تشكيل الرواتب | Setup role + Applicable From |

## 4. الإسقاط إلى Frappe

| الأصل | الهدف | القرار |
|---|---|---|
| Payroll User Rights | **User Permission** على Category/Employee Group + Role Profile | مباشر — Frappe يدعم row-level permissions |
| Supervisor granting | Role "Payroll Supervisor" + permission to manage User Permissions | F-HR-11 |
| تقييد التقارير | Report Permission Query / shared filters | من SYS |
| لا self-service | **Employee Self-Service في HRMS يفتح الجديد** (سلايب/إجازات إلكترونية) — إضافة قيمة لا استنساخ | قرار تصميمي (GAP موجب) |
