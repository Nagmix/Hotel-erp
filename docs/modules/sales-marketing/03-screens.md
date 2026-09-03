# 03 — الشاشات (Screens) — وحدة SLM

> **جرد الشاشات الموثقة (52 وظيفة → ~60 شاشة مع النوافذ الفرعية)** — الترقيم S-SM-xx. النمط العام: شاشات إدخال كلاسيكية بـF1/double-click lookups + شاشة تسجيل دخول مستقلة للمخطط التنفيذي (الوحيدة بكلمة مرور!).

---

## 1. شاشات Sales Tracking (SLT) — 10 وظائف

| ID | الشاشة | العناصر الموثقة | المصدر |
|---|---|---|---|
| S-SM-01 | Daily Occupancy Entry | Date · Property (F1) · total rooms · % occupancy · Average Room Revenue · **زر breakup حسب نوع الغرفة** · Save/Back | SLT §1 |
| S-SM-02 | F&B Promotion Entry | From/To · Property (F1) · **Outlet (F1)** · purpose/event name · sponsor · **avg rate per Pax** · total amount · benefits · remarks | SLT §2 |
| S-SM-03 | Company Budgets | اختيار **Company Range/Company Type** → قائمة شركات → شاشة فرعية: budget period (مدى تواريخ) · classification · Room Nights expected · anticipated revenue · remarks · **زر multi-period** | SLT §3 |
| S-SM-04 | Prospect Entry | Company (F1) · CEO · classification · address · holding company · **Sales Executive (F1 — قائمة فريق المبيعات)** · turnover · main business · **competitors** · remarks · contacts · **زر Frequent Traveler** | SLT §4 |
| S-SM-05 | **Sales Manager Tool (360°)** | Company (double-click) → Company Name/CEO/type للقراءة + أزرار Add/Edit Company (تحوّل لـCompany Profile تحت AR!) + **10 عروض تبويبية** (انظر S-SM-06..15) | SLT §5 |
| S-SM-06 | — General Information | "You **cannot modify any fields**. The information displayed here are entered during prospect entry creation" — قراءة فقط | SLT ص10 |
| S-SM-07 | — Sales Activity | "from the **previous month**" افتراضياً + زر New Entry (→ Daily Sales Call) | SLT ص11 |
| S-SM-08 | — Entertainment | Entertainment/Gift Entries للشركة + زر New Entry (→ Entertainment/Gift) | SLT ص11 |
| S-SM-09 | — Negotiated Rates | "the **CGR Rates** for Company selected with full details" | SLT ص11-12 |
| S-SM-10 | — Hotel Amenities | المرفقات المرتبطة + زر New Entry | SLT ص12 |
| S-SM-11 | — Reservations | حجوزات الشركة **لتاريخ المحاسبة** + Cancelled + No Show + **checkbox: Show Past Reservation** | SLT ص12 |
| S-SM-12 | — In-house Guests | كل نزلاء الشركة الحاليين | SLT ص12 |
| S-SM-13 | — Revenue | "month wise revenue earned from different revenue heads like **Tariff, Food, and Beverages**" | SLT ص13 |
| S-SM-14 | — Receivables | "opening balance, charges, payment, closing balance" + **"The cutoff date assumed for arriving at the balances is Accounting date"** | SLT ص13 |
| S-SM-15 | — Guest Visits | زيارات ضيوف الشركة لشهر (افتراضياً السابق) | SLT ص13 |
| S-SM-16 | — **Hotel Position** | "availability based on the room types" → نقر نوع الغرفة = **Hourly Position** → **Next day Chart** → Detailed Position → **Yearly position (مع خيار Over Booking!)** → double-click شهر = تفصيل الشهر | SLT ص14-16 |
| S-SM-17 | Daily Sales Call | Date · Time · Sales Executive · Account (F1 + **checkbox CGR**) · Contact Name/Designation · **Activity Type (Hotel Visit/Tele Called)** · Notes + زر More · **follow-up date/time** | SLT §6 |
| S-SM-18 | Entertainment/Gift Entry | Sales Executive (قائمة) · Account (F1) · Contact (F1) · **Type: Entertainment → (Entertainment Type/Outlet/Session) أو Gift → شاشة هدايا** · Place (خارج الفندق) · Date · Amount · **Authorizer** | SLT §7 |
| S-SM-19 | Business Loss Entry | Search Criteria (F1 شركات) → عرض Company/Sales Executive/Holding Company · date lost · **competitor** · reason · remarks | SLT §8 |
| S-SM-20 | **Executive Planner — Login** | "Enter the **user id and password**" — شاشة دخول مستقلة (الوحدة الوحيدة!) | SLT §9 |
| S-SM-21 | — Appointments | فرز Company Name/zip/City/State → شاشة Time/contact person/Designation/Notes + أزرار: **Details (شركة + مواعيد سابقة) · Reschedule (date/time/reason) · Cancel (reason) · Transfer (مندوب + reason)** | SLT §9 |
| S-SM-22 | — Things To Do | **شبكة ساعات 7am–8pm** · تصنيف **Important/Normal** · نقر وقت = إدخال مهمة · **tag completed** · زر عرض غير المكتمل | SLT §9 |
| S-SM-23 | — In-house Guest | "Guest information staying in the hotel as on current date" | SLT §9 |
| S-SM-24 | Transfer Prospects | قائمة كل Prospects بعمود **To Company Profile (No/Yes)** → double-click على No → شاشة توليد الكود: **"first three characters stand for type of company (COM/TAG/AIR)... The system checks the last serial number for the company type and automatically generates the next number"** → إدخال/تعديل New Company Code | SLT §10 |

