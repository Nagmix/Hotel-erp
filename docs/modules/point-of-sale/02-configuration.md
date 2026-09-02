# 02 — الإعداد (Configuration) — وحدة POS

> المصدر: POS-SET (Module Attributes + INI + صلاحيات + طباعة) + TS (Open/Close). **POS هي أغزر الوحدات مفاتيح SYS** — 3 Module Attributes موثقة نصاً هنا + INI 404 + روابط متعددة.

---

## 1. Module Attributes الخاصة بـ POS (الموثقة نصاً في POS-SET)

| # | الاسم/السياق | السلوك | المصدر |
|---|---|---|---|
| **6** | NC Bill Print (يُذكر في Order Entry Flags) | Over Ride NC Bill Print في Outlet **"will override the POS Module Attribute #6"** — أي أن علم المنفذ يعلو على المفتاح العام في منع طباعة فواتير NC | POS-SET §1 ص8-9 |
| **29** | Common Menu Master | YES = أصناف **مشتركة** لكل/مختارة من المنافذ (Menu Master بنمط Outlets متعددة + Rate Master + النقل بين المنافذ) / NO = أصناف **لكل منفذ** (Applicable From + Available Hours + GL Code) | POS-SET §24 ص71+73 |
| **32** | Network Printer | **يفعّل حقل Network Printer في Kitchens** — توزيع KOT على مطابخ عبر الشبكة | POS-SET §15 ص45 |

> `[NOT DOCUMENTED]` باقي Module Attributes للـ POS (المرقّعة إلى 30+ موضعاً في SYS) — تحسم عند قراءة SYS-SSP.

## 2. INI Switches الخاصة بـ POS

| # | الاسم | المنطق | المصدر |
|---|---|---|---|
| **404** | Member Discount (Primary/Secondary) | **1 = خصومات للأعضاء الرئيسيين فقط** (Add وModify) / **0 = لكل الأعضاء (رئيسي + ثانوي)** — وفي وضع 0 يمكن إدخال Member Code وSrl # يدوياً أو بالاختيار | POS-SET §41 ص121-122 |

## 3. إعدادات التشغيل الحرجة

### 3.1 Outlet Settlements — §17 ص50-52

> **"bill settlement by cash is a mandatory mode of settlement and not optional for any of the outlets"** — النقد إلزامي دائماً؛ الأنماط الأخرى اختيارية لكل منفذ (Applicable From + اختيار من قائمة).

**التسويات الفاعلة في التطبيق (Touch Screen):** "only Cash, Credit Card, Cheque, Coupon, Guest & Void Settlements are accepted. Others will not work" (TS ص32).

### 3.2 POS Report Options — §18 ص52-54
مصفوفة **تقرير × (Void ☐ / Complimentary ☐)** — تحدد بيانات الفواتير الملغاة/المجانية الداخلة في كل تقرير — "User is advised to list these cautiously".

### 3.3 POS User Access — §20 ص56-58
مصفوفة **User (كاشيرو POS فقط!) × عملية (KOT / Billing / Settlement) × وظائفها** بقيم Yes/No + عمود **Applicable To: Regular / Touch Screen / PDA** — ثلاثي الأبعاد (مستخدم × عملية × تطبيق).

### 3.4 Restrict Outlet Access — §21 ص60-61
اختيار **مستخدم × منافذ** للتقييد (مثال موثق: IDSS-Supervisor مقيَّد عن Health Club, LE Grand Hall, Minibar, Pastry Shop, Souq Cafe). **دلالة:** الوصول الافتراضي = كل المنافذ؛ التقييد استثناء (نمط allow-by-default هنا — عكس AR User Access!).

### 3.5 Central KOT Definition — §33 ص102-104
ربط **Outlet → طابعة KOT مركزية واحدة** "irrespective of the location of KOT counters".

### 3.6 Bill Printer Selection — §34 ص104-106
**عدة طابعات فاتورة لكل منفذ** — "The POS user will get an option to select the Printer to print the bill during Order Entry".

