# 06 — التحققات (Validations) — وحدة POS

> V-POS-01..28 مصنفة: Prevent (منع حفظ/تنفيذ) / Warn (استفتاء) / System (سلوك آلي) / Lock (حاجب إجرائي).

---

## 1. تحققات الإدخال (الهيكلية)

| ID | القاعدة | النوع | المصدر |
|---|---|---|---|
| V-POS-01 | Applicable From ≥ اليوم لتفعيل أي Master | **Prevent** | POS-SET §1/§2/... |
| V-POS-02 | سجل اليوم: تعديل Status فقط (باقي الحقول بسجل مستقبلي) | **Lock** | POS-SET §1 ص10 |
| V-POS-03 | Item Code: numeric ≤4 | **Prevent** | POS-SET §24 |
| V-POS-04 | Outlet Code ≤3 / Session ≤2 / KOT Type numeric ≤2 / Table ≤5 / Server ≤3 / Kitchen ≤3 / Menu Group ≤3 / TS Group ≤2 / Modifier ≤2(TS ≤4) | **Prevent** | POS-SET |
| V-POS-05 | Table Suffix: مجموع خانات (طاولة+لاحقة) **≤6** | **Prevent** | TS ص45 |
| V-POS-06 | KOT Book **≤100 ورقة** | **Prevent** | POS-SET §30 |
| V-POS-07 | Open Item: **لا تعديل بعد الإنشاء** (حذف+إعادة) | **Lock** | TS ص21 |
| V-POS-08 | Quantity المقسومة **< الكمية الفعلية** | **Prevent** | TS ص31 |

## 2. تحققات التسوية والفوترة

| ID | القاعدة | النوع | المصدر |
|---|---|---|---|
| V-POS-09 | **Balance = 0.00 قبل Save** — وإلا لا تُسوّى الفاتورة | **Prevent** | TS ص33 |
| V-POS-10 | أنماط التسوية **6 حصراً** — "Others will not work" | **Prevent** | TS ص32 |
| V-POS-11 | Guest Settlement: **رقم غرفة صحيح → ضيف من الجدول** | System | TS ص36 |
| V-POS-12 | CC: **سحب البطاقة يلتقط التفاصيل آلياً** | System | TS ص34 |
| V-POS-13 | **Resettlement: استفتاء إلزامي** ("Do you want to resettle it?") | **Warn** | TS ص36 |
| V-POS-14 | Reprint قبل التسوية: **إبطال الرقم القديم + رقم جديد** | System | TS ص41 |
| V-POS-15 | Void/حذف صنف: **Reason إلزامية** (معرَّفة/جديدة) | **Prevent** | TS ص17 |
| V-POS-16 | Print Bill: **تسوية نقدية تلقائية** | System | TS ص24 |

## 3. تحققات الأمن والإقفال

| ID | القاعدة | النوع | المصدر |
|---|---|---|---|
| V-POS-17 | Close Shift: **Password + لا KOTs/Bills معلقة** | **Prevent/Lock** | TS ص46 |
| V-POS-18 | Close Outlet: **تأكيد YES + لا معلقات** | **Prevent/Lock** | TS ص46 |
| V-POS-19 | تغيير الوردية: **إغلاق السابقة أولاً** | **Lock** | TS ص4 |
| V-POS-20 | رؤية المنافذ في Session Statistics: **المخوَّلة فقط** | System | POS-LUK §6 |
| V-POS-21 | Login: اختيار DB (PMS/Dummy) — بيئتا إنتاج/تدريب | System | TS ص1 |

## 4. تحققات الخصومات والتسويق

| ID | القاعدة | النوع | المصدر |
|---|---|---|---|
| V-POS-22 | Happy Hours: **تداخل زمني ممنوع** (رسالة موثقة) | **Prevent** | POS-SET §31 ص98 |
| V-POS-23 | Happy Hours جارٍ اليوم: **From Date معطّل + سجل جديد من الغد** | System | POS-SET §31 ص98 |
| V-POS-24 | **Passive لا يُعاد Active** (Happy Hours) | **Prevent** | POS-SET §31 ص98 |
| V-POS-25 | Sales Promotion: **Main Item ≥1 إلزامي** | **Prevent** | POS-SET §32 ص100 |
| V-POS-26 | Member Discount: نطاق الأعضاء بقرار **INI 404** | System | POS-SET §41 ص121 |
| V-POS-27 | Discount Manual: **Reason إلزامية** | **Prevent** | TS ص25 |
| V-POS-28 | Tax Exemption: **Reason إلزامية لكل ضريبة معفاة** | **Prevent** | TS ص27 |

## 5. تحققات متفرقة موثقة

| ID | القاعدة | النوع | المصدر |
|---|---|---|---|
| V-POS-29 | طابعات **كل المطابخ إلزامية** (Open Items) | **Prevent** | POS-SET §19 |
| V-POS-30 | Post Guest History: التاريخ **≤ تاريخ المحاسبة** | **Prevent** | POS-GST §4 |
| V-POS-31 | Table Booking: تاريخ الاستعلام **≥ اليوم و< تاريخ الحجز** | **Prevent** | POS-LUK §3 |
| V-POS-32 | نقل الأصناف بين منافذ: **تطابق العملات الأجنبية** | **Prevent** | POS-SET §25 |
| V-POS-33 | Modifier داخل Group: **لا حذف** (F5) | **Prevent** | POS-SET §27 |
| V-POS-34 | طباعة النموذج: **يجب Make Active أولاً** + Body Details معرَّف | **Prevent** | POS-SET §23 |

## 6. مصفوفة الرسائل الموثقة نصاً

| الموقف | الرسالة/الأثر | المصدر |
|---|---|---|
| Reprint قبل التسوية | إبطال الرقم + توليد جديد (سلوك لا رسالة) | TS ص41 |
| إعادة تسوية | "Bill is already Settled. Do you want to resettle it?" | TS ص36 |
| Balance ≠ 0 | "check will not be settled" | TS ص33 |
| تداخل Happy Hours | "Time slot overlaps with existing Time slot." | POS-SET §31 |
| تعديل Happy Hours اليوم | "This modification will be effect from next day" | POS-SET §31 |
| إغلاق بمعلقات | "you will not be able to close your shift/outlet" | TS ص46 |
| نزول العملة الخفية | رسالة النص تحجب قبل الحفظ | TS ص33 |

> **ملاحظة تحققية:** لا يوجد تحقق موثق لعدم **تجاوز Covers الحد الأقصى** للطاولة عند الطلب (`Max Covers ≤3 خانات` هي حد حقل لا منطق تشغيلي موثق) — `[NOT DOCUMENTED]`.
