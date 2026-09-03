# 08 — التقارير (Reports) — وحدة Care

> **20 تقريراً موثقة** (REP 73 ص) — أثقل كتلة تحليلية نسبية في المشروع (تقارير إنتاجية/كفاءة لا مالية)، بأنماط موحدة: معايير → Load → شبكة → **Chart** (7 تقارير) → **Drilldown** (3 تقارير حتى 4 مستويات!).

---

## 1. الأنماط المشتركة

| النمط | التفصيل |
|---|---|
| أطر زمنية | Date Range / Monthly / Yearly (+ Month Wise / Day Wise حصراً في #6/#7) |
| أوضاع العرض | Summary / Details (#1/#3/#5) |
| Chart | #1 (Dept/Agent/ChartType) · #3 (Employee/ChartType) · #5 · #12 (Dept/Employee/ChartType) · #13 (Dept/**Over All Feedback**/ChartType) · #16 (Employee/ChartType) · #17 |
| Drilldown | #6: Main Description → رقم الشهر → سجل المهمة الكامل · #7: Department → Main → رقم → سجل |
| سجل المهمة الكامل (مستوى 3/4) | Guest name · Incident date/time · **Check-in date · Check-out date** (من PMS!) · Incident note · Department details · Incident category · Feedback · Elapsed time · Status (Closed/Open...) |
| الرسائل البيانية | Chart window + اختيارات معايير + إعادة عرض |

## 2. الجرد التفصيلي (20)

| # | التقرير | الغرض والحقول المميزة |
|---|---|---|
| 1 | **Call Attended List** | مكالمات "agent/**IVR** or any other User"؛ Call time, incident#, room#, guest name, incident؛ مجموعات لكل تاريخ + النطاق + المستخدمون؛ Summary/Details + Spool/Print + Chart |
| 2 | Task by Runner/Technician | المهام المكتملة لكل فني: room#, guest, location, incident, **start/end date-time**؛ "total calls opened, attended and closed" لكل فني/تاريخ |
| 3 | **Response Time Analysis** | "rate the **efficiency** of the employee"؛ raised/closed/not closed لكل أسبوع/شهر؛ estimated vs consumed time؛ **لا Details مع Yearly** (V-CA-13)؛ Chart + Scroll <</>> |
| 4 | Work Start Statistics | أوقات البدء: task#, assign date-time, description, **SMS received date-time**, employee, actual start, closed date-time, status؛ **Both/Open/Closed**؛ مجموعات لكل تاريخ/نطاق |
| 5 | Staff Productivity | "analyze the staff productivity": calls count, **max/min/average durations**, average estimated time, **average variance**, closed/not closed؛ Summary/Details + Chart |
| 6 | **Tasks Statistics** (Drilldown!) | حسب Main Description × تاريخ/شهر مع Priority+Status؛ **ثلاث مستويات**: Main → أرقام → السجل الكامل؛ Month Wise/Day Wise؛ Go Back |
| 7 | Tasks Statistics by Depart | مثل #6 لكن مدخلها Department (رباعي المستويات)؛ "Room Related Guest Request" مثال Main |
| 8 | **Top Tasks Statistics** | "helps **management** to observe the top tasks"؛ **Top N** field؛ Open: occurrence rate, #escalated, **ratio of escalated**, escalation est time؛ Closed: max/min/**avg response rates**؛ **Calculate With: Assigned Date / Work Start Date** (V-CA-16) |
| 9 | Repeated Issues List | الحوادث المتكررة؛ **Rooms (Floor+Dept) / Other Locations (بلا Floor — V-CA-14)**؛ All / Issues Repeated + **"No of Times"** field؛ room#, issue#, desc, issue+closed date-time, guest, logger, assigned, attendee, status |
| 10 | Incidents by Floor List | حسب الطابق؛ Rooms/Other؛ All/**Selected Task** (بحث تدريجي)؛ room#, incident date, guest, desc, attendee؛ الترتيب: **Floor → Department → Task** |
| 11 | SMS Sent List | ما أُرسل SMS: date, complaint#, location, runner, **mobile number**, **acknowledgement date**؛ Total SMS لكل تاريخ |
| 12 | Task Category Report | حسب الفئة: **Requests/Complaints/Incidents/Others**؛ **4 مستويات فرز: Department, Runner/Technician, Date, Task type**؛ serial#, incident#, room#, guest, note, desc؛ ملخصات لكل تاريخ ثم لكل قسم؛ Chart |
| 13 | **Guest Feedback Statistics** | تقييمات الضيوف: agent (سجّل التقييم), runner (المخصص), agent (البدء), total, satisfied, not satisfied, not served, **guest name إن unavailable**؛ ملخص لكل قسم ثم الكل؛ Chart + **Over All Feedback** |
| 14 | Extended/Trans. Incident | ثلاثة أنماط عرض حسب الاختيار: **Extended** (+Estimated Time, Extended Date/Time) / **Transferred** (+To/From, Transferred Date/Time) / **Closed** (+Closed Date/Time) — مع Reason وlogged User دائماً؛ فرز Departments ثم Floors |
| 15 | **Escalation Report** | المهام المصعدة: complaint#, task date-time, desc, assigned date-time, agent, **room#/outlet**, escalation level + **to whom escalated**, escalation closed date-time, status؛ فلاتر Dept/Floor/**Escalation Level** |
| 16 | Feedback List | Feedback أو Cancelled/Stopped × **Issue Date / Feedback Date**؛ task#, task date-time, room#, guest, closed date-time, feedback date-time, type, note (+الملغاة: date+note)؛ Chart |
| 17 | Shift List | المهام حسب الوردية: task#, date-time, desc, assigned, **SMS date-time**, started by, start time, closed, status+reason؛ ملخص لكل تاريخ + النطاق: **(Raised, Closed, Open, SMS Queued!)**؛ Chart |
| 18 | Cancelled/Stopped Task | التمييز الموثق: Cancelled=لم تبدأ / Stopped=بدأت؛ Both/Cancelled/Stopped؛ room#, dept, guest, incident date, task, stopped date, reason, user؛ ملخص نهائي |
| 19 | Staff Log-in & Log-out List | employee name, **employee number**, designation, login/logout date-time, **login type**؛ الترتيب: Department → Shift → Date |
| 20 | Task List (الماجستير) | المهام **المعرّفة في النظام**: Main Category, Sub Category, **IVR Code**, Estimated Time, designation, task type؛ All/Multiple Task؛ **Main معطل مع All Departments** (V-CA-15) |

## 3. الكتل التحليلية (Insight Blocks)

| الكتلة | التقارير | القرار الذي تخدمه |
|---|---|---|
| **إنتاجية الفرد** | 2, 3, 4, 5, 19 | تقييم/مكافأة الفني (efficiency + variance + login discipline) |
| **صحة العمليات** | 6, 7, 8, 17 | اختناقات الأقسام والأوقات (escalation ratio, SMS Queued!) |
| **جودة الخدمة** | 13, 16 | Guest Satisfaction (Satisfied/Not/Not Served/Unavailable) |
| **سلامة العملية** | 11, 14, 15, 18 | المساءلة (acknowledgement dates, transferred from/to, escalated to whom, cancel reasons + user) |
| **مرجعية الإعداد** | 20 | تدقيق أكواد IVR وأوقات التعريف |

## 4. الاكتشافات التحليلية للتقارير

1. **أول ظهور لمقياس SMS Queued كملخص إداري** (Shift List): قياس تراكم البوابة نفسها كمؤشر صحة تقنية — مبتكر للحقبة.
2. **Drilldown حتى 4 مستويات** (Tasks Statistics by Depart) مع بيانات إقامة الضيف (CI/CO من PMS) في القاع — أعمق سلسلة تنقيب موثقة في تقارير المشروع بعد MGT-LUK.
3. **النسب والإحصاءات المحسوبة**: occurrence rate, ratio of escalated, average variance — تجاوز العرض الخام إلى القياس الكمي.
4. **تقرير الماجستير Task List مع IVR Code** — الدليل الثاني (بعد Call Attended "agent/IVR") على وجود قناة هاتفية تفاعلية مدمجة (GAP-CA-D04).
5. **لا تقرير مالي واحد** — بما يتسق مع غياب الترحيل المحاسبي (GAP-CA-D01): الكتلة كلها تشغيلية.
6. **طباعة/تصدير خاضعة لـ Restrict Reports** (Spool/Export/Excel/OpenCalc/Direct لكل مستخدم) — راجع 07 §4.
