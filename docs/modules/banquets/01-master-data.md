# 01 — البيانات الرئيسية (Master Data) — وحدة Banquets

> مرجعيات القاعات والقوائم والموردين والفعاليات. **نمط موحد صارم:** أكواد مولدة آلياً + Modify-Locked (الاسم/الحالة فقط) + "لا حذف — الحالة فقط" يتكرر في 9+ كيانات.

---

## 1. الكيانات المكانية (القاعات)

### 1.1 Floor (الطوابق)
**المصدر:** SET §7. الحقول: Code (آلي) + Long Name (≤30) + Short Name (≤15). التعديل: Long/Short/Status. "Function Room Setup Styles created cannot be deleted; only status can be changed" (نفس النمط).

### 1.2 Associated Room (الغرف المرتبطة)
**المصدر:** CFG §1. 3 أنواع: **Green Room / Storage Room / Pre-Function Area** — "can be linked to the main function rooms and the same can be blocked when the main function room is blocked or released". الحقول: Applicable date (**≥ اليوم**) + Property + Long/Short + **Location** + **Floor** + النوع + **المقاسات: Length/Breadth/Height + Units** (Area محسوب). "cannot be deleted, only status can be changed".

### 1.3 Function Room (الكيان المركزي — 6 تبويبات)
**المصدر:** CFG §5 ص12-16.

| التبويب | الحقول الموثقة |
|---|---|
| **DETAILS** | Applicable From (**= "accounting date"** الافتراضي، ≥ فقط) + Property + Room Type + الاسم + Associated Rooms + **Location** + Floor + **Available Hours** + **Minimum Revenue** (!) + **Security Type** + **Venue Dimensions** (مقاسات) |
| **FEATURES** | Venue Features (متعدد من Function Room Features) + Room Description |
| **SEATING** | "seating capacity **for each type** of seating styles under the capacity column" + **صور أنماط الجلوس** إن حُفظت ("visible in the space provided on the left side") |
| **PICTURES** | صور القاعة + وصف |
| **LAYOUT** | صورة المخطط + وصف (يمين) |
| **LOCATION** | صورة الموقع + وصف |

**القواعد:** "Records defined in this program cannot be deleted only status can be changed" + Passive تُدفع أسفل الشبكة وتختفي من العمليات.

### 1.4 Tag Sub Venues
**المصدر:** CFG §10. قاعة رئيسية (checkbox ثابت لا يُلغى!) + اختيار Sub-Function Rooms → "will not be displayed in the list box to tag with other main Function rooms" (حصرية). **العرض:** "combined with the Main Function Room in Make Booking, Availability Chart and Block & Release Rooms". Passive في Function Room → تختفي من Sub هنا.

### 1.5 Function Room Features / Setup Style
**المصدر:** CFG §§2-3. Features: Description فقط. **Setup Style:** Long/Short + **Setup Type** (من القائمة الافتراضية) + **Min/Max recommended Pax** + Description + **Image** — أنماط جلوس معرّفة مستخدم بسعة موصى بها.

## 2. كيانات التسعير والسياسات

### 2.1 Cancellation Policy
**المصدر:** CFG §4. Policy Code (آلي) + Description + **Days range (From/To) + Value Type (V أو P) + Value/Percentage** — "that will be charged to the Party in case the Party cancels the Booking". لا حذف (الحالة فقط).

### 2.2 Corporate Rate Master (أسعار الشركات — 3 عائلات)
**المصدر:** SET §18 ص80-91.

| العائلة | الحقول | ملاحظات |
|---|---|---|
| **Room Rate** | Property + Rate Id (F1) + Applicable date + Description + Function Room (F1) + Room Charges + tax type + tax structure | "By default, the **Hall Tax Structure defined in the print forms program** will be displayed" |
| **F&B Rate** | + **Event Type** (F1) + Rate/Pax Charges + tax type | "Double click in the Event Type column to modify" |
| **Non F&B Rate** | + Equipment (F1) + Non F&B Charges + tax type + structure | "By default, the Tax Structure will be displayed **empty**" |

**الحذف:** "select the record and press **F5**" — استثناء موثق عن قاعدة "لا حذف"!

### 2.3 Corporate Rate Tagging
**المصدر:** SET §19. Company Code (F1 من **Company Master** الموجود) + Room Rate Id + F&B Rate Id + Non F&B Rate Id → "the same rates can be applied for a reservation in **Banquet Booking and Requirement Entry**". F1 مزدوجة لعرض الأسعار القائمة (عرض فقط).

