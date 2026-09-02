# 15 — تحليل تجربة الاستخدام (UX Analysis) — وحدة Banquets

> أنماط التفاعل الأصلية واستخلاصها للواجهة الجديدة (RTL Arabic-First). BNQ تحمل **أفضل لوحة عمليات موثقة** (Availability Chart) وأثقل نموذج إدخال (Make Booking 7 أقسام).

---

## 1. الأنماط الموثقة

### 1.1 لوحة القيادة (Availability Chart)

- قسمان (تفاصيل أعلى + مصفوفة قاعات ملونة أسفل) + شريط تاريخ (Back/Next) + **حالة ساعية**.
- ألوان موثقة: 4 حالات حجز (قابلة للتخصيص) + Management أحمر/Maintenance أخضر (مع *) + FP أزرق/بنفسجي + restricted رمادي + Across-Dates داكن.
- **إجراءات من الرسم:** زر Booking + نقر مزدوج Amend — "Command Center" حقيقي.
- **تخصيص الأعمدة/الصفوف** (بإعادة تحميل — عيب يُصلح).

### 1.2 نموذج الحجز المتعدد الأقسام

Make Booking بـ 7 أقسام: Party → Company → Booking Info → Billing → Payment Terms → Main Function Room → Other Details — **كل قسم بأزرار توسعة (…) للتفاصيل** (Address/Handled-By/Payment Details/الغرف الإضافية...).

### 1.3 الاختصارات الموثقة

| الاختصار | الوظيفة | المصدر |
|---|---|---|
| **F11** | No-Show جماعي (اختيار متعدد) / **إعادة تسمية صنف في Requirement** | BOK §2 + BIL §11 |
| **F12** | **جعل الصنف Complimentary** | BIL §11 |
| **F1/نقر مزدوج** | كل المساعدات (Rooms/Companies/Items/WorkSheet...) | الوحدة كلها |
| **F5** | حذف سجل Corporate Rate | SET §18 |
| **أسهم أعلى/أسفل** | تصفح >4 أحداث في مربع اليوم | SET §10 |
| Enter | انتقال Details→Features (في Function Room) + تفعيل الاختيار | CFG §5 + CFG §11 |
| **السحب الأفقي** | "sliding the horizontal bar" (نطاق Availability) | LUK §1 |

### 1.4 الترميز اللوني الوظيفي (أغنى وحدة)

| اللون | الدلالة | السياق |
|---|---|---|
| **أزرق خلفية الحقل** | **إلزامي** — "Fields with Blue background color are mandatory" | كل النماذج |
| أخضر | الصف المفعّل في User Access + صنف supplementary | SET §20 + BIL §3 |
| وردي | حجز ملغى | BOK Search |
| أحمر/أخضر + (*) | Management/Maintenance Block | LUK §1 |
| أزرق/بنفسجي | FP Printed/Finalized | LUK §2 |
| رمادي | قاعة محظورة الحجز | LUK §2 |
| داكن | Across-Dates | LUK §2 |

### 1.5 المحركات الذكية

- **Copy Requirement Entry Engine:** بحث بـ 9 معايير (Res#/Party/Company/Pax/Property/Function/Room/FunctionDate/ReservationDate) → View/Copy — محرك إعادة استخدام.
- **Scan & Search Engine:** بحث حر + فرز (Function Date/Reservation Date) + فلتر الملغاة.
- **البريد الآلي** (بعد الحجز) — بشرطي PDF + Outlook Express (تقنية 2000s تُستبدل بـ SMTP/Notification).

## 2. عيوب UX الموثقة (تُصلح)

| العيب | الدليل | الإصلاح |
|---|---|---|
| إعادة التحميل بعد تخصيص الأعمدة | "the program exits. You have to load the program again" | حفظ فوري + تحديث React |
| نموذج 7 أقسام بواحد | Make Booking | Stepper عربي RTL بأقسام |
| منع التعديل الجوهري | "cannot be deleted, only status can be changed" ×9 | سياسة إصدارية واضحة + أسباب |
| التقويم محدود 4 أحداث/مربع | سهم أزرق + لوحة مفاتيح | قائمة منبثقة + Popover |
| Outlook Express | auto email | SMTP قياسي + قوالب |

## 3. توصيات الواجهة الجديدة

1. **صفحة "لوحة الولائم"**: Availability Chart كـ Command Center (مصفوفة قاعات×ساعات ملونة + شريط أيام + إجراء حجز/تعديل بالنقر) — **أعلى أولوية ترجمة في الوحدة**.
2. **معالج حجز من 7 خطوات** (Party→Company→Info→Billing→Terms→Room→Details) بحفظ جزئي واسترجاع.
3. **بطاقة حدث** موحدة (مثل Guest Folio في FO): الحجز + المتطلبات + الوديعة + الفاتورة + التسويات في صفحة واحدة بتبويبات.
4. **محرر ورقة متطلبات**: F11/F12 يتحولان لأزرار ظاهرة (إعادة تسمية/مجاني) + عدّادات Allowed لكل مجموعة.
5. **مقياس توفر 3 أيام** بسلايدر + Popover للتفاصيل.
6. **شارة الوديعة الحاجبة** على الحجز (5 قواعد EC-BQ) بألوان تحذير.
7. **نموذج قاعة 6 تبويبات** كما هو (Details/Features/Seating مع صور/Pictures/Layout/Location) + معاينة معرض صور.
