# 01 — البيانات الرئيسية (Master Data) — وحدة ACR

> المرجع: ACR-SET §2 (ص2-8) و§5 (ص10-17) + ACR-OPR §1 (ص2-4). Company Profile هو **Master مشترك عبر 7 وحدات** — يُوثَّق هنا من منظور AR (مرجع التخصيص الأساس).

---

## 1. Company Profile (الملف المركزي للذمم)

> "You can record vital and detailed information of existing and prospective customers of the property... Information recorded here is used in Front Desk, Sales & Marketing, Point of Sale, Accounts Receivables, Banquets, Conferencing and Membership modules" (ACR-SET §5 ص10-11). أنشئه من S&M حرفياً: "using the **Company Profile option under Sales & Marketing**" (ACR-SET §2 ص2) — أي أن الدخول من ACR-SET §5 يفتح نفس الملف.

### 1.1 هوية الكود (بنية مركبة!)

| الحقل | القاعدة الموثقة | المصدر |
|---|---|---|
| Company Code | **حتى 7 خانات alphanumeric**؛ **أول 3 خانات = نوع الشركة** معرَّف مسبقاً في FO Setup → Company Types؛ **الأربع التالية** حرة alphanumeric | ACR-SET §5 ص11 |
| Company Name | نص حر | ACR-SET §5 ص11 |
| Chief Executive (Title/Name) | عنوان واسم المدير التنفيذي | ACR-SET §5 ص11 |
| Classification | قائمة نظامية تحدد نوع الحساب | ACR-SET §5 ص11 |

**دلالة معيارية:** الكود = `TTTXXXX` (TTT: Company Type prefix) — إيجاد النوع من الكود نفسه دون استعلام. في ERPNext: يُعادل `customer_group` مع كود مركب.

### 1.2 الحقول التعريفية والتشغيلية

| الحقل | الدلالة | المصدر |
|---|---|---|
| Watch List / To Date | Yes/No + تاريخ — "room occupancy and business received information of a guest/company account up to a specified date" — يُستهلك في تقرير Watch List Companies تحت S&M | ACR-SET §5 ص11-12 |
| Holding Company | الشركة الأم/مالكة الحصة الأغلبية للحساب | ACR-SET §5 ص12 |
| Pan # | رقم البطاقة الضريبية للشركة | ACR-SET §12 → ص12 |
| Address / City / State / Country / Zip | العنوان البريدي الكامل | ACR-SET §5 ص12 |
| Phone # / Fax # / IATA # | هاتف/فاكس/رمز IATA (للوكلاء) | ACR-SET §5 ص12 |
| Email / Web | البريد والموقع | ACR-SET §5 ص12 |
| Sales Office | مكتب المبيعات الذي أبرم الصفقة (F1 lookup) | ACR-SET §5 ص12 |
| Sales Executive | منفّذ الصفقة (F1 lookup) | ACR-SET §5 ص12 |
| Bill Inst | تعليمات الفوترة (F1 lookup) | ACR-SET §5 ص12 |
| Mar Seg | Market Segment (F1 lookup) | ACR-SET §5 ص12 |
| Default Amenities | مرافق افتراضية متفق عليها مع العميل (F1) | ACR-SET §5 ص12 |
| Remarks | ملاحظات | ACR-SET §5 ص12 |

### 1.3 قائمة السوداء (Black Listed)

- اختيار Yes ⇒ **إلزامي** إدخال **السبب + اسم المجيز** (شاشة فرعية) (ACR-SET §5 ص12).
- عرض التفاصيل: زار Black List متاح **فقط في وضع Modify** (ACR-SET §5 ص16).

### 1.4 Bookers (شاشة فرعية)

| الحقل | الوصف | المصدر |
|---|---|---|
| Bookers Type | نوع الوسيط (F1 lookup) | ACR-SET §5 ص12-13 |
| Bookers Code | كود الوسيط (F1 lookup) | ACR-SET §5 ص13 |
| Name | معروض تلقائياً | ACR-SET §5 ص13 |

### 1.5 تبويب تفاصيل AR (نواة وحدة الذمم) — ACR-SET §5 ص13-14

| الحقل | القاعدة | المصدر |
|---|---|---|
| **Bypass Invoice** | Yes/No — توليد فاتورة للحساب أم لا | ص13 |
| **Allow Credit** | Yes/No — السماح بتسوية الفواتير ائتماناً | ص13 |
| **Credit Days** | عدد أيام الائتمان (إلزامي إذا Allow Credit = Yes) | ص13 |
| **Invoice Currency** | عملة طباعة فواتير AR | ص13 |
| **Interest %** | فائدة على الفواتير المتجاوزة لمدة الائتمان | ص13 |
| **Credit Limit** | "If the current bill and/or the amount receivable exceed the specified credit limit, **settlement of the Front Desk, Point of Sale or Banquet bill or manual posting of the bill is not allowed**" | ص14 |
| **Commission %** | عمولة (وكلاء سفر/بطاقات ائتمان) | ص14 |
| **Collection Executive** | مسؤول التحصيل (F1 lookup) | ص14 |
| Billing Details/Address | عنوان الفوترة — يظهر في Invoice/Reminder | ص14 |

