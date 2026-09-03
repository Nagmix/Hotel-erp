# 09 — الاستعلامات (Lookups) — وحدة FNB

> **7 استعلامات** (LUK 15 ص) — استعلامات **تحريرية-عرضية مختلطة**: أحدها يبني ربطاً من داخل شاشة العرض (Open/Modifiers — Lookup-as-Editor)، وواحد يُحيل لبناء الوصفات (زر Recipe Master)، والبقية تنقيب بعمق درجي معلن الحدود ("No Drill Down Available for this Category").

---

## L-FB-01: Item Recipe Details (LUK ص2-4)

- **المعايير**: Outlet · Cost Type · **FROM/TO date + FROM/TO item** (نطاقان مزدوجان).
- **الشرط المسبق**: "details are reflected **after the Sales/ Cost Extraction is processed**" — الاستعلام ابن الاستخراج.
- **النطاق**: "item wise sales details in terms of **quantity & value** along with the cost details **only for items to which recipes have been specified**".
- **التنقيب**: "Press **F3** to view Recipe details. Double-click on any of the records" — مستوى تفصيل الوصفة من داخل الاستعلام.

## L-FB-02: Recipe Details (LUK ص4-5)

- **المعايير**: Outlet · **Menu Type** → **Load**.
- **النطاق**: "all menu items defined at the POS outlets **for which recipes are defined and also those for which the recipes are not defined**" (عكس L-FB-01 عمداً!) · "outlet wise or menu type wise".
- **الإجماليات**: "Consumption Total, Selling Price Total and the **Cost % Total**".
- **التنقيب**: "Double-click on the records to view the recipe details. (If the recipe is **not defined, then you cannot view the details**)".
- **⭐ الإحالة البنّاءة**: "Recipe Master – Select this option to **add a recipe or a sub recipe** to the menu types... refer CHAPTER – SETUP of this Module" — استعلام يقود للبناء (قناة اكتشاف النقص → إصلاح فوري).

## L-FB-03: Non-Chargeable Query (LUK ص5-7)

- **المعايير**: Date (يوم واحد) · Cost Type · Outlet · **NC Type**.
- **القائمة الموثقة**: "(They can be **Complimentary, Spoilage or for House Consumption etc.**)" — ثلاث قيم + "etc." مفتوحة (UNK-066).
- **المخرجات**: "Non-chargeable item details with **KOT type summary / restaurant summary / kitchen summary**" + "total cost price for each Restaurant Type, Kitchen Type and KOT Types **separately** and also the **Summary** of these" — بنية مزدوجة (تفصيل + ملخص ثلاثي المحاور).
- **الأثر التحليلي**: تجميع تكلفة المبيعات غير المحصَّلة — عين مكافحة الإساءة (مجاني/تلف/داخلي).

## L-FB-04: Recipe–Ingredient Details (LUK ص7-8)

- **المعايير**: Recipe Name dd · Date · Item (Help) · KOT Type → Load.
- **النطاق**: "all the recipes and the ingredients of the recipes... item wise and **KOT Type wise**".
- **زر Consolidate**: "Click Consolidate to view a **consolidated list** of recipes and their ingredients" — تجميع إجمالي المكونات عبر الوصفات (أساس Auto Indent عقلياً!).
- **التنقيب**: double-click → تفاصيل الوصفة.

## L-FB-05: Stock Query (LUK ص8-11)

- **المعايير**: FROM/TO date · Cost Type · Kitchen · خيار تجميع · نطاق item/group · **Quantity: Stock UOM أو Conversion UOM**.
- **الوظيفة**: "stock position at the kitchen for a **specified date range**... processed on the basis of cost types" + "Options are provided to **print** the quantity on stock, conversion UOM or **both**".
- **التنقيب والطباعة**: "Double-click on any of the records to view the **item stock details**" + Print → تقريران مختلفان حسب اختيار UOM — استعلام بمساري مخرجات.

## L-FB-06: Standard Vs. Actual (Q) (LUK ص12-13)

- **المعايير**: Date range · **Item Range أو Group Range** · F1 (Store Code + Item Name) · Print Quantity UOM.
- **الوظيفة**: "comparison of cost report where analysis in terms of **Standard Cost (Consumption) and Actual Cost (Recipe)**" — ⚠️ الأقواس هنا معكوسة الدلالة عن متن REP#10 (التناقض المسجل C-FB-01)؛ المرجع الحاسم REP ص22.
- **التنقيب**: double-click → التفاصيل.

## L-FB-07: Profitability Analysis (LUK ص13-15) ⭐

- **المعايير**: Date range · Property · Cost Type · **Kitchen/Restaurant** · **Consumption Type (Issue Based / Recipe Based)**.
- **قيد XOR الصارم**: "if you select the option **Issue Based then you cannot select the Restaurant** option. If you select the option **Recipe Based then you cannot select the option Kitchen**" (LUK ص14) — المنهج يحدد بُعد التحليل!
- **Link Help**: "Click **Link Help** to link the Restaurant/Cost Center and Kitchen" — مساعد الربط مدمج في الاستعلام (المقابل التشغيلي لشاشة Costing Link).
- **نهاية التنقيب المعلنة**: "If there are not further details, you get the message **'No Drill Down Available for this Category'**" — رسالة حدود نادرة الصراحة.

---

## أنماط عائلة الاستعلامات

| النمط | الدلالة |
|---|---|
| **Load/Generate + double-click drill** | موحد في 7/7 — عمق درجي بمستويين غالباً |
| **استعلام يحرِّر**: L-FB-08 (Open/Modifiers في COP ص15-16) يبني الربط كاملاً من شاشة العرض | ثالث Lookup-as-Console بعد TEL/MNT — لكن هنا بناء بيانات (وليس تعديل حالة!) |
| **استعلام يُحيل للبناء**: L-FB-02 (زر Recipe Master) | قناة اكتشاف-إصلاح |
| **رسائل حدود معلنة** | "No Drill Down Available for this Category" — نظافة UX نادرة |
| **اعتماد ما بعد الاستخراج** (L-FB-01) | ترتيب بياني: Extraction → Lookups → Reports |
