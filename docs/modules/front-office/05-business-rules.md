# 05 — قواعد العمل (Business Rules) — وحدة Front Office

> **قاعدة التوثيق:** كل قاعدة مصدرها (ملف/صفحة). القواعد المستنتَجة توسم `[INFERENCE]`.

---

## BR-FO-01: قيود التاريخ المحاسبي (Accounting Date Constraints)

| القاعدة | المصدر |
|---|---|
| Check-in لا يجري إلا في التاريخ المحاسبي الحالي | FOM-RES ص58 |
| نقل/تبديل الغرف لا يجري إلا في التاريخ المحاسبي الحالي | FOM-RES ص60 |
| تعديل تعرفة الأيام **المستقبلية فقط** — الماضي مرفوض برسالة خطأ | FOM-REG ص47 |
| No-Show يوسم بعد اكتمال Night Audit لتاريخ الوصول | FOM-RES ص47-48 |
| Folio Re-Instate متاح **قبل Night Audit فقط** | FOM-CAS ص80 |
| حظر الترحيل أثناء Guest Balance إلا للتاريخ التالي (Night Audit) | FOM-DEP (الجلسة 1) |

## BR-FO-02: قواعد الحجز (Reservations)

| القاعدة | المصدر |
|---|---|
| مجموع غرف Room Details يجب أن يساوي حقل Rooms في الشاشة الرئيسية | FOM-RES ص6 |
| Duplicate reservation detection → تنبيه قبل الحفظ | FOM-RES ص8 |
| أسماء مشابهة في Guest History → Guest Profile screen قبل الحفظ | FOM-RES ص8 |
| Re-Instate Cancel → **رقم حجز جديد**؛ القديم الملغى لا يُستعاد | FOM-RES ص47 |
| Close Room Inventory (C) يمنع الحجز لليوم/النوع — **walk-ins مسموحة** | FOM-RES ص68 |
| الاحتفاظ (Retention) عند الإلغاء/No-Show يُدخل يدوياً لكل ضيف (Charge Amt) | FOM-RES ص67-68 |
| Add يتطلب ضيفاً واحداً على الأقل قبل إضافة سجلات بتواريخ/أنواع مختلفة تحت رقم واحد | FOM-RES ص27-28 |

## BR-FO-03: قواعد التسجيل (Check-in)

| القاعدة | المصدر |
|---|---|
| Express Check-in يعرض غرف النوع المحجوز **المتاحة فقط** | FOM-REG ص7 |
| Walk-ins: تُعرض Vacant افتراضياً + **OOO معروضة لمنع check-in عليها** | FOM-REG ص17 |
| تخصيص غرفة معلمة للصيانة → تنبيه Alert | FOM-REG ص33 |
| Extension Password: **رقمية فقط** + صالحة حتى checkout + لكل Reg# في الغرف المتعددة | FOM-REG ص100-102 |
| تفعيل/تعطيل Extension: عبر two-way link يتبع check-in/checkout (Local/STD/IDD) | FOM-REG ص102 |
| Guest Photo: الاستبدال يسأل أولاً (Yes/No)؛ يُرحَّل للتاريخ إذا Post History=Y | FOM-REG ص66-67 |
| Cancel Check-In: يتطلب سبباً + تفويضاً (Reason Entry) | FOM-REG ص93-94 |

## BR-FO-04: قواعد الغرف والمجموعات

| القاعدة | المصدر |
|---|---|
| OOO: يتطلب Description + Reason (قائمة معرفة) + Department؛ From/To **غير قابلين للتحرير** | FOM-RES ص54 |
| OOS: يتطلب Description فقط؛ From/To غير قابلين للتحرير | FOM-RES ص55 |
| Group Billing Instruction: التوجيه **Direct أو Company** حسب الـ Outlet — مثال موثق: F&B → القائد (Company) والباقي Direct للأعضاء | FOM-REG ص95-96 |
| Group icon يميز قائد المجموعة | FOM-REG ص93 |
| Daywise Over Booking: يسمح بـ overbooking حتى حد لكل نوع/يوم | FOM-REG ص96-97 |
| Create Hotel Chart: **يتطلب username/password صالحين**؛ نشاط خلفي (Hotel Chart من Reservations+Registrations+Room Blocks، Agent Chart من Allocations+Blocks) | FOM-REG ص97-98 |

## BR-FO-05: قواعد الترحيل والفوترة (Posting)