## 3. كيانات القوائم والتصنيف

### 3.1 Item Type / Banquet Menu Groups / Event Types
**المصدر:** SET §§8-9 + CFG §6. Item Type (≤25 — للفرز في Item Classification/Menu Card/Requirement) · Menu Groups (Long ≤30/Short ≤15 + **Sequence** غير مكرر — "followed to print the Menu Groups in **Function Prospectus**") · Event Type: "Default event classifications like **AGM, Birthday, Conference, Wedding, and Party** are displayed on loading".

### 3.2 Item Classification and Description
**المصدر:** CFG §7. Property + Banquet Outlet + Item (F1 → Group تلقائي) + Banquet Group + Item Type + **"Veg/Non-Veg"** + Description + **Catering type** + (عرض: Currency/UOM/سعر البيع من Menu Master) — "The Items after classified as Vegetarian/Non Vegetarian will be displayed in Requirement Entry".

### 3.3 Menu Master (بنمطين — POS MA 29!)
**المصدر:** CFG §8.

**النمط المشترك (MA 29=Yes):** Item Code (**رقمي ≤4**) + Name/Short + Menu Group + menu type + Classification (**Touch Screen Menu Group**) + Cost% + outlet + description/UOM/qty + Kitchen Code + **KOT printer** + tax structure + **Default Bill** (فاتورة مستقلة/مدمجة) + **Print Order** + **NC Flag** + **Discount flag** + **Level 1/2/3** (مستويات القائمة!).

**النمط الفردي (MA 29=No):** يضيف: Applicable From + **Available Hours** + **Sub Store Code (المطبخ!)** + KOT Printer + **Preparation Time** + **GL Code (F1!)** + Remarks + **Local Currency tab** (qty/desc/UOM/rate) + **Foreign Currency** (اختياري: Currency + rate).

### 3.4 Setup Menu Card / Package Menu Card
**المصدر:** CFG §9.

| العنصر | Menu Card | Package Menu Card |
|---|---|---|
| المحتوى | "You can tag Menu Card only with **FB Items**" | "with FB and Non FB Items **or with an existing Menu Card**" |
| الحقول | Applicable date (server) + Property + Menu Code (F1 → الأصناف والمجموعات تُعرض) + Menu Name + **Recom. Pax** + **Editable (Yes = اسم الصنف قابل للتحرير في Requirement Entry!)** + Description | Package Menu Code/Name + Recom. Pax + Editable |
| الانتقاء | "Food Classification, Item type, Banquet group, Group name & Item Name" + تبديل إدراج/استبعاد (✓→✗) + **عدّاد Defined لكل مجموعة** | FB → **Catering** يظهر؛ Non FB → **Tax structure + Quantity** |
| **Allowed** | "number of menu items that can be ordered in requirement entry" **لكل مجموعة** | نفسه |
| الحذف | لا — الحالة فقط (والكميات قابلة للتعديل في Modify) | نفسه |

## 4. كيانات المورد والتجهيزات

### 4.1 Equipment Master (3 طبقات)
**المصدر:** SET §12. **Category** (Name ≤30) → **Sub-Category** (تحت Category) → **Equipment**: Property + Category + Sub-Category + Name (≤30) + **In house Quantity** ("number of dining chairs available in the Property") + **In house Rate** + **Tax structure** — "all **Non Food & Beverage equipments**".

