# 04 — سير العمل (Workflows) — وحدة Care

> **WF-CA-01..16**: دورات العمل الموثقة نصاً عبر الدلائل الثلاثة — قلب الوحدة هو **آلة حالة المهمة عبر SMS** (WF-CA-04) ودورة التصعيد التلقائي (WF-CA-05).

---

## WF-CA-01: دورة تهيئة الوحدة (One-time)
```
PMS جاهز (Users/Departments/Designations/Shifts/Locations)
 → [SET §1] User Creation: ربط كل مستخدم PMS → Group (Agent/Supervisor) + BelongsTo
 → [SET §2] Define Rights: Group/User × Menu Options (+Add/Modify/Delete)
 → [SET §3] Organizational Structure: Property→Department→Designation→Employee (photo!)
 → [SET §3] Reporting To لكل Designation (سلسلة التصعيد!)
 → [SET §4] Task Definition لكل قسم (Main/Sub + Est Time + Priority + Charges + Feedback + Escalation timeouts)
 → [SET §5] Multi Tasks (اختياري)
 → [SET §6] Restrict Reports حسب المستخدم
```

## WF-CA-02: الدورة الشهرية — الروستر
```
Add → Month/Year (≥ الحالي) → Department → Enter
 → عرض التصنيفات/الموظفين × الأيام (صفوف التصنيف صفراء)
 → سحب وردية على الموظف (شهر كامل) أو على تاريخ (يوم)
 → right-click يوم → Weekly Off (كل مماثلات اليوم)
 → تعيين الطوابق (بعد الورديات!): Add or Change Floors → Select Floors → select/deselect
 → تعديلات اليوم الواحد (مستقبلي فقط) → Save
 → (الشهور اللاحقة: Add جديد / أو Modify لروستر قائم / Restore للتراجع)
```

## WF-CA-03: دخول/خروج الطاقم (يومي)
```
Login: User Type (Supervisor/GRE/Duty Manager) → Employee# (F1) → Shift (F1 — المتاحة وقت الدخول)
 → Mobile# (قناة المهام) + Pager# → Submit
 [Alerts: وردية مغايرة → سماح بعد تنبيه · عطلة/إجازة → Yes · لا روستر → 'Schedule Not Entered' منع]

Logout (بعد إغلاق/نقل كل مهامه وتسجيل الملاحظات):
 → Logout → User Type → Employee# (F1 = المسجلون فقط)
 → إل تأشير استرداد Mobile + Pager → Submit
 [الموبايل يعود متاحاً لموظف الوردية التالية بنفس القسم]
```

## WF-CA-04: آلة حالة المهمة عبر SMS (القلب) — OPR ص33-44
```
[Manual Entry] Room/Unoccupied/Other Area → F1 → (بيانات الضيف تظهر للـ Room)
 → Task (بحث تدريجي) [+ مهام متعددة لنفس المكان]
 → Special Instructions (≤25) → Confirm → (ينتقل إلى Request/Incident List مع Priority+EstTime)
 → [Thank You] ═══ المؤقت يبدأ (Est/Escalation) ═══
 → SMS آلي للموظف المسجل: "<1> Complaint#: 1 Room#: OR0707 Task.. Spe.Ins.. Est.Time: 10 mins Priority: High EscLevel: 0"
 → SMS Status: Queued → Delivered
 → [الموظف يرد "1 S"] → TASK #1 WORK STARTED → Work in Progress
 → [الموظف يرد "1 C"] → TASK #1 WORK CLOSED
 → (Feedback required? نعم → Awaiting Feedback → [WF-CA-06] : لا → تختفي من الشاشة)
```
**فروع الخطأ الموثقة** (OPR ص40-43):
- تكرار S → `TASK #1 IS ALREADY STARTED`
- S لمهمة غير مخصصة له → `TASK #1 IS NOT ASSIGNED TO YOU. WORK NOT STARTED`
- C قبل S → `TASK #1 IS NOT YET STARTED`
- تكرار C → `TASK #1 IS ALREADY CLOSED`
- **إغلاق المشرف أثناء العمل** → `COMPLAINT #1 CLOSED. CLOSED BY: JOHN REASON: ISSUE RESOLVED`

## WF-CA-05: التصعيد التلقائي (Escalation)
```
[Thank You] → انقضاء Estimated Time دون إغلاق
 → Esc Level 1 → SMS للمستوى التالي في Reporting Link (timeout من تعريف المهمة)
 → Level 2 → Level 3 → Level 4 (ألوان مميزة لكل مستوى)
 [أي مستوى: المشرف يستطيع Close/Transfer/Extend — WF-CA-08]
 [رصد: Escalation Report + Top Tasks (Open: ratio escalated!)]
```

## WF-CA-06: دورة الملاحظات (Feedback)
```
[Awaiting Feedback] → [Feedback Cancel] → radio Feedback → double-click المهمة (صف أبيض + تعبئة)
 → التقييم: Satisfied / Not Satisfied / Not Served / Guest Unavailable
 → نص الملاحظة → Save
 → تغذية: Guest Feedback Statistics + Feedback List (+Charts)
```

## WF-CA-07: الإلغاء/الإيقاف
```
[Feedback Cancel] → radio Cancel or Stop Tasks → اختيار (غير المبدوءة)
 → Cancel (افتراضي: لم تبدأ) أو Stop (بدأت ثم أُلغيت)
 → Notes (السبب) → Save → تختفي من الشبكة
 → تغذية: Cancelled/Stopped Task report (يعرض التمييز!) + Feedback List (خيار Cancelled/Stopped)
```

