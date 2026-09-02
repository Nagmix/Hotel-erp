# تصنيف البيانات: الرئيسية مقابل المعاملات (Master Data vs Transactions)

> **المرحلة:** Phase 1 | مبنية على `entities.md` — التصنيف هنا يحدد بنية DocTypes والصلاحيات وإدارة التغيير لاحقاً.

---

## 1. مبدأ التصنيف

| الفئة | التعريف | خصائص في ERPNext لاحقاً |
|---|---|---|
| **Master Data** | مرجع ثابت يُشار إليه في المعاملات | DocType غير قابل للإلغاء، تغيير بإصدارات (Applicable From!) |
| **Configuration** | إعداد يتحكم في سلوك النظام | غالباً Single/Setup records + صلاحيات عليا |
| **Reference/Classification** | قوائم تصنيفية (lookup) | DocType بسيط + ربط Select |
| **Transaction** | حدث أعمال مؤرخ لا يُعدَّل بعد الإقفال | إلزامية الحفظ بالتاريخ المحاسبي + تجميد بعد Night Audit |
| **Status/Operational** | كيان حالة يتغير بالتشغيل (Room Status) | تحديثات متكررة + audit log |

---

## 2. Master Data حسب الوحدة (مع خاصية Applicable From الموثقة)

> ⚠️ خاصية جوهرية موثقة: كثير من الـ Masters تحمل **Applicable From** (تاريخ سريان) — أي أن FortuneNext يدير **إصدارات زمنية للبيانات الرئيسية** (تغيير سعر أو نوع غرفة يسري من تاريخ مستقبلي). هذا قرار تصميمي معماري مهم لنظامنا.

### Front Office
- **إصدارية زمنية (Applicable From موثقة):** Room Types, Room Features, Meal Plans, Plan Rates, Package Elements, Tax Structures, Room Rates [موثقة بالجداول]
- **عادية:** Room Master (الغرف), Companies, Business Sources, Market Segments, Nationalities, Guest Status, Reservation Modes, Flight Master, Bookers Types, Revenue Codes, Billing Instructions, Pay Modes, Vehicle Definitions, Guest Preferences, Trace Templates
- **إعدادية:** FO User Authorization, Resv. Mandatory Fields, User Identification, Bill/Forms Designers, Budgets/MIS Specs

### POS
- Outlets (+ ربط Sessions/OrderTypes/Currencies), Menus, Menu Groups/Levels, Items, Modifiers, Kitchens, Tables + Layout, Servers + Outlet Mapping, Hot Keys, Touch Groups, Happy Hours, Promotions, Discounts, Open Items, DSR Session Groups, KOT Books

### Banquets
- Function Rooms (+ Associated Rooms, Features, Setup Styles), Event Types, Menu Master + Menu Cards, Item Classifications, Cancellation Policies, Staff, Sub-Venues/Tags, Country-State-City, Block Reasons, Floors

### Materials
- Stores, Item Groups, Item Locations, Inventory Items (+ Barcode, Conversions, Components, Taxes), Vendors (+ Rating, Terms, Contracts, Item-by-Vendor), Indent Templates, Cost Centers, Budgets

### F&B Costing
- Recipes/Sub-Recipes, Costing Links, Sales/Cost Budgets, Costing Start Date

### Membership
- Member Categories, Membership Structure, Revenue Codes, Service Rates, Facility Codes/Fixed Rates, Complaint Categories, System Attributes, Cover Charges, Late Fees, User Defined Fields

### HR
- Banks, Branches, Grades, ED Codes + Calculations (معادلات!), Attendance Codes, Categories, HODs, Statutory Definitions, Salary Templates, Bonus Periods, Leave Groups/Details, Costing Groups, Denominations, Staff Budgets

### Financials
- Financial Accounts (COA: Main/Sub Heads), Statistics Masters/Budgets, Cheque Books, Transaction Types + Voucher Links + Rights, روابط FO/POS/MM/Payroll/Membership/AR → Finance

