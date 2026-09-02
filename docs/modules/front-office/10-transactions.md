# 10 — المعاملات (Transactions) — وحدة Front Office

> كتالوج مستندات المعاملات وحالاتها وانتقالاتها — موثق من RES/REG/CAS/DEP.

---

## 1. سلسلة المستندات (Document Chain)

```
Reservation # ──(check-in)──> Registration # ──> Folio #
                                    │
                                    ├──(print)──> Bill #
                                    │                │
                                    │                └──(settle)──> Receipt #  ──> [AR إن ائتماني]
                                    │
                                    ├──(reservation deposit)──> Deposit Receipt
                                    ├──(refund)──> Deposit Refund + Retention Charge
                                    └──(forex)──> FX Voucher # / Encashment #
```

كل مرحلة تولّد رقماً مستقلاً: Reservation# (RES ص9)، Reg# (REG ص17)، Folio# (CAS ص31)، Bill# (CAS ص70)، Receipt# (CAS ص78)، Voucher# (CAS ص87 — تلقائي/يدوي حسب INI Switch)، Encashment# تلقائي (CAS ص90).

## 2. حالات الحجز (Reservation States)

| الحالة | الدخول | الخروج | المصدر |
|---|---|---|---|
| **Booked** (Confirmed/Waitlist) | Add / Copy | check-in / cancel / no-show | RES §1 |
| **Provisional** | حجز مبدئي | تأكيد/إلغاء | REG ص15 (عمود Provisional) |
| **Waitlist** | Mode/Booking type | توفر/إلغاء (peach color) | RES ص15 + REG ص15 |
| **Cancelled** | Cancel + Reason | Re-Instate Cancel (**رقم جديد**) | RES §1.3/§1.7 |
| **No-Show** | تلقائي بعد Night Audit | Re-Instate No-Show (تواريخ جديدة) | RES §1.8 |
| **Checked-In** | Express/Reservation/Room Rack | Checkout | REG §1-§4 |
| **Partial Checked-In** | check-in جزء من الضيوف | بقية الضيوف / Checkout | RES ص58 + REG ص5 |

## 3. حالات الفوليو (Folio States)

| الحالة | الدخول | الخروج | المصدر |
|---|---|---|---|
| **Open (Posting)** | عند check-in | Print Bill / Checkout | CAS |
| **Stopped** | طباعة الفاتورة (إن Attribute 16=Yes) | Release Stop Posting | CAS ص82-83 |
| **Billed** | Print Bill | Settlement | CAS §13 |
| **Settled** | Settlement مطابقة | Re-Settlement | CAS ص78-80 |
| **Closed** | Checkout + تسوية | Folio Re-Instate (**قبل Night Audit فقط**؛ الرئيسية أولاً) | CAS §14 |
| **Linked** | Link Rooms (فاتورة واحدة) | Delink | CAS §9 |

## 4. معاملات الترحيل (Posting Transactions)

| المعاملة | القيد الهيكلي (هيكل بيانات) | المصدر |
|---|---|---|
| Post Charge | Room/Reg + Revenue Code + Currency + Charges + Ex.Rate + Total | CAS §1 |
| Room Rate | Room + Accounting Date + Currency + Rate + Plan + Day Count (1/0.5) | CAS §1 |
| Additional Rate | النوع (Rate/Plan/Extra Bed/Retention) + Taxable + Tax + Day Total | CAS §1 |
| Extra Charge | From/To + Revenue + (Reservation/Rooms/Guests) + Tax Inclusive + Qty + Charges | RES §Extra |
| Fixed Charge | Transaction Date + Revenue + Ref# + Adult/Child + مستلمون | CAS §4 |
| Deposit | (Guest/Rsvn/City) + Mode + Particulars + Amount (+CC/Auth/Cheque details) | CAS §1 |
| Paid Out | (Rooms/City) + Folio + Currency + Ex.Amount + Mode + Reason + Voucher | CAS §1 |
| Allowance | (Bill/Consolidated) + Revenue + From/To + Amount/Tax + Discount + Reason+Auth | CAS §1 |
| Split/Transfer | مصدر + هدف + (Selective Tags / All) + تفويض | CAS §5-§8 |

## 5. أحداث دورة اليوم (Day-cycle Events)

- **Room Blocks:** OOO (Reason+Dept+Desc) / OOS (Desc) — RES §3.
- **Room Status:** Vacant/Dirty/Occupied/OOS/OOO/Reserved — REG §1/§3.
- **Create Hotel Chart / Agent Chart:** نشاط خلفي — REG §23.
- **Night Audit sequence:** Post Tariff → Guest Balance → Night Balance → Open New Date — DEP.
