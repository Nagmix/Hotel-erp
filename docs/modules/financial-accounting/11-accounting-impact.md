# 11 — الأثر المحاسبي (Accounting Impact) — وحدة FAS ⭐ النواة

> **هذه الوثيقة تحسم QA-1/QA-2/QA-3/UNK-006** (كانت معلقة من `docs/modules/front-office/11-accounting-impact.md` §6). المصادر: FAS-SET §3/§6-§11 + FAS-TRN §E/§F/§G/§H.

---

## 1. الروابط الستة (6 Posting Links) — التعريف الكامل الموثق

### 1.1 FO to Finance Link (FAS-SET §6 ص12-15) — Sales/Income Journal

**أنواع الإيراد (Revenue Types) الموثقة كاملة:**

| Revenue Type | المحتوى | ملاحظات محاسبية موثقة |
|---|---|---|
| **Revenue Heads** | كل أكواد الإيراد المعرفة في FO Revenue Codes | — |
| **Outlets** | منافذ POS (من Setup Outlets) | لترحيل **خصومات المنافذ (Allowance/Rebate) في Front Desk + Short Charges** لفواتير المنافذ |
| **Taxes** | كل ضرائب FO/POS/Banquets | Service Charges, Luxury Tax, Sales Tax... |
| **Plans** | خطط الطعام | MAP, EP, CP, B&B... |
| **Telephone Heads** | إيرادات الهاتف | Local, ICC (محلي), IDD (دولي) |
| **Paid Out** | Guest Paid Out + **City Ledger Paid Out** | — |
| **Advance Collection** | المسددات المقدمة | Advance Cash, Cheque, Credit Card... |
| **Room Revenue Heads** | Room Tariff + Extra Bed | — |
| **Retention Charges** | رسوم الاستبقاء | — |
| **Settlements** | كل أنماط التسوية في FO وPOS | **"For settlements, only debit account has to be defined"** |
| **Guest Ledger Balance** | B/F وC/F لرصيد دفتر الضيوف | **"B/F should be posted as Credit and the C/F as Debit"** |
| **Round Off** | مولّد آلياً | **حسابات منفصلة للعملة المحلية والأجنبية** |
| **No Transaction** | مولّد آلياً | **إلزامي حساب Suspense** — يستقبل المبالغ غير الموزعة (تفصيل §2) |

**قواعد الربط:** لكل Revenue Code: **Debit + Credit Account Heads**؛ إذا كانا Control Accounts → **Sub Ledger إلزامي**؛ بعد إدخالهما يُربط Cost Center + Department (**لحسابات الدخل والمصروف فقط**) + Cash Flow.

### 1.2 POS to Finance Link (FAS-SET §7 ص15-16)

- **البعدان:** Restaurant Code (من POS Setup Outlets) × **Group Code (Menu Groups من POS)**.
- **النمط المحاسبي الموثق:** "The Debit account is normally a Liability or Expense, while the Credit account should be an Asset or Income" — **قيمة مبيعات المنفذ تظهر Credit؛ الخصومات (Allowances/Rebate) تظهر Debit**؛ **حسابات غير Bank/Cash فقط**؛ Control → Sub Ledger.
- النظام **يسمح بتغيير Cost Center** في هذا الرابط.

### 1.3 MM to Finance Link (FAS-SET §8 ص16-18) → Purchase Journal

- **البعدان:** Store (يربط بالـ Property عبر Link Store) × Item **أو** Item Group.
- **القاعدة الموثقة:** "Purchase should always be linked to **Asset** A/C Code and Consumption should always be linked to **Expense** A/C Code followed by CC and Dept"؛ **Expense/Asset وغير Bank/Cash فقط**؛ إذا الربط بالصنف → الأصناف الجديدة تحتاج ربطاً.
- أدوات: Unlinked Items (All/Purchase/Consumption؛ F3 متابعة، Shift+F3 عكسي)؛ بحث بالاسم/حساب الشراء/حساب الاستهلاك.

### 1.4 Payroll to FAS Link (FAS-SET §9 ص18-21)

- يربط **ED Codes** (رواتب) بحسابات GL — **"mandatory for the journal posting"**.
- Calculation Method (Executive/Manager/...) + Applicable From (MM/YY)؛ **F2** → ربط Cost Centers وDepartments بين Payroll وFAS (ربط تنظيمي ثنائي الاتجاه).

### 1.5 Membership to FAS Link (FAS-SET §10 ص21-23)

- ربط Revenue Headings بعضوية المنافذ بنمط D/C نفسه؛ الفرق غير الموزع → حساب معرف مؤقتاً + إعادة معالجة Post Membership to Finance.

### 1.6 Link AR to Finance (FAS-SET §11 ص23-25) — AR Receipts

- "transactions that are posted using the Transaction Entry option under the Accounts Receivable module are posted based on the linked account codes to General Ledger".

**مصفوفة التحقق الموثقة (حسابات AR):**

| الغرض | Account Type | GL Type |
|---|---|---|
| **Sundry Debtors** | Client | **Others** (مع IDS ACR: **Client A/C + GENERAL** لحساب السيطرة) |
| **Cash** | Client | Cash |
| **Bank** | Client | Bank |
| **Commission** | Client | Others |

