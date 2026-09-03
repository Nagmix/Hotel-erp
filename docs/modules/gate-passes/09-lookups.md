# 09 — الاستعلامات (Lookups/Queries) — وحدة GTP

> **استعلام واحد** (Gate Pass Query) — أضأل حصيلة استعلامية في المشروع؛ الرسالة المعمارية: الوحدة "ورقة + سجل" لا مساحة عمل تحليلية. الاستعلام الوحيد يحمل **خمسة محاور مرشحة** (مراكز + زمن + نوع + حالة Pending) — أثقل شاشة معايير في الوحدة!

---

## Q-GP-01: Gate Pass Query (§3 ص6-7)

**النص الحرفي:** "This query option is to view Gate Pass Transaction Details for **all cost centers or selected**, for given **date range or Gate Pass # range, or as on date**, **Returnable /Non Returnable or both**, **only pending or all gate passes**."

```
المحاور الخمسة:
  1. Cost Centers: All / Selected
  2. النطاق الزمني: Date Range / As on date / Gate Pass # Range
  3. النوع: Returnable / Non-Returnable / Both
  4. الحالة: Pending فقط / All
  5. (Display)
```

## التحليل

| البعد | القراءة |
|---|---|
| **تعدد المحاور مقابل شاشة واحدة** | خمسة أبعاد في استعلام وحدةٍ بلا ماسترات — كل التعقيد في التصفية لا في البيانات |
| **Pending كمرشح وليس ككيان** | "only pending **or all gate passes**" — الحالة تعرضية (مشتقة من الاستلام/التاريخ) لا جدول حالة |
| **Gate Pass # Range** | نطاق أرقام — يستدعي ترقيماً رقمياً متسلسلاً [يدعم الاستنتاج الآلي — UNK-075] |
| **As on date** | نفس زوجة Pending (R-GP-02) — لحظة التقييم |
| لا Drill/تصدير | عرض خالص |

## الغائب

| الغياب | البديل |
|---|---|
| استعلام استلام | يُرى من Receive نفسها (استرجاع + عرض) |
| استعلام بمرجع Ref# | Ref# مفتاح استرجاع في Receive فقط — ليس في Query! (غرابة) |
| استعلام مورد | Vendor محور في Print فقط — Query لا تملكه! |

> **D-GP-5:** يُدمج Query/Report في Query Report واحد بمحاور موحدة (إضافة Vendor وRef# للمحاور الخمسة) — إغلاق ثغرتي الشاشة.
