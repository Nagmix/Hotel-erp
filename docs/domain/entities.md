# كيانات المجال (Domain Entities) — الإصدار التأسيسي

> **المرحلة:** Phase 1 | **قاعدة الإثبات:** كل كيان مسجل بمصدره. الحقول الموثقة من جداول "Column/Fields" في الأدلة (محفوظة آلياً في `field-extracts/`).
> **الرموز:** [D] موثق نصاً | [I] استنتاج | [ND] غير موثق بعد

---

## 1. كيانات المكان (Physical & Organizational)

| الكيان | التعريف الموثق | المصدر | حقول موثقة (مختارة) |
|---|---|---|---|
| **Property** | كود المنشأة الفندقية (يظهر في كل الإعدادات — يوحي ببنية multi-property) [I] | FOM-SET §1, SYS-SSP | Property Code |
| **Floor** | طابق — يُعرَّف في Room Master وإعدادات الولائم والـ Care | FOM-SET §38, BNQ-SET, Care-Ops | — |
| **Room** | الغرفة الفردية (رقم، نوع، مميزات، حالة) | FOM-SET §8 | Room No, Room Type, Floor, Features, Status |
| **Room Type** | نوع الغرفة — الأساس لكل التسعير والحجز | FOM-SET §1 | Code(3), Name(30), ShortName(10), Total Rooms, OverBooking%, Display Seq, Max Pax, Advance%, Cancellation Charge%, Retention Charge%, Group Count, Applicable From |
| **Room Feature** | خاصية الغرفة (تُختار عند تعريف الغرفة) | FOM-SET §2 | Code(3), Name(30), Short Name(10) |
| **Function Room** | قاعة مناسبات/وليمة | BNQ-CFG | — (تهيئة Associated Rooms, Setup Styles, Features) |
| **Outlet** | منفذ بيع (مطعم/بار/...) | POS-SET §1 | — (Sessions, Order Types, Currencies, Kitchens ترتبط به) |
| **Restaurant Table** | طاولة في منفذ POS | POS-SET | Table Master, Table Layout Design |
| **Kitchen** | مطبخ يصدر/يستلم KOT | POS-SET | Central KOT Definition |
| **Store** | مخزن (MGT) | MGT-SET | Stores Creation, Stores Start Date |
| **Item Location** | موقع صنف داخل المخزن | MGT-SET | — |
| **Department** | قسم تشغيلي (يظهر في كل الوحدات + الترحيل) | SYS-SSP | — |
| **Cost Center** | مركز تكلفة (مفتاح ترحيل محاسبي) | SYS-SSP, MGT-SET | Sub Cost Centre, Link Cost Centers to Dept |
| **Asset Location** | موقع الأصول | FAS-FXD | — |

## 2. كيانات الأشخاص والأطراف (Parties)

| الكيان | التعريف | المصدر | حقول موثقة (مختارة) |
|---|---|---|---|
| **Guest** | النزيل — ملف مركزي Guest Master + Guest History | FOM-GST, FOM-RES | Title, First/Last Name, Nation, Occupation, Address, Phone, Email, Guest Code (تلقائي للمتكرر) |
| **Guest History** | سجل النزلاء المتكررين (يفعَّل خيار Post History) | FOM-RES ص15, FOM-GST | — |
| **Company** | شركة عميلة (عقود، أسعار، فوترة مدينة) | FOM-SET §9, SLM-PRF | Company Type, Company Profile, Rates, Retention/Cancellation Policy |
| **Travel Agent / Booker** | وكالة/حاجز — عمولة الوكيل موثقة في ACR | FOM-SET §19, ACR-OPR | Booker Type, Agent Commission |
| **Member** | عضو النادي/العضوية | MEM-MPF/MMN | Membership No, Category, Corporate/Individual, Validity |
| **Staff / Employee** | الموظف (Personnel Master) + تسوية Staff في الفوليو | HRP-SET, FOM-CAS | — |
| **Vendor** | مورد المشتريات | MGT-SET | Vendor Master, Rating, Terms of Payment, Contract Info, Item Master by Vendor |
| **Sales Executive / Collection Executive** | مندوب مبيعات/تحصيل | FOM-SET §22-23, SLM-PRF | Sales Office, Bookers Master |

## 3. كيانات التسعير والتسويق (Rate & Commerce)

