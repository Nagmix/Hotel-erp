# 01 — البيانات الرئيسية (Master Data) — وحدة SLM

> **الجرد الكامل للكيانات الرئيسية الموثقة في الوحدة** — مصدرها الوحيد الأدلة الأربعة. SLM تملك **مستودعي عملاء** (Prospects منفصل عن Company Master!) + ماسترات شخصية (مبيعات/تحصيل) + ماسترات وكلاء ثلاثية + ماستر خصومات إيراد.

---

## 1. كيانات العملاء (المستودعان)

### 1.1 Prospect (الشركة المحتملة) — SLT §4

| الحقل | الوصف الموثق |
|---|---|
| Company Name | اسم الشركة (F1 لقائمة الشركات — يُستخرج من Company Master!) |
| CEO | "Enter the name of the CEO of the company selected" |
| Classification | "Tag the applicable classification" |
| Address | تفاصيل العنوان |
| Holding Company | "Enter the holding company's name" |
| Sales Executive | "Press F1 to get the list of sales team" — المسؤول عن العمل |
| Turnover | "a rough turn over amount of the company" |
| Main Business | النشاط الرئيسي |
| Competitors | "the defined competitors for this business" — حقل تنافسي داخل ماستر العميل! |
| Remarks | ملاحظات مستقبلية |
| Contact Details | قسم جهات الاتصال |
| Frequent Travelers | "Click to enter details of the **Frequent Traveler from the Company**" — مسافرون دائمون من الشركة |

> **دلالة معمارية:** حقل Competitors داخل ماستر العميل يجعل تقارير Market Share/الخسائر قابلة للربط التنافسي من نفس المستودع.

### 1.2 Company Profile (شركة CGR / ضيف) — PRF §7 — **كيان AR المشترك**

**الحزمة الأساسية:**

| الحقل | الوصف الموثق |
|---|---|
| Company Code | **7 خانات alphanumeric: أول 3 = النوع (من Company Types تحت FO Setup!) + 4 حر** |
| Company Name | اسم الضيف/الشركة |
| Chief Executive Title/Name | المدير التنفيذي ولقبه |
| Classification | "system-defined classifications to identify the type of account" |
| Watch List + To Date | Yes/No + تاريخ — "room occupancy and business received information... up to a specified date" |
| Holding Company | "the owning company or that has a majority stake" |
| Address / PAN # / City / State / Country / Zip | العنوان القانوني والضريبي |
| Phone # / Fax # / IATA # | هواتف + رقم IATA (وكالات السفر!) |
| Email / Web | البريد والموقع |
| Sales Office | مكتب المبيعات الذي "has finalized the deal" |
| Sales Executive | المندوب الذي أبرم الصفقة |
| Bill Inst | "billing instruction as required by the guest/company" (من Billing Instructions) |
| Mar Seg | Market Segment |
| Default Amenities | "amenities that the property has agreed to provide" |
| Remarks | ملاحظات |
| Black Listed | Yes → **reason + name of authorizer** (التفاصيل تُعرض في Modify mode فقط) |

**الحزمة المالية (AR Details) — PRF ص13:**

| الحقل | الوصف الموثق |
|---|---|
| Bypass Invoice | Yes/No — "if you want to generate an invoice to the account" |
| Allow Credit | Yes/No — السماح بتقييد التسوية الائتمانية |
| Credit Days | عدد أيام الائتمان (مشروط بـAllow Credit = Yes) |
| Invoice Currency | "currency in which the AR invoices has to be printed" |
| Interest % | "percentage of interest applicable on bills **that exceed the specified credit days**" |
| Credit Limit | مبلغ — **تجاوزه يمنع تسوية FO/POS/BNQ أو الترحيل اليدوي!** |
| Commission % | "normally applicable to travel companies or agents and credit card companies" |
| Collection Executive | "responsible to track and collect amounts receivable" |
| Billing Details/Address | "reflected in the invoice or reminder printouts for mailing" |

**حزم فرعية:** Bookers (Type/Code/Name) · Contacts (Title/Name/Designation/DOB/Anniversary/Email/Mobile/Tel Extn) · **Revenue Discount Link** (ربط ماستر خصم بحساب العميل — "percentage of discount applicable against the respective revenue heads").

### 1.3 Bookers Master — PRF §4

