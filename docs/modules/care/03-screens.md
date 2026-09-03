# 03 — جرد الشاشات (Screens Inventory) — وحدة Care

> **32 شاشة/برنامج موثقة** عبر الدلائل الثلاثة، مع الحقول وأزرار الوظائف ومفاتيح الاختصار الموثقة نصاً. النمط الغالب: **قوائم سياقية right-click** (شجرة الهيكل + شبكة المهام) و**سحب وإفلات** في الروستر.

---

## 1. شاشات Setup (6)

### S-CA-01: User Creation — SET ص5-6
- الحقول: User (F1/double-click ← PMS) · Group dropdown (Agent/Supervisor) · Belongs To (Supervisor Group → Department).
- الأزرار: Save. التعديل: إعادة اختيار المستخدم + تغيير + Save.

### S-CA-02: Define Rights — SET ص7-9
- المراحل: Groups/Users radio → قائمة يمين → Continue → شاشة Sub Modules + Menu Options (تحت Main Module CARE) →勾选 → Save.
- الأزرار: Select (الكل) / Deselect (إلغاء الكل) / Continue / Save.

### S-CA-03: Organizational Structure — SET ص10-24
- **شاشة شجرية**: Property (يسار) ← Department ← Designation ← Employee.
- القوائم السياقية الموثقة: Property→Department · Department→Designation · Designation→Employee (Add New) · Designation→**Reporting To…** · Employee→Delete / Edit Details / From Help→**Deleted List**.
- لوحة يمين: حقول الموظف (§01.2.2) + Photo/Clear Photo + Confirm.
- أول تصنيف لقسم جديد: رسالة → Exit → يظهر خيار Reporting.
- التعديل الهرمي: نافذة Reporting To → Department+Designation dropdowns → Ok → "Previously Referred To…" يتحدث.

### S-CA-04: Task and Complaints — SET ص25-27
- الحقول: Department · Main Category Code/Description · Sub Category Code/Description · Estimated Time for Response (دقائق) · Designation · Type (Complaint/Request/Incident/Other) · Charges (Y/N) · Feedback (Y/N) · Priority (High/Normal/Low) · **Escalation timeout لكل مستوى**.
- الأزرار: Add / Save. Multi-sub: F1/double-click على Main → إضافة sub إضافية.

### S-CA-05: Multi Task Definition — SET ص28-31
- الحقول: Department · Main Category (Enter/F1/dbl → sub auto-populate) · Multi Task (بحث تدريجي حرفي).
- الشبكة: task + department لكل عنصر. **F5** حذف صف. Save.

### S-CA-06: Restrict Reports — SET ص32-34
- User dropdown → زر (عرض) → شبكة Module × Reports Name × Spool × Export × Format (Excel/Open Calc/Direct).
- التبديل: double-click/Space/Enter على Yes/No. Save / Exit.

## 2. شاشات Operations (6 رئيسية + 12 نافذة فرعية)

### S-CA-07: Monthly Roster — OPR ص5-18
- الرأس: Add / Modify / Restore / Save + Month/Year + Department + شريط حالة (الوردية/الطابق أسفل الشاشة).
- الشبكة: Designation (صفوف صفراء) → Employee × أيام الشهر + عمود Default Floor.
- **لوحة الورديات القابلة للسحب**: General/Morning/Evening/Night...
- القوائم السياقية: Clear (حذف وردية — ليس للتواريخ الماضية!) · Weekly Off (يوم → كل مماثلاته) · Add or Change Floors (من العمود أو التاريخ).
- نافذة Select Floors: Available Floors + select/deselect + Select/Deselect + Select.

### S-CA-08: Staff Login — OPR ص19-26
- الحقول: User Type (Supervisor/GRE/Duty Manager) · Employee# (F1 ← قائمة الموظفين) · الاسم+القسم (عرض) · Shift (F1 — **تُدرج الورديات المتاحة وقت الدخول فقط**؛ يُمكَّن فقط إذا لا وردية معينة أو وردية مختلفة) · **Mobile#** (أي رقم من Org Structure — عليه تصل المهام) · Pager#.
- الأزرار: Submit.
- تنبيهات: وردية غير معينة (alert + سماح) · عطلة/إجازة (alert + Yes) · **'Schedule Not Entered'** (منع — لا روستر).

### S-CA-09: Staff Logout — OPR ص27-28
- الحقول: User Type · Employee# (F1 يعرض **المسجلين حالياً فقط!**) · checkbox **Mobile** + **Pager** (استرداد العهدة).
- الأزرار: Submit. الشرط الضمني: "Once all the assigned tasks have been closed or transferred to the next employee logging in to the shift, and feedback entered".

### S-CA-10: Manual Entry Program (الأم) — OPR ص29-55
- **منطقة الإدخال**: Room/Unoccupied Room/Other Area (Enter) → F1 اختيار → **بيانات الضيف تظهر يميناً تلقائياً** → Task (بحث تدريجي) → Special Instructions (≤25) → Confirm → نقل للـ Request/Incident List → **Thank You** (يبدأ المؤقت!).
- **SMS Status window**: Complaint# · department · request · request time · est time · SMS status (Delivered/Queued) · Assigned employee · Room# · Guest Name · **Elapsed time** · Request Date/Time. Special Instructions تظهر بمرور المؤشر.
- **زر Request/Incidents** (تحت Special Instructions): متاح **لخيار ROOM فقط** — Show All / Pending / Close — يعرض Runner/Technician name.
- **الأدوات**: آلة حاسبة 15 خانة · تقويم · التوقيت القياسي لمدينة (dropdown) · **Zoom** (يمين النافذة) + Close.
- الأزرار الجانبية الموثقة: Feedback Cancel · Cancel/Stop · Work Start · Group SMS · Lost and Found.

