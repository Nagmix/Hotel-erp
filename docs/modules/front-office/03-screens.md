# 03 — كتالوج الشاشات (Screens) — وحدة Front Office

> **الحالة:** كتالوج شاشات موثق من فهارس الوثائق الأربع المقروءة كاملاً (RES/REG/CAS/DEP) + النص.
> مواصفات الشاشات التفصيلية (Fields/Actions/State/Rules/Side Effects وفق قالب §7) تُبنى في Phase 4 على هذا الكاتالوج — الشاشات الجوهرية أولاً.

---

## أولويات المواصفات (لـ Phase 4)

**P0 — الجوهرية (تُوثَّق أولاً):**
1. Quick Reservation (Room Booking) — RES §1.1
2. Room Rack Console — RES §3
3. Express Check-In — REG §1
4. Walk-in (الكامل) — REG §3
5. Guest Management — REG §6
6. Posting (شاشة الكاشير الأم) — CAS §1
7. Check Out + Bill Summary/Split — CAS §1.CheckOut + DEP
8. Settlements — CAS §13

**P1 — المهمة:** Room Type Booking، Reservation Check-In، Special Rooms Check-In، Guest Services، Change Rate، Group Billing Instruction، Deposits، Bill Allowance، Split Folios، Transfer Folios، Deposit Refund، Foreign Exchange Entry.

**P2 — الداعمة:** بقية شاشات REG (Hurdle Rate، Hotel Chart، Billing Broadcast، SMS...) وشاشات RES المساندة وشاشات CAS المتخصصة.

---

## سجل الشاشات (Screen Registry)

