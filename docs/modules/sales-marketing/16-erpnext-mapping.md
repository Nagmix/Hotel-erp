# 16 — الموائمة مع ERPNext/Frappe (ERPNext Mapping) — وحدة SLM

> **أفضل موائمة بنية في المشروع حتى الآن**: ERPNext CRM (Lead→Customer) + Sales Person + Pricing Rules + Contact يغطون ~60% من الوحدة بمعمارية أصلية — الباقي فندقي صرف (Allotment/Release/Hotel Profile) بـcustom assets.

---

## 1. خريطة الموائمة الكبرى

| الأصل (SLM) | هدف ERPNext/Frappe | جودة الموائمة | ملاحظات التنفيذ |
|---|---|---|---|
| **Prospect** | **Lead** (CRM) | ★★★★★ حرفية | lead_name/organization/نوع الاتصال + Custom: holding/competitors/turnover |
| **Transfer Prospects** | **Lead → Customer conversion** (الزر القياسي!) | ★★★★★ | التوليد TTT+حرف+مسلسل = Naming Series custom على Customer (naming by type prefix) |
| **Company Profile** | **Customer** (+ Customer Group/ Territory) | ★★★★ | watch_list/blacklist = Custom flags + reason child |
| **AR Terms** (credit) | **Customer: credit limit** + Sales Invoice settings | ★★★★ | credit_days/interest/commission/bypass = Custom (AC-R-2) |
| **Contacts** (DOB/Anniversary) | **Contact** (لديه ميلاد؟) + Custom: anniversary | ★★★★ | anniversary وfield Custom بسيط |
| **Frequent Traveler** | Contact مع role/tag | ★★★ | |
| **Bookers Master** | Custom/Contact tag أو Sales Partner | ★★ | مفهوم فندقي (مرتبط FO reservations) |
| **Sales Executives / Collection Executives** | **Sales Person** (شجرة!) | ★★★★ | Collection = Sales Person branch أخرى أو role |
| **Map Users/Sales Exec** | User ↔ Sales Person link (القياسي) | ★★★★★ | متوفر أصلاً |
| **Daily Sales Call** | **CRM Call Log** أو Activity/Event | ★★★★ | follow_up = تاريخ Activity القادم |
| **Sales Call Types** | Custom: Call Type | ★★★ | |
| **Appointments (Planner)** | **Event** (Calendar) | ★★★★★ | reschedule/cancel/transfer = تعديل + Custom status |
| **Things To Do** | **ToDo** (Frappe) | ★★★★★ | priority (High/Low→Important/Normal) + completed flag قياسي |
| **In-house Guest view** | Custom view فوق Reservation/Folio | ★★★ | |
| **Sales Manager Tool (360°)** | **Customer dashboard** (ERPNext يبنيه تلقائياً!) + custom panels | ★★★★ | ERPNext dashboard generator يقارب الفكرة |
| **Revenue Discount Master** | **Pricing Rule** (discount %) | ★★★★★ | شروط revenue code/menu type = conditions؛ تفعيل تواريخ = valid_from/to قياسي! |
| **Link Rates to Company** | **Price List** + Item Price (linked to Customer Group/Specific Customer) | ★★★★ | include/exclude tax = Item Price tax mode |
| **Company Package Rates** | Price List + package items | ★★★ | مفهوم الباقة يحتاج نمذجة |
| **Agent Allocation/Forecast/Release** | **Custom (فندقي صرف)** | ★ | لا مقابل — Allotment doctype مخصص (F-SM-3) |
| **Retention/Cancellation Policy** | Custom + قالب رسوم على الفوليو | ★★ | F-SM-7 |
| **Hotel Amenities** | Custom doctype + Product Bundle/serv | ★★ | مجانية — تُعرض عند الحجز |
| **Company Budgets** | **Sales Person Target Allocation** أو Custom Budget | ★★★ | الفندقية: room nights + revenue معاً |
| **Business Loss Entry** | Custom (Opportunity lost-reason) | ★★★ | ERPNext lead/opportunity فيه "lost" جزئياً |
| **Entertainment/Gift** | **Expense Claim**-lite أو Custom + GL اختياري | ★★★ | يسد GAP-SM-P2 |
| **F&B Promotion** | **Campaign** (CRM!) | ★★★★ | Campaign موصول بالفوترة للقياس |
| **Hotel Profile** | Custom doctype (محتوى تسويقي) | ★★ | كتل child tables |
| **Daily Occupancy (تاريخي)** | Custom واحد append-only | ★★ | |
| **Birthday/Anniversary List** | Report فوق Contact | ★★★★ | |
| **Company Letters** | **Email Template + Newsletter** | ★★★★★ | يعوض Outlook بلا خسارة |
| **Company Labels** | **Print Format** (Label) | ★★★ | |
| **E-Mail ID List** | Query Report فوق Contact | ★★★★ | |
| **Watch List Companies** | Query Report فوق Customer | ★★★★ | |
| **Market Share Analysis** | Custom Report (يحتاج مصدر منافسين!) | ★★ | يُحسم مع UNK-049 |
| **Company Contribution/Productivity/Sales/Variance** | Query/Script Reports فوق invoices | ★★★ | فرز/group native |