| القاعدة | المصدر |
|---|---|
| Room Rate يرحّل **شحنة واحدة** للغرفة؛ التنفيذ المتكرر يسجل الأخير فقط → للتعدد Additional Room Rate | FOM-CAS ص22-23 |
| Day Charge عند ترحيل التعرفة: **1 أو 0.5** فقط (نصف يوم) | FOM-CAS ص21 |
| ترحيل All Rooms يُنفَّذ عادة عند Night Audit | FOM-CAS ص22 |
| Fixed Charge Posting: **يمنع تكرار نفس revenue+guest في نفس اليوم المحاسبي** | FOM-CAS ص46 |
| Bill Allowance: From/To **ضمن مدى Arrival↔Departure** | FOM-CAS ص26 + ص29 |
| Bill/Consolidated Allowance: يتطلب Reason + Remarks + Authorized By | FOM-CAS ص28 + ص33 |
| Allowance على الضريبة: Yes/No/**Exempt** | FOM-CAS ص27 |
| بنية الضريبة في Consolidated Allowance تتبع الوصف (luxury/service/VAT) | FOM-CAS ص33 |
| Miscellaneous Charges: **لغير المقيمين فقط** | FOM-CAS ص19 |
| Print Bill يوقف الترحيل على الفوليو (إذا Attribute 16=Yes) → يُفك عبر Release Stop Posting | FOM-CAS ص82-83 |
| Prov Bill: بلا رقم فاتورة وغير قابل للتسوية — للعرض فقط | FOM-CAS ص37 |

## BR-FO-06: قواعد التقسيم/النقل/الربط

| القاعدة | المصدر |
|---|---|
| Split Folios يتطلب **Pax > 1** | FOM-CAS ص57 |
| Split F&B حسب أنواع القائمة: Food/Liquor/Soft Drinks/Tobacco/Others + Tips + Round Off | FOM-CAS ص55 |
| Transfer Folios: Selective (لكل معاملة Tag) أو All + **تفويض إلزامي** | FOM-CAS ص59-61 |
| Link Rooms هدفه فاتورة واحدة لغرف متعددة (تسهيل checkout) | FOM-CAS ص61 |
| Delink يبدأ من **Main Room** | FOM-CAS ص65 |

## BR-FO-07: قواعد التسوية (Settlements)

| القاعدة | المصدر |
|---|---|
| التسوية يجب أن **تتطابق (tally)** — وإلا رسالة رفض | FOM-CAS ص77-78 |
| تسوية جزئية متاحة + **Multi-settlement لنفس الفاتورة** | FOM-CAS ص69 + ص78 |
| 9 أنماط: Cash / Credit Card / Companies / Staff / Bill on Hold / Foreign Exchange / Complimentary / Cheque (+Multi) | FOM-CAS §13 |
| **كل التسويات الائتمانية تُحوَّل تلقائياً إلى Accounts Receivables** | FOM-CAS ص69 |
| إمكانية الاحتفاظ بالضيف **مشغولاً بعد التسوية** | FOM-CAS ص69 |
| Tip Amount متاح في أنماط Cash/Forex/Complimentary/Cheque | FOM-CAS §13 |
| Credit Card: Authorization # تلقائي من portal عند السحب — **غير إلزامي** | FOM-CAS ص12 |
| Resettlement لفاتورة مسواة متاح (بنمط مختلف) | FOM-CAS ص79-80 |
| لكل تسوية Receipt يولَّد + قابل للطباعة | FOM-CAS ص78 |
| Clear Room# behavior مرتبط بـ **INI Switch 64** | FOM-CAS ص78 |

## BR-FO-08: قواعد المخارج النقدية والصرف

| القاعدة | المصدر |
|---|---|
| Paid Outs: للضيوف (Rooms) أو لغيرهم (City Ledger) + سبب من قائمة معرفة + Voucher# | FOM-CAS §Paid Outs |
| Paid Outs يدعم متعدد العملات **لكل معاملة** (بعد Advance/Post Charge...) | FOM-CAS ص19 |
| Foreign Exchange Entry: Voucher# تلقائي أو يدوي حسب **INI Switch** + تسجيل فئات البنكنوت (Quantity/Description/Denomination/Amount/Local) + العمولة تُخصم → Net | FOM-CAS §17 |
| Credit Card Encashment: رقم Encashment **تلقائي** + Less Commission % | FOM-CAS §18 |
| Tag Agent Commission: الفواتير المسواة تُوسم Yes → تختفي من قائمة الدفع (لون مختلف) + Retrieve | FOM-CAS §19 |

## BR-FO-09: قواعد خدمات الضيف والاتصالات

| القاعدة | المصدر |
|---|---|
| تعليمات Cashier/Housekeeping تظهر **pop-out وقت Night Audit** | FOM-REG ص84 |
| تعليمات Night Audit: يومية أو بتاريخ محدد | FOM-REG ص83 |
| Billing Broadcast: تظهر scrolling عند الفوترة في المنافذ + **التعديل للمستقبلي فقط** | FOM-REG ص99-100 |
| Wakeup Call: Room أو Extension + جماعي (Group) + Reminder اختياري | FOM-REG §7 |
| Inquire Reservation: قراءة فقط — **لا حفظ** | FOM-RES ص41 |

## BR-FO-10: قواعد تتبع التغييرات والمراجعة

| القاعدة | المصدر |
|---|---|
| Audit (الحجز): يعرض القديم/الجديد + المستخدم + الوقت لخمسة أبعاد (Reservation/Change Room/Room Rate/Amend Stay/Occupancy) | FOM-RES §Audit (ص29-30) |
| كل عمليات النقل/التبديل/الإلغاء/الخصم تتطلب تفويضاً (Authorized By) موثقاً | موثق في مواضع متعددة (REG + CAS) |
| Room Floor Plan: الألوان تعبر عن الحالة (الأحمر = مشغولة) | FOM-REG ص38 |

---

## قواعد سلوك النظام الملازمة (System Behavior Rules)

- **Color Coding الموثق:** حجز waitlist=peach، frequent check-in=green، checked-in=purple (REG ص15)؛ تخصيص غرفة=أزرق (RES ص11)؛ Masked guest=أحمر (REG ص80)؛ الغرفة المحظورة تظهر بلون مختلف (RES ص17).
- **قيم Yes/No:** سلوكيات كثيرة مفاتيح تبديل (Print Voucher، Assign Rooms، Deposits، Send SMS، Post History، Scanty Baggage، Card Use Amount، Additional tariffs، Room Count، Print in Voucher، Require Reminder...).
- **INI Switches المتأثرة بوحدة FO الموثقة حتى الآن:** 64 (Clear Room# بعد التسوية)؛ Voucher# تلقائي/يدوي في Foreex. — `[PENDING]` جرد كامل من FOM-SET/SYS-SSP.
- **FO Module Attribute 16:** "Posting to be stopped once the bill is printed" يفعّل Release Stop Posting. — `[PENDING]` جرد بقية الـ Attributes من FOM-SET.
