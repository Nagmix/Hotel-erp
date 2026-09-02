# PHASE 0 — جرد الوحدات (Module Inventory)

> **نطاق الوثيقة:** الوحدات الوظيفية المكتشفة في FortuneNext 6i بناءً على فهرسة الملفات الـ 65 وفهارسها الداخلية.
> **الترتيب:** حسب الأهمية المعمارية ثم حجم الوثائق.

---

## 1. خريطة الوحدات الكاملة

| # | الوحدة (EN) | الوحدة (AR) | الكود | وثائق | صفحات | الأهمية في المعمارية |
|---|---|---|---|---|---|---|
| 1 | Front Office | مكتب الاستقبال | FOM | 11 | 747 | **القلب الفندقي (PMS Core)** — الحجوزات، الوصول، الإقامة، الفوليو، الكاشير، Night Audit |
| 2 | Point of Sale | نقاط البيع | POS | 4 | 350 | مبيعات المطاعم/المنافذ + KOT + تسويات + ربط بفوليو النزيل |
| 3 | Materials Management | إدارة المواد | MGT | 4 | 293 | دورة المشتريات الكاملة + المخازن + الاستلام والإصدار |
| 4 | Banquets | الولائم | BNQ | 5 | 255 | حجز قاعات المناسبات + المتطلبات + التسعير المسبق + الفوترة |
| 5 | HR & Payroll | الموارد البشرية والرواتب | HRP | 4 | 253 | التوظيف + الحضور + الرواتب + ترحيل القيود للمالية |
| 6 | Financial Management | الإدارة المالية | FAS | 5 | 218 | **المحور المحاسبي (GL Hub)** — يستقبل ترحيلات من جميع الوحدات |
| 7 | Care (Fortune Care) | خدمة الضيافة والمهام | — | 3 | 187 | إدارة مهام/شكاوى الضيوف + الروستر + إنتاجية الموظفين + SMS |
| 8 | Membership | العضويات | MEM | 5 | 133 | دورة عضوية كاملة (طلب→فحص→موافقة→تجديد→إلغاء) + فوترة |
| 9 | System Setup | إعداد النظام | SYS | 1 | 110 | المستخدمون + الصلاحيات + قاعدة البيانات + إعدادات عامة |
| 10 | Sales & Marketing | المبيعات والتسويق | SLM | 4 | 103 | ملفات الشركات + العقود والأسعار + تتبع المبيعات + التنبؤ |
| 11 | Accounts Receivable | الحسابات المدينة | ACR | 5 | 89 | أرصدة الشركات/الوكالات + الفوترة الدورية + التحصيل + التقادم |
| 12 | Telephones | الهاتف | TEL | 4 | 83 | محاسبة المكالمات + ترحيل إيراد المكالمات لفوليو النزيل |
| 13 | Maintenance | الصيانة | MNT | 3 | 81 | شكاوى الصيانة + أوامر العمل + الصيانة الوقائية + المعدات |
| 14 | F&B Costing | تكاليف الأغذية والمشروبات | FNB | 4 | 76 | وصفات + مخزون المطابخ + التكلفة المعيارية مقابل الفعلية |
| 15 | Fixed Assets | الأصول الثابتة | FXD | 1 | 25 | الأصول + الإهلاك + ترحيل الإهلاك للمالية |
| 16 | Gate Passes | تصاريح البوابة | GTP | 1 | 13 | ضبط حركة المواد داخل/خارج الفندق |
| 17 | Touch Screen | شاشة اللمس | TSC | 1 | 46 | واجهة POS اللمسية (مرجع UX سلوكي) |

---

## 2. تفكيك كل وحدة (Sub-modules)

### 2.1 Front Office (FOM) — 11 وثيقة

