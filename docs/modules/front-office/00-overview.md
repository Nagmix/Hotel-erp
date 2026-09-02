# 00 — نظرة عامة على وحدة الفندق الأمامي (Front Office)

> **الوحدة المرجعية:** FortuneNext 6i — Front Office Module (FOM)
> **المصادر:** FN6i-NT-FOM-RES / FOM-REG / FOM-CAS / FOM-DEP / FOM-SET / FOM-LUK / FOM-REP / FOM-GST / FOM-HSK / FOM-CRG / FOM-SMS
> **حالة القراءة:** RES ✅ كامل | REG ✅ كامل | CAS ✅ كامل | DEP ✅ كامل | SET (جداول آلية + ص1-15) | البقية: فهارس فقط

---

## 1. حدود الوحدة (Module Boundaries)

وحدة الفندق الأمامي هي **مركز عمليات الفندق** والقلب التشغيلي للنظام بأكمله. تغطي دورة الضيف الكاملة من الحجز حتى المغادرة: إدارة الحجوزات (Reservations)، تسجيل الوصول (Check-in/Registrations)، إشغال الغرف وإدارتها (Room Management)، أعمال الكاشير والفوترة والتسويات (Cashiering)، والمغادرات (Departures)، إضافة إلى خدمات الضيف (Guest Services) والمرافق التشغيلية (الرسائل، المكالمات التنبيهية، الشكاوى، SMS، الهاتف).

**ما تفعله الوحدة:**
- دورة الضيف: حجز → تخصيص غرفة → تسجيل وصول → ترحيل شحنات → فوترة → تسوية → مغادرة → إعادة فتح/إلغاء.
- إدارة حالة الغرف: Room Rack (Occupied/Reserved/Vacant/Dirty/OOO/OOS) وانتقالات الحالة.
- البنية المالية للضيف: Folio (فاتورة حية) + التسويات بأنماطها التسعة + الودائع/المستردات.

**ما لا تفعله الوحدة (حدود صريحة موثقة):**
- **لا تنتج القيود المحاسبية النهائية** — الترحيل إلى Financial Management يتم عبر روابط الترحيل الموثقة في FAS-SET (انظر `11-accounting-impact.md`).
- **لا تدير مطاعم/نقاط البيع** — فواصل POS تُرحَّل إلى فوليو الضيف (FOM-CAS ص4: "If you are using IDS POS module, Restaurant bill will be posted for POS module").
- **لا تدين حسابات الشركات** — التسويات الائتمانية تُحوَّل تلقائياً إلى Accounts Receivables (FOM-CAS ص69).

---

## 2. الوحدات الفرعية (Sub-modules) وشاشاتها

### 2.1 الحجوزات (Reservations) — FOM-RES

| # | الوظيفة | الوصف الوظيفي | المصدر |
|---|---|---|---|
| 1 | Room Booking (Quick Reservation) | حجز سريع بمعلومات دنيا + توسيع لاحق عبر Amend | RES §1 (ص3-37) |
| 1.1 | Add a new reservation | حجز جديد: تواريخ ذكية + Property + Company + Booker + Room Type + Mode + Rate Info | RES §1.1 |
| 1.2 | Amend existing information | تعديل حجز قائم + إثراء ملف الضيف (Guest Info, Pickup/Drop, Privilege/Credit Card, Passport/Visa, Vehicle, Likes/Dislikes, Trace, Guest Note, Documents, Extra Charges, Revenue Discount) | RES §1.2 (ص14-27) |
| 1.3 | Cancel a Reservation | إلغاء + سبب + معتمد + تفاصيل المتصل + رد الودائع | RES §1.3 (ص37-40) |
| 1.4 | Inquire about Reservation | استعلام للقراءة فقط (لا حفظ) | RES §1.4 (ص40-41) |
| 1.5 | Assign a Room to the guest | تخصيص غرفة (Interconnected/Features/Release) | RES §1.5 (ص41-45) |
| 1.6 | Copy Reservation | نسخ حجز مشابه | RES §1.6 (ص45-46) |
| 1.7 | Re-Instate Cancel | إعادة تفعيل ملغى — **برقم حجز جديد** | RES §1.7 (ص46-47) |
| 1.8 | Re-Instate "No Show" | إعادة تفعيل No-Show (يُوسم بعد Night Audit) | RES §1.8 (ص47-48) |
| 1.9 | Hotel Profile | عرض ملف الفندق | RES §1.9 |
| 2 | Room Type Booking | شبكة توفر شهرية + حجز بالسحب على التواريخ + Detailed Position | RES §2 (ص49-51) |
| 3 | Room Rack Console | لوحة الغرف: حجز/بلوك/Check-in/Checkout/Transfer/Swap + OOO/OOS + Information Tips | RES §3 (ص51-61) |
| 4 | Reserved Guest Messages | رسائل لضيف محجوز له | RES §4 (ص61-62) |
| 5 | Assign Guest Rooms | تخصيص غرف للحجوزات + عرض المميزات | RES §5 (ص62-67) |
| 6 | Retentions-Cancel/No Show | رسوم الاحتجاز للإلغاء/عدم الحضور | RES §6 (ص67-68) |
| 7 | Close Room Inventory | إغلاق المخزون ليوم/نوع غرفة (حرف C) — walk-ins مسموحة | RES §7 (ص68) |

