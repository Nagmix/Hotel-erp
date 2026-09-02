# 14 — نموذج البيانات (Data Model) — وحدة FAS

> الكيانات الموثقة من FAS-SET/TRN/MST/LUK. ERD نصي أولي — تُفصل الحقول في Phase 9.

---

## 1. الكيانات (Entities)

| # | الكيان | المفتاح/البنية | الحقول الجوهرية الموثقة | المصدر |
|---|---|---|---|---|
| 1 | **MainHead** | code (3 رقمي فريد) | account_category (Assets/Liabilities/Income/Expense — نظامي)، name(30)، short(10)، head_type (MAIN)، **is_system_generated** | FAS-SET §1 |
| 2 | **SubHead** | code (3 رقمي فريد) | name(30)، short(10)، **main_head_id** | FAS-SET §2 |
| 3 | **AccountHead (COA)** | account_code (5/8) | group_code→SubHead، name(30)، short(**إلزامي** 20)، cost_center، department (للدخل/المصروف)، **account_type (Client/Payables/Sub ledger)**، **gl_type (CASH/BANK/OTHERS)**، **pdc_type (Rcv/Pay)**، restrict_journal، stop_posting، tax_applicable، consider_as_payable، activate_tds، **properties[] (متعدد!)** | FAS-MST §1 |
| 4 | **SubLedger** | sl_code (7 حرفي فريد) | long_name(40)، short(18)، **account_heads[] (متعدد)**، tds_details? | FAS-MST §1 |
| 5 | **VendorMaster** | vendor_code (7 = 3 نوع + 4) | بيانات 10 مجموعات (راجع `01-master-data.md` §2)؛ credit_days/limit، advance_pct، stop_purchase، stop_payment، payment_schedule (Adhoc/Daily/Fixed-9days)، 5 cash discount slabs، interest slabs، bank (BACS/sorting/txn_limit)، 2 contacts، tax codes[]، black_list (who+reason) | FAS-MST §1 |
| 6 | **TransactionType** | (property, code 2 رقمي) | book_type (9 أنواع نظامية)، name/short، doc_numbering (auto/manual + prefix/prefill/init_period/starting/restart/suffix)، print_voucher + form_id + printer، particulars_per_entry، particulars_mandatory | FAS-SET §3 |
| 7 | **FinancialYear** | (property, seq) | accounting_period_months (6-24)، start/end dates، **audited_months[] (Y/N)** | FAS-SET §18 |
| 8 | **FATransaction (GL Entry)** | doc_no (آلي/يدوي) | property، transaction_code، txn_date، **lines[]: account+sl، currency، bill#، amount، D/C**، narration (250)، balance_enforced | FAS-TRN §E |
| 9 | **PDCEntry** | — | account (PDC Rcv/Pay)، cheque#/date، status (pending/posted/deleted) | FAS-TRN §F |
| 10 | **ChequeBook** | book_ref | account، start_no، no_of_cheques، minimum_cheques، status، **cheques[] (حالة open...)** | FAS-MST §4 |
| 11 | **FOTOFinanceLink** | (revenue_type, revenue_code) | **debit_account + credit_account (+SL)**، cost_center، department، cash_flow | FAS-SET §6 |
| 12 | **POSTOFinanceLink** | (restaurant, menu_group) | debit_account، credit_account (+SL)، cc (قابل للتغيير) | FAS-SET §7 |
| 13 | **MMTOFinanceLink** | (store, item|group) | account_code (أصل شراء / مصروف استهلاك)، cc، dept | FAS-SET §8 |
| 14 | **PayrollTOFASLink** | (ed_code) | account، cc_link، dept_link، calculation_method، applicable_from | FAS-SET §9 |
| 15 | **MembershipTOFASLink** | (revenue_heading) | D/C accounts | FAS-SET §10 |
| 16 | **ARTOFASLink** | (purpose) | account_type/gl_type constraints | FAS-SET §11 |
| 17 | **TDSNatureOfPayment** | code (3) | description، form16_name، tax_structure، applicable_form، tds_section، applicable_date | FAS-SET §12 |
| 18 | **TDSTaxLink** | (tax_code) | account + SL + round_off (none/higher/lower/nearer) + amount | FAS-SET §13 |
| 19 | **Budget** | (budget_type, account, cc, dept, month) | amount (apportion/fixed)، **actuals (محسوبة)** | FAS-TRN §4 |
| 20 | **BudgetType** | code (2) | name/short، applicable_from | FAS-SET §19 |
| 21 | **RetainedEarning** | (fy, account) | percent (توزيع صافي P&L) | FAS-SET §25 |
| 22 | **ExpenseAllocation** | allocation_code (3) | method (Abs %/Fixed Amount)، book_type (Payments/Journal)، D/C، account+SL، cc/dept، pct/amount | FAS-MST §1 |
| 23 | **StatisticsMaster** | code (5) | name(60)، short(10)، group_code (**Rooms/Shares**) | FAS-MST §2 |
| 24 | **StatisticsTxn** | doc | fy، doc_date، group (Rooms/Shares)، currency، account، amount | FAS-TRN §2 |
| 25 | **PreDefinedNarration** | serial (آلي) | narration | FAS-SET §20 |
| 26 | **UserReport** | report# (3) | basis (Account/CC/Dept)، headers (60×3)، **groups[]** (type/account_type/pct/hide/page_break/sign_reverse)، **group_links**، **columns[]** (type/variance/hide)، item_details، **report_links[]** (تجميع MIS) | FAS-SET §17 |
| 27 | **VendorTaxSplit** | (tax_code, vendor) | tag Yes/No | FAS-SET §24 |
| 28 | **CCtoDeptLink** | (dept, cc) | link Y/N | FAS-SET §22 |
| 29 | **BankRecon** | (bank_txn) | status (realized/unrealized)، realized_dt، reason | FAS-TRN §3 |
| 30 | **TDSChallanTag** | (tds_entry) | bank، challan_no، challan_date، tagged | FAS-TRN §6 |

