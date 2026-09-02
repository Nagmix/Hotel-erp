# 01 — البيانات الرئيسية (Master Data) — وحدة POS

> المصدر: POS-SET (§1-§15 + §24-§28 + §31-§33 + §41) + POS-GST (§1-§3). **كل Masters إصدارية (Applicable From + Status Active/Passive + Last Updated)** — نمط موحد موثق في ص4 POS-SET "Standards".

---

## 1. عائلة المنفذ (Outlet Cluster)

### 1.1 Outlet — POS-SET §1 ص5-9

| الحقل | القاعدة | المصدر |
|---|---|---|
| Applicable From | ddmmyy (افتراضي اليوم؛ ≥ اليوم للتشغيل) | ص6 |
| **Outlet Code** | **≤3 خانات alphanumeric** | ص6 |
| Name / Short Name | ≤30 / ≤10 | ص6 |
| Outlet Type | من قائمة معرَّفة | ص6 |
| **Linkage** | ربط بـ **Front Office / Finance / كليهما** | ص6 |
| **Tax Currency** | عملة فرض الضرائب + **Round Off: None/Nearer/Higher/Lower** (أمثلة مرجعية في Property Codes بـ SYS) | ص6-7 + ص25 |
| Department / Cost Center | من SYS (General Setup) | ص7 |
| **KOT Form ID / Bill Form ID** | Pgm IDs للطباعة | ص7 |
| Bill Printer Name / Settlement Printer | طابعات الفاتورة/التسوية | ص7 |
| Tax Structure | بنية ضريبية للمنفذ + **All Inclusive (Yes = ضريبة داخل السعر)** | ص7 |
| **Multi Currency** | Yes/No — شرط ظهور المنفذ في Link Outlet Currencies | ص7 + ص24 |
| **Bill Initialization Type** | **Yearly (+ Initialization Date DDMM) / Monthly / Daily / None** | ص7-8 |
| F & B Outlet | هل المنفذ مطعم/بار | ص8 |
| **Copies** | عدد نسخ طباعة الفاتورة | ص8 |
| **Activate Delivery Module** | خدمة توصيل الطلبات | ص8 |
| Token/Counter Print ID | طباعة Token | ص8 |
| **Order Entry Flags (5):** | Accept Text for Table # / Accept Text for KOT / **Over Ride NC Bill Print (يتجاوز Module Attribute #6!)** / Do not print Standard KOT / **Accept Room # for NON Room Service Outlets** | ص8-9 |

**قاعدة التعديل الإصدارية:** "You can modify all the fields of an Outlet that is defined for a future date. For Outlets defined for the current date, you can modify **only the status**... a new record has to be entered for a future date" (ص10).

### 1.2 Outlet Session — §2 ص11-14
Session Code (**≤2 alphanumeric**) · Name ≤30 · Short ≤10 + Applicable From.

### 1.3 Outlet Order Type (KOT Type) — §3 ص14-17
KOT Type (**numeric ≤2**) · Name · Short — أنواع مثل **Standard / Complimentary / Staff** (يذكرها §5 ص21).

### 1.4 Link Outlet Sessions — §4 ص17-20
Outlet × Session + **Order (يبدأ بـ 1)** + **Starting/Ending Time (24h HH:MM)** + **Minimum Cover Charge** + **Applicable On (أيام الأسبوع)**.

### 1.5 Link Outlet Order Types — §5 ص20-23
Restaurant (Type يُملأ آلياً) × KOT Type + **KOT # Type**: **Auto Generation / Validate KOT book / Manual Entry** — **"The Standard KOT type is mandatory for every restaurant"** (ص21).

### 1.6 Link Outlet Currencies — §6 ص23-25
Outlet (**بشرط Multi Currency=Yes**) × Currency + **Round Off + Round Off Amount لكل عملة**.

## 2. عائلة القوائم (Menu Cluster)

### 2.1 Menu Master — §24 ص71-75

**نمطان بقرار Module Attribute 29:**

