# 01 — البيانات الرئيسية (Master Data) — وحدة TEL

> **8 ماسترات صمّاء + 1 ماستر إدخال تفاعلي**: الامتدادات (بشرائح الحساب الرباعية) · روابط التوائم · أكواد الدول (بشراكة LCA/9999999999) · أكواد المناطق (بحدود دنيا/عليا وأشرطة شراكية ×3) · الشرائح الزمنية-النبضية (غير قابلة للتعديل!) · جدول الأعياد (بمولد أيام الأسبوع) · معرّف المكالمة (بادئات) · دفتر العناوين (ماستر تفاعلي بفئتين و عنوانين). ما عدا Address Book كلها **استاتيكية تُستهلك بمحرك التسعير**.

---

## 1. ماستر الامتدادات (Telephone Extensions)

| الحقل | المواصفات | ملاحظات |
|---|---|---|
| Extension # | رقمي ≤6 محارف | مفتاح الهوية |
| Extension (النوع) | قائمة: **Room / Department / Shop/Public** | يوجه حقل "النوع التالي" |
| Property | قائمة من SYS | تعيين عقاري |
| Extension Info | Department/Room # أو Shop # حسب النوع | "If you selected the Extension 'Room', then the cursor will move to the Room # field" — انتقال مؤشر ذكي |
| Calculation % (Local) | رقمي ≤3 | 100=كما هو · 150=×1.5 · 200=×2 · 0=مجاني |
| Calculation % (STD) | رقمي ≤3 | **0% ممنوعة** |
| Calculation % (IDD) | رقمي ≤3 | **0% ممنوعة** |
| Calculation % (Others) | رقمي ≤3 | "حد أدنى" أو 00.00 للمجاني |
| Extension Name | نصي ≤30 | اختياري — "enables you to identify one extension from the other" |
| Extension Type | **Phone / Fax** | ثنائية جهازية |
| Equipment Code | نصي | اختياري — كود المعدة الهاتفية |
| Location Details | نصي | اختياري |

- **قاعدة القسم الحاسمة:** "Calls recorded from any of the departments are **charged at the normal Service Provider's rates**" — امتدادات الأقسام لا تُربّح (بلا نسبة فندقية) — منطق "المكالمات الإدارية تكلفة".
- **التعديل:** عبر F1/النقر المزدوج على Extension # → شاشة Browse → اختيار → تعديل → حفظ (SET ص6).

## 2. روابط الامتدادات (Link Extensions)

| العنصر | الوصف |
|---|---|
| الغرض | "linking of extensions is mainly useful for extensions provided in **Twin Rooms, Banquets, shops and Public rooms**" |
| القاعدة التشغيلية | "The Extensions in Linked Rooms **must be linked** using this option **so as to avoid errors during billing**" — إلزامي لغرف التوائم |
| البنية | Main Extension (F1 Browse) + Linked Extn Details (متعددة) |
| التعديل | حذف روابط فردية أو **Delink All** بنافذة تأكيد منبثقة |
- **الدلالة المعمارية:** تحويل مكالمات الغرفة التوأم لفوليو المالك الفعلي — تجميع امتدادات تحت هوية فوترة واحدة.

## 3. جدول الأعياد (Holiday Table)

| الحقل | المواصفات |
|---|---|
| Date | "should be **greater than the accounting date**" — ddmmyy |
| Day | **تلقائي** من التاريخ |
| Occasion | اسم العيد (مثال: Christmas) |

- **Auto Generation:** "to view the dates of entire weekdays for a given date range... you can know on what all dates Monday... Tuesday... appears" — اختيار يوم أسبوع (الأحد-السبت) + From/To → Generate → قائمة كل تواريخ اليوم المختار → تُدرج في جدول الأعياد. الغرض: "a day where **discounted call charges** are applied" — التعرفة المخفضة تُبنى على أساس أيام الأسبوع كاملة (عطل أسبوعية)!
- **الاستهلاك:** "All the calls (Local / STD / IDD) have a **different rate during Holidays** than the Regular days. The holiday list is defined **based on the country**" — تُقرأ في Time-Rate Slabs (قسم Holidays).

## 4. أكواد الدول (Country Codes)

| الحقل | المواصفات |
|---|---|
| Country Code | أبجدي-رقمي ≤10 |
| Name | ≤30 |
| Status | Active/Passive |

- **تعديل مقيد:** "In the modify mode, you can modify the **Country Name and Status**... but **cannot modify the Country Code**" — ثبات الهوية.
- **الشراكتان الإلزاميتان:**
  1. **LCA** — "This code will be used to tag a slab code for local call charge calculation"
  2. **9999999999 / "Country Code Not Defined"** — "used to tag a slab code for countries that are not defined"

## 5. أكواد المناطق (Area Codes)

| الحقل | المواصفات |
|---|---|
| Country Code | اختيار (مفتاح خارجي لأكواد الدول) |
| Area Code | أبجدي-رقمي ≤10 |
| Area Name | ≤30 |
| Slab Code | F1 — "used to calculate the call charges" |
| Minimum Charge | "If you give a minimum rate charge then **this will overwrite the Slab code**" |
| Maximum Charge | كذلك — سقف يسقف ناتج الشريحة |

