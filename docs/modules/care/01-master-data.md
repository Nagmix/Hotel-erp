# 01 — البيانات المرجعية (Master Data) — وحدة Care

> جرد كل الكيانات المرجعية الموثقة في الدلائل الثلاثة، مع الحقول والقيود ومصدر كل كيان (محلي مقابل PMS). **المبدأ المعماري الحاكم: Care لا يملك إلا الحد الأدنى من الماجستير المحلي — كل شيء آخر يُسترجع من PMS.**

---

## 1. خريطة مصادر البيانات (PMS-centric!)

| الكيان | المصدر | الدليل النصي |
|---|---|---|
| User (المستخدم) | **PMS** — "You cannot create new Users; you can only map the Users that are created in PMS" | SET ص5 |
| Group/User في Define Rights | **PMS** — "the Groups & Users will be retrieved from PMS" | SET ص7 |
| Department (القسم) | **PMS** — "All the Departments that are available from PMS database will be displayed" | SET ص11 |
| Designation (التصنيف الوظيفي) | **PMS** — "All the Designations that are available from PMS database will be displayed" | SET ص13 |
| Shift (الوردية) | **PMS/Maintenance** — "The Shifts and Locations parameters are mapped from the Maintenance module in PMS" | OPR ص5 |
| Location/Other Area (الموقع) | **PMS/Maintenance** — "The Locations parameter is retrieved from the Maintenance module in PMS" | OPR ص33 |
| Room + Guest details | **PMS حي** — اختيار Room# يعرض بيانات الضيف فوراً؛ وسجل المهمة يحمل Check-in/Check-out | OPR ص34 + REP ص25 |
| Lost and Found records | **PMS + محلي** — "You can view the PMS Lost and Found details from this option" + إضافة سجلات محلية بـ Module=outlet | OPR ص60 + ص64 |
| **Employee (موظف Care)** | **محلي خالص** — يُنشأ داخل Organizational Structure (اسم/عنوان/اتصال/صورة) | SET ص16-17 |
| Task/Complaint (تعريف المهمة) | **محلي** — Main/Sub Category + أوقات + أولويات + تصعيد | SET ص25-27 |
| Multi Task (المهمة المجمعة) | **محلي** — تجميع مهام أقسام متعددة تحت كيان واحد | SET ص28-31 |

> **الدلالة:** Care "وحدة ساتلية" — لو فُصل PMS عنها لتعطلت كلياً (لا دخول مستخدمين ولا أقسام ولا ورديات ولا غرف). هذا هو الاعتماد الأحادي الأقوى الموثق في المشروع حتى الآن.

## 2. الموظف التشغيلي (Care Employee) — الكيان المحلي الوحيد الجوهري

### 2.1 البنية المكانية (شجرة ثلاثية المستويات)
```
Property (من PMS — يظهر يسار الشاشة)
 └── Department (من PMS — right-click Property → Department)
      └── Designation (من PMS — right-click Department → Designation)
           └── Employee (محلي — right-click Designation → Employee → Add New)
                └── Reporting To... (رابط تصعيد — right-click Designation)
```

### 2.2 حقول الموظف (SET ص16-17)

| الحقل | ملاحظات |
|---|---|
| Last name / Middle name / First name | **غير قابلة للتعديل بعد الإنشاء** — "You cannot edit the employee name" (SET ص24) |
| Address (العنوان المنزلي) | نص حر |
| Personal contact number (هاتف منزلي) | رقم الاتصال الشخصي |
| **Extension number** | تحويلة المكتب |
| **Pager number** | رقم البيجر |
| **Mobile number** | ⚠️ **قناة استلام المهام**: "THE EMPLOYEE'S MOBILE NUMBER... IS THE NUMBER WHERE HE WILL RECEIVE THE MESSAGES FROM THE AGENTS" |
| **Walky-Talky number** | رقم اللاسلكي |
| Email address | البريد الإلكتروني |
| Photo / Clear Photo | تحميل/تحديث/مسح صورة |

### 2.3 دورة حياة الموظف (SET ص20-24)

| العملية | الآلية | قيود |
|---|---|---|
| إنشاء | Add New → تعبئة → Confirm | أول تصنيف لقسم جديد: رسالة ثم يظهر خيار Reporting |
| تعديل | right-click → Edit Details | **كل الحقول عدا الاسم** |
| حذف | right-click → Delete → YES | **حذف ناعم**: "added to the Deleted List" |
| استرجاع | Designation → Employee → From Help → **Deleted List** → اختيار → Home → تأكيد | يُسترجع من قائمة المحذوفين |
| تسلسل الإبلاغ | right-click Designation → Reporting To → (Department + Designation) → Ok | يُحدَّث ويظهر تحت "Previously Referred To…" — سلسلة التصعيد تتبعه حرفياً |

### 2.4 مثال سلسلة التصعيد الموثقة (SET ص18)
`Room boy → Housekeeping Supervisor → Housekeeping Manager → Front Office Manager → General Manager → Managing Director`
— "Once the reporting levels are defined, **Escalations in the task will follow the order** as defined in the Reporting levels."

## 3. تعريف المهمة/الشكوى (Task and Complaints) — SET ص25-27

