# 08 — التقارير (Reports) — وحدة FNB

> **13 تقريراً** (REP 28 ص) — **أكبر كثافة تقارير لكل صفحة في المشروع** (تقرير لكل ~2.2 صفحة)، ببنية شاشة موحدة صارمة: **معايير → Preview → Generate**، و13 نمط توليد يتراوح بين جرد ورقي (Stock Sheet) وتحليل مالي مقارن (Sales Analysis/Cost Report). عائلتان: **تدقيق بيانات** (Checklists/Lists/Sheets) و**تحليل إدارة** (Analysis/Report/Variance).

---

## أ) عائلة تدقيق البيانات (7)

### R-FB-01: Recipe Checklist (REP ص2-3)
- **المعايير**: Recipe أو Sub Recipe · Restaurant · **Recipe # من-إلى**.
- **الوظيفة**: "generate a specified range of all recipes and sub recipes list that are entered using **menu items with similar names** and also based on the restaurants (POS Outlets)" — جرد الوصفات بأسماء مشابهة (مكافحة التكرار التسميات!).
- **ملاحظة المصدر**: "Recipe details are picked up from **RECIPE ITEMS** option. SUB RECIPE will generate the details **only based on SUB ITEMS created**".

### R-FB-02: Kitchen Stock Checklist (REP ص4-6)
- **المعايير**: نمط **(Opening Balance / Adjustment / Physical Stock)** · Date range · Cost Type · Cost Center · تجميع **By Location أو By Item**.
- **الوظيفة**: "details entered in the **Kitchen Stock Entry and the Outlet Opening Stock** options" — تقرير يوحّد مصدري الجرد والافتتاحي.

### R-FB-03: Kitchen Stock Statement (REP ص8-9)
- **المعايير**: Date · Cost Type · Kitchen · print quantity + نمط تجميع · **day / month / both**.
- **الوظيفة**: "statement of the **stock position** at the Kitchen/ Outlet... stock details **for each item** in the kitchen".

### R-FB-04: Stock Sheet (REP ص10-13)
- **المعايير**: Date · Cost Type · Kitchen · print quantity.
- **الوظيفة**: "a **Checklist** of the stock at the kitchen/ Outlet... related to the **item stock details**" — ورقة عدّ ورقية بالأساس.

### R-FB-05: Missing Recipe List (REP ص13-14) ⭐
- **المعايير**: Cost Type فقط — أبسط شاشة تقرير في الوحدة.
- **الوظيفة**: "generate a list of all Food and Beverage, Point of Sale items **for which recipes have not been specified**... displays a list of the **missing recipes**" — أداة اكتمال المحرك الوصفي (يجعل المنهج الوصفي قابلاً للإنجاز تدريجياً).

### R-FB-06: Inter Transfer Checklist (REP ص17-19)
- **المعايير**: Date range · **Transfer Type (Inter Kitchen transfer / Inter Cost Transfer / Value Transfer)** · ✓ Item Code Description Required.
- **الوظيفة**: "details of Inter kitchen transfers and Inter cost transfers" — مرآة أنماط التحويل الثلاثة في COP.

### R-FB-07: Manual Sales/Cons Report (REP ص27-28)
- **المعايير**: **(Manual Sales / Manual Consumption)** · Restaurant type · Date range · Cost Type.
- **الوظيفة**: "report of **sales done to the various outlets**... also a report of **consumption done at the various cost centers**" — تقرير مزدوج الوجه للإدخال اليدوي.

## ب) عائلة التحليل الإداري (6)

### R-FB-08: Sales Analysis (REP ص6-7) ⭐
- **المعايير**: Date · Outlet type · Session · الأصناف المنطبقة.
- **الوظيفة**: "Sales for a given Date made in **all F & B Outlets** at the property along with **covers** and **predefined budgets with variances**. Apart from for the day figures, **month and year figures are also reflected**" — أفق ثلاثي (يوم/شهر/سنة) + ميزانية/تباين — **أهم تقرير يومي إداري**.
- **الترابط**: يستهلك Sales/Cost Budgets (SET §3) مباشرة.

### R-FB-09: Physical Stock Variance (REP ص14-17)
- **المعايير**: Date range · Cost Type · Kitchen · **Item/Group range** · UOM (stock/conversion/both) · **All Items أو Physical stock items فقط** · ✓ طباعة تفاصيل الاستهلاك.
- **الوظيفة**: "the physical Stock Variance at the kitchen" — تقرير العجز/الفائض (قلب مكافحة التسرب).

### R-FB-10: Cost Report (REP ص19-21) ⭐⭐ (الأثقل)
- **المعايير**: **Report Format dd** (قيم غير معدودة — UNK-064) · Date range · **Forecast (budgeted number)** · Cost Type · ✓ Year to Date · ✓ **Kitchen Stock Not Required** · **Detail أو Summary**.
- **الوظيفة**: "to know the cost, based on **consumption/kitchen/potential or recipe**" — أربع كلمات مفتاحية، منها **"potential" بلا تعريف في أي مكان** (UNK-064) — التقرير الجامع للوحدة.

### R-FB-11: Standard vs. Actual (R) (REP ص22-23)
- **المعايير**: Date range · Item/Group Range · UOM (Stock/Conversion/both) · **80 أو 132 عموداً**.
- **الوظيفة والدلالة الحاسمة**: "analysis is made in terms of standard cost (consumption) and actual cost (recipe)... **Standard consumption is based on recipe details. Actual is arrived based on consumption at cost centers**" — النظري = الوصفة، الفعلي = الاستهلاك (والأقواس في العنوانين معكوسة — تناقض مسجل).
- **الإرث الطباعي**: خيارا العرض 80/132 عموداً — أطوار الطابعات الصفية!

### R-FB-12: Open Item/Modifier (R) (REP ص24-26)
- **المعايير**: Open Item أو Modifier · Date range · Cost Type · Restaurant · **UOM: Consumption أو Issue**.
- **الوظيفة**: "list of open items/modifiers... for a given date range, cost type and restaurant" — ثنائية UOM استهلاك/صرف جديدة (مقابل stock/conversion في الجرد!).

### R-FB-13: Print Buffet Information (REP ص26-27)
- **المعايير**: Date range · Outlet · Session · **اختيار الطابعة من قائمة** + Print.
- **الوظيفة**: "print the buffet information" — **التقرير التشغيلي الوحيد** (يذهب لطابعة المطبخ/البوفيه لا للمكتب) — بثالوث Session/Outlet/Date.

---

## أنماط عامة في حصيلة التقارير

| النمط | الدلالة |
|---|---|
| **Preview قبل Generate في 12/13** | نمط شاشة موحد (Buffet يستثني بPrint مباشر) |
| **ثلاث عائلات UOM**: Stock/Conversion (الجرد) · Consumption/Issue (المفتوح/المعدِّلات) · Print Quantity (Statement/Sheets) | ثراء وحدات قياس لا يتكرر إلا في TEL |
| **نطاقات From/To إلزامية** في نصف التقارير | عقلية دفعات لا استعلام آني حر |
| **لا تواريخ "نفس الشهر"** (مقابل TEL/SLM) | القيود الزمنية أرخى هنا (وحدة تحليل) |
| **لا Export/Excel موثق** (مقابل Parameter Listing في MNT!) | كل التقارير شاشة/طابعة فقط |
| **لا مخططات** (Charts) | كل الأرقام جداول — أعلى جفاف رقمي في المشروع بعد FAS-REP |
