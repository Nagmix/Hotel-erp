# قاموس المصطلحات الموحد (Unified Terminology Glossary)

> **المرحلة:** Phase 1 — الإصدار التأسيسي، يُوسَّع مع كل مرحلة.
> **الغرض:** توحيد المصطلح عبر كل الوثائق والكود والواجهة. **قاعدة:** المصطلح العربي هنا هو المستخدم في UI النهائي، والإنجليزي للكود والأسماء الداخلية فقط.
> **الحالة:** `مقرر` = معتمد لهذا المشروع | `مقترح` = قيد المراجعة

---

## 1. نواة العمليات الفندقية (PMS Core)

| # | English Technical | FortuneNext Term | المصطلح العربي | UI Label النهائي | Internal Code |
|---|---|---|---|---|---|
| 1 | Reservation | Reservation | الحجز | الحجز | Reservation |
| 2 | Quick Reservation | Quick Reservation | الحجز السريع | حجز سريع | QuickReservation |
| 3 | Group Reservation | Group Booking | حجز المجموعة | حجز مجموعة | GroupReservation |
| 4 | Guest | Guest | النزيل | النزيل | Guest |
| 5 | Guest History | Guest History | سجل النزلاء | سجل النزلاء | GuestHistory |
| 6 | Repeat Guest | Repeat Guest | النزيل المتكرر | نزيل متكرر | RepeatGuest |
| 7 | Check-in | Check In / Registration | تسجيل الوصول | تسجيل الوصول | CheckIn |
| 8 | Express Check-in | Express Check In | الوصول السريع | وصول سريع | ExpressCheckIn |
| 9 | Walk-in | Walk in | نزيل مباشر (بلا حجز) | مباشر (بدون حجز) | WalkIn |
| 10 | Check-out | Check Out / Departure | تسجيل المغادرة | تسجيل المغادرة | CheckOut |
| 11 | Pax | Pax (Checkout/Transfer) | شخص (ضيف) | عدد الأشخاص | Pax |
| 12 | Stay | Stay / Amend Stay | الإقامة | الإقامة | Stay |
| 13 | Room | Room | الغرفة | الغرفة | Room |
| 14 | Room Type | Room Type | نوع الغرفة | نوع الغرفة | RoomType |
| 15 | Room Status | Room Status | حالة الغرفة | حالة الغرفة | RoomStatus |
| 16 | Vacant | Vacant | شاغرة | شاغرة | Vacant |
| 17 | Occupied | Occupied | مشغولة | مشغولة | Occupied |
| 18 | Dirty / Clean | Dirty / Clean | غير نظيفة / نظيفة | تحتاج تنظيف / جاهزة | RoomCleanStatus |
| 19 | Room Assignment | Assign Rooms | تخصيص الغرفة | تخصيص غرفة | RoomAssignment |
| 20 | Room Transfer | Room Transfer | نقل الغرفة | نقل الغرفة | RoomTransfer |
| 21 | Room Block | Room Block | حجب الغرفة | حجب غرفة | RoomBlock |
| 22 | Interconnected Rooms | Interconnected | غرف متصلة | غرف متصلة | ConnectedRooms |
| 23 | Room Rack / Floor Plan | Room Rack Console / Room Floor Plan | خريطة الغرف | خريطة الغرف | RoomRack |
| 24 | Hotel Position | Hotel Position | وضع الفندق (الإشغال) | وضع الفندق | HotelPosition |
| 25 | Expected Arrivals | Expected Arrivals | الوصولون المتوقعون | الوصولون المتوقعون | ExpectedArrivals |
| 26 | No-Show | No Show / Provisional No Show | عدم الحضور | عدم الحضور | NoShow |
| 27 | Waitlist | Waitlist Query | قائمة الانتظار | قائمة الانتظار | Waitlist |
| 28 | Amenity / Room Features | Room Features | مميزات الغرفة | مميزات الغرفة | RoomFeature |
| 29 | Hurdle Rate | Hurdle Rate | الحد الأدنى للسعر | سعر الحد الأدنى | HurdleRate |
| 30 | Overbooking | Over Booking % | الحجز الزائد | نسبة الحجز الزائد | OverbookingPct |

## 2. المبيعات والفوليو (Cashiering & Revenue)

