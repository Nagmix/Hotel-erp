# 04 — عائلة الإشغال والمقيمين والتدقيق (REP §24–50)

> ~27 تقريراً تغطي الضيف من الكوبونات إلى تعليمات الغرف، مع **مجموعة Audit Reports (31.1–31.8)** — أغنى مجموعة تدقيق داخلي في المشروع.

---

## 1. الخدمات الموجهة للضيف المقيم (24–33)

| # | التقرير | الخصوصية الموثقة |
|---|---|---|
| 24 | **Coupon Printing** | كوبونات خطط الطعام "based on plan definition for in-house guests" · Arrivals أو **In-House** (مع In-House يُدخل Guest Name) · **Room Type** · نوع الخطة: **Break Fast / Lunch / Dinner** · Proceed ثم "Change option under **Coupons In-house as YES** and Print" · يتطلب SYS+FO print forms |
| 25 | **Message Printing** | رسائل "Awaited Checkin **or** In House guests" · **New messages only / Messages for the day** · Load (أو Enter مرتين) · يعرض "the room number... time of message, the **User who recorded** the message and the status" |
| 26 | **Guest Trace Report** | تفضيلات الضيوف المسجلة عند الحجز "so that the Guests' preferences are taken care of when the Guest arrives" · Trace Date · **اختيار الإدارات المستهدفة** (إرسال تقارير للإدارات!) |
| 27 | **Guests In-House** | All / **Only Booker** / Today's Arrival only · Room# Wise / Guest Name Wise · **"Include Non CVGR and One Time Guest"** — تعريف حرفي: "Non CVGR are guests who may be FITs or may have come from a company that is **not in contract** with the Property. A **One Time Guest** is a Guest who has visited the property for the first time" |
| — | **Occupancy Report** (غير مرقم) | "Choose report name option from dropdown and select either **Filter or Selection**" + فلاتر: current day arrival, special room, first time, foreign national, company, day use, scanty baggage, title, group · Sort by room/name |
| 28 | **Inhouse List** | **Select the User id from the dropdown list** (من أرحّب؟) · **News Paper Details** · "additional option to print **package rates** based on module attributes" |
| 29 | **Occupancy List – One Line** | ملخص سطر واحد لليوم — "The date will be auto populated. Click Ok." (تقرير بلا معايير!) |
| 30 | **Guest List** | By Name / By Room · **Print All Room / Billing Instruction / Floorwise** |
| 32 | **Wakeup Call List** | "list of all guests who have requested for a Wakeup Call... This also includes **reminders with food requests**" + "view **which user has taken the request**" · التاريخ "≥ current date" · **Skip One Line** |
| 33 | **Newspaper List** | الصحف المحددة عند التسجيل · تاريخ آلي |

## 2. مجموعة Audit Reports (31.1–31.8) — جوهرة التدقيق

التعريف الرسمي: "These are **eight audit reports** relating to the Guest stays, room statuses, transactions room types, etc."

| # | تقرير التدقيق | ما يُرصد | الخصوصية الحرفية |
|---|---|---|---|
| 31.1 | **Amend Guest Stay** | تغيير تواريخ المغادرة | "the list of all guests whose **departure dates have changed**" · Include Special Rooms · اليوم الحالي |
| 31.2 | **Room Status** | حالة الغرف قديم/جديد | "the **old status and the new status** of a particular room or all the rooms" · Room # أو All Rooms · فترة عبر الشهور · القاعدة "> accounting date" |
| 31.3 | **Transfer Folio** | تحويلات الفواتير | "transfer of bill amount at any of the revenue outlets or **allowances (credit note)**" · **All / Transfer Folio / Split Bill** |
| 31.4 | **Room Transfer** | نقل الغرف | "the old and new room numbers from where to where the guest has moved **along with the user's name who has authorized it**" — أثر مخوّل الإجراء! · "≤ accounting date" |
| 31.5 | **Transactions** | كل القيود | **All / By User / By Room / By Rev Code** (اختيار المستخدم من dropdown) |
| 31.6 | **Reopen Folio** | إعادة فتح فوليو | "if the guest folio was closed incorrectly... or if the Guest checked out and **checked in back again on the same date**" · "≤ accounting date and **within the same year and month**" |
| 31.7 | **Room Rate** | تعديل الأسعار | "The report displays the **old room rate and the new room rate**" · **By Room / By User / By Date** · **Inhouse / History** |
| 31.8 | **Change Room Type** | تغيير نوع الغرفة | "Room number 102 was changed from **Standard to Suite**" (المثال الرسمي) · "≤ current date and **within the same Month and Year**" |

