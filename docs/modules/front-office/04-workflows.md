# 04 — سير العمل (Workflows) — وحدة Front Office

> **قاعدة:** كل خطوة موثقة بمصدرها (ملف/صفحة). الاستدلال يوسم `[INFERENCE]`.

---

## WF-FO-01: الحجز السريع (Quick Reservation) — Happy Path

**المصدر:** FOM-RES §1.1 (ص3-14)

```
1. إدخال Arrival (Enter=اليوم | رقم+Enter=N أيام | F1=تقويم | يدوي)
2. إدخال Departure → Nights تُحسب آلياً
3. اختيار Property (إن تعددت)
4. Company code (F1) — إن كان الحجز شركاتياً
5. Booker type (F1) + Mobile — إن كان عبر وكيل حجز
6. Room Type + Mode + عدد الغرف (✓ أخضر يؤكد) + Adults/Children
7. Room Details (سرير مفرد/مزدوج/ثلاثي + Extra Bed)
   ⚠ قيد: مجموع الغرف هنا = حقل Rooms الرئيسي
8. Hotel Position (تحقق توفر) | Agent Allocation | Daywise Plan
9. Booking Type: Confirmed أو Waitlist
10. Rate Information → Rate ID → Rate Table (Room Type × Meal Plan × Currency)
    + خيارات الحزمة (حصري التعرفة / شامل / ضريبة الخطة شاملة)
    + Print in Voucher: Yes/No
11. Confirm → Package Selection → أسماء الضيوف
    ⚠ مطابقة Guest History: أسماء مشابهة → Guest Profile screen
    ⚠ كشف التكرار: حجز مكرر → تنبيه
12. Save → Post Save Dialog:
    - Reservation number يولَّد
    - Print Voucher (نعم → طباعة/إيميل)
    - Assign Rooms (نعم → Assign Guest Rooms)
    - Deposits (نعم → Cash/Credit Card/Cheque)
13. إثراء لاحق (Amend): Guest Info / Pickup & Drop / Privilege & Credit Card
    / Passport & Visa / Vehicle / Likes & Dislikes / Trace / Guest Note (F9)
    / Documents (F10) / Extra Charges / Revenue Discount
```

**التقاطعات:**
- Deposit عند الحجز → يظهر عند Check-in (FOM-CAS ص9)
- Extra Charges قبل الوصول → posting target: Reservation / Rooms / Guests (FOM-RES ص24-25)

---

## WF-FO-02: الحجز متعدد الضيوف برقم واحد (Add)

**المصدر:** FOM-RES §Add (ص27-29)

بعد إدخال ضيف واحد على الأقل: `Add` → تواريخ مختلفة + Room Type مختلفة + أسماء → رقم حجز واحد لضيوف متعددين (عرض عبر `Additions`). يتطلب الحقول الإلزامية لكل ضيف.

---

## WF-FO-03: إلغاء حجز ورد الوديعة

**المصدر:** FOM-RES §1.3 (ص37-40)

```
1. Cancel → Scan Booking (بحث بمعايير متعددة)
2. تأكيد الحوار (Yes)
3. عمود Cancel: No → Yes
4. Proceed → Reason Entry: سبب (من قائمة أو جديد) + اسم المعتمد + بيانات المتصل
5. Proceed → الحجز يُلغى
   ⚠ إذا كانت هناك ودائع: نافذة Deposit تظهر → Refund → اختيار الإيداع
   → مبلغ الرد + السبب → Save
```

**ملاحظة:** Re-Instate Cancel (§1.7) ينشئ **رقم حجز جديداً** — رقم الإلغى القديم لا يُستعاد (ص47: "The cancelled reservation details will not exist").

---

## WF-FO-04: No-Show وإعادة تفعيله

**المصدر:** FOM-RES §1.8 (ص47-48) + FOM-RES §6 (ص67-68)