| # | English | FortuneNext | العربي | UI Label | Code |
|---|---|---|---|---|---|
| 31 | Folio | Folio | فوليو النزيل (كشف الحساب) | كشف الحساب | Folio |
| 32 | Posting | Posting / Post Charges | ترحيل شحنة | ترحيل | Posting |
| 33 | Charge | Charges | شحنة (رسوم) | رسوم | Charge |
| 34 | Extra Charges | Extra Charges | رسوم إضافية | رسوم إضافية | ExtraCharge |
| 35 | Deposit | Deposit | الوديعة (العربون) | وديعة | Deposit |
| 36 | Paid Out | Paid Outs | مصروفات مفروضة (للنزيل) | مدفوعات نيابة عن النزيل | PaidOut |
| 37 | Allowance | Bill / Consolidated Allowance | الخصم من الفاتورة | تسوية/خصم | Allowance |
| 38 | Settlement | Settlements | التسوية | تسوية الحساب | Settlement |
| 39 | Bill | Bill / Bill Print | الفاتورة | الفاتورة | Bill |
| 40 | Bill on Hold | Bill on Hold | فاتورة معلقة | فاتورة معلقة | BillOnHold |
| 41 | Split Folio / Charges | Split Folios / Split Charges | تقسيم الفوليو/الرسوم | تقسيم الحساب | FolioSplit |
| 42 | Transfer Folio | Transfer Folios | نقل الفوليو | نقل كشف الحساب | FolioTransfer |
| 43 | Revenue Code | Revenue Codes | رمز الإيراد | رمز الإيراد | RevenueCode |
| 44 | Posting Date / Accounting Date | Accounting Date | التاريخ المحاسبي | التاريخ المحاسبي | PostingDate |
| 45 | Business Date (hotel day) | Open New Date | اليوم الفندقي | اليوم الفندقي | BusinessDate |
| 46 | Night Audit | Night Audit / Day End Process | التدقيق الليلي | إقفال اليوم (التدقيق الليلي) | NightAudit |
| 47 | Night Balance | Night Balance | رصيد الليلة | رصيد الليلة | NightBalance |
| 48 | Guest Balance | Guest Balance | رصيد النزلاء | رصيد النزلاء | GuestBalance |
| 49 | Consolidated Entry | Consolidated Entry | القيد الموحد | قيد موحد | ConsolidatedEntry |
| 50 | Excess/Short | Excess/Short (Night Report) | زيادة/عجز الصندوق | زيادة/عجز | ExcessShort |
| 51 | Tip Amount | Tip Amount | البقشيش | بقشيش | TipAmount |
| 52 | Paid Out Reasons | Paid Out Reasons | أسباب المصروف | سبب الدفع نيابة | PaidOutReason |
| 53 | Foreign Exchange | Foreign Exchange Entry | صرف العملات | صرف عملات | ForexEntry |

## 3. الأسعار والخطط (Rates & Plans)

| # | English | FortuneNext | العربي | UI Label | Code |
|---|---|---|---|---|---|
| 54 | Rack Rate | Rack Rate | السعر الأساسي (الرسمي) | السعر الأساسي | RackRate |
| 55 | Discounted Rate | Discounted Rate | السعر المخفض | سعر مخفض | DiscountRate |
| 56 | Contract Rate | Contract Rate | سعر العقد (الشركات) | سعر العقد | ContractRate |
| 57 | Package | Package / Package Rate | الحزمة | حزمة | Package |
| 58 | Package Elements | Package Elements | عناصر الحزمة | توزيع الحزمة | PackageElement |
| 59 | Meal Plan | Meal Plans | خطة الوجبات | خطة الوجبات | MealPlan |
| 60 | Bed & Breakfast | B& B | إقامة مع فطور | إقامة مع فطور | BB |
| 61 | Plan Rate | Plan Rate Master | سعر الخطة | سعر الخطة | PlanRate |
| 62 | Rate Table / Rate ID | Rate Table / Rate ID | جدول الأسعار | جدول الأسعار | RateTable |
| 63 | Tax Structure | Room Tax Structures | هيكل الضريبة | هيكل الضريبة | TaxStructure |
| 64 | Tax Inclusive / Exclusive | Tax Incl./Excl. | شامل الضريبة / غير شامل | شامل الضريبة/غير شامل | TaxInclExcl |
| 65 | Market Segment | Market Segments | قطاع السوق | قطاع السوق | MarketSegment |
| 66 | Business Source | Business Sources | مصدر العمل | مصدر العمل | BusinessSource |
| 67 | Privilege Card | Privilege Card | بطاقة الامتياز | بطاقة الامتياز | PrivilegeCard |
| 68 | Loyalty Card | Loyalty Cards | بطاقة الولاء | بطاقة الولاء | LoyaltyCard |
| 69 | Retention Charge | Retention Charge | رسوم حجز (عدم حضور) | رسوم عدم الحضور | RetentionCharge |

## 4. المطاعم والولائم (POS & Banquets)

