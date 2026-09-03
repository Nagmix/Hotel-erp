# 03 — جرد الشاشات (Screens Inventory) — وحدة MEM

> **~80 شاشة وظيفية/تقريرية**: 12 (SET) + 7 (MMN) + 10 (MPF) + 13 (MTR) + 38 (RPL). النمط العام: شاشات Master-Detail بتبويبات (Tabs) + أزرار F1 للمساعدة + مفاتيح وظيفية قياسية.

---

## 1. البنية القياسية للشاشة (Identifying Standards — SET ص1)

| الزر | الوظيفة |
|---|---|
| Add | إدخال جديد |
| Change | تعديل |
| Delete | "Remove or erase... **works conditionally**" |
| Browse | عرض/تصفح |
| Previous / Next | "enabled **only after you click Browse**" |
| Save | حفظ |
| Utilities | "Command Window, Internode Communication, Calculator, Calendar, Scratch Pad, and Yellow Pages" |
| Exit | خروج |

> عائلة الأزرار القياسية ذاتها الموثقة في FO/POS/SET — إرث بيئة واحدة (نافذة أوامر + اتصال Internode + آلة حاسبة + تقويم + مفكرة + دليل أصفر!).

## 2. جرد الشاشات التشغيلية

| # | الشاشة | الدليل/الصفحة | عناصر مميزة |
|---|---|---|---|
| S1 | Member Categories | SET ص3 | Ref. Details زر + Accept/Member مزدوج لكل من (زوج/أبناء/إضافيين) |
| S2 | Screening Details | SET ص5 | مصفوفة فئة × (Applicable؟/Mandatory؟) |
| S3 | Service Rate Master | SET ص6-8 | 3 تبويبات (Member/Guest/Affiliated) × Adult/Children + Confirm |
| S4 | Membership Revenue Codes | SET ص8 | Once/Recurring + Refundable + Subscription Charge |
| S5 | Membership Structure | SET ص9-10 | Revenue × Category × Currency (سعر صرف تلقائي) + Primary/Adult/Child |
| S6 | Complaints Categories | SET ص10 | Main/Sub |
| S7 | System Attributes | SET ص10-12 | 13 سمة Yes/No |
| S8 | Facility Fixed Rates | SET ص12 | 5 أدوار × 5 فترات |
| S9 | Membership Facility Codes | SET ص13 | Code/Short/Long |
| S10 | Cover Charges | SET ص13-15 | فترة + Revenue + Amount/Category + Age + Membership years + 2 checkbox (Adjustment/Senior) |
| S11 | Late Charge Fee Definition | SET ص15 | Load لكل الفئات + Tax structure من FO |
| S12 | Member UDF | SET ص16 | Field Data Type dropdown |
| S13 | Membership Address Change | MMN ص2-3 | Address Type + تعديل مباشر |
| S14 | Renewal Entry | MMN ص3-4 | Corporate/Individual + تاريخ تجديد + **Member More Info** |
| S15 | Members Blacklist/Revoke | MMN ص4-5 | **Double-click على عمود Blacklist/Revoke للتبديل Yes/No** + Authorized + Reason |
| S16 | Members Termination | MMN ص6-8 | Terminated/Revoke + عمود Terminate? |
| S17 | Members Resignation | MMN ص8-10 | Resignation/Revoke + عمود Resigned? |
| S18 | Members Deceased | MMN ص10-12 | Cause of Death + **شاشة الخلافة** (اختيار Primary جديد أو None) |
| S19 | Category Transfer | MMN ص12-13 | Old→New + Remarks (+ ربط شاشة الطلب/Credit Limit) |
| S20 | Corporate Applications | MPF ص2-5 | 3 تبويبات + Financial Parameters + أزرار نسخ العناوين |
| S21 | Membership Application | MPF ص5-12 | 4 تبويبات + Spouse (بصورة وتوقيع!) + Children + Modify بفلاتر |
| S22 | Application Screening | MPF ص12-18 | Checkboxes تحقق + **زر بريد إلكتروني** + More Details (5 عروض فرعية) + Interview Required |
| S23 | Assign Interview Dates | MPF ص18-19 | Date/Time/Person/Remarks |
| S24 | Interview Details | MPF ص20-21 | Status: Considered/Rejected/Cancelled |
| S25 | Transfer Corporate Application | MPF ص21-24 | Validity (إلزامي!) + **Membership Receipt Entry تُفتح عند SAVE** |
| S26 | Transfer Membership Application | MPF ص24-27 | التبويبات + **Credit Limit Details** |
| S27 | Corporate Master | MPF ص27-28 | إدخال مباشر |
| S28 | Membership Master | MPF ص28-29 | إدخال مباشر + Credit Limit |
| S29 | Affiliated Club Master | MPF ص29-30 | Affiliated Category Name + **Photo** |
| S30 | Membership Receipt Entry | MTR ص2-3 | 4 أنواع أهداف + Currency (Rate تلقائي) + Payment Type |
| S31 | Revenue/Facility Entry | MTR ص3-5 | تبويبا Revenue Details / Facility Details (Fixed/Billing) |
| S32 | Guest Visit Entry | MTR ص5-6 | صفوف Check-in + Insert/Edit Guest Details + Entry Fee |
| S33 | Service Bill Entry | MTR ص7-12 | Acc.Date + Confirm + جدول بالغين/أطفال + Discount + **شاشات التسوية** (AR/Cash/CC/Cheque) |
| S34 | Register Complaints | MTR ص12-13 | Club Member / Against Club Member + Priority + Assigned To |
| S35 | Attend Complaints | MTR ص13-14 | قائمة + Action By + Remarks |
| S36 | Event Definition | MTR ص14-15 | Venue + From/To DateTime + Chief Guest |
| S37 | Process Subscription | MTR ص15-16 | From/To + زر تنفيذ |
| S38 | Process Facility Charges | MTR ص16 | From/To (**From ≤ Today**) |
| S39 | Post Subscription to AR | MTR ص16-17 | **قائمة أعضاء بcheckboxes** + Select/تخطي |
| S40 | Cover Charges Posting | MTR ص17 | **Process/Cancel** + Month/Year |
| S41 | Posting Late Charges | MTR ص17-18 | Late Fee Posting Month + **Post Transaction** |

