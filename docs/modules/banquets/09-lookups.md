# 09 — الاستعلامات (Lookups) — وحدة Banquets

> استعلامان فقط لكنهما **أغنى لوحتي عمليات في المشروع**: التوافر اليومي والرسم البياني الشامل.

---

## 1. Function Room Availability (التوافر القصير)

**المصدر:** BNQ-LUK §1 ص2-4.

| البند | الموثق |
|---|---|
| النطاق الزمني | "date range of **maximum three days**" و **≥ التاريخ الحالي** |
| الافتراضي | Property + Current date |
| الفلاتر | checkbox **'Function Room Block'** (عرض المحظورات) + "User Defined Reservation Type/s" (عدّ الغرف تحت كل حالة) |
| العرض | "start and end time until when the function room is booked" + **ال Hourly status** أسفل التفاصيل |
| الترميز اللوني | المحظور بـ **asterisk (*)**: **Management = أحمر · Maintenance = أخضر** — (راجع 05 BR-BQ-03) |
| التقويم | "Maximum date range can be viewed by **sliding the horizontal bar**" |

## 2. Availability Chart (لوحة العمليات الشاملة)

**المصدر:** BNQ-LUK §2 ص4-12.

### 2.1 البنية (قسمان)

**القسم العلوي (التفاصيل):** "Function room name, Reservation Status, Reservation contact details, Event Date & Timings, Event name, Res#, Party Name, Expected\Guaranteed Pax, Room charges, Pax Rate, Transaction amount, Transaction date and User id" — الحالة ملوّنة من Reservation Status (SET §11).

**القسم السفلي (المصفوفة):** "all the Function rooms defined in that property and the availability... with certain colors for each reservation status" + **ال Hourly status** أسفلها.

### 2.2 السلوك الموثق

| السلوك | النص/الدلالة | المصدر |
|---|---|---|
| التنقل الزمني | **Back/Next** — "previous dates as well as future dates" | ص5-6 |
| **دمج الحالات** | "All the user defined reservation status will be **compacted\combined to their basic reservation types**... under the four basic reservation status (Inquiry, waitlist, provisional, Confirmed)" — **إلا INI 408=1** | ص5/7 |
| **Across Dates داكن** | "The grid in Function date & Time **darkened** indicates that the booking done is 'Across dates'" | ص5 |
| **Dry Days** | "will appear for the days as defined in the Setup Event Calendar" | ص9 |
| **زر Booking** | "make a new booking... only if you have User Access Rights" | ص9 |
| **Amend** | نقر مزدوج على Res# — "only for the current or future date" + User Authorization | ص10-11 |
| **FP ألوان** | Printed = أزرق · Finalized = بنفسجي | ص12 |
| **Room restricted = رمادي** | قاعة محظورة الحجز | ص12 |

### 2.3 التخصيص الشخصي (أول تخصيص أعمدة موثق في المشروع!)

| الأداة | القاعدة |
|---|---|
| **Columns Order** | ترتيب أعمدة القسم العلوي — "type the new number... **cannot be left blank or zeros**" + Save → **"the program exits. You have to load the program again"** |
| **Function Room Order** | ترتيب صفوف القاعات السفلي — نفس القاعدة + إعادة التحميل |

## 3. أنماط UX المستخلصة

1. **لوحة Command Center:** Availability Chart = نموذج React جاهز (قسم تفاصيل + مصفوفة ملونة + مفتاح ألوان + شريط تاريخ) — **المكون الأعلى قيمة ترجمة في الوحدة**.
2. **الدمج التجميعي للحالات** (اختصاري 4 أنواع) مقابل التفصيل (INI 408) — نمط toggle عرض.
3. **إعادة تحميل بعد التخصيص** — في الجديد: حفظ فوري بلا إعادة تحميل (تحسين UX مؤكد).
4. **التقويم الأفقي الانزلاقي** (سلايدر أيام) لعينة 3 أيام.
