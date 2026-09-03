# 03 — جرد الشاشات (Screens Inventory) — وحدة MNT

> **~35 شاشة** (12 تهيئة + 8 تشغيل بخمس شاشات فرعية + 15 تقريراً/استعلاماً بفلاترها). النمط الموحد: أزرار Fortune القياسية (New/Change/Delete-مشروط/Browse/Prev/Next/Save/Menu/Exit) + F1 عالمي + **النقر المزدوج كأداة تحرير أساسية** (خلايا الشبكات، NO→YES، Action Taken column).

---

## 1. شاشات Setup (12)

| # | الشاشة | الحقول/العناصر البصرية | المصدر |
|---|---|---|---|
| 1 | Define Locations | Location (6) · Name (30/3) · Short Name (10/3) — Browse/Modify | SET ص3-4 |
| 2 | Define Equipment Category | نمط ثلاثي (كود 3) | SET ص5-6 |
| 3 | Define Cost Category | نمط ثلاثي | SET ص6-7 |
| 4 | Define Shifts | نمط ثلاثي + Starting/Ending Time + Shift Order | SET ص8-9 |
| 5 | Define Service Types | نمط ثلاثي | SET ص10 |
| 6 | Define Service Rhythms | نمط ثلاثي + **No of Days** | SET ص11-12 |
| 7 | Define Skills | نمط ثلاثي | SET ص12-13 |
| 8 | Define Employees | Employee # (رقمي 7) · Name · Designation (F1) · Skill (قائمة) | SET ص14-15 |
| 9 | Define Complaint Priorities | نمط ثلاثي + Priority Order + **Color (F1)** | SET ص15-16 |
| 10 | Identify Engg Store (s) | **قائمة checkbox** لكل مخازن Inventory + حد أدنى 1 | SET ص17-18 |
| 11 | Identify Engg Cost Center | قائمة checkbox + حد أدنى 1 | SET ص18-19 |
| 12 | User Defined Print Forms | **مصمم كامل**: أيقونات مشروع (8) + Page Layout + Match Samples + Tool Box + Scales/Grid/Status/Lock + F4/F3 خصائص + Logo | SET ص19-24 |

## 2. شاشات Operations (8 + 5 فرعية) ⭐

