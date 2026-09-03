# 02 — دليل الحسابات واليوميات (Chart + Transaction Checklist + Day Books) — FAS-REP (Phase 7)

> §1 + §2 + §2(2) + §3 + §4 (Day Book / Format 2 / Cash-Bank Book) = 7 تقارير — أساس اليومية المالية.

---

## 1. §1 Chart of Accounts List

**الوصف:** "extract a list of all the **Account Heads** defined for a Property. A detailed list can be generated on the basis of **Account Categories, All or Individual**, on different sequences along with a Range option."

| # | المعيار | القيم |
|---|---|---|
| 1 | Property | dropdown |
| 2 | **Account Category** | **Assets / Liabilities / Income / Expenses** — افتراضياً All |
| 3 | Range (From/To) | اختياري — بلا نطاق: كل سجلات التسلسل |
| 4 | الترتيب | Account Code / Account Name |

- **التصنيف الرباعي الكلاسيكي** (أصول/خصوم/دخل/مصروف) كفلاتر — نفس التقسيم المحاسبي العالمي — أول ظهور صريح له في طبقة REP.
- بند الإخراج: "Select one of the report output options from the **Option dropdown list** and click Continue... Click Cancel to terminate" — نمط Continue/Cancel (بوابة تأكيد إخراج).

## 2. §2 Transaction Checklist (+ النسخة الثانية)

**§2 الأصل:** "checklist which reflects all the transaction posted for a given date range. Select transactions code 'All' to reflect all the transaction posted or select the specific transaction code... There is an option to print **Document Total, Summary or deleted transaction**."

| # | المعيار |
|---|---|
| 2 | Property |
| 3 | **F3 = Financial Year** |
| 4 | Transaction Code (All/نوع) |
| 5 | Date range + **Printing options** |

- **"deleted transaction" خيار طباعة موثق** — الحذف قابل للعرض من كشف الحركات القياسي (قبل Audit Trial §33 المتخصص!) — عائلة المحذوفات تمتد: MGT §23 · FAS §2 و§33.
- ثلاثية طباعة: Document Total / Summary / deleted.

**§2(2) Transaction Checklist (2):**
- "Fill in the required fields, select the printing options and click Ok" — وصف أفق عام.
- **المثال الحرفي**: "if you select search transactions by **Doc#** and select the option '**Delete Transaction**' then you can view the list of **all deleted transactions with the given Doc#**".
- **الفرق الوظيفي المعلن**: الاسترجاع **بDoc#** + وضع حذف مركّز — "Checklist (2)" = نسخة استرجاعية (لا وصف مميز آخر!) → UNK-097 (ما الذي يميزها فعلاً؟ شاشاتها بلا توثيق).

## 3. §3 Ledger Opening Balance

**الوصف الحرفي:** "will reflect the opening balances entered for a specific month. (**which normally is the start month of the FAS module**)."

- **شهر بدء وحدة FAS** مفهوم مؤسسي موثق ضمن تقرير الرصيد الافتتاحي (بداية الحوسبة المالية للملك).
- أبسط تقرير في الوحدة: Property + OK (معيار واحد! — يقابل MGT 4.8 بنفس البساطة).

## 4. §4 Day Book — اليومية النقدية والمصرفية

**الوصف:** "generated for **all cash and bank transaction** posted for a particular date or date range. This report can be generated based on the **Account codes and sub ledger codes**."

| # | المعيار |
|---|---|
| 1 | Property + **FY** + date range |
| 2 | Account + Sub Ledger + **Currency** |
| 3 | **include document total** + **Print Narration** |
| 4 | Ok |

- **ثنائية الخيارين**: الإجماليات المستندية + السرد (Narration — التعليق المحاسبي) — يومية بسردياتها.
- ثلاث عملات (Account/SL/Currency) — اليومية **متعددة العملات** صراحة.

## 5. §4 Day Book (Format 2) — يومية Contra بالمثال المصرفي الكامل

**الوصف الحرفي:** "generate Day Books for Cash and Bank Account Heads where **only the contra transactions** along with the **Account Opening and Closing Balances as well as the running balance** are reflected."

**المثال الحرفي الكامل (ص12 — أثمن سرّ نصي في الوحدة):**

> "Example: Account Head **A008000 (SBI Frankfurt** has a debit balance of US$ 1000 and a Receipt of US$ 500 (**received from Debtors**) is credited to this account head and the debit amount is accounted to the Bank Account Head. When a Day Book is generated for the SBI Frankfurt Account Head, the **contra transaction i.e. the credit amount posted to the Debtors account** is reflected."

**تفكيك المثال:**

```
A008000 SBI Frankfurt: رصيد مدين 1000$
قبض 500$ من المدينين → دائن على A008000، والمدين على حساب المصرف الآخر
توليد Day Book لـA008000 → يعرض حركة الـContra (الجانب الدائن على المدينين)
```

- **كود حساب مسرب (A008000) + مصرف حقيقي (SBI فرانكفورت) + عملة (USD)** — **الكود الحسابي الوحيد المرئي بالحزمة** (مقابل FIMSHTBL الاسمي في FXD).
- **Format 2 = منظور Contra**: اليومية لحساب نقدي تعرض **الوجه المقابل** فقط (مع افتتاحي/ختامي/جارٍ) — تدقيق آلي للحركات المتقابلة.
- عائلة "Format 2" ثالثة ظهور بعد LB-F2 وTB-F2 (يُفصّل في 00 §4.1).

## 6. §4 Cash/Bank Book

**الوصف:** "reflects the **transaction balance** for a designated **financial period** of a property."

| الحقول (حرفياً Ø-List): |
|---|
| Property name · Financial Year · From and To date · **Account Name (F1)** · **Sl. Name (F1)** · Currency → OK |

- **Sl. Name** (Serial Name بF1) — كيان "مسلسل" (شبه دفتر؟) يظهر هنا وفي Voucher Print — مفهوم فرعي غامض → مرشح UNK (تُرك عمداً: تقاطع مع Sub Ledger).
- توثيق بحقول enumerate (**Ø marks**) — نمط قائمة حقول نادر (مرة واحدة في الوحدة).

## 7. جدول العائلة

| التقرير | المفتاح المميز | ملاحظة مميزة |
|---|---|---|
| 1 CoA List | **تصنيف رباعي** | أول ظهور Assets/Liabilities/Income/Expenses كفلاتر |
| 2 Transaction Checklist | TC Code + **deleted option** | محذوفات من الكشف العادي |
| 2(2) TC (2) | **Doc# + Delete** | نسخة استرجاعية |
| 3 Ledger Opening Balance | **شهر بدء FAS** | معيار واحد فقط |
| 4 Day Book | Narration + Currency | يومية سردية متعددة العملات |
| 4 Format 2 | **Contra فقط + Running** | **مثال A008000/SBI/USD** |
| 4 Cash/Bank Book | **Sl. Name (F1)** | رصيد فترة مالية |

**الاكتشاف التجميعي:** اليوميات الثلاث (Day Book/Format 2/Cash-Bank Book) + كشف الحركات الثنائي = **خمس زوايا على نفس دفتر النقد والمصارف** (الكشف الشامل/Contra/رصيد الفترة/بالحذف/بDoc#) — تعدد زوايا يقابل تعدد زوايا الاستلام في MGT §4 — **نفس فلسفة المنتج: تقرير لكل سؤال محتمل**.
