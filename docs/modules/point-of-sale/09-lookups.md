# 09 — الاستعلامات واللوحات (Lookups) — وحدة POS

> POS-LUK (7 استعلامات تفاعلية) + شاشات الانتظار (Pending) + المساعدات — كلها **مقيَّدة بالمنفذ** أولاً (نمط POS الأصيل).

---

## 1. الاستعلامات التفاعلية السبع

| ID | الاستعلام | السلوك التفاعلي | المصدر |
|---|---|---|---|
| L-POS-01 | **Pending KOTs** | Outlet (أو Table/Room #) → Load: Restaurant Code · Table/Room · KOT # · Session · Date · Items · Server + إجماليات Qty/Amount + Clear لإعادة الاستعلام | LUK §1 |
| L-POS-02 | **Pending Bills** | Outlet → Enter×2/Load: Date · Session · Table/Room · **Res/Bill #** · Amount · Time · Server · User · Total + **Double-click لتفاصيل الفاتورة** | LUK §2 |
| L-POS-03 | **Table Booking Status** | Date (**≥ اليوم و< Table Reserved Date**) + Restaurant → Date/Time · Reservation # · Covers · Guest Name · Phone # · Table # · **Special Instruction** · Items + **"Defined" → الطاولات المحجوزة للضيف** | LUK §3 |
| L-POS-04 | **Browse KOTs** | Month/Year + Restaurant + **Search By: KOT# / Bill#** → القائمة | LUK §4 |
| L-POS-05 | **Settlement Summary** | Outlet + Date (**≤ تاريخ المحاسبة**) + Session + ☐ للأنماط (cash/credit/cheque/forex/coupon) → تفاصيل + **إجماليات كبرى لكل نمط** | LUK §5 |
| L-POS-06 | **Session Statistics** | Outlet (**المخوَّلة فقط**) + Session + **Void/Comp ☐** → الإحصاءات + أزرار: **NC KOT** (Guest/Type/Amount) · **KOT Audit** (Old/New) · **Happy Hours** (slot + comp item + qty + groups + %) · **Void/Comp/BOH** (bill type/#/amount/server/**reason**) · **Table Booking** · **Menu Movement** (Current/All Sessions) + **Average Per Check + Covers** | LUK §6 |
| L-POS-07 | **Consolidated Sales** | Process → ملخص لكل منفذ: نوع قائمة × تحصيل (Cash/Credit منفصلين) | LUK §7 |

## 2. نوافذ الانتظار كمؤشرات تشغيل حية

| النافذة | المعلومات | دلالة الحالة | المصدر |
|---|---|---|---|
| Pending KOTs | طلبات بانتظار الفوترة | KOT **بلا Check** | LUK §1 |
| Pending Bills | فواتير بانتظار التسوية | Check **بلا Settlement** | LUK §2 |
| **حالة الفاتورة في التسوية** | **"Settled / Pending / Cancelled"** | عرض صريح بثلاث حالات | TS ص33 |
| أيقونات الطاولات | **Waiter = مشغولة** · **Printer = مطبوعة غير مسوّاة** | تمييز بصري | TS ص16/41 |
| ألوان Layout | **G=Vacant · R=Occupied · B=Billed · Y(Brown)=Reserved** | خريطة الحالة | POS-SET §39 |

## 3. المساعدات (Help) الموثقة

| المساعدة | الاستدعاء | المصدر |
|---|---|---|
| Item Code Help (F1) | حقول الأصناف | POS-SET |
| Guest Name/Information Help (F1) | Guest History + **"(The module and Guest Code appear beside the name)"** | POS-GST §3 |
| Table Help (**"?"**) | Check # / Table # في التسوية والطباعة | TS ص32/40 |
| Sessions/Servers/Kitchens/Currencies/Groups/Modifiers | كل حقول الإعداد | POS-SET |
| Member Section | Member Discount (مع Guest Name بحث) | POS-SET §41 |
| **Details** (تفاصيل الضيف) | نتائج بحث Guest History → عرض Guest Master | POS-GST §4 |

## 4. محركات البحث العميقة (Guest History)

- **معايير أساسية:** Guest information · Company name · Address.
- **معايير موسعة (More):** **Total Visits (تقريبي + مدى!)** · **Total Revenue (تقريبي + مدى)** · **Visit From (تقريبي + مدى)** · DOB شهر (Guest/Spouse) · **Anniversary (MM)** — "You can enter an approximate value" (بحث تقريبي نادرة التوثيق!) (POS-GST §5).

## 5. زوايا العرض التشغيلية

| الزاوية | الاستعلام | المصدر |
|---|---|---|
| المنفذ | كل الاستعلامات (نمط POS) | LUK |
| الجلسة | Session Statistics · Settlement Summary | LUK §5/§6 |
| الكاشير/النادل | Pending (Server column) · Session Statistics | LUK |
| الضيف | Guest History + Visit Details | GST |
| نوع التحصيل | Settlement Summary · Consolidated Sales | LUK §5/§7 |
