# 14 — نموذج البيانات (Data Model) — وحدة Banquets

> **46 كياناً** (E-BQ-01..46) — الوحدة الثانية كثافة بعد MGT بفضل هيكل الحجز الغني.

---

## 1. المرجعيات المكانية

| الكود | الكيان | المفتاح | أهم الحقول | المصدر |
|---|---|---|---|---|
| E-BQ-01 | Country/State/City | كود آلي ×3 | أسماء + Status | SET §4 |
| E-BQ-02 | Floor | آلي | Long/Short | SET §7 |
| E-BQ-03 | **FunctionRoom** | RoomCode | 6 تبويبات (Details/Features/Seating×Capacities/Pictures/Layout/Location) + **MinimumRevenue/SecurityType/AvailableHours/Dimensions** | CFG §5 |
| E-BQ-04 | AssociatedRoom | آلي | النوع (Green/Storage/Pre-Function) + Dimensions + Location/Floor | CFG §1 |
| E-BQ-05 | SubVenueTag | Main+Sub | حصرية | CFG §10 |
| E-BQ-06 | RoomFeature | آلي | Description | CFG §2 |
| E-BQ-07 | SetupStyle | آلي | Setup Type + Min/MaxPax + Image | CFG §3 |
| E-BQ-08 | BlockReason | آلي | Desc ≤25 | SET §6 |
| E-BQ-09 | RoomBlock | — | From/To + Type (Management/Maintenance) + Reason + Department | BOK §3 |

## 2. مرجعيات الحجز والحدث

| الكود | الكيان | المفتاح | الحقول | المصدر |
|---|---|---|---|---|
| E-BQ-10 | EventCalendar | — | Name + DayType + From/To + **DryDay + BookingAllowed + BookingMadeBy** + Icon | SET §10 |
| E-BQ-11 | ReservationStatus | آلي | Name + Type + **Color** + Sequence | SET §11 |
| E-BQ-12 | EventType | — | Name + Classification (AGM/Birthday/Conference/Wedding/Party) | CFG §6 |
| E-BQ-13 | CancellationPolicy | آلي | Days From/To + ValueType (V/P) + Value | CFG §4 |
| E-BQ-14 | CorporateRate×3 | RateId | Room/F&B(EventType)/NonF&B(Equipment) + Applicable + Taxes | SET §18 |
| E-BQ-15 | CorporateRateTag | Company | RateIds الثلاثة | SET §19 |
| E-BQ-16 | **BanquetBooking** | **Res# آلي** | Party(Email/Mobile/Security/Catering) + Company + Booker + FO Defaults(Market/Source/PayMode) + PaymentTerms(Pre/During/Post%) + Policy + **FunctionRooms + AcrossDates + Pax(Expected/Guaranteed) + Rate/Pax + HallCharges + Tax + Status** | BOK Make |
| E-BQ-17 | BookingOtherDetails | Res# | AddOn/AssociatedRooms + ServiceManagers + Host/ChiefGuest(+Banners) + Instructions/Flow + DeptInstructions + SeatingStyles | BOK Make |
| E-BQ-18 | FollowUp | Res# | User (من Banquet Staff) | BOK Make |

## 3. مرجعيات القوائم

| الكود | الكيان | المفتاح | الحقول | المصدر |
|---|---|---|---|---|
| E-BQ-19 | ItemType | آلي | Desc ≤25 | SET §8 |
| E-BQ-20 | MenuGroup | آلي | Long/Short + **Sequence (FP order)** | SET §9 |
| E-BQ-21 | ItemClassification | Item+Outlet | Group + ItemType + **Veg/NonVeg** + Catering | CFG §7 |
| E-BQ-22 | **MenuMaster (BNQ)** | Code ≤4 | بنمطين (MA 29) + KOT printer + **DefaultBill/PrintOrder/NCFlag/Discount/Levels 1-3/Cost%/GLCode(فردي)/PreparationTime/AvailableHours/SubStore** + Local/Foreign rates | CFG §8 |
| E-BQ-23 | MenuCard | MenuCode | RecomPax + **Editable + Allowed per group + Defined counts** | CFG §9 |
| E-BQ-24 | PackageMenuCard | Code | FB+NonFB+MenuCard مرجعي + Allowed | CFG §9 |

