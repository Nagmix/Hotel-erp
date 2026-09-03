# 14 — نموذج البيانات (Data Model) — وحدة SLM

> **النمذجة المفاهيمية لكيانات الوحدة** — 20 كياناً أساسياً + علاقاتها. القاعدة النمطية الكبرى: **مستودعا عملاء بجسر تخرّج** + **كيان مركزي مشترك (Company)** تحوم حوله 15+ كياناً فرعياً.

---

## 1. مخطط الكيانات والعلاقات (ER مبسط)

```
┌────────────────────────────────────────────────────────────────┐
│ [مستودع 1] PROSPECT (SLT §4)                                    │
│  company_name (F1→Company!) · ceo · classification · address     │
│  holding_company · sales_executive · turnover · main_business    │
│  competitors · remarks                                           │
│  ├──< PROSPECT_CONTACT                                           │
│  └──< FREQUENT_TRAVELER (من الشركة)                              │
└──────────────┬──────────────────────────────────────────────────┘
               │ Transfer Prospects (SLT §10) — أحادي الاتجاه
               │ شرط: استيفاء أهداف الفندق
               │ توليد كود: TTT(نوع)+حرف أول+مسلسل آلي
               ▼
┌────────────────────────────────────────────────────────────────┐
│ [مستودع 2] COMPANY (Company Profile — PRF §7) ★ الكيان المركزي   │
│  code (7: 3 نوع+4) · name · ceo_title/name · classification     │
│  watch_list(y/n)+to_date · holding_company · address · pan       │
│  city/state/country/zip · phone/fax/iata · email/web             │
│  sales_office · sales_executive · bill_inst · mar_seg            │
│  default_amenities · remarks · blacklisted(y/n)                  │
│  ├── AR_TERMS: bypass_invoice · allow_credit · credit_days       │
│  │   invoice_currency · interest_pct · credit_limit              │
│  │   commission_pct · collection_executive · billing_address     │
│  ├──< COMPANY_CONTACT (title/name/designation/dob/anniversary/    │
│  │        email/mobile/tel_extn)                                  │
│  ├──< COMPANY_BOOKER (type/code)                                  │
│  ├─── REVENUE_DISCOUNT_MASTER (رابط)                              │
│  ├──< BLACKLIST_LOG (reason + authorizer)                         │
│  ├──< BUDGET (period+classification+room_nights+revenue) ×مدد    │
│  ├──< RETENTION_POLICY (property/room_type/pct)                   │
│  ├──< CANCELLATION_POLICY (property/room_type/from_day/to_day/pct)│
│  ├──< AGENT_ALLOCATION (range/property/room_type/rooms/           │
│  │        overbook_pct/confirm_days/week_access)                  │
│  │        └──< RELEASE_DATE (from_auto/cutoff_days)               │
│  ├──< AGENT_FORECAST (range/property/room_type/rooms)             │
│  ├──< RATE_LINK (rate_structure+tax_incl/excl+package+amenities)  │
│  ├──< SALES_CALL (date/time/exec/contact/activity/notes/          │
│  │        follow_up_date+time)                                    │
│  ├──< ENTERTAINMENT_GIFT (type:ent{etype,outlet,session}|gift·    │
│  │        place/date/amount/authorizer)                           │
│  └──< BUSINESS_LOSS (date/competitor/reason/remarks)              │
└────────────────────────────────────────────────────────────────┘
        ▲ يستهلكه: FO · POS · AR · BNQ · MEM · (Conferencing!)
        
┌─ ماسترات مستقلة ────────────────────────────────────────────────┐
│ REVENUE_DISCOUNT_MASTER (id≤4رقمي/desc/active/expiry)            │
│   └──< DISCOUNT_LINE (revenue_code, pct)                         │
│   └──< MENU_DISCOUNT (revenue_code=F&B, menu_type, pct)          │
│     menu_type ∈ {FOOD, LIQUOR, SOFTDRINKS, TOBACCO, OTHERS}      │
│ HOTEL_AMENITY (code فريد, name)                                  │
│ SALES_CALL_TYPE (code, desc — Rate Negotiations/…)               │
│ BOOKER (type FO, code, name/address/pan/tel)                     │
│ EXEC_USER_MAP (sales_executive ↔ sys_user)  ← شرط Planner        │
│ FNB_PROMOTION (from/to/property/outlet/purpose/sponsor/          │
│   rate_per_pax/amount/benefits/remarks)                          │
│ DAILY_OCCUPANCY_HIST (date/property/rooms_total/pct/arr          │
│   └──< OCC_BREAKUP_ROOMTYPE)                                     │
│ APPOINTMENT (time/contact/designation/notes + reschedule/cancel/ │
│   transfer{reason, to_exec})                                     │
│ TODO_ITEM (hour 7-20/important|normal/completed)                 │
│ HOTEL_PROFILE ★ (code≤3/name/owner/group/classification)         │
│   ├──< HOD (designation/name/residence/mobile/pager)             │
│   ├──< HOTEL_OUTLET (capacity/dress_code/smoking/time/           │
│   │     min_cover_charge/chef/specialty/view/remarks)            │
│   ├──< HOTEL_ROOM (room_type/desc/total/view/amenities           │
│   │     + rates seasonal/off × single/double)                    │
│   ├──< HOTEL_BANQUET (venue/capacity/sqft/attributes)            │
│   ├──< HOTEL_CGR (company+amenities)                             │
│   ├──< VIP_VISIT (guest/arr/dep/room_no/comments)                │
│   ├──< PICNIC_SPOT (name/attractions/distance_kms/mode/          │
│   │     travel_time/charges)                                     │
│   ├── PICTURE (bmp) + GENERAL_INFO (temps/distances/fares/       │
│     landmark)                                                    │
└──────────────────────────────────────────────────────────────────┘
```