| الوثيقة | الوظيفة الفرعية | الموضوعات الأساسية |
|---|---|---|
| RES | الحجوزات | إنشاء/تعديل/إلغاء الحجز، حجز بنوع الغرفة، Room Rack Console، تخصيص غرفة، حجز الشركات/المجموعات |
| REG | تسجيل الوصول | Express Check In، Check-in من حجز، Walk-ins، Special Rooms، Room Floor Plan، Room Transfer، Amend Stay |
| CAS | الكاشير | Post Charges، Deposits، Paid Outs، Allowances، Check Out، Folio، تسويات، الترحيل للحسابات |
| DEP | **إقفال اليوم (Night Audit)** | Create Guest Balance، Create Night Balance، Cancel Night Audit، Consolidated Entry، Open New Date |
| HSK | الإشراف الفندقي | حالات الغرف، تنظيف، الغسيل (Laundry)، جداول الموظفين، حجب الغرف |
| GST | سجل النزلاء | Guest Master، تفضيلات، شكاوى، تاريخ الزيارات، قوائم أعياد الميلاد |
| LUK | الاستعلامات | Hotel Position، Room Status، Expected Arrivals، Waitlist، InHouse Statistics، Rev. Management Tool |
| REP | التقارير | 120 صفحة تقارير تشغيلية وإيرادية |
| SET | الإعدادات | Room Types، Room Master، Rate Master، Tax Structures، Meal Plans، Package Elements، Company Types، Business Sources |
| CRG | الكونسيرج | Left Luggage، Parcels، Ticket Request، Valet Parking، Baggage Tickets |
| SMS | الرسائل النصية | Mobile Master، Service Definition، تنبيهات المغادرة للأقسام |

### 2.2 Point of Sale (POS) — 4 وثائق

| الوثيقة | الوظيفة الفرعية | الموضوعات الأساسية |
|---|---|---|
| SET | الإعدادات | Outlets، Sessions، Order Types، Currencies، Menu Groups/Levels، Servers، Departments for NC |
| GST | سجل النزلاء | Guest Master بمستوى POS + Loyalty Cards + تفضيلات |
| LUK | الاستعلامات | Pending KOTs، Pending Bills، Table Booking Status، Settlement Summary، Session Statistics |
| REP | التقارير | Sales By Item/Group/Date/Shift، Sales Daybook، Daily Sales، Consolidated Sales (158 صفحة!) |

### 2.3 Financial Management (FAS) — المحور المحاسبي

| الوثيقة | الوظيفة | الموضوعات الأساسية |
|---|---|---|
| SET | الإعدادات | **Main Heads / Sub Heads (مستويات دليل الحسابات)**، Transaction Types، Voucher Link، **روابط الترحيل من كل الوحدات** |
| MST | البيانات الرئيسية | Financial Account Master، Statistics Master، Cheque Book Master |
| TRN | المعاملات | قيود، تسوية بنكية، موازنات، Interactive Payment، TDS، Voucher Authorization، فتح السنة المالية |
| LUK | الاستعلامات | Ledger Balance، Day Book، Trial Balance، P&L، Balance Sheet، Cash Flow |
| REP | التقارير | 64 صفحة تقارير مالية |

> ⚠️ **اكتشاف جوهري (من FAS-SET):** وثيقة إعدادات المالية تحتوي على روابط تكامل صريحة:
> **FO to Finance Link • POS to Finance Link • MM to Finance Link • Payroll to FAS Link • Membership to FAS Link • Link AR to Finance**
> هذه هي نقاط التكامل المعمارية الموثقة بين الوحدات التشغيلية والمحور المحاسبي — يجب تحليلها بدقة في Phase 6.

### 2.4 Materials Management (MGT)

| الوثيقة | الوظيفة | الموضوعات الأساسية |
|---|---|---|
| SET | الإعدادات | Stores، Item Groups، Inventory Master، Vendor Master، Terms of Payment، Vendor Rating |
| DNT | القيود اليومية | Purchase Requisition، Indent، PO، Standing PO، Service Work Order، Quotation Analysis، Re-Order، Inter Store Transfer |
| LUK | الاستعلامات | حالة الطلبات/أوامر الشراء/الاستلام والإصدار |
| REP | التقارير | سجلات الاستلام، حركة المخزون، تقارير الموردين |

### 2.5 باقي الوحدات (ملخص)

