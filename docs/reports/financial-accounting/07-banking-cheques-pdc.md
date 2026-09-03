# 07 — المصرفية والشيكات (Banking / Cheques / PDC) — FAS-REP (Phase 7)

> §23 Bank Reconciliation + §24 Advice/Cheque Print + §25 Voucher Print + §32 PDC Check List + Bank Payment Report = 5 تقارير — الدورة النقدية المصرفية.

---

## 1. §23 Bank Reconciliation — **العملية-التقرير المزدوجة**

**الوصف الحرفي:** "This is an **operation** where all Bank transactions entered in the General Ledger is reconciled with the **Statement given by the Bank**. This enables you to have an account of **Cheque Deposited and Issued for Payment that are realized** and thereby ascertain the **Actual Bank Balances**. Reconciliation of the transactions can be done for any period and **this forms the basis for reflection in the Bank Reconciliation Query / Report options**."

**الوضعان (حرفياً):**

| الوضع | المعايير |
|---|---|
| **Realized** | Property (pre-defined) + bank Account code (F1) + **From/To Realized Date** |
| **Unrealized** | default Property + Account code + **As on date** + **"Balance As Per bank Statement"** (حقل!) |

- **مفهوم Realized**: الشيك "تحقق" (قُبض/دُفع فعلياً عبر المصرف) — التسوية بتواريخ **تحقق** الشيكات لا تواريخ إصدارها!
- **"Balance As Per Bank Statement" يُدخل يدوياً** — كشف المصرف يُقرأ ويُكتب رقمه في الشاشة (تسوية يدوية-نصف آلية) — الورق ما زال حاضراً في القلب المصرفي.
- **ثلاثية أدوات**: العملية (هذه) + **Query** + **Report** — (تُذكر كمستقلة "Bank Reconciliation Query / Report options").

## 2. §24 Advice / Cheque Print — **مستند الدفع بأكمل تفاعل Tag**

**الوصف:** "printing of payment **Advice at the time of making payment to the Vendor**. The print has the **Cheque details along with information of the bill/s for which the payment will be made**."

**ملاحظة Print Forms (نمط حرفي رابع):** "The Advice / Cheque Print program is developed as per your specifications on **pre-printed or plain, continues or cut sheet stationery** on **Dot Matrix / Desk Jet / Laser Jet Printers**. (Refer Print Forms option under Setup)."

**المعايير (11 خطوة — أطول سلسلة موثقة في الوحدة):**

| # | المعيار |
|---|---|
| 1 | Property + **Transaction Code** — "can be printed **only codes with Book Type Payment and Exchange**" |
| 2 | FY + **Month & Year** |
| 3 | **Date wise / Cheque No wise / Vendor Code wise** |
| 4 | النطاق — **"Date entered should be within specified Month / Year"** |
| 5 | Doc No (F1) / Vendor (F1) |
| 6 | **Normal / Repeat** — "first time... or the **Repeat option to re-print**" |
| 7 | cheque # + **name as on the cheque** |
| 8 | **Load** → المعاملات |
| 9 | **Tag YES** (default No — Enter أو Double Click) — "Single or **Multiple bills can be selected**" + **أزرار Un Tag / TagAll / Un TagAll** |
| 10 | Cheque Type |
| 11 | Printer type + Print |

**النقاط البنيوية:**
- **قيد Book Type**: فقط معاملات نوع الدفع والصرف — Advice مستندي الدفع حصراً.
- **Normal/Repeat** — إعادة طباعة رسمية (مقابل إعادة طباعة POS بلا تعطيل — هنا **Repeat وضع صريح** = الأثر مسموح ومعلن! — عائلة إعادة الطباعة: POS (10) · FAS-24 (Normal/Repeat) · 16A (New/Reprint)).
- **أزرار UnTag/TagAll/UnTagAll** — أغنى تحكم Tag في الحزمة (ثلاثية أزرار).
- **الفاتورة مع الشيك**: Advice يجمع شيك + فواتيره — مستند مطابقة دفع (نظير تجاري لGRN الاستلام).

## 3. §25 Voucher Print — **برامج بمعاملات القسائم**