### 2.2 التسجيلات (Registrations) — FOM-REG

| # | الوظيفة | الوصف الوظيفي | المصدر |
|---|---|---|---|
| 1 | Express Check In | check-in سريع لمن لديه حجز مع غرف مخصصة مسبقاً + فلاتر (VIP/F9-Note/F10-Doc/Messages/Partial/Repeat) + Current Status + Hotel Position (Hourly/Detailed/Yearly/Graphs) | REG §1 (ص3-13) |
| 2 | Reservation Check In | check-in للحجوزات بمعايير بحث + Color Legends (green=frequent, peach=waitlist, purple=checked-in) | REG §2 (ص13-16) |
| 3 | Walk-ins (Express/Walk-in) | check-in بلا حجز: مبسط (غرفة+اسم+مغادرة) أو كامل (عنوان، جواز، شركة، Bill Inst، Pay Mode، Plan Code، Scanty Baggage، Vehicle، Revenue Discount، Special Instruction، Local Add، Others) | REG §3 (ص16-33) |
| 4 | Special Rooms Check-in | check-in ضيوف/قادة مجموعات إلى غرف خاصة + G-FOLIO للمجموعات | REG §4 (ص33-37) |
| 5 | Room Floor Plan Display | خريطة طوابق ملوّنة + Room Transfer من الخريطة | REG §5 (ص37-39) |
| 6 | Guest Management | إحصاءات Live للضيوف المقيمين: Change Guest Info (History/Change Tariff/Pax Details/Rate/Discount) + Room Transfer/Swap + Amend Stay + Credit Limit | REG §6 (ص39-55) |
| 7 | Guest Services | Messages/Locator/Likes-Dislikes/Wakeup Calls (فردي أو جماعي)/Log-Attend-Browse Complaints | REG §7 (ص55-66) |
| 8 | Guest Photo (In-House) | صورة الضيف المقيم → تُرحَّل لـ Guest History إذا Post History = Y | REG §8 (ص66-67) |
| 9 | Invoice By Arrival | فواتير وصول حجوزات وكلاء السفر (Add/Modify/Cancel/Print + Break Up + Ad hoc Charges + Control Report) | REG §9 (ص67-80) |
| 10 | Mask Guests | إخفاء حضور ضيف (VIP) من العام | REG §10 (ص80-81) |
| 11 | Turn Away / Walkout Guest | تسجيل الرفض (→ Denial Report) | REG §11 (ص81-82) |
| 12 | Room Instruction | تعليمات الغرفة: Cashier/Night Audit/Housekeeping — تظهر عند Night Audit | REG §12 (ص82-84) |
| 13 | Change Rate | تغيير التعرفة: Company/Currency/Classification/Checkout/Plan/Rate Type + Pax Details | REG §13 (ص84-86) |
| 14 | Hurdle Rate | تعرفة يومية محددة من تاريخ محاسبي، بإدخال Month/Year | REG §14 (ص86-87) |
| 15 | Group Rate Updation | خصم/خطة للمجموعات (Discount% + Change Plan All) | REG §15 (ص87-88) |
| 16 | Stop Charges Posting | حظر ترحيل شحنات لضيف مقيم حسب Revenue Code (Select All متاح) | REG §16 (ص88-89) |
| 17 | Link Room to Groups | ربط غرف أفراد بمجموعة | REG §17 (ص89-91) |
| 18 | Delink Rooms | فصل غرفة عن مجموعة (أيقونة قائد المجموعة) | REG §18 (ص91-93) |
| 19 | Cancel Check-Ins | إلغاء check-in منجز + سبب + معتمد | REG §19 (ص93-94) |
| 20 | Link FIT Rooms as Groups | ربط غرف أفراد متأخرين بمجموعة | REG §20 (ص94-95) |
| 21 | Group Billing Instruction | توجيه فواتير أعضاء المجموعة لفوليو القائد (Direct vs Company حسب الـ Outlet) | REG §21 (ص95-96) |
| 22 | Daywise Over Booking | نمط overbooking يومي حسب نوع الغرفة بحد أقصى | REG §22 (ص96-97) |
| 23 | Create Hotel Chart | نشاط خلفي: Hotel Chart أو Agent Chart — بتحقق username/password | REG §23 (ص97-98) |
| 24 | Billing Broadcast | بث تعليمات/عروض للمنافذ لفترة — تظهر متscrolling عند الفوترة (تعديل المستقبلي فقط) | REG §24 (ص98-100) |
| 25 | Extension Password Setup | كلمة مرور رقمية لتمديد غرفة/قسم — صالحة حتى checkout (غرفة متعددة الضيوف → Reg# لكل ضيف) | REG §25 (ص100-102) |
| 26 | Activate-Deactivate Extension | تفعيل/تعطيل Local/STD/IDD عبر two-way link يتفاعل مع check-in/checkout | REG §26 (ص102) |
| 27 | Adhoc SMS Message | رسالة لمجموعة/غرفة/Check-Out guests + Message to All | REG §27 (ص102-105) |
| 28 | SMS Status | حالة الرسائل real-time (Bookings/Check-ins/Complaints/Room Transfers/Birthdays/Checkouts) + Refresh | REG §28 (ص105) |

### 2.3 أعمال الكاشير (Cashiering) — FOM-CAS

| # | الوظيفة | الوصف الوظيفي | المصدر |
|---|---|---|---|
| 1 | Posting | الشاشة الأم: كل الغرف المشغولة + معاملاتها. تشمل: Post Charges / Deposits (Guests، Rsvn، City Ledger) / Paid Outs (Rooms، City Ledger) / Miscellaneous Charges / Room Rate (Individual، All Rooms) / Additional Room Rate (Rate/Plan/Extra Bed/Retention) / Bill Allowance / Consolidated Allowance / Check Out | CAS §1 (ص2-38) |
| 2 | Post Extra Charges | شحنات إضافية بالسعة (Adult/Child) لجميع أيام البقاء حتى المغادرة | CAS §2 (ص43-46) |
| 3 | Tag Deposits to Rooms | ربط الودائع المدفوعة عند الحجز/الوصول بالغرف | CAS §3 (ص46) |
| 4 | Fixed Charge Posting | شحنة محددة ليوم محاسبي لـ revenue محدد (لا تكرار لنفس revenue+guest في نفس اليوم) | CAS §4 (ص46-49) |
| 5 | Split Front Desk Charges | تقسيم شحنات (يدوي بمبلغ أو آلي بعدد سجلات) | CAS §5 (ص49-53) |
| 6 | Split F & B Charges | تقسيم فواصل F&B حسب نوع القائمة (Food/Liquor/Soft Drinks/Tobacco/Others) + Tips + Round Off | CAS §6 (ص53-56) |
| 7 | Split Folios | فصل فواتير متعددي الإشغال بنفس الغرفة — **يتطلب Pax > 1** | CAS §7 (ص56-59) |
| 8 | Transfer Folios | نقل فاتورة غرفة إلى أخرى (Selective/All Transactions) + تفويض | CAS §8 (ص59-61) |
| 9 | Link and Delink Rooms | ربط غرف لفاتورة واحدة (تسهيل checkout) وفصلها | CAS §9 (ص61-65) |
| 10 | Confirm Checkouts | تعديل وقت المغادرة لتجاوز اليوم | CAS §10 (ص65-66) |
| 11 | Pax Checkout | checkout ضيوف إضافيين (وليس الرئيسي) | CAS §11 (ص66-68) |
| 12 | Check out | قائمة مغادري اليوم (Company/Group/Room Type/Floor) | CAS §12 (ص68-69) |
| 13 | Settlements | تسوية الفواتير المطبوعة: 9 أنماط + جزئي + Multi-settlement + Tip + إبقاء الإشغال + Receipt Print + Foreign Exchange Entry + Resettlement | CAS §13 (ص69-80) |
| 14 | Folio Re-Instate | إعادة فتح فوليو مغادِر — **قبل Night Audit فقط؛ الرئيسية قبل المرتبطة** | CAS §14 (ص80-82) |
| 15 | Release Stop Posting | فتح الفوليو بعد طباعة الفاتورة (يعتمد على FO Module Attribute 16) | CAS §15 (ص82-83) |
| 16 | Deposit Refund | رد الودائع: Refund Amount أو Retention Charges (Cash/Credit Card/Cheque) | CAS §16 (ص83-86) |
| 17 | Foreign Exchange Entry | تسجيل صرف عملات: فئات البنكنوت + عمولة + ضريبة | CAS §17 (ص86-89) |
| 18 | Credit Card Encashment | صرف نقدي من بطاقة الضيف + عمولة فندقية % | CAS §18 (ص89-91) |
| 19 | Tag Agent Commission | وسم فواتير الوكلاء المسددة + Retrieve Tag Entries | CAS §19 (ص91-93) |
| 20 | Pax Transfer | نقل pax/cover بين الغرف + تفويض | CAS §20 (ص93-95) |

### 2.4 المغادرات (Departures) — FOM-DEP

وُثّقت كاملة في الجلسة 1 (14 وظيفة): Checkout، Departure Register، Departure Snaps، Rollaway Bed، Auto Bed Turn، وغيرها. انظر `04-workflows.md` §4.

---

## 3. مستخدمو الوحدة (من `docs/domain/hotel-roles.md`)

Front Office Manager / Front Office Assistant / Night Auditor / Reservation Clerk / Bell Captain / Guest Relation Executive (وأدوار الوحدات المتقاطعة: Cashier).

---

## 4. التفاعلات المعروفة مع الوحدات الأخرى (Cross-Module Touchpoints)

| التفاعل | الوحدة الطرف | الاتجاه | المصدر |
|---|---|---|---|
| فواصل المطاعم تُرحَّل لفوليو الضيف | Point of Sale | POS → FO | FOM-CAS ص4 |
| كل التسويات الائتمانية تُحوَّل تلقائياً | Accounts Receivables | FO → AR | FOM-CAS ص69 |
| ترحيل إيرادات FO إلى دفتر الأستاذ | Financial Management | FO → FAS | FAS-SET (رابط 1) — انظر `document-map.md` |
| تعليمات غرف تظهر عند Night Audit | (داخلي Night Audit) | REG → Night Audit | FOM-REG ص82-84 |
| تفعيل/تعطيل التمديدات الهاتفية عند check-in/checkout | Telephones | FO ↔ TEL | FOM-REG ص102 |
| صور الضيوف → Guest History | (داخلي + GST) | REG → History | FOM-REG ص66-67 |
| Room Blocks (OOO/OOS) تشارك مع Housekeeping/Maintenance | HSK/MNT | RES ↔ HSK | FOM-RES ص54-56 |

> **قاعدة التوثيق:** كل بند أعلاه مذكور بمصدره. ما لم يوثَّق يوسم `[NOT DOCUMENTED]` أو `[PENDING DEEP READ]`.

---

## 5. المفاهيم الجوهرية المكتشفة (Key Domain Concepts)

1. **التاريخ المحاسبي (Accounting Date / Business Date):** العمليات (check-in، transfer/swap، ترحيل الشحنات) لا تجري إلا في التاريخ المحاسبي الحالي — حركة الغرفة/الضيف مقيدة به زمنياً. (FOM-RES ص58/60، FOM-CAS ص20)
2. **الفوليو (Folio):** كيان مالي حي لكل تسجيل؛ يُقسَّم (Split)، يُنقل (Transfer)، يُربط (Link)، ويُجمَّد بعد طباعة الفاتورة ما لم يُفك عبر Release Stop Posting.
3. **دورة Night Audit:** Post Tariff → Guest Balance → Night Balance → Open New Date — تحكم دورة حياة اليوم المحاسبي بالكامل (موثقة في FOM-DEP).
4. **أنماط التسوية التسعة:** Cash / Credit Card / Companies / Staff / Bill on Hold / Foreign Exchange / Complimentary / Cheque + Multi-settlement — التسوية يجب أن تتطابق (tally) وإلا رفض النظام.
5. **الفوليو الافتتاحي والتجميد:** طباعة فاتورة FO توقف الترحيل على الفوليو (Attribute 16)، وإعادة الفتح (Release) عملية مصرّح بها.
6. **الإصدارية في البيانات:** Reservation → Check-in → Folio → Settlement سلسلة مستندات مترابطة، كل مرحلة تولّد أرقامها (Reservation # / Reg # / Folio # / Bill # / Receipt #).
