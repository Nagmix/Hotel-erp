# 06 — قيود الإدخال والتحقق (Validations) — وحدة FXD

> **V-FX-01..13** — قيد إدخال محاسبي واحد صريح (تماثل الربط) + قيود هيكلية موثقة بالأطوال والتواريخ والآلية + قيد سلوكي فريد (**تعطيل** اختيار P&L عند التساوي — أول حقل يُطفأ بقاعدة عمل لا بخفاء دائم).

---

## القيود الموثقة

| ID | القيد | السلوك عند المخالفة | المصدر |
|---|---|---|---|
| **V-FX-01** | **تماثل الربط الرباعي**: ربط حساب واحد في Sub Group يستلزم ربط البقية | "program will validate" — منع الحفظ | ص5 |
| **V-FX-02** | Start Date **لا يُعدَّل** بعد الحفظ | الحقل مقفل | ص3-4 |
| **V-FX-03** | كود Main Group **لا يُعدَّل** بعد الإنشاء | الحقل مقفل | ص4 |
| **V-FX-04** | Asset code آلي 12 محرفاً (5+3+4) | لا إدخال يدوي أصلاً | ص7 |
| **V-FX-05** | Sub Group code **5 محارف** (F1) | رفض غير المطابق | ص7 |
| **V-FX-06** | Long name ≤ 70 · Manufacturer ≤ 60 · Long/Short في الماسترات 30/10 | حدود النصوص | ص4-7 |
| **V-FX-07** | **Date installation ≤ server date** | "Should be less than or equal to" — رفض | ص8 |
| **V-FX-08** | Currency افتراضية محلية + Rate آلي بالعامل | قيد هيكلي | ص8 |
| **V-FX-09** | **Depn. Op. Bal شرطي**: يُدخل فقط إذا start date depn < FA start date | "should be defined **if**..." | ص9 |
| **V-FX-10** | حقول PO/GRR/Bill "can be defined as **mandatory**, with INI switch validation" | التفعيل بمفتاح INI (غير مرقم) | ص9 |
| **V-FX-11** | كل معاملة > FA Start Date | منع زمني | ص3 |
| **V-FX-12** | Quantity البيع/الاستبعاد ≤ Balance Quantity المتاحة | ضمن شبكة التفاصيل (الأصل محسوب ومعروض) | ص14 |
| **V-FX-13** | **تساوي البيع مع القيمة → تعطيل اختيار P&L ledger** | حقل يُطفأ بقاعدة | ص13 |

## التحققات الآلية (حقول محسوبة لا تقبل الإدخال)

| الحقل | المعادلة | موضع الحماية |
|---|---|---|
| Total Value | Qty × Item Price | Master |
| Currency rate | عامل العملة | Master + Component + Transaction |
| Exchange amount | Amount × Rate | Component Entry |
| Asset code | FIMSHTBL | Master |
| Local Amount | Sale × Rate | Transaction |
| Asset Value | Qty × Item Price من Master | Transaction |
| Gain/Loss Amount | Sale vs Asset Value | Transaction |
| Last date depn | نظام | Master (عرض) |
| Current closing (Qty balance, NBV, Total Depn) | نظام | Master (عرض) |

## ثغرات تحقق موثقة الغياب (راجع 17)

| الغياب | الخطر |
|---|---|
| لا تحقق موثق أن **Residual Value < Item Price** | إهلاك سالب نظرياً |
| لا تحقق أن **Life span > 0** أو أن الفترة تتفق مع النسبة | انقسام منهجي SLM بالفترات مقابل النسب |
| لا تحقق **Quantity > 0** | أصل بلا كمية |
| لا منع **بيع أصل لم يُحسب إهلاكه** | قيمة دفترية غير محدثة عند البيع |
| لا تحقق توافق **Transaction Type** في FI Posting مع م المحسوب مسبقاً | ترحيل مزدوج/ناقص محتمل |
| لا تأكيد Save في FI Posting (Load ثم Save بلا Confirm) | ترحيل غير مقصود |
