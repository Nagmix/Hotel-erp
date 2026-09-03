# 10 — المعاملات (Transactions) — وحدة FXD

> **T-FX-01..06** — أربع معاملات ذات حالة + محركان دفعيان: كل معاملة تسكن (Property × Financial Period) وتوثق الحقول الآلية العشرة؛ **البيع/الاستبعاد هو الوحيد الذي يفتح شاشة ترحيل** — والكل يحدث بعد بوابة Start Date.

---

## T-FX-01: إنشاء أصل (Fixed Asset Master — Save)

| البعد | الموثق |
|---|---|
| المفتاح | Asset code آلي (12 محرفاً — FIMSHTBL) |
| البيانات | 35 حقلاً + شبكتا Tax/Component + Current closing |
| الأثر | "opening balance quantity" للكمية؛ لا ترحيل عند الإنشاء (الترحيل عند الإهلاك/البيع فقط) |
| الحالة الناتجة | Asset status من القائمة (قيم غير موثقة) |

## T-FX-02: إضافة مكوّن (Fixed Asset Component Entry)

| البعد | الموثق |
|---|---|
| المفتاح | Property + Financial Period (F3) + Asset Code (F1) + Date |
| القيمة | Component Code + Currency + [Rate آلي] + Amount → [Exchange آلي] |
| الأثر المحاسبي | "The component added **will increase the asset value**" — تعديل قيمة الأصل القائم |
| الأثر الإهلاكي | ❌ غير موثق: هل يعاد حساب الإهلاك؟ هل يمتد العمر؟ (UNK-070) |
| الترحيل | لا ترحيل GL موثق عند الإضافة (قيمة تتراكم داخلياً) |

## T-FX-03: بيع/استبعاد (Fixed Assets Transaction) — ⭐ معاملة الترحيل

| البعد | الموثق |
|---|---|
| المفتاح | Property + FY + Asset Code + Type (Sale افتراضي/Disposal) + Date |
| الكميات | Quantity جزئية + شبكة (Original/Sold/Disposed/**Balance**) |
| المبالغ | Sale Amount + [Local = Sale×Rate] + [Asset Value = Qty×Price] + NBV + [Gain/Loss] |
| الدفع | **Pay Mode: Bank/Cash** — بطاقة "provided later" |
| الترحيل (الأصل مربوط فقط) | (1) accumulated posting ledger حسب ربط Sub Group (2) Sale Amount → Cash/Bank (3) P&L ledger حسب Gain/Loss (4) **تساوي → P&L يتعطل** |
| الحالة الناتجة | كمية Balance تنخفض؛ عند الصفر → أصل مستنفد (يظهر بZero Quantity checkbox في List!) |

## T-FX-04: حساب الإهلاك (Calculate Depreciation)

| البعد | الموثق |
|---|---|
| المفتاح | "till specified month and year" |
| المحرك | SLM (فترات أو نسبة) أو WDV (نسبة متناقصة) — **بقرار INI #475** |
| الأثر | تحديث Last date depn + تاريخ الإهلاك لكل أصل (يُستهلك من Dep History) |
| العكس | **Rollback موثق** — "can be rolled back with roll back options" (بلا مواصفة نطاق/أثر GL) |
| الترحيل | ❌ لا يرحّل شيئاً — فصل صريح Calc/Post |

## T-FX-05: الترحيل المالي (FI Depr Posting to FA)

| البعد | الموثق |
|---|---|
| المفتاح | Property + Transaction Type + Date[MMYY] + FY |
| الشبكة | Load → مجموعات مربوطة قابلة + **غير مربوطة تُبرز أزرق وتُستثنى** |
| الأثر GL | قيود شهرية بتاريخ **نهاية الشهر** · منهج **SLM فقط** · تجميع **Sub group wise فقط** |
| الذواكر | Last Dep. Post Date تتقدم بعد Save |
| العكس | لا Rollback موثق للترحيل (الاسترجاع للحساب فقط!) — ثغرة [NOT DOCUMENTED] |

## T-FX-06: استلام مبيعات؟ (غائب)

> لا معاملة "استلام قيمة بيع" منفصلة — قيمة البيع تدخل مباشرة في T-FX-03 وتُرحَّل Cash/Bank آنياً: نمط "الترحيل الفوري عند الحفظ" (مثل FO Consolidated Entry لا مثل AR Cycle).

## مصفوفة دورة الحياة (الحالات الكمية)

```
الكمية: Original ──(Sale)──→ Sold
              └──(Disposal)──→ Disposed
Balance = Original − Sold − Disposed
الحالات: [نشط: Balance>0] → [مستنفد جزئياً] → [مستنفد: Balance=0]
                    ↓
        Zero Quantity checkbox في Fixed Asset List
```

## حواف دورة الحياة الموثقة/الغائبة

| الحافة | الحالة |
|---|---|
| أصل مستنفد يُباع (Residual = قيمة) | البيع عبر T-FX-03 بالكمية الصفرية؟ [NOT DOCUMENTED] |
| نقل أصل بين مواقع/فنادق | ❌ لا Transfer (الموقع جزء من الكود الآلي — ثابت بنيوياً!) |
| إعادة تقييم | ❌ |
| دمج/تفكيك أصول | ❌ (المكوّنات تُضاف لا تُفصل) |
| حذف معاملة بيع خاطئة | ❌ لا Cancel/Reverse موثق — **خطير في وحدة ترحيلية** |