| الكيان | التعريف | المصدر | حقول موثقة |
|---|---|---|---|
| **Room Rate Master** | أسعار الغرفة حسب النوع×الخطة×العملة | FOM-SET §7, FOM-RES ص7 | Rate Types: Rack/Discounted/Contract/Package, Rate ID, Rate Table |
| **Meal Plan** | خطة الوجبات (B/B, L/N, D/N — تركيبات) | FOM-SET §4 | Plan Code(3), Name, Short Name, Sessions (B/F, L/N, D/N) |
| **Plan Rate Master** | سعر الخطة | FOM-SET §5 | Applicable From, Property, Plan |
| **Package Element** | عنصر الحزمة — نسبة توزيع سعر الحزمة على بنود إيراد | FOM-SET §3 | Element ID(6), Description, Revenue, Percentage% (المجموع=100), Tax Structure, Tax Incl./Excl. |
| **Revenue Code** | رمز تصنيف الإيراد (يستخدمه FO/MEM/POS...) | FOM-SET §24, MEM-SET | — |
| **Room Tax Structure** | هيكل ضريبة الغرفة | FOM-SET §6 | Tax Structure, Tax Code (من SYS: Tax Code/Slab/Structure) |
| **Market Segment / Group Market Segment** | قطاع السوق (تصنيف إيراد تحليلي) | FOM-SET §12-13 | — |
| **Business Source / Group Business Source** | مصدر العمل | FOM-SET §10-11 | — |
| **Nationality** | جنسية (تصنيف) | FOM-SET §14 | — |
| **Guest Status** | حالة النزيل (تصنيف) | FOM-SET §15 | — |
| **Guest Classification (Gst. Clf.)** | تصنيف النزيل (خيارات فرز في Posting) | FOM-CAS ص7 | — |
| **Reservation Mode** | نمط الحجز | FOM-SET §16 | — |
| **Discount / Revenue Discount** | خصم على نوع إيراد (Discount ID) | FOM-RES ص25, SLM-PRF | Discount Id |
| **Privilege Card** | بطاقة امتياز (ولاء قديم) + Loyalty Cards في POS | FOM-SET §20, POS-GST | Card Type, Number, Loyalty Eligible Revenue, Points Rate |
| **Company Contract Rates** | أسعار الشركة/الوكالة (Contract) | SLM-PRF, SLM-LUK | Rate Structures, Company Package Rates |

## 4. كيانات الحجز والإقامة (Stay Cycle) — Transient Core

| الكيان | التعريف | المصدر | ملاحظات |
|---|---|---|---|
| **Reservation** | الحجز — رقم يولد تلقائياً | FOM-RES | بحث: اسم/شركة/مجموعة/تاريخ وصول/رقم حجز |
| **Reservation Line/Rooms** | تفاصيل الغرف داخل الحجز (نوع، عدد، بالغين/أطفال) | FOM-RES خطوة 8-13 | عدد الغرف = مجموع تفاصيل الغرف (قاعدة) |
| **Quick Reservation** | حجز سريع ثم إثراء لاحق (Amend) | FOM-RES §1.2 | — |
| **Group Reservation** | حجز مجموعة: Group Code/Name، يولد رمز مجموعة تلقائياً عند بلوغ Group Count | FOM-SET §1, FOM-RES | Group Count (عتبة التجميع) |
| **Room Assignment** | تخصيص غرفة (أثناء الحجز أو الوصول) — مع Interconnected Rooms view | FOM-RES ص10-11 | Release لإلغاء التخصيص |
| **Registration** | تسجيل وصول — رقم تسجيل Reg# | FOM-REG | Express / من حجز / Walk-in / Special Rooms |
| **Walk-in** | وصول بلا حجز | FOM-REG §3 | — |
| **Stay / Amend Stay** | الإقامة (مدة، تعديل المدة) | FOM-REG | — |
| **Folio** | حساب النزيل — Split Folios / Transfer Folios / Split FO & F&B Charges | FOM-CAS §5-8 | — |
| **Check-out** | مغادرة (تأكيد المغادرة، Pax Checkout) | FOM-CAS §10-12 | Confirm Checkouts, Pax Checkout |
| **Deposit** | عربون (نقد/بطاقة/شيك) قبل أو أثناء الإقامة، Tag to Rooms، وRefund | FOM-RES ص12-13, FOM-CAS §3, §16 | — |
| **Guest Trace** | تتبع احتياج النزيل لقسم مسؤول (مرتبط بأيام/تواريخ) | FOM-SET §33, FOM-RES ص20 | Department, Days/Date |
| **Guest Note / Documents** | ملاحظات + مركز مستندات (استلام/إرسال + رفع ملفات) | FOM-RES ص21-23 | Received/Sent, Date, Person, Subject |
| **Extra Charges** | رسوم إضافية (pickup/غسيل/مكالمات) — Reservation/Rooms/Guest | FOM-RES ص24 | Posting method, Tax Incl/Excl, Qty, Charges |
| **Pickup/Drop** | استقبال/توصيل (مطار/قطار/باص، مجاني/مدفوع، خاص/مشترك) | FOM-RES ص16 | — |
| **Passport & Visa** | بيانات جواز/تأشيرة النزيل | FOM-RES ص17, POS-GST | — |
| **Left Luggage / Baggage Tickets** | أمتعة محفوظة (Concierge) | FOM-CRG | — |