## 2. جرد الحقول الموثقة (إحصاء)

| الكيان/المجموعة | عدد الحقول التقريبي | ملاحظات |
|---|---|---|
| COMPANY + الحزم الفرعية | ~45 | 18 أساسي + 10 AR + 8 اتصال + حاجز + قائمة سوداء |
| PROSPECT + مسافرون | ~15 | أغنى ماستر "محتمل" في المشروع |
| AGENT (ثلاثي) | ~16 | Allocation 9 + Forecast 5 + Release 3 |
| Rate/Discount | ~12 | خصم menu-wise يتفرع |
| Hotel Profile (10 كتل) | ~40 | محتوى تسويقي شامل |
| التتبع (Calls/Ent/Loss/Budget/Planner) | ~30 | |
| **الإجمالي** | **~160 حقلاً** | منها ~45 في الكيان المركزي |

## 3. المفاتيح والقيود الفريدة

| الكيان | المفتاح/القيد | المصدر |
|---|---|---|
| COMPANY | code (7 خانات: 3 نوع إلزامي من Company Types) | PRF §7 |
| توليد التحويل | فهرس مركب: (type_prefix, first_letter, serial) — **مسلسل لكل نوع+حرف** | SLT §10 |
| AMENITY | كود فريد | PRF §6 |
| DISCOUNT | id رقمي ≤4 (فريد ضمن الماستر) | PRF §5 |
| HOTEL_PROFILE | code ≤3 alphanumeric | PRF §17 |
| BUDGET | (company, period) — multi-period مسموح للشركة نفسها | SLT §3 |
| AGENT_ALLOCATION | (company, property, room_type, date_range) | PRF §12 |
| APPOINTMENT | (exec_user, date, time) منطقياً | SLT §9 |

## 4. قيم التعدادات (Enums) الموثقة

| التعداد | القيم | المصدر |
|---|---|---|
| Activity Type (Sales Call) | Hotel Visit · Tele Called ("etc,.") — قائمة مفتوحة قليلاً | SLT §6 |
| Entertainment/Gift Type | Entertainment · Gift | SLT §7 |
| Menu Type (F&B Discount) | FOOD · LIQUOR · SOFTDRINKS · TOBACCO · OTHERS | PRF §5 |
| Rate Type (Lookup) | Non Rack · Package | LUK §3 |
| Watch List / Black Listed / Allow Credit / Bypass Invoice | Yes/No | PRF §7 |
| Budget classification | revenue · room nights | SLT §3 |
| Company Type prefixes (أمثلة موثقة) | COM · TAG · AIR | SLT §10 |
| TODO classification | Important · Normal | SLT §9 |
| Birthday/Anniversary source | Company · Prospect · Both × Contact Person · Frequent Travelers | REP §5 |
| Market Share date scope | شهر واحد (From=To شهر/سنة) | REP §2 |

## 5. قرارات النمذجة لإعادة البناء (Frappe)

| # | القرار | المبرر |
|---|---|---|
| D-M-1 | **Prospect = Lead** (ERPNext CRM) و**Company = Customer** — التخرّج = التحويل القياسي Lead→Customer | تطابق بنية ERPNext حرفياً (status + conversion) |
| D-M-2 | Frequent Traveler من الشركة = Contact مع علامة "Is Frequent Traveler" | يعيد استخدام Contact القياسي |
| D-M-3 | AR Terms = حقول Customer القياسية (credit_limit/credit_days عبر Sales Invoice settings) + Custom لـ interest/commission/bypass/collection_exec | ERPNext أصلاً يملك نصفها |
| D-M-4 | Agent الثلاثي = doctypes مخصصة (Hotel Allotment/Forecast/Release) — لا مقابل ERPNext | مفهوم فندقي صرف |
| D-M-5 | Revenue Discount = Pricing Rules (شروط: revenue code/item group + menu type) | منع تكرار منطق الخصم |
| D-M-6 | Hotel Profile = doctype تسويقي content-heavy (مع child tables) + صورة (رفع BMP يُستبدل بصيغ حديثة) | |
| D-M-7 | Planner = Event (Frappe Calendar) + ToDo — والتحويل/الإلغاء بتعديل الحالة مع سبب | يعيد إنتاج Appointments/Things To Do بأصل منصة |
| D-M-8 | Daily Occupancy التاريخي = doctest واحد بلا تعديل بعد الإدخال (append-only) | طبيعته الأصلية |
| D-M-9 | competitors = Data field ح Morse (JSON) أو child table | الحاجة التقاريرية فقط |
| D-M-10 | Map Users/Sales Exec = ربط User↔Sales Person القياسي | يغني عن doctype مخصص |