| # | English | FortuneNext | العربي | UI Label | Code |
|---|---|---|---|---|---|
| 70 | Outlet | Outlet | منفذ البيع | منفذ | Outlet |
| 71 | Shift / Session | Session / Open-Shift | الوردية | الوردية | Session |
| 72 | KOT | Kitchen Order Ticket | أمر المطبخ | أمر المطبخ | KOT |
| 73 | Pending Bills | Pending Bills | فواتير معلقة | فواتير معلقة | PendingBill |
| 74 | Menu / Menu Group | Menu Master / Groups | قائمة الطعام | قائمة الطعام | Menu |
| 75 | Modifier | Modifier Master | الإضافات (المعدلات) | إضافات | Modifier |
| 76 | Open Item | Open Items Definition | صنف حر | صنف حر | OpenItem |
| 77 | Happy Hours | Happy Hours | ساعات خاصة | ساعات خاصة | HappyHours |
| 78 | Banquet | Banquets | الوليمة/المناسبة | المناسبات والولائم | Banquet |
| 79 | Function Room | Function Room | قاعة المناسبات | قاعة | FunctionRoom |
| 80 | Booking (Banquet) | Banquet Booking | حجز المناسبة | حجز مناسبة | BanquetBooking |
| 81 | Requirement Entry | Requirement Entry | تسجيل المتطلبات | متطلبات المناسبة | RequirementEntry |
| 82 | Pre-Costing | Pre Costing (Chef Eng) | التكلفة التقديرية | التكلفة التقديرية | PreCosting |
| 83 | Auto Indent | Auto Indent | الطلب التلقائي | طلب تلقائي | AutoIndent |
| 84 | Setup Style | Function Room Setup Style | نمط التجهيز | نمط التجهيز | SetupStyle |
| 85 | No-Show Cancellation (BNQ) | No Show Cancellation | إلغاء عدم الحضور | إلغاء عدم الحضور | NoShowCancel |

## 5. المحاسبة والمالية (Finance & AR)

| # | English | FortuneNext | العربي | UI Label | Code |
|---|---|---|---|---|---|
| 86 | General Ledger | GL Codes / Ledger | دفتر الأستاذ العام | الأستاذ العام | GL |
| 87 | Chart of Accounts | Main Heads / Sub Heads | دليل الحسابات | دليل الحسابات | COA |
| 88 | Voucher | Transaction Voucher | السند | سند | Voucher |
| 89 | Journal / Day Book | Day Book | اليومية | يومية الحركات | DayBook |
| 90 | Trial Balance | Trial Balance | ميزان المراجعة | ميزان المراجعة | TrialBalance |
| 91 | Accounts Receivable | ACR | الحسابات المدينة | الحسابات المدينة | AR |
| 92 | Statement of Account | Statement of Accounts | كشف الحساب | كشف حساب | SOA |
| 93 | Aging | Aging Summary | تقادم الديون | أعمار الديون | Aging |
| 94 | Debtors Follow-up | Debtors Follow-Up | متابعة المدينين | متابعة المدينين | DebtorFollowUp |
| 95 | Match Bills–Receipts | Match Bills - Receipts | مطابقة الفواتير والإيصالات | مطابقة الفواتير | BillMatching |
| 96 | Travel Agent Commission | Travel Agent Commissions | عمولة الوكيل | عمولات الوكلاء | AgentCommission |
| 97 | Credit Card Consolidation | Credit Card Consolidation | تجميع البطاقات | تجميع بطاقات | CardConsolidation |
| 98 | Bank Reconciliation | Bank Reconciliation | التسوية البنكية | تسوية بنكية | BankReconciliation |
| 99 | TDS | TDS Tagging | ضريبة الاستقطاع | ضريبة استقطاع | TDS |
| 100 | Fixed Asset | Fixed Asset Master | الأصل الثابت | أصل ثابت | FixedAsset |
| 101 | Depreciation | Calculate Depreciation | الإهلاك | إهلاك | Depreciation |
| 102 | Cost Center | Cost Center | مركز التكلفة | مركز التكلفة | CostCenter |
| 103 | Department | Department | القسم | القسم | Department |
| 104 | Financial Year | Open Financial Year | السنة المالية | السنة المالية | FiscalYear |
| 105 | Budget | Budget / Statistics Budget | الموازنة | الموازنة | Budget |

## 6. المواد والمشتريات (Materials)

