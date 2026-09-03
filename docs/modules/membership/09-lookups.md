# 09 — الاستعلامات التفاعلية (Lookups) — وحدة MEM

> **6 استعلامات تفاعلية بدرجة تفاعل أعلى من التقارير** — أغناها **Membership Summary** و**Spending Pattern** بحفر حتى تفاصيل الفاتورة. النمط العام: فلاتر + **زر Load** + شبكة نتائج قابلة للنقر.

---

## 1. Corporate Information (استعلام شركة)
- Member/Application + Membership# (F1) → **تعبئة تلقائية كاملة** لكل التفاصيل
- تبويبات العرض: General / Register Address / Local Address / Mailing Address / Reference
- "If there are more than 1 reference, click **Next or Previous** to move between records" (RPL ص31) — **تصفح مرجعي متعدد داخل السجل**.

## 2. Member Information (استعلام عضو)
- Member/Application + Membership# (F1)
- تبويبات: General / Reference / Personal Info / Address / Work Details / Other Details (RPL ص32)
- **نفس عائلة "More Details"** الموثقة في Application Screening (MPF ص13-17) — عائلة عرض موحدة مستعملة في مكانين.

## 3. Pending Complaints (استعلام الشكاوى المعلقة)
- عرض: "nature of the complaint, member's name... and the complaint number"
- **"The count of the pending complaints is shown in the graph on the left side of the screen"** (RPL ص33) — **رسم بياني مدمج داخل شاشة استعلام** (ثاني ظهور لرسوم مدمجة بعد dashboard في SYS).

## 4. Membership Summary (ملخص العضويات بالحفر) ⭐
- "query the **count of members based on their status** for a given month range"
- سلسلة الحفر الموثقة: "The user will have **drill down options till the member information screen**" (RPL ص33-34):
```
Month Range → Load → عدّادات الحالة (شبكة)
  → Double-click سجل → تفاصيل
    → فرز بالنقر على رؤوس الأعمدة (ascending/descending)
      → النقر على صف عضو → شاشة Member Information كاملة
  → Exit → الرئيسية | → Print → نسخة مطبوعة
```
- **أعمق حفر ثلاثي المستويات في الوحدة** (عداد → سجل → ملف عضو).

## 5. Settlement Query (استعلام التسويات)
- Service type + أنواع الشحنات: **Pending/Settled/Both** + Date Range → Load → النتائج مباشرة (RPL ص54) — استعلام فوري لتتبع فواتير الخدمة.

## 6. Spending Pattern (نمط الإنفاق بحفر مالي) ⭐
- بُعدان: **Service أو Member** + Membership# (F1) أو Service Type + **Month/Year range** → Load
- "Double-click on each of the revenue amount to view the **bill details**" (RPL ص55) — **حفر من رقم إجمالي إلى فاتورة أصلية**
- أزرار إخفاء: **Hide Count column / Hide Revenue column** — تخصيص عرض في الزمن الحقيقي
- **أقرب شيء لمفهوم BIOLAP cube** في المشروع: بُعد (خدمة/عضو) × زمن (شهور) × مقياس (عدد/إيراد) بحفر للتفصيل.

---

## جدول مقارنة درجات التفاعل

| الاستعلام | فلاتر | Load | حفر | رسم | طباعة | إجراءات جانبية |
|---|---|---|---|---|---|---|
| Corporate Information | ✓ | (تعبئة تلقائية) | — | — | — | تصفح مراجع |
| Member Information | ✓ | (تعبئة تلقائية) | — | — | — | تبويبات 6 |
| Pending Complaints | — | — | — | **✓ عدّاد** | — | — |
| Membership Summary | ✓ (شهور) | ✓ | **✓ 3 مستويات** | — | ✓ | فرز رؤوس |
| Settlement Query | ✓ | ✓ | — | — | — | — |
| Spending Pattern | ✓ (بُعد+زمن) | ✓ | **✓ للفاتورة** | — | — | **إخفاء أعمدة** |

> **النمط المعماري للواجهة:** وحدة MEM تمثل **ذروة نمط الاستعلام التفاعلي Load-and-Drill** في المشروع — أكثر حتى من POS LUK وMGT LUK (التي كانت تصفحية أساساً) — قرار F-ME-12: ترجمتها إلى Script Report مع drill-down في Frappe.