## 2. العلاقات الجوهرية (ERD نصي)

```
MainHead 1─n SubHead 1─n AccountHead n─n SubLedger
AccountHead n─1 CostCenter, Department (شرط: Income/Expense فقط)
Property 1─n TransactionType, FinancialYear
FATransaction n─1 TransactionType, FinancialYear, Property
FATransaction 1─n TxnLine n─1 AccountHead (+SubLedger optional)
FOTOFinanceLink n─1 RevenueCode(FO) ; n─2 AccountHead (D/C)     ← تكامل FO
POSTOFinanceLink n─1 Outlet(POS) × MenuGroup ; n─2 AccountHead  ← تكامل POS
MMTOFinanceLink n─1 Item|ItemGroup ; n─1 AccountHead            ← تكامل MM
VendorMaster 1─n VendorTaxDetail, Contact(≤2), TaxCode[]
PDCEntry n─1 AccountHead (PDC type) ; → BankAccount (عند Post)
ChequeBook 1─n Cheque (open/used) n─1 AccountHead (Bank)
UserReport 1─n ReportGroup ; ReportLink n─1 UserReport (master)
```

## 3. قيود تصميم مستنتجة (بمصادرها)

| القيد | الأساس الموثق |
|---|---|
| كل قيد: ΣDebit = ΣCredit (قيد DB) | FAS-TRN §E |
| AccountHead: (account_code) فريد عالمياً؛ (gl_type∈{CASH,BANK,OTHERS}) | FAS-MST §1 |
| TransactionType: فريد لكل (property, code)؛ ≤99 | FAS-SET §3 |
| FinancialYear: Audited month lock (check constraint) | FAS-SET §18 |
| الروابط: D/C حسابات؛ إذا control → SL إلزامي | FAS-SET §6-§11 |
| Vendor: code 7 حرفي = 3+4 | FAS-MST §1 |
| RetainedEarning: Σpercent — يوزع صافي P&L | FAS-SET §25 |
