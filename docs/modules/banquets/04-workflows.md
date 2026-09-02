# 04 — سير العمل (Workflows) — وحدة Banquets

> WF-BQ-01..16 من المتن. دورة الحدث الكاملة: حجز → متطلبات → تكاليف → indent آلي → وديعة → فاتورة → تسوية → إقفال.

---

## WF-BQ-01 — إعداد قاعة (Function Room كاملة)

**المصدر:** CFG §§1-5 + SET §§7/6.

1. Floor (SET §7) + Function Room Features + Setup Style (أنماط الجلوس بسعة).
2. Configure → Function Room → Applicable From (≥ accounting date) + Property + Room Type + الاسم + ربط Associated Rooms.
3. **DETAILS:** Location/Floor/Available Hours/**Minimum Revenue**/Security Type + Venue Dimensions → Enter.
4. **FEATURES:** Venue Features + Room Description.
5. **SEATING:** السعة لكل نمط (مع صور الأنماط).
6. **PICTURES/LAYOUT/LOCATION:** الصور + الأوصاف → Save.
7. (اختياري) Tag Sub Venues: رئيسية + فرعيات (مدمجة عرضياً في الحجز/التوافر/البلوك).
8. (اختياري) Associated Room مستقلة (Green/Storage/Pre-Function).

## WF-BQ-02 — ضبط التقويم والسياسات

**المصدر:** SET §10 + CFG §4.

1. Setup Event Calendar: Property + Event Name + Day Type + From/To + **Dry Day** + **Booking Allowed** + Booking Made By → Save (يظهر في اليوم).
2. Cancellation Policy: Description + **Days From/To + Value Type (V/P) + Value** → Save.
3. Reservation Status (الملونة): Name + Type + Color + Sequence.

## WF-BQ-03 — حجز حدث (Make Booking)

**المصدر:** BOK §1 ص6-21.