## 4. إعداد الطباعة (User Defined Print Forms) — §23 ص61-68

> **مصمم طباعة مرئي كامل** (الأعمق توثيقاً في النظام كله):

| العنصر | الموثق | المصدر |
|---|---|---|
| المشاريع | New/Open/Delete/Browse/Save/Print/Print Preview | ص62 |
| **Page Layout** | Header/Footer/Body rows — **"The sum of Header rows, Footer rows, and body rows must be equal to the total length of the stationery"** + **6 rows = 1 inch** + Match Samples (طباعة مطابقة) | ص62-63 |
| **Tool Box** | كل الحقول/الأعمدة الممكنة — **"If the tool highlighted in blue color is selected, then the bill will include all the items of the selected tool"** | ص63-64 |
| خصائص الحقل (F4) | Line# · Left · Width · Alignment · **Print From/To (قص النص الطويل)** · **Last Page (للطباعة في الصفحة الأخيرة فقط — مثل UserId)** | ص64-65 |
| **Body Details** | **إلزامي!** + Top Line/Left/Rows/Columns + خصائص العمود F3 (Width/Print Bold) | ص65-66 |
| Logo | Width/Height/Picture (Browse+Upload) | ص66 |
| User Text | نص حر (Captions) | ص66-67 |
| **أنواع البرامج** | **Bill print · KOT Print · NC Bill Print · Invoice Print** + Printer Type (Normal/Slip) | ص63 |
| **التفعيل** | **"It is mandatory to activate a form before printing"** — File > New > **Make Project Active** — النموذج النشط يطبع | ص67-68 |

## 5. Parameter List — §23(2) ص69-71
عرض كل إعدادات النظام (اختيار + **Show All Records** لعرض Active وPassive) → **IDS Report Engine** (Display/Spool/Print/Export).

## 6. صيانة KOT

### 6.1 Purge KOT Books — §37 ص108-109
- **"You can purge Standard or Complimentary KOT books for Validate KOT Book type only"** — التنقية لنمط التحقق بالكتاب حصراً.
- **شرط مسبق: Void للكتب أولاً** عبر Void KOTs تحت Billing.

### 6.2 Quick Menu Update — §28 ص89-91
| الخيار | الحقول | زمن السريان |
|---|---|---|
| **Option 1** | Applicable Hours · Menu Levels · Preparation Time · Cost% · Default Bill · Print Order · Touch Screen Grouping · KOT Printer · Bill Printer | **فوري عند إعادة تحميل POS Order Entry** |
| **Option 2** | New Name · Short Name · Menu Group | **من اليوم التالي فقط** |

## 7. خريطة التكوين الكاملة

| الإعداد | النوع | أثره | قابلية التغيير |
|---|---|---|---|
| Module Attribute 6 | مفتاح | طباعة فواتير NC (مع تجاوز على مستوى المنفذ) | ✔ |
| Module Attribute 29 | مفتاح معماري | بنية Menu Master (مشترك/منفصل) — **قرار بنيوي صعب التراجع** | ⚠ حساس |
| Module Attribute 32 | مفتاح | طابعات الشبكة للمطابخ | ✔ |
| INI 404 | مفتاح | نطاق خصومات الأعضاء | ✔ |
| Outlet Settlements | تكوين تشغيلي | أنماط التسوية (النقد إلزامي) | ✔ (إصداري) |
| POS Report Options | تكوين تقارير | شمول Void/Comp | ✔ |
| POS User Access | صلاحيات | كاشير × عملية × تطبيق | ✔ |
| Restrict Outlet Access | صلاحيات | مستخدم × منافذ (استثناء) | ✔ |
| Bill Init Type | ترقيم | دورة أرقام الفواتير | ✔ (إصداري) |
| User Defined Print Forms | طباعة | مشاريع + Make Active | ✔ |
| DSR Session Groups | تقارير | 3 فئات DSR | ✔ |