```
1. النظام يوسم No-Show بعد اكتمال Night Audit لتاريخ الوصول
2. Retentions-Cancel/No Show: تحميل قائمة الإلغيات/عدم الحضور
   → إدخال Charge Amt لكل ضيف → Save (رسوم الاحتجاز)
3. Re-Instate No-Show (عند عودة الضيف): Scan Booking → أسماء وتواريخ جديدة → Save
```

**رابط محاسبي:** Retention Charges قابلة للترحيل عبر Additional Room Rate → Retention Charges (FOM-CAS ص23-25) وDeposit Refund → Retention Charges (FOM-CAS ص85-86).

---

## WF-FO-05: تسجيل الوصول — الأنماط الأربعة

### 5.A Express Check In (المصدر: FOM-REG §1، ص3-13)

```
قائمة الوصولات (Expected/No Show/Next Day) + فلاتر
(Guest Name/Res#/Company/Group/Flight + VIP/F9-Note/F10-Doc/Messages/Partial/Repeat)
→ Double-click الضيف → تصحيح الاسم إن لزم → تخصيص غرفة من المتاح بنفس النوع
(فلاتر: Interconnected/Opposite/Special Features/Vacant/Dirty/OOO)
→ Check-in → الغرفة تخصَّص
مرافقات: Current Status | Hotel Position (Hourly/Detailed/Next Day/Yearly/2D Bar/2D Line)
```

### 5.B Reservation Check In (المصدر: FOM-REG §2، ص13-16)

بحث (Length of Stay وغيرها) → سجل يحمل 22 حقلاً ظاهراً (Reservation No/Wait List/Guest/Group/Company/Ref/Room/Date/Type/Bill Inst/Confirm/Special Inst/Provisional/Flight/Pax/Property/Dates/Rate/Meal Plan/Contact) → Color Legends: green=frequent, peach=waitlist, purple=checked-in.

### 5.C Express Walk-in (المصدر: FOM-REG §3، ص16-17)