### S-CA-11: Feedback Cancel — OPR ص45-48
- radio: Feedback / Cancel or Stop Tasks.
- Feedback: شبكة مهام → double-click (صف أبيض + تعبئة الحقول: Complaint#/Room#/المهمة/الضيف) → تقييم (**Satisfied/Not Satisfied/Not Served/Guest Unavailable**) → نص الملاحظة → Save.
- Cancel/Stop: شبكة → radio Cancel/Stop (**للمهام غير المبدوءة فقط**؛ الافتراضي Cancel) → Notes (السبب) → Save → تختفي من الشبكة.

### S-CA-12: Work Start (يدوي) — OPR ص53-55
- Complaint# → عرض وصف المهمة + Special Instructions → **Work Start**.
- للمهام غير المخصصة: تظهر في Work-In-Progress بعمود Assigned To فارغاً → right-click → **Assign**.

### S-CA-13: Group SMS — OPR ص56-59 (+66 مستقلة)
- dropdown All/department → شبكة موظفين → checkboxes (+select-all) → Add → Selected Details (Remove للإزالة) → **حقل Mobile# + Add لأرقام خارج النظام** → SMS Message Text → Send → Status → "SMS Sent". Exit.

### S-CA-14: Lost and Found — OPR ص60-65
- الأزرار: **View Lost Articles** (نطاق تاريخ أو Load) · **Return** (العثور+الإرجاع) · Add (Module dropdown=**outlet** + Guest details) · Modify (Help) · Print · double-click للتفصيل · cancel.

### S-CA-15: Agent Console — OPR ص67
- "All the statuses of the Current Task" + عمليات: Group SMS / Lost & Found / Feedback Cancel / Work Start / **Break**. الأزرار: Sign Off.

### S-CA-16: Supervisor Lookup — OPR ص68-80
- **Department dropdown** (المشرف يختار قسمه؛ "Normal login users can view the status for all the departments").
- أزرار: **Clear Pending SMS** (زر بيسار الشاشة).
- قوائم سياقية على المهمة:
  - **Close** → نافذة Close Comp/Req#: Reason + **Approximate Cost** + Close.
  - **Transfer** → نافذة Transferred To (المسجلون دخولاً في نفس القسم!) + Reason + More + Confirm.
  - **Extend Est. Time** → أيام/ساعات/دقائق ("The elapsed time will extend automatically") + Reason + Confirm.
  - **Assign** → قائمة الحاضرين → اختيار → Assigned To يمتلئ + SMS تخصيص.

## 3. شاشات التقارير (20) — REP

> النمط الموحد: شاشة معايير (dropdowns + date options) → **Load** → شبكة نتائج + **Chart** (بعضها) + Spool/Print. التفصيل الكامل في 08-reports.md.

| # | الشاشة | معايير مميزة | Chart | Drilldown |
|---|---|---|---|---|
| 1 | Call Attended List | Agent/Other Users · Dept · Agent · Summary/Details | ✓ (Dept/Agent/نوع) | — |
| 2 | Task by Runner/Technician | Runner أو All | — | — |
| 3 | Response Time Analysis | Dept · Runner · Summary/Details (**لا Details مع Yearly!**) | ✓ | Scroll <</>> |
| 4 | Work Start Statistics | Dept · Runner · **Both/Open/Closed** | — | — |
| 5 | Staff Productivity | Dept · Runner · Summary/Details | ✓ | — |
| 6 | Tasks Statistics | Month Wise/Day Wise · Priority · Status | — | **ثلاثي**: Main→أرقام→سجل |
| 7 | Tasks Statistics by Depart | Month/Day · Priority · Status | — | **رباعي**: Dept→Main→رقم→سجل |
| 8 | Top Tasks Statistics | Open/Closed · **Top N** · **Calculate With (Assigned/Work Start)** | — | — |
| 9 | Repeated Issues List | **Rooms/Other Locations (بلا Floor!)** · All/Issues Repeated + **No of Times** | — | — |
| 10 | Incidents by Floor List | Rooms/Other · All/Selected Task (بحث حرفي) | — | — |
| 11 | SMS Sent List | Runner أو All | — | — |
| 12 | Task Category Report | 4 مستويات فرز (Dept/Runner/Date/Type) | ✓ | — |
| 13 | Guest Feedback Statistics | Dept · Agent · Runner · **Over All Feedback** | ✓ | — |
| 14 | Extended/Trans. Incident | **Extended/Transferred/Closed** · Floor · Dept | — | — |
| 15 | Escalation Report | Dept · Floor · **Escalation Level** | — | — |
| 16 | Feedback List | **Issue Date/Feedback Date** × **Feedback/Cancelled-Stopped** | ✓ | — |
| 17 | Shift List | Shift · Date Range/Monthly (+**SMS Queued** في الملخص!) | ✓ | — |
| 18 | Cancelled/Stopped Task | Both/Cancelled/Stopped | — | — |
| 19 | Staff Log-in & Log-out List | Dept · Shift | — | — |
| 20 | Task List (ماجستير) | All/Multiple Task · Dept · Main (**معطل مع All Departments**) | — | — |

## 4. إحصاء الشاشات

| الفئة | العدد |
|---|---|
| Setup | 6 |
| Operations (رئيسية) | 6 |
| نوافذ فرعية مذكورة (Reporting To · Select Floors · Close Comp/Req# · Transferred To · Extend · Assign · Select Floors-day · Feedback/Cancel/Stop · Request/Incidents view · View Lost Articles · Returned Details · Chart windows) | 12+ |
| التقارير | 20 |
| **الإجمالي الموثق** | **≈44 عنصر شاشي (32 برنامجاً رئيسياً/فرعياً)** |
