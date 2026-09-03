# 01 — البيانات الرئيسية (Master Data) — وحدة GTP

> **لا ماسترات داخلية إطلاقاً.** كل مرجع موثق مستعارة من خارج الوحدة (Cost Center · Vendor · UOM) — والباقي **حقول حرة** (Particulars نصي، Authorized By/Responsibility أسماء حرة، Ref# حر). الوحدة الأضأل بنيوياً: 0 ماستر داخلي في 13 صفحة.

---

## 1. الحالة المائعة للمراجع المستعارة

| المرجع | الاستخدام الموثق | الموطن الأصلي | الحالة |
|---|---|---|---|
| **Cost Center** | "From the **Cost Center dropdown list** select the cost center to which the selected goods belong" (ص2) — dropdown جاهز | FAS/عائلة مراكز التكلفة | ✅ قائمة موجودة (السلوك موثق) |
| **Vendor Code** | "In the Vendor Code field **select** the vendor code" (ص2) — اختيار | [مصدر غير محسوم] | ⚠️ **UNK-074** — امتداد سابع لUNK-058 |
| **Vendor Name** | "In the Vendor Name **enter** the vendor's name" (ص2) — **إدخال يدوي** | ❌ لا يُسحب مع الكود! | ⚠️ انفصال Code/Name موثق حرفياً |
| **UOM** | "the unit of measurement in the **UOM field**" (شبكة الإصدار — ص3) | [ماستر وحدات عام؟] | ⚠️ UNK-077 — حر أم قائمة؟ |
| **Gate Pass #** | مفتاح استرجاع ("retrieve... based on Gate Pass #") | النظام | ⚠️ UNK-075 — توليده غير موثق |
| Authorized By / Responsibility | أسماء أشخاص حرة | ❌ لا ماستر موظفين | UNK-076 — عائلة UNK-038 |

## 2. البنية التحتية الوحيدة الداخلية: سجل التصريح (المفهوم لا الجدول)

```
GatePass (سجل معاملة):
  ├─ Gate Pass #              [توليد؟ — UNK-075]
  ├─ Gate Pass Ref#           [مرجع حر من المستخدم]
  ├─ Gate Pass Date           [تاريخ الإصدار]
  ├─ Cost Center              [dropdown]
  ├─ Authorized By            [اسم حر]
  ├─ Vendor Code + Vendor Name [اختيار + إدخال يدوي منفصلان!]
  ├─ Responsibility           [اسم حامل الإصدار]
  ├─ <Items grid>
  │    ├─ Particulars         [اسم الصنف نصي حر]
  │    ├─ UOM                 [حر/قائمة؟]
  │    ├─ Returnable          [نعم/لا]
  │    ├─ Quantity            [رقم]
  │    └─ Expected date of return  [تاريخ — للمرتجع]
  ├─ Remarks                  [نافذة منبثقة عند إدخال الكمية!]
  └─ <Receipts> (من Receive)
       ├─ Date                [لكل دفعة استلام]
       ├─ Quantity received   [جزئية مسموحة]
       └─ [تعديل بالنقر المزدوج]
```

## 3. تحليل "الماستر الافتراضي" (ما كان يمكن أن يكون)

| المفهوم | لماذا ليس ماستراً هنا | القرار المقابل في المشروع |
|---|---|---|
| **أصناف** | Particulars نص حر — لا كود صنف ولا ربط MGT Inventory | عند إعادة البناء: Item Link اختياري + حقل وصف حر (نمط Open Items في POS!) |
| **موردون** | كود يُختار (من مصدر خارجي) + اسم يدوي | Vendor Master موحد (قرار عائلة UNK-058) |
| **أسباب الخروج** | "servicing, material transfers etc" — أمثلة نثرية لا قائمة | **Reason Master** مقترح (D-GP-1) |
| **وحدات القياس** | حقل حر | UOM ماستر عام |
| **موظفون/معتمدون** | أسماء حرة | Employee Store (UNK-038) |

## 4. عائلات المشروع — موقف GTP

| العائلة | العضوية |
|---|---|
| بلا ماسترات داخلية | **فريدة** — أول وحدة صفر ماسترات (أضأل من TEL؟ لا — TEL امتداداتها ماسترات كاملة) |
| Vendor بلا موطن | **الامتداد السابع** لUNK-058 (MNT→FXD→GTP) |
| موظفون أحرار | امتداد UNK-038 (اسم Authorizer/Responsibility) |
| Long/Short Name | ✗ غائب كلياً |
| Status active/passive | ✗ غائب |
| User/Last Updated | ✗ **غائب!** — أول وحدة معاملات بلا أثر مستخدم واحد |
