# 08 — التقارير (Reports) — وحدة FXD

> **5 تقارير مطبوعة** (كل مسار الترحيل والتحليل يصب هنا) — نمط التقارير المبسّط: 1-3 معايير + زر عرض/طباعة؛ أثقلها **Dep Details (R)** بثلاثة أنماط تجميع واختيار طريقة الطباعة؛ ولا تقرير واحد يذكر أعمدة موصوفة أو 80/132 (على خلاف FNB) — تقارير محاسبية كلاسيكية موجزة التوثيق.

---

## الجرد

| # | التقرير | المدخلات الموثقة | المخرجات الموثقة | المصدر |
|---|---|---|---|---|
| R-FX-01 | **Depreciation Details (R)** | FY + From/To[MMYY] + **نوع: Asset/Group/Location** + طريقة الطباعة | "depreciation details of **all Assets** in the Property... calculated and displayed based on the **method and rate** defined in the Depreciation % menu option" | §15 ص20-21 |
| R-FX-02 | **Fixed Asset List** | From/To Date + **Asset By / Sub Group By / Location By** + **checkbox 'Zero Quantity Required'** | "a list of all Fixed Assets existing in the Property... **Detailed information**... on the basis of..." + "creates a **separate box list wise** according to the chosen option" | §16 ص21-22 |
| R-FX-03 | **Asset Transaction List** | FY | "list of all Asset wise transactions... transactions entered in the Fixed Assets Transaction entry" | §17 ص22 |
| R-FX-04 | **Asset Ledger** | FY + **Location أو By Group** | "vital information of Fixed Assets depreciation by Financial Year with **Actual Asset value as on date**" | §18 ص23 |
| R-FX-05 | **Asset Sales Register** | FY + **Sales أو Disposal** | "list of all Sales / Disposal of Assets... transactions entered in the Fixed Assets **Sales** entry" | §19 ص24 |

## ملاحظات تحليلية

| الملاحظة | الدلالة |
|---|---|
| **Q مقابل R للوظيفة نفسها** | Dep Details موجودة كاستعلام (ص18) وكطباعة (ص20) بمعايير متطابقة تقريباً — النمط المزدوج المعروف (تقارير FO/HRP) |
| **Zero Quantity Required** | checkbox فريد: إظهار الأصول المستنفدة (المرحَّلة بالكامل؟) — أداة تدقيق نهاية الحياة؛ [UNCERTAIN] هل Required = "أدرِج" أم "استثنِ"؟ الصياغة تحتمل الوجهين |
| **"separate box list wise"** | تبوّب فيزيائي داخل التقرير حسب خيار التجميع — نمط تجميع مطبعي نادر الوصف |
| **Asset Ledger** | أقرب تقرير لـ"دفتر الأصل": إهلاك السنة + القيمة الفعلية بتاريخ — **لا تواريخ as-on صريحة سواها** |
| Sales Register ثنائية القناة | اختيار Sales/Disposal يغذي تقريراً واحداً — بينما Transaction List يجمعهما معاً |
| **لا تقرير ميزانية/تخطيط** | لا مقارنة planned/actual — الوحدة تنفذ لا تخطط |
| **لا تقرير تاريخي للتسجيل** | تاريخ البيع/الاستبعاد فقط عبر Disposal History (Q) — راجع 09 |
| طريقة الطباعة | ذكرت مرة واحدة (R-FX-01) بلا جرد قيم — [NOT DOCUMENTED] |

## المخرجات الورقية المقترحة للمطابقة (بنية مستنتجة)

```
Fixed Asset List:  [Code | Names | Group | Location | Install Date | Qty | Value | Status]
Dep Details (R):   [Asset | FY | Month | SLM amount | WDV amount* | Rate]  *حسب INI#475
Asset Ledger:      [Asset | Opening | Period Depn | Accumulated | NBV as-on]
Sales Register:    [Tx# | Asset | Date | Qty | Sale Amount | Gain/Loss | Mode]
```