| الحقل | القيم/القواعد |
|---|---|
| Department | اختيار القسم المالك |
| Main Category | Code + Description |
| Sub Category | Code + Description — **متعددة تحت كل Main** ("Multiple Tasks") |
| Estimated Time for Response | **بالدقائق** |
| Designation | "the Designation to whom the Task has to be assigned" — التخصيص الافتراضي للتصنيف |
| Type | **Complaint / Request / Incident / Other** |
| Charges applicable | Yes / No |
| Feedback required | Yes / No — يحدد المرحلة Awaiting Feedback بعد الإغلاق |
| Priority | **High / Normal / Low** |
| Escalation timeouts | "Under each escalation levels, enter the escalation timeout... in minutes in which the next levels of escalations should be ESCALATED" — حتى 4 مستويات |

## 4. Multi Task Definition (المهمة المجمعة) — SET ص28-31

- **الغرض**: "group multiple tasks/complaints/requests of various departments to a single entity of a department".
- الآلية: Add → Department → Main Category (Enter/F1/double-click → **sub-category تُستوطن تلقائياً**) → Multi Task field: "Enter any letters in the field and the matching tasks list pops up" (بحث تدريجي!) → Enter → الشبكة → Save.
- **عبر الأقسام**: "Under the main task we can select the **other department's tasks also**".
- حذف عنصر: click + **F5**.
- **السلوك عند التشغيل**: "In the Manual Entry program, when you select the task defined under the Multiple Task... **all the tasks defined under that department will be assigned. A different complaint number will be created for each task**" — انفجار المهمة المجمعة إلى مهام فردية برقم مستقل لكل منها! الأولويات من تعريف كل مهمة.

## 5. الروستر الشهري (Monthly Roster) — OPR ص5-18

| المفهوم | التفصيل الموثق |
|---|---|
| البنية | Department × (Designation rows **بلون أصفر** × Employee) × أيام الشهر + عمود **Default Floor** |
| مفاتيح الإدخال | Month/Year (≥ الشهر الحالي!) + Department (يتطلب Organizational Structure معرفاً مسبقاً) |
| الورديات | General / Morning / Evening / Night (+ حسب تعريف PMS) — **سحب وإفلات** على اسم الموظف = شهر كامل، أو على تاريخ = يوم واحد |
| Weekly Off | right-click على اليوم → Weekly Off → **كل الأيام المماثلة في الشهر** تتحول 'O' (مثال: كل أيام الاثنين) |
| Floors | **بعد الورديات فقط** (وإلا رسالة منع!) — "Add or Change Floors" من Default Floor column أو right-click تاريخ؛ نافذة Select Floors؛ Deselect لكل الطوابق |
| عداوة الماضي | "You **cannot delete shifts for the past dates**" + "In the modify mode alterations can be made **only to the future days of the current month**" |
| الأزرار | Add (شهر جديد) · Modify (من قائمة الروسترات) · **Restore** (إلغاء التغييرات) · Save |
| تتبع الحالة | "You can view the status of the shift and floor on the bottom of the screen" |

## 6. الملاحظات المفقودة (Lost & Found) — OPR ص60-65

| المرحلة | الحقول الموثقة |
|---|---|
| الضياع | قيمة المادة (value of article) + مكان الضياع + التاريخ والوقت |
| العثور | اسم من عثر عليها + التاريخ والوقت + المكان |
| الإرجاع | لمن أُرجعت + متى + **اسم الشخص الموظف المسؤول** (authorized person's name) |
| المصدر | عرض بيانات **PMS Lost and Found** (View Lost Articles بتاريخ أو Load) + إضافة سجلات محلية (Add → Module dropdown = **outlet**! + Guest details) + Modify عبر Help + Print |

## 7. كيان Group SMS (OPR ص56-59)

- المستلمون: All/department → شاشة موظفين → checkbox فردي أو **select-all** → Add → Selected Details → Remove للإزالة.
- **أرقام خارج النظام**: "If you want to enter extra mobile numbers other than those available in the CARE system" + Add.
- النص: SMS Message Text → Send → حالة الإرسال حتى "SMS Sent".

## 8. جرد الكيانات المرجعية الإجمالي

| # | الكيان | النوع | مكان التعريف |
|---|---|---|---|
| 1 | CareUserMapping | ربط (User←PMS + Group Agent/Supervisor + BelongsTo Dept) | SET §1 |
| 2 | OrgStructure: Property | عرض من PMS | SET §3 |
| 3 | OrgStructure: DepartmentNode | مرجعي (PMS) | SET §3 |
| 4 | OrgStructure: DesignationNode | مرجعي (PMS) | SET §3 |
| 5 | CareEmployee | **محلي** (حقول §2.2 + Photo) | SET §3 |
| 6 | ReportingLink (Designation→Designation) | محلي (سلسلة تصعيد) | SET §3 |
| 7 | DeletedEmployeeList | أرشيف استرجاع | SET §3 |
| 8 | TaskCategory (Main+Sub) | محلي | SET §4 |
| 9 | TaskDefinition (Sub Category كاملة الخصائص) | محلي | SET §4 |
| 10 | MultiTask + MultiTaskItem | محلي (عبر أقسام!) | SET §5 |
| 11 | MonthlyRoster + RosterDay (shift/floor/weekly-off) | محلي شهري | OPR §1 |
| 12 | StaffLoginSession (types 3 + mobile/pager + استرداد) | تشغيلي | OPR §2 |
| 13 | Task/Incident (الشكوى الحية) | تشغيلي | OPR §3 |
| 14 | SMSMessage (in/out + status) | تشغيلي | OPR §3 |
| 15 | FeedbackRecord | تشغيلي | OPR §3 |
| 16 | LostFoundArticle | تشغيلي/عرض PMS | OPR §3 |
| 17 | ReportAccessMatrix (Spool/Export/Format) | محلي | SET §6 |
