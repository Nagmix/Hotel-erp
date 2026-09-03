# 05 — قواعد العمل (Business Rules) — وحدة Care

> **BR-CA-01..18**: القواعد الحاكمة الموثقة نصاً، مرتبة بالتسلسل الجوهري (آلة SMS → التصعيد → الورديات → الهيكل → التقارير).

---

## قواعد آلة الحالة والـ SMS

### BR-CA-01: الالتزام الزمني يبدأ بـ Thank You وليس بالحفظ
- النص: "The Task Assigned Estimated/Escalation time starts **once you click Thank You**." (OPR ص36)
- **اللغة الاستدلالية**: الحفظ (Confirm) يضع المهمة في Request/Incident List بلا مؤقت — الالتزام التشغيلي لحظة "شكراً لك" الودية مع الضيف.

### BR-CA-02: بروتوكول أوامر SMS الردّية
- البدء: `COMPLAINT# SPACE S` (مثال: `1 S`) — الإغلاق: `COMPLAINT# SPACE C` (`1 C`). (OPR ص39/42)
- لا بدء لمهمة غير مخصصة، ولا إغلاق قبل بدء — كل فرع يُرد برسالة خطأ صريحة (راجع WF-CA-04).

### BR-CA-03: التخصيص الآلي للحاضر فقط
- "the system will automatically send SMS to the **concerned department's logged in User**" (OPR ص29) — لا مهمة SMS لموظف غير مسجل دخولاً؛ الفرع البديل = Unassigned ثم Assign يدوي (OPR ص77-80).

### BR-CA-04: نقل المهمة داخل القسم نفسه فقط
- "the task can be transferred to another employee **who is logged in to the shift of the same department**" + نافذة Transferred To تعرض "the **logged in users of the same department**". (OPR ص73)
- **الاستدلال المعماري**: الحضور شرط التخصيص عبر كل العمليات.

### BR-CA-05: إغلاق المشرف يسلب المهمة من الحاضر
- "If the **SUPERVISOR closes the task while the attendee is still working** on the task" → SMS للحاضر: `COMPLAINT #1 CLOSED. CLOSED BY: JOHN REASON: ISSUE RESOLVED` (OPR ص43) — مسار سلطة موثق بغلق من مستوى أعلى مع إشعار إلزامي.

### BR-CA-06: الامتداد يمدد الزمن المنقضي تلقائياً
- "Select the estimated extension time in days, hours and minutes. (**The elapsed time will extend automatically**)." (OPR ص76) — الامتداد ليس ملاحظة بل تعديل حالة زمنية.

### BR-CA-07: الإلغاء للم لم تبدأ والإيقاف لما بدأ
- "Cancelled tasks are those tasks that **have not been started** and Stopped tasks are those tasks that **have already been started and cancelled**" (REP ص64) + أداة Cancel/Stop تعمل "for the tasks that are **not yet started**" (OPR ص49) — **تناقض ظاهري**: الأداة تشترط عدم البدء بينما التقرير يميز مهمات Stopped بدأت! → التفسير المحتمل: الإيقاف يمر عبر مسار آخر (مشرف/نظام) — يُسجل كحالة استنتاجية E-CA-09.

## قواعد التصعيد

### BR-CA-08: التصعيد يتبع Reporting Link حرفياً
- "Escalations in the task will follow the order as defined in the Reporting levels" (SET ص18) — مثال السلسلة: Room boy→HK Supervisor→HK Manager→FO Manager→GM→MD.

### BR-CA-09: مهلة كل مستوى تصعيد قابلة للتهيئة لكل مهمة
- "Under each escalation levels, enter the **escalation timeout**... in minutes in which the next levels of escalations should be ESCALATED" (SET ص26) — 4 مستويات × دقائق مستقلة.

## قواعد الورديات والروستر

### BR-CA-10: لا دخول بلا روستر
- "the Monthly Roster for the current month (shift and floor) **should be defined first** for the employee to be able to login. Else you get an error message **'Schedule Not Entered'**" (OPR ص20).

### BR-CA-11: الدخول خارج الوردية/أيام العطل مسموح بتنبيه
- "If the Login user tries to Login in a shift which is NOT his assigned Shift, the system will **allow him to Login only after indicating the Shift time variation**" + مثله للعطلة/الإجازة بـ Yes (OPR ص19-20) — تنبيه لا منع.

### BR-CA-12: الماضية محمية في الروستر
- "You **cannot delete shifts for the past dates**" (OPR ص9) + "alterations can be made **only to the future days of the current month**" (OPR ص14) — نمط عائلة التجميد (راجع FO اليومي/MGT الشهري/FAS السنوي/HRP الرواتب) في بُعد زمني مصغر (روستري).

### BR-CA-13: الطوابق تُعرَّف بعد الورديات
- "To define the floors you have to define the shifts first. If the shift is not defined and you are trying to define floors, then you will get the following message" (OPR ص11) — تبعية تسلسلية محكومة برسالة.

### BR-CA-14: عهدة الموبايل تنتقل بين الورديات
- "The same mobile number will be **reassigned to other personnel of the department in the next shift**" (OPR ص19) + استرداد موثق عند الخروج بالـ checkboxes (Mobile/Pager) (OPR ص28).

## قواعد الهيكل والهوية

### BR-CA-15: الهوية من PMS حصراً
- لا إنشاء مستخدمين (SET ص5)؛ الأقسام والتصنيفات من قاعدة PMS (SET ص11/13)؛ الورديات/المواقع من PMS Maintenance (OPR ص5/33)؛ الاسم غير قابل للتعديل للموظف (SET ص24).

### BR-CA-16: حذف الموظفين ناعم دوماً
- "The employee details will be deleted, and **added to the Deleted List**" (SET ص20) مع مسار استرجاع موثق (SET ص21) — لا فقدان نهائي.

### BR-CA-17: المهمة المتعددة تنفجر لشكاوى فردية
- "all the tasks defined under that department will be assigned. **A different complaint number will be created for each task**" (SET ص31) + مهام أقسام أخرى داخل المجموعة (SET ص29).

### BR-CA-18: حقوق الوحدتين (Agent مقابل Supervisor) تُحمل عند التعيين
- Agent: "can only log the Complaints" / Supervisor: "log, **Extend, Transfer and Close**... (in Supervisor Lookup program.)" (SET ص5) — ومشرف القسم يرى قسمه بينما "Normal login users can view the status **for all the departments**" (OPR ص68) — **انعكاس صلاحيات غير بديهي** (المشرف أضيق نطاقاً من المستخدم العادي في الرؤية!).
