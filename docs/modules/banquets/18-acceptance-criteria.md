# 18 — معايير القبول والدخان (Acceptance Criteria & Smoke Test) — وحدة Banquets

> AC-BQ-01..10 (42 معياراً) + **Smoke Test 26 خطوة**.

---

## 1. مجموعات معايير القبول

### AC-BQ-01 — المرجعيات المكانية

| # | المعيار | التتبع |
|---|---|---|
| 1.1 | Function Room بـ 6 تبويبات (Dimensions/Minimum Revenue/Seating per style + صور) | 01 §1.3 |
| 1.2 | Associated Room (3 أنواع) + Block تزامني مع الرئيسية | 01 §1.2 + WF-BQ-07 |
| 1.3 | Sub Venues حصرية (لا تُوسم لأمين) ومدمجة العرض | BR-BQ-12 |
| 1.4 | Applicable From ≥ accounting date | V-BQ-06 |

### AC-BQ-02 — التقويم والحالات

| # | المعيار |
|---|---|
| 2.1 | Event Calendar (Dry Day/Booking Allowed/Made By) **يحجب الحجز** فعلياً (BR-BQ-02) |
| 2.2 | Reservation Status ملونة + Sequence فريد + **الدمج الافتراضي للرسم** وINI 408=1 يفصّل (BR-BQ-03) |
| 2.3 | >4 أحداث/يوم → قائمة بديلة (بلا سهم لوحة مفاتيح في الجديد) |

### AC-BQ-03 — الحجز

| # | المعيار |
|---|---|
| 3.1 | Make بـ 7 أقسام + FO defaults (Market/Source/PayMode) تسحب تلقائياً (I-BQ-01) |
| 3.2 | **Across Dates** يحتكر (حجز ثانٍ مرفوض) ويُعرض داكناً (EC-BQ-07) |
| 3.3 | Inquiry بلا قاعة (EC-BQ-27) + **نسخه ممنوع** (EC-BQ-06) |
| 3.4 | Payment Terms بنسب Pre/During/Post + Cancellation Policy تُعرض |
| 3.5 | Amend بتغيير التواريخ → تنبيه مسح الغرف + Nullify للمتطلبات (A-BQ-15/16) |
| 3.6 | **إلغاء ذي وديعة مرفوض** (EC-BQ-01) — No-Show كذلك (EC-BQ-02) |
| 3.7 | Copy ينقل الحزم الموثقة (Party/Event/Pax/Rate/Hall/Seating) (WF-BQ-06) |

### AC-BQ-04 — المتطلبات والتكلفة

| # | المعيار |
|---|---|
| 4.1 | 4 مسارات Requirement (Package/Menu/Items/Copy بمحرك 9 معايير) (WF-BQ-08) |
| 4.2 | **F11 rename + F12 complimentary** (أزرار ظاهرة في الجديد) |
| 4.3 | Allowed لكل مجموعة يقيّد الطلب + Editable flag يعمل |
| 4.4 | Finalize → تجميد ناعم بتنبيه (EC-BQ-26) |
| 4.5 | Pre Costing: Recipe أو Inventory يدوي (Open Item → tagging) (WF-BQ-09) |

### AC-BQ-05 — Auto Indent ⭐ (يحسم UNK-011)

| # | المعيار |
|---|---|
| 5.1 | Auto Indent: Work Sheet# → Res/Party تلقائي (A-BQ-06) |
| 5.2 | Department/CC → recipes populate (A-BQ-07) → **Material Request في MGT** (F-BQ-6) |

### AC-BQ-06 — الودائع

| # | المعيار |
|---|---|
| 6.1 | 3 وسائل + Projected/Deposit/Running Balance (WF-BQ-11) |
| 6.2 | Vouchers أصلي/Modified/Deleted (F-BQ-8) |
| 6.3 | Inquiry ممنوعة من الوديعة (EC-BQ-05) |
| 6.4 | Refund/Retention: تعديل قبل Save فقط (EC-BQ-04) + Balance يتحرك (A-BQ-18) |

### AC-BQ-07 — الفوترة والتسوية

