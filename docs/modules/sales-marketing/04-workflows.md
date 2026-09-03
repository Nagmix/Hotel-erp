# 04 — سير العمل (Workflows) — وحدة SLM

> **14 سير عمل موثق** WF-SM-01..14. الوحدة بطبعها **CRM دورة حياة** — الأعمال الكبرى: دورة Prospect→CGR، دورة مكالمة→متابعة، دورة تخصيص وكيل→حجز، دورة موازنة→انحراف، ودورة خطاب تسويقي.

---

## WF-SM-01 — دورة حياة العميل المحتمل (السير الجوهري)

```
Prospect Entry (SLT §4)
  │  بيانات: CEO/holding/competitors/turnover/Frequent Travelers
  ▼
Daily Sales Calls (§6) ──→ follow-up date/time ──→ Visit/Tele-call
  ▼
Business Loss Entry (§8)؟              Entertainment/Gift (§7)
  │  (خسارة: منافس/سبب)                    │  (استقطاب: هدايا/إعلان)
  ▼                                        ▼
[أهداف الفندق مستوفاة — قراري بشري]
  ▼
Transfer Prospects (§10)
  │  double-click "No" في عمود To Company Profile
  │  توليد كود: TTT(نوع)+حرف أول+مسلسل آلي  ←  COM/TAG/AIR
  ▼
Company Master = شركة CGR ✓
  ▼
Company Profile (PRF §7): AR terms + Contacts + Discounts + Bookers
  ▼
Link Rates to Company (§9) + Amenities + Retention/Cancellation Policies
```

**الحوافز الموثقة:** "The Hotel therefore sends their Sales Executives and **lures various companies to enter into a contract** with them by offering them **various discount schemes**. The Hotel sets certain targets for each company... **Until the company fulfils the Hotel's requirements, it is known as Potential Company**" (SLT ص7).

## WF-SM-02 — دورة المكالمة والمتابعة

```
Daily Sales Call (Date/Time/Exec/Account/Contact/Activity Type/Notes)
  │ + Sales Call Types كـ Reason (Rate Negotiations/Casual/Service Related)
  ▼
follow-up date + time ──→ Follow-up/Schedule Report (REP §4 — تواريخ مستقبلية)
  ▼
[زيارة تالية] ──→ مكالمة جديدة ──→ (تكرار)
```
- المخرجات التحليلية: Sales Call Report (REP §3 — خلال الشهر) + Sales Performance (العدد + الانحراف عن الموازنة + الخسائر + إنفاق الهدايا!).

## WF-SM-03 — خسارة العمل

```
Business Loss Entry: شركة (بحث) → date lost → competitor → reason → remarks
  ▼
Business Lost Report (REP §1): فرز Sales Executive Wise أو Reason Wise
  ▼
(تحليل تنافسي → Market Share Analysis REP §2)
```

## WF-SM-04 — دورة الموازنة والانحراف

```
Company Budgets (SLT §3):
  Company Range أو Company Type → اختيار شركة →
  [budget period + classification (revenue/room nights) +
   Room Nights expected + anticipated revenue] × فترات متعددة
  │  ⚠️ "potential companies are not included in this budget" — CGR فقط!
  ▼
(تشغيل فعلي: حجوزات/إيرادات FO)
  ▼
Sales Performance (Budget) (REP §7): Room Nights + Budget Variance +
  Business Lost + Gifts & Entertainment amount + # Sales Calls
Company Prod. Variance Report (REP §18): سنة حالية vs سابقة
  (Room Nights, ARR, Revenue)
```

## WF-SM-05 — دورة تخصيص الوكيل (ثلاثية + حجز)

```
Agent Allocation (PRF §12): مدى تواريخ (From=Accounting date) +
  شركة/Property/Room Type + غرف + Over-Book% + Confirmation days +
  Week Access (أو Day Access إن Module Attribute #8=YES)
  ▼
Agent Forecast (§13): غرف متوقعة (تُعامل شبه مؤكدة — "should match with allocation")
  ▼
Agent Release Dates (§14): cutoff days متعددة داخل المدى
  [التفعيل: INI #41 = '0'!]
  ▼
(برنامج الحجز في FO): "reservation program prompts you to assign
  the rooms requested as Inside or Outside allocation"
  ▼
Allocation List (REP §8) + Forecast List (REP §9)
```

## WF-SM-06 — دورة المخطط التنفيذي

```
Map Users/Sales Exec (PRF §16): Executive ↔ User ID
  ▼
Executive Planner Login (SLT §9): user id + password
  ▼
ثلاث مناطق:
  A) Appointments: إنشاء (Time/Contact/Designation/Notes)
     → فرز (Company/zip/City/State)
     → [تعديل]: Reschedule (date/time/reason) | Cancel (reason)
                 | Transfer لمندوب آخر (اختيار + reason)
  B) Things To Do: نقر ساعة (7am-8pm) → مهمة (Important/Normal)
     → tag completed | عرض غير المكتمل
  C) In-house Guest: نزلاء اليوم
  ▼
Logout ("This logs out the user that is logged into the Executive Planner")
```
**شرط التمكين:** "can be executed **only by sales executives who have been mapped** to a user id" — أو كل المستخدمين بـINI #239.

