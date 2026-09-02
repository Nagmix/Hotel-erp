# 13 — الحالات الاستثنائية (Exceptions & Edge Cases) — وحدة Front Office

> الحالات الخارجة عن المسار السعيد، الموثقة نصاً.

---

| # | الحالة | السلوك الموثق | المصدر |
|---|---|---|---|
| E1 | ضيف بلا حجز ممتلئ الفندق | Walk-in يعرض OOO لمنع check-in؛ Turn Away يسجل الرفض → Denial Report | REG ص17 + §11 |
| E2 | حجز مكرر | تنبيه Duplicate قبل الحفظ | RES ص8 |
| E3 | أسماء ضيوف متشابهة في History | Guest Profile screen للاختيار | RES ص8 |
| E4 | غرفة معلمة صيانة عند التخصيص | Alert message | REG ص33 |
| E5 | تعديل تعرفة تاريخ ماضٍ | Error message — ممنوع | REG ص47 |
| E6 | إلغاء حجز مع ودائع | إجبار نافذة Deposit → Refund | RES §1.3 |
| E7 | تسوية غير متطابقة | "Settlement is not tallied" → Cancel | CAS ص77-78 |
| E8 | تسقاط نصف يوم | Day Charge = 0.5 | CAS ص21 |
| E9 | حجز Waitlist ثم توفر | Re-Instate patterns | RES §1.7-1.8 |
| E10 | No-Show بعد Night Audit | وسم تلقائي + Retention | RES §1.8 + §6 |
| E11 | إعادة فتح فوليو بعد Night Audit | **ممنوع** (Re-Instate قبل NA فقط) | CAS ص80 |
| E12 | إعادة فتح غرفة مرتبطة | يجب فتح Main Room أولاً | CAS ص82 |
| E13 | إشغال متعدد يطلب فواتير منفصلة | Split Folios (Pax>1) | CAS §7 |
| E14 | Split F&B لأنواع متعددة | حسب نوع القائمة + Tips + Round Off | CAS §6 |
| E15 | تغطية تغيير/تبديل غرف بعد تاريخ اليوم | ممنوع (التاريخ المحاسبي فقط) | RES ص60 |
| E16 | مغادرة متأخرة عن اليوم | Confirm Checkouts (تعديل وقت المغادرة) | CAS §10 |
| E17 | ضيف VIP يخفي حضوره | Mask Guests | REG §10 |
| E18 | مغادرة pax دون الرئيسي | Pax Checkout | CAS §11 |
| E19 | حظر بيع نوع غرفة ليوم | Close Room Inventory (C) — walk-ins مستثناة | RES §7 |
| E20 | overbooking محدود | Daywise Over Booking بسقف | REG §22 |
| E21 | تعارض خصومات على ضريبة | Yes/No/Exempt | CAS ص27 |
| E22 | رسائل نقدية لغير المقيمين | Miscellaneous Charges (بدون غرفة) | CAS §19 |
| E23 | مديونية تجاوزت حد الائتمان | Credit Limit (بزيادة موثقة + Card Use Amount) | REG §6 |
| E24 | سلوك الاتصال الهاتفي للضيف المنتهي | إلغاء التمديد تلقائياً (two-way link) | REG §102 |
| E25 | تعديل broadcast منتهي | ممنوع — المستقبلي فقط | REG ص99-100 |
| E26 | تكرار Room Rate posting | الأخير يسجل فقط | CAS ص22 |
| E27 | حجوزات وكيل بوصول متعدد بنفس اليوم | اختيار checkbox متعدد في Invoice by Arrival | REG ص68-69 |
| E28 | إقامة طويلة بدفعات | Cutoff Date (فترة أولى تسوى والباقي لاحقاً) | CAS §36-37 |
