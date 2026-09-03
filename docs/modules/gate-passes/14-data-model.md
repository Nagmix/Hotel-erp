# 14 — نموذج البيانات (Data Model) — وحدة GTP

> **كيانان فقط / ~20 حقلاً** — أصغر نموذج بيانات في المشروع بفارق: GatePass (رأس + شبكة أصناف) وGatePassReceipt (دفعات استلام بابن). لا جدول مسلسلات (توليد الرقم مجهول!) ولا أي كيان مرجعي داخلي.

---

## 1. مخطط الكيانات (ERD نصي)

```
CostCenter (خارجي) ──┐
Vendor[؟] (خارجي)  ──┤
UOM[؟] (خارجي)     ──┤
                    ▼
              GatePass ──── (طباعة: Print + printer type)
              ├─ gate_pass_no        [UNK-075: توليد آلي؟]
              ├─ ref_no              [حر]
              ├─ date
              ├─ cost_center         (FK خارجي)
              ├─ authorized_by       (نص حر)
              ├─ vendor_code         (FK خارجي [؟])
              ├─ vendor_name         (نص يدوي — منفصل عن الكود!)
              ├─ responsibility      (نص حر)
              └─< GatePassItem
                   ├─ particulars    (نص حر)
                   ├─ uom            ([؟])
                   ├─ is_returnable  (bool)
                   ├─ quantity
                   ├─ expected_return_date
                   └─ remarks        (من نافذة مشروطة بالكمية)
                         └─< GatePassReceipt
                              ├─ date
                              └─ qty_received    (جزئية — قابلة للتعديل double-click)
```

## 2. جرد الحقول (كل الموثق)

| الكيان | الحقول | ملاحظات |
|---|---|---|
| **GatePass** | gate_pass_no · ref_no · date · cost_center · authorized_by · vendor_code · vendor_name · responsibility | 8 حقول رأس — كل المراجع خارجية/حرة |
| **GatePassItem** | particulars · uom · is_returnable · quantity · expected_return_date · remarks | 6 حقول بند |
| **GatePassReceipt** | date · qty_received | 2 حقول دفعة — أضأل كيان في المشروع |

**الإجمالي: 16 حقلاً فعلياً** (مقابل ~100 في FXD و~35 في Master واحد!)

## 3. الحالات المشتقة (لا جدول حالة موثق)

```
Status (مشتق حسابياً):
  Non-Returnable → "نهائي" فور الإصدار
  Returnable: (Σ qty_received < quantity) → Pending
              (Σ = quantity)              → Complete [بلا قاعدة إغلاق]
              (date > expected)           → Overdue [بلا كيان]
```

## 4. أسرار البيانات الموثقة

| السر | الشاهد |
|---|---|
| **Vendor Name كحقل مستقل** | يدوي رغم وجود الكود — أرشيف نصي بلا FK |
| **remarks على مستوى البند (شرطياً)** | نافذة تظهر عند إدخال الكمية — الارتباط بالبند مستنتج [INFERENCE] |
| لا User/Last Updated | أول معاملة بلا أثر مستخدم مطلقاً |
| لا جدول مسلسل | (مقابل FIMSHTBL في FXD!) — توليد GP# غامض |
| لا حالات مخزنة | كل Status مشتق لحظياً في الاستعلامات |
| **شبكة استلام قابلة للتعديل** | double-click — بلا Versioning |
