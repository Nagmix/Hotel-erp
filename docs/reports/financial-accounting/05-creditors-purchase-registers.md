# 05 — سجلات الدائنين والمشتريات والمصروفات — FAS-REP (Phase 7)

> §10 Creditors Outstanding + §11 Purchase Tax Register + §12 Purchase Register + §13 Expense Register + §15 Debit Note Print + §16 Contract Debit Note List = 6 تقارير — الوجه الدائني للمشتريات.

---

## 1. §10 Creditors Outstanding — **أعمار الدائنين**

**الوصف:** "details of outstanding Bills for all or specific Vendors for a given Month & Year **based on the Ageing period**. A **Detailed or Summary** of the outstanding information can be processed."

| # | المعيار |
|---|---|
| 1 | Property + FY + **Account Code** |
| 2 | Vendor Selection: **Range / Selection** |
| 3 | الفترة: **As On / Month / Date** (ثلاثية!) |
| 4 | Net Balance: **Debit / Credit / Both** |
| 5 | Print sequence: **by bill or Doc date** · Summary/Detail |
| 6 | Ok |

**النقاط البنيوية:**
- **Ageing الدائنين** — النظير المحاسبي ل ageing المدينين في ACR (Debtors Follow-Up بالجلسة القديمة) — **ثنائية الأعمار الكاملة للميزانية التجارية**: ACR (مدينون) + FAS-10 (دائنون).
- **As On / Month / Date** — ثلاثية وضع الفترة (نقطي/شهري/تاريخ حر) — أوسع من ثنائية as-on/range.
- Net Balance **بالثلاث** (Debit/Credit/Both) — رصيد صافٍ بمقصد مدين أو دائن (مورد له رصيد مدين = مسترد!).

## 2. §11 Purchase Tax Register

**الوصف:** "reflects **all taxable items** that are purchased for a Property. It generates a list of all purchased items upon which certain type of **tax structure has been imposed**."

- المعايير: Property + date range + **أنواع الضرائب** + **رقم الضريبة: "Number or Service Charge number and Value Added Tax number"**.
- **ثلاثية أرقام الضريبة**: Register Number / **Service Charge Number** / **VAT Number** — نفس الثلاثية تظهر في Expense Register (§13) — **معجم أرقام الضريبة الموحد** (رقم السجل / رقم الخدمة / رقم VAT).
- الوجه المالي لـMGT-24 VAT (استلامي) — عائلة ضريبية ثلاثية عبر الوحدات: MGT-24.1 (استلام) · MGT-24.2 (شبح توأم) · FAS-11 (سجل شرائي).

## 3. §12 Purchase Register — **أبسط تقرير في الوحدة**

"maintain all purchase records of goods pertaining to an individual property." — المعايير: **Property + date range + Ok** (معيارين!).

- أبسط تقرير FAS (وفي الحزمة كلاها مع MGT-4.8 وFAS-3) — **سجل المشتريات الخام** بلا أي بعد (لا مورد/لا مجموعة/لا ضريبة) — مقابل سجلات MGT متعددة الزوايا — النقاء الشامل هنا والاشتت هناك.

## 4. §13 Expense Register — **عتبة المبلغ "Above"**

**الوصف:** "all expenses borne by a property or company... detail description about all expenses that have occurred during a particular financial year/period."

| # | المعيار |
|---|---|
| 1 | Property (auto-populate — "The Property name **will auto populate**... If there is more than one property... select") |
| 2 | Financial Period (**Enter أو F3**) |
| 3 | date range |
| 4 | **Above**: "enter the minimum expense amount. (**All expenses above the mentioned amount will be shown**)" |
| 5 | All Vendors / **Vendor Range** (F1) — "(You have to select vendors, **as the payments to be done to the vendors is an expense** to the Property)" |
| 6 | **رقم الطباعة: Number (auto) / Service Charge Number / VAT Number** |

