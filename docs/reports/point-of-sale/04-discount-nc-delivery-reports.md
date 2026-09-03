# 04 — تقارير الخصومات وNC والتوصيل (§6/§12 + §11 + §7)

> ثلاث عائلات: الخصومات (المكررة مرتين!) · المبيعات غير الخاضعة للرسوم NC (4) · توصيل الطلبات DLV (3).

---

## 1. Discount Reports (§6.1–6.3) + القسم المزدوج (§12)

### 1.1 الجرد المقارن — التناقض المزدوج

| البند | **§6.1 Discount Register** | **§12 Discount Register** (المكرر!) |
|---|---|---|
| الصفحات | ص96-98 | ص103-105 |
| التاريخ | نطاق ≤ Accounting + **نفس الشهر** | نطاق ≤ Current + نفس الشهر |
| المرشحات | Outlet · **Settlement Mode** | **Discount % (رقم!)** · Outlet · **Session** · Settlement Mode |
| الأنماط | — | **By Bill XOR By Date** + **Show Session Total** + **Summary By: Reason / Cashier / Settlement Mode** |
| مصدر النص | "This report gives the list of all transactions where the discount is given on the bill amount" | "This report will allow the user to view the discounts given for a particular range of date restaurant, session and settlement mode wise" |

> **C-POS-01 (تناقض مسجل):** نفس الاسم "Discount Register" بقسمين مختلفين بمعايير مختلفة (§6.1 و§12) + كتلة §6 كلها واقعة فيزيائياً بعد §11 (خارج ترتيب TOC). الاحتمالات: تقريران مختلفان يتشاركان الاسم، أو نسختان تطوريتان لتقرير واحد. **القرار للتنفيذ:** يُعتمد §12 (الأغنى) ويُدمج فيه مرشح Settlement Mode من §6.1 — ويُسجل الغموض في unknowns (UNK-087).

### 1.2 محتوى Discount Register (من كلا الوصفين)

- تفاصيل الحركة: date · bill# · **bill amount · PAX · table# · settlement amount · settlement mode**.
- تفاصيل الخصم: **discount % · discountable amount · discounted amount · balance after the discount** — السلسلة المحاسبية الرباعية كاملة!
- **"Reason for allowing the discount and the User name who has allowed the discount"** — الخصم بسبب + مسؤول (تدقيق حوكمة الخصم).
- إجماليات يومية: bill/discount/balance.

### 1.3 Discount Summary (§6.2) وDiscount Summary (Reason) (§6.3)

- نفس الهيكل (menu type · نطاق · إجماليات يومية) مع إضافة **السبب** في 6.3.
- **C-POS-02 (خطأ تحريري):** ملاحظة SETUP في 6.2 تقول "select the Void and Complimentary options corresponding to **Sales By Item**" — نسخ/لصق من 1.1! الصواب المنطقي: Discount Summary.
- خيار Summary By (Reason/Cashier/Mode) في §12 يجعل 6.2/6.3 قابلتين للدمج فيه عملياً.

## 2. Non Chargeable (NC) Sales Reports (§11.1–11.4)

> سياق NC: مباعة بتكليف إداري (Complimentary/House/Staff...) دون تحصيل — راجع R-POS-05 (Session Statistics) للوحدة الأم.

| # | التقرير | المدخل | المخرج |
|---|---|---|---|
| 11.1 | **Non Chargeables by Date** | نطاق (نفس الشهر) + Outlet + **NC Type** dropdown | لكل تاريخ: مبلغ NC + **القسم المعني** (department it is applicable to) |
| 11.2 | **Non Chargeable Sales** | نطاق + Outlet + NC Type + **Menu Types checkboxes** + Print KOT Total | table# · guest name · KOT# · bill# · qty/value — **إجماليات KOT/Department/NC/Outlet أربعة** |
| 11.3 | **Non Chargeables Summary** | نطاق "within **any month**" (عبور شهور مسموح!) + Outlets + NC Type | NC كل نوع قائمة تحت منفذ/نوع NC/قسم + إجمالي عام |
| 11.4 | **NC Outlet Summary** | نطاق + NC Type + Outlets | إجمالي NC لكل قسم×منفذ |

**قاعدة 132 الإجبارية (11.4):**
> "Note: If more than **seven outlets** are selected, then print the report using **132 column format**."

- عتبة 7 منافذ → 132 عموداً إجبارياً (لا checkbox اختياري — إكراه عرض!) — مقابل حد **8 منافذ معالجة** في Sales By Group (1.4): عتبات جوار متقاربة (7/8) بمنطقين مختلفين (عرض إجباري vs معالجة).
- **11.3 عبور الشهور**: "within any month" — صياغة تعني أي شهر (السماح بأي فترة؟) مقابل "within the same month" في 11.1/11.2 — انتبه تحريري مُسجل في مصفوفة التواريخ.

**NC Type**: قائمة ممنوعة من POS-SET (أنواع NC: Complimentary/House-Consumption/Spollage... راجع FNB-LUK NC Query ثلاثي المحاور) — REP يستهلكها كـdropdown دون تعريف.

## 3. Delivery Reports (§7.1–7.3) — نافذة CRM التوصيل

> "Delivery sales related reports where you can view the **customer's menu orders and delivery details** by Item, Area or Time" — التوصيل بمنطق **Area (منطقة)** — أول تجزئة جغرافية في طبقات التقارير.

| # | التقرير | المدخل | المخرج |
|---|---|---|---|
| 7.1 | **DLV Frequency Report** | Date ≤ Current · **Area list** · Summary checkbox · **4 قنوات إخراج معلنة** | لكل منطقة: **customer name · id · address · telephone** + **count & amount of orders** + إجماليات المنطقة + الإجمالي العام — **بِطاقة عميل جغرافية** |
| 7.2 | **DLV Item Details** | نطاق + **Customer Id** (F1 Help — "system generated when a customer places an Order for delivery") | الأصناف الموصلة لكل عميل (code/qty/value) + bill/bill date/settlement mode/net after discounts |
| 7.3 | **DLV Monthly Frequency** | **نطاق Month/Year** (≤ Current Month/Year) + Areas + **Report Type: Frequency XOR Sales** | لكل شهر×منطقة: عدد مرات الطلب أو إجمالي المبيعات + إجماليات أعمدة/صفوف |

**الدلالات:**

1. **Customer Id للطلبات مولّد آلياً** — سجل عميل توصيل دائم (وليس عابراً) يولد عند أول طلب — نافذة صغيرة على متجر عملاء POS التوصيل.
2. منطق **Frequency vs Sales** (7.3) نفس ثنائية الكم/القيمة في Popularity — عائلة تكرار الاستعمال.
3. عائلة DLV **بلا قيد same-month** — أوسع نطاقاً من عائلة المبيعات (7.2 نطاق حر ≤ Current).

## 4. الأنماط العابرة في الملف كله

| النمط | الشاهد | المواضع |
|---|---|---|
| **مسؤول السماح بالخصم** | "User name who has allowed the discount" | 6.1 — أثر مستخدم بنوع حادثة (السماح) وليس فقط الإدخال |
| **السلسلة الرباعية للخصم** | discountable → discounted → balance | 6.1 |
| **عتبة العرض 7 منافذ → 132** | إكراه لا خيار | 11.4 |
| **NC بأثر قسم** | "the department it is applicable to" | 11.1 — تحميل تكلفة/مسؤولية NC على القسم |
| **Area كبعد تجميع** | Delivery كلها | 7.x |
| **الهاتف والعنوان في تقارير POS** | 7.1 | بيانات اتصال عميل داخل تقرير مبيعات — ذكر نادر |
