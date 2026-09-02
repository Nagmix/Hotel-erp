# 05 — قواعد العمل (Business Rules) — وحدة Banquets

> BR-BQ-01..16 — الوحدة الهجينة: قواعد FO الحجزية فوق قواعد POS الكاشيرية.

---

## BR-BQ-01 — نمطا الحجز والاحتكار المكاني

**المصدر:** BOK ص10/20-21.

1. **Across Dates:** "booked starting from the moment From Time and will remain occupied till the To Time is over for an entered date range... **no other bookings can be taken** until the function date is over" — احتكار مستمر (يُعرض **معتماً** في Chart).
2. **الفترة الزمنية:** القاعة لنطاق ساعي عبر تواريخ متعددة (تتوفر حجوزات أخرى خارجها).
3. **Inquiry بلا قاعة:** "Inquiry Bookings can be taken without selecting a Function Room" — الاستفسار أخف من الحجز.
4. Add on/Associated **ضمن حدود** Function start/End حصراً.

## BR-BQ-02 — بوابة التقويم (Event Calendar Gate)

**المصدر:** SET §10.

- "Only if the status is 'Yes', the **supervisor\user is allowed to do booking** on that specified date" — حظر تقويمي صريح (Booking Made By يحدد الجمهور).
- Dry Day يظهر في "Booking, Requirement Entry and Availability Chart".
- تعديل حدث ماضٍ = الحالة فقط.
- "If a user is defining an event calendar for a day which has a booking already done it will display 'Reservation record exists for the given date & time'".

## BR-BQ-03 — ألوان الحالة ودمجها

**المصدر:** SET §11 + LUK §2.

1. لون فريد لكل Reservation Status (تعريف) → عرض في Availability + Function Room Help.
2. **الدمج الافتراضي:** "All the user defined reservation status will be **compacted\combined to their basic reservation types**... display under the **four basic**" — إلا إذا **INI 408=1**.
3. **ألوان الرسم الموثقة:** Management Block = أحمر + Maintenance = أخضر (مع *) · **FP Printed = أزرق** · **FP Finalized = بنفسجي** · **Room restricted = رمادي** · الملغى في Scan = **وردي** · Supplementary = **أخضر**.

## BR-BQ-04 — قواعد المنفذ والجلسة (POS مشتركة)

1. "The same person **cannot operate 2 shifts** at a time" (BIL §1).
2. "User must be **PO Cashier**... grouped as POCashier using Create User" (BIL §2).
3. "The **Server date and the accounting date should be the same**" عند فتح المنفذ.
4. **Skipping Session** → تحذير؛ آخر جلسة + تغير التاريخ → الاستمرار بنفس accounting date ثم فتح جديد.
5. **Close Shift ب password** + MA 26 (تسوية المعلقات إلزامية عند Yes).
6. "Without closing the previously opened shift, the cashier **cannot open another shift**".
7. Close Outlet للتاريخ الحالي — "will **record sales accurately**".

## BR-BQ-05 — التسوية الحاجبة (Settlement Gates)

**المصدر:** BIL §4.

1. **نفس التاريخ المحاسبي:** "bills must be settled during the **same accounting date**".
2. **Void ممنوع في BNQ:** "In Banquets Void Settlement is restricted".
3. **التحويلات إلى AR:** Credit Card / Company / Staff → كلها "sent to/saved in the Accounts Receivable" — Company "treated as **outstanding** until payment is received".
4. **Blacklist:** "If a Company is Blacklisted, then the message will be displayed along with the **authorized person's name and the reason**" — **إشعار موثق المسؤولية**.
5. **Available Credit** يعرض فقط عند MA 21=Yes.
6. **Multiple Settlement:** Cash + نمط واحد آخر على الأقل (باستثناء NC/Comp/Void/Hold).
7. **Resettlement conditions:** "only if it has **not been originally printed at Front Office** and has **not been settled to the room account** of the guest and the guest has already checked out" [⚠️ [UNCERTAIN] البند الأخير ملتبس] + MA 3=Yes → **لا إعادة تسوية لنقدي/عملات** + صلاحية Resettle من User Access.

## BR-BQ-06 — قواعد الإيراد (Revenue Recognition)

1. **Complimentary وNon Chargeable: "not considered as Sales for the Hotel"** — استثناء صريح من الإيراد (مرحلة 6).
2. **Project/Payment المرحلي:** نسب Pre/During/Post-Function.
3. **Cancellation Policy:** "Days range, the value type (V or P)... that will be **charged** to the Party in case... cancels".