**النقاط البنيوية:**
- **عتبة Above** — فلتر حد أدنى للمصروف (تركيز على الكبير!) — نفس Minimum Amount في Detail Register (§17) — عائلة عتبة مبلغية ×2.
- **التعليل المحاسبي الموثق**: لماذا الموردون؟ — "المدفوع للموردين هو مصروف للملك" — **جملة تعليمية نادرة** (الوثيقة تشرح المنطق لا الخطوات فقط).
- **auto-populate** للملك (سياق محلي افتراضي ثانٍ بعد LB).

## 5. §15 Debit Note Print — **قصة العقد الاقتصادية كاملة + Tag/Load**

**الوصف الحرفية (الاقتصاد كاملاً):**
> "These Vendors do supply all stuffs to the hotel at a **specified rate for a fixed time period as per contract** signed between the two parties. During the contract period, in case there is **any price fluctuation or the vendor's inability to supply the items**, the hotel purchases the same from **different vendor or open market**. **If the rate of the item purchased is higher than the contract rate, then difference in the rate will be debited to the contract vendor using the Contract Debit Note option**."

**دورة العمل الكاملة:**
```
عقد مورد (سعر ثابت/مدة) → تقلب سعر أو عجز مورد
   → شراء بديل من مورد آخر/سوق مفتوح بسعر أعلى
   → الفرق (سعر السوق − سعر العقد) يُحمَّل على مورد العقد
   → Contract Debit Note (طباعة هنا بالموسومة)
```

| # | المعيار |
|---|---|
| 1 | **Vendor contract code** من قائمة |
| 2 | **Date أو Debit Note** (ثنائية استرجاع) |
| 3 | Date + نطاق |
| 4 | Printer type |
| 5 | **Load** — "The data will display" |
| 6 | **Tag → Yes** (double-click تحت عمود Tag) |
| 7 | Ok |

- **أول Tag/Load في الوحدة** (تُفصّل في 01 §4).
- جسر MGT ثلاثي: العقود (SET Contracts) · Standing PO (تعهد يومي) · Comparative (مقارنة عطاءات) — **الاقتصاد التعاقدي المخزني يكتمل محاسبياً بمذكرة خصم**.

## 6. §16 Contract Debit Note List — **الأعمدة المعلنة كاملة**

**الوصف:** "list of transactions posted through the Contract Debit Note option... Information processed includes the **debit note date / number, GRN number / date, vendor name, item code /name, currency, deference value, debit value, and waive amount along with debit note total and grand total**."

- **أعمدة نصية كاملة** (ثاني تقرير بعد Detail Register) — **GRN number/date داخل أعمدة مالية** — أثر GRN (مستند MGT!) في قلب تقرير FAS.
- **"deference value"** — خطأ مطبعي صارخ لـ**difference** (توثّق دون تناقض).
- **waive amount** — **مبلغ إسقاط**: إدارة تسمح بإعفاء جزء من فرق العقد! (قرار تنازلي موثق كعمود — بعد Authorize في FO).
- **قيد التشغيل الحرفي**: "This report will work **only if the Debit Notes are generated using the Debit Note Print option**" — التقرير يعمل فقط بعد التوليد من §15 (سلسلة أداة مغلقة: طباعة→قائمة).

## 7. جدول العائلة

| التقرير | البعد | الميزة القصوى |
|---|---|---|
| 10 Creditors Outstanding | **Ageing** | As On/Month/Date + Net D/C/Both |
| 11 Purchase Tax Register | ضريبي | **ثلاثية أرقام الضريبة** |
| 12 Purchase Register | خام | **معياران فقط** |
| 13 Expense Register | مصروف | **Above عتبة + تعليل محاسبي** |
| 15 Debit Note Print | تعاقدي | **القصة الاقتصادية + Load/Tag** |
| 16 CDN List | تعاقدي | **أعمدة كاملة + GRN + waive + deference** |

**الاكتشاف التجميعي:** هذه العائلة تُظهر **الوجه الدائني الكامل للميزانية التشغيلية**: أعمار دائنين (من يشاء المال؟) · ضريبة شراء · سجلات خام/عتبية · **تسوية تعاقدية بفرق سعر** — وهي المرآة المعاكسة لعائلة MGT-03/05 (استلام/مورد) — دورة المشتريات **تُغلق محاسبياً هنا** (PJV بعد §18).
