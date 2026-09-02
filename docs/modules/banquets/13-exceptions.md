# 13 — الحالات الحدية والاستثناءات (Edge Cases) — وحدة Banquets

> 26 حالة موثقة/مستنتجة — أثقلها: الودائع الحاجبة والاحتكار المكاني والتجميد الناعم.

---

## 1. ودائع وإلغاء

| # | الحالة | السلوك | المصدر |
|---|---|---|---|
| EC-BQ-01 | إلغاء حجز له وديعة | **ممنوع** — "make the paid outs first" | BOK ص28 |
| EC-BQ-02 | No-Show لحجز ذي وديعة | "cancellation... will be **restricted**" | BOK §2 |
| EC-BQ-03 | حذف وديعة وباقي رصيد | رسالة تنبيه بوجود الرصيد | BIL §9 ص45 |
| EC-BQ-04 | Refund/Retention بعد Save | تجميد كامل — لا تعديل/حذف | BIL §10 |
| EC-BQ-05 | Deposit على Inquiry | ممنوع — "except Inquiry bookings" | BIL §9 |
| EC-BQ-06 | نسخ حجز Inquiry | **ممنوع** | BOK ص34 |

## 2. احتكار وتقويم

| # | الحالة | السلوك | المصدر |
|---|---|---|---|
| EC-BQ-07 | حجز ثانٍ خلال Across Dates | **ممنوع** — "no other bookings can be taken until the function date is over" | BOK ص20 |
| EC-BQ-08 | حجز بيوم Booking Allowed=No | ممنوع (حسب Booking Made By) | SET §10 |
| EC-BQ-09 | Add on خارج نطاق الحدث | ممنوع — "not exceeding" | BOK ص12 |
| EC-BQ-10 | تعريف Event على يوم فيه حجز | "Reservation record exists for the given date & time" | SET §10 |
| EC-BQ-11 | تعديل Event ماضٍ | الحالة فقط | SET §10 |

## 3. تسوية وطباعة

| # | الحالة | السلوك | المصدر |
|---|---|---|---|
| EC-BQ-12 | Void في BNQ | **ممنوع برسالة** | BIL §4 |
| EC-BQ-13 | NC بلا MA 16 | الخيار غير مفعل | BIL §4 |
| EC-BQ-14 | إعادة تسوية (نقدي + MA 3=Yes) | ممنوعة | BIL §4 |
| EC-BQ-15 | إعادة تسوية مطبوعة FO / مسواة غرفة | ممنوعة | BIL §4 |
| EC-BQ-16 | تسوية بعد تغير accounting date | ممنوعة — "same accounting date" | BIL §4 |
| EC-BQ-17 | تسوية شركة Blacklisted | **رسالة بالاسم والسبب** (استمرار؟ [UNCERTAIN] — الأرجح استمرار بوعي) | BIL §4 |
| EC-BQ-18 | Reprint بتاريخ مستقبلي | "end date cannot be greater than the current date" | BIL §7 |
| EC-BQ-19 | Cancel Bill بعد الطباعة | "will not populate in the records again" | BIL §§7-8 |

## 4. الجلسات والإغلاق

| # | الحالة | السلوك | المصدر |
|---|---|---|---|
| EC-BQ-20 | كاشير بورديتين معاً | ممنوع — "cannot operate 2 shifts at a time" | BIL §1 |
| EC-BQ-21 | فتح Shift بلا إغلاق السابق | ممنوع | BIL §5 |
| EC-BQ-22 | Close Shift بمعلقات (MA 26=Yes) | ممنوع | BIL §5 |
| EC-BQ-23 | تخطي Session | تحذير Continue/Cancel | BIL §2 |
| EC-BQ-24 | آخر جلسة + تبدل التاريخ | "continue with the same accounting date" | BIL §2 |

## 5. متطلبات وورش عمل

| # | الحالة | السلوك | المصدر |
|---|---|---|---|
| EC-BQ-25 | Amendment بعد Requirement | **Nullify prompt** — إبطال ورقة العمل بقرار | BOK Amend |
| EC-BQ-26 | تعديل Requirement Finalized | تنبيه "Do you like to Edit?" | BIL §11 |
| EC-BQ-27 | Inquiry بلا قاعة | مسموح | BOK ص11 |

## 6. مرجعيات وواجهة

| # | الحالة | السلوك | المصدر |
|---|---|---|---|
| EC-BQ-28 | >4 أحداث في يوم تقويم | **سهم أزرق + أسهم لوحة مفاتيح** | SET §10 |
| EC-BQ-29 | Tag Sub Venue مرتين | ممنوع (حصرية للأم) | CFG §10 |
| EC-BQ-30 | Passive Sub Venue | يختفي من Tag هنا (لا من Function Room) | CFG §10 |
| EC-BQ-31 | Sequence فراغ/صفر/مكرر | ممنوع (Columns/Rooms Order + Status Sequence) | LUK §2 + SET §11 |
| EC-BQ-32 | تخصيص أعمدة ثم Save | **خروج من البرنامج** — إعادة تحميل إلزامية | LUK §2 |
| EC-BQ-33 | 3+ أيام في Function Room Availability | ممنوع (الحد 3) | LUK §1 |

## 7. استنتاجات تصميمية

1. **الودائع نقطة تحكم مركزية** (5 حالات) — تستحق Badges + حاجز واضح في UI الجديد.
2. **التجميد الناعم (Finalize/Save)** نمط متدرج — يعاد بعTitled dialog عربي صريح.
3. **إعادة التحميل بعد التخصيص** = عيب UX أصلي يُصلح بالحفظ الفوري.
