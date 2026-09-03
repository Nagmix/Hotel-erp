# 16 — الموائمة مع ERPNext/Frappe (ERPNext Mapping) — وحدة GTP

> **F-GP-1..8** — وحدة "بناء حر صغير": لا يوجد تطبيق Gate Pass في ERPNext (لا مفهوم التصريح الأمني أصلاً!) — لكن كل مكوناتها **لقطات موسعة لأصول قائمة**: Material Transfer (حركة) + **Gate Pass doctype مخصص صغير** (أبسط DocType في إعادة البناء) + Query/Print Formats. التقدير: **~3 أصول مخصصة / 1-2 أسبوع** (أسرع وحدة مع SLM-PRF).

---

## 1. الخريطة العامة

| مكون GTP | الأصل Frappe/ERPNext | الحالة | القرار |
|---|---|---|---|
| Gate Pass (رأس) | **DocType مخصص** (gate_pass) | 🔧 مخصص بسيط | F-GP-1 |
| شبكة الأصناف | Child Table (gate_pass_item) | 🔧 | F-GP-1 |
| Cost Center | Link إلى Cost Center الأصلية | ✅ | F-GP-2 |
| Vendor (Code+Name) | **Link Vendor** + fetch name آلي | ✅ (يسد الانفصال!) | F-GP-3 |
| UOM | Link UOM | ✅ | F-GP-3 |
| Receive (جزئي) | Child Table gate_pass_receipt أو جدول دفعات | 🔧 | F-GP-4 |
| Pending/Complete | حقل محسوب (custom status) | 🔧 | F-GP-4 |
| Rبط MGT المفقود | **Material Transfer** (اختياري) | ✅ عند الربط | F-GP-5 |
| عدم العودة | زر Convert to Permanent (Stock Entry) | 🔧 | F-GP-5 |
| Register/Pending/Report | **Query Report + Print Format** | ✅ | F-GP-6 |
| Gate Pass Print (بطاقة) | **Print Format** (بطاقة + A4) | ✅ | F-GP-7 |
| Authorized By/Responsibility | Link Employee (اختياري) + نص | 🔧 | F-GP-8 |

## 2. القرارات التفصيلية

### F-GP-1: DocType التصريح (أبسط ما يُبنى في المشروع)
```python
gate_pass: naming_series (GP-.#### يسد UNK-075!) · ref_no · date · cost_center (Link)
           vendor (Link) → vendor_name fetch (يسد BR-GP-03!) · authorized_by · responsibility
gate_pass_item: particulars · uom (Link) · is_returnable (Check) · qty (Float)
           expected_return_date (Mandatory depends on is_returnable!) · remarks
```
- 16 حقلاً فقط — أنقى DocType في التحويل كله.

### F-GP-4: الاستلام والحالة
- Child `gate_pass_receipt` (date + qty) + **validation سقف تراكمي** (يسد V-GP الثغرة الأولى) + حقل status محسوب: Pending / Complete / **Overdue** (scheduler يومي يقارن expected_return_date).
- تعديل الدفعات بـVersioning أصلي (يسد فجوة double-click الأثر).

### F-GP-5: الجسر المفقود يُبنى اختيارياً
- checkbox "استقطاب حركة مخزنية" → **Material Transfer** مقابل (المستودع الوجهة: المورد/خارج) — يعمل فقط عند ربط البند بصنف Inventory (اختياري — يبقى particulars الحر الافتراضي أمانة للأصل).
- زر **"Close as Not Returned"** → تحويل دائم (Entry) + خروج نهائي من Pending — يحسم الدورة المتجمدة (D-GP-7).

### F-GP-6/7: المخرجات
- Query Report واحد (محاور موحدة: مراكز/زمن/GP#/Vendor/Ref/النوع/الحالة) + Print Format بطاقة بوابة **صغيرة للحراسة** (QR اختياري) + A4 سجل مرتجع.
- **Status "Printed"** بطابع زمن لكل نسخة (يسد ثغرة إعادة الطباعة — D-GP-4).

### F-GP-8: المساءلة
- authorized_by/responsibility: Link Employee اختياري (يستفيد من كيان الموظف الموحد — قرار عائلة UNK-038) مع سقوط حر كاحتياط.

## 3. ما يسقط كلياً

| مكوّن FN6i | لماذا |
|---|---|
| Vendor Name اليدوي | fetch آلي |
| Popup شرط الكمية | سلوك حقل عادي |
| خيارات القوائم المعقدة | محاور Query موحدة |

## 4. الخلاصة

> لا مكافئ جاهز — لكن الكيان بسيط لدرجة أن "البناء المخصص" أرخص من أي مواءمة قسرية: **يوم برمجة للDocType + يوم للتقارير**. الوحدة تحمل لقب "أرخص تحويل" (مع كونها الأعزل أصلاً).
