# 02 — قوائم الأصناف والموردين والعقود + تفاصيل الصنف — MGT-REP (Phase 7)

> §1 (≡6.1) + 6.2/6.3/6.4 + §9.1–9.4 = 8 تقارير أوراق — "طبقة الدليل المرجعي" لماسترات MGT.

---

## 1. §1 Inventory Item List (≡ §6.1 — C-MR-02)

**الوصف الحرفي:** "you can generate details of items entered in the Inventory Items. You can generate the list for all or specific stores and on item type which is optional. The information processed here can be based on sequence of Item Code/Name/Group/Physical Location/Last Updated."

**المعايير (ص4-5):**

| # | المعيار | القيم |
|---|---|---|
| 1 | Store | قائمة — أو الكل |
| 2 | Item Type | اختياري |
| 3 | Sequence + Range | **Item Code / Name / Group / Physical Location / Last Updated** (خمسة مفاتيح تسلسل!) |
| 4 | Passive Records | Checkbox — تضمين الخامل |

**النقاط البنيوية:**
- **Physical Location** كمفتاح تسلسل — الموقع الفيزيائي داخل المخزن (ماستر MGT-SET) يصبح مفتاح عرض — تقرير "جرد رفّ" ضمني.
- **Last Updated** كمفتاح تسلسل — تتبع الميتاداتا التحريرية (آخر تحديث) — أول تسلسل بميتاداتا في الحزمة.
- **الازدواج الحرفي**: §6.1 (ص46-48) يكرر **نفس النص والخطوات والمعايير** كلمة بكلمة — C-MR-02 (الكتالوغ يضم نسختين من نفس التقرير تحت رقمين).

## 2. §6.2 Item List by Vendor

**الوصف:** "view the list of items based on each vendor. The user have the option to view contract or open items."

- فلتر **ثلاثي**: All Items / Contract Items / Open Items — يعكس ثنائية العقد في Vendor Contract Master (SET §6).
- Sequence + Range — نفس نمط §1 لكن بلا Passive.
- جسر ضمني: الأصناف-حسب-المورد = انعكاس علاقة Item↔Vendor من ماستر MGT-SET (Vendor-Item linking بالعقود).

## 3. §6.3 Vendor List — أعمق تقرير ماستر في الوحدة

**الوصف:** "view the list of vendors based on regular details/black listed details or last updated details. The user have the option to search the vendor details based on Vendor Code or Vendor Name."

**فضاء المعايير (3 أبعاد × قيم):**

| البعد | القيم |
|---|---|
| **نوع التفاصيل** | Regular Details / **Black List Details** / Last Updated |
| **منظور العرض** | standard / payment / **bank** / contract / **tax** (خمس مناظير!) |
| **الترتيب** | By Vendor Code / Vendor Name + Range |

**النقاط البنيوية:**
- **Black List Details** — المورد المحظور له تقرير مستقل: آلية حظر الموردين (من SET Vendor Master) قابلة للتدقيق والعرض — عنصر حوكمة مشتريات موثق.
- **5 مناظير** لبطاقة المورد (قياسية/دفع/بنك/عقد/ضريبة) — أوسع منظور ماستر في تقارير الحزمة (يقابل توزيع حقول ماستر المورد عبر شاشات SET).
- آخر ثلاثي: Regular/BlackList/LastUpdated — نفس عائلة (حالي/محذوف-محظور/ميتاداتا).

## 4. §6.4 Contract List

**الوصف:** "view the contractors list that can be viewed by vendors, contract numbers or by expiry date of the contracts."

- ثلاثة مفاتيح عرض: **By Vendor / By Contract Number / By Expiry Date** + النطاق المقابل.
- **الملاحظة الحرفية:** "If you select the option **By Item under Vendor option**, select the store and enter the items range." — وضع رابع مدفون في Note: العرض **حسب الصنف تحت المورد** (أي فحص عقود موردٍ بعينها لأصناف بعينها في مخزن بعينه — استعلام تقاطعي ثلاثي الأبعاد).
- **Expiry Date** كمفتاح — تتبع انتهاء العقود (إنذار تجديد ضمني) — يقابل Contract Master في SET §6.

## 5. §9.1 Item Stock Details