| النمط | Attr 29 | البنية | المصدر |
|---|---|---|---|
| **Common** | YES | Item Code (**numeric ≤4**) + Name/Short + Menu Group + Menu Type + Classification (Touch Group) + Cost% + **Outlets (متعددة)** + Description/UOM/Quantity + Kitchen + KOT Printer + Tax Structure + Default Bill + Print Order + NC Flag + Discount + Levels 1/2/3 | ص71-73 |
| **Per-Outlet** | NO | نفس الحقول + **Applicable From + Available Hours + Sub Store Code + Preparation Time + GL Code + Remarks** + تبويب Local Currency (Qty/Desc/UOM/Rate) + تبويب **Foreign Currency** (اختياري Rate لكل عملة) | ص73-75 |

### 2.2 POS Rate Master — §25 ص75-79
تحديث أسعار لصنف/مجموعة (From/To) لكل منفذ: Cost% · Kitchen · KOT Printer · Discount · Tax Structure · Print Order · NC Flag · Default Bill · Levels · Currency + **نقل الأصناف بين المنافذ (بشرط تطابق العملات الأجنبية بين المصدر والهدف!)** — *يعمل فقط مع Common Menu Master*.

### 2.3 Modifier Master — §26 ص79-82
Restaurant × Item Code × **Modifier Item (numeric ≤2)** + Name ≤40 + **Recipe** + **Additional Charge**.

### 2.4 Touch Screen Modifiers — §27 ص82-89
ثلاث طبقات: **Modifier** (كود ≤4 + اسم ≤20 + شحنة إضافية؛ حذف بـ F5 **إذا لم يكن في Group**) → **Group Modifier** (كود ≤3 + اسم ≤30 + أعضاء) → **ربط Group بالأصناف** (لكل مطعم).

### 2.5 Menu Groups (§8) / Touch Screen Groups (§14) / Menu Levels (§11)
- Menu Group: كود **numeric ≤3** + Name/Short (§8 ص28-31).
- Touch Screen Group: كود **numeric ≤2** — "will reflect as a menu group in **touch screen application only**" (§14 ص41-43).
- Menu Levels: **Outlet × Major Classification + Sub Classification (numeric ≤2)** + Name — تصنيف بالأنواع/التحضير/نباتي... (§11 ص35-37). **التعديل: Name + Status فقط** (ص37).

## 3. عائلة الأصول التشغيلية

### 3.1 Servers — §9 ص31-34
Server Code (**≤3 alphanumeric**) + Name ≤30 + Short ≤10 + **Employee # (numeric ≤6)** — تُستخدم في KOT وتقارير الطاولات.

### 3.2 Server Outlet Mapping — §10 ص34-35
عنوان + صورتان فقط `[NOT DOCUMENTED تفصيلاً]` — ربط النادلين بالمنافذ (GAP-POS-D02).

### 3.3 Restaurant Table Master — §12 ص37-39
Restaurant × **Table # (≤5 alphanumeric)** + **Maximum Covers (≤3 numeric)** + **Location View ≤30** — **التعديل: Covers + Location View فقط** (ص39).

### 3.4 Design Table Layout — §39 ص111-115
مصمم مرئي للطاولات بأرضيات (Floors): صور GIF في مجلد **RESTBL** بأسماء قياسية — **ترميز الألوان: G(reen)=Vacant · R(ed)=Occupied · B(lue)=Billed · Y(=Brown)=Reserved** + C/R أشكال × 4 + Flower/Blank + خطوط بأعراض + نصوص أفقية/عمودية + نسخ تصميم بين الأرضيات (**بلا أسماء الطاولات**).

### 3.5 Kitchens — §15 ص44-47
Kitchen Code (**≤3**) + Name/Short + **Network Printer** — "Every item must be tagged to the kitchen defined here" + **التفعيل بـ POS Module Attribute #32**.

### 3.6 Item Hot Keys — §13 ص39-41
Restaurant × **Control Key (قائمة) × Function Key** + Item Code + **Quantity** — إدخال سريع للأصناف المتكررة. **التعديل: Status فقط؛ لا عرض لمفاتيح الوظائف في أي وضع — إسناد جديد بدلاً من التعديل** (ص41).

### 3.7 Issue KOT Book — §30 ص93-95
Restaurant × KOT Type × **Starting/Ending KOT** × **Issued To (Server)** — **حد أقصى 100 ورقة للكتاب!** + التعديل: اسم المستلم فقط.

