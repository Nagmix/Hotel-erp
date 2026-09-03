# 12 — التكاملات (Integrations) — وحدة GTP

> **I-GP-01..06** — الوحدة الأعزل رقمياً: **لا جسر صاعد واحد ولا نازل واحد** — كل "التكامل" مرجعي استهلاكي (Cost Centers من عائلة FAS، Vendor من موطن مجهول) أو **موضوعي بلا نص** (أسباب الخروج تذكر servicing/material transfers بلا أي ربط MGT/FXD). عائلة UNK-058 (المورد) تبلغ امتدادها السابع والأخير هنا.

---

## 1. خريطة التكاملات

| ID | من | إلى | النوع | النص/الأساس | الحالة |
|---|---|---|---|---|---|
| **I-GP-01** | GTP (Issue) | Cost Centers (عائلة FAS/SLM) | مرجعي dropdown | "From the Cost Center dropdown list select the cost center to which the selected goods **belong**" (ص2) | ✅ استهلاك موثق |
| **I-GP-02** | GTP (Issue) | [Vendor Master؟] | مرجعي مشطور | Code يُختار + **Name يُدخل يدوياً** (ص2) | ⚠️ UNK-074 — **الامتداد السابع لUNK-058** |
| **I-GP-03** | GTP (Items) | [UOM Master؟] | مرجعي | حقل UOM حر بشبكة الأصناف (ص3) | ⚠️ UNK-077 |
| **I-GP-04** | GTP ↔ **MGT** | — | **موضوعي بلا جسر** | "goods taken out... for reasons like servicing, **material transfers** etc" (ص2) — أسباب المخزن ذُكرت نثراً بلا ربط Inventory/Transfer واحد | [INFERENCE] الفجوة الضابطة الكبرى |
| **I-GP-05** | GTP ↔ **FXD** | — | احتمال مقصود؟ | أصل يخرج للصيانة (تكامل منطقي FXD-MNT-GTP) — لا إحالة نصية بالأصل ("Asset Issue Gate Pass" في متن §1 يوحي بقراءة قديمة للعنوان!) | [UNCERTAIN] — راجع 13 |
| **I-GP-06** | GTP → الطابعات | عتادي | "Select a **printer type** from the list" (ص10) | قناة إخراج العتاد |

## 2. التحليل: الجزيرة الورقية

```
كل علاقات GTP المعمارية:
   - استهلاك مرجعي (3 قوائم خارجية)
   - مخرج ورقي (طابعة)
   - لا أحد يستهلك مخرجاتها رقمياً!
        ↓
"الجزيرة الورقية" — أضأل عضو في عائلة العزل (MNT "الجزيرة المعزولة" كانت تستعير
  مخازن/مراكز/أصناف من MGT؛ GTP لا تستعير سوى القوائم الثلاث)
```

## 3. فرص التكامل المفقودة (خريطة القرار)

| الفرصة | النص الداعم | قرار إعادة البناء |
|---|---|---|
| **خروج مخزني → MGT Stock/Transfer** | "material transfers" صراحة | D-GP-7: تصريح مرتبط بMaterial Transfer يخصم/يسجل الحركة |
| خروج خدمة → Service Work Order (MGT) | "servicing" صراحة | ربط اختياري بSWO |
| خروج أصل → FXD/MNT | منطق الصيانة | Asset Movement في ERPNext يحمل السبب |
| عدم عودة → Adjustment MGT | دورة Pending المتجمدة | زر "Convert to Permanent Transfer" (قرار [NOT DOCUMENTED] يحسم فراغ الدليل) |
| Vendor Name ↔ Code | BR-GP-03 | توليد آلي (D-GP-2) |

## 4. موقع GTP في خريطة الجسور

- **لا تنتمي** لعائلة الجسور المالية (F4-F9/F12/F13) ولا السلوكية (FNB→POS/MGT) — الوحدة الطرفية الوحيدة في المشروع بدرجة صفر اتصال.
- مع GTP تكتمل خريطة التكاملات الموثقة نصاً — **كل الجسور المرقمة (16+ F-link وS-link وI-link) لا تحوي واحداً يلمس GTP**.