## 5. كيانات المبيعات المباشرة (POS & Banquets)

| الكيان | التعريف | المصدر |
|---|---|---|
| **POS Order / Bill** | طلب/فاتورة منفذ | POS-SET, POS-LUK (Pending Bills) |
| **KOT (Kitchen Order Ticket)** | أمر المطبخ — انتظار/تصفح/إصدار KOT Books | POS-LUK, POS-SET |
| **Outlet Session / Shift** | وردية المنفذ (Open/Close Shift) | POS-SET, BNQ-BIL |
| **Order Type** | نوع الطلب بالمنفذ | POS-SET |
| **Menu / Menu Group / Menu Level** | قائمة الطعام وهرميتها | POS-SET |
| **Item / Open Item / Modifier** | الصنف + المعدلات + Hot Keys + Touch Screen Groups | POS-SET |
| **Happy Hours / Sales Promotion** | ساعات سعيدة وعروض | POS-SET |
| **Banquet Booking** | حجز قاعة مناسبة (Make/Amend/Cancel/No-Show/Block/Release) | BNQ-BOK |
| **Banquet Requirement Entry** | متطلبات المناسبة → Pre-Costing → Auto Indent | BNQ-BIL §11-13 |
| **Banquet Deposit / Refund / Retention** | وديعة الوليمة + الاسترداد + رسوم الحجز | BNQ-BIL §10 |
| **Event Type / Menu Master (BNQ)** | نوع المناسبة + قوائم الولائم | BNQ-CFG |
| **Setup Style / Cancellation Policy (BNQ)** | أنماط تجهيز القاعة + سياسة الإلغاء | BNQ-CFG |

## 6. كيانات العضوية (Membership)

| الكيان | التعريف | المصدر |
|---|---|---|
| **Membership Application** | طلب عضوية (فردي/شركة) + فحص + مقابلات | MEM-MPF |
| **Membership Master** | ملف العضو | MEM-MPF |
| **Corporate Master / Affiliated Club** | عضوية الشركات + الأندية المنتسبة | MEM-MPF |
| **Renewal / Termination / Resignation / Deceased / Blacklist** | دورة حياة العضوية | MEM-MMN |
| **Membership Receipt / Subscription / Facility Charges** | إيصالات واشتراكات ورسوم منشآت — Post to AR | MEM-MTR |
| **Member Categories / Structure / Revenue Codes** | تصنيفات وهيكل العضوية | MEM-SET |

## 7. كيانات التوريد والتكلفة (Procurement & Costing)

| الكيان | التعريف | المصدر |
|---|---|---|
| **Purchase Requisition / Indent** | طلب شراء داخلي (+ Indent Templates) | MGT-DNT, MGT-SET |
| **Purchase Order / Standing PO** | أمر شراء / متكرر | MGT-DNT |
| **Service Work Order** | أمر عمل خدمي | MGT-DNT |
| **Quotation Analysis** | تحليل عروض الموردين | MGT-DNT |
| **Goods Receipt / Issue** | استلام/إصدار مخزني | MGT-DNT (Receipt Register...) |
| **Inventory Item** | صنف المخزون (+ Barcode, Item Conversions, Components) | MGT-SET |
| **Item Group / Vendor Rating / Terms of Payment** | مجموعات الأصناف وتقييم المورد وشروط الدفع | MGT-SET |
| **Inter Store Transfer / Sub Store Transfer** | تحويلات بين المخازن | MGT-DNT |
| **Re-Order Process** | إعادة الطلب (حدود إعادة الطلب) | MGT-DNT |
| **Recipe / Sub-Recipe** | وصفة (F&B) | FNB-SET |
| **Kitchen Stock / Opening Stock** | مخزون المطبخ | FNB-COP |
| **Sales/Cost Budgets / Costing Link** | موازنات التكلفة + ربط التكاليف | FNB-SET |
| **Fixed Asset / Asset Groups / Components** | أصل ثابت + مجموعات + مكونات + إهلاك | FAS-FXD |