**الوصف:** "printing of transaction **Vouchers / Forms**... based on the **Voucher Print program IDs specified against the Transaction Codes in the Transaction Types parameter**."

| # | المعيار |
|---|---|
| 1 | Property + Transaction Code + FY + Month & Year |
| 2 | **Date / Document No** |
| 3 | From/To (بلا نطاق = الكل) |
| 4 | **Name and Address** — "name of the person against whom the voucher is issued **can be printed on the voucher**. Click Yes and enter" |
| 5 | **Load** + **Toggle Tag** ("To select all transactions, click on Toggle Tag") |
| 6 | **Output Printer** — "All printer definitions through the **Printer Settings**... The printer **connected to the System from where the Print Command is being executed**, will appear as a **Default printer**" |
| 7 | Ok |

**النقاط البنيوية:**
- **نمط التسجيل الثاني**: البرامج ضد Transaction Codes (في Transaction Types) — لا قائمة Print Forms عامة (يُفصّل في 01 §3).
- **الطابعة الافتراضية تتبع موقع التنفيذ** — طباعة محطية (station-aware) ديناميكية.
- **Name/Address على القسيمة** — إضافة عنوان سريعة قبل الطباعة (حقل حر موثق).
- **خطأ ترقيم**: الخطوة الثانية مرقمة **"8"** (بين 1 و3) — أثر نسخ/لصق صارخ.

## 4. §32 PDC Check List — **دورة الشيكات المؤجلة**

**الوصف:** "identify account for **Post Dated Cheques (PDC)** separately; this option has to be **tagged as PDC Receivable or PDC Payable**. For Post Dated Cheques received from **Debtors**, the PDC Type should be tagged as **PDC Receivable** and for **Creditors** as **PDC Payable**."

| # | المعيار |
|---|---|
| 1 | Property ("list of all pre-defined properties") |
| 2 | FY (**F3** — "list of pre-defined Financial Years") |
| 3 | Date range — **"From date should be within the financial year specified"** |
| 4 | **PDC Account** من قائمة |
| 5 | From/To Sub Ledger (F1) |

- **PDC كحساب مستقل** — الشيكات المؤجلة حسابات موازنة (Receivable/Payable) — معمار موثق: شيك مستقبلي لا يلمس النقد حتى تاريخه.
- ثنائية المدين/الدائن للشيكات المؤجلة — **مصفوفة الشيك الرباعية**: (فوري/مؤجل) × (قبض/دفع).

## 5. Bank Payment Report (تحت §34 — بلا رقم)

"generate a report to view the payment reports for a given period."

| # | المعيار |
|---|---|
| 1 | FY |
| 2 | date range |
| 3 | **cheque status** — فلاتر حالة الشيك! |
| 4 | **Bank Name** |
| 5 | [زر] → التقرير |

- **حالة الشيك كفلتر** — دورة حياة الشيك (صادر/محقق/مرتجع؟) تصل التقارير (يقابل Realized في §23).
- تصنيفه الفعلي: مصرفي (وضع هنا) رغم إدراجه TOC تحت User Reports.

## 6. جدول العائلة

| التقرير | الكيان المركزي | الميزة القصوى |
|---|---|---|
| 23 Bank Rec | **كشف المصرف** | Realized/Unrealized + **رصيد كشف يدوي** |
| 24 Advice/Cheque | **الشيك+الفواتير** | Normal/Repeat + TagAll ثلاثية أزرار + Book Type قيد |
| 25 Voucher Print | **القسيمة** | برنامج-لكل-نوع + طابعة محطية |
| 32 PDC List | **الشيك المؤجل** | Rec/Pay ثنائية + قيد FY |
| Bank Payment | الدفعات | **cheque status** فلتر |

**الاكتشاف التجميعي:** عائلة مصرفية **متكاملة الدورة**: كشف (23) → دفع بشيك (24) → قسيمة (25) → مؤجل (32) → حالة (Bank Payment) — مع **قانونين عمليين موثقين**: تسوية بتاريخ التحقق (لا الإصدار) + رصيد كشف المصرف يدوياً — **الحد اليدوي للاتوماتية**: حتى في وحدة GL المالية، الورق المصرفي الخارجي إدخال يدوي (حد تكامل لم يتجاوزه FN6i).
