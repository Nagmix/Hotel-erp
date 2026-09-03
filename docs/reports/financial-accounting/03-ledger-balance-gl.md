# 03 — أرصدة الحسابات والدفاتر الكبرى (Ledger Balance / GL / Detail Register) — FAS-REP (Phase 7)

> §5 (×2) + §6 General Ledger + §17 Detail Register = 4 تقارير — نواة الدفاتر التحليلية.

---

## 1. §5 Ledger Balance

**الوصف:** "reflects the balance of a designated financial year. In this ledger balance, **the property name and financial year appear by default**. The financial year can be changed by pressing **F3 help**."

| # | المعيار |
|---|---|
| 1 | Property Code + Date Range |
| 2 | Account name (**F1**) |
| 3 | **running balance required** — "view the total balance separately **including both debit and credit**" |
| 4 | **Department or Cost Center in the From and To boxes** |

**النقاط البنيوية:**
- **قيم افتراضية ملكية-زمنية**: الملك+السنة يظهران تلقائياً (تقرير "يعرف سياقه") — F3 لتغيير السنة.
- **Running Balance خيار** (وليس دائماً) — الرصيد الجاري التراكمي قابل للإطفاء.
- **Department أو Cost Center كنطاق From/To** — الأبعاد التنظيمية/التكلفية **فلاتر نطاق** (ليست تجميعاً!) — استخدام نطاقي للأبعاد (مقابل التجميعي في §6).

## 2. §5 Ledger Balance Format 2

**الوصف:** "viewed based on a selected financial year with the option of **by date, month and year** for a selected **general ledger or sub ledger** with **day total or day balance**."

- **مصفوفة خيارات ثلاثية**: (تاريخ/شهر/سنة) × (GL/SL) × (**Day Total/Day Balance**) — أعمق تحكم حبيبي في دفتر الرصيد.
- "Fill in all the required fields **as shown in the screenshot above**" — إحالة بصرية (لا وصف نصي — الأفق العام).
- عائلة Format 2 الثانية (بعد Day Book F2): F2 = نسخة أعمدة/تجميع بديلة.

## 3. §6 General Ledger — الدفتر العام بأربعة منظورات

**الوصف:** "generated for a selected Financial Year with **month range**. You have options of **General Ledger, Sub Ledger, Department and Cost Center**."

| # | المعيار |
|---|---|
| 1 | **F3 = FY** |
| 2 | **Month range** (From/To شهور — لا تواريخ!) |
| 3 | **GL / SL / Department / Cost Center** |
| 4 | All / Selected |

**النقاط البنيوية:**
- **"(Note: when you select one of these options, respective additional options will appear, select the required options)"** — **Adaptive UI ثانٍ مؤكد** (بعد MGT 4.1) — اختيار المنظور يولّد خياراته (Sub Ledger→حساب فرعي · Department→أقسام · CC→مراكز).
- **نطاق شهري** (From/To months) — الدفتر العام يعمل بالشهر (لا باليوم) — فترة محاسبية صرفة (مقابل Day Book اليومي! — **طبقة زمنية لكل تقرير**: يومية/شهرية).
- **أربعة مناظير** للدفتر العام: GL / SL / Dept / CC — نفس منظوري MGT CC Consumption (Consolidated/CC/Department) — **قاموس الأبعاد الموحد عبر الوحدتين**: حساب/حساب فرعي/قسم/مركز تكلفة.

## 4. §17 Detail Register — السجل التفصيلي بأعمدة معلنة

**الوصف:** "records all transaction details of a Property. In this report you can view the **account number, sub ledger number, voucher number, bill number, bill date, details of the transaction and the debit amount** for each transaction. You can also view the **opening balance, closing balance and the grand total**."

| # | المعيار |
|---|---|
| 1 | Property + FY + date range |
| 2 | **Currency** dropdown |
| 3 | A/C Code — **"The respective Account Type will be displayed"** |
| — | **ملاحظة تكيّف المؤشر**: "If the selected account has a sub ledger, **the cursor will move to the SL Code field, else the cursor will move to the Minimum Amount field**" |
| 4 | SL Code range (**F1**) |
| 5 | **Minimum Amount** — "view all transaction of the set minimum amount and above" |

**النقاط البنيوية:**
- **الأعمدة معلنة نصياً كاملة** (نادر في FAS!) — رقم حساب/SL/قسيمة/فاتورة/تاريخها/التفاصيل/**مدين فقط** (لا دائن؟ — الدفتر المدين التفصيلي؟ أو دفتر ذات وجه واحد → سؤال توثيقي).
- **المؤشر التكيّفي (Adaptive Cursor)**: مسار الإدخال يتبع طبيعة الحساب (SL أو عتبة المبلغ) — دقة تفاعلية فريدة (ثالث نمط Adaptive بعد MGT 4.1 شاشات وFAS 6 خيارات).
- **عتبة Minimum Amount** (فوق حد) — نفس "Above" في Expense Register — عائلة فلاتر العتبة المبلغية.
- Open/Close/Grand Total — سجل بمعادلة يومية كاملة.

## 5. جدول العائلة

| التقرير | النطاق الزمني | الأبعاد | الميزة |
|---|---|---|---|
| 5 Ledger Balance | FY + Date range | **Dept/CC كنطاق From/To** | Running خياري + افتراضات سياقية |
| 5 LB Format 2 | FY | GL/SL | **(Date/Month/Year) × (Day Total/Balance)** |
| 6 General Ledger | **Month range** | **GL/SL/Dept/CC** | Adaptive + الأبعاد الأربعة |
| 17 Detail Register | Date range | SL | **أعمدة معلنة + مؤشر تكيّفي + عتبة مبلغ** |

**الاكتشاف التجميعي:** عائلة الدفاتر تقدّم **سلّم تدرّج التحليل**: Ledger Balance (رصيد) → LB-F2 (تشريح زمني) → General Ledger (دفتر منظوري شهري) → Detail Register (ذرة الحركة بأرقامها المستندية) — من الرصيد إلى القسيمة في أربع درجات (نفس منطق Drill-Down الحديث — لكن كأربعة تقارير منفصلة بدل تقرير واحد متدرج → **GAP تصميمي D-مرشح**: الاشتت بدل التدرج).