## 8. كيانات البشر (HR)

| الكيان | التعريف | المصدر |
|---|---|---|
| **Employee / Personnel Master** | الموظف | HRP-PNT, HRP-SET |
| **Job Requirement / Application / Interview / Offer** | التوظيف من الطلب حتى العرض | HRP-RQP |
| **Attendance / Attendance Codes** | الحضور ورموزه | HRP-SET/PNT |
| **ED Code / ED Calculation (Equation)** | بنية الراتب (Earnings/Deductions) + معادلات الحساب | HRP-SET |
| **Salary Template / Grade / Category** | قوالب الراتب والدرجات | HRP-SET |
| **Payroll Transaction / Processing** | معالجة الرواتب والإغلاق | HRP-PNT |
| **Leave (Leave Group/Details)** | الإجازات | HRP-SET |
| **Statutory Deductions (ESI, LWF...)** | الاستقطاعات النظامية (نظام هندي — يحتاج معادلة عربية) | HRP-SET |
| **Roster / Shifts (Care)** | جداول مناوبة المهام | Care-Ops |

## 9. كيانات الدعم (Support)

| الكيان | التعريف | المصدر |
|---|---|---|
| **Complaint (Guest/Task)** | شكوى/مهمة — موحدة تقريباً بين Care وMNT وMEM | Care-Ops, MNT-OPR, MEM-MTR |
| **Task Lifecycle** | Raise → Assign → Work Start → Close / Transfer / Extend | Care-Ops |
| **Equipment / PM Schedule** | معدات + صيانة وقائية + قراءات | MNT-SET/OPR |
| **Job Order (MNT)** | أمر عمل صيانة | MNT-OPR |
| **Telephone Extension / Call / Time-Rate Slab** | امتداد + مكالمة + شرائح تسعير زمنية + ترحيل إيراد | TEL-SET/CAC |
| **Gate Pass** | تصريح حركة مادة/شخص عبر البوابة | FAS-GTP |
| **Laundry Item / Rate / Entry** | عناصر ومعدلات الغسيل + قيده | FOM-HSK |
| **Housekeeping Room Status / Credits** | حالة الغرفة + رصيد تنظيف | FOM-HSK |
| **Room Block / Block Reasons** | حجب غرفة + أسبابه | FOM-HSK, FOM-SET §31 |
| **SMS Services** | رسائل نصية (خدمات وتنبيهات مغادرة الأقسام) | FOM-SMS, Care |
| **User / Access / Menu Access** | المستخدم وصلاحياته | SYS-SSP, ACR-SET, POS-SET (POS User Access) |
| **Currency / Exchange Rate** | عملة + سعر صرف (Exchange Entry) | SYS-SSP |
| **Tax Code / Slab / Structure** | رمز الضريبة + الشريحة + الهيكل (مستوى نظام) | SYS-SSP |
| **Night Audit Info / Night Balance** | نتيجة التدقيق الليلي | FOM-DEP |
| **Consolidated Entry** | قيد إيراد/تحصيل لمنافذ غير مفحوسة (قيد مزدوج متوازن) | FOM-DEP §3 |
| **Ledger / Voucher (FAS)** | حساب GL + سند | FAS-SET/TRN/MST |
| **Cheque Book / Bank Reconciliation** | دفتر شيكات + تسوية بنكية | FAS-MST, FAS-TRN |
| **Statistics Master / Budget** | إحصاءات وموازنات مالية | FAS-MST, FAS-TRN |

---

## ملاحظات جودة

- الكيانات أعلاه مستخرجة من فهارس وجداول حقول موثقة؛ تفاصيل الحقول الكاملة موجودة آلياً في `field-extracts/` (2,099 حقلاً موثقاً حتى الآن) وستُنسخ إلى Screen Specs في Phase 3/4.
- كيانات قيد التدقيق: **Folio تفاصيله الكاملة** (FOM-CAS يجب قراءته بالكامل)، **FAS Posting Rules** (FAS-SET/TRN)، **AR Invoice/Statement** (ACR-BIL/OPR).
- الجدول الزمني للتوسيع: كل وحدة تُحلَّل في Phase 3 توسِّع كياناتها بكل حقولها وتتحول موثقة المصدر صفحة بصفحة.