- **Banquets (BNQ):** BOK (الحجز) + CFG (تهيئة القاعات والقوائم) + BIL (الفوترة والتسويات والودائع) + SET + LUK
- **Membership (MEM):** MPF (الطلبات والفحص) + MMN (التجديد/الإنهاء) + MTR (الإيصالات والفوترة و**ترحيل الاشتراكات إلى AR**) + SET + RPL
- **HR & Payroll (HRP):** RQP (التوظيف) + SET (التعريفات) + PNT (الحضور والرواتب) + REP (تقارير الموظفين والرواتب)
- **Maintenance (MNT):** SET (المواقع/المعدات/المهارات) + OPR (الشكاوى/أوامر العمل/الصيانة الوقائية) + RPL
- **F&B Costing (FNB):** SET (الوصفات والموازنات) + COP (استخراج التكاليف، مخزون المطابخ، الاستهلاك، Auto Indent) + LUK + REP
- **Sales & Marketing (SLM):** PRF (ملفات الشركات والعقود والأسعار) + SLT (تتبع المبيعات والتنبؤ والموازنات) + LUK + REP
- **Care:** SETUP (الهيكل التنظيمي والمستخدمون) + OPERATIONS (الروستر، المهام/الشكاوى، Lost & Found) + REPORTS
- **Telephones (TEL):** SET (الامتدادات، شرائح الوقت/الأسعار، **Telephone Revenue Posting**) + CAC (محاسبة المكالمات) + LUK + REP
- **Fixed Assets (FXD):** الأصول + الإهلاك + **ترحيل الإهلاك للمالية (FI Depr Posting to FA)**
- **Gate Passes (GTP):** إصدار/استلام/استعلام تصاريح البوابة
- **System Setup (SYS):** المستخدمون، الصلاحيات، DBs (PMS/Training)، إعدادات عامة

---

## 3. الوحدات غير الموجودة في الكتالوج (استنتاج أولي)

> [INFERENCE] بناءً على غياب أدلة مستقلة لها — يُستكمل في Phase 2 عند القراءة الفعلية:

- **Night Audit** كم وحدة مستقلة — موجودة داخل Front Office (وثيقة DEP) وليست وحدة منفصلة.
- **Conference & Banqueting Sales** — مغطاة ضمن Banquets.
- **Spa / Golf /_activities** — غير ظاهرة كوحدات مستقلة.
- **Revenue Management** — يظهر "Rev. Management Tool" في FOM-LUK فقط (استعلام، لا وحدة كاملة).
- **Central Reservations / GDS / OTA integrations** — لم يظهر دليل مستقل حتى الآن؛ بانتظار التحقق من محتوى FOM-RES وSLM.

---

## 4. تبعيات أولية بين الوحدات (من فهارس الوثائق فقط — تُدقق في Phase 5/6)

```
SLM (عقود/أسعار الشركات)
  └─→ FOM-RES (الحجوزات بأسعار الشركات)
        └─→ FOM-REG (الوصول) ─→ FOM-CAS (الفوليو والكاشير)
                                      │
FOM-HSK (حالة الغرفة) ←── FOM-REG     │
                                      ├──→ ACR (حسابات الشركات/الوكالات)
POS (مبيعات المنافذ) ──(room charge)──┤         │
                                      ├──→ FAS (الترحيل المحاسبي)
TEL (مكالمات) ──(posting)─────────────┤         ↑
BNQ ──(BIL)───────────────────────────┤    MEM-TRN (Post Subscription to AR)
MGT ──(MM to Finance Link)────────────┤
FNB ──(Costing Link + Auto Indent)──→ MGT
HRP ──(Payroll to FAS Link)──────────→ FAS
FXD ──(Depr. Posting)───────────────→ FAS
Care ──(task engine + SMS) ──(يدعم جميع الأقسام)
```

> **قاعدة:** هذه العلاقات مستخرجة من عناوين موثقة في فهارس الوثائق، ولم يُتحقق من تفاصيلها الحقلية بعد.

---

## 5. أولويات التحليل المقترحة (Risk-based)

1. **P0 — Front Office كاملاً** (747 صفحة): هو نواة PMS وكل شيء يتفرع منه.
2. **P0 — Financial Management SET/TRN**: يحدد قواعد الترحيل لكل الوحدات.
3. **P1 — POS + ACR**: حلقة الإيراد والتحصيل.
4. **P1 — Materials Management + FNB**: دورة التكلفة والمخزون.
5. **P2 — BNQ, MEM, HRP, MNT, Care, TEL, SLM, FXD, GTP, SYS**.