| # | المعيار |
|---|---|
| 7.1 | 3 أنماط تقسيم + Discount prompt + Balance تلقائي (WF-BQ-13) |
| 7.2 | Deposit attach prompt (A-BQ-03) |
| 7.3 | 11 نمطاً + Multiple (Cash+آخر) + **Void مرفوض** (BR-BQ-05) |
| 7.4 | CC/Company/Staff → **AR** (فعلياً) + Company → outstanding + Blacklist بالاسم/السبب (I-BQ-04/05/06) |
| 7.5 | Guest → **FO Folio** ببيانات الضيف (A-BQ-10) |
| 7.6 | Comp/NC **ليست مبيعات** (E-BQ-12 → تُستبعد من Sales Journal) |
| 7.7 | Resettlement بشروطه (بلا FO print/room/checkout + MA 3) (BR-BQ-05) |
| 7.8 | التسوية **بنفس accounting date** (V-BQ-24) |

### AC-BQ-08 — الإقفال اليومي

| # | المعيار |
|---|---|
| 8.1 | Open Shift (كاشير واحد/وقت) + PO Cashier role (BR-BQ-04) |
| 8.2 | Skipping تحذير + آخر جلسة/تاريخ (EC-BQ-23/24) |
| 8.3 | Close Shift بكلمة مرور + MA 26 (EC-BQ-22) → Close Outlet (BR-BQ-04) |

### AC-BQ-09 — الاستعلامات

| # | المعيار |
|---|---|
| 9.1 | Function Room Availability ≤3 أيام + بلوكات ملونة + hourly |
| 9.2 | **Availability Chart كامل**: قسمان + Back/Next + ألوان الحالة + dry days + FP أزرق/بنفسجي + restricted رمادي + Booking/Amend من الرسم |
| 9.3 | تخصيص الأعمدة/القاعات **بلا إعادة تحميل** (تحسين مؤكد) |

### AC-BQ-10 — Corporate Rates والطباعة

| # | المعيار |
|---|---|
| 10.1 | 3 عائلات Rates + Tagging إلى Company + تطبيقها في Booking/Requirement (BR-BQ-10) |
| 10.2 | F5 حذف Rate (الاستثناء الوحيد) |
| 10.3 | Print Forms الأربعة + FP بترتيب Menu Group Sequence (F-BQ-4) |

---

## 2. Smoke Test (26 خطوة)

**التأسيس:** 1. Function Room بـ 6 تبويبات → ✅AC-1.1 · 2. Event Calendar بحظر حجز → محاولة الحجز **مرفوضة** → ✅AC-2.1 · 3. Reservation Status ملونة
**الحجز:** 4. Make (FO defaults تلقائي) → 5. **Across-Dates** ثم حجز ثانٍ **مرفوض** → ✅AC-3.1/3.2 · 6. Inquiry بلا قاعة → ✅AC-3.3 · 7. Copy الحجز → 8. نسخ Inquiry **مرفوض** → ✅AC-3.7
**الودائع:** 9. Deposit (3 وسائل) + Voucher → 10. **إلغاء ذي وديعة مرفوض** → ✅AC-3.6/6.1
**المتطلبات:** 11. Requirement (Menu Card) + F12 مجاني → 12. Finalize → تعديل بتنبيه → ✅AC-4.2/4.4 · 13. Pre Costing بـ Recipe → 14. **Auto Indent → Material Request في MGT** → ✅AC-5.1/5.2
**الفوترة:** 15. Bill + Amount Split + Discount → 16. Deposit attach prompt → ✅AC-7.1/7.2
**التسوية:** 17. Company Settlement → AR outstanding + Blacklist message → ✅AC-7.4 · 18. Guest → FO Folio ببيانات الضيف → ✅AC-7.5 · 19. **Void مرفوض** → ✅AC-7.3 · 20. Multiple (Cash+CC) → 21. Complimentary **ليست مبيعات** → ✅AC-7.6
**الإقفال:** 22. Close Shift (password + معلقات MA 26) → Close Outlet → ✅AC-8.3
**الاستعلام:** 23. Availability Chart كامل الألوان → 24. FP Print → أزرق → ✅AC-9.2/10.3
**الحوكمة:** 25. Refund بعد Save **مجمّد** → ✅AC-6.4 · 26. Event ماضٍ → الحالة فقط → ✅AC-2.1

---

## 3. عتبة الانتقال

- ✅ 42 معياراً مربوطاً بالتتبع + 26 خطوة دخان (11 حالة رفض)
- ✅ UNK-011 **Resolved كاملاً** (أعلى إنجاز)
- ⬜ QR-BQ: مطابقة Resettlement الغامضة (GAP-BQ-02) — قرار تنفيذي مؤجل
- **نقطة الاستئناف القادمة:** HRP (الرواتب — 4 ملفات/253 ص) وفق الترتيب.