## 4. المعدات والموردون والخدمة

| الكود | الكيان | الحقول | المصدر |
|---|---|---|---|
| E-BQ-25 | EquipmentCategory / SubCategory | Name ≤30 | SET §12 |
| E-BQ-26 | Equipment | InHouseQty/Rate + Tax | SET §12 |
| E-BQ-27 | SupplierEquipmentRate | **أدوان: 1hr/2hrs/HalfDay/FullDay/MultiDays + MinDays** + Ad-Hoc/Contract | SET §13 |
| E-BQ-28 | Vendor (نسخة MGT!) | كامل 7 خانات TTT+XXXX | SET §13 |
| E-BQ-29 | Contract (نسخة MGT) | Applicable/Expiry/Ref | SET §13 |
| E-BQ-30 | ServiceManager | Name/Designation/Dept/Email×2/Mobile×2 | CFG §12 |
| E-BQ-31 | BanquetStaff | User (SYS) + Select | CFG §11 |

## 5. التقييم والطباعة

| الكود | الكيان | الحقول | المصدر |
|---|---|---|---|
| E-BQ-32 | EventQuestionGroup / Answer | Food/Lodging · Good/Satisfactory | SET §14 |
| E-BQ-33 | EventQuestion | Question + **Answers 1-6 (2 إلزام) + Scores** | SET §14 |
| E-BQ-34 | EventTemplate | Name + EventType + Questions[] | SET §15 |
| E-BQ-35 | PrintForms | 4 Program IDs + Tax structures + Group codes + Printer | SET §16 |

## 6. المعاملات

| الكود | الكيان | المفتاح | الحالات | المصدر |
|---|---|---|---|---|
| E-BQ-36 | Shift/OutletSession | — | Open/Closed | BIL §§1-2/5-6 |
| E-BQ-37 | **RequirementEntry (WorkSheet#)** | WS# | مسودة/Finalized | BIL §11 |
| E-BQ-38 | RequirementItem | WS+Item | **Chargeable/Complimentary(F12)/Replacement + Rename(F11)** + Qty | BIL §11 |
| E-BQ-39 | PreCosting | WS+Item | Recipe-linked أو InventoryItems[] + Department | BIL §12 |
| E-BQ-40 | **AutoIndent** | Indent# (MGT) | يربط WS + Dept + CC | BIL §13 |
| E-BQ-41 | Deposit (+Voucher) | Res# | Cash/Card/Cheque + أصلي/Modified/Deleted | BIL §9 |
| E-BQ-42 | RefundRetention | Res# | Retention/Refund + Amount + Reason + Balance | BIL §10 |
| E-BQ-43 | BanquetBill | Bill# | Printed/Pending/Cancelled + Splits | BIL §3/7-8 |
| E-BQ-44 | SupplementaryItem | Bill+Item | أخضر | BIL §3 |
| E-BQ-45 | Settlement | Bill# | 11 نمطاً + Multiple + Resettled | BIL §4 |
| E-BQ-46 | NoShowCancellation | متعدد Res# | F11 جماعي | BOK §2 |

## 7. العلاقات الجوهرية

```
FunctionRoom ──(SubVenue)──► FunctionRoom (حصرية)
FunctionRoom ──1:N──► AssociatedRoom (block معاً)
BanquetBooking ──N:1──► FunctionRoom (+AddOns) · EventType · CancellationPolicy · CorporateRate(Company)
BanquetBooking ──1:1──► RequirementEntry(WS) ──1:N──► Items (F12→Comp!)
        │                        │
        │                        ├──► PreCosting ──► AutoIndent ──► MGT
        └──1:N──► Deposit ──► Refund/Retention (Balance)
                 └──1:1──► BanquetBill ──► Settlement ──► {AR/FO Folio/FAS}
MenuMaster ──(MA 29)──► Common/PerOutlet · MenuCard ──► PackageMenuCard
```

## 8. إسقاط أولي (تفصيل 16)

- BanquetBooking ≈ Event/Function Booking مخصص (لا نظير ERPNext قياسي مباشر — F-BQ-2).
- RequirementEntry ≈ BOM-like worksheet + Sales Order Items.
- Availability Chart = بنية فريقة زمنية (slot-based) على FunctionRoom.
