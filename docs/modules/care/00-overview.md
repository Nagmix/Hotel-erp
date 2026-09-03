# 00 — نظرة عامة (Overview) — وحدة Care (Fortune Care v6)

> **وحدة خدمة الضيوف وإدارة المهام (Guest Service Optimization)**: تسجيل شكاوى/طلبات/حوادث الضيوف → تخصيصها لموظفي الورديات عبر **م محرك SMS ثنائي الاتجاه فريد** → تصعيد تسلسلي آلي عبر التسلسل الهرمي → ملاحظات الضيوف → إنتاجية الطاقم بـ 20 تقريراً تحليلياً. المقروء عميقاً كاملاً (الجلسة 9): **SETUP (34 ص/6 أقسام) + OPERATIONS (80 ص/6 وظائف) + REPORTS & LOOKUPS (73 ص/20 تقريراً) = 187 ص كاملة**.

---

## 1. حدود الوحدة

| البند | الوصف الموثق |
|---|---|
| الاسم النظامي | Fortune Care v6 — "Setup under Fortune Care v6 is used to map Users from PMS, assign groups, and define Access Rights to the Users and Groups, define Organisational Structure, tasks/complaints and Multi Tasks to the departments" (SET ص4) |
| الوظيفة الجوهرية | **أربع وظائف طبقية**: (1) Setup — ربط مستخدمي PMS وتعيين مجموعات (Agent/Supervisor) + الصلاحيات + الهيكل التنظيمي (أقسام→تصنيفات→موظفون→تسلسل تصعيد) + تعريف المهام/الشكاوى + المهام المتعددة + تقييد التقارير؛ (2) Operations — الروستر الشهري (سحب وإفلات!) + دخول/خروج الطاقم + **Manual Entry (محرك الشكاوى بـ SMS)** + Group SMS + Agent Console + Supervisor Lookup (إغلاق/نقل/تمديد/تخصيص)؛ (3) Reports & Lookups — 20 تقريراً تحليلياً بإمكانية Drilldown ورسوم بيانية؛ (4) Lost and Found — دورة مفقودات كاملة بعرض بيانات PMS |
| المركز المعماري | **الوحدة الأكثر اعتماداً على PMS في المشروع**: المستخدمون والأقسام والتصنيفات والورديات والمواقع وبيانات الغرف/الضيوف وحتى Lost & Found — كلها تُسترجع من PMS (الواجهة الأمامية لـ FO) — Care لا يملك أي ماجستير بيانات خاص به إلا الموظفين التشغيليين والمهام |
| نمط التشغيل | دورة يومية: Roster شهري مسبق → Staff Login للوردية (بموبايل يستلم المهام) → رفع شكوى (Room/Unoccupied/Other Area) → **زر Thank You يبدأ المؤقت** → SMS آلي → رد الموظف `1 S` (بدء) → `1 C` (إغلاق) → Awaiting Feedback → تسجيل التقييم (Satisfied/Not/Not Served/Guest Unavailable) → تصعيد تلقائي عند تجاوز الأوقات عبر سلسلة Reporting |
| النطاق | دورة حياة مهمة كاملة (Raise→Assign→Start→Close→Feedback/Cancel/Stop) · تصعيد 4 مستويات بأوقات قابلة للتهيئة · روسترات شهرية بورديات وأدوار ومواقع (طوابق) · دخول/خروج بموبايل/بيجر مع استرداد العهدة · Group SMS للبث (VIP!) · Lost & Found (ضياع→عثور→إرجاع بموظف مسؤول) · تحليلات إنتاجية كاملة |
| خارج النطاق | فوترة الضيوف (لا يوجد ترحيل لفوليو الضيف موثق — راجع 11/17) · الرواتب/الحضور لـ HR (الروستر خاص بـ Care ولا يغذي HRP Attendance — فجوة GAP-CA-D02) · صيانة الأصول (وحدة MNT منفصلة تستخدم نفس مفاهيم Maintenance في PMS) |

> ⚠️ **الحسم الحاسم لـ UNK-010 (الجسر الخارجي):** دليل SET ص5 و11 و13 ينص حرفياً: "You cannot create new Users; you can only map the Users **that are created in PMS**" / "All the Departments that are available **from PMS database** will be displayed" / "All the Designations that are available **from PMS database** will be displayed" — أي أن **Care لا يقرأ HRP Personnel Master إطلاقاً**، بل ينشئ موظفيه التشغيليين محلياً (اسم/عنوان/جهات اتصال/صورة) داخل الهيكل التنظيمي الخاص به. **UNK-010 = RESOLVED كاملاً**: مخزنان منفصلان للموظفين (HRP للرواتب مقابل Care للخدمة) يشتركان فقط في أبعاد القسم/التصنيف من PMS — قرار تكامل موثق في 12-integrations §1.2 و16-erpnext-mapping (F-CA-2).