- **الشراكات الثلاث الإلزامية (حرفياً):**
  - (A) Country: **LCA** / Area: **LCA** / "LOCAL CALL" / شريحة محلية
  - (B) Country: **9999999999** / Area: **9999999999** / "Country Code Not Defined" / **أعلى شريحة IDD**
  - (C) Country: **فارغ** / Area: **9999999999** / "Area Code Not Defined" / **أعلى شريحة STD**
- **قاعدة اقتصادية دفاعية:** المكالمة غير المعرفة تُسعَّر بأغلى شريحة من فئتها (لن يخسر الفندق لأن بياناته ناقصة).

## 6. الشرائح الزمنية-النبضية (Time-Rate Slabs) ⭐

> **أغنى ماستر في الوحدة — والوحيدة غير القابلة للتعديل.**

| الحقل | المواصفات |
|---|---|
| Applicable From | ddmmyy — "You must enter a date **greater than the current date** to activate the setting active for a future date" |
| Slab Code | F1 للسابقة — "cannot select a slab code that was **created on the same date**" (سابقة فقط) |
| Name | ≤30 "based on the call type" |
| Currency Code | F1 من SYS (عملة الشريحة!) |
| From Time | **نظامي تلقائي 00.00** |
| To Time | إدخال — بعد الإدخال "press Enter twice" لفتح قسم الأسعار |

**قسم الأسعار (بعد Enter ×2):** جدولان — **Regular Days** و**Holidays**، لكل منهما عمودان:

| صاحب التعرفة | Seconds (طول النبضة) | Rate (سعر النبضة) |
|---|---|---|
| **P&T (Post & Telegram)** = مزوّد الخدمة | — | — |
| **Hotel** | — | — |

- **الحتمية الزمنية (مع مثال رقمي):** "You **cannot Modify or Delete** a time rate slab record. If you want to make changes... **Add a new record with the same slab code but with a new applicable from date**... it will consider the call rates from the record that has the **latest applicable from date**" — مثال: شريحة "1" بتاريخين 18-Dec-2011 و1-Jul-2012 → التسعير يستخدم **2012**.
- **عائلة التوثّق الزمني:** الرابعة في المشروع (بعد Rate Master/HRP، Service Rate/MEM، Corporate Rate/BNQ) — كلها "أحدث سريان يفوز".

## 7. معرّف المكالمة (Call Identifier)

| الحقل | الوصف |
|---|---|
| Code | "The code is the **initial portion of the called number**" — بادئة الرقم المطلوب |
| Call Type | Local / STD / IDD / Others |

- **مثال التصنيف الحرفي:** "one zero at the beginning are STD, two zeroes are IDD and no zeroes are Local. **09986056565, 005674886754, 9980688744**"
- **التعديل:** حذف السطر ثم إضافة سطر جديد (لا تعديل موضعي!) — "Delete the code or call type that the user want to modify. Enter the new code or call type".

## 8. دفتر العناوين (Create Address Book) — ماستر تفاعلي

| الحقل | المواصفات |
|---|---|
| Main Category | **إلزامي** ≤15 — أمثلة موثقة: Hotels, Restaurants, Resorts, Hospitals, Cab Services |
| Sub Category | اختياري ≤15 — "Luxury and Budget" تحت Hotels · "Vegetarian/Non-Vegetarian" · "Chinese/Continental" · "Beach, Hill, Health" |
| Prefix | ≤10 |
| Name | ≤45 |
| Residence Address / Office Address | كتل مزدوجة (أدناه) |
| Address | ≤100 |
| City | ≤30 |
| State | ≤30 |
| Country | — |
| Phone # | ≤30 |
| Fax # | ≤30 |
| **Pager #** | ≤20 (إرث تقني موثق!) |
| Email | ≤30 |
| Cellular # | ≤20 |
| Remarks | ≤200 |

- **"Panel" → Yellow Pages:** "You can also view the whole list of Main Category and Sub Category if you click the **'Panel' button**... and then click **'Yellow Pages'**" — قناة تصفح شاملة.
- **التعديل:** Change → Main Category (Enter) → Sub Category يُعرض تلقائياً (Enter) → التفاصيل تظهر → تعديل → Save.

## 9. خريطة الاستهلاك (أي ماستر يقرأه أي محرك)

| المستهلك | ما يقرأه |
|---|---|
| محرك التسعير (الاستقبال) | Call Identifier (التصنيف) → Country/Area (الشريحة/الحدود) → Time-Rate Slab (النبض/السعر عادي-عيد) → Holiday Table (نوع اليوم) → Calculation % (الامتداد) |
| محرك الترحيل | Revenue Posting (Consolidate + Rev Code لكل نوع) |
| بوابة الامتداد | Activate/Deactivate + بوابات Local/STD/IDD |
| كلمة المرور | الامتداد/الغرفة المشغولة + Reg# |
| التقارير | كل الماسترات (Telephone Master List بثلاثة أنماط) |