## 2. الأصول المخصصة المطلوبة (Custom Assets) — F-SM-1..8

| # | الأصل | الوصف | الحجم التقديري |
|---|---|---|---|
| **F-SM-1** | **دورة Lead→Customer فندقية** | Naming Series (COM/TAG/AIR+حرف+مسلسل) + حقول prospect الغنية (competitors/turnover/holding) + منع العكسية | S |
| **F-SM-2** | توحيد ماسترات FO المستضافة | Sales Office/Execs/Collection/Bookers/Company Types = مصدر Frappe واحد بواجهتين | M |
| **F-SM-3** | **محرك التخصيص الوكيلي** | Allotment + Forecast + Release Dates + منطق Inside/Outside prompt لطبقة الحجز | **L** (الوحيد الكبير) |
| **F-SM-4** | Credit Gate موحد | نقطة فحص واحدة (credit_limit) تستدعيها FO/POS/BNQ/Manual — أعادة تنفيذ BR-SM-01 | M |
| **F-SM-5** | قناة الحملات | Email Template + Newsletter + توجيه CEO/contact-list + Birthday report | S |
| **F-SM-6** | قياس الحملات/المهرجانات | ربط Campaign بتقارير POS/BNQ (أثر R-لو) | S |
| **F-SM-7** | Retention/Cancellation engine | سياسات نسب + مدى أيام + تحصيل عند No-Show/إلغاء (في FO) | M |
| **F-SM-8** | Hotel Profile content | doctype + 10 child tables + استدعاء من شاشة الحجز | M |

> **التقدير الكلي: 8 أصول (L×1 + M×4 + S×3) — أنسب وحدة تنفيذاً بعد HRP** لأن قلبها (CRM) منصة-جاهز.

## 3. ما يجب استيراده/توليده كبيانات (Data Migration)

| البيان | المصدر الأصلي | وجهة Frappe |
|---|---|---|
| Prospects | ماستر Prospect | Lead (status=Open) |
| Companies | Company Master | Customer (+ naming series تحفظ الكود القديم 7 خانات كـcustomer_code) |
| شروط AR | حقول Profile | Customer credit + Custom |
| تخصيصات الوكلاء | AGENT_* | Allotment custom |
| خصومات | Revenue Discount Master | Pricing Rules |
| ميزانيات | Company Budgets | Targets/Budget |
| بيانات المدن/الأعياد | Contacts | Contact |

## 4. مخاطر الموائمة

| الخطر | التخفيف |
|---|---|
| Lead القياسي أفق أضيق من Prospect (لا holding/competitors) | Custom fields على Lead — بلا تعارض ترقية |
| Pricing Rule مفاتيحها item/price list — والإيراد هنا revenue code فندقي | ربط revenue code بـItem معيارية أو Item Group mapping (قرار F-SM-2 التبعي) |
| Sales Person شجرة مبيعات وليست "فريق مكاتب" بالضرورة | هيكل شجرة: Property > Sales Office > Exec — يلائم |
| Conversion القياسي ينشئ Customer فوراً بلا "اعتماد استيفاء أهداف" | خطوة اعتماد بسيطة (workflow state) قبل التحويل |
| Event/ToDo فردية لكل مستخدم — والجلسة الفرعية الأصل تحمي منافسة المندوبين | permissions الـowner (P-SM-3) |

## 5. قرار المزامنة العكسية (ERPNext → الأصل)

لا حاجة لأي مزامنة عكسية: الوحدة تقرأ FO/POS/AR عبر الاستعلام القياسي (dashboard/reports) — طبقة SLM فوق طبقة التشغيل، تماماً كالأصل (12 §4).