## 2. جرد الوظائف الموثقة (6 + 6 + 20 ≈ 32 وظيفة/تقريراً + فرعيات)

| الدليل | الوظائف | العدد | المصدر |
|---|---|---|---|
| **CARE-SET** (Setup) | User Creation (ربط مستخدمي PMS!) · Define Rights (Group/User) · Organizational Structure (Department→Designation→Employee→Reporting To + Delete/Retrieve/Edit!) · Task and Complaints (تصنيف رئيسي/فرعي + وقت + أولوية + تصعيد) · Multi Task Definition (تجميع مهام عبر الأقسام!) · Restrict Reports (Spool/Export/Excel/OpenCalc/Direct) | 6 (17 خطوة فرعية) | TOC SET ص2 |
| **CARE-OPR** (Operations) | Monthly Roster (Roster/Shifts/Weekly Offs/Floors — سحب وإفلات) · Staff Log-in and Log-out (Login بأنواع 3 + Logout باسترداد عهدة) · Manual Entry Program (Raising + Feedback Cancel + Cancel/Stop + Work Start + Group SMS + Lost and Found + Color Legends + Zoom) · Group SMS (مستقل) · Agent Console (+Break) · Supervisor Lookup (Close/Transfer/Extend Est. Time/Assign/Unassigned + Clear Pending SMS) | 6 (24 خطوة/نافذة فرعية) | TOC OPR ص2 |
| **CARE-REP** (Reports & Lookups) | Call Attended List (+IVR!) · Task by Runner/Technician · Response Time Analysis · Work Start Statistics · Staff Productivity · Tasks Statistics (Drilldown!) · Tasks Statistics by Depart · Top Tasks Statistics · Repeated Issues List · Incidents by Floor List · SMS Sent List · Task Category Report · Guest Feedback Statistics · Extended/Trans. Incident · Escalation Report · Feedback List · Shift List · Cancelled/Stopped Task · Staff Log-in & Log-out List · Task List (بأكواد IVR) | 20 | TOC REP ص2 |

## 3. المفاهيم الجوهرية الموثقة

| المفهوم | الدلالة | المصدر |
|---|---|---|
| **محرك SMS ثنائي الاتجاه** | التخصيص آلي للموظف المسجل دخوله: `<1> Complaint #: 1 Room #: OR0707 Task: ... Spe. Ins: ... Est. Time: 10 mins Priority: High Esc Level: 0` والرد **`1 S`** للبدء و**`1 C`** للإغلاق — مع فروع خطأ موثقة نصياً (ALREADY STARTED / NOT ASSIGNED TO YOU / NOT YET STARTED / ALREADY CLOSED) ورسالة إغلاق المشرف `COMPLAINT #1 CLOSED. CLOSED BY: JOHN REASON: ISSUE RESOLVED` — **آلة حالة كاملة عبر الهاتف المحمول** | OPR ص38-43 |
| **زر Thank You = بداية المؤقت** | "The Task Assigned Estimated/Escalation time starts **once you click Thank You**" — لحظة الالتزام الزمني منفصلة عن لحظة الحفظ | OPR ص36 |
| **التصعيد التسلسلي** | "If any complaints are not addressed or not closed by the estimated time, the escalations will flow in the reporting hierarchy" — سلسلة مثال: Room boy → HK Supervisor → HK Manager → FO Manager → GM → MD، مع **timeout بالدقائق لكل مستوى** في تعريف المهمة (حتى 4 مستويات ملونة) | SET ص18 + ص26 + OPR ص30 |
| **الورديات والطوابق من Maintenance في PMS** | "The Shifts and Locations parameters are **mapped from the Maintenance module in PMS**" + خيارات Raising: Room/Unoccupied Room/Other Area — "The Locations parameter is retrieved from the Maintenance module in PMS" | OPR ص5 + ص33 |
| **موبايل الموظف = قناة المهام** | "THE EMPLOYEE'S MOBILE NUMBER... IS THE NUMBER WHERE HE WILL RECEIVE THE MESSAGES" (SET ص16) + عند Login: "On this mobile number the employee will be receiving the tasks" و"**The same mobile number will be reassigned to other personnel of the department in the next shift**" (OPR ص19/25) — نظام عهدة موبايل لكل وردية | SET ص16 + OPR ص19 |
| **الموظف غير المسجل = Unassigned** | "a task will show as unassigned if **no employee has logged in for the shift** under the respective department" — البدء اليدوي (Work Start) ثم التخصيص لاحقاً right-click → Assign | OPR ص77-80 |
| **ملغاة ≠ موقوفة** | "**Cancelled tasks are those tasks that have not been started** and **Stopped tasks are those tasks that have already been started and cancelled**" — تمييز دقيق موثق | REP ص64 |
| **صور الحالة الملونة** | أولويات Low/Normal/High + مستويات تصعيد 1-4 بألوان + **Pink في Guest Name = غرفة غير مشغولة** + **Magenta في Room# = منطقة أخرى** | OPR ص30 |
| **IVR** | تقرير Call Attended يعرض مكالمات "agent/**IVR** or any other User" + Task List يعرض **IVR Code** لكل مهمة — يوجد رمز هاتف تفاعلي لرفع الشكاوى آلياً (صندوق أسود غير موثق التفاصيل — GAP-CA-D04) | REP ص5 + ص69 |
| **الحذف الناعم للموظفين** | "The employee details will be deleted, and **added to the Deleted List**" ثم الاسترجاع "Right-click Designations → Employee → From Help → **Deleted List**" + قيد: "You **cannot edit the employee name**" | SET ص20-24 |