### 4.2 Supplier Master (معدّات خارجية)
**المصدر:** SET §13. ربط مورد → معدّات + **أدوان سعرية: 1 hour / 2 hours / Half day / Full day / Multi days + Min days** + Tax structure. **نمطا السعر: Ad-Hoc / Contract Rate** (عقد من Help). "Rates defined in this option **cannot be deleted**. Only status can be changed". **إنشاء مورد جديد مدمج** — **نفس Vendor Master نصاً حرفياً مع MGT** (كود 7 = 3 Type + 4، Title/Name/…/Black Listed/Currency/TDS!) وإنشاء Contract (Applicable From/Contract#/Vendor/Expiry/Ref#).

## 5. كيانات الأحداث والتقييم

### 5.1 Event Question Definition
**المصدر:** SET §14. **Groups** (Food/Lodging…) → **Answers** (Good/Satisfactory…) → **Question** (Code آلي) + **حتى 6 إجابات متوقعة مع Score اختياري — إجابتان إلزاميتان للحفظ**. "used in the Event Template Definition... to know the customer feedback about the function".

### 5.2 Event Template Definition
**المصدر:** SET §15. Template Name + **Event Type** (افتراضي General) + checkbox للأصناف من "Defined Questions" (مرتبة بمجموعاتها). **Event Type غير قابل للتعديل** — "you have to change the Status... to Passive and create a new template".

### 5.3 Setup Event Calendar
**المصدر:** SET §10. Property + Event Name (مثل Christmas) + **Day Type** (افتراضيات PMS) + Date/Time From-To + **Dry Day (Yes/No)** + **Booking Allowed (Yes/No)** + **Booking Made By (User/Supervisor/all)** + Status + أيقونة. **قيود العرض:** "A maximum of 4 events will be visible in the box of a day. If more than 4... a **blue arrow**... up & down arrow keys". **التعديل:** "only the status... if the event has already occurred" — الماضي يُقفل.

### 5.4 Reservation Status
**المصدر:** SET §11. Name (≤30) + **Type** (من الافتراضية: Inquiry/waitlist/Provisional/Confirmed) + **Color legend فريدة** ("displayed against the selected Function rooms based on the function date & time") + **Sequence** (لا تكرار ولا فراغ — "reflected in the Function Room Help screen"). التعديل: **الحالة فقط** (+ Sequence بنافذة).

## 6. كيانات التواصل

| الكيان | الحقول | المصدر |
|---|---|---|
| **Property Information** | Logo/Image/**Location Map**/**Driving Map** (نقر مزدوج للإضافة — "auto populated if saved") + **Driving description** + Address (≤99) + **4 هواتف + 4 فاكسات** (≤15) + Email + Website + Country/**Region (N/S/E/W)**/State/City | SET §5 |
| **Country-State-City** | 3 تبويبات؛ الأكواد آلية؛ التعديل: الاسم + الحالة فقط | SET §4 |
| **Banquet Staff** | "users exclusively for banquet module" — قائمة **Create User (SYS)** + Select → "displayed in the **Follow up user** option of the Make Booking"؛ Passive في Create User → يختفي | CFG §11 |
| **Service Managers** | Name (≤30) + Designation + Department + Email + **Alternate Email** + Mobile + **Alternate Contact** | CFG §12 |
| **Banquet Block Reasons** | Description (≤25) — "to block the Function Rooms and Associated Rooms in the **Block/Release** Rooms menu option" | SET §6 |

## 7. جدول القيود الموحد

| الكيان | الطول/الصيغة | Applicable From | Modify-Locked | الحذف |
|---|---|---|---|---|
| Country/State/City | كود آلي | — | الاسم+الحالة | ممنوع |
| Floor | Long ≤30/Short ≤15 | — | الاسمان+الحالة | ممنوع |
| Block Reason | Desc ≤25 | — | Desc+الحالة | ممنوع |
| Item Type | Desc ≤25 | — | Desc+الحالة | ممنوع |
| Menu Group | Long ≤30/Short ≤15 + Seq فريد | — | الاسمان+الحالة | ممنوع |
| Reservation Status | Name ≤30 + Sequence | — | **الحالة فقط** | ممنوع |
| Associated Room | أبعاد+وحدات | ✓ ≥ اليوم | **الحالة فقط** | ممنوع |
| Function Room | 6 تبويبات | ✓ (=accounting date) | كامل بعد الإنشاء؟ [مقيد بالحالة على الأرجح] | ممنوع |
| Cancellation Policy | V/P + Days | — | كامل+الحالة | ممنوع |
| Supplier Master (معدّات) | أدوان 5 + Min days | — | الحالة | **ممنوع صراحة** |
| Corporate Rates | Rate Id + Applicable | ✓ | معدّل في Modify | **F5 — استثناء وحيد!** |
| Event Question | ≤6 إجابات (2 إلزام) | — | كامل+الحالة | ممنوع |
| Event Template | — | — | **Event Type محظور** (Passive+جديد) | ممنوع |
| Menu Master | Code رقمي ≤4 | ✓ (فردي) | — | [NOT DOCUMENTED] |
| Service Managers | Name ≤30 | — | كامل+الحالة | ممنوع |