**الوصف:** "view stock details of Items of a specific Store, Transaction (Receipts, Issues, Receipt Return etc), UOM etc for a given Date Range."

- **ثلاث مستويات إخراج**: By Item / By Group / **Group Summary**.
- فلتران تضمينيان: **Direct Items** + **Open Items** (Direct = غير مخزني يُستهلك فور الاستلام — ثنائية Stockable/Direct من ماستر SET).
- يتكامل مع LUK "Item Stock Status/Balance" (استعلامات سريعة) لكن بعمود UOM ومعايير أوسع.

## 6. §9.2 Item Stock Levels — تقرير المواءمة مع حدود المخزون

**الوصف الحرفي:** "view Item Stock levels which can be used for the analysis of the Stock position of the Items **in comparison to the Minimum, Maximum and Re-order levels specified in the Inventory Items for Stockable type of Items**."

- **مقصور على Stockable** — الأصناف المباشرة خارج نطاقه منطقياً (لا حدود لها).
- "Select an option from the **available item levels**" — مستويات متعددة قابلة للاختيار (تقاطع الرصيد مع Min/Max/Re-order — أي فوق/تحت/ضمن الحدود).
- **الجسر التشغيلي الأهم مع §17**: هذا التحليل التحضيري + Re-Order Level Items (§17) = دورة إعادة الطلب: تحليل → إنذار → طلب (PR/Indent).

## 7. §9.3 Ledger by Item — دفتر الصنف

**الوصف:** "view all the transaction details of each item in a specified Store. The user can view these details for a range of Items or Groups for a specified Date or Month range. The user can also view **Zero transaction details**."

- **دفاتر المادة (Item Ledger)** = قلب OLTP التتبع — يقابل Store Ledger (18.4) الذي يعمل على مستوى المخزن كله بعد Process.
- وضع **Zero transactions** — إظهار الأصناف عديمة الحركة في الفترة (الوجه الآخر لNon Moving §14 لكن داخل دفتر!).
- ثنائية **Date / Month range** — نفس مفتاح §4/§5.
- الشاشة موثقة بعبارة عامة: "Select the appropriate options for each fields as shown in the below screen" (ص65-66) — أفق الوصف العام.

## 8. §9.4 Item Expiry List — إنذار الصلاحية المبكر

**الوصف الحرفي:** "view a list of expired (unusable) Items for a specified date range and is based on the details entered in the **Receipt Entry**. The Item Expiry List will be **populated on time based on the number of days entered for a specific store**."

**تفكيك:**
1. **مصدر البيانات = Receipt Entry** — تاريخ انتهاء الصلاحية يُسجَّل عند الاستلام (Batch tracking من SET/Transactions).
2. **الإنذار المبكر**: "populated on time based on the number of days entered" — إدخال **N أيام** يجعل القائمة تجلب الأصناف التي ستنتهي خلالها — إنذار استباقي وليس حصراً بعد الفوات.
3. "for a specific store" — عتبة الأيام **لكل مخزن** (تخصيص حساسية الإنذار حسب المخزن — مخزن الأغذية أكثر حساسية من العتاد).
4. تسلسل Group/Item + نطاق.

**الجسر**: يلتقي مع **Batch Balance** في Closing Stock by Type (§6') — إدارة الصلاحية = إدارة الدفعات — عائلة كاملة غير موجودة في FO/POS إطلاقاً.

## 9. جدول التجميع

| التقرير | المفتاح الفريد | الفلتر المميز | جسر |
|---|---|---|---|
| 1 Inventory Item List | **Last Updated/Physical Location** كتسلسل | Passive | SET Items |
| 6.2 Item List by Vendor | Vendor | **Contract/Open** | SET Contracts |
| 6.3 Vendor List | 5 مناظير × 3 تفاصيل | **Black List** | SET Vendor Master |
| 6.4 Contract List | **By Expiry Date** | By Item under Vendor | SET Contracts |
| 9.1 Item Stock Details | Item/Group/Summary | **Direct + Open** | TRN Receipts/Issues |
| 9.2 Item Stock Levels | **Min/Max/Re-order** | Stockable فقط | SET Items limits |
| 9.3 Ledger by Item | كل الحركات | **Zero transactions** | TRN all |
| 9.4 Item Expiry List | **N أيام إنذار** | Store-specific | TRN Receipt (Batch) |
