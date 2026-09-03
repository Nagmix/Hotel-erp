# 14 — نموذج البيانات (Data Model) — وحدة MEM

> **~25 كياناً / 200+ حقلاً** — يوثق العلاقات والقيود البنيوية كما وردت نصاً. الوحدة تمتلك **مخزن أعضاء مستقلاً بالكامل** + دفتر مالي مساعد مرتبط بكيان AR الخارجي.

---

## 1. مخطط العلاقات الجوهري (ERD منطقي)

```
MEMBER_CATEGORY (1) ───< (N) SCREENING_DETAIL [Applicable?/Mandatory? per category]
      │
      ├─(1:N)─ CORPORATE_APPLICATION ──(convert)──> CORPORATE_MASTER ──(auto)──> [AR: COMPANY MEMCxxx]
      │              │                                   │
      │              └─(1:N)─ NOMINEE = MEMBERSHIP_APPLICATION ──(convert)──> MEMBERSHIP_MASTER
      │                          │        │                                   │
      │                          │        └─(1:N)─ INTERVIEW (Considered/Rejected/Cancelled)
      │                          └─(screening)─ APPLICATION_SCREENING (verified per checklist)
      │
      ├─(1:N)─ SERVICE_RATE_MASTER ─(N:1)─ FACILITY_CODE
      │            └─(3 tiers: Member/Guest/Affiliated × Adult/Children + TaxStructure[FO])
      ├─(1:N)─ MEMBERSHIP_STRUCTURE (RevenueCode × Category × Currency × Primary/Adult/Child)
      ├─(1:N)─ FACILITY_FIXED_RATES (5 roles × 5 periods)
      ├─(1:N)─ COVER_CHARGES (period × Amount + Age + MembershipYears + SeniorExemption)
      ├─(1:N)─ LATE_CHARGE_FEE (TaxStructure[FO] / Not applicable)
      └─(M:N)─ MEMBER_UDF (code + datatype)

MEMBERSHIP_MASTER (1) ─┬─< MEMBER_FAMILY (Spouse[photo+signature]/Children/Additional; P/S/C)
                       ├─< CREDIT_LIMIT (AllowCredit + Limit)
                       ├─< STATUS_EVENTS (Blacklist/Terminated/Resigned/Deceased + AuthPerson + Reason)
                       ├─< ADDRESS (Residential/Work/Abroad + mailing flag)
                       └─< AR_ACCOUNT [MEMC001 — خارجي]

AFFILIATED_CLUB (1) ─< AFFILIATED_MEMBER_RATES (شريحة أسعار ثالثة)

MEMBER (1) ─┬─< MEMBERSHIP_RECEIPT (4 جهات + Currency + PaymentType)
            ├─< REVENUE_FACILITY_TAG (Revenue: period | Facility: Fixed/Billing)
            ├─< GUEST_VISIT (+companions + EntryFee category)
            ├─< SERVICE_BILL (+lines: adults/children × 3 tiers + Discount[Reason] + Settlement)
            ├─< COMPLAINT (from/against + Priority + AssignedTo + ActionBy)
            ├─< MEMBER_EVENT (Venue + From/To + ChiefGuest)
            └─< POSTING_BATCH (Subscription/Facility/Cover/Late × Month/Year × Process/Cancel)
```

## 2. الكيانات المركزية بالتفصيل

### MEMBERSHIP_MASTER (كيان القلب)
| مجموعة الحقول | التفاصيل |
|---|---|
| الهوية | Membership# (يدوي/تلقائي — سمة #1) + Category + Application# (لو عبر دورة) |
| الصلاحية | From + **UPTO** (إلزامي بسمة #13) + Renewal date |
| الأسرة | Spouse (بيانات كاملة + **Photo + Signature**) + Children (حد عمري من Category) + Additional family (Accept/Member لكل!) |
| المالية | **AR Company Code (MEMCxxx تلقائي — سمة #10)** + Credit Limit (Allow Y/N + Limit) |
| العنوان | 3 أنواع + وسم mailing |
| UDF | حقول مخصصة (datatype dropdown) |

### SERVICE_BILL
```
Header: Bill# (auto) + AccDate (from FO if linked) + BillingType (Membership/Affiliated)
        + Membership#/Affiliated# + Category + GuestName
Lines:  Code (ServiceRateMaster) + Persons(Adults) + Rate(تلقائي) + Tier(Members/Guest/Affiliated)
        + Persons(Children) + Rate(تلقائي) + Tier
        + Discount (NONE/AMOUNT/PERCENTAGE + Amount + Reason)
Settlement: AR | CASH | CREDIT CARD (Type+Company+Card#+Auth) | CHEQUE (#+Date+Bank+Branch)
```

### STATUS_EVENT (سجل الحالات — 4 أنواع)
```
Membership# + MemberType (P/S/C) + EventKind (Blacklist/Termination/Resignation/Deceased)
 + AuthPerson + Reason (+ CauseOfDeath)
 + [Deceased only: Succession → NewPrimary (Member ref | NONE)]
```

### POSTING_BATCH (المحركات الدورية)
```
Kind (Subscription|Facility|Cover|Late) + Period (Month/Year)
 + Mode (Process | Cancel — للCover فقط) + Selected members (checkboxes — للSubscription)
 + Late only: ReferenceMonth = Period − 1 (الرصيد كآخر يوم من الشهر السابق)
```

## 3. أنماط البيانات النوعية

1. **حقول المسؤولية داخل السجل** (AuthPerson/Reason): نمط "Audit-in-Row" — لا جدول تدقيق منفصل (مقارنة بـ HRP Payroll Audit القيمي).
2. **الأسر كمصفوفة أدوار** (P/S/C + Accept/Member flags): التمييز بين "البيانات مقبولة" و"العضوية معتبرة" — **علامة is_member منفصلة عن وجود السجل**.
3. **الشريحة الثلاثية كحقل تصنيف** في كل سطر فاتورة (Members/Guest/Affiliated) — الأسعار نفسها في 3 جداول ماستر متوازية.
4. **التواريخ المركبة**: Valid until للطلب، From/UP TO/Renewal للتحويل، Period Month/Year للدوريات، From-To DateTime للفعاليات.
5. **UDF الأصلي**: Member UDF بـ datatype حقيقي (dropdown) — وحدة نادرة توثق أنواع حقول مخصصة.
6. **لا مفاتيح INI**: كل التهيئة صفوف بيانات (System Attributes = 13 صف Yes/No).

## 4. التقديرات الكمية

| المقياس | القيمة |
|---|---|
| كيانات الماستر | 12 |
| كيانات الأعمال | 13 |
| حقول موثقة (تقريبي) | 200+ |
| كيانات لها عمليات حالة | 5 (Member/Cover/Subscription/Complaint/Interview) |
| علاقات عبر وحدات | 3 صريحة (AR×2 + FO×2 سلبية-حدود) + عملات |
| جداول تقارير | 38 تعريفات (لا كيانات — قراءات) |