### System (SYS)
- Users + Access + Menu Access, Property Codes, Departments, Cost Centers, Designations, UoM, Reason Codes, Currencies + Exchange, Tax Codes/Slabs/Structures, Religions, Occupations, Credit Cards, Captions, INI/DB

---

## 3. Transactions حسب الوحدة

| الوحدة | المعاملات (موثقة بالفهارس) |
|---|---|
| **FO** | Reservations (Make/Amend/Cancel/Re-instate/Copy/No-Show), Registrations (Check-ins/Walk-ins), Room Transfers, Postings (Charges/Deposits/PaidOuts/Allowances), Deposits (Tag/Refund), Extra Charges, Folio Splits/Transfers, Checkouts, Settlements, Forex, Card Encashment, Agent Commission Tags, Pax Transfers, Traces, Guest Notes/Docs |
| **Night Audit** | Post Tariff, Guest Balance, Night Balance, Consolidated Entries, Adjustments, Open New Date, Cancel Night Audit |
| **POS** | Sessions (Open/Close), Orders, KOTs, Bills, Settlements, Reprints, Deposits (BNQ-style) |
| **Banquets** | Bookings (Make/Amend/Cancel/Copy/No-Show/Block/Release), Deposits/Refunds/Retentions, Requirements, Pre-Costing, Auto Indents, Bills + Settlements |
| **Membership** | Applications, Receipts, Revenue/Facility Entries, Guest Visits, Service Bills, Complaints, Subscriptions/Facility Posting, Tax Posting, Renewals/Terminations/Resignations/Blacklists |
| **AR** | Transaction Entries, Receipts + Matching/Untagging, Agent Commissions, Card Consolidations, Outstanding Updates, SOA + Rollbacks, Invoices/Reminders, Balance Confirmations, Credit Traces, Follow-ups |
| **FAS** | Vouchers (بكل Transaction Types), Bank Reconciliation, Budgets, Interactive Payments, TDS Tagging, Cheque Cancel, Financial Year Open, Voucher Authorizations, Statistics Transactions |
| **FXD** | Asset Transactions, Component Entries, Depreciation Runs + Posting |
| **MGT** | Requisitions, Indents, POs/SPOs, SWOs, Quotations Analysis, Re-orders, Receipts/Issues, Store Transfers, Opening Balances, Budget Entries |
| **FNB** | Costing Extractions, Kitchen Stocks/Opening, Manual Sales/Consumption, Inter-Kitchen Transfers, Stock Balance Transfers, Auto Indents |
| **HR** | Applications/Interviews/Offers, Attendance, Payroll Runs + Supplementary, Closings/Cancellations |
| **MNT** | Complaints, Actions, Job Orders, PM Schedule Entries, Equipment Readings |
| **TEL** | Calls (auto-posting), Transfers, Extension Activate/Deactivate, Passwords, Error Updates |
| **GTP** | Issue/Receive Gate Passes |
| **Care** | Rosters, Log-in/out, Tasks/Complaints (Raise/Assign/Start/Close/Transfer/Extend), Feedbacks, SMS |

---

## 4. قاعدة التجميد (Transaction Immutability) — موثقة

1. بعد **Open New Date**: تعديل/حذف معاملات التاريخ المغلق **ممنوع** (FOM-DEP §5).
2. أثناء **Create Guest Balance**: الترحيل مسموح للتاريخ التالي فقط (FOM-DEP §4).
3. آلية التصحيح الموثقة: **Cancel Night Audit** (قبل فتح تاريخ جديد) + **Night Audit Adjustments** (قناة المالية) + **Rollback SOA** (ACR) + Amend/Cancel في الوحدات قبل الإقفال.

> 🔎 **دلالة معمارية:** النظام المستهدف يحتاج آلية "قفل يومي" (business-date lock) على مستوى المنصة — قرار معماري يجب توثيقه في `docs/decisions/` لاحقاً.
