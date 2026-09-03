# 02 — عائلة الحجوزات والوصول (REP §1–23 + Cancellation/No Shows)

> بنود 1–23: من Operational Report إلى بطاقات التسجيل + Cancellation/No Shows الختامية. ~24 تقريراً تُغطي دورة الحجز كاملة قبل وبعد الوصول.

---

## 1. تقارير دورة الحجز (1–11)

| # | التقرير | المعايير والخصوصية الموثقة |
|---|---|---|
| 1 | **Operational Report** | الخيارات: **All / Reservations / Day Use / Amendments / Cancellation** · نطاق تاريخ (To > From) · Amendments: **All Records أو Latest Records** ("view all amended records or only the latest amended records") · checkbox **Include Special Room** |
| 2 | **Amend/Cancel by Arrival** | "highlights any amendments or cancellations made to the reservations, **on the date of arrival**" · خيارات Amendments/Cancellations/**Both** |
| 3 | **Reservation Advance List** | المبالغ المدفوعة مقدماً **للتاريخ الحالي** — "The date will be displayed by default" (تاريخ آلي بلا مدخل) |
| 4 | **Re-Confirm Bookings** | تعريف **Cut Off date** ("the date when the Property calls the customer to confirm their reservation") · الأساس: **Reservation Date أو Arrival Date** · تاريخ إعادة التأكيد "≥ the accounting date" · **Show Prior Cutoff** + Save **أو** Print |
| 5 | **No Shows** | "the revenue that has to be generated for that day/stay period" — **حساب إيراد ضائع**: خيار **A Day أو Stay Period** · Property |
| 6 | **Reservation Guest Message Print** | رسائل ضيوف الحجوزات لتاريخ + **نطاق Res# (من/إلى)** · **Display → Notepad** أو Print · يتطلب Program ID + User Defined Print Forms (SYS+FO Setup) |
| 8 | **Print Voucher** | Based On: **Reservations / Cancellation** · مرشح: **Res# / Mem. ID / Arrival Date** — قاعدة حرفية: "IF you select Cancellations, then you will have to filter the data by **Reservation # only. The other two options... will be disabled**" · نافذة تأكيد + **Print أو Email** (القناة البريدية الوحيدة!) |
| 9 | **Reprint Voucher** | إعادة طباعة قسائم أُنشئت ولم تُطبع · التاريخ "≤ current date" |
| 10 | **Agent Booking Report** | حجوزات وإلغاءات الوكلاء لفترة ("can be across months and years") · F1 Company · **Conf/Wait/Incl. Cancel** |
| 11 | **Denial Report** | "customers who had reserved/booked the rooms but later cancelled... Such customers are called as **Turn Away Guests**" — تعريف موسعي للسوق المفقود |

**ملاحظة تحليلية**: العائلة تحتوي أقدم ذكر لمفهومين revenue-management مبكرين: (أ) **إيراد الـNo Show المحسوب** لفترة الإقامة كاملة، و(ب) **Turn Away Guests** كفئة سوقية — كلاهما مدخلات حتمية لأي reproduction حديث.

## 2. تقارير الوصول (12–23)

| # | التقرير | المعايير والخصوصية الموثقة |
|---|---|---|
| 12 | **Expected Arrivals (80)** | **قاعدة تاريخ صريحة: "The date range entered should be a future date only because we are generating the report for expected arrivals"** · مرشحات: All Reservations / By Foreign Nationals / By Classifications / By Guest Status · **One Line Format و/أو FIT/Group Break Up** · Sort: Guest Name/Res# · **Include W/S Bookings** (قائمة الانتظار) · مرشح Bookers/Provisional |
| 13 | **Expected Arrivals (132)** | نفس 12 بصيغة 132 عموداً + **Print Likes/Dislikes** + **Print Guest Status Summary** + "Arrivals with **Booker Information Only**" |
| 14 | **Today's Arrivals** | التاريخ = accounting date آلياً · مصادر الوصول (6): **All / Reservation Checkins / Walkins / Express Walkins / Group Checkins / Group Fast Checkins** · عرض: **Room wise / Time wise / Company Wise** |
| 15 | **Arrival Register** | سجل يومي "with **statutory information** about all guests... also gives the **PAX details**" · **Details/Summary** (Summary بلا PAX) · **Pax Details** متاح فقط مع Details — "The number of guests in each room" |
| 16 | **Arrivals for the Day** | "All the check-ins with Guest and PAX details as on a given date" · القاعدة: التاريخ "< the accounting date" (سجلي) |
| 17 | **GH Arrivals List** | ضيوف متكررون من **Guest History** ("tagged as Repeat Guests in Guest History") · القاعدة: "> the accounting date" · All Arrivals checkbox · Property/Unit |
| 18 | **Group Arrivals** | "Arrival details of Guests who checkin as special Groups... also displays the **Company details and the billing instructions**" · F1 Group Code · Summary/Details (تفاصيل: Guest name/Nationality/status/classification) · **Sort Sequence: Res No. / Arrival Date / Group / Company** |
| 20 | **Guest Pickup/Drop Report** | "to ensure pickup and drop facility is provided" · Expected **Arrivals أو Departures** · التاريخ "≥ accounting date" · F1 Group · Room Type Sort · **Print Info. If Pk/Dp. Is YES** (طباعة معلومات النقل فقط عند التأكيد!) |
| 21 | **Registration Card** | طباعة لضيوف يوم محدد · F1/double-click Res# · "The option **Setup is used to define and save the print formats for FIT and Group** Reservations" |
| 22 | **Pre – Registration Card** | **Copies field** (عدد النسخ!) · Start/End Res · Enter-to-move-cursor موثقة |
| — | **Guest Reg. Card** (غير مرقم) | مدخل **Room#** (F1/Help) → تعبئة آلية لبيانات الضيف → Print |
| 23 | **Security** | مجمّع فرعي — انظر `03-security-statutory-reports.md` |

## 3. Cancellation / No Shows (ختام المتن — غير مرقّم في التسلسل)

نفس فلسفة No Shows (5) لكن بخيار صريح: "Select either **Cancellation or No Show** option for display" — تقرير ثنائي الوضع يفصل الفقد إلى: ملغى (ألغى بنفسه) vs لا-show (لم يحضر).

## 4. الأنماط العابرة في هذه العائلة

1. **ثلاثية قواعد التواريخ الموجهة بالزمن**: future-only (12/13) · past-only (16) · future-strict (17 ">") — التقرير يعرف "اتجاه الزمن" من طبيعته (توقع/سجل) ويفرضه على المدخل.
2. **F1 كمعيار استرجاع موحد** في Company/Group/Res# — مع نص متكرر حرفياً: "press F1 on the keyboard **to get the ... list**".
3. **قفل مرشح حسب Based On** (8): اختيار Cancellation يقفل كل المرشحات إلا Res# — أول XOR معلن في REP (يليه 104/102).
4. **PAX كبعد إحصائي أول** — يظهر في 15/16/52/65/99/115 — وليس مجرد عدد أشخاص.
5. **الإقران التشغيلي**: 12/13 زوج 80/132 (نفس التقرير بصفي ورق مختلف) — نمط يظهر لاحقاً في 102 (Night Report).
