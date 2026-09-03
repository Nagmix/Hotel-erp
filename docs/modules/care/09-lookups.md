# 09 — الاستعلامات والبحث (Lookups) — وحدة Care

> Care ليست وحدة Lookups كثيفة (لا دليل LUK خاص بها — GAP-CA-D02)، لكن تحوي **11 نمط استعلام تشغيلي حياً** موزعاً داخل الشاشات + Lookup المشرف كغرفة عمليات.

---

## 1. الاستعلامات الحية الموثقة

| # | الاستعلام | المكان | التفصيل |
|---|---|---|---|
| 1 | **Employee Name Help** (F1) | Staff Login | "double-click in the field or Press F1 to select the employee name from the Employee Name Help Screen" — الاسم+القسم يُعرضان |
| 2 | **قائمة المسجلين حالياً** (F1 في Logout) | Staff Logout | "press F1 on your keyboard to **view the list of logged in employee**" — استعلام حضور حي |
| 3 | **Shift Help** (F1) | Staff Login | "select the employee's shift from the Shift Help Screen. Note: The **available shifts during the login time** will be listed" — استعلام مقيد بالزمن الحالي |
| 4 | **Room/Unoccupied/Other Area** (F1) | Manual Entry | من "the Maintenance module in PMS" — الغرف/المناطق الحية؛ Room# يجرّ بيانات الضيف فوراً |
| 5 | **البحث التدريجي للمهام** | Manual Entry + Multi Task + Incidents by Floor | "Enter any letters in the field and **the matching tasks list pops up**" / "type a letter of the task... you will get the list of matching tasks" — نفس النمط في 3 مواضع |
| 6 | **Request/Incidents للغرفة** | Manual Entry (زر ROOM فقط) | Show All / Pending: "previous requests or incidents for the selected room" + request/incident, time raised, estimated time, **elapsed time**, **Runner/Technician name** |
| 7 | **Special Instructions hover** | Manual Entry (SMS Status) | "you can view it by **moving the cursor** on the SMS Status" — تلميح حي |
| 8 | **Supervisor Lookup** | العمليات | شبكة كل حالات المهام للقسم المختار + عمليات السياق (Close/Transfer/Extend/Assign) — **غرفة عمليات وليست استعلاماً** |
| 9 | **Deleted Employee List** | Org Structure → Help | "From Help → **Deleted List**" → اختيار → Home → استرجاع |
| 10 | **Lost Articles / Returned** | Lost & Found | View Lost Articles (نطاق تاريخ/Load) + Return (قائمة المعثور والمُرجع) — يعرض **بيانات PMS L&F** |
| 11 | **Pending SMS + Clear** | Supervisor Lookup | "Click [زر] to **clear any pending SMS**" — إدارة قائمة انتظار البوابة |

## 2. أوضاع الاستعلام المشترك

- **F1 = معيار المشروع العام** (متسق مع FO/POS/BNQ/MGT/HRP) — كل حقول الاختيار القياسية.
- **الشبكة الحية (Live grid)**: Manual Entry SMS Status وSupervisor Lookup هما لوحتا مراقبة تتحديثان بالحالة (Delivered/Queued/WIP/Awaiting Feedback) — أقرب شيء لمفهوم Dashboard في 6i.
- **البحث التدريجي (Type-ahead)**: نمط متقدم متكرر 3 مرات — أصل UX جيد للترجمة الحرفية (F-CA-7).

## 3. غرفة عمليات Supervisor Lookup بالتفصيل — OPR ص68-80

| العنصر | الوصف |
|---|---|
| النطاق | قسم واحد للمشرف (dropdown) / كل الأقسام للمستخدم العادي |
| الأعمدة | حالات المهام الجارية (SMS Status / WIP / Awaiting Feedback) + Unassigned |
| العمليات السياقية | Close (Reason+Cost) · Transfer (نفس القسم+Reason) · Extend (D/H/M+Reason) · Assign (للحاضرين) |
| الأدوات | **Clear Pending SMS** |
| التكامل | كل عملية تولّد SMS موثق (راجع WF-CA-04/08) |

## 4. ملاحظة غياب دليل LUK

- الوحدات السابقة: FO-LUK/POS-LUK/MGT-LUK/BNQ-LUK (وداخل HRP تقارير). **Care بلا دليل LUK** في الحزمة (اسم الملف REP يجمع "REPORTS & LOOKUPS" لكن محتواه 20 تقريراً فقط) — GAP-CA-D02: استعلامات دقيقة (تقاطع موظف×وردية×طابق مثلاً) غير موثقة.