غرفة (تُعرض مع أيام توفرها) + Departure + الاسم (Title/Last/Middle/First) → Express Walk-in → Room Rack window (Reg#, Room#, Departure) → Ok. **بلا بيانات إضافية.**

### 5.D Walk-in الكامل (المصدر: FOM-REG §3، ص18-33)

```
غرفة + مغادرة + اسم → Walk-in → شاشة البيانات الكاملة:
- العنوان + Designation + Occupation + Classification (عادي/Time-share...)
- Guest Status (F1) + Document Center (DW): status/المزوّد/Subject + مرفقات (F5/F6)
- Nationality + More → Passport Information → Confirm
- Pax Type + Check out time format (12 Noon / 24 Hour)
- Trace: تفضيلات من قائمة → All/Guest → Days column (تاريخ/وقت)
- Send SMS: Yes/No
- Company → Details → Company Code (F1) → Confirm
- Bookers → Booker Type (F1) → Confirm
- Bill Inst (F1) + Business Source (F1) + Market Segment (F1)
- Pay Mode (F1) + Plan Code (F1) + Rate
- Scanty Baggage: Yes/No
- Vehicle Information (نموذج كامل)
- Revenue Discount (F1 Discount Id / إنشاء: Id + Description + Revenue item)
- Special Instruction + Local Add (عنوان جهة محلية) + Others (Flight/Swipe/Card)
→ Save → الضيف مقيم (تحقق عبر Occupied / Dirty / All)
⚠ تخصيص غرفة معلّمة للصيانة → تنبيه Alert
```

---

## WF-FO-06: إدارة الإقامة (In-Stay Management)

**المصادر:** FOM-REG §6 (ص39-55) + FOM-REG §12-16

### 6.A تغيير بيانات الضيف (Change Guest Info)
Retrieve بـ Room#/Reg# → تعديل → History: كامل معلومات الحجز → Change Tariff / Pax Details (child↔adult, Extra Bed) / Rate Information (حسب Rate Type) / خصومات Revenue → **Reason + Authorized By + Remarks** → Save.
> ⚠ **قيد:** تعديل التعرفة للأيام **المستقبلية فقط** — تعديل الماضي → رسالة خطأ (FOM-REG ص47).

### 6.B نقل/تبديل الغرفة (Room Transfer / Swap)
- **Transfer:** Room Change → غرفة → Show Rooms → Room Rack → غرفة vacant مفضلة → Save → **نافذة تفويض: Remarks + اسم المصرِّح** → Ok.
- **Swap:** تبادل غرفتين لضيفين + نفس التفويض.
> ⚠ **قيد:** النقل/التبديل في **التاريخ المحاسبي فقط** (FOM-RES ص60).

### 6.C تعديل الإقامة (Amend Stay)
Room# → guest/Reg/Departure → تغيير Departure date/time → Apply → Save (امتداد أو تقصير).

### 6.D حد الائتمان (Credit Limit)
Room# → Card Use Amount Yes → إدخال Amount في شبكة Credit Card Amount (أو No → Amount مباشرة) → Save → Preview.

### 6.E تعليمات الغرفة (Room Instruction — FOM-REG §12)
Room# → تعليمات Cashier → Night Audit (يومي أو بتاريخ محدد) → Housekeeping.
> البنود تظهر عند Checkout أو أثناء Night Audit، ورسائل Cashier/Housekeeping تظهر pop-out وقت Night Audit (ص84).

### 6.F تغيير التعرفة / Hurdle / خصم المجموعات / حظر الترحيل
- **Change Rate (§13):** Company/Currency/Classification/Checkout format/Plan/Rate Type + Pax Details.
- **Hurdle Rate (§14):** Month/Year → تعرفة لكل يوم من تاريخ محاسبي.
- **Group Rate Updation (§15):** Group → Load → Discount% → Apply + Change Plan (لكل المجموعة).
- **Stop Charges Posting (§16):** Occupancy Search → اختيار Revenue Codes (أو Select All) → Save → تُحظر الشحنات عليها.

---

## WF-FO-07: الترحيل والفوترة (Posting & Billing)

**المصدر:** FOM-CAS §1 (ص2-38)

### 7.A ترحيل شحنة يدوية (Post Charges)
Posting → الغرف المشغولة (بحث/فرز: Room#/Group/Company/Nationality/Room Type/Guest Name/Resv#/Status/Clf/Reg#) → Post Charges → Add → Room# → Revenue Code (F1) → Particulars → Currency (افتراضي: العملة المحلية) → Charges → Exchange Rate → Save. (Total Amount شامل الضرائب)
> ملاحظة: فواتير المطاعم تُرحَّل من POS مباشرة (ص4) — Double-click على معاملة Outlet يعرض بنودها.

### 7.B الودائع (Deposits)
ثلاث بوابات: **For Guests** (Room# + Cash/CreditCard/Cheque) / **For Rsvn** (Reservation# بمعايير Guest/Company/Group/ArrDate/Ref#) / **For City Ledger** (Company#).
- Credit Card: Type (F1) + Company Code (F1) + Particulars + Amount + Authorization # (تلقائي عبر portal عند السحب؛ غير إلزامي).
- Cheque: Cheque#/Date/Bank/Branch.
- عمليات: Add/Modify/Delete/Browse.

### 7.C Paid Outs
**Rooms** (للضيوف المقيمين): Room# + Folio# + Currency → Exchange Amount → الحساب آلي + Mode (Cash/CreditCard) + المبلغ + Particulars + Reason (F1 قائمة معرَّفة) + Voucher#.
**City Ledger** (لغير الضيوف): Company → نفس البنود. يدعم متعدد العملات لكل معاملة (ص19).

### 7.D Miscellaneous Charges — **لغير المقيمين فقط**
Revenue Code + Description + Mode + Particulars + Charges (مثال موثق: زائر يتصل هاتفياً → تُرحَّل المكالمة لفوليو الضيف المقيم) (ص19-20).

### 7.E ترحيل تعرفة الغرفة (Room Rate)
- **Individual:** Additional tariffs Yes/No (+ Room Count Yes/No) → Room# → تُعرض آلياً (التاريخ المحاسبي، العملة، سعر اليوم، Rate/Plan) → قابل للتعديل → Day Charge = **1 أو 0.5** (نصف يوم) → Save.
- **All Rooms:** Save → Continue/Abort. تُنفَّذ عادة عند Night Audit (ص22).
> ⚠ **قيد سلوكي:** Room Rate يرحّل شحنة **واحدة** للغرفة — التنفيذ المتكرر يسجّل الأخير فقط؛ للتعدد استخدم Additional Room Rate (ص22-23).

### 7.F Additional Room Rate
أنواع الترحيل: **Rate / Plan / Extra Bed / Retention Charges** — لكل منها: Room# → Guest Info → Currency → المبلغ → Taxable Amount → Tax Amount → Day Total + Local Value → Room Count Yes/No → Save.

### 7.G الخصومات (Allowances)
- **Bill Allowance (على معاملات FO/POS):** Room# → Select Revenue → Insert/Delete + From/To + Revenue Code.
  > ⚠ **قيد:** From/To ضمن مدى Arrival↔Departure (ص26، ص29).
  - Tax column: Yes/No/Exempt.
  - Apply Discount: Percentage أو Amount → Apply → يظهر في عمود Allowance.
  - F&B Break: عرض تفصيلي بنود F&B للفاتورة.
  - Save → **Reason + Remarks + Authorized By** → Confirm.
- **Consolidated Allowance:** Room# → Folio/Reg/Guest آلياً → Revenue → Voucher# → Currency → Base Amount (+Local Value آلياً) → Tax selection (luxury/service/VAT حسب الوصف) → Amount per Tax → Save → Reason/Authorized By → Confirm.

### 7.H الفوترة عند المغادرة (Check Out screen)
معايير (Company/Group/Room Type/Floor) → **Cutoff Date** (تسوية جزئية للفترة الأولى — مثال موثق: ضيف شهر يدفع أول 15 يوماً) → Bill Summary (+ تغيير Billing Instruction) → Details (Excel) → **Print Bill** (نهائي) / **Prov Bill** (بدون رقم، غير قابل للتسوية، للعرض فقط) / **Split Bill** (Merge / Revenue Split / New Bill / سحب المعاملة) / **Reprint POS Bill** (بتاريخ أو شهر + مطعم + Normal/Compliment + Bill#).

---

## WF-FO-08: التقسيم والنقل والربط

**المصادر:** FOM-CAS §5-§9

| العملية | المسار | قيود موثقة |
|---|---|---|
| Split Front Desk Charges | Help → ضيف → Opt=Y → Split Manually (Trn Amt) / Automatically (عدد سجلات) | — |
| Split F&B Charges | Room# (متعدد) → Load → Split=Y → Split Menu (Food/Liquor/Soft Drinks/Tobacco/Others + Tips + Round Off) → أرقام التقسيم → Ok → Preview/View Bill | التقسيم حسب نوع القائمة |
| Split Folios | Room# → Load → Split → Selected=Yes → Save | **Pax > 1 إلزامي** |
| Transfer Folios | From Room → To Room → Selective (Tag=Yes لكل معاملة / Select All) أو All → Save → تفويض (Remarks+Authorized) → Save | تفويض إلزامي |
| Link Rooms | Link → Main Room (F1) → Load → غرفة مرتبطة → Selected=Yes → Save | لطباعة فاتورة واحدة لغرف متعددة |
| Delink Rooms | Delink → Main Room# → Load → Selected=Yes → Delink | — |
| Pax Transfer | Room# → Transfer To → Save → تفويض → Ok | نقل pax/cover بين الغرف |

---

## WF-FO-09: التسوية والمغادرة المالية (Settlement)

**المصدر:** FOM-CAS §13 (ص69-80)

```
Settlements → Bill# (F1 من قائمة الفواتير المعلقة) → تفاصيل (Guest/Net Amount)
→ Enter → اختيار نمط التسوية:
  • Cash: Amount + Tip Amount + Remarks → Confirm
  • Credit Card: Type (F1) + Company (F1) + رقم البطاقة + صلاحية M/Y
    + Authorization # + Currency + Amount + Remarks → Confirm
  • Companies: Company Code (F1) + Amount + Remarks → Confirm
  • Staff: Staff Code (F1) + Amount + Remarks → Confirm
  • Bill on Hold: Amount + Remarks → Confirm
  • Foreign Exchange: Exchange Details → العملة → Received → تحويل آلي
    (مثال موثق: دولار → INR) + Tip → Confirm
  • Complimentary: المبلغ آلي + Tips + Remarks → Confirm
  • Cheque: رقم/تاريخ/بنك/فرع + Amount + Tips + Remarks → Confirm
→ Save
  ⚠ إن لم تتطابق التسوية: رسالة "Settlement is not tallied" → Cancel وإعادة المطابقة
  Multi-settlement متاح لنفس الفاتورة
  Clear Room# window (INI Switch 64) → Ok → الفاتورة مسواة والغرفة غير مشغولة
```

**عمليات مرافقة:**
- **Receipt Print:** لكل تسوية receipt → قائمة (Room/Reg/Bill/Receipt/Date/Net) → Print.
- **Foreign Exchange Entry:** تفاصيل تسوية العملة الأجنبية (Room/Reg/Bill/Date/Currency/Rate/Amount).
- **Resettlement:** اختيار فاتورة مسواة → Ok → إعادة تسوية بنمط مختلف.
- **إبقاء الإشغال:** النظام يتيح الاحتفاظ بالضيف مشغولاً بعد التسوية (ص69).

---

## WF-FO-10: ما بعد المغادرة وقبل Night Audit

**المصادر:** FOM-CAS §14-§16 + FOM-DEP

- **Folio Re-Instate (§14):** إعادة فتح فوليو مغادِر **قبل Night Audit فقط** — الغرفة المرتبطة/الفرعية تتطلب إعادة فتح الرئيسية أولاً (ص82).
- **Release Stop Posting (§15):** فتح فوليو بعد Print Bill — مشروط بـ **FO Module Attribute 16 = Yes** ("Posting to be stopped once the bill is printed").
- **Deposit Refund (§16):** Res# → Refund Amount أو Retention Charges (Cash/Credit Card/Cheque) + Rooms/Room Type/Occupancy.
- **Confirm Checkouts (§10):** تعديل وقت مغادرة يومية اليوم.

---

## WF-FO-11: العمليات النقدية المكتبية

**المصادر:** FOM-CAS §17-§19

- **Foreign Exchange Entry (§17):** Add → Currency → Voucher (F1، تلقائي/يدوي حسب INI Switch) → Receipt# → Particulars/Encashment#/Exchange Amount → Room/Guest (F1) + Passport# + Outlet + Bill# (F1) + Bill Date/Amount/Paid Out + Nationality (F1) + العنوان → **شبكة الفئات:** Quantity (عدد الأوراق) + الوصف + Denomination + المبلغ + Local Value → الإجمالي (عملة أجنبية + محلي) − العمولة = Net Amount → Save. (الضريبة قابلة للحساب)
- **Credit Card Encashment (§18):** Add → Currency (F1) + Card Type (F1) + Company (F1) + رقم البطاقة + Authorization + Particulars + Total Amount (+Local Value) → Less Commission % → Net Amount → Authorized By + Remarks → Save. (رقم Encashment يولَّد آلياً)
- **Tag Agent Commission (§19):** From/To + Company (F1) → Load → فواتير (Room/Arr/Dep/Guest/Tariff) → Tag=Yes للمسدد → Save → تختفي من قائمة الدفع. Retrieve Tag Entries لاسترجاع الموسومة.

---

## WF-FO-12: عمليات الإشغال والمخزون

**المصادر:** FOM-RES §3-§7 + FOM-REG §17-§23

- **Room Rack Console:** سحب التواريخ + Right-click: Room Booking / OOO / OOS / Check-in (Partial متاح) / Checkout / Transfer & Swap. مؤشرات: عمودي=نقل/تبديل، أفقي=Amend Stay/Extend Blocks، Double-click=Release blocks.
- **OOO:** From/To **غير قابلين للتحرير** + Description + Reason (قائمة معرفة) + Department → Save.
- **OOS:** From/To غير قابلين للتحرير + Description → Save.
- **Amend/Release Block:** سحب من Departure للامتداد؛ Double-click على تاريخ للتقليص.
- **Close Room Inventory:** Month/Year → Double-click عمود Status → حرف **C** → يُمنع الحجز لليوم/النوع — **walk-ins تبقى مسموحة** (RES ص68).
- **Create Hotel Chart:** username/password → Property (أو All) → Hotel Chart (Reservations+Registrations+Room Blocks) أو Agent Chart (Allocations+Blocks لكل وكيل) — نشاط خلفي.
- **Daywise Over Booking:** Property + MMYY → نمط overbooking يومي حسب النوع بحد أقصى.

---

## WF-FO-13: خدمات الضيف والاتصالات

**المصادر:** FOM-REG §7-§8 + §25-§28 + FOM-RES §4

| الخدمة | التدفق | ملاحظات موثقة |
|---|---|---|
| Messages (مقيم) | Search Name → رسالة + مرسل (اسم/هاتف/عنوان) → Save | — |
| Reserved Guest Messages | Name (F1) → الرسالة → Save | للحجزين غير الواصلين |
| Locator | Room# → موقع الضيف → Save | — |
| Likes/Dislikes | Add/Modify → Room# → الإدخال → Save | التوصية: توثيق الكامل لاطلاع كل موظفي FO |
| Wakeup Calls | Room أو Extension → الوقت + طلبات (طعام...) + Require Reminder+وقته | جماعي: Group Code → Double-click Yes لكل ضيف |
| Complaints (Log/Attend/Browse) | Log: Room/Other + Department + Nature → Save. Attend: اختيار + Attended By + Date/Time + Remarks → Save. Browse: Department/Room/Date + All/Pending/Completed | — |
| Guest Photo | ضيف → Select (تصفح) → Save | استبدال الصورة القديمة بسؤال؛ يُرحَّل للتاريخ إذا Post History=Y |
| Mask Guests | Double-click السجل (يظهر أحمر) → التفاصيل → Save | VIP إخفاء الحضور |
| Turn Away | From/To + Property + Room Type + Rooms/Pax + اسم + تواصل + Company + Remark → Save | → Denial Report |
| Extension Password | Room/Extension → كلمة مرور **رقمية** → Reg# (F1) للغرف متعددة الضيوف → Save | صالحة حتى checkout |
| Activate/Deactivate Extension | Room/Extension → Activate أو Deactivate → Local/STD/IDD (Yes/No) → Save | two-way link: يتفاعل مع check-in/checkout |
| Adhoc SMS | Group/Room/Check-Out Guest → تحديد الضيوف → الرسالة + Mobile# → Message to All → Ok → Send | — |
| SMS Status | أزرار (Bookings/Check-ins/Complaints/Transfers/Birthdays/Checkouts) → All → Refresh | real-time |
| Billing Broadcast | Add → From/To + Subject + المنافذ + الرسالة → Save | تظهر scrolling عند الفوترة؛ التعديل للمستقبلي فقط |

---

## WF-FO-15: تدفق Housekeeping (FOM-HSK — موثق كاملاً، الجلسة 3)

> FOM-HSK = 18 وظيفة: Room Block · Clear Rooms · HK Room Status · HK Credits · Employee Schedule · Room Cleaning Assignments · Laundry Item/Rate Master · Laundry Holiday Table · Laundry Entry · Laundry Bill Printing · Settle Laundry Bill · Hold Laundry · Lost and Found · HK Inventory Master/Issue/Return · User Defined Print (LAU).

**15.1 حجب الغرفة (Room Block):**
1. عرض الشبكة (غرف × تاريخ) بحالاتها؛ التاريخ ≥ اليوم (FOM-HSK §1 ص5).
2. **OOO:** Right-click على Dirty/Vacant → Out of Order → From (يومياً آلياً) + To + Description + **Reason من dropdown** + **Department المُبلَّغ** → Confirm → **تمييز بني**.
3. **OOS:** Right-click → Out of Service → From آلي + To + Description → Confirm → **تمييز بنفسجي**.
4. التحرير: Right-click على حالة OOO/OOS → نافذة قائمة الغرف المحجوبة → **uncheck + Confirm** للإفراج.
5. تمديد الحالة: **Click & Drag** من حافة الخلية؛ نقلها: **Drag & Drop** إلى تواريخ أخرى → Save.

**15.2 حالة الغرف المنزلية (HK Room Status):** تحديد الحالة من dropdown لكل غرفة + pax (بالغ/طفل/رضيع — **فقط عند Occupied**) + Instruction (تعليمات خاصة) → Save. يغذي **Room Verification Report** (pax/أمتعة متروكة/غرف منظفة) (FOM-HSK §3 ص13-15).

**15.3 الغسيل (Laundry):** Item Master + Rate Master + Holiday Table (أسعار بديلة أيام العطل) → **Laundry Entry** (Room/ضيف → البنود والكميات) → **Bill Printing** (Guest → Room# → Select Yes → Print → Confirm؛ **الطباعة تستدعي التسوية آلياً**) → **Settle Laundry Bill** (Bill# F1؛ إن كانت مسواة: رسالة → Ok لإعادة التسوية/Cancel) بأنماط Guest/Cash/Company/Credit Card/Staff/Complimentary/Void-BOH → **Hold Laundry** لمتابعة المعلق (tagged/untagged مع مصرّح) (FOM-HSK §7-13 ص26-43).

**15.4 المفقودات (Lost & Found):** Add → Module/Outlet + تفاصيل (القيمة/الموقع/التاريخ/الضيف) + **مَن وجدها** (اسم/تاريخ/وقت/موقع) → حفظ → عند الإعادة: Date + **Whom** + **Authorized By** → Confirm → قائمة Return (FOM-HSK §14 ص43-48).

**15.5 الجدولة والتنظيف:** Employee Schedule (نوبة ≤ **7 أيام**، CREATE/MODIFY) + Occupancy Forecast (A.R.R مع Complimentary/House Guest/Provisional) + Room Cleaning Assignments (فرز بالحالة، Summary بالطابق/الموظف، تعيين موظفين → أزرق) + HK Credits (Stayover/Checkout/Vacant لكل نوع غرفة) (FOM-HSK §4-6 ص15-24).

## WF-FO-16: تدفق Guest History والولاء (FOM-GST — موثق كاملاً، الجلسة 3)

> FOM-GST = 17 وظيفة: Guest Master · Guest Comments Entry · Repeat/Birthday/Anniversary Lists · Guest History List · Guest Revenue List · Guest Visit/Comment Reports · Mailing Letters/Labels · Merge History · Purge Guest History · Setup Loyalty Cards/Master · Loyalty Ledger · Redemption Entry.

**16.1 Guest Master (10 تبويبات):** Guest Code **آلي** → Name/Address/City/State/Country/Zip/Phone/Email + Designation/Nationality/Guest Status/Classification + Gender + Special Instruction + عدد الليالي + **Black Listed Y/N** → Contact (Company Code F1 → تعبئة آلية + Secretary + بيانات الشركة) → Passport (رقم/صدار/جهة/انتهاء) → Personal (DOB/Anniversary/Occupation/Frequent Flyer/Loyalty/CC + **الزوجة والأبناء بتفاصيلهم**) → Privilege Card (Card Type من FO Setup + Number) → Visit Details (Reg#/Room/Arrival/Departure/Amount/Last Rate/Company/Visa + **Feed Back**: تقييم Room/Cleanliness/Food/Service + Revenue breakup بالـ Rev. Code) → Likes&Dislikes → Comments → Complaints (Department + Nature + Date/Time) → Photo → Preferences (من Guest Preferences الموحدة) → Save (FOM-GST §1 ص2-17).

**16.2 دورة الولاء:** Setup Loyalty Cards (Card Type 3 أرقام + وصف) → Setup Loyalty Master (Card# ≤15 حرفاً + Join ≤ تاريخ الخادم + Expiry + Guest + Display Text + **خصومات لكل منفذ** بنسبة/قيمة وبحسب menu types وcovers → Active) → Loyalty Ledger (Card# → Points Accrued/Redeemed/Balance/Amount) → Redemption Entry (A/C Date + Card → نقاط/مبلغ/Rate/Value + **Reason + Authorized By**) (FOM-GST §14-17 ص50-57).

**16.3 صيانة السجل:** Merge History (Guest Name ≥ **3 أحرف** إلزامي + Company اختياري + Load → checkbox للضيوف → تحديد **Main واحد (M)** → Merge) · Purge Guest History (Continue → Guest Query Engine → **حذف نهائي**) · Mailing Letters/Labels (مراسلات تسويقية) (FOM-GST §12-13 ص48-50).

## WF-FO-17: خدمات الكونسيرج (FOM-CRG — موثق كاملاً، الجلسة 3)

> **تصحيح موثق (الجلسة 3):** CRG = **Concierge** (وليس Charge Groups كما ظُنّ سابقاً — [CORRECTION]). 5 وظائف: Left Luggage · Parcels & Deliveries · Ticket Request · Valet Parking · Guest Baggage Tickets.

| الخدمة | التدفق الموثق | المصدر |
|---|---|---|
| **Left Luggage** | نوع الضيف (Inhouse/Checked Out) → Room# (F1 → اسم الضيف آلياً) → No of Bags (≤ 99) + Expected Pickup + Description → Save → عند الاستلام: Right-click → Picked up → Luggage collected (تاريخ/وقت آليان) → **تمييز peach** | FOM-CRG §1 ص2-6 |
| **Parcels & Deliveries** | Room# → Package description + Arrived From + Date/Time + Sender → Save → عند التسليم: Right-click → Delivered (تاريخ/وقت) → **peach** | FOM-CRG §2 ص6-9 |
| **Ticket Request** | Room# → نوع الطلب من قائمة → Charges Applicable (Yes→Amount مفعّل / No→**معطّل**) → Date/Time + Description → Save → عند التأكيد: Confirmed → Purchase/Confirmed + Remarks + Date/Time → **peach** | FOM-CRG §3 ص9-12 |
| **Valet Parking** | Room# → رقم تسجيل المركبة + نوع + ماركة + وصف (لون) + Date/Time → Save → عند الاستلام: Picked Up (تاريخ/وقت) → **peach** | FOM-CRG §4 ص12-15 |
| **Guest Baggage Tickets** | Show All (كل المقيمين: room/reg#/name/arrival) → Double-click الضيف → No of Baggage + بنود (اسم/عدد) → Save؛ F5 حذف؛ **F2 = passive** (لا يظهر) → Print Voucher | FOM-CRG §5 ص15-19 |

**قاعدة القسائم الموثقة:** قالب Voucher يجب أن يكون معرفاً مسبقاً في **User Defined Reports تحت System Setup** — وإلا رسالة **"Category does not exist"** (FOM-CRG ص6 + ص19).

---

## سير العمل المعلَّق (محدود الآن)

- WF-FO-14: دورة Night Audit التفصيلية → مكتملة في FOM-DEP (الجلسة 1) وتُدمج هنا في `docs/workflows/` عند إنشائها.
- ~~WF-FO-15/16/17~~ → **مكتملة أعلاه بالقراءة العميقة (الجلسة 3).**
- قراءة FOM-REP (~4,507 سطر) → مؤجلة لمرحلة التقارير (Phase 7).
