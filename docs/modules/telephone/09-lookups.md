# 09 — الاستعلامات (Lookups) — وحدة TEL

> **9 استعلامات (LUK — 21 ص)** — ثلاث فصائل: (1) **تشغيلية هاتفية** (Unbilled/Room Calls/Dial Code)؛ (2) **لوحة عامل السنترال** (Guest Information/Search/In-House)؛ (3) **إنتاجية شخصية** (Address Book/Yellow Pages). + **عرض PMS** (View Transfers/Extensions) بأثر تدقيقي (User+Authorizer!).

---

## 1. View Unbilled Calls (التشخيص) ⭐

| البند | المواصفات |
|---|---|
| الغرض | "list of all calls that are not billed due to various reasons" — أمثلة الدليل: "Calls made from extensions that are **not defined** or calls made from a room that the application identifies as **unoccupied**" |
| المُدخل | Date (افتراضي **Accounting Date**) + **Error Type dropdown** ("the various reasons for which a call may not be billed") |
| التشغيل | "Click Load or hit **Enter twice**" |
| الناتج | "room number, extension number, duration of the call, telephone number, place" |
| الغاية | "the user can get the list of bills that have to be billed and **added to the respective Guest folio**" |
- **الفرق عن REP:** هنا فلتر السبب (تشخيص) — والتقرير سرد شامل؛ الإصلاح الفعلي في CAC §2 (Select YES).

## 2. Room Calls Query

| البند | المواصفات |
|---|---|
| المُدخل | Extension# (F1 — غرفة/قسم/متجر/عام) + From/To Time (**24h**) + include taxes + **P&T Charge / Guest Charge** |
| الناتج | "date/time of call, call type, called number, destination, duration and charges" |
| **الملخص** | "total number of calls made under each call type and the total charges" |
- استعلام لحظي لامتداد واحد — أداة نزيل متصلٍّ يسأل عن فاتورته.

## 3. Dial Code Search