| # | English | FortuneNext | العربي | UI Label | Code |
|---|---|---|---|---|---|
| 106 | Purchase Requisition | Purchase Requisition | طلب الشراء | طلب شراء | PurchaseRequisition |
| 107 | Indent | Indent Entries | طلب الاحتياج الداخلي | طلب احتياج | Indent |
| 108 | Purchase Order | Purchase Order | أمر الشراء | أمر شراء | PurchaseOrder |
| 109 | Standing PO | Standing Purchase Order | أمر شراء دائم | أمر شراء متكرر | StandingPO |
| 110 | Service Work Order | Service Work Order | أمر عمل خدمي | أمر خدمة | ServiceWorkOrder |
| 111 | Goods Receipt | Receipt Register | إشعار الاستلام | استلام مواد | GoodsReceipt |
| 112 | Store | Stores Creation | المخزن | المخزن | Store |
| 113 | Inventory Item | Inventory Master | صنف المخزون | الصنف | Item |
| 114 | Item Group | Item Group Creation | مجموعة الأصناف | مجموعة الأصناف | ItemGroup |
| 115 | Vendor | Vendor Master | المورد | المورد | Vendor |
| 116 | Vendor Rating | Vendor Rating | تقييم المورد | تقييم المورد | VendorRating |
| 117 | Terms of Payment | Terms of Payment | شروط الدفع | شروط الدفع | PaymentTerms |
| 118 | Inter Store Transfer | Inter Store Transfer | تحويل بين المخازن | تحويل مخزني | StoreTransfer |
| 119 | Re-order | Re-Order Process | إعادة الطلب | إعادة الطلب | Reorder |
| 120 | Opening Balance | Opening Balance | رصيد افتتاحي | رصيد افتتاحي | OpeningBalance |

## 7. الموارد البشرية والخدمة (HR & Service)

| # | English | FortuneNext | العربي | UI Label | Code |
|---|---|---|---|---|---|
| 121 | Employee | Personnel Master | الموظف | الموظف | Employee |
| 122 | Designation | Designations | المسمى الوظيفي | المسمى الوظيفي | Designation |
| 123 | Grade | Grade Definition | الدرجة | الدرجة | Grade |
| 124 | Attendance | Attendance Entry | الحضور | الحضور | Attendance |
| 125 | Payroll | Payroll Processing | الرواتب | الرواتب | Payroll |
| 126 | Earnings/Deductions | ED Code | البدلات والاستقطاعات | بدلات واستقطاعات | EDCCode |
| 127 | Salary Template | Define Salary Template | قالب الراتب | قالب الراتب | SalaryTemplate |
| 128 | Leave | Leave Group/Details | الإجازة | الإجازة | Leave |
| 129 | Roster | Monthly Roster | جدول المناوبات | جدول المناوبات | Roster |
| 130 | Task/Complaint | Task / Complaint | المهمة/الشكوى | مهمة / شكوى | Task |
| 131 | Lost & Found | Lost and Found | المفقودات | المفقودات | LostAndFound |
| 132 | Housekeeping | House Keeping | الإشراف الفندقي (التنظيف) | الإشراف الفندقي | Housekeeping |
| 133 | Laundry | Laundry Entry | الغسيل | الغسيل | Laundry |
| 134 | Concierge | Concierge | الكونسيرج | خدمات الكونسيرج | Concierge |
| 135 | Gate Pass | Gate Pass | تصريح البوابة | تصريح بوابة | GatePass |
| 136 | Maintenance / Engineering | Maintenance | الصيانة الهندسية | الصيانة | Maintenance |
| 137 | PM Schedule | PM Schedule Master | جدول الصيانة الوقائية | صيانة وقائية | PMSchedule |
| 138 | Equipment | Equipment Master | المعدة | المعدة | Equipment |

## 8. العضوية والنظام (Membership & System)

| # | English | FortuneNext | العربي | UI Label | Code |
|---|---|---|---|---|---|
| 139 | Member | Membership Master | العضو | العضو | Member |
| 140 | Membership Application | Membership Application | طلب العضوية | طلب عضوية | MembershipApplication |
| 141 | Renewal | Renewal Entry | تجديد العضوية | تجديد | Renewal |
| 142 | Subscription | Process Subscription | الاشتراك | الاشتراك | Subscription |
| 143 | Blacklist | Members Blacklist | القائمة السوداء | إيقاف عضوية | Blacklist |
| 144 | Cover Charge | Cover Charges | رسم الدخول | رسم دخول | CoverCharge |
| 145 | User Access | User Access / Rights | صلاحيات المستخدم | الصلاحيات | UserAccess |
| 146 | Menu Access | User Menu Access | صلاحيات القوائم | صلاحيات القوائم | MenuAccess |
| 147 | Caption | Changing Caption | تسمية الحقل | تسمية مخصصة | Caption |

---

## قواعد القاموس

1. **عربي أولاً في كل UI** — المصطلح الإنجليزي لا يظهر للمستخدم النهائي إلا عند غياب مقابل عربي متفق عليه (يُراجع ويُستبدل).
2. **وحدة السياق:** بعض المصطلحات تتعدد معانيها بالسياق (Posting = ترحيل محاسبي/شحنة فندقية) — يُثبت المعنى بالسياق في شاشاته.
3. **إضافات لاحقة:** كل مصطلح جديد يُسجل أولاً هنا قبل استخدامه في أي Screen Spec أو API أو DocType.
4. **العربية الفصحى المهنية:** تجنب العامية؛ مصطلحات قطاع الضيافة السعودية/الخليجية المعتمدة (نزيل، إشغال، تدقيق ليلي) مقدمة على غيرها.