## 3. عناصر الواجهة النوعية (أبرز 12)

1. **Double-click لتبديل الحالة** (MMN): أعمدة Blacklist?/Terminate?/Resigned? تُقلب بالنقر المزدوج — نمط تحرير خلية سريع.
2. **شاشة الخلافة** (MMN ص11): تظهر فقط عند وفاة Primary — اختيار البديل من العائلة أو None.
3. **صورة + توقيع للزوج/الزوجة** (MPF ص10) ولصورة النادي المتفق معه (MPF ص30) — Upload بالتصفح.
4. **3 تبويبات أسعار** (SET ص7-8) بزر Confirm لكل مصفوفة.
5. **زر البريد** (MPF ص18 + RPL ص33): إرسال التحقق/أمنيات الميلاد + **تحديث البريد بالنقر المزدوج على العنوان**.
6. **أزرار نسخ العناوين** (MPF ص4): "Click on the appropriate Copy button to copy the address".
7. **More Details** (MPF ص13-17): 5 نوافذ عرض (Reference/Personal/Address/Work/Other).
8. **F1 Universal** في كل حقول الأرقام (Membership#/Application#/Receipt...).
9. **استدعاء الشاشة عند الحفظ** (سمات 2-5 + MPF ص23): Receipt Entry تفتح تلقائياً بعد Save.
10. **أزرار Load** (MTR ص17 + SET ص15 + RPL ص33): تحميل بيانات قبل المعالجة.
11. **رسم بياني مدمج** في Pending Complaints: "The count of the pending complaints is shown in the **graph** on the left side of the screen" (RPL ص33).
12. **أزرار إخفاء أعمدة** في Spending Pattern: "options to **hide the count column and the revenue column**" (RPL ص55).

## 4. تدفق التنقل الدوري

- القائمة الرئيسية: Membership → {Setup / Member Profiles / Member Maintenance / Member Transactions / Reports & Lookups} (هيكل 5 رؤوس موثق في مقدمات الأدلة الخمسة).