## 2. شاشات Profiles (PRF) — 17 وظيفة

| ID | الشاشة | العناصر الموثقة | المصدر |
|---|---|---|---|
| S-SM-25 | Sales Office / Sales Executives / Collection Executives | **ثلاث شاشات FO مستضافة** — "For more information, refer... under Front Office Setup" | PRF §1-3 |
| S-SM-26 | Bookers Master | Bookers Type (lookup) · Bookers Code · Name/Address/PAN #/Tel # + Add/Modify | PRF §4 |
| S-SM-27 | Revenue Discount Master | Active Date (**ddmmyy**، ≥ اليوم) · Discount ID (**رقمي ≤4 خانات**) · description · Expiry Date · شبكة % لكل revenue code · **double-click على كود F&B = شاشة Menu Type (FOOD/LIQUOR/SOFTDRINKS/TOBACCO/OTHERS)** | PRF §5 |
| S-SM-28 | Hotel Amenities | Amenities Code (فريد) · Name | PRF §6 |
| S-SM-29 | **Company Profile** | الحزمة الكاملة (راجع 01 §1.2) + **5 شاشات فرعية**: Bookers · AR Details · Contacts · Revenue Discount Link (عمودان: قائمة ماسترات + ربط) · **Blacklist Details (Modify mode فقط!)** | PRF §7 |
| S-SM-30 | Update Company Profile | **Dropdown لاختيار ما يُحدَّث → Old Value (زر اختيار من قائمة) → New Value → Save** — أداة تحديث جماعي | PRF §8 |
| S-SM-31 | Link Rates to Company | Company (F1) → عرض Name/Tel/IATA · **Non-rack Rate Structure (F1)** → نافذة **Include/Exclude Tax** → **زر Package Rates** · Amenities (F1) → شبكة الأسعار **بالإشغال (single/double/triple) × Room type × plan × Currency** | PRF §9 |
| S-SM-32 | Retention Policy | Company (F1) + عرض البيانات · Property · Room Type (قائمة) · **% Retention Charge** | PRF §10 |
| S-SM-33 | Cancellation Policy | Company (F1) + عرض · Property · Room Type · **From Day/To Day + Cancellation %** | PRF §11 |
| S-SM-34 | Agent Allocation | **From Date (افتراضياً Accounting date، قابل للتحرير!)** · To Date · Company/Property/Room Type (F1) · rooms allocated · **Over-Book %** · Confirmation days (**reserved/arrival**) · **Week Access (أو Day Access حسب Module Attribute #8!)** | PRF §12 |
| S-SM-35 | Agent Forecast | Date range · Company/Property/Room Type · **total rooms forecasted** | PRF §13 |
| S-SM-36 | Agent Release Dates | اختيار Agent من شاشة Allocation → عرض التخصيص → **شاشة cutoff: تواريخ From مولدة تلقائياً + cutoff days لكل مدى** | PRF §14 |
| S-SM-37 | Sales Call Types | Code + Description | PRF §15 |
| S-SM-38 | Map Users/Sales Exec | **Sales Executive (قائمة معرفة تحت FO)** + **User Id (من User Setup تحت SYS)** | PRF §16 |
| S-SM-39 | **Hotel Profile** | 10 كتل (راجع 01 §6): HODs · Outlets · Rooms (+Rates: **seasonal/Off-Seasonal × Single/Double**) · Banquets · CGR · VIP · Picnic Spots · **Picture (BMP فقط — زر Browse/Upload)** · General Info (حرارة/مسافات/أجرة/landmark) | PRF §17 |

## 3. شاشات التقارير (REP) — 19 تقريراً

> كل التقاير بنمط واحد: شاشة معايير → **"Select one of the report output options (Display, Spool, Print or Export)"** + Cancel. المعايير المميزة موثقة في 08-reports.

## 4. شاشات الاستعلامات (LUK) — 6 استعلامات

| ID | الشاشة | العناصر | المصدر |
|---|---|---|---|
| S-SM-40 | Browse Company | "selective criteria such as **Watch List, Holding Company, Sales Executive**..." + **Credit Limit range** (شاشة فرعية: From/To → قائمة الشركات ضمن المدى!) | LUK §1 |
| S-SM-41 | View Rate Structures | Date → عرض rack/non-rack · Property/Room Type/Plan/Currency · **عند non-rack: زر Company = الشركات المرتبطة بالبنية** | LUK §2 |
| S-SM-42 | Company Rates — Datewise | Property · Company · Date · Room Type/Plan/Currency · **Rate Type: Non Rack أو Package** → "tariff chart... highlighting in multiple currency... Discount applicable, if any, is also reflected" + أزرار Browse (Room/Plan/Currency/Company) | LUK §3 |
| S-SM-43 | Browse Hotel Profile | "This information can be **browsed from Room Booking screen**!" — افتراضياً أول فندق + زر Clear + اختيار Property | LUK §4 |
| S-SM-44 | Company Package Rates | Property · Company (F1) · **Package # (F1)** → "rates and other details... day wise for occupancy type, **extra adult and child pax**" | LUK §5 |
| S-SM-45 | Company Rates (Query) | **Search By: Company Name/Company Code** → Enter → Rate ID + description → **Room Rate Master – Help** ("rate applicability, plan type and Currency") → double-click = أسعار أنواع الغرف | LUK §6 |

## 5. جرد عناصر UI المميزة

- **شاشة دخول بكلمة مرور** واحدة (Executive Planner) — تعتمد ربط Map Users/Sales Exec.
- **شبكة ساعات 7am–8pm** (Things To Do) — نمط تقويم يومي فريد في المشروع.
- **قائمة فرز رباعية** في Appointments: Company Name/zip/City/State.
- **عمود تحويل قابل للنقر** (To Company Profile: No → double-click = شاشة التحويل).
- **5 شاشات فرعية** خلف Company Profile (أغنى زر drill-in بعد Guest Profile في FO!).
- **ملاحظة نصية خام في الدليل:** LUK ص9 يتضمن "**BELOW SCREENSHOTS ARE REQUIRED**" — أثر توثيقي أصلي (GAP-SM-D05).

**إجمالي: ~60 شاشة/نافذة موثقة (24 SLT + 15 PRF + 19 REP + 6 LUK) مع 4 قوائم رئيسية.**
