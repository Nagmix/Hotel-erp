# 10 — المعاملات ودورات الحياة (Transactions) — وحدة Banquets

> دورة حياة الحدث الكاملة + الحالات والأرقام والأحداث المؤتمتة.

---

## 1. دورة حياة الحدث (Event Lifecycle)

```
Inquiry (بلا قاعة!) ──► Provisional ──► Confirmed ──► Finalized (FP بنفسجي)
      │                     │                │                │
      │ (نسخه ممنوع)        │                │                ▼
      │                     │           Requirement Entry (ورقة عمل) ──Finalize──┐
      │                     │                │                                   │
      ▼                     ▼                ▼                                   ▼
   Cancel (بلا ودائع!)   No-Show        Deposit (Cash/Card/Cheque)      Pre Costing (Recipes)
      │                (F11 جماعي)          │                                   │
      │                                     │ Refund/Retention                  ▼
      │                                     ▼                              **Auto Indent** → MGT
      │                              Banquet Bill (3 splits)                     │
      │                                     │                                    │
      │                                     ▼                                    │
      └──────────► Cancellation Policy charges ◄──── Settlement (11 modes) ──► AR/FO Folio
                                             │
                                             ▼
                                    Close Shift → Close Outlet (نفس accounting date)
```

## 2. جدول الحالات الموثقة

| الكائن | الحالات | المصدر |
|---|---|---|
| Reservation | **Inquiry / waitlist / Provisional / Confirmed** (الأساسية) + user-defined (ملونة) | SET §11 |
| الحجز في Scan | عادي + **ملغى (وردي)** + "Show only Cancellations" | BOK §1 |
| FP | Printed (أزرق) · **Finalized (بنفسجي)** | LUK §2 |
| Requirement Entry | مسودة → **Finalized** (تحرير بتنبيه) | BIL §11 |
| Settlement | Invoice/Bill → Settled (+Resettled) | BIL §4 |
| Shift/Outlet | Open → Closed (بمصادقة) | BIL §§5-6 |
| Block | **Management (أحمر) / Maintenance (أخضر)** + Release | BOK §3 |
| Room في الرسم | متاح/محجوز (ملون) + **restricted (رمادي)** + across-dates (داكن) | LUK §2 |
| Deposit Vouchers | أصلي/Modified/Deleted | BIL §9 |

## 3. الأرقام المولدة

| الرقم | اللحظة |
|---|---|
| **Reservation Number** | "A Reservation Number will be generated for this booking" (بعد تأكيد الحفظ) |
| أكواد المرجعيات | عند الإنشاء (Country/State/City/Floor/.../ServiceManager) |
| Rate Id (Corporate) | يدوي/مساعدة — ليس آلياً |
| Vouchers (ودائع) | لكل عملية + نسخ معدّلة/محذوفة |
| Bill#/Invoice | عند الطباعة (Invoice Print/Print Bill) |
| Indent# (Auto Indent) | يُختار من MGT (F1) — الترقيم في MGT |

## 4. الأحداث المؤتمتة الموثقة (Automation Events)

| # | الحدث | المحفّز | الأثر | المصدر |
|---|---|---|---|---|
| A-BQ-01 | **Auto email بعد الحجز** | إدخال بريد Party + الحفظ | "an auto email will be sent to the added email id **provided the user have an access to PDF** and the system is configured with **outlook express**" | BOK ص7 |
| A-BQ-02 | **فتح Availability تلقائي** | إدخال أوقات الحجز | "After entering the timings, the availability chart... will be opened" | BOK ص10 |
| A-BQ-03 | **Deposit attach prompt** | فوترة حجز له وديعة معلقة | "Deposit is pending... Do you want to attach?" | BIL §3 ص18 |
| A-BQ-04 | **Discount prompt بعد التقسيم** | حفظ Amount Split | "pop up a message to provide any discount on the **discountable amount**" | BIL §3 ص13 |
| A-BQ-05 | **Balance تلقائي في التقسيم** | أول Net Amount | "the balance bill amount will be auto populated in the next row" | BIL §3 ص12 |
| A-BQ-06 | **Auto-populate من Work Sheet** | اختيار Work Sheet# في Auto Indent | "The reservation number and the Party Name will auto populate" | BIL §13 |
| A-BQ-07 | **Recipes حسب القسم** | اختيار Department في Auto Indent | "recipe details will populate based on the department selected" | BIL §13 |
| A-BQ-08 | **Available Credit عرض** | Company Settlement + MA 21 | "The credit limit... is displayed in the Available Credit field" | BIL §4 |
| A-BQ-09 | **Blacklist إشعار** | Company Settlement لشركة مدرجة | "message... along with the authorized person's name and the reason" | BIL §4 |
| A-BQ-10 | **بيانات الضيف من الغرفة** | Guest Settlement + Room# | "Guest Name, Meal Plan, Pax, Birthday, Anniversary and Guest status are displayed" | BIL §4 |
| A-BQ-11 | **إرسال CC للـ AR** | Credit Card Settlement | "sent to the Accounts Receivable module for further processing" | BIL §4 |
| A-BQ-12 | **Company→AR outstanding** | Company Settlement | "treated as outstanding until payment is received" | BIL §4 |
| A-BQ-13 | **Staff→AR حفظ** | Staff Settlement | "saved in the Accounts Receivables module" | BIL §4 |
| A-BQ-14 | **Exchange Rate/Local تلقائي** | Foreign Exchange Settlement | "Exchange Rate for the selected Currency Code and the amount in local currency is displayed" | BIL §4 |
| A-BQ-15 | **تنبيه مسح الغرف عند Amend** | تغيير Function dates | "alert message to clear the selected Add on Rooms, Associated rooms" | BOK Amend |
| A-BQ-16 | **رسالة Requirement عند Amend** | استرجاع حجز ذي متطلبات | "message... requirement entry has been made" + Nullify عند Exit | BOK Amend |
| A-BQ-17 | **عدّاد Defined لكل مجموعة** | إدراج/استبعاد أصناف في Menu Card | "the count of menu items under each group gets altered accordingly" | CFG §9 |
| A-BQ-18 | **Balance من Retention/Refund** | إدخالها | "total deposit will be get deducted... balance amount will be displayed" | BIL §10 |

## 5. التوقيت والتجميد

- **نفس accounting date** للتسوية (قاعدة حاجبة).
- **Requirement Finalized** = تجميد مع سماح تحرير بتنبيه (نموذج "تجميد ناعم").
- **Retention/Refund Saved** = تجميد كامل.
- **Event ماضٍ** = الحالة فقط.
- **Cancel Bill** = "This bill will **not populate in the records again**" (إزالة نهائية من العرض — أقرب لحذف منطقي للفاكورة غير المسواة).
