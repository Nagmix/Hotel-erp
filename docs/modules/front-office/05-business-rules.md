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
- **INI Switches المتأثرة بوحدة FO الموثقة:** 64 (Clear Room# بعد التسوية)؛ Voucher# تلقائي/يدوي في Foreex؛ **INI 58 = 0 لتفعيل Reservation Mode (FOM-SET ص1544)**. — جرد INI الكامل في SYS-SSP [مرحلة لاحقة].
- **FO Module Attribute 16:** "Posting to be stopped once the bill is printed" يفعّل Release Stop Posting. — بقية الـ Attributes في SYS-SSP [مرحلة لاحقة].

## BR-FO-11: قواعد هندسة التعرفة (Rate Architecture) — الجلسة 3

| القاعدة | المصدر |
|---|---|
| **مجموع نسب Package Elements = 100% حصراً** عبر كل عناصر الحزمة | FOM-SET §3 ص13 |
| **هياكل ضريبية منفصلة إلزامية** لكل من: Tariff، Extra Bed، Plan | FOM-SET §6 ص21 Note |
| ضريبة On Tax تتطلب رقم الضريبة المرجعية (تسلسل ضمن الهيكل) | FOM-SET §6 ص21 |
| ضريبة Pax مع Consolidate تتطلب Revenue Code + Rate Selection (Rack/Charged/High/Low) | FOM-SET §6 ص21 |
| **نسخية تعرفة زمنية:** زيادة To date فقط إذا > تاريخ المحاسبة؛ التخفيض حتى تاريخ المحاسبة ثم إغلاق وإعادة إنشاء من الغد | FOM-SET §7 ص29-30 Note |
| Rate grid: أسعار مختلفة **لكل يوم من أيام الأسبوع** × نوع الغرفة × الإشغال (S/D/T/Q) + Extra Adult/Child + هيكل ضريبة لكل خلية | FOM-SET §7 ص28 |
| Package Amount يُفكّك إلزامياً عبر أعمدة Tariff/Plan/Services | FOM-SET §7 ص24-26 |

## BR-FO-12: قواعد تسوية المنافذ والفوترة

| القاعدة | المصدر |
|---|---|
| **النقد إلزامي لكل منفذ:** "bill settlement by cash is a mandatory mode of settlement and not optional for any of the outlets" | FOM-SET §26 ص70 |
| الكاشير لا يقبل إلا أنماط التسوية المعرفة للمنفذ المحدد | FOM-SET §26 ص70 |
| Billing Instruction Type: Direct أو Company فقط — وبدون Revenue Codes يفترض فاتورة واحدة | FOM-SET §25 ص68 |

## BR-FO-13: قواعد التغيير الهيكلي والتنقية

| القاعدة | المصدر |
|---|---|
| تغيير نوع غرفة: **Vacant فقط** (لا Occupied/Blocked/Dirty) + خروج مستخدمي FO + Create Hotel Chart بعده | FOM-SET §8 ص33 Note |
| **Group code آلي إذا عدد حجوزات الغرفة ≥ Group Count** (Room Type) | FOM-SET §1 ص8 |
| Purge Reservations: 60-365 يوماً | FOM-SET §64 ص140-141 |
| Purge FO Transactions: ≥60 (Audit Tariff أو FO Transactions) | FOM-SET §65 |
| Purge Guest Ledger: ≥120 **وبعد معالجة كل تقارير GL/Room History** | FOM-SET §66 ص142 |
| **مصفوفة التعديل:** لكل Master حقول تعديل محددة نصاً (48 قاعدة Note) — ما عداها نسخة جديدة بتاريخ مستقبلي | FOM-SET Notes (§1-§67) |

## BR-FO-14: قواعد خدمات الكونسيرج والغسيل والمفقودات

| القاعدة | المصدر |
|---|---|
| سجلات الكونسيرج (أمتعة/طرود/تذاكر/سيارات): التسليم/الاستلام = إبراز **peach** | FOM-CRG ص2-15 |
| طبع قسيمة الكونسيرج يتطلب قالباً معرفاً في **User Defined Reports (SYS)** — وإلا خطأ "Category does not exist" | FOM-CRG ص6/ص19 |
| Ticket Request: بدون رسوم (No) → حقل Amount **معطّل** | FOM-CRG ص9-10 |
| Baggage: F5 حذف، F2 تفعيل passive (الاسم السلبي لا يظهر) | FOM-CRG ص16-18 |
| Laundry: **الطباعة تستدعي التسوية آلياً**؛ إعادة تسوية فاتورة مسواة تتطلب تأكيداً (Ok/Cancel) | FOM-HSK §11-12 ص30-37 |
| Split Bill للغسيل **للإشغالات المتعددة**؛ Discount بالنسبة أو المبلغ + سبب؛ Tax Exemption بقيمة وسبب | FOM-HSK §11 ص33-35 |
| Settle Laundry بأنماط: Guest/Cash/Company/CC/Staff/**Complimentary**/**Void-BOH** (بملاحظة "void the bill or nullify the bill") | FOM-HSK §12 ص36-41 |
| Hold Laundry: نطاق التاريخ **داخل الشهر نفسه** + وضع tagged يتطلب **مصرّحاً** وملاحظات | FOM-HSK §13 ص42-43 |
| Lost & Found: تسجيل القيمة والموقع + من وجدها + من استلمها **+ المصرّح** بالعودة | FOM-HSK §14 ص43-48 |

## BR-FO-15: قواعد سجل الضيوف والولاء

| القاعدة | المصدر |
|---|---|
| Guest Code **تلقائي** لكل ضيف؛ تحديث السجل **في كل زيارة** | FOM-GST §1 ص3 |
| Guest Master: تبويبات (Contact/Passport/Personal/Privilege Card/Visit Details/Likes&Dislikes/Comments/Complaints/Photo/Preferences) + **Black Listed Yes/No** | FOM-GST §1 ص3-17 |
| Merge History: ضيف رئيس **واحد حصراً** (M) — البقية تدمج فيه؛ البحث يلزم ≥ 3 أحرف | FOM-GST §12 ص48-50 |
| Purge Guest History: **نهائي غير قابل للاسترجاع** عبر Guest Query Engine | FOM-GST §13 ص50 |
| Loyalty Master: Card# (15 حرفاً)، Join Date ≤ تاريخ الخادم، Expiry، خصومات **لكل منفذ** (بنسبة/قيمة، وبحسب covers) | FOM-GST §15 ص51-55 |
| Redemption Entry: نقاط مكتسبة/مستبدلة + **سبب + مصرّح** | FOM-GST §17 ص57 |
| Revenue Forecast: نطاق **15 يوماً** يبدأ من تاريخ ≥ المحاسبة + خيار تضمين Complimentary/House Guest في ARR | FOM-LUK §21 ص48 |

## BR-FO-16: قواعد إدارة الغرف والجدولة المنزلية

| القاعدة | المصدر |
|---|---|
| OOO يتطلب **سبباً من قائمة + قسماً يُبلَّغ**؛ OOS وصفاً فقط؛ From يتعبأ آلياً باليوم؛ التحرير عبر نافذة الإفراج (uncheck + Confirm) | FOM-HSK §1 ص2-10 |
| **Click&Drag = تمديد الحالة أياماً إضافية؛ Drag&Drop = نقلها لتواريخ أخرى** | FOM-HSK §1 ص3 |
| عرض الحجز بحالة الغرفة يتطلب تاريخاً ≥ اليوم | FOM-HSK §1 ص5 |
| HK Room Status: تفاصيل pax (بالغ/طفل/رضيع) **متاحة فقط عند Occupied** + تعليمات خاصة لكل غرفة | FOM-HSK §3 ص13-14 |
| HK Credits: نقاط (Stayover/Checkout/Vacant) **محددة لكل نوع غرفة** | FOM-HSK §4 ص15-16 |
| Employee Schedule: نوبات **بحد أقصى 7 أيام** من تاريخ الجدولة (≥ تاريخ المحاسبة) | FOM-HSK §5 ص17-22 |
| Room Cleaning Assignments: فرز بحالة (Vacant/Occupied Dirty/Clean + Include OOO) + Summary بالطابق/الموظف + تعيين الموظفين (أزرق) | FOM-HSK §6 ص23-24 |