### 2.1 Register Complaints (OPR ص2-4)
| الحقل | المواصفة |
|---|---|
| Complaint # | **توليد آلي** |
| Ref. No | 10 محارف ألف-رقمية كحد أقصى |
| Room # / Location Code | **اختيار ثنائي** ثم F1 حسب الاختيار |
| Department | القسم **الرافع** للشكوى |
| Complaint Type | **Common أو Repeated** |
| Complaint | نص التفاصيل |
| Reported By | اسم المُبلِّغ |
| بعد الحفظ | حوار طباعة Yes/No → **Job Request** (بوابة ENG#1) |

### 2.2 Action Taken (OPR ص5-15) — 3 مسارات + شاشتان فرعيتان
- **شاشة التوجيه:** اختيار "By **Job Order #**, by **Complaint #** or by **PM Schedule #**" + F1.
- **مسار Job Order #:** Help Screen بمعايير بحث مركبة: "Complaints or PM Schedules and further **Date, Department, Room or Location**" (OPR ص7).
- بعد الاختيار: شبكة فيها عمودا **Action Taken** و**Status** — كلاهما **نقر مزدوج** للتحرير؛ ثم "complaint **start and end date and time**".
- **الشاشة الفرعية 1 — Cost Analysis:** "Complaint #, **Cost Category and Service Provider** from the Help screen. Enter the amount in the Amount field. The details appear on the respective columns" (OPR ص11).
- **الشاشة الفرعية 2 — Repair Details:** "complaint #, Equipment code, **store code, and Cost Center**. Enter the **quantity** of the item, **the value will be auto calculated**" + "Item code... picked up from Inventory stores. **open item: 999999999999**... item name entered manually... **will not affect Inventory stores**" (OPR ص13).
- المساران الآخران (Complaint # / PM Schedule #): "Follow steps 5 to 15" حرفياً — نفس الشاشة اللاحقة.

### 2.3 Assign Shifts (OPR ص15-17)
- From/To Date: "(The date should be a **future date** and the date range should be **within 31 days**)".
- **شبكة تواريخ × موظفين** — لكل خلية نقر مزدوج → Shift Help (F1).
- **F2 = Copy Paste previous CELL · F3 = Copy Paste previous ROW** — تسريع إدخال الروستر الوحيد الموثق.

### 2.4 Equipment Master (OPR ص17-19) + 4 شاشات فرعية
| الحقل | المواصفة |
|---|---|
| Equipment Code | **8 محارف** ألف-رقمية + F1 للموجود |
| Equipment Name + Category | قائمة الفئات |
| Room أو Location | ثنائية الاختيار |
| Manufacturer / Model No / Serial Number / Installation Date | هوية المعدة المادية |
| Vendor Code | F1 → "vendor details like **name and address** appear on screen" |
| Value + Currency | "value of the equipment and the relevant currency" |

| الشاشة الفرعية | الحقول |
|---|---|
| **AMC Details** | مطلوب أو لا + Vendor + Expiry Date (OPR ص18) |
| **Spares Required** | Store · Item · Quantity · Vendor · **Lead Time** "(Time by which the spares are required)" (OPR ص18) |
| **Standard Readings** | **Minimum and Maximum UOM** (OPR ص19) |
| **Remarks** | نص حر "important remarks about the equipment" (OPR ص19) |

### 2.5 PM Schedule Master (OPR ص20-21)
- Equipment Code (F1 → الاسم آلياً) · Service Provider (Vendor, F1) · شبكة أعمدة: **Service Type (F1) · Service Rhythm (F1) · AMC Y/N آلي** · Start Date · **Lag (التأخير المسموح بالأيام)** · Task.
- "You can **modify any fields before saving**... To modify details after the information is saved, click Modify, select the record" — تعديل موثق صراحة (نمط ألطف من خلود الشرائح!).

### 2.6 PM Schedule Entry (OPR ص21-22)
- **PM Schedule # آلي** "once all the mandatory fields are completed" · Equipment (F1) · Start Date · **Must Complete By** (مع القيد: ≤ Lag days) · Task.
- "The dates are **automatically calculated based on the frequency of service**" — التوليد الزمني من الإيقاع.

### 2.7 Job Order Generation (OPR ص22-26) — مرحلتان ⭐
- **المرحلة 1:** اختيار Complaint أو PM Schedules + نطاق تاريخي → شبكة → "Double-click under the **Select column to change the NO option to YES**. All records tagged as YES indicates that a Job Order has to be generated".
- **المرحلة 2 (الأولويات):** "For each record double-click under the **Priority column** to assign a priority level" → "**the record will be highlighted in the color** that was set for the priority level".
- **الإسناد:** "Select if you want to assign the Priority to the **Employee or the Service Provider (Vendor)** and select the Employee/Service Provider Code accordingly. The respective details... appear on the screen".
- الطباعة → **Job Order** (بوابة ENG#2).

### 2.8 Equipment Reading Entry (OPR ص26-28)
- Equipment Code (F1) · "Date and Time **from when the reading entry begins**" · عمود **Actual Value** (أرقام) — للقراءات المعرفة في Standard Readings **فقط**.

## 3. شاشات التقارير والاستعلامات (15)

| # | الشاشة | الفلاتر | المصدر |
|---|---|---|---|
| 1 | Complaints List | نطاق تاريخ + **Location أو Department** + All/Pending/Closed | RPL ص2-4 |
| 2 | Duty Chart | نطاق تاريخ فقط (شرط مسبق: ورديات معرفة+معينة) | RPL ص4-5 |
| 3 | **Complaint Status (Q)** ⭐ | Pending/**WIP**/Closed → قائمة → **نقر مزدوج = فتح سجل + تغيير حالة + إدخال Action Taken + أولوية + حفظ برسالة** | RPL ص5-7 |
| 4 | Equipment Wise Complaints | نطاق معدات From/To (أو F1) + نطاق تاريخ | RPL ص7-9 |
| 5 | Location Wise Complaints | **Room أو Location** + نطاق + تاريخ + All/Pending/Closed | RPL ص9-11 |
| 6 | Action Taken Report | تاريخ + **Complaints/PM Schedules/كلاهما** | RPL ص11-13 |
| 7 | Employee Wise Action Taken | تاريخ + All/Selected Employee (EMP# + F1) | RPL ص13-15 |
| 8 | Equipment Details List | معيار: **Equipment/Category/Location أو AMC** + نطاق + ترتيب Name/Category/Location | RPL ص15-17 |
| 9 | PM Schedule List | تاريخ + معيار **Service Type/Service Rhythm/Equipment** + نطاق + ترتيب Category/Location | RPL ص17-19 |
| 10 | Resolution Time Report | معيار **Date (نطاق) أو Priority (مستويات)** | RPL ص19-21 |
| 11 | Job Order Report | تاريخ + نوع Complaints/PM + حالة Pending/Closed/All | RPL ص21-23 |
| 12 | Spares and Cost Report | تاريخ + معيار **Equipment/Location/Room** + نطاق | RPL ص23-25 |
| 13 | **Job/Complaint Print Engine** | Job Order أو Complaint؛ Complaint: بالرقم أو التاريخ؛ JobOrder: Complaint/PMS + بالرقم أو التاريخ + **اختيار طابعة** | RPL ص25 |
| 14 | Equipment Readings List | نطاق تاريخ | RPL ص26-28 |
| 15 | **Parameter Listing** | "Select the Parameter" → **MS-Excel** | RPL ص28-29 |

## 4. أنماط التفاعل العابرة للشاشات

- **النقر المزدوج = 4 وظائف مختلفة:** إدخال Action Taken · تغيير Status · NO→YES · إسناد Priority — أثقل وحدة استخداماً للنقر المزدوج بعد POS.
- **ثنائية Room/Location** في 5 شاشات (شكوى، معدات، تقارير 5/12) — استدعاءات F1 تتكيف حسب الاختيار.
- **الحواران بعد الحفظ** (طباعة Job Request/Job Order) — نمط "احفظ ثم اسأل عن الورق" نفسه في FO/POS.
- **شبكات قابلة للتحرير في مكانها** (Action Taken + Job Order Generation + Assign Shifts) — أقرب تجربة إلى Grid-First في المشروع.