| ID | الشاشة | الوثيقة | القسم | الأولوية | حالة المواصفة |
|---|---|---|---|---|---|
| SC-FO-001 | Quick Reservation | FOM-RES | §1.1 | P0 | ⬜ pending |
| SC-FO-002 | Rate Information (Rate Table) | FOM-RES | §1.1-17 | P0 | ⬜ pending |
| SC-FO-003 | Package Selection | FOM-RES | §1.1-23 | P1 | ⬜ pending |
| SC-FO-004 | Post Save Dialog | FOM-RES | §1.1-26 | P0 | ⬜ pending |
| SC-FO-005 | Assign Guest Rooms | FOM-RES | §1.1/§5 | P0 | ⬜ pending |
| SC-FO-006 | Scan Booking (بحث الحجوزات) | FOM-RES | §1.3/§1.4 | P1 | ⬜ pending |
| SC-FO-007 | Room Type Booking (Grid) | FOM-RES | §2 | P1 | ⬜ pending |
| SC-FO-008 | Room Rack Console | FOM-RES | §3 | P0 | ⬜ pending |
| SC-FO-009 | OOO / OOS Block | FOM-RES | §3 | P1 | ⬜ pending |
| SC-FO-010 | Retentions Cancel/No-Show | FOM-RES | §6 | P1 | ⬜ pending |
| SC-FO-011 | Close Room Inventory | FOM-RES | §7 | P2 | ⬜ pending |
| SC-FO-012 | Express Check-In | FOM-REG | §1 | P0 | ⬜ pending |
| SC-FO-013 | Reservation Check-In | FOM-REG | §2 | P1 | ⬜ pending |
| SC-FO-014 | Express Walk-in | FOM-REG | §3 | P1 | ⬜ pending |
| SC-FO-015 | Walk-in (Full) | FOM-REG | §3 | P0 | ⬜ pending |
| SC-FO-016 | Special Rooms Check-in + G-FOLIO | FOM-REG | §4 | P1 | ⬜ pending |
| SC-FO-017 | Room Floor Plan Display | FOM-REG | §5 | P2 | ⬜ pending |
| SC-FO-018 | Guest Management (Change Guest Info) | FOM-REG | §6 | P0 | ⬜ pending |
| SC-FO-019 | Room Transfer / Swap | FOM-REG | §6 | P0 | ⬜ pending |
| SC-FO-020 | Credit Limit | FOM-REG | §6 | P1 | ⬜ pending |
| SC-FO-021 | Guest Services (Messages/Locator/Likes/Wakeup/Complaints) | FOM-REG | §7 | P1 | ⬜ pending |
| SC-FO-022 | Guest Photo (In-House) | FOM-REG | §8 | P2 | ⬜ pending |
| SC-FO-023 | Invoice By Arrival (+ Break Up + Ad hoc Charges) | FOM-REG | §9 | P1 | ⬜ pending |
| SC-FO-024 | Mask Guests | FOM-REG | §10 | P2 | ⬜ pending |
| SC-FO-025 | Turn Away / Walkout | FOM-REG | §11 | P2 | ⬜ pending |
| SC-FO-026 | Room Instruction | FOM-REG | §12 | P1 | ⬜ pending |
| SC-FO-027 | Change Rate | FOM-REG | §13 | P1 | ⬜ pending |
| SC-FO-028 | Hurdle Rate | FOM-REG | §14 | P2 | ⬜ pending |
| SC-FO-029 | Group Rate Updation | FOM-REG | §15 | P1 | ⬜ pending |
| SC-FO-030 | Stop Charges Posting | FOM-REG | §16 | P1 | ⬜ pending |
| SC-FO-031 | Link/Delink Rooms to Groups + FIT | FOM-REG | §17/§18/§20 | P2 | ⬜ pending |
| SC-FO-032 | Cancel Check-Ins | FOM-REG | §19 | P1 | ⬜ pending |
| SC-FO-033 | Group Billing Instruction | FOM-REG | §21 | P1 | ⬜ pending |
| SC-FO-034 | Daywise Over Booking | FOM-REG | §22 | P2 | ⬜ pending |
| SC-FO-035 | Create Hotel Chart | FOM-REG | §23 | P2 | ⬜ pending |
| SC-FO-036 | Billing Broadcast | FOM-REG | §24 | P2 | ⬜ pending |
| SC-FO-037 | Extension Password Setup | FOM-REG | §25 | P2 | ⬜ pending |
| SC-FO-038 | Activate-Deactivate Extension | FOM-REG | §26 | P2 | ⬜ pending |
| SC-FO-039 | Adhoc SMS / SMS Status | FOM-REG | §27/§28 | P2 | ⬜ pending |
| SC-FO-040 | Posting (Cashiering Main) | FOM-CAS | §1 | P0 | ⬜ pending |
| SC-FO-041 | Post Charges | FOM-CAS | §1 | P0 | ⬜ pending |
| SC-FO-042 | Deposits (Guests/Rsvn/City Ledger) | FOM-CAS | §1 | P0 | ⬜ pending |
| SC-FO-043 | Paid Outs (Rooms/City Ledger) | FOM-CAS | §1 | P1 | ⬜ pending |
| SC-FO-044 | Miscellaneous Charges | FOM-CAS | §1 | P2 | ⬜ pending |
| SC-FO-045 | Room Rate (Individual/All) + Additional Room Rate | FOM-CAS | §1 | P0 | ⬜ pending |
| SC-FO-046 | Bill Allowance / Consolidated Allowance | FOM-CAS | §1 | P1 | ⬜ pending |
| SC-FO-047 | Check Out (list) + Cutoff Date | FOM-CAS | §1 | P0 | ⬜ pending |
| SC-FO-048 | Bill Summary / Print Bill / Prov Bill | FOM-CAS | §1 | P0 | ⬜ pending |
| SC-FO-049 | Split Bill (Merge/Revenue Split/New Bill) | FOM-CAS | §1 | P1 | ⬜ pending |
| SC-FO-050 | Post Extra Charges | FOM-CAS | §2 | P1 | ⬜ pending |
| SC-FO-051 | Tag Deposits to Rooms | FOM-CAS | §3 | P2 | ⬜ pending |
| SC-FO-052 | Fixed Charge Posting | FOM-CAS | §4 | P1 | ⬜ pending |
| SC-FO-053 | Split Front Desk / F&B Charges | FOM-CAS | §5/§6 | P1 | ⬜ pending |
| SC-FO-054 | Split Folios / Transfer Folios | FOM-CAS | §7/§8 | P1 | ⬜ pending |
| SC-FO-055 | Link and Delink Rooms | FOM-CAS | §9 | P2 | ⬜ pending |
| SC-FO-056 | Confirm Checkouts / Pax Checkout | FOM-CAS | §10/§11 | P1 | ⬜ pending |
| SC-FO-057 | Settlements | FOM-CAS | §13 | P0 | ⬜ pending |
| SC-FO-058 | Folio Re-Instate | FOM-CAS | §14 | P1 | ⬜ pending |
| SC-FO-059 | Release Stop Posting | FOM-CAS | §15 | P1 | ⬜ pending |
| SC-FO-060 | Deposit Refund | FOM-CAS | §16 | P1 | ⬜ pending |
| SC-FO-061 | Foreign Exchange Entry | FOM-CAS | §17 | P1 | ⬜ pending |
| SC-FO-062 | Credit Card Encashment | FOM-CAS | §18 | P2 | ⬜ pending |
| SC-FO-063 | Tag Agent Commission | FOM-CAS | §19 | P2 | ⬜ pending |
| SC-FO-064 | Pax Transfer | FOM-CAS | §20 | P2 | ⬜ pending |

**إجمالي:** 64 شاشة مسجلة من الوثائق المقروءة. (+ شاشات DEP الموثقة في الجلسة 1 تُدمج عند بناء المواصفات — راجع `00-overview.md` §2.4.)

> شاشات FOM-SET / FOM-LUK / FOM-REP / FOM-GST / FOM-HSK / FOM-CRG / FOM-SMS: `[PENDING DEEP READ]` — تُضاف عند القراءة.
