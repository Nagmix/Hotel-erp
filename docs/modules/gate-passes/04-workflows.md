# 04 — تدفقات العمل (Workflows) — وحدة GTP

> **WF-GP-01..07** — دورتان فقط: **دورة الخروج** (إصدار → بوابة → وربما لا عودة) و**دورة العودة** (استرجاع ثلاثي المفاتيح → وسم استلام جزئي/كلي → تعديل)، وحولهما حلقة استعلام/طباعة يومية. أضيق وحدة تدفقات في المشروع — وأصعبها من ناحية "ماذا لو لم يعد الصنف؟" (لا تدفق معالجة متأخر موثق!).

---

## WF-GP-01: إصدار تصريح (Issue)

```
[مادة تغادر الفندق: servicing / material transfer / ...]
        ↓
Issue Gate Pass → Ref# + Date + Cost Center
        ↓
Authorized By (اسم المعتمد) + Vendor Code [اختيار] + Vendor Name [يدوي!] + Responsibility
        ↓
<شبكة الأصناف> لكل صنف:
   Particulars + UOM + Returnable (نعم/لا) + Quantity
        ↓ [Returnable = نعم]
Expected date of return
        ↓ [أثناء إدخال Quantity]
→ نافذة Remarks منبثقة → ملاحظات
        ↓
Save → التصريح جاهز للطباعة/البوابة
```

## WF-GP-02: استلام مرتجع (Receive) — ⭐ دورة العودة

```
[المادة عادت — كلياً أو جزئياً]
        ↓
Receive Gate Pass → اختيار مفتاح الاسترجاع:
   (Gate Pass # | Vendor Name | Gate Pass Ref#)
        ↓ [مثال Gate Pass #]
إدخال/اختيار من Help → OK → عرض التصريح
        ↓
[إدخال استلام] → Date + Quantity
        ↓ [جزئي؟]
"Provision to tag partial items received" — وسم الكمية المستلمة فقط
        ↓
Save
        ↓ [تصحيح؟]
Click [إدخال استلام] مجدداً → double-click السجل → تعديل
        ↓
[لا مواصفة: إغلاق التصريح عند اكتمال الكمية — متى يصبح "مستوفى"؟]
```

## WF-GP-03: الاستعلام اليومي (Query)

```
اختيار: كل مراكز التكلفة أو محدد
        ↓
نمط النطاق: (Date Range | As on date | Gate Pass # Range)
        ↓
النوع: (Returnable | Non-Returnable | All | **Pending** | All)
        ↓
Display → التفاصيل
```

## WF-GP-04: سجل المرتجع اليومي (Register)

```
Enter date range + checkbox 'Include remarks'
        ↓
Print → "all **returnable** Gate Passes issued by various departments"
        [غير المرتجع غائب عن السجل بنيوياً!]
```

## WF-GP-05: المعلق بتاريخ (Pending)

```
Enter as-on date + خيارات Query + checkbox 'Include remarks'
        ↓
Print → "pending Gate Passes register as on a date"
        [مفهوم Pending مرتبط بExpected date of return — [INFERENCE] تجاوز التاريخ المتوقع بلا استلام]
```

## WF-GP-06: طباعة تصريح (Print)

```
اختيار المحور: (Date | Gate Pass # | Vendor)
        ↓
Date range / قيمة المحور
        ↓
Returnable أو Non-Returnable
        ↓
Select printer type
        ↓
Print
```

## WF-GP-07: تقرير التفاصيل (Report)

```
نفس بنية Query (مراكز + نطاق زمني/GP# + نوع)
        ↓
Display "transaction details of Gate Passes based on the selection criteria"
```

## التدفق الغائب (المخاطر)

| السيناريو | الحالة |
|---|---|
| **عدم عودة مرتجع** | لا تدفق معالجة (شطب/إهلاك/تحويل permanent) — يبقى Pending للأبد؟ [NOT DOCUMENTED] |
| تجاوز Expected date | هل يظهر بالمعلق تلقائياً؟ [INFERENCE نعم — لكن القاعدة غير مصرّحة] |
| تعديل تصريح صادر | ❌ لا مسار |
| إلغاء تصريح | ❌ لا مسار |
| استلام صنف غير مرتجع | منطقياً ممنوع؟ غير موثق — [NOT DOCUMENTED] |