- شرط التفعيل: **FAS Switch 4 "FOM to FAS Posting Required" = Yes** (SYS Module Attributes).
- **التدفق الموثق:** عند حفظ قيد AR → يُرحَّل لشاشة FA Transaction بالحسابات المرتبطة D/C → **يمكن تغيير الحساب المرتبط بـ F5 ثم F1** قبل الحفظ.

## 2. آلية الفروق غير الموزعة (Undistributed) — النمط الموثق الموحد

1. **أثناء Post FO to Finance:** يجب **Total Debit = Total Credit** (الفرق = 0) وإلا:
2. شاشة بالفرق → Yes → **يُرحَّل الفرق آلياً إلى الحساب الموسوم "No Transaction"** (Suspense — **إلزامي تعريفه**) "on a temporary basis".
3. **دلالة الفرق:** "the FO / POS to Finance definition is not linked properly (new defined revenue codes, tax codes and outlet codes)".
4. **العلاج الموثق:** تحديث التعريفات → **re-process Post FO to Finance** — (نمط "التصحيح بإعادة المعالجة" لا بالتعديل المباشر).

## 3. توقيت الترحيل (Posting Timing) — المحسوم

| الحدث | التوقيت الموثق | المصدر |
|---|---|---|
| **FO/POS Sales Journal** | بعد Day End في FO و**Open New Date**؛ **Effective Date = عادة اليوم السابق لتاريخ النظام**؛ تنفيذ يدوي لعملية Post FO to Finance | FAS-SET §6 + FAS-TRN §G |
| Purchase Journal | عند الطلب (PJV) بشرط Bill No/Date؛ Effective ≤ اليوم | FAS-TRN §H |
| Consumption | **شهري (INI 283=1) أو يومي (=2)** | FAS-TRN §J |
| Payroll / Membership | عند الطلب | FAS-TRN §K/§M |
| AR Receipts | **فوري عند حفظ قيد AR** (يظهر في FA Transaction فوراً) | FAS-SET §11 |
| PDC | عند التحصيل/الصرف (Post) | FAS-TRN §F |

## 4. أمثلة قيود موثقة بالأرقام (Worked Examples — FAS-TRN §H ص22-23)

**ضريبة الشراء — الطريقة 1 (يتحملها المشتري):** INV Switches 1+4 = No؛ Tax Exemption tag=Yes؛ Link Exempt Tax → حساب التزام؛ Vendor Tax Split = No.
> استلام الصنف 2040: Qty=10, Rate=10, Value=100, Tax 1% = 1.00 → **PJV: Debit 100 · Vendor Credit 99.00 · Tax Credit 1.00**

**الطريقة 2 (يتحملها البائع):** Switch 1=No, 4=Yes؛ Vendor Tax Split = Yes.
> **PJV: Debit 100 + Tax Debit 1.00 · Vendor Credit 101.00**

## 5. أحداث القيود المشتقة (من كل الوحدات → GL)

| الحدث المصدر | القيد الموثق | المصدر |
|---|---|---|
| مبيعات FO/POS (يومياً) | Sales Journal: لكل Revenue Code إيراد D/C من رابط §6/§7 | FAS-TRN §G |
| Guest Ledger Balance | **B/F Credit · C/F Debit** | FAS-SET §6 |
| تسويات FO/POS | **Debit فقط** من رابط Settlements | FAS-SET §6 |
| مشتريات MM | Regular/Service PJV → Payable Control (Credit) + Items (Debit من رابط الشراء) | FAS-TRN §H |
| استهلاك MM | Journal استهلاك (Credit حسابات المخزون/الاستهلاك) | FAS-TRN §J |
| رواتب | Journal من ED Codes | FAS-SET §9 |
| عضويات | Sales Journal عضوية | FAS-TRN §K |
| فروق غير موزعة | **Debit/Credit لحساب No Transaction Suspense** (مؤقت) | FAS-SET §6 |
| Round Off | حسابات منفصلة Local/Foreign | FAS-SET §6 |
| PDC استلام | Debit: PDC Receivable | FAS-TRN §F |
| PDC تحصيل | **Debit: Bank/Cash · Credit: PDC Receivable** (القبول Cash/Bank فقط) | FAS-TRN §F |
| إقفال سنة | أصول/التزامات → أرصدة افتتاحية + صافي P&L → Retained Earnings (بنسب) | FAS-TRN §8 |
| Contract Debit Note | Debit: قيمة الفرق على مورد العقد | FAS-TRN §L |

## 6. المتبقي غير موثق

| البند | الحالة |
|---|---|
| قيود Tips (QA-4) | `[NOT DOCUMENTED]` في FAS — يُبحث في POS/AR |
| معالجة Complimentary محاسبياً (QA-5) | `[NOT DOCUMENTED]` — خيار ARR تقارير فقط (FOM-LUK §21) |
| توزيع أطراف قيد Night Balance النقدي للكاشير | المبدأ موثق (توازن + فرق→Suspense)؛ التفصيل الداخلي في DEP |
