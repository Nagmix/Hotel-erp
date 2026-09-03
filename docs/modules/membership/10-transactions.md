# 10 — المعاملات (Transactions) — وحدة MEM

> **T-ME-01..14**: المعاملات اليومية والدورية. المحرك المركزي **Service Bill Entry** (T-ME-04) و**المحركات الدورية الخمسة** (T-ME-08..12) التي ترحّل إلى AR.

---

## T-ME-01: Membership Receipt Entry (الإيصال)
| الحقل | التوثيق |
|---|---|
| الهدف | **Membership / Corporate / Application / Member** — أربع جهات إصدار |
| Membership # | F1 أو إدخال |
| Receipt # + Date | يدوي أو تلقائي (سمة #6) — وسلسلة منفصلة للطالبين (سمة #7) |
| Revenue | كود الإيراد المسدد |
| Currency + Rate | العملة + "This field is **automatically filled**" |
| Amount + Payment Type + Remarks | المبلغ وطريقة الدفع |

**الاستدعاء التلقائي:** من 4 نقاط حفظ (سمات 2-5) + عند التحويل (MPF ص23) + عند التجديد (MMN ص3-4).

## T-ME-02: Revenue/Facility Entry (وسم الفوترة الشهرية)
- **تبويب Revenue Details**: Membership# + Member Type + Name + Revenue Type + **Revenue Charges Period (monthly/quarterly/yearly/half yearly/none)**
- **تبويب Facility Details**: اختيار المرافق + "If the availability facility is chargeable then select 'Yes'" + **Chargeable value type: Fixed/Billing** + فترة + تاريخ
- الدور: تجهيز بيانات المحركين T-ME-08/T-ME-09 — **توسيم وليس تحصيلاً**.

## T-ME-03: Guest Visit Entry (زيارة ورسوم دخول)
- Membership# + Category تلقائي + **صفوف Check-in؟** ("This allows adding more number of guests by selecting of a particular row")
- **Insert Guest Details / Edit Guest Details** للمرافقين
- **Entry Fee**: "Select the category of member or **non-member A/C** for which entry fee is to be applied" — رسوم دخول بشرائح
- ⚠️ وجهة ترحيل رسوم الدخول **غير موثقة** (UNK-047).

## T-ME-04: Service Bill Entry (محرك الفوترة) ⭐
```
Acc.Date (تلقائي من FO لو سمة #12) → Service Type → Confirm
 → Membership Billing / Affiliated Billing → Membership#/Affiliated# → Category + Name تلقائي
 → Code من Service Rate Master → عدد بالغين (Rate تلقائي) + عدد أطفال (Rate تلقائي)
    [شرائح: Members / Guest / Affiliated — الأرقام لكل شريحة]
 → Discount: NONE/AMOUNT/PERCENTAGE + Amount + **Reason**
 → Save → جدول الفواتير
 → Settlement (سمة #11 = تسوية Company تلقائية) أو يدوي:
    AR • CASH • CREDIT CARD (Type/Company/Card#/Authorization/Remarks)
    • CHEQUE (#/Date/Bank/Branch/Remarks)
```
- **النطاق الصريح**: "used for **non-Food and Beverage (F&B) services only**" (MTR ص7).
- الفاتورة تجمع بالغين وأطفالاً بأسعار شريحتهم تلقائياً من الماستر — **بلا تسعير يدوي**.

## T-ME-05: Register Complaints
- Club Member / **Against Club Member** + Membership# + Nature + **Priority** + **Assigned To** + Date/Time/Type تلقائي.

## T-ME-06: Attend Complaints (الإغلاق)
- From/Against + قائمة المعلقة → Double-click → **Action By** + Remarks → Save.

## T-ME-07: Event Definition (فعاليات الأعضاء)
- Membership# + Event Description + **Venue** + From/To (Date+Time) + Contact (+phone/mobile/email/fax) + **Chief Guest** + Remarks — "Members can hold functions, parties, or events in the club facilities" (MTR ص14).

## T-ME-08: Process Subscription (محرك الاشتراكات)
"arrive at the subscription rates for every member by retrieving the values from the master database and the subscription charges are subsequently **posted to the relevant members AR account**" — From/To + زر المعالجة.

## T-ME-09: Process Facility Charges (محرك المرافق)
نفس النمط؛ القيد: "The **From Date should be less than or equal to current date**".

## T-ME-10: Post Subscription to AR (الترحيل الانتقائي) ⭐
- From/To → قائمة الأعضاء → **checkboxes** (الكل افتراضياً) → Save
- "This facility offers the flexibility to **withhold, withdraw, or overwrite** the subscription charges mentioned in the membership master" (MTR ص17) — ثلاثية تحكم تشغيلي دقيقة غير موجودة في أي محرك ترحيل آخر بالمشروع.

## T-ME-11: ~~Membership Tax Posting~~ (فجوة توثيق)
- مذكورة في فهرس MTR (#11) **بلا جسم في النص** — الوظيفة الوحيدة في 43 ملفاً مقروءاً بهذا الوضع (GAP-ME-D01 → UNK-045).

## T-ME-12: Cover Charges Posting (رسوم الغطاء)
- **Process/Cancel** + Month/Year — الترحيل القابل للإلغاء الشهري الوحيد.

## T-ME-13: Posting Late Charges (رسوم التأخير) ⭐
- Late Fee Posting Month → **حساب رصيد آخر يوم من الشهر السابق** → إذا Debit → احتساب الرسوم (وفق Late Charge Fee Definition ببنية ضريبة FO) → Post Transaction → **ACR**
- المثال الموثق: January-2011 → رصيد 31-Dec-2010.

## T-ME-14: الإنهاءات والتغيرات (من MMN — انظر WF-ME-07/08/09)
Blacklist/Termination/Resignation/Deceased + Renewal + Category Transfer + Address Change — معاملات **تغيير حالة** وليست مالية (بلا ترحيل موثق لحظة الإنهاء — انظر 11 §5).

---

## مصفوفة الأثر المالي للمعاملات

| المعاملة | أثر فوري | أثر AR | دورية |
|---|---|---|---|
| Receipt | تحصيل | **مدين/دائن للحساب** | — |
| Service Bill | فاتورة | تسوية AR أو نقد فوري | يومية |
| Revenue/Facility Tag | — (وسم) | — (عبر المحركات) | — |
| Process Subscription | — | **ترحيل مدين** | شهرية |
| Process Facility | — | **ترحيل مدين** | شهرية |
| Cover Posting | — | **ترحيل مدين (قابل للإلغاء)** | شهرية |
| Late Charges | — | **ترحيل مدين على المتأخرين** | شهرية (بإزاحة) |
| Guest Visit Entry Fee | غير موثق | غير موثق (UNK-047) | يومية |
| الإنهاءات | حالة فقط | **لا ترحيل موثق** (GAP-ME-P1) | عند الطلب |
