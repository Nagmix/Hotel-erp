# 14 — نموذج البيانات (Data Model) — وحدة Front Office

> استنتاج هيكلي للكيانات والعلاقات **من السلوك الموثق** (لا نسخ بنية IDS). النموذج الكامل الرسمي يُبنى في Phase 9.

---

## 1. الكيانات الجوهرية (Core Entities)

| الكيان (Code Name) | المفتاح/السمات الموثقة | المصدر |
|---|---|---|
| `Reservation` | Reservation#, Property, Arrival/Dep (+Time), Nights, Room Type, Mode, Booking Type (Confirm/Waitlist), Company, Booker, Rooms, Adults/Children, Rate Info, Pax list (Additions) | RES §1 |
| `Registration` | Reg#, Reservation#, Room#, Guest, Departure DT, Bill Inst, Plan, Currency, Company, Classification, Status | REG §2-3 |
| `Folio` | Folio#, Reg#, حالة (Open/Stopped/Billed/Settled/Closed/Linked) | CAS |
| `Bill` | Bill#, Folio#, Billing Instruction, Net Amount, حالة الطباعة | CAS §13 |
| `Receipt` | Receipt#, Bill#, Room/Reg, Date, Net | CAS ص78 |
| `Settlement` | Bill# + نمط (9) + Amount + Tip + Remarks (+ CC details/Company/Staff/Cheque) | CAS §13 |
| `PostingLine` (شحنة) | Room/Reg, Revenue Code, Currency, Ex.Rate, Charges, Total(شامل ضريبة), Accounting Date | CAS §1 |
| `RoomRatePosting` | Room, Date, Currency, Rate, Plan, DayCount(1/0.5) | CAS §1 |
| `Deposit` | (Guest/Rsvn/CityLedger) + Mode + Amount + Particulars + CC/Cheque details | CAS §1 |
| `PaidOut` | (Rooms/City), Folio, Currency, ExAmount, Mode, Reason, Voucher# | CAS §1 |
| `Allowance` | نوع (Bill/Consolidated), Revenue, From/To, Amount/Tax, Discount, Reason+Auth | CAS §1 |
| `GuestProfile` | Title/First/Middle/Last, Guest Code (متكرر), العنوان, الجنسية, جواز, Visa, Company, T1..T14 خدمات | RES/REG |
| `Room` | Room#, Type, Block, Floor, Status, Features, OOO/OOS blocks | RES §3 + REG §1/§5 |
| `RoomBlock` | Room, From/To, النوع (OOO/OOS), Reason, Department, Description | RES §3 |
| `Group` | Group Code/Name, Leader, أعضاء (Reg#s), Billing Instructions | REG §17-21 |
| `GuestService` | Messages/Locator/Likes/Wakeup/Complaints (Room/Ext, Dept, Status, AttendedBy) | REG §7 |
| `RoomInstruction` | Room, تعليمات (Cashier/NA/HK)، يومية/تاريخ | REG §12 |
| `ForeexEntry` | Voucher#, Currency, فئات (Qty/Desc/Denom/Amount/Local), Commission, Net | CAS §17 |
| `CCEncashment` | Encashment# (آلي), Currency, Card, Total, Commission%, Net, Auth | CAS §18 |
| `SMSMessage` | الهدف (Group/Room/CheckOut), Mobile#, Status (real-time) | REG §27-28 |
| `BillingBroadcast` | From/To, Subject, Outlets, Message | REG §24 |
| `TurnAway` | From/To, Property, Room Type, Rooms/Pax, Guest, Contact, Reason | REG §11 |
| `AuditTrail(Reservation)` | البعد (5), القديم, الجديد, User, Time | RES §Audit |

## 2. العلاقات الجوهرية (موثقة سلوكياً)

```
Reservation 1─1..n Registration (Additions: ضيوف متعددون برقم حجز واحد — RES §Add)
Registration 1─1 Folio ─1─n.. PostingLine
Folio 1─1..n Bill ─1─n Settlement ─1─1 Receipt (لكل تسوية)
Reservation 1─n Deposit (تُعرض عند check-in — CAS ص9)
Room n─1 RoomType; Room 1─n RoomBlock
Group 1─n Registration (Link/Delink — REG §17-18)
Registration n─1 GuestProfile (History match — RES ص8)
Folio n─1 MainFolio (Link Rooms — CAS §9)
Pax transfer: Registration ↔ Registration (نقل pax)
```

## 3. قيود التصميم المستخلصة (للنظام الجديد)

1. **المستندات متسلسلة الأرقام** وغير قابلة لإعادة الاستخدام (Re-Instate يولد رقماً جديداً — RES ص47).
2. **الأرقام التلقائية:** Voucher (INI switch)، Encashment، Receipt، Reservation، Reg، Bill.
3. **التفويض المزدوج:** (المنفذ = مستخدم النظام) + (المصرِّح = اسم يدوي) — نمط يعاد تصميمه بأدوار صريحة.
4. **التاريخ المحاسبي بُعد إلزامي** لكل معاملة مالية.
5. **حالة الغرفة آلة حالات** (Vacant→Dirty→Occupied→...) تُدار مركزياً (Room Rack).
6. **Pax ككيان منفصل** داخل التسجيل (Adult/Child/ExtraBed — قابل للنقل والخصم العمري).

`[PENDING]` حقول كل كيان بالتفصيل من field-extracts + قراءة SET العميقة.
