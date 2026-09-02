# 05 — قواعد العمل (Business Rules) — وحدة POS

> 16 مجموعة (BR-POS-01..16) — كل قاعدة بمصدرها. قواعد TS (العمليات) هي الأكثر حسمية للسلوك اليومي.

---

## BR-POS-01 · قواعد المنفذ (Outlet)

| # | القاعدة | المصدر |
|---|---|---|
| 1 | **النقد وضع تسوية إلزامي لا يُستثنى لأي منفذ** | POS-SET §17 ص50 |
| 2 | الأنماط الفاعلة في التسوية حصراً: Cash/CC/Cheque/Coupon/Guest/Void — "Others will not work" | TS ص32 |
| 3 | التعديل الإصداري: سجل اليوم = Status فقط؛ سجل المستقبل = كل الحقول؛ التعديل اللاحق = **سجل جديد بتاريخ > تاريخ المحاسبة** | POS-SET §1 ص10 (ونمطها في §2/§3/§7...) |
| 4 | Link Outlet Currencies يظهر المنفذ **فقط إذا Multi Currency=Yes** | POS-SET §6 ص24 |
| 5 | فتح Outlet شخص واحد + التاريخ المحاسبي آلي (= Bill Date)؛ تغيير Session = إعادة فتح بلا إغلاق | TS ص5 |
| 6 | فتح Shift لكل كاشير؛ تغيير الوردية يستلزم إغلاقها أولاً | TS ص4 |

## BR-POS-02 · قواعد KOT

| # | القاعدة | المصدر |
|---|---|---|
| 1 | **Standard KOT إلزامي لكل مطعم** ("The Standard KOT type is mandatory for every restaurant") | POS-SET §5 ص21 |
| 2 | KOT # Type لكل ربط: Auto Generation / Validate KOT book / Manual Entry | POS-SET §5 ص22 |
| 3 | **كتاب KOT ≤ 100 ورقة**؛ التعديل = اسم المستلم فقط | POS-SET §30 ص94-95 |
| 4 | حذف/تعديل صنف في KOT ⇒ **Reason إلزامية** (معرَّفة أو جديدة) | TS ص17 |
| 5 | طباعة KOT **في مطابخ الأصناف** (Kitchen لكل صنف)؛ الشبكة بـ Module Attribute 32 | POS-SET §15 + TS ص15 |
| 6 | Purge KOT: لنوع **Validate** حصراً + **Void أولاً** | POS-SET §37 ص108-109 |

## BR-POS-03 · قواعد الفاتورة (Check)

| # | القاعدة | المصدر |
|---|---|---|
| 1 | طباعة Check متاحة **فقط للطاولات ذات KOT** | TS ص23 |
| 2 | **Print Bill يسوّي نقداً تلقائياً** ("Print Bill and Settle it to Cash automatically") | TS ص24 |
| 3 | **Provisional/Dummy Bill = Check برقم فاتورة صفر** | TS ص24 |
| 4 | **إعادة الطباعة قبل التسوية: إلغاء الرقم القديم + توليد رقم جديد** | TS ص41 |
| 5 | ترقيم الفواتير بدورة: **Yearly (Init Date DDMM) / Monthly / Daily / None** | POS-SET §1 ص7-8 |
| 6 | Round Off للفاتورة: None/Nearer/Higher/Lower (لكل عملة في المنفذ) | POS-SET §1/§6 |

## BR-POS-04 · قواعد التسوية (Settlement)

| # | القاعدة | المصدر |
|---|---|---|
| 1 | **Balance = 0.00 إلزامية قبل الحفظ** — "otherwise check will not be settled" | TS ص33 |
| 2 | تسوية Guest: **Room # → Enter → الضيف من الجدول** — و**AR/Company/BoH = نفس نمط Guest** | TS ص36 |
| 3 | CC: **السحب يلتقط التفاصيل آلياً** + Tips اختياري | TS ص34 |
| 4 | **Resettlement**: فاتورة مسوّاة → استفتاء "Do you want to resettle it?" → YES → وضع آخر | TS ص36 |
| 5 | Cash: المبلغ المستلم → **Balance = الباقي للضيف** | TS ص34 |
| 6 | Tips حقول في CC/الشيك/Guest (ليست في Cash/القسيمة) | TS ص34-36 |

## BR-POS-05 · قواعد التقسيم والدمج (Split/Link)