## BR-BQ-07 — الودائع (قفل مالي وقائي)

1. "You **cannot cancel Bookings with DEPOSITS**. You should make the paid outs first" (BOK Cancel).
2. No-Show: "If deposit amount is entered... cancellation of such reservation(s) **will be restricted**".
3. Deposit "for a single or multiple function rooms **except Inquiry bookings**".
4. **Running Balance =** Total Deposit − (Refund + Retention).
5. Retention/Refund: **قابل للتعديل بعد Confirm — مجمّد بعد Save**.
6. حذف وديعة مع رصيد متبقٍ → رسالة تنبيه.
7. **Bill ↔ Deposit:** "Deposit is pending for this reservation. Do you want to attach?" عند الفوترة.

## BR-BQ-08 — Requirement Entry (قواعد ورقة العمل)

1. القيم من الحجز (Pax/Rate/Hall) **قابلة للتعديل** (INI 346 يضبط تعديل Pax).
2. **F11** = إعادة تسمية الصنف · **F12** = Complimentary · الافتراضي Chargeable.
3. **Allowed لكل مجموعة** يقيّد عدد الأصناف القابلة للطلب.
4. **Editable flag:** Yes → "Item name can be editable in requirement entry".
5. **Finalize** → تجميد + تحرير لاحق بتنبيه.
6. **Copy Requirement Entry** ينسخ: الأصناف + Special Instructions + **rate type (chargeable/complimentary/replacement)**.
7. **Amend الحجز → Nullify للمتطلبات** (إبطال موجّه).
8. "Service timings... **common for the entire** Requirement Entry".

## BR-BQ-09 — Auto Indent (الجسر المخزني)

"Select the department for which the items should be **indented**" + "ingredient details will be obtained from the **recipe**... or... **linked manually**" + "If it is an open item, the inventory items should be **tagged** as no recipe will be available" + "recipe details will **populate based on the department** selected".

## BR-BQ-10 — Corporate Rates (الأسعار التعاقدية)

1. 3 عائلات (Room/F&B per Event Type/Non F&B per Equipment) بـ Rate Id + Applicable date.
2. Tagging إلى **Company Master** → تُطبق في "Banquet Booking and Requirement Entry".
3. Default Hall Tax من **Print Forms program** — نقطة تكامل ضريبي مركزية.
4. **الحذف بـ F5** — الاستثناء الوحيد الموثق عن "لا حذف".

## BR-BQ-11 — Modify-Locked العام

"cannot be deleted, only status can be changed from Active to Passive or vice versa" — في 9+ كيانات (Associated/Function Room/Setup Style/Cancellation Policy/Supplier rates/Event Template/...) + "Passive records will be moved to the bottom of the grid... **not appear for operations**". + **قاعدة زمنية للروابط:** Session/Order Type المستقبلية تُعدَّل كاملة؛ اليومية = الحالة فقط.

## BR-BQ-12 — Sub Venues (الحصرية)

"the sub-Function room(s) that have been tagged... **will not be displayed**... to tag with other main Function rooms" — المجموعة الفرعية حصرية للأم. Passive في Function Room → تختفي من القائمة هنا.

## BR-BQ-13 — Amenity/Print

1. Function Prospectus: FP Printed → أزرق؛ FP Finalized → بنفسجي.
2. **Print Order + Menu Group Sequence** يتحكمان بترتيب الطباعة ("dependent on the menu group selected" / "followed to print the Menu Groups in Function Prospectus").
3. المصمم: "The sum of Header rows, Footer rows, body rows must be equal to the total length of the stationery. (**6 rows = 1 Inch**)".

## BR-BQ-14 — الضرائب (بنى مركبة)

1. **Inclusive/Exclusive toggle** في الحجز (بجوار Hall Charges).
2. بنى العرض من **INI 409**؛ الافتراضية للقاعة من Print Forms.
3. Menu Master: Tax Structure لكل صنف (+ GL Code في النمط الفردي!).

## BR-BQ-15 — أرقام مولدة آلياً

Reservation Number (عند الحفظ) · كل أكواد المرجعيات (Country/State/City/Floor/Reasons/ItemType/Equipment/Categories/Policy/Question/Template/ServiceManager) · Vouchers للودائع (مع نسخ معدّلة/محذوفة).

## BR-BQ-16 — التخصيص الشخصي للرسم

Columns Order + Function Room Order: "The sequence number **cannot be left blank or zeros**" + "When you click Save, **the program exits. You have to load the program again**" — إعادة تحميل إلزامية.