### 3.8 DSR Session Group — §36 ص106-108
تجميع الجلسات تحت **3 فئات كحد أقصى** (Breakfast/Lunch/Dinner) — Record # (≤3 سجلات) + Description ≤20 + Sessions — لخدمة Daily Sales Report.

## 4. التسويق والخصومات

### 4.1 Happy Hours Definition — §31 ص95-98
Outlet + From/To Date + From/To Time + Discount (Item/Mn Grp) + **Type: P (نسبة) / A (مبلغ — للصنف فقط!)** + معدلات **لكل يوم أسبوع على حدة أو All** + نسخ العناصر المخفضة.

### 4.2 Sales Promotion Master — §32 ص98-102
Promotion Code (**numeric ≤4**) + Name ≤40 + **Covers** + Promotion Value + **Calculation Type: Minimum/Maximum/Average/None** + Tax Structure + Group + أصناف بثلاث فئات: **Main / Additional / Complimentary** (**إلزام بند Main واحد على الأقل!**) + Quantity + **Available (أيام الأسبوع)**.

### 4.3 Member Discount Defn. — §41 ص116-122
**Member (من Membership — Member Section screen)** × **Outlet** × **Menu Type (Food/Liquor/Soft Drinks/Tobacco/Others/All)** = نسبة خصم + **Member Srl # (1=رئيسي، غير ذلك=ثانوي)** + **INI 404**: 1 = خصومات **للرئيسي فقط** / 0 = **للرئيسي والثانوي**.

### 4.4 Open Items Definition — §19 ص54-56
**Menu Type** + **NC Cost %** + **Discount Allowed** + Default Bill + **طابعات كل المطابخ إلزامية** ("It is mandatory define the printers for all the kitchens").

### 4.5 Update NC Change — §40 ص115-116
تحديث **نسبة NC** لمجموعة (Group Code/Name) لكل مطعم.

## 5. Guest History (POS-GST) — قاعدة الضيوف الخاصة بالمنافذ

### 5.1 Guest Master — POS-GST §1 ص2-18

> **خاصية معمارية: يُفتح باختيار Outlet أولاً** (ص3) + **"For each Guest, the system will automatically generate Guest Code"** (ص4).

| التبويب | الحقول الجوهرية | المصدر |
|---|---|---|
| Main | الاسم/العنوان/هاتف/بريد + Designation/Nationality/Guest Status/Guest Classification + Gender + **Special Instruction** + Nights + **Black Listed (Yes/No)** | ص4 |
| Contact | **Company Code (F1 — قوائم FO!)** + Secretary + بيانات الشركة | ص5 |
| Passport | Passport # + Issue Date/Place + Valid Until | ص6 |
| Personal | DOB/Anniversary/Smoker/Occupation/Frequent Flyer/Loyalty/CC Type+#+ **Spouse كاملة** + **Children Info (Name/DOB/Gender)** + **Guest Privilege Card (Card Type من FO + Number)** | ص7-11 |
| **Visit Details** | تاريخ/وقت + Restaurant + Session + Amount + **طريقة التسوية** + CC# + **Breakup (أصناف + كميات!)** | ص11-13 |
| Likes & Dislikes | Likes/Dislikes + وصف | ص13-14 |
| Comments | نص حر | ص15 |
| Complaint Details | **Department + Nature of Complaint + Date/Time** | ص15-16 |
| Visual | صورة الضيف (Browse/Save/Delete) | ص16-17 |
| **Preferences** | "The details captured in **Guest Preferences option of Front Office module** will be shown here" + اختيار Activity | ص17-18 |

### 5.2 Setup Loyalty Cards — §2 ص18-19
Card Type (**≤3 رقمي**) + Card Description.

### 5.3 Setup Loyalty Master — §3 ص19-24
Card Type + **Card # (≤15 alphanumeric)** + **Join Date (≤ تاريخ الخادم) + Expiry Date** + Guest (F1 — **"The module and Guest Code appear beside the name"**!) + Display Text + **خصومات لكل منفذ × نوع قائمة × Covers** + Status (Active افتراضي).
