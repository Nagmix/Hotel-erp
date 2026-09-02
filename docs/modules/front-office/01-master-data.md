# 01 — البيانات الرئيسية (Master Data) — وحدة Front Office

> البيانات المرجعية التي تعتمد عليها عمليات FO. الحقول التفصيلية لكل Master موجودة في `field-extracts/Front_Office/FN6i-NT-FOM-SET.json` (استخراج آلي: 59 جدول حقول، 2,099 حقلاً) — والسرد الوظيفي أدناه موثق بقراءة FOM-SET العميقة **الكاملة (الجلسة 3 — Quality Gate)**.

---

## 1. البيانات الرئيسية المشغِّلة للعمليات (الموثقة نصاً)

| Master | استخدامه الموثق | المصدر |
|---|---|---|
| **Room Rate Master** | مصدر التعاريف: "The rates are predefined in the Room Rate Master in the Front office Setup" (Rack/Discounted/Contract/Package) | FOM-RES ص6-7 |
| **Room Master / Room Rack** | الغرف وحالاتها (Vacant/Dirty/Occupied/OOO/OOS/Reserved) + Blocks + Floors + Features | RES §3 + REG §1/§3/§5 |
| **Room Type Master** | أنواع الغرف (مثال موثق: QU / Queen Room / Standard / Suite) | RES ص6 + ص35 + REG ص7 |
| **Meal Plan (Plan Code)** | خطة الوجبات مع التعرفة (Rate Table: Room Type × Plan × Currency) | RES ص6-7 + REG §3 |
| **Company Master** | بيانات الشركة (Company Code + Details) | RES ص4 + REG §3 |
| **Booker Types** | أنواع وكلاء الحجز | RES ص5 |
| **Guest History** | سجل الضيوف السابقين (مطابقة تلقائية عند الحجز/check-in؛ Guest Code يظهر آلياً للمتكرر) | RES ص8 + ص15-16 |
| **Pay Modes** | "Pay modes are defined on Fortune using the Pay Modes option" | RES ص13 |
| **Billing Instructions** | تعليمات الفوترة (Bill Inst #) | RES ص13 + REG §3/§21 |
| **Business Source / Market Segment** | تصنيف مصدر العمل/السوق | RES ص13 + REG §3 |
| **Revenue Codes** | رموز الإيرادات (Post Charges / Stop Posting / Allowances) | CAS §1 + REG §16 |
| **Discount Id / Revenue Discount** | هوية الخصم + الوصف + Revenue item | REG §3 + RES §Revenue Discount |
| **Credit Card Types** | أنواع البطاقات + Company Code | CAS §13/§Deposits |
| **Currency Master** | العملات + أسعار الصرف اليومية | CAS §1 + RES §Rate Info |
| **Nationality List** | جنسيات الضيوف (F1) | CAS §17 + REG §6 |
| **Guest Classification** | تصنيف الضيف (عادي/Time-share...) | REG §3 + §6 |
| **Guest Status List** | حالات الضيف (F1) | REG §3 |
| **OOO Reasons** | قائمة أسباب تعطيل الغرف | RES §3 OOO |
| **Paid Out Reasons** | قائمة أسباب المصروف المدفوع | CAS §Paid Outs |
| **Group Master** | المجموعات (Code/Name) + القائد + ربط FIT | REG §17-§21 |
| **Property Master** | الفنادق (Multi-property) | RES §1.1 + REG §23 |
| **Departments** | الأقسام (OOO، Trace، الشكاوى) | RES §Trace + REG §7 |
| **Features (Hotel/Room)** | مميزات الغرف/الفندق (مثال: Balcony, View...) | REG §1 + RES §1.5 |
| **Wake-up/Extension Master** | التمديدات الهاتفية (Room/Extension) | REG §7/§25-26 |

## 2. النمط الإصداري الموحد (من `docs/domain/master-data.md`)

الـ Masters تتبع نمط: **Status Active/Passive + Applicable From + Last Updated** — إصدارية زمنية (لا حذف فعلي) + قاعدة تجميد بعد الاستخدام.

## 3. كتالوج FOM-SET الكامل (67 قسماً) — موثق بالقراءة العميقة (الجلسة 3)

> الجرد الموثق من فهرس ومتن FOM-SET (145 صفحة). التصنيف: **Core Masters** / **Simple Lists** / **Behavior Config** / **Form & Report Designers** / **Data Ops**.

### 3.1 هندسة التعرفة (Rate Architecture) — القراءة العميقة الكاملة

| Master | الحقول الموثقة | قواعد موثقة | المصدر |
|---|---|---|---|
| **Room Types** | Applicable From, Property, Room Type (3), Name (30), Short Name (10), Total Rooms, Over Booking % (3), Display Sequence, Max Pax (4), **Advance %**, **Cancellation Charge %**, **Retention Charge %**, **Group Count** | تعديل = status فقط؛ لبقية الحقول نسخة بتاريخ مستقبلي؛ **Group code يُعيَّن آلياً إذا عدد الحجوزات ≥ Group Count** | FOM-SET §1 ص6-10 |
| **Room Features** | Code (3), Name (30), Short Name (10) | تُستخدم كخصائص للغرف في Room Master | FOM-SET §2 ص10-12 |
| **Package Elements** | Element ID (6), Description (30), Revenue (من Revenue Codes), Percentage %, Tax Structure, Tax Incl./Excl. | **مجموع النسب عبر عناصر الحزمة = 100%** | FOM-SET §3 ص12-14 |
| **Meal Plans** | Plan Code (3), Name (30), Short Name (10), Sessions: B/F, L/N, D/N | تعديل = sessions + status فقط | FOM-SET §4 ص14-16 |
| **Plan Rate Master** | Applicable From, Property, Plan, Currency, Plan Charges (S/D/T/Q، 15.2)، Extra Person (Adult/Child)، Tax Structure (للخطة + للشخص الإضافي) | تظهر في Room Rate Master حسب الخطة المختارة | FOM-SET §5 ص16-19 |
| **Room Tax Structures** | Tax Structure (4 رقمي)، Description (30)، Tax # (تسلسل آلي)، Tax Code، Calculation Type (**Percentage/Amount/Slab**)، Factor، Slab #، Comparison (None/Consolidate)، Calculation (**On Tax**/Consolidate/**Pax**)، Tax # (عند On Tax)، Revenue Code (عند Pax → Rate Selection: **Rack/Charged/High/Low**) | **هياكل ضريبية منفصلة إلزامية لكل من: Tariff وExtra Bed وPlan**؛ تعديل = status فقط | FOM-SET §6 ص19-23 |
| **Room Rate Master** | ثلاثة أنماط: **Package** (ID 4 رقمي، From/To، Room Type، Occupancy: Single/Double/Triple/Quadra، Room Pax، Extra Bed Pax، Days/Nights، Currency، Package Amount + **Breakup بالأعمدة: Tariff/Plan/Services**) / **Rate** (Rate Table # 4 رقمي، Currency، Meal Plan، **شبكة أيام الأسبوع × أنواع الغرف** بأسعار S/D/T/Q + Extra Adult/Child + هيكل ضريبة لكل خلية + شاشة **Service Rate**: Service Code, Adult/Child Rate, Tax Structure, Tax Inclusive) / **Non Rack** (عقود الشركات؛ تعريف مثل Rate) | **النسخية الزمنية للتعرفة:** زيادة To date مسموحة فقط إذا أكبر من تاريخ المحاسبة؛ تخفيضها حتى تاريخ المحاسبة فقط ثم يُغلق الجدول ويُعاد إنشاؤه من اليوم التالي | FOM-SET §7 ص23-30 |
| **Room Master** | Room #, Room Type, Block, Floor, Max Pax, Rate Table, Available Features→Features Selected + **Connecting Rooms** (متجاورة بباب بينها) + **Opposite Rooms** + **Change Room Type** (Old→New + Room Type/Count) | **تغيير نوع الغرفة: فقط إذا Vacant — ممنوع إذا Occupied/Blocked/Dirty**؛ خروج مستخدمي FO قبل التغيير + تنفيذ **Create Hotel Chart** لإعادة بناء Hotel Position؛ تعديل = Block/Floor/Features/MaxPax/RateTable/status | FOM-SET §8 ص30-34 |

### 3.2 Core Masters التشغيلية

| Master | الحقول الدلالية | المصدر |
|---|---|---|
| **Revenue Codes** §24 | Audit Group (**آلي عند الإنشاء، غير قابل للتعديل**)، Revenue Code (3, immutable)، Classification (**Credit Only/Debit Only/Both**)، Revenue Type (**Cash/Voucher/None**)، Voucher Print (Prgm. ID for Debit/Credit + Print Option ports)، Misc. Revenue Yes/No (قيود الخدمة بالضيوف الداخليين)، **Tax Structure (للـ Misc) + Guest Tax Structure (للضيف الداخلي) — هيكلان منفصلان** | FOM-SET §24 ص65-67 |
| **Billing Instructions** §25 | Billing Instruction # (3)، Description (30)، Bill Split No.، Type (**Direct/Company**)، Long Name (30)، Short Name (15)، Revenue Codes متعددة + خيار "One bill assumed if no REVENUE CODE are defined" | FOM-SET §25 ص67-69 |
| **Outlet Settlements** §26 | Applicable From + Outlet (من **POS Setup** — رابط تكاملي) + أنماط التسوية | FOM-SET §26 ص70-71 |
| **Pay Modes** §27 | Pay Mode (3), Description (30) | FOM-SET §27 ص71-73 |
| **Guest Exemptions** §28 | Module (**FOM/POS**)، Classification (**Regular/House Guest/Complimentary/Diplomats/Time Share**)، Main Revenue، Sub Revenue، Menu Type، Exemption % | FOM-SET §28 ص73-75 |
| **Plan Breakup** §29 | Room Type، Plan Bifurcation/Other Revenues، Plan Code/Main Revenue (Tariff افتراضي — **صالح لتعرفة الغرفة فقط**)، بنود Rev. Code/%/Tax Str | FOM-SET §29 ص75-77 |
| **Guest Trace** §33 | Trace Code (**آلي**)، Description (50)، Department | FOM-SET §33 ص83 |
| **Resv. Mandatory Fields** §34 | حقول إلزامية تظهر بعلامة * في Room Booking/Walk-In (أو Select All) | FOM-SET §34 ص83-84 |
| **Guest Preferences** §43 | Preference (11 نوعاً: Hobbies/Sports/Cuisines/Alcoholic/Non-Alcoholic/Restaurants/Holiday Destinations/Magazines/Newspapers/Spa/Color) + Description (30) | FOM-SET §43 ص98-100 |
| **Loyalty Eligible Revenue** §45 | Card Name، App Date، Mod Code (**FOM وPOS فقط**)، Revenue Type (منافذ محددة أو إجمالي فاتورة FO) | FOM-SET §45 ص102-103 |
| **Points Rate Definition** §46 | Applicable Date، Card Type، Reward Rate (مثال: 5 نقاط/1000)، Redemption Rate (مثال: خصم 500 على 5 نقاط) | FOM-SET §46 ص103-105 |

### 3.3 قوائم بسيطة (Simple Lists)

| القائمة | الدلالة | المصدر |
|---|---|---|
| Company Types §9 | Payable/Receivable | ص34-35 |
| Business Sources §10 / Group Business Sources §11 / Market Segments §12 / Group Market Segments §13 | كود + وصف | ص35-39 |
| Nationality §14 · Guest Status §15 · Reservation Mode §16 (تعديل كل الحقول) · MIS Levels §17 · Flight Master §18 · Bookers Type §19 · Privilege Card Type §20 · Sales Office §21 (كل الحقول) · Sales Executives §22 · Collection Executives §23 | كود/وصف | ص39-65 |
| Paid Out Reasons §30 (وصف+status) · Block Reasons §31 (كود 2 رقمي) · Vehicle Definition §32 (Make/Model/Capacity، للنقل في الحجز) | أسباب ومركبات | ص77-82 |
| Events/Occasions §37 (From/To فقط؛ تُعرض في الشاشة الرئيسية) · User Identification §36 (خيارات إثبات الهوية في الحجز) | سلوك الحجز | ص85-87 |
| Housekeeping Staff §39 (عدا الكود) · Laundry Services Type §40 · Laundry Rate Types §41 · Laundry Round off §42 | غسيل وإدارة | ص88-98 |

### 3.4 سلوك وصلاحيات (Behavior Config)

| الإعداد | الدلالة | المصدر |
|---|---|---|
| **FO User Authorization** §35 | تفويض مستخدمين لـ **5 عمليات مميزة**: Accept Over-Booking / Fix Hurdle Rate / Update Hotel Chart / Folio Re-Open / Edit Market Segment — "للمشرفين أو أصحاب السلطة الأعلى" | FOM-SET §35 ص84-85 |
| **Room Floor Design** §38 | مصمم مخطط الطابق بصور .gif؛ **ترميز ألوان حالة الغرفة الموثق**: VC=أخضر · VD=أصفر · RS=أزرق · OD=رمادي · OC=أحمر · OO=بني · OS=بنفسجي · Blank | FOM-SET §38 ص87-88 |
| **Guest Survey Template** §44 | Outlet + Line # + سؤال (60) + Comments Defined→Selected (تقييم المنفذ) — تعديل عدا Outlet/Line# | FOM-SET §44 ص100-102 |

### 3.5 مصممو النماذج والتقارير (§47–63)

Reg Card Form §47 · Pre-Reg Card §48 · FO Bill Customize §49 (إعادة تسمية بنود الفاتورة + توحيد Revenue Codes قبل الطباعة) · FO Bill Spec §50 (رأس/جسم/تذييل + الإجمالي في كل الصفحات أم الأخيرة) · FO Bill Summary §51 · Guest Ledger Report §52 · Bill wise Revenue Setup §53 · Night Sales Report §54 · **FO Budgets §55** (Room Night/Revenue/Pax/Bed Night، عملات متعددة، شهرية، بتصنيف Market Segment/Business Source/Nationality/Room Type) · Night Sales Budgets §56 (للمنافذ) · Manager Reports §57 (Actual/Calculated/Sub Head) · Comparative MIS Spec §58 · MIS Revenue Grouping §59 · MIS Revenue Budget §60 (يومي يجتمع شهرياً) · Setup MIS Revenue §61 · Operational Report §62 (**FO فقط**) · User Defined Print Forms §63 — FOM-SET ص105-140

### 3.6 عمليات البيانات (Data Ops)

| العملية | القاعدة الموثقة | المصدر |
|---|---|---|
| **Purge Reservations** §64 | Cutoff: **حد أدنى 60 يوماً، أقصى 365** | ص140-141 |
| **Purge FO Transactions** §65 | Cutoff ≥ **60**؛ خيار: Audit Tariff Transactions أو FO Transactions؛ يعرض عدد السجلات + تاريخ آخر Purge | ص141-142 |
| **Purge Guest Ledger** §66 | Cutoff ≥ **120**؛ **يجب معالجة تقارير GL/Room History قبل التنقية** | ص142 |
| **MIS Occupancy Entry** §67 | MIS بأثر رجعي (**date < accounting date حصراً**): Total Rooms/No Shows/Blocks(OOO) + Occupancy (Walk-ins/Reservations/Day Use/Complimentary/House Guest/Ext Bed — لأغادية Single فقط) + Arrivals (Count/Persons/ADTPax/CHDPax) | ص142-145 |

## 4. مصفوفة التعديل (Modify Matrix) — القاعدة الموثقة لكل Master

> النمط: **لكل Master مجموعة حقول قابلة للتعديل محددة نصاً**؛ ما عداها يتطلب نسخة جديدة بتاريخ Applicable From مستقبلي:

| المجموعة | الـ Masters |
|---|---|
| **status فقط** | Room Types · Room Features · Tax Structures · Company Types · Business Sources · Market Segments · Nationality · Guest Status · MIS Levels · Flight Master · Bookers Type · Privilege Card Type · Sales Executives · Collection Executives · Outlet Settlements · Pay Modes · Guest Exemptions · Guest Preferences |
| **كل الحقول** | Package Elements · Group Business Sources · Group Market Segments · Reservation Mode · Sales Office · Billing Instructions · Laundry Services/Rate Types · FO Bill Customize |
| **استثناء الكود** | Revenue Codes (عدا Audit Group + Code) · Housekeeping Staff (عدا الكود) · Survey Template (عدا Outlet + Line#) |
| **مجموعات محددة** | Meal Plans (sessions+status) · Plan Rate (الأسعار+الضريبة) · Room Master (Block/Floor/Features/MaxPax/RateTable+status) · Plan Breakup (بنود الإيراد) · Paid Out/Block Reasons (وصف+status) · Vehicle (سعة+status) · Events (From/To) · Budgets (القيمة+per day/month) |

> مصدر المصفوفة: Notes الموثقة في خاتمة كل قسم من FOM-SET (48 قاعدة Note جُمعت جميعها).