| # | القاعدة | المصدر |
|---|---|---|
| 1 | تقسيم **3 طرق**: متساوٍ (عدد) · بالأصناف (Split column) · **بالكميات (كسرية مسموحة: 0.5!)** | TS ص28-31 |
| 2 | الكمية المقسومة **أقل من الكمية الفعلية** ("Value should be less than the actual item quantity") | TS ص31 |
| 3 | Link Tables: طاولة رئيسية + مرتبطات → **فاتورة واحدة** (اختيار أي طاولة يعرض الكل) | TS ص43-44 |
| 4 | Table Suffix: طاولة مؤقتة — **مجموع الخانات ≤ 6** | TS ص45 |
| 5 | طباعة الفواتير المتقسمة: **المحدد فقط، أو تتابعياً عند تحديد الكل** | TS ص30 |

## BR-POS-06 · قواعد القوائم والأسعار

| # | القاعدة | المصدر |
|---|---|---|
| 1 | Menu Master بنمطين بقرار **Module Attribute 29** (مشترك/لكل منفذ) | POS-SET §24 |
| 2 | نقل الأصناف بين المنافذ: **تطابق العملات الأجنبية** بين المصدر والهدف | POS-SET §25 ص78 |
| 3 | Quick Menu Update: **Option 1 فوري** (إعادة تحميل) / **Option 2 من الغد** | POS-SET §28 |
| 4 | Batch Rate Change: All أو Range + **عمود Tax قابل للتغيير** | POS-SET §29 |
| 5 | Item Code **numeric ≤4** | POS-SET §24 |
| 6 | **Open Item: غير قابل للتعديل بعد الإنشاء** (حذف + إعادة) | TS ص21 |

## BR-POS-07 · قواعد الخصومات

| # | القاعدة | المصدر |
|---|---|---|
| 1 | Manual: % أو Amount + **Reason إلزامية** + Discountable Amount آلي | TS ص25 |
| 2 | Predefined: من **Revenue Discount** (المعرفة على الشركات — راجع ACR) | TS ص26 |
| 3 | Happy Hours: **Type A (مبلغ) للصنف فقط** — المجموعات نسبة % حصراً | POS-SET §31 ص96 |
| 4 | Happy Hours: نسبة لكل يوم أسبوع أو All | POS-SET §31 |
| 5 | **تداخل الفترات الزمنية ممنوع**: "Time slot overlaps with existing Time slot" | POS-SET §31 ص98 |
| 6 | تعديل Happy Hours جارٍ اليوم: **سجل جديد من الغد** + رسالة "This modification will be effect from next day" + **From Date ≤ اليوم = معطّل** | POS-SET §31 ص98 |
| 7 | **Passive لا يُعاد Active** — سجل جديد حصراً | POS-SET §31 ص98 |
| 8 | Member Discount: منفذ × نوع قائمة + **INI 404** (1=رئيسي/0=رئيسي+ثانوي) | POS-SET §41 |
| 9 | Sales Promotion: **Main Item واحد على الأقل إلزامي** + Calculation (Min/Max/Avg/None) + أيام السريان | POS-SET §32 |

## BR-POS-08 · قواعد NC

| # | القاعدة | المصدر |
|---|---|---|
| 1 | NC KOT يُرفع **لقسم معرَّف في Departments for NC** (داخلي أو خارجي Tax/Justice/Health) | POS-SET §7 |
| 2 | NC أقسام خارجية = **مصروفات التقادم** عبر Open Items Definition (**NC Cost %** لكل نوع قائمة) | POS-SET §19 |
| 3 | Over Ride NC Bill Print (علم المنفذ) **يتجاوز Module Attribute #6** | POS-SET §1 ص8-9 |
| 4 | Promo/Comp يجعل **قيمة الصنف صفراً** | TS ص21-22 |

## BR-POS-09 · قواعد الإقفال اليومي

| # | القاعدة | المصدر |
|---|---|---|
| 1 | Close Shift: **لكل كاشير + Password** — و**KOTs/Bills معلقة تحجب** | TS ص46 |
| 2 | Close Outlet: شخص واحد + تأكيد — و**المعلقات تحجب** | TS ص46 |
| 3 | تسلسل التشغيل: Shift فردي/Outlet جماعي — فتح الوردية شرطها إغلاق سابقتها للتغيير | TS ص4 |

## BR-POS-10 · قواعد الضيوف (POS Guest History)