- **مساران:** بالرقم (Dial # → Enter) أو بالمكان (Place Name → Enter).
- الناتج: "any Country's code and name, Area code and Area name and the **minimum and maximum call charges** and the rate slabs".
- أداة عامل السنترال لتحويل مكالمة بتعرفة صحيحة قبل الاتصال.

## 4. Guest Information ⭐ (وحدة تحكم العامل)

| المكوّن | الوصف الموثق |
|---|---|
| المدخل | Name/Room# + **F1 → Room Help** → نقر مزدوج → التفاصيل |
| زر Instructions | "if the Guest has given any instructions regarding the room" |
| زر Complaints | "if the Guest has any complaints regarding the room" |
| زر Messages | "View All Messages" → **Tag → YES** (أُبلّغ) → "will not show in the Guest Page Messages again" |
| زر Guest Location | "where the Guest can be located in the Property" → **Tag → YES** (وُجد) → إخفاء |
| **زر SL# (إداري)** | "for administrative purposes only and used only by the **System Administrator** to resolve **SL# mismatch issues**" |

- **النمط:** رسائل-صفحة كلاسيكية (Paging) بإشعارات تنتهي بالإبلاغ — الرسالة غير المبلّغة تبقى والنية المعلنة "no more required".

## 5. Guest Search

- "in-house guests, reserved guests and checked out guest details" + **Room History** — نافذة PMS كاملة من داخل TEL (غير مفصّلة في الدليل — إحالة ضمنية لبيانات FO).

## 6. In-House Statistics (تفويض FO حرفي) ⭐

- "in-house rooms and pax wise occupancy details room type wise, Status wise, Plan wise, Nationality wise, Company wise, Rate wise etc... guests who have arrived on the current date"
- **التفويض:** "For complete information on this Menu Option – INHOUSE STATISTICS **refer CHAPTER – LOOKUPS of MODULE – FRONT OFFICE**"
- **نمط إعادة الاستخدام الموثقة:** TEL تشير لتنفيذ FO نفسه (لا ازدواج) — أنقى حالة Delegation في المشروع بعد واجهات BNQ=POS.

## 7. Create Address Book (Yellow Pages) — ماستر تفاعلي

- **الغرض:** "record and save frequently called telephone numbers and **create your own Yellow Pages**".
- **الفئتان:** Main (إلزامي 15) — أمثلة: "Hotels, Restaurants, Resorts, Hospitals, Cab Services" · Sub (اختياري 15) — "Luxury and Budget" / "Vegetarian and Non-Vegetarian" / "Chinese and Continental" / "Beach, Hill, Health".
- **العنوانان:** Residence + Office بـ9 حقول لكلٍّ (Address 100/City 30/State 30/Country/Phone 30/Fax 30/**Pager 20**/Email 30/Cellular 20) + Remarks 200.
- **سلوك الفئات:** "Multiple entries under main and sub category can be entered. After the information is entered and saved, the **previous saved categories are displayed**" — تراكمية.
- **التصفح الشامل:** "Panel → Yellow Pages" — "view the whole list of Main Category and Sub Category".
- **التعديل:** Change → Main (Enter) → Sub يُعرض (Enter) → التفاصيل → تعديل.

## 8. Print Yellow Pages

- "hard copy of all the frequently called telephone numbers saved in the Yellow Pages or the address book".
- الفلتر: Main Category → "name, address and contact details of all the matching records".
- الأمثلة التوثيقية للفئة: "Doctors, Hospitals, Theaters, Air / Rail-Ticket Bookings, Hotels, Resorts, and Transport".

## 9. View Transfers/Extensions (نافذة PMS التدقيقية) ⭐

| الراديو | الناتج |
|---|---|
| **Transfer** (الافتراضي) | "all the Transfers of calls from **one room to another**... **old room numbers and the new room numbers** along with the **Guests names**" |
| **Extension** | "extension of Guests' **stay**... guest's name, his **earlier departure date and time and the new departure date and time**. **The User who has worked on this request and the person who has authorized this request** is also displayed" |

- **ملاحظة تسمية:** "Transfers" هنا = تحويلات **الغرف** (بيانات FO) لا تحويلات المكالمات (TE CAC §3) — ازدواج مصطلح "Transfer" داخل الوحدة نفسها! (راجع 13-exceptions).
- **الأثر التدقيقي:** عرض المنفّذ + المعتمِد معاً — نمط مسؤولية مزدوجة نادر التوثيق.

## 10. مصفوفة الاستعلامات

| الاستعلام | المدخل الفوري؟ | يتصل بـFO | يتصل بالتسعير | نمط YES |
|---|---|---|---|---|
| View Unbilled Calls | Accounting Date تلقائي | (فحص الإشغال) | — | — |
| Room Calls Query | F1 | — | P&T/Guest + ملخص | — |
| Dial Code Search | — | — | Min/Max/Slabs | — |
| Guest Information | F1 Room | تعليمات/شكاوى/رسائل/موقع | — | **Tag YES ×2** |
| Guest Search | — | إقامة كاملة + Room History | — | — |
| In-House Statistics | — | **مفوَّضة لـFO** | — | — |
| Address Book | فئات تراكمية | — | — | — |
| Print Yellow Pages | فئة | — | — | — |
| View Transfers/Ext | Date تلقائي | تحويلات غرف + تمديدات | — | — |

## 11. ثغرات الاستعلامات

| الثغرة | التفصيل |
|---|---|
| Guest Search بلا تفصيل | فقرة من سطرين — أعمق استعلام PMS الأقل توثيقاً في الوحدة |
| لا بحث بالاسم في Dial Code | مسارا الرقم/المكان فقط |
| Address Book ملكية فردية؟ | "create **your own** Yellow Pages" — هل يشارك بين المشغلين؟ غير موثق (GAP-TE-P02) |
| رسائل بلا إنشاء | TEL تعرض رسائل FO وتدير إبلاغها — لكن إنشاء الرسائل موثق في FO فقط |