### 1.6 تبويب جهات الاتصال — ACR-SET §5 ص14-15

Title · Name · Designation (F1) · Date of Birth · Anniversary Date · Email · Mobile # · Tel Extn — يمكن إضافة عدة جهات اتصال (زر Add في Debtors Follow-Up CRT ص6).

### 1.7 ربط Revenue Discount Master — ACR-SET §5 ص15-16

- "link a revenue discount master to a customer account... indicate the **percentage of discount applicable against the respective revenue heads**".
- آلية: قائمة معرَّفة مسبقاً (F1) → اختيار Master واحد → Confirm. **العلاقة: Company (N) — (1) Revenue Discount Master**.

## 2. AR Opening Balance (بيانات افتتاحية إصدارية) — ACR-SET §2

| العنصر | القاعدة | المصدر |
|---|---|---|
| نوع القيد | Debit (فاتورة) / Credit (نقد/شيك/بطاقة) / Adjustment — **بنفس بنية Transaction Entry** | ص2-7 |
| أساس التسجيل | "Bill Number/Date or consolidated outstanding balance" — **التوصية النصية: بالفاتورة** ("subsequent payments... can be matched based on the selection of Bills") | ص2 |
| شرط مسبق | تسجيل Company Profile أولاً + **Module Attribute #3 = YES** | ص3 |
| Doc # | يولَّد تلقائياً بعد الحفظ | ص4 |
| حقول الفاتورة | Bill #/Date · Currency · Exchange Rate · Amount · Value (محلي) · Receipt#/Date · Commission %/Amount · Net | ص4-5 |
| حقول الشيك | Bank Name/Branch (F1) · Cheque #/Date · Location (F1) · Local/Outstation | ص5-6 |
| حقول البطاقة | Company (F1) · Card Type (F1) · CC # · Authorization # | ص6 |
| القفل | "Once the Statement of Accounts is processed for the start month of ACR operation, you will not be allowed to enter the outstanding balances" — الحل: Rollback SOA → تعديل → إعادة المعالجة | ص3 |
| التعديل | شاشة Modify بمعايير بحث: Doc # / Company / Company Name / Bill # / Bill Date / Receipt # | ص6-8 |

## 3. تعريف Aging — ACR-SET §3 ص8-9

| العنصر | القاعدة |
|---|---|
| النوع | **Receivable** (من قائمة Type) |
| تاريخ السريان | "current date or a date greater than the current date to activate the setting" |
| البنية | تُدخل خانات **To** فقط (30/60/90/120/121+)؛ **From يُحسب آلياً** (الابتداء 0) |
| أساس الحساب | **Bill Date** — "number of days for which the payment has to be received... based on the bill date" |
| النطاق المشترك | "Certain queries and report options in the **Accounts Receivable and Financial Management module** is based on this definition" |
| Print Text | اسم عمود كل فترة في Aging Summary Report |
| **Aging with Interest** | معيار فائدة لكل فترة من 4 خيارات **نظامية**: (1) **% on Closing Balance** (2) **Amount** (3) **None** (4) **% on Opening Balance** — + العامل في عمود Amount |

## 4. قائمة تفاصيل البنوك (Bank Details List) — ACR-OPR §1 ص3 / ACR-SET §2 ص6

- قائمة مرجعية: Bank Name + Branch + Place — تُنشأ بزر مخصص وتُستدعى بإدخال الشيكات (نفسها في Opening Balance وTransaction Entry).
- خاصية الشيك: **Local / Outstation** (هل بنك الشيك في نفس الولاية التي بها الفندق).

## 5. البيانات المرجعية المستهلكة (معرَّفة في وحدات أخرى)

| المرجع | مصدر التعريف | الاستهلاك في ACR |
|---|---|---|
| Company Types (بادئة الكود) | **FO Setup** | أول 3 خانات من Company Code (ACR-SET §5 ص11) |
| Property Codes | SYS | اختيار Property في كل الشاشات |
| Outlets | SYS/POS | حقل Outlet في القيود والافتتاحيات |
| Exchange Rates (Exchange Entry) | FAS | يُعرض ولا يُحرَّر في القيود (ACR-OPR §1 ص3) |
| Revenue Discount Masters | S&M/FNB | ربط بالشركة (ACR-SET §5 ص15) |
| Billing Instructions / Market Segments / Amenities / Sales Offices / Sales Executives / Designations / Booker Types | S&M/FO | حقول Profile بـ F1 lookups |
| Card Types / CC Companies | FO/POS | تسويات البطاقات |