| الحقل | الوصف |
|---|---|
| Bookers Type | من "Bookers Type Definition **under Front Office Setup**" |
| Bookers Code | كود الحاجز |
| Name / Address / PAN # / Tel # | بيانات الاتصال |

> Bookers Type نفسه ماستر FO مشترك (كما Sales Executives/Offices/Collection Execs — كلها "refer ... under Front Office Setup" — انظر §5).

## 2. كيانات هيكل المبيعات

| الكيان | الحقول الموثقة | المصدر |
|---|---|---|
| **Sales Office** | (ماستر FO مشترك — "For more information, refer Sales Office **under Front Office Setup**") | PRF §1 |
| **Sales Executive** | (ماستر FO مشترك — "tagged to a company... responsible for all kinds of sales happening at the property from their respective companies") | PRF §2 |
| **Collection Executive** | كود + ربط بشركات في company master — "handle the revenue collection from companies who owe money" | PRF §3 |
| **Map Users/Sales Exec** | Sales Executive ↔ User ID (من User Setup تحت SYS) — "facilitates the usage of the **Executive Planner**" | PRF §16 |
| **Sales Call Types** | Code + Description — أمثلة موثقة: **Rate Negotiations / Casual Calls / Service Related calls** — "tagged as Reason in the Daily Sales Call Entry" | PRF §15 |
| **Hotel Amenities** | Amenities Code + Name — "non-chargeable facilities... Airport Pick-up, Drop to Airport, a welcome drink, fruit basket" | PRF §6 |

## 3. كيانات الخصومات والأسعار

### 3.1 Revenue Discount Master — PRF §5

| الحقل | الوصف الموثق |
|---|---|
| Active Date | "current date or a date greater than the current date to activate" — صيغة ddmmyy |
| Discount ID | "numeric values of character length up to **4**" |
| Description | يظهر "in many transactions, hence enter valid discount description" |
| Expiry Date | تاريخ انتهاء الصلاحية |
| % (لكل Revenue Code) | نسبة الخصم لكل رأس إيراد في الشبكة |
| Menu-Type % (F&B فقط) | **FOOD / LIQUOR / SOFTDRINKS / TOBACCO / OTHERS** — "individual percentage discount for each menu type" |

> **قاعدة استهلاك مزدوجة موثقة:** "Discount codes are tagged during **reservations/Registrations**" + "applicable during the generation of **Bills in F&B outlets** and various transaction entries" — الخصم يُعرّف هنا ويُنفذ في FO/POS.

### 3.2 Rate Links (شاشات مرجعية) — PRF §9 / LUK

- **Link Rates to Company:** Company + Non-rack Rate Structure + خيار **Include/Exclude tax for tariff** + Package Rates link + Amenities — "The room and plan rates are displayed in the table based on the type of occupancy: single, double, triple... for a particular Room type, plan code and for a particular type of currency".
- **Room Rate Master–Help** (LUK §6): "rate applicability, plan type and Currency details".
- **Company Package Rates** (LUK §5): "rates are displayed day wise for occupancy type, **extra adult and child pax**".

## 4. كيانات سياسات الحجز (تُستهلك في FO)

| الكيان | الحقول الموثقة | الاستهلاك |
|---|---|---|
| **Retention Policy** (PRF §10) | Company + Property + Room Type + **% Retention Charge** ("Percentage of Room rate agreed by the Hotel to the Company") | "charged to the company by using **Retention-Cancel/No show option under front office**" |
| **Cancellation Policy** (PRF §11) | Company + Property + Room Type + **From Day/To Day + Cancellation %** | "compare the number of days in respect to the cancellation date prior to arrival date and levy the charges" |

## 5. كيانات الوكلاء (ثلاثية التوزيع)

### 5.1 Agent Allocation — PRF §12

| الحقل | الوصف الموثق |
|---|---|
| Date Range | "By default, the **Accounting date will be picked as From Date** and can be edited" |
| Company / Property / Room Type | مفاتيح التخصيص |
| Rooms Allocated | عدد الغرف للوكيل |
| Over-Book % | "percentage of rooms that can be booked **above and over** the number of rooms allocated" |
| Confirmation Days | "days before which the company or the travel agent has to confirm the booking... with respect to **reserved date or arrival date**" |
| Week Access | "dependent on the **Module Attribute # 8 for Reservations**: NO → week access screen (rooms allocated to the days selected) · YES → day access screen (rooms day wise)" |