**النمط الجوهري**: كل تقرير تدقيقي يقترن بأثر المسؤول (31.4 حرفياً، 31.5 بالخيار) — سلسلة المساءلة التي بدأت في REG/LUK تستمر هنا كطبقة استرجاع جاهزة.

## 3. تصنيفات الضيوف والإقامة (35–50)

| # | التقرير | الخصوصية |
|---|---|---|
| 35 | **VIP List (In House)** | "room wise VIPs list for the day" + arrival/departure/designation/company |
| 36 | **Guest Classification** | قائمة الإشغال بحسب التصنيف (dropdown) لفترة |
| 37 | **Extra Bed Report** | طلبات الأسرة الإضافية اليوم الحالي (تاريخ آلي) |
| 38 | **Extra Bed Report (Past)** | "< accounting date" · فترة عبر الشهور |
| 39 | **Special Guest List** | **Complimentary / Diplomats / House Guest** · **Print Reason**: "The Reason will be printed\displayed, **only if the "Print Reason" option is selected**" · "based on the occupancy for the accounting date" |
| 40 | **Long Staying Guests** | **حقل Stay Days** + Guest Status + **Revenue Details** (checkbox) · فترة قابلة للتعديل عبر الشهور |
| 41 | **Room Instructions Report** | All أو Room # · الموجه إليهم: **Cashier / Night Audit / House Keeping / All** · المثال الحرفي: "Front Office gives instruction to the Cashier '**Collect Rs. 500/- against Transportation**'" · Night Audit يفتح خيار daily أو تاريخ محدد |
| 42 | **Company Guests** | "≤ accounting date" · Walkins أو All · **All / CGR / Non CGR** — "CGR, if you want to view the list of only those Guests who have come from a company that has **a contract** with the Property" |
| 43 | **Company In-House** | بحث **Company Code أو Company Name** (F1) · Include Spl. Rooms |
| 44 | **Group / FIT List** | Selection Criteria: All Rooms/All Groups/Selective Room/Selective Group/**Complimentary Rooms**/House Guest Rooms/Day Use Rooms · Include Special Rooms · Sort · **Rate Options** (قائمة) · **Room Wise Consolidation** · "The summary will be printed **at the end** of the Report" |
| 45 | **Room Upgrade List** | "Room upgrades may happen if the customer requests for a room upgrade **or due to non availability of the reserved rooms**" — تعريف سببي مزدوج |
| 46.1 | **Vacant Rooms** | "clean or dirty... for each room category" + مثال: "total number of clean rooms in the **Standard** category and **Suite** category" |
| 46.2 | **Vacant Room [Feature]** | الحالة + الميزات: "Twin Bed, Double Decker, Arc Design, King size bed" |
| 46.3 | **Current Room Status (D)** | "irrespective of vacant or occupied" · **Dummy / Occupied / Vacant / Dirty** (اختيار متعدد) |
| 47 | **Birthday List** | "This information is taken from the **guest history** screen. Guests' information **has to be linked to the Guest History** at the time of reservation/registration" — تبعية بيانات صريحة · "≥ accounting date" |
| 49 | **In-House Guest By Title** | checkboxes للقاب (Mr./Miss/Mrs...) · **Include Designation** — "The designations are mentioned **below the guests' names**" |

## 4. القرارات المعمارية

1. **قاعدة Dummy Rooms** (46.3/108): "rooms which will not be given to guests, they will be **for demo purposes only**" — عائلة الغرف الوهمية ثالثة الظهور (بعد REG/SYS) وتؤكد Need for Room.is_dummy عند التنفيذ.
2. **CVGR كعقد سعر**: Non-CGR/CGR/One-Time ثلاثية تسويقية (27/42) — تتقاطع مع تعريفات CGR في Rate Master (73) — بعد مرشح Rate Variance.
3. **التدقيق = old/new ثنائية**: 31.2 (حالة) · 31.7 (سعر) — القيمة القديمة تُحفظ دائماً؛ أي تنفيذ حديث يفرض change-log على Room/Rate/Type.
4. **Reopen Folio كحالة يومية**: "checked out and checked in back again **on the same date**" — تقرير التدقيق الوحيد الذي يوثق دورة حياة كاملة (شطب→إعادة فتح) كاستخدام مشروع.
