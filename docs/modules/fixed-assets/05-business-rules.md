# 05 — قواعد العمل (Business Rules) — وحدة FXD

> **BR-FX-01..22** — أعلى كثافة قواعد محاسبية مؤكدة في وحدة واحدة بعد FAS ذاتها: قفل بوابة أحادي · منهجان بحساب وواحد بترحيل · ترحيل شهري بتاريخ نهاية الشهر · تماثل الربط الرباعي · تعطيل اختيار P&L عند التساوي · قيمة اسمية صفرية كمفهوم فلسفي.

---

## القواعد المؤكدة (الموثقة نصاً)

| ID | القاعدة | المصدر الحرفي |
|---|---|---|
| **BR-FX-01** | **بوابة Start Date أحادية**: property-wise، لا تعديل بعد الحفظ، كل معاملة لاحقة > التاريخ | "Once its saved user cannot modify the same... Any transaction... will be greater than this date" (ص3-4) |
| **BR-FX-02** | **أصول ما قبل البوابة = افتتاحية**: تُسجل بـDepn. Op. Bal إذا بدأ إهلاكها قبل التحنيط | "The assets which are there earlier... opening balance assets" + حقل Depn. Op. Bal (ص2/9) |
| **BR-FX-03** | **كود الأصل آلي مركّب 12=5+3+4** بمسلسل لكل توليفة (فرعية×موقع) من FIMSHTBL | (ص7) |
| **BR-FX-04** | **الربط بالدليل اختياري** — لكنه شرط الترحيل: "If asset group linked to chart of account, then those assets transaction will be posted to financial module also" | (ص5) |
| **BR-FX-05** | **تماثل الربط الإلزامي**: أي حساب واحد مربوط → الأربعة إلزامية | "if balance sheet a/c is linked, then profit and loss a/c must be mandatorily linked" (ص5) |
| **BR-FX-06** | **التكامل المباشر مع Ledger Accounting**: ترحيل الإهلاك يحدّث P&L وBS معاً | "when depreciation is posted... the relevant profit & loss and balance sheet accounts are updated" (ص2) |
| **BR-FX-07** | **INI #475 يقرر المنهج المعتَمد** (SLM أو WDM) على مستوى النظام كله | "will consider either... based on the value of INI switch #475" (ص2) |
| **BR-FX-08** | **النسب تُعرَّف دائماً للمنهجين معاً** (SLM% وWDM%) على مستوى Sub Group أو Asset لكل FY | شاشة Method (ص10-11) |
| **BR-FX-09** | **الحساب قابل للاسترجاع**: "The calculated depreciation can be rolled back with roll back options" | (ص14) |
| **BR-FX-10** | **الترحيل شهري فقط** وبتاريخ نهاية الشهر | "Posting to FA will be done on monthly basis, where posting date will be month's end date" (ص16) |
| **BR-FX-11** | **الترحيل بمنهج SLM فقط** — WDV يُحسب ولا يُرحَّل | "posting of depreciation will be done on its straight line method of depreciation only" (ص16) |
| **BR-FX-12** | **غير المربوط يُبرز أزرق ويُستثنى** من الترحيل | "those assets posting will not be done and the same will be highlighted with blue color" (ص16) |
| **BR-FX-13** | **الترحيل بتجزئة Sub Group** حتى لو عُرض asset-wise | "Posting will be done as per sub group wise only" (ص17) |
| **BR-FX-14** | **المكوّن يزيد قيمة الأصل** | "The component added will increase the asset value" (ص11) |
| **BR-FX-15** | **بيع/استبعاد جزئي بالكمية** مع تتبع (Original – Sold – Disposed – Balance) | شبكة التفاصيل (ص14) |
| **BR-FX-16** | **Gain/Loss آلي بالاتجاهين**: Sale > Asset Value → ربح؛ أقل → خسارة | (ص14) |
| **BR-FX-17** | **التساوي يعطّل P&L**: "If asset value and sales value is equal, then profit and loss ledger selection will be deactivated" | (ص13) |
| **BR-FX-18** | **البيع يُرحَّل إلى Cash أو Bank** حسب Pay Mode؛ بطاقة الائتمان مؤجلة | "Sales amount will be posted to cash or bank account (credit card transaction option will be provided later)" (ص13) |
| **BR-FX-19** | **تجميع قيمة الإهلاك يرحَّل عبر ربط Sub Group** ("accumulated description posting ledger") | (ص13) |
| **BR-FX-20** | **Total Value = Quantity × Item Price** (آلي) | (ص9) |
| **BR-FX-21** | **Local Amount = Sale Amount × Exchange Rate** (آلي) | (ص14) |
| **BR-FX-22** | **القيمة الاسمية صفر عند نهاية العمر** كمفهوم إداري: أي تحصيل بعدها "nominal profit" | (ص2) |

## معادلات الوحدة (أعلى كثافة رياضية صريحة بعد HRP-PNT)

```
Total Value        = Quantity × Item Price                       (Master — آلي)
Local Amount       = Sale Amount × Exchange Rate                 (Transaction — آلي)
Asset Value        = Quantity × Item Price / Qty (من Master)     (Transaction — آلي)
Gain/Loss          = Sale Amount − Asset Value                   (اتجاه فقط موثق — آلي)
SLM (بالفترات)     = (Initial − Final) / Periods                 (مثال: (10,000−2,000)/10 = 800)
SLM (بالنسبة)      = % × القيمة كل فترة
WDV                = % × WDV المتناقص                            (مثال 40%: 30,000→18,000→10,800→6,480→3,888)
Net Book Value     = القيمة − مجمع الإهلاك                        [INFERENCE — يُعرض فقط]
```

## السلوكيات المشتقة (غير مصرّحة — مستنتجة من الحقول الآلية)

| الاستنتاج | الأساس | الدلالة |
|---|---|---|
| تعديل Item price/Qty في Master يعيد حساب Total Value فوراً | حقل آلي | القيمة قابلة للتصحيح ما لم تُرحَّل |
| Last date depn يتقدم مع كل حساب ناجح | حقل عرض فقط يتحدث | مؤشر تراكم داخلي |
| التمييز بين Last Dep. **Calc** Date وLast Dep. **Post** Date | حقلا عرض في FI Posting | **حساب بلا ترحيل ممكن** (ودليل الازدواج مقصود) |
| مسلسل FIMSHTBL لا يُعاد تدويره عند حذف الأصل (لا حذف موثق أصلاً) | غياب أي ذكر حذف | أرقام ميتة محتملة [UNCERTAIN] |