1. Scan and Search Engine → **Make**.
2. **Party Details:** Name/Email/Mobile/Handled By/Security/Catering (+Address +Handled-By أخرى) — بريد Party → **auto email بعد الحجز** (بشرط PDF access + Outlook Express).
3. **Company Information** (F1) + Contact Person + Booker Type/Code.
4. **Booking Info:** Market Segment/Business Source (من **FO defaults**) + Source Company + Reference/Sales Person/Office/Location.
5. **Billing Info:** Payment By (افتراضي Party) + Payment Details + **PAN#** + Pay Mode (من FO defaults).
6. **Payment Terms:** نسب Pre/During/Post-Function + **Cancellation Policy** (عرض التفاصيل).
7. **Main Function Room:** Property + Event Type + Status + النمط (**Across Dates** أو فترة زمنية) + From/To date/time → **يفتح Availability تلقائياً** + Expected/Guaranteed Pax + Rate/Pax + Hall Charges + Tax (INI 409) + **Inclusive/Exclusive toggle** + Follow up (Banquet Staff!) + Function Room Help (**Inquiry بلا قاعة!**).
8. **Other Details:** Add on/Associated Rooms (داخل حدود الحدث) + Service Managers + Host/Chief Guest (+لافتات الغرفة/الخارج!) + Special Instructions/Flow of Events + Department Instructions + Seating Styles.
9. Save → تأكيد → **Reservation Number** — أو **New** (حجز آخر بنفس Res# وتفاصيل Party المشتركة).

## WF-BQ-04 — تعديل حجز (Amend)

**المصدر:** BOK Amend ص22-27.

1. نقر مزدوج/يمين → Amend.
2. **تغيير Function Start/End** → تنبيه مسح Add on/Associated → Yes.
3. تعديلات **يومية** (غرف/مديرين/تعليمات لكل تاريخ عبر نطاق الحدث).
4. استرجاع حجز له Requirement Entry → رسالة وجوده → Exit → **Nullify? Yes** (إبطال ورقة العمل).
5. Save.

## WF-BQ-05 — إلغاء الحجز / No-Show

**المصدر:** BOK §1-2.

**إلغاء فردي:** يمين → Cancel → **الكل أو الحدث المحدد** → Reason + Remarks + Authorized User → Confirm.
- **قيد الودائع:** "You cannot cancel Bookings with DEPOSITS. You should make the **paid outs** first".

**No-Show الجماعي:** (تواريخ ≤ الخادم تلقائياً!) → **F11** على تحديد متعدد → Reason/Remarks/Authorized → Confirm × 2 — الودائع تمنع أيضاً.

## WF-BQ-06 — نسخ حجز (Copy)

**المصدر:** BOK Copy ص30-34. المنسوخ: "Party details, Event type, Expected pax, guaranteed pax, Rate\Pax, Hall Charges... and **seating styles**" → إدخال التاريخ/الغرف/الإضافات → Save. **قيد:** "Copy of **Inquiry** Bookings is restricted".

## WF-BQ-07 — حظر/تحرير قاعة (Block/Release)

**المصدر:** BOK §3. From/To date/time + Property + Room Type (Function/Associated) + Associated + **Block Type: Management (أحمر)/Maintenance (أخضر)** + Reason + Description + Department + Specification → Block → يظهر في Availability. **Release:** نقر مزدوج + Release.

## WF-BQ-08 — ورقة المتطلبات (Requirement Entry — 4 مسارات)

**المصدر:** BIL §11 ص49-60.

1. Resv# → تحميل 3 تبويبات (Event/Contact/Billing) + Guaranteed Pax/Rate/Pax/Hall (قابلة للتعديل! + INI 346) + Tax Inclusive/Exclusive.
2. المسار: **Package Menu Card** (أصنافه → انتقاء + تعديل كميات Non F&B) / **Menu Card** / **Items** (F&B/Non F&B/**Open Items**) / **Copy** (محرك بحث بـ 9 معايير! → View/Copy — "will copy the Requirement Entry Items, Special Instructions, the rate type like chargeable or complimentary or replacement Item").
3. الأصناف chargeable افتراضياً — **F11 إعادة تسمية** / **F12 Complimentary**.
4. Save → **Finalize window**: Confirm (تثبيت) أو حفظ بلا تثبيت — المثبت: "Requirement Entry has been Finalized Do you like to Edit?".

## WF-BQ-09 — التكلفة المسبقة (Pre Costing Chef Eng)

**المصدر:** BIL §12. Resv# (F1) → تحميل أصناف المتطلبات → لكل صنف: **Department** (وجهة الـ indent) + مصدر المكونات: **Recipe** (إن وجدت) أو **ربط Inventory Items يدوي** ("If it is an open item, the inventory items should be tagged as no recipe will be available") → Tag → Save (قابل للتعديل بنفس Res#).

## WF-BQ-10 — الترحيل الآلي للمخزن (Auto Indent) ⭐

**المصدر:** BIL §13 ص65-66.

1. Auto Indent → New → **Indent#** (F1) + **Work Sheet#** (F1 → Res# + Party Name تلقائياً).
2. Indent Date + Reference + **Department + Cost Center**.
3. **"The recipe details will populate based on the department selected"** → حفظ الـ indent الموجه للمخزن (MGT).

> **هذه هي القناة الموثقة لـ UNK-011:** BNQ → (Recipes/Inventory) → MGT Indent.

## WF-BQ-11 — الودائع (Deposit)

**المصدر:** BIL §9. بحث (Res#/Function date/Property/Event) → (باستثناء Inquiry!) → التبويبات:
- **Cash:** Amount + Particulars → Confirm → Print voucher.
- **Card:** Amount + Type + # + Bank + Expiry (mm/yyyy) + Auth# + Holder + Particulars.
- **Cheque:** Amount + # + Bank + Branch + Date + Particulars.
- الإيصالات: **أصلي/معدّل/محذوف** (نماذج طباعة مستقلة!) + قيد الحذف مع رصيد متبقٍ → رسالة.

**العرض:** Projected Amount (Rate/Pax + Hall) + Deposit Amount + Running Balance (من Refund/Retention).

## WF-BQ-12 — الاستقطاع/الاسترداد (Refund/Retention)

**المصدر:** BIL §10. (لذوات الودائع فقط) → Transaction Type (**Retention/Refund**) + Amount + Reason → Confirm (قابل للتعديل قبل Save — Balance يتحدث) → **Save = تجميد** ("You will not able to perform modify\delete... after SAVING").

## WF-BQ-13 — فاتورة الوليمة (Banquet Bill + التقسيم الثلاثي)

**المصدر:** BIL §3.

1. Billing → Banquet Bill → بحث (Res#/Function date/Company/Party) → (شبكة ملونة = سابقة) → Select.
2. (إضافات) Supplementary Items: Code → Menu item → Sub Menu → **أخضر**.
3. التفكيك الأيسر + Summary الأيمن (+Guest address عبر Details).
4. التقسيم: **Amount Split** (Net Amount لكل دافع + الباقي تلقائي + **Discount prompt** — Amount أو %) / **Item Split** / **No of Split** (متساوٍ).
5. **Deposit pending → "Do you want to attach?"** → OK.
6. **Invoice Print / Print Bill / Cancel Bill (يحذف الفاتورة)**.

## WF-BQ-14 — تسوية الوليمة (Settlement — 11 نمطاً)

**المصدر:** BIL §4 ص18-31.

1. Bill# (F1) → User → تحديد → التفاصيل تلقائية.
2. النمط: Cash / Foreign Exchange / **Credit Card** (→ AR! + MA 8 swipe + **بطاقات متعددة بالأزرار المرقمة**) / Cheque / **Company** (→ AR outstanding + Available Credit بـ MA 21 + **رسالة Blacklist باسم المُدرِج وسببه!**) / **Guest** (Room# → بيانات الضيف) / Staff (→ AR أيضاً) / **Void (ممنوع!)** / Coupons / **Complimentary (ليست مبيعات!)** / **Non Chargeable (MA 16 + NC Type/Dept — ليست مبيعات!)**.
3. **Multiple:** Cash + نمط آخر (باستثناء NC/Comp/Void/Hold) — مثال NRS 5,976.
4. **Resettlement:** بلا طباعة FO + بلا تسوية غرفة + الضيف غير مغادر + **صلاحية POS User Access** + MA 3 (يحظر إعادة النقدي/العملات).
5. **"bills must be settled during the same accounting date"**.

## WF-BQ-15 — الإقفال اليومي (Close Shift → Close Outlet)

**المصدر:** BIL §§5-6.

1. Close Shift: Cashier + **Password** → الملخص → Close (MA 26: المعلقات تمنع).
2. Close Outlet: اختيار → Close → Confirm — "will record sales accurately".

## WF-BQ-16 — إعادة الطباعة والمعلقات

**المصدر:** BIL §§7-8. **Reprint** (تاريخ ≤ اليوم) → انتقاء → عرض → Invoice/Bill Print (+Cancel Bill يحذف من السجلات!). **Pending** (قبل التسوية): نفس البنية + أعمدة (Date/Session/Table-Room/Res-Bill#/Amount/Time/Server/User/Total).