## 4. التفاعلات مع الوحدات (موثقة نصاً)

- **Care ← PMS/FO (سبع قنوات موثقة!):** (1) المستخدمون "created in PMS"؛ (2) المجموعات والمستخدمون في Define Rights "retrieved from PMS"؛ (3) الأقسام "from PMS database"؛ (4) التصنيفات "from PMS database"؛ (5) الورديات والمواقع "mapped from the Maintenance module in PMS"؛ (6) الغرف والضيوف — اختيار Room# يعرض بيانات الضيف فوراً، وسجل المهمة يحمل Check-in/Check-out dates؛ (7) Lost and Found — "You can view the **PMS Lost and Found details** from this option".
- **Care × HRP (حسم UNK-010):** **لا جسر مباشر** — موظفو Care سجلات مستقلة خفيفة (اسم/عنوان/اتصال/صورة) بينما Personnel Master في HRP كيان الرواتب؛ التقاطع فقط في أبعاد القسم/التصنيف المسترجعة من PMS. (راجع 12-integrations §1.2)
- **Care → الضيوف (ملاحظات):** تقييم رباعي Satisfied/Not Satisfied/Not Served/Guest Unavailable + نص ملاحظة — يغذي Guest Feedback Statistics.
- **Care ↔ بوابة SMS خارجية:** إرسال/استقبال مع حالات Queued/Delivered وClear Pending SMS في Supervisor Lookup — مزوّد غير موثق (GAP-CA-D05).
- **Care × IVR:** أكواد مهام قابلة للطلب الهاتفي (التوثيق يقتصر على ذكر IVR — انظر GAP-CA-D04).
- **الشحنة المالية الوحيدة:** "In the Approximate Cost, if field, enter value of charges incurred if any" عند إغلاق المهمة + Charges applicable Y/N في تعريف المهمة — **بلا ترحيل موثق لأي فوليو/قيد** (راجع 11-accounting-impact).

## 5. أهم الاكتشافات المعمارية (الجلسة 9)

1. **UNk-010 محسوم نهائياً:** Care وحدة تابعة معماريّاً لـ PMS (FO) وليست جارة لـ HRP — نمط "الوحدة الساتلية PMS-centric" الجديد في المشروع؛ HRMS في إعادة البناء يحتاج قرار F-CA-2 (موظف الخدمة = Employee في Frappe مع حقول اتصال، أو doctype خفيف مستقل).
2. **محرك SMS آلة-حالة:** إشعارات + أوامر نصية (`1 S`/`1 C`) + فروع خطأ + إشعار إغلاق المشرف — لا نظير لها في وحدات المشروع الأخرى → قرار F-CA-3 (Frappe: Notification + webhook SMS gateway مع خادم معالجة ردود).
3. **التقسيم الدقيق للحالة:** Queued → Delivered → Work in Progress → Awaiting Feedback → Closed + Cancelled/Stopped + Unassigned + Escalated 0-4 — أغنى آلة حالة تشغيلية في المشروع (14 حالة!).
4. **الروستر ≠ الحضور:** روستر Care (ورديات/طوابق/أيام راحة) لا يُرحّل إلى Attendance في HRP إطلاقاً (GAP-CA-D02) — فرصة تكامل ضائعة في المنتج الأصلي، وقرار تصميم مطلوب في إعادة البناء (F-CA-6).
5. **التكلفة المسجلة غير المفوترة:** Approximate Cost عند الإغلاق دون أي مسار فوترة موثق (GAP-CA-D01) — المرشح الطبيعي: ترحيل لفوليو الضيف عبر FO.
6. **إصدارية غير متسقة:** أغلفة "VER 10 AUGUST" مقابل REVISION HISTORY "Version 1, 9 August 2013" (Sadanand/Noel) — نفس نمط فجوات الإصدار الموثق في وحدات أخرى (GAP-CA-D06).
