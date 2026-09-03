# 03 — فهرس الشاشات (Screens Catalog) — وحدة GTP

> **~9 شاشات** — دليل نمط خطوات مرقّم (1. Click. 2. In the field...) بجُمل قصيرة، لا جداول Field/Action/Points (انفصال عن نمط FXD/FNB!): أضأل وحدة شاشاتٍ في المشروع؛ أهم ما فيها **شبكة أصناف الإصدار** و**نافذة الملاحظات المنبثقة عند إدخال الكمية** و**الاسترجاع ثلاثي المفاتيح**.

---

## 1. الجرد الكامل

| # | الشاشة | النوع | المصدر |
|---|---|---|---|
| S-GP-01 | **Issue Gate Pass** (رأس + شبكة أصناف) | معاملة | §1 ص2-3 |
| S-GP-01a | Remarks popup (عند إدخال Quantity) | منبثقة | ص2 (Note) |
| S-GP-02 | **Receive Gate Pass** (اختيار مفتاح) | معاملة | §2 ص3-4 |
| S-GP-02a | استرجاع بـGate Pass # (help) | فرعية | ص4 |
| S-GP-02b | شاشة استلام التفاصيل (Date + Quantity) | فرعية | ص4-5 |
| S-GP-03 | Gate Pass Query | استعلام | §3 ص6-7 |
| S-GP-04 | Gate Pass Register | تقرير | §4 ص7-8 |
| S-GP-05 | Pending Gate Passes | تقرير (as-on) | §5 ص8-9 |
| S-GP-06 | Gate Pass Print | طباعة | §6 ص10-11 |
| S-GP-07 | Gate Pass Report | تقرير | §7 ص11-12 |

## 2. شاشة Issue بالتفصيل (خطوات الدليل الحرفية)

```
1. Click [New/Issue]
2. Gate pass Ref#          → مرجع حر للبضاعة
3. Gate Pass Date          → تاريخ الإصدار
4. Cost Center             → dropdown
5. Authorized By           → اسم المعتمِد (حر)
6. Vendor Code             → اختيار
7. Vendor Name             → إدخال يدوي (منفصل عن الكود!)
8. Responsibility          → اسم المُصدِر (حر)
9. <شبكة التفاصيل>
   Particulars             → اسم الصنف (حر)
   UOM                     → وحدة القياس
   Returnable?             → نعم/لا
   Quantity                → الكمية
   Expected date of return → للمرتجع
   [عند إدخال الكمية → نافذة Remarks منبثقة]
10. Click [Save]
```

## 3. شاشة Receive بالتفصيل (الدورة الأنيقة)

```
1. اختيار مفتاح الاسترجاع: ( ) Gate Pass #  ( ) Vendor Name  ( ) Gate Pass Ref#
2. [Gate Pass #] → إدخال/اختيار من Help → OK
3. → عرض التصريح المسترجع
4. Click [إدخال استلام] → شاشة التفاصيل
5. إدخال Date + Quantity (جزئية مسموحة) → OK
6. Save
   [تعديل لاحق: Click مرة أخرى + double-click على السجل المطلوب]
```

## 4. أنماط التفاعل الموثقة

| النمط | الموثق | الشاشات |
|---|---|---|
| خطوات مرقمة نثرية | "1. Click... 2. In the... field enter..." | كل الوحدة (بديل جداول FXD!) |
| **Help (؟)** | "Enter the Gate Pass # or **select it from the help screen**" | Receive + Print (Select the table number **using help/"?" symbol** نمط TSC!) |
| **نافذة منبثقة شرطية** | "When you **enter the quantity** you get the following screen, where you can enter any **remarks**" | Issue — أول popup مشروط بحقل |
| double-click للتعديل | "double-click on the record that you want to modify" | Receive |
| زر Print + اختيار طابعة | "Select a printer type from the list" | Print |
| خيارات راديو ثلاثية | مفاتيح الاسترجاع | Receive + Query + Report |

## 5. ملاحظات UX مقتبسة

- الدليل يذكر الأزرار بلا أسماء أحياناً ("Click ." — أزرار ساقطة من الاستخراج النصي): [NOT DOCUMENTED] تسميات الأزرار.
- **لا F1/F3 موثقة** — الاسترجاع اليدوي/Help العام فقط (أضأل استخدام لمفاتيح الوظائف في وحدة معاملات).
- لا شاشة تعديل للإصدار ذاته — **التعديل الموثق للاستلام فقط** (تعديل التصريح الصادر غير موجود أصلاً! — راجع 10/13).