| # | القاعدة | المصدر |
|---|---|---|
| 1 | POS Guest Master **مقيَّد بالمنفذ** (اختيار Outlet أولاً) + **Guest Code آلي** | POS-GST §1 |
| 2 | Post Guest History: التاريخ **≤ تاريخ المحاسبة** | POS-GST §4 |
| 3 | الضيف غير موجود ⇒ **إنشاء سجل من نفس المسار** | POS-GST §4 |
| 4 | **Privilege Card types معرَّفة في FO** ("defined in the Front Office Module") | POS-GST ص10 |
| 5 | **تفضيلات FO تُعرض في POS** ("captured in Guest Preferences option of Front Office... will be shown here") | POS-GST ص18 |
| 6 | Loyalty Card # **≤15 alphanumeric** + Join Date ≤ تاريخ الخادم | POS-GST §3 |

## BR-POS-11 · قواعد الطاولات والحجز

| # | القاعدة | المصدر |
|---|---|---|
| 1 | Table # **≤5 alphanumeric** + Covers ≤3 numeric — **التعديل: Covers + Location View فقط** | POS-SET §12 |
| 2 | ألوان الحالة في Layout: **أخضر شاغرة/أحمر مشغولة/أزرق مفوترة/بني محجوزة** | POS-SET §39 ص112 |
| 3 | نسخ تصميم بين الأرضيات **بلا أسماء الطاولات** | POS-SET §39 ص115 |
| 4 | Table Booking Status: تاريخ الاستعلام **≥ اليوم و< Table Reserved Date** | POS-LUK §3 ص6 |
| 5 | Minimum Cover Charge لكل Session في المنفذ | POS-SET §4 |

## BR-POS-12 · قواعد الصلاحيات

| # | القاعدة | المصدر |
|---|---|---|
| 1 | POS User Access: **كاشيرو POS فقط** × عمليات **KOT/Billing/Settlement** × **Applicable To (Regular/Touch/PDA)** | POS-SET §20 |
| 2 | Restrict Outlet Access: تقييد مستخدم عن منافذ (الافتراضي: الكل) | POS-SET §21 |
| 3 | Session Statistics: **رؤية المنافذ المخوَّلة فقط** ("only those outlets... to which you have access rights") | POS-LUK §6 ص11 |

## BR-POS-13 · قواعد الطباعة

| # | القاعدة | المصدر |
|---|---|---|
| 1 | **تفعيل النموذج إلزامي قبل الطباعة** (Make Project Active) — النموذج النشط يطبع | POS-SET §23 |
| 2 | **Header + Footer + Body = طول الورقة** و**6 صفوف = 1 بوصة** | POS-SET §23 |
| 3 | **Body Details إلزامي في النموذج** | POS-SET §23 |
| 4 | طابعات **كل المطابخ إلزامية** في Open Items Definition | POS-SET §19 |
| 5 | أنواع النماذج: Bill/KOT/NC Bill/Invoice + Normal/Slip printer | POS-SET §23 |

## BR-POS-14 · قواعد التقارير والإحصاء

| # | القاعدة | المصدر |
|---|---|---|
| 1 | **Average Per Check = Settlement Amount ÷ No. of Bills** (صيغة نصية موثقة!) | POS-LUK §6 ص12 |
| 2 | POS Report Options تحدد شمول **Void/Complimentary** لكل تقرير | POS-SET §18 |
| 3 | KOT Audit يعرض **Old وNew** للمراجعات | POS-LUK §6 ص12 |
| 4 | DSR Session Group: **≤3 فئات** | POS-SET §36 |
| 5 | Settlement Summary: أنماط cash/credit/cheque/**foreign exchange**/coupon + الصافي | POS-LUK §5 |

## BR-POS-15 · قواعد الأصناف والمطبخ

| # | القاعدة | المصدر |
|---|---|---|
| 1 | **"Every item must be tagged to the kitchen"** | POS-SET §15 ص44 |
| 2 | Modifiers: حذف المعدِّل **ممنوع إذا كان في Group** (F5) | POS-SET §27 ص84 |
| 3 | Menu Level: التعديل = Name + Status فقط | POS-SET §11 ص37 |
| 4 | Item Hot Keys: التعديل = Status فقط (لا عرض للمفاتيح — إسناد جديد) | POS-SET §13 ص41 |
| 5 | متاح Applicable From للصنف (Per-Outlet) + **Available Hours** | POS-SET §24 |

## BR-POS-16 · قواعد التقييم والملاحظات

| # | القاعدة | المصدر |
|---|---|---|
| 1 | Guest Comment Entry **يتطلب Survey Template معرَّفاً مسبقاً** لكل منفذ | POS-GST §10 |
| 2 | Complaint: **Department + Nature + Date/Time** | POS-GST §1 |
| 3 | Comment Analysis: "Guest Acceptance Audit" لمدى زمني (التاريخ < اليوم) | POS-GST §12 |