## WF-CA-08: عمليات المشرف (Supervisor Lookup)
```
Supervisor Lookup → Department dropdown → الشبكة الحية
 → Close: right-click → Reason + Approximate Cost → Close (+SMS إشعار للحاضر — WF-CA-04 فرع 5)
 → Transfer: right-click → Transferred To (المسجلون بنفس القسم!) + Reason → More → Confirm
 → Extend Est. Time: right-click → أيام/ساعات/دقائق + Reason → Confirm (Elapsed يتمدد تلقائياً)
 → Assign: (لمهمة Work Start يدوية غير مخصصة) → right-click → Assign → اختيار الحاضر → SMS تخصيص
 → Clear Pending SMS: زر عام (تفريغ الرسائل العالقة)
```

## WF-CA-09: المهمة غير المخصصة (Unassigned)
```
لا موظف مسجل للقسم + رُفعت شكوى للقسم
 → [Work Start يدوي] → Complaint# → Work Start → تظهر في WIP بـ Assigned To فارغ
 → (لاحقاً عند Login أحدهم) right-click → Assign → SMS
 [دليل المستخدم: "The same Task can be transferred to the respective Department's logged users through Supervisor log-in"]
```

## WF-CA-10: المهمة المتعددة (Multi Task فوري)
```
[Manual Entry] اختيار مهمة من نوع Multi Task
 ═══ انفجار تلقائي ═══ كل مهام المجموعة تُخصص (عبر الأقسام!)
 → رقم شكوى مستقل لكل مهمة ("A different complaint number will be created for each task")
 → كل مهمة بأولويتها ووقتها المعرّفَين → تتبع كل واحدة عبر WF-CA-04 مستقلة
```

## WF-CA-11: البث الجماعي (Group SMS)
```
[Group SMS] All/department → checkboxes موظفين (+select-all) → Add
 → Selected Details (Remove لإخراج) [+ Mobile# + Add لأرقام خارجية]
 → SMS Message Text → Send → Status حتى SMS Sent
 [حالة الاستخدام الموثقة: VIP visits — "Visiting of any VIP guests... intimated to the concerned departments' employees"]
```

## WF-CA-12: المفقودات (Lost and Found)
```
عرض: View Lost Articles (نطاق تاريخ/Load) [بيانات PMS + المحلية] → double-click تفصيل
 → Return: قائمة ما عُثر وأُرجع → double-click → Returned Details → cancel
إضافة محلية: Add → Module (=outlet!) + تفاصيل الضياع + Guest → Save
تعديل: Modify → Help → اختيار → تعديل → Save
طباعة: Print
```

## WF-CA-13: استعلام الغرفة الحي (Room-during-Entry)
```
[Manual Entry] خيار ROOM → F1 → Room#
 → Guest details فوراً يمين الشاشة (PMS حي)
 → [Request/Incidents] (ROOM فقط!): Show All / Pending → تاريخ الضيوف السابقة + Runner/Technician
 [دعم قرار: "view if there were any previous requests or incidents for the selected room"]
```

## WF-CA-14: وحدة تحكم الوكيل (Agent Console)
```
Agent Console → كل حالات المهام الجارية
 → Group SMS / Lost & Found / Feedback Cancel / Work Start / Break
 → Sign Off
```

## WF-CA-15: تدقيق الاتصال الهاتفي (Call-based)
```
[IVR/Agent] مكالمة ضيف → تسجيل (Call Attended يوثق: time of call, incident#, room#, guest, incident)
 → توليد مهمة كالمعتاد (WF-CA-04)
 → تقرير Call Attended List (Summary/Details/Chart + مجموعات لكل تاريخ/نطاق/مستخدم)
```

## WF-CA-16: دورة الرواتب الوهمية (تحذير تحليلي — ليست موثقة كترحيل!)
```
إغلاق المهمة → Approximate Cost (قيمة أعباء إن وجدت) + Charges Y/N في التعريف
 → ═══ لا مسار موثق لفوليو الضيوف أو قيود مالية ═══ (GAP-CA-D01)
```

---

## خريطة الحالة الكاملة للمهمة (14 حالة موثقة)

| الحالة | الدخول | الخروج |
|---|---|---|
| Request/Incident List (مسجلة قبل Thank You) | Confirm | Thank You |
| **SMS Queued** | Thank You | إرسال فعلي |
| **SMS Delivered** | بوابة SMS | رد S أو إغلاق مشرف |
| **Work in Progress** | رد `S` | رد `C` أو Close/Transfer |
| **Awaiting Feedback** | رد `C` (Feedback=Y) | تسجيل التقييم |
| **Closed** | رد `C` أو إغلاق مشرف | نهائية (تقارير) |
| **Cancelled** (لم تبدأ) | Cancel + Notes | نهائية |
| **Stopped** (بدأت) | Stop + Notes | نهائية |
| **Unassigned** (بدأت يدوياً) | Work Start يدوي | Assign |
| **Escalated L1..L4** | انقضاء timeout | أي إغلاق/نقل/تمديد |
| Pink Guest (غرفة غير مشغولة) | رفع على Unoccupied | — (تلوين) |
| Magenta Room# (منطقة أخرى) | رفع على Other Area | — (تلوين) |
