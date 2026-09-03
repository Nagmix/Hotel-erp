# 06 — التحققات (Validations) — وحدة HRP

> **V-HR-01..30** + مصفوفة الرسائل — كل تحقق موثق من المتن.

---

## A. تحققات الإدخال (Field-level)

| # | التحقق | القاعدة | المصدر |
|---|---|---|---|
| V-HR-01 | Bank Code | 3 خانات alphanumeric | SET §1 |
| V-HR-02 | Long/Short Name (كل المرجعيات) | ≥3 خانات إلزامي؛ ≤30/≤10 | SET §1-8 |
| V-HR-03 | Language/ED Code | 1-3 alphanumeric إلزامي | SET §3/§5 |
| V-HR-04 | Attendance code | "1 or 3 digit code" | SET §6 |
| V-HR-05 | Category code | ≤10 alphanumeric | SET §8 |
| V-HR-06 | Employee# | numeric ≤7 خانات | PNT §1 |
| V-HR-07 | Salary Template# | ≤10 خانات | SET §13 |
| V-HR-08 | Cal Code | 6 خانات فريد | SET §10 |

## B. تحققات الإصدارية والزمن

| # | التحقق | القاعدة | المصدر |
|---|---|---|---|
| V-HR-09 | Applicable From | **≥ تاريخ اليوم** (Grade/Template/HOD/EDCalc/Branch) — "The date cannot be lesser than the current system" | SET §4/§10/§11/§13 |
| V-HR-10 | نطاق Starting Period | Daily: To=From · Weekly +7 · Fortnightly +15 · Monthly تقويمي/متدحرج | SET §9 |
| V-HR-11 | أيام الحضور الافتراضي | "≤ date range entered in the date field" | PNT §6 |
| V-HR-12 | تاريخ إصدار القرض | ضمن شهر المعالجة وإلا → Processing Date تلقائياً | PNT §20 |
| V-HR-13 | نطاق تقرير المعاملات | "must not exceed the date range of the period selected" | REP §7 |

## C. تحققات المعادلات والمحرك

| # | التحقق | القاعدة | المصدر |
|---|---|---|---|
| V-HR-14 | **Test Equation** | زر تحقق صحة المعادلة قبل الحفظ | SET §10 ص21 |
| V-HR-15 | **Check Formula** (UDR) | "used to check the correctness of the specified formula" | SET §20 ص37 |
| V-HR-16 | Min/Max clamp للشرائح | "If the ED amount calculated for this slab is less than the minimum amount, then Fortune considers the minimum... more than the maximum... the maximum" | SET §10 |
| V-HR-17 | تعطيل حقول Eligibility | "The Amount, Minimum Amount and Maximum Amount fields are disabled in this slab type" | SET §10 ص24 |
| V-HR-18 | تطابق المعادلة مع Accept | "an equation has to be specified for this method of calculation" (Accept يتطلب معادلة!) | SET §10 ص17 |

## D. تحققات دورة العمل

| # | التحقق | القاعدة | المصدر |
|---|---|---|---|
| V-HR-19 | Attendance فردي | "single employee at a time" | PNT §5 |
| V-HR-20 | Default فئوي-أحادي | "single attendance for category wise" | PNT §6 |
| V-HR-21 | تجميد المغادرين | لا Modify لـ suspended/resigned/terminated | PNT §3 |
| V-HR-22 | قفل أصل القرض | التعديل عبر Return Entry حصراً | PNT §21 |
| V-HR-23 | Job Req المقيد | Modify = Authentication status + Remarks فقط | RQP §1 |
| V-HR-24 | Copy Inquiry ممنوع؟ | (مطابق BNQ — سياق RQP: البحث والتعديل؛ لا نسخ موثق للطلبات) | RQP عموماً |
| V-HR-25 | Accept بحضور يوم | "employee should be present for at least one day" | SET §10 |
| V-HR-26 | وجود Employer# للخصم المشترك | PF/ESI تقتضي رقم صاحب العمل | SET §5 |

## E. تحققات التكامل

| # | التحقق | القاعدة | المصدر |
|---|---|---|---|
| V-HR-27 | ملف الواجهة PYATYYMM.DAT | البنية: EMP(7)/DATE(8)/CODE(3)/DAYS(5,2) بفواصل — "Any change... will be intimated... at least two weeks in advance" (عقد تغيير!) | PNT §7 |
| V-HR-28 | كودات الملف مطابقة للنظام | "as per the Attendance Codes created in the Payroll Module" | PNT §7 |
| V-HR-29 | AR link company code | يجب ربط code بالموظف قبل النقل (double-click) | PNT §22 |
| V-HR-30 | تغيير بنية الملف موثق كتابياً | "vendor... should confirm in writing directly to IDS Bangalore" — **متطلب حوكمة بائع** | PNT §7 |

## F. مصفوفة الرسائل الموثقة

| السياق | الرسالة/السلوك | النوع |
|---|---|---|
| Personnel Master Save | مطالبة إدخال Employee# ثم شاشة تأكيد | Info/Prompt |
| Payroll Transaction (Tag More) | رسالة تأكيد بعد Confirm ("You get the message") | Confirm |
| ED Priority | تلميح دائم أسفل الشاشة: "Press F3 to change Priority Order" | Hint |
| Attendance Interface | إشعار أسبوعين مسبق لأي تغيير بنية | Contractual |
| Supplementary | تنقل بالتبويبات عبر أزرار Next | Navigation |

## G. الفجوات المكتشفة (تُسجَّل في 17)

- **GAP-HR-V01:** لا تحقق موثق لتفرد Employee# (النص يقول "unique" فقط في Grade) — يُفترض unique constraint.
- **GAP-HR-V02:** لا تحقق موثق لتزامن الحالات (Closing) مع القروض الجديدة.
- **GAP-HR-V03:** مدى TO amount للدرجات (تداخل نطاقين؟) غير موثق.
