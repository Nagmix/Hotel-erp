# 10 — المعاملات (Transactions) — وحدة Care

> المعاملات التشغيلية الحية: **المهمة/الشكوى** (المعاملة المركزية) + جلسة الدخول + رسالة SMS + الملاحظة + سجل المفقودات + البث. **لا معاملات مالية** (راجع 11).

---

## 1. المهمة/الشكوى (Task/Incident) — المعاملة المركزية

### 1.1 البنية الحقلية الموثقة (تجميع من كل المواضع)

| الحقل | المصدر/القيمة | التوثيق |
|---|---|---|
| Complaint/Incident # | تسلسلي (مستقل لكل مهمة حتى داخل Multi Task) | SET ص31 |
| المكان | Room# / Unoccupied Room / Other Area (اسم الموقع يظهر في عمود Room# للمناطق) | OPR ص33/45 |
| Guest Name | من PMS حي (فارغ = غرفة غير مشغولة أو منطقة أخرى!) | OPR ص45 |
| Room# | من PMS (OR0707 نمط الكود في مثال SMS!) | OPR ص38 |
| Task (Main/Sub) | من Task Definition | OPR ص35 |
| Special Instructions | ≤25 حرفاً رقمياً-حرفياً | OPR ص36 |
| Type | Complaint/Request/Incident/Other | SET ص26 |
| Priority | High/Normal/Low (تلوين) | SET ص26 + OPR ص30 |
| Estimated Time | دقائق من التعريف (+امتدادات D/H/M) | SET ص26 + OPR ص75 |
| Escalation Level | 0 (بداية) → 1..4 (تلوين) | OPR ص38/30 |
| Assigned To | الموظف المسجل دخولاً / فارغ = Unassigned | OPR ص77 |
| Runner/Technician | المنفذ الفعلي | OPR ص51 |
| SMS Status | Queued / Delivered | OPR ص37 |
| Elapsed time | زمن منقضٍ (يتمدد مع Extend!) | OPR ص39 + ص76 |
| Status | Open / Work in Progress / Awaiting Feedback / Closed / Cancelled / Stopped | عابر |
| Check-in / Check-out dates | **من PMS** (تظهر في drilldown التقارير) | REP ص25 |
| Feedback | Satisfied/Not/Not Served/Guest Unavailable + Note | OPR ص47 |
| Close Reason + **Approximate Cost** | عند إغلاق المشرف | OPR ص72 |
| logged User | من رفع/أغلق (accountability) | REP ص41 |

### 1.2 دورات كتابة موثقة

- **رفع**: Confirm → Request/Incident List → Thank You (تنشيط المؤقت) → SMS آلي.
- **بدء**: رد `S` أو Work Start يدوي → WIP.
- **إغلاق**: رد `C` أو Close مشرف (Reason+Cost).
- **نقل**: Transfer (To من مسجلي القسم + Reason).
- **تمديد**: Extend (D/H/M + Reason) — Elapsed يتمدد.
- **إلغاء/إيقاف**: Cancel/Stop + Notes (غير المبدوءة).
- **Multi Task**: اختيار واحد → N مهام فردية بأرقام مستقلة.

## 2. جلسة الدخول (Staff Login Session)

| الحقل | ملاحظات |
|---|---|
| User Type | Supervisor / GRE / Duty Manager |
| Employee# + Name + Department | F1 + عرض |
| Shift | من الروستر أو اختيار (المتاحة وقت الدخول) |
| **Mobile#** | قناة المهام (أي رقم من Org Structure) |
| **Pager#** | عهدة ثانية |
| Login/Logout date-time | يغذي تقرير #19 |
| استرداد Mobile/Pager | checkboxes عند الخروج |
| شروط الخروج | إغلاق/نقل كل المهام + الملاحظات |

## 3. رسالة SMS (كلا الاتجاهين)

| الاتجاه | المحتوى الموثق |
|---|---|
| صادر (تخصيص) | `<1> Complaint #: 1 Room #: OR0707 Task: Task details Spe. Ins: Special Instructions Est. Time: 10 mins Priority: High Esc Level: 0` |
| صادر (رد نظام) | `TASK #1 WORK STARTED` / `TASK #1 WORK CLOSED` |
| صادر (أخطاء) | `TASK #1 IS ALREADY STARTED` / `TASK #1 IS NOT ASSIGNED TO YOU. WORK NOT STARTED` / `TASK #1 IS NOT YET STARTED` / `TASK #1 IS ALREADY CLOSED` |
| صادر (إغلاق مشرف أثناء العمل) | `COMPLAINT #1 CLOSED. CLOSED BY: JOHN REASON: ISSUE RESOLVED` |
| وارد (أوامر) | `1 S` (بدء) / `1 C` (إغلاق) |
| Group SMS | نص حر لقائمة مستلمين (+أرقام خارجية) — حالة حتى SMS Sent |
| تصعيد | "Depending on the level of escalation the escalation number changes in the SMS as 1/2/3/4" |

## 4. سجل المفقودات (Lost & Found Record)

- مراحل الحقول: الضياع (قيمة/مكان/تاريخ-وقت) → العثور (شخص/تاريخ-وقت/مكان) → الإرجاع (لمن/متى/موظف مسؤول).
- مصدر مزدوج: عرض PMS + سجلات محلية (Add بـ Module=outlet).
- الطباعة: Print.

## 5. ملاحظات الضيف (Feedback Record)

- التقييم الرباعي + Note + تاريخ/وقت التسجيل (Feedback Date) مقابل تاريخ المهمة (Issue Date) — التقارير تفصل بينهما (REP ص59).

## 6. جرد المعاملات الإجمالي

| # | المعاملة | مشغّلها | حالة النتيجة |
|---|---|---|---|
| 1 | Task Raise | Agent/أي وكيل | Request List |
| 2 | Thank You Commit | الوكيل | SMS Queued |
| 3 | SMS Send (آلي) | النظام | Delivered |
| 4 | Work Start (SMS S) | المنفذ | WIP |
| 5 | Work Close (SMS C) | المنفذ | Closed/AwaitingFeedback |
| 6 | Supervisor Close | المشرف | Closed (+SMS إشعار) |
| 7 | Transfer | المشرف | WIP (منفذ جديد) |
| 8 | Extend | المشرف | WIP (زمن ممتد) |
| 9 | Assign (لUnassigned) | المشرف | WIP (مخصص) |
| 10 | Cancel/Stop | وكيل بطلب ضيف/مشرف | Cancelled/Stopped |
| 11 | Feedback Entry | الوكيل | مكتملة |
| 12 | Staff Login | الموظف | جلسة نشطة |
| 13 | Staff Logout | الموظف | جلسة مغلقة (+استرداد) |
| 14 | Group SMS | أي مصرح | SMS Sent |
| 15 | Lost&Found Add/Modify | مستخدم | سجل |
| 16 | Escalation Tick (مؤقت) | النظام | Esc L+1 |

> **لا معاملات مالية إطلاقاً** — تقاطع المحاسبة يقتصر على حقل Approximate Cost وصفي (راجع 11-accounting-impact).
