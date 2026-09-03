# 05 — تقارير الضرائب والامتثال الهندي (§16.1–16.5 + §9 PAN)

> خمسة تقارير ضريبية + تقرير PAN الهندي — أثقل كتلة امتثال في طبقات REP بعد أمن FO (C-Form/Police).

---

## 1. Tax Reports (§16)

### 1.1 Tax Register (§16.1) — الأعمدة بنسب مئوية

| البند | القيمة |
|---|---|
| المدخل | نطاق (نفس الشهر) + Outlet + **Tax type** + **By Bill# / By Date / Consolidated** |
| البنية العمودية | "If the tax type is **VAT and two tax percentages are defined under VAT - 10% and 12%**, then... the turnover and tax amount for the first tax percentage will be displayed in the **first column**, ...second... **second column** and in the **third column, the total** turnover and tax amount" |

**الدلالة:** الأعمدة **تولد ديناميكياً من نسب الضريبة** المعرّفة تحت النوع (Tax% × Tax Type) — بنية Pivot حقيقية: (turnover, tax) لكل نسبة + عمود إجمالي. لا تقرير آخر في الحزمة يولّد أعمدته من بيانات الإعداد هكذا.

- By Bill → يعرض bill# وPAX لكل فاتورة · By Date → إجمالي الفواتير لكل تاريخ · Consolidated → إجمالي النطاق كله.
- **لاحظ**: خيار Void/Complimentary هنا **inline في شاشة التقرير نفسه** (خطوة 4) وليس فقط في مصفوفة SETUP — مساران متوازيان.

### 1.2 Tax Register (All) (§16.2) — الأنواع المتعددة

- نفس المدخلات + **Page Skip** + **Tax List باختيار متعدد** ("You have the option to select multiple tax types") — المرحلة الثانية من الشاشة تعرض قائمة الضرائب بعد Continue.
- لكل منفذ: bill amount + discount amount + tax amount لكل ضريبة مختارة — **الخصم مجاور للضريبة** (منظور الوعاء).

### 1.3 Tax Breakup (§16.3) — التركيب اليومي

- **Details XOR Summary**.
- لكل تاريخ: عدد الفواتير · bill amount · **taxable amount** · مبالغ كل ضريبة · **"amount rounded off to"** · **non taxable amount** — أغلى سطر ضريبي يومي (6 مقاطع).
- Details = تفكيك كل الفواتير تحت كل تاريخ · Summary = إجمالي كل تاريخ.

### 1.4 Non – Taxable Turnover (§16.4) — المعفى + تعريف City Ledger

- المدخل: نطاق + Outlets + **Tax Code** + **All Settlements / Cash Settlement / City Ledger**.
- **التعريف الحرفي الأثري:** "(**City Ledger** - where the bills of the Guest are debited to his Company)" — تعريف AR داخل تقرير ضريبي!
- المخرج: مبيعات كل مجموعة قائمة غير خاضعة (non taxable) لكل تاريخ تحت كل منفذ + إجماليات.

**الدلالة:** تصنيف الإعفاء الضريبي **مربوط بنمط التسوية** (Cash vs City Ledger) — أي أن الوعاء المعفى قد يختلف بحسب من دفع! (تحليل امتثالي نادر).

### 1.5 Tax Exemption (§16.5) — المُعفى صراحة

- "sales on which the **tax is exempted (waived off)**" — إعفاء بقرار (تنازل) وليس طبيعة الصنف.
- لكل فاتورة: bill# · date · bill amount · **tax exempted amount under each tax** + الإجمالي المعفى من كل الضرائب — إجماليات بحسب الجلسة والمنفذ.

> **ثلاثية المفاهيم الضريبية في POS-REP:** Non-Taxable (غير خاضع بطبيعته، 16.4) · Tax Exemption (خاضع لكن أُعفي، 16.5) · Tax Breakup (التفكيك الكامل، 16.3) — منظومة مفاهيم كاملة يلخصها عمود non taxable amount في 16.3.

## 2. Print PAN Information (§9) — امتثال هندي صريح

> "This report gives the list of all such settlements where the **PAN information of the Guest has been requested for exceeding the bill amount**. (Note: The PAN information is required for settlements above the prescribed limit. **This is affected by Switch 137**.)"
> "Note: **This option is applicable only for Indian Government.**"

| البند | القيمة |
|---|---|
| PAN | Permanent Account Number — الرقم الضريبي الشخصي الهندي |
| العتبة | "prescribed limit" — **قيمتها غير موثقة** → UNK-085 |
| المفتاح | **INI Switch 137** (رابع مفتاح INI تكتشفه REP-POS: 137/335 + المتوارثة 368/511 من FNB) |
| المدخل | Date (≤ Accounting **across months** — عبور شهور!) + Outlet |
| المخرج | bill# · guest name · **guest's address** · bill amount · **date of payment** · **mode of payment** · **PAN** |

**الدلالات:**

1. الربط **Switch → سلوك التقاط** (طلب PAN عند تجاوز الحد) → تقرير يعرض من طُلب منهم — سلسلة: مفتاح نظامي → تحقق إدخال → تدقيق امتثال.
2. عبور الشهور في التاريخ ("across months") — استثناء ضمن عائلة same-month.
3. التقارير الممولة جغرافياً: POS تتبع FO (C-Form/RBI-RLM/Income-Tax) في تخصيص الهند — لكن هنا بصراحة "applicable only for Indian Government" (إعلان سوق مستهدف!).

## 3. خريطة الضرائب عبر المشروع (بعد POS-REP)

| الوحدة | الطبقة الضريبية | الشاهد |
|---|---|---|
| POS-SET | تعريف Tax Type/النسب/الربط | (ماستر — راجع modules/point-of-sale) |
| **POS-REP** | **الخمسة + PAN** | هذا الملف |
| FO-REP | **Consolidated Tax Register (FO×POS!)** | 94 — "FO + POS معاً" (راجع 03-security في FO) |
| FNB-REP | Consolidated Tax في تقارير التكلفة | (راجع food-beverage-costing) |
| FAS | ترحيل الضرائب للدفاتر | Tax posting rules |

> جسر جديد يكتمل: Tax Register (POS) هو **المصدر التفصيلي** الذي يجمعه FO-REP 94 على مستوى الفندق — العلاقة Detail(POS)→Consolidated(FO) موثقة الآن من الطرفين.

## 4. ملاحظات تحويل سريعة

- 16.1 → تقرير **Pivot** على Sales Invoice taxes (الأعمدة من جدول Item Tax Template/نسب الضرائب) — Script Report.
- 16.4 → فلترة حسب وضع الدفع + تصنيف UOM الضريبي (is_taxable) — يحتاج Custom Field.
- §9 PAN → حقل PAN إلزامي شرطي على POS Invoice عند تجاوز عتبة إعداد (Feature Flag نقدي بدل INI) + تقرير امتثال.
