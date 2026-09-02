# 03 — الشاشات (Screens) — وحدة FAS

> جرد من الوثائق المقروءة الأربع (SET/TRN/MST/LUK). الأولوية: P0 (تشغيل يومي) / P1 (دوري) / P2 (إعداد نادر).

| ID | الشاشة | الوثيقة | القسم | الأولوية |
|---|---|---|---|---|
| SC-FA-001 | Main Heads | FAS-SET | §1 | P2 |
| SC-FA-002 | Sub Heads | FAS-SET | §2 | P2 |
| SC-FA-003 | Transaction Types (+Document Number +Print Details) | FAS-SET | §3 | P2 |
| SC-FA-004 | Transaction Voucher Link | FAS-SET | §4 | P2 |
| SC-FA-005 | Transaction Type Rights | FAS-SET | §5 | P2 |
| SC-FA-006 | FO to Finance Link | FAS-SET | §6 | P2 |
| SC-FA-007 | POS to Finance Link | FAS-SET | §7 | P2 |
| SC-FA-008 | MM to Finance Link (+Link Store +Unlinked Items) | FAS-SET | §8 | P2 |
| SC-FA-009 | Payroll to FAS Link (+CC/Dept linking) | FAS-SET | §9 | P2 |
| SC-FA-010 | Membership to FAS Link | FAS-SET | §10 | P2 |
| SC-FA-011 | Link AR to Finance | FAS-SET | §11 | P2 |
| SC-FA-012 | TDS Nature of Payment | FAS-SET | §12 | P2 |
| SC-FA-013 | TDS Tax Link | FAS-SET | §13 | P2 |
| SC-FA-014 | TDS Defaults | FAS-SET | §14 | P2 |
| SC-FA-015 | Print Forms | FAS-SET | §15-§16 | P2 |
| SC-FA-016 | Create User Reports (+Group Definition/Linking/Formula/Item Details/Report Linking) | FAS-SET | §17 | P1 |
| SC-FA-017 | Financial Period (Audited) | FAS-SET | §18 | P2 |
| SC-FA-018 | Budget Types | FAS-SET | §19 | P2 |
| SC-FA-019 | Pre Defined Narration | FAS-SET | §20 | P2 |
| SC-FA-020 | Trial Balance Print Order | FAS-SET | §21 | P2 |
| SC-FA-021 | Link CC to Department | FAS-SET | §22 | P2 |
| SC-FA-022 | Link Exempt Tax to Finance | FAS-SET | §23 | P2 |
| SC-FA-023 | Vendor Tax Split | FAS-SET | §24 | P2 |
| SC-FA-024 | Retained Earning Account | FAS-SET | §25 | P2 |
| SC-FA-025 | Specify Aging | FAS-SET | §26 | P2 |
| SC-FA-026 | Print Form Designer | FAS-SET | §27 | P2 |
| SC-FA-027 | **FA Transactions (الشاشة الأم — tabs: Period/Master/Link)** | FAS-TRN | §1 | **P0** |
| SC-FA-028 | Ledger Opening Balance | FAS-TRN | §1D | P1 |
| SC-FA-029 | **Transaction Entry** (+Journals/Allocation/Ledger Balance/TDS Query) | FAS-TRN | §1E | **P0** |
| SC-FA-030 | PDC Transactions (+Debit Details) | FAS-TRN | §1F | P0 |
| SC-FA-031 | **FO to Finance Posting (Post FO/POS)** | FAS-TRN | §1G | **P0** |
| SC-FA-032 | Purchase Journal Posting (Regular) (+Posting PJV) | FAS-TRN | §1H | P0 |
| SC-FA-033 | Service PJV | FAS-TRN | §1H | P1 |
| SC-FA-034 | Consolidate PJV (+Auto PJV Posting +Narration) | FAS-TRN | §1I | P1 |
| SC-FA-035 | Consumption Posting | FAS-TRN | §1J | P1 |
| SC-FA-036 | Membership to FA Posting | FAS-TRN | §1K | P1 |
| SC-FA-037 | Contract Debit Note (+Item Details) | FAS-TRN | §1L | P1 |
| SC-FA-038 | Payroll to FA Posting | FAS-TRN | §1M | P1 |
| SC-FA-039 | Pending Postings (+Posting Selection) | FAS-TRN | §1N | P1 |
| SC-FA-040 | Statistics (في FA Transactions) | FAS-TRN | §1O | P2 |
| SC-FA-041 | Statistics Transaction | FAS-TRN | §2 | P2 |
| SC-FA-042 | Bank Reconciliation | FAS-TRN | §3 | P1 |
| SC-FA-043 | Budget (+Fixed months) | FAS-TRN | §4 | P1 |
| SC-FA-044 | Interactive Payment Match | FAS-TRN | §5 | P1 |
| SC-FA-045 | TDS Tagging | FAS-TRN | §6 | P1 |
| SC-FA-046 | Cancel Cheque | FAS-TRN | §7 | P1 |
| SC-FA-047 | Open Financial Year (+Rollback) | FAS-TRN | §8 | P1 |
| SC-FA-048 | Voucher Authorization | FAS-TRN | §9 | P2 |
| SC-FA-049 | Financial Account Master (tree +create main/sub/COA) | FAS-MST | §1 | P1 |
| SC-FA-050 | Chart of Accounts | FAS-MST | §1 | P2 |
| SC-FA-051 | Vendor Master (+TDS/Payment/Bank/Contact/Tax/Other Details — 7 نوافذ فرعية +Discount/Interest) | FAS-MST | §1 | P1 |
| SC-FA-052 | Sub Ledger | FAS-MST | §1 | P2 |
| SC-FA-053 | Expense Allocation | FAS-MST | §1 | P2 |
| SC-FA-054 | Statistics Master | FAS-MST | §2 | P2 |
| SC-FA-055 | Statistics Budget Master | FAS-MST | §3 | P2 |
| SC-FA-056 | Cheque Book Master | FAS-MST | §4 | P2 |
| SC-FA-057 | Ledger Balance (lookup) | FAS-LUK | §1 | P0 |
| SC-FA-058 | Day Book (Q) (+تعديل مباشر!) | FAS-LUK | §2 | P0 |
| SC-FA-059 | Trial Balance (+Modify Column) | FAS-LUK | §3 | P0 |
| SC-FA-060 | Profit and Loss | FAS-LUK | §4 | P0 |
| SC-FA-061 | Balance Sheet | FAS-LUK | §5 | P0 |
| SC-FA-062 | Payable Outstanding (+تفاصيل vendor) | FAS-LUK | §6 | P1 |
| SC-FA-063 | Chart of Accounts List (تعديل أونلاين) | FAS-LUK | §7 | P1 |
| SC-FA-064 | Cash Flow Query | FAS-LUK | §8 | P1 |
| SC-FA-065 | Transaction Search (Search Records +Ctrl+F) | FAS-LUK | §9 | P0 |

**الإجمالي: 65 شاشة/نافذة موثقة** (+ شاشات FAS-REP عند قراءتها في Phase 7).