### 5.2 Agent Forecast — PRF §13
Date Range + Company + Property + Room Type + **Total rooms forecasted** — "tentative bookings... **may be considered as confirmed**" + قاعدة: "Forecast information... **should match with the allocation information created for the same company**".

### 5.3 Agent Release Dates — PRF §14
"**multiple Cutoff days** as per the need within the allocated period" — "From date is auto generated based on the start date" — الاستهلاك: "the reservation program prompts you to assign the rooms requested as **Inside or Outside allocation**" — تفعيله بـ**INI #41 = '0'**!

## 6. Hotel Profile (الماستر التسويقي الشامل) — PRF §17

| الحقل/الكتلة | الوصف الموثق |
|---|---|
| Hotel Code | "alphanumeric values of character length up to **three**" |
| Name / Owner / Address / Group / Classification | الهوية والعنوان |
| **HODs** | Designation + Name + Residence # + Mobile # + Pager # |
| **Outlets** | name, Capacity, **Dress Code, Smoking permissions**, Time, **Minimum Cover Charge, Chef**, Specialty, View, Remarks |
| **Rooms** | Room Type + وصف + total rooms + View + Amenities + **rates: seasonal and Off Seasonal tariff for Single/Double** |
| **Banquets** | venue name + capacity + **sq/ft area** + special attributes |
| **CGR Details** | "CGR (Common Guaranteed Rates) details for a Company" + Amenities |
| **VIP Visits** | Guest name + arrival/departure + room # + Comments |
| **Picnic Spots** | name + main attractions + distance KMS + mode of transportation + travel time + total charges |
| **Hotel Picture** | "**You can upload only bmp files**" |
| **General Info** | avg min/max temperature + مسافات/أجرة (bus stand/railway/airport/other) + landmark + general information |

> **النطاق المزدوج:** "default Hotel and **groups of hotels within the Property or any other Hotel(s) information on which a comparative study has to be done**. The information recorded here is used **across all modules**" — يشمل فنادق المنافسين (لمدة Market Share).

## 7. كيانات التتبع التشغيلي (بيانات مصدرية للتقارير)

| الكيان | الحقول | المصدر |
|---|---|---|
| Daily Occupancy (تاريخي) | Date + Property + total rooms + % occupancy + **Average Room Revenue** + room-type-wise breakup | SLT §1 |
| F&B Promotion | From/To + Property + Outlet + purpose/event + sponsor + **avg rate per Pax** + total amount + benefits + remarks | SLT §2 |
| Company Budget | Company (Range/Type) + budget period + classification (**revenue/room nights**) + Room Nights expected + anticipated revenue + remarks + **multiple periods** | SLT §3 |
| Daily Sales Call | Date + Time + Sales Executive + Account (مع checkbox CGR) + Contact Name/Designation + **Activity Type (Hotel Visit/Tele Called)** + Notes + More info + **follow-up date/time** | SLT §6 |
| Entertainment/Gift | Sales Executive + Account + Contact + **Type: Entertainment (→Type/Outlet/Session) أو Gift (شاشة هدايا)** + Place (خارج الفندق) + Date + Amount + **Authorizer** | SLT §7 |
| Business Loss | Company (بحث) + date lost + **competitor** + reason + remarks | SLT §8 |
| Executive Planner — Appointments | Time + contact person + Designation + Notes + (فرز Company Name/zip/City/State) + إجراءات reschedule/cancel/**transfer** | SLT §9 |
| Executive Planner — Things To Do | **hourly 7am–8pm** + تصنيف **Important/Normal** + tag completed + view not-completed | SLT §9 |

## 8. خلاصة النمذجة

- **15+ كيان ماستري** منها 3 مشتركة مع FO (Sales Office/Execs/Collection Execs) + 1 كيان AR مركزي (Company Profile).
- نمط **"مستودعان للعملاء"**: Prospects (سوق) وCompany Master (عقد) — بجسر تحويل مشروط.
- كيانان تنافسيان فريدان: **Competitors داخل Prospect** + **فنادق المنافسين داخل Hotel Profile**.
- حقول شخصية غنية: DOB/Anniversary (لجهات الاتصال — وقود تقارير Birthday/Anniversary!) + Pager # (عصر التقنية!).
