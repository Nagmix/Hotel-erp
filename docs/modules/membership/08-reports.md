# 08 — التقارير (Reports) — وحدة MEM

> **32 تقريراً مطبوعاً + 6 استعلامات تفاعلية = 38** (RPL ص1-56). التصنيف الوظيفي: عضوية/انضمام 12 · تسويق CRM 4 · شكاوى 2 · مالية AR مصغرة 15 · تحليل إنفاق 1 · إعادة طباعة 1 · المراجع التفاعلية (في 09-lookups).

---

## 1. عائلة الانضمام والعضوية (12)

| # | التقرير | المدخلات المميزة | ملاحظات |
|---|---|---|---|
| 1 | Corporate Members List | Corporate Member/Corporate Application + Range + **New/Update Member + Updated date** + Skip page | "Corporate member details are recorded in 'Corporate Master'" |
| 2 | Pending Applications | Membership/Corporate + Category + All/Range + **عنوان الطباعة Residence/Work Place/Abroad** | يرصد غير المعالجين |
| 3 | Screening Details Report | Category + printing options + All/Range | حالة الفحص |
| 8 | Member Expiry List | Category + Date Range | "membership expiry date and the renewal date... along with start date" |
| 11 | Membership Details | Membership/Application + Category + Status + **Range/Updated/New** + **خيارات طباعة (Birthday/Bank/Mailing...)** | أغنى تقرير ملف: قائمة تحقق تفاصيل |
| 12 | Renewal Report | Corporate/Individual + **Renewed/Non-Renewed** + كل الفئات/المختارة + المرشحون + **Upto Current Date/Date Range** | |
| 13 | Status Report | Date Range + نوع الحالة | "the reason the member was terminated or resigned or **died**" |
| 15 | Membership Released | Category + Date Range | Membership#/Category/Validity/Released Date (UNK-046) |
| 16 | Blacklisted Members | Date Range + Category | |
| 17 | Subscription Cancellation | Details/Summary + Subscription type + **All Members/Range** + **ترتيب Member wise/Subscription wise** | "who have added or removed subscription, the type, the rate and amount... the date added or removed" |
| 18 | Membership Summary List | Details/Summary + Category + **month/year** + خيارات القائمة السوداء الثلاثية | |
| 22 | Birthday List (Member) | Date Range (ضمن شهر) | **+ تحديث البريد بالنقر المزدوج + زر Send Email** |

## 2. عائلة التسويق CRM (4)

| # | التقرير | القيمة التسويقية |
|---|---|---|
| 4 | Birthday/Anniversary (MEM) | Members/Applications + قائمة Birthday/Anniversary + Active/Terminated + خيارات القائمة السوداء + Print Address — "used as reference to **wish the members**" |
| 5 | Mailing Labels (MEM) | نوع العضو + **عنوان (Residence/Work/Abroad)** + Category + **Services availed!** + Member Name Like + **ترتيب: Membership#/Pin Code/Category/City** | بطاقات مراسلة بفلاتر جيو-ديموغرافية |
| 9 | Age Report | Adult wise/Child wise + **فلاتر عمر AND سنوات عضوية (≤/≥/Between)** | تحليل تركيب الأعمار |
| 22 | Birthday List | (فوق) — القناة البريدية الفعلية |

> **دورة CRM مكتملة داخل وحدة واحدة**: استهداف (Age/Labels) → قوائم (Birthday/Anniversary) → تنفيذ (Send Email) — نظير مبكر لـ CRM module — راجع F-ME-11.

## 3. عائلة الشكاوى (2)

| # | التقرير | المدخلات |
|---|---|---|
| 10 | Complaint Register | **From Club Member / Against Club Member** + Date Range + **Pending/Attended/both** |
| 21 | Pending Complaints | (استعلام تفاعلي — انظر 09-lookups) |

## 4. العائلة المالية — دفاتر AR المصغرة (15) ⭐

| # | التقرير | الدلالة المالية |
|---|---|---|
| 24 | Settlement Summary (MEM) | Service type + Date Range + Print Summary + **Print by User** |
| 25 | Bill Details | Date Range + **Company Range** |
| 26 | Members List (Charges) | Service type + **Include Black List Members** |
| 27 | Transaction Check List - MEM | Date Range + Category + **Payment mode + User id** — "all transactions (debits, credits & adjustments)" |
| 28 | Receipt Register (MEM) | Date Range + **Cash/Credit Card/Cheque** + **Bank Wise Breakup (Y/N)** + **Category Wise Page Breakup (Y/N)** |
| 29 | Credit Card Register (MEM) | **Company code** + Date Range + **Commission % (اختياري!)** |
| 30 | Closing Balance | **Month/Year** + خيارات القائمة السوداء — "opening balances, transactions and closing balances" |
| 31 | Due Report | Month/Year + خيارات القائمة السوداء — "balances of each member **as on a given date**" |
| 32 | Charges | Date Range + charge category + **Summary/Bill Details** |
| 33 | Control Report | **Month/Year** + Category + **consolidated debit/credit** + Summary |
| 34 | Closing Balance Details | Date Range + **Company Range** |
| 35 | Membership Control Report | Summary/Details + **Revenue code** + Date Range + **revenue wise breakup** + **"total revenues made by the members with outlet filtration"** |
| 36 | Members Register | **Members/Non-members** + Date Range + **Outlet Details/Summary + قائمة Outlets** + **Page Skip per member + Nil Balance Y/N** — "total revenues date wise and Outlet wise" |
| 14 | Reprint Non Member Receipt | Receipt date + **from/to receipt numbers** |

> 📌 **الملاحظة المعمارية:** هذه العائلة نسخة مطابقة وظيفياً من تقارير ACR (Receipt Register/Closing Balance/Due/Control/Credit Card Register) — لكن **مقيّدة بأعضاء العضوية** — أي أن الوحدة تحتفظ **بدفتر أستاذ مساعد خاص بها** يُقفل شهرياً عبر ترحيلات WF-ME-11..14 (راجع 11-accounting-impact §4).
> 📌 **Commission % اختياري** في Credit Card Register = احتساب عمولة البنك آلياً على مجموعة الإيصالات (فريدة في المشروع!).

## 5. الزيارات (2)

| 6 | Visit Details | Date Range + Category + Members Range + **فقط أعضاء/ضيوف/كلاهما** + ترتيب Date/Category/Members |
| 7 | Member Visit Details | نسخة الأعضاء فقط |

## 6. أنماط التقارير العامة (للمرحلة 7 — REP deep-read)

1. **ثلاثية خيارات القائمة السوداء** تتكرر في 5 تقارير (4/18/22/30/31) — include/exclude/**only**.
2. **نمط Load-then-drill** في الاستعلامات (انظر 09).
3. **Skip Page / Page Breakup** — خيارات طباعة فيزيائية متكررة (1/28/36).
4. **فلاتر النطاق الموحدة**: All/Range في كل تقارير القوائم.
5. أغلب التقارير بنمط **شاشتين**: شاشة فلاتر → Print Preview → صيغة نهائية (سلسلة Generate ثابتة).
