# 06 — قواعد التحقق (Validations) — وحدة Banquets

> V-BQ-01..30 الحقول والقواعد الموثقة. **الترميز اللوني للإلزام موثق هنا لأول مرة:** "Fields with Blue background color are mandatory fields".

---

## 1. تحققات المرجعيات

| # | التحقق | الشرط | المصدر |
|---|---|---|---|
| V-BQ-01 | Applicable From للروابط | ≥ اليوم (Sessions/Order Types/Currencies) | SET §§1-3 |
| V-BQ-02 | Session Order | "has to **begin with one**" | SET §1 ص5 |
| V-BQ-03 | أوقات الجلسة | "24 hours and **HH:MM** format" | SET §1 ص5 |
| V-BQ-04 | Standard KOT إلزامي | "The Standard KOT type is **mandatory** for every restaurant" | SET §2 ص7 |
| V-BQ-05 | Multi-Currency قبل ربط العملة | "You must tag 'Yes' to Multi-Currency... for the Outlet to be displayed" | SET §3 ص9 |
| V-BQ-06 | Applicable Date (Associated Room/Function Room/Corporate) | "cannot be less than the current date" / "equal to or greater than the **accounting date**" | CFG §1/§5 + SET §18 |
| V-BQ-07 | أكواد آلية غير قابلة للتعديل | Country/City/State/Floor/Reason/ItemType/Equipment/Categories/Policy/Question/Template/ServiceManager — "system generated. You cannot modify" | كل SET/CFG |
| V-BQ-08 | Modify-Locked (الاسم+الحالة فقط) | Country/State/City/Floor/Reason/ItemType/MenuGroup(اسمان)/Features/EventType/Category/SubCat | SET/CFG مواضع متعددة |
| V-BQ-09 | **الحالة فقط** (أشد) | Reservation Status · Associated Room | SET §11 + CFG §1 |
| V-BQ-10 | Event Template — Event Type محظور | "you have to change the Status... to Passive and create a new template" | SET §15 ص67 |
| V-BQ-11 | الأطوال | Country Name — · Floor Long ≤30/Short ≤15 · Reason ≤25 · Item Type ≤25 · Menu Group Long ≤30/Short ≤15 · Reservation Status ≤30 · Category ≤30 · SubCat ≤30 · Equipment ≤30 · Service Manager ≤30 · Property Address ≤99 · Tel/Fax ≤15 (×4) · Menu Item Code **رقمي ≤4** | SET/CFG مواضع متعددة |
| V-BQ-12 | Menu Group Sequence | "cannot be duplicated" + Reservation Status Sequence "Duplicate sequence numbers or empty fields are not allowed" | SET §§9/11 |
| V-BQ-13 | السعة الموصى بها | Setup Style Min/Max Pax | CFG §3 |
| V-BQ-14 | Event Question | "A maximum of **6 answers** can be tagged, out of which **2 answers are mandatory**" | SET §14 ص61 |

## 2. تحققات الحجز والجدولة

| # | التحقق | الشرط | المصدر |
|---|---|---|---|
| V-BQ-15 | نطاق Function Room Availability | "within **three days** and... **more than or equal to the current date**" | LUK §1 ص3 |
| V-BQ-16 | Add on/Associated ضمن الحدث | "not exceeding the Function start & End date & timings" | BOK ص12 |
| V-BQ-17 | تعديل حدث ماضٍ | الحالة فقط | SET §10 ص36 |
| V-BQ-18 | تعديل روابط اليوم | "For the Sessions defined for the **current date**... only the **status**" | SET §1 ص6 |
| V-BQ-19 | No-Show الجماعي | "function dates **lesser than the server date**" (ويعرض ≥ الخادم للانتقاء — الصياغتان معاً) | BOK §2 ص34/35 |
| V-BQ-20 | حظر الحجز التقويمي | Booking Allowed=No → الرفض حسب Booking Made By | SET §10 |
| V-BQ-21 | **إلغاء ذي وديعة ممنوع** | "You cannot cancel Bookings with DEPOSITS... make the paid outs first" | BOK ص28 |
| V-BQ-22 | نسخ Inquiry ممنوع | "Copy of Inquiry Bookings is restricted" | BOK ص34 |

## 3. تحققات الفوترة والتسوية

| # | التحقق | الشرط | المصدر |
|---|---|---|---|
| V-BQ-23 | Reprint نطاق | "The **end date cannot be greater than the current date**" | BIL §7 |
| V-BQ-24 | التسوية في نفس اليوم المحاسبي | "must be settled during the **same accounting date**" | BIL §4 |
| V-BQ-25 | Void ممنوع | "Void Settlement is restricted" (رسالة) | BIL §4 ص27 |
| V-BQ-26 | NC مشروط | "activated **only if** POS Module Attribute number 16... 'Yes'" | BIL §4 ص29 |
| V-BQ-27 | Swipe مشروط | MA 8 | BIL §4 ص22 |
| V-BQ-28 | إعادة تسوية النقدي | MA 3=Yes → ممنوعة (Cash/Foreign Currency) | BIL §4 ص31 |
| V-BQ-29 | Close Shift بمعلقات | MA 26=Yes → "must settle all the pending bills/KOTs" | BIL §5 ص33 |
| V-BQ-30 | Retention/Refund بعد Save | "not able to perform modify\delete... after SAVING" | BIL §10 |

## 4. مصفوفة أنماط التسوية (11)

| النمط | العميل/المرجع | يعمل مع Multiple؟ | يرحّل إلى |
|---|---|---|---|
| Cash | — | نعم (قاعدة المزج) | — |
| Foreign Exchange | Currency (F1) + Exchange Rate | نعم | — |
| Credit Card | Card Type/Company/#/Expiry/Auth + **متعدد** | نعم | **AR** |
| Cheque | #/Date/Bank/Branch | نعم | — |
| Company | Company Code + Available Credit | نعم | **AR (outstanding)** |
| Guest | Room# (بيانات الضيف الكاملة) | نعم | **FO Folio** |
| Staff | Staff Code (بحث ديناميكي) | نعم | **AR** |
| Void | — | — | **ممنوع في BNQ** |
| Coupons | Coupon# | [NOT DOCUMENTED] | — |
| Complimentary | — | لا | (ليست مبيعات) |
| Non Chargeable | NC Type + Dept + Guest | لا | (ليست مبيعات) |