## WF-SM-07 — إنشاء/تعديل Company Profile (مركز AR)

```
Company Profile (PRF §7): Add →
  1. الحزمة الأساسية (كود 7 خانات: 3 نوع FO + 4 حر)
  2. Bookers (نافذة: Type/Code/Name)
  3. AR Details (نافذة: Bypass Invoice/Allow Credit/Credit Days/
     Invoice Currency/Interest %/Credit Limit/Commission %/
     Collection Executive/Billing Address)
  4. Contacts (نافذة: Title/Name/Designation/DOB/Anniversary/Email/Mobile/Tel Extn)
  5. Revenue Discount Link (نافذة: اختيار ماستر من القائمة)
  6. Black List: Yes → reason + authorizer
  ▼
Modify mode: عرض Blacklist Details (نافذة سادسة)
```
**المستهلكون نصاً:** "used in **Front Desk, Sales & Marketing, Point of Sale, Accounts Receivables, Banquets, Conferencing and Membership**" — 7 وحدات!

## WF-SM-08 — التحديث الجماعي (Mass Update)

```
Update Company Profile (PRF §8):
  Dropdown (اختيار ما يُحدَّث من بِنى الأسعار) →
  Old Value (زر قائمة اختيار) → New Value (بنفس الطريقة) → Save
  ▼
(يتغير الربط لكل الشركات المتأثرة!)
```
> أداة إدارية خطيرة — لا توثيق لمعاينة عدد السجلات المتأثرة قبل الحفظ (ملاحظة إعادة البناء R-SM-2).

## WF-SM-09 — ربط الأسعار والمرفقات

```
Link Rates to Company (PRF §9):
  Company → عرض (Name/Tel/IATA) →
  Non-rack Rate Structure → نافذة Include/Exclude Tax →
  [اختياري] Package Rates →
  Amenities → شبكة: إشغال (single/double/triple) × room type × plan × currency
  ▼
(LUK §3/§5/§6: الاستعلام عن الأسعار بثلاث زوايا)
```

## WF-SM-10 — التسويق بالخطابات

```
Company Letters (REP §12):
  مدى الشركات → Include Company Code؟ → Send Email؟
  │  CEO → بريد الشركة | designation آخر → قائمة جهات الاتصال
  │  (المحتوى من Word processing software)
  │  Attach (مرفقات) + Subject → Send (عبر Microsoft Outlook!)
  ▼
أو Print (طباعة جماعية)
  ▼
مساندة: Company Labels (2/3 أعمدة) + E-Mail ID List (CEO أو by Designation)
```

## WF-SM-11 — دورة أعياد الميلاد/المناسبات

```
Contacts (DOB + Anniversary) + Frequent Travelers (من Prospects)
  ▼
Birthday/Anniversary List (REP §5):
  Both/Company/Prospect × Birthday/Anniversary ×
  Contact Person/Frequent Travelers × مدى MM/YY
  ▼
(قائمة اتصال تسويقي)
```

## WF-SM-12 — الاحتلال التاريخي (ما قبل التشغيل)

```
Daily Occupancy Entry (SLT §1):
  Property (نفس المجموعة أو مختلفة!) → date → total rooms →
  % occupancy → Avg Room Revenue → breakup أنواع الغرف
  ▼
MIS reports "for entire Financial Year" (تقارير ما قبل live)
```
> حالة إدخال بيانات تراكمية فريدة — تُستخدم مرة عند التنفيذ ثم للأرشيف.

## WF-SM-13 — دورة F&B الترويجية

```
F&B Promotion Entry (SLT §2):
  مهرجان (American/Mexican/Chinese/Russian themes أو
  Christmas/New Year/Halloween/Thanksgiving أو Sea Food/Vegetable's Galore)
  → From/To + Outlet + sponsor + rate/Pax + amount + benefits
  ▼
(قياس الأثر عبر تقارير إيراد POS/BNQ — خارج SLM)
```

## WF-SM-14 — دراسة الحصة السوقية

```
(مصدر بيانات المنافسين — غير موثق شاشةً! GAP-SM-D01)
  ▼
Market Share Analysis (REP §2):
  From/To (نفس الشهر إلزامياً!) + Property →
  "room occupancy information of other competing Hotels"
  ▼
(مقارنة مبيعات الغرف: فندقنا vs المنافسين)
```

---

## خريطة قواعد السير (مُلخص لقواعد العمل المرتبطة)

| WF | القواعد الحاكمة | في 05 |
|---|---|---|
| WF-SM-01 | BR-SM-02/03 (بنية الكود + قيد التحويل) | ✓ |
| WF-SM-04 | BR-SM-03 (استثناء Prospects) | ✓ |
| WF-SM-05 | BR-SM-07/08 (INI #41 + Attribute #8 + تطابق Forecast) | ✓ |
| WF-SM-06 | BR-SM-09/10 (كلمة المرور + From=Accounting) | ✓ |
| WF-SM-07 | BR-SM-01/05 (القفل الائتماني + Blacklist) | ✓ |
| WF-SM-10 | BR-SM-20 (CEO vs جهات الاتصال) | ✓ |
