# 02 — الإعدادات والتهيئة (Configuration) — وحدة Care

> كل عناصر التهيئة الموثقة: ربط المستخدمين، الصلاحيات (مستويان!)، قيود التقارير، بنية التصعيد، وإعدادات التشغيل الضمنية. **Care وحدة "Zero-config" نسبياً**: لا INI keys ولا Property Setup خاص بها — كل التهيئة أبعاد PMS + تعريفات محلية.

---

## 1. قائمة عناصر الإعداد الموثقة

| # | العنصر | النوع | الدليل |
|---|---|---|---|
| 1 | User Creation (ربط مستخدم PMS → Group + BelongsTo) | ربط هوية | SET §1 ص5-6 |
| 2 | Define Rights (Group/User × Sub Modules × Menu Options + Add/Modify/Delete) | صلاحيات قوائم | SET §2 ص7-9 |
| 3 | Organizational Structure (الشجرة + Reporting) | هيكل + تصعيد | SET §3 ص10-24 |
| 4 | Task and Complaints (تعريف المهام) | ماجستير تشغيلي | SET §4 ص25-27 |
| 5 | Multi Task Definition | تجميع مهام | SET §5 ص28-31 |
| 6 | Restrict Reports (Spool/Export/Excel/OpenCalc/Direct لكل مستخدم) | تقييد تقارير | SET §6 ص32-34 |

## 2. ربط المستخدمين (User Creation) — SET ص5-6

- **قيد معماري حاكم**: "You cannot create new Users; you can only map the Users that are created in PMS. If you want to create a new User, login to PMS, create the new User and map that User in Fortune Care."
- حقول الشاشة: User (F1/double-click من قاعدة PMS) + Group dropdown + **Belongs To (Supervisor Group → Department)** + Save.
- **التعديل**: إعادة اختيار المستخدم وتغيير Group/Department ثم Save.
- مجموعتان فقط:
  - **Agent** — "Users under this group can **only log the Complaints**".
  - **Supervisor** — "can log the Complaints, **Extend, Transfer and Close** the Complaint (in Supervisor Lookup program.)" — أي أن الصلاحية الوظيفية الجوهرية تُحمل عند التعيين لا عند الشاشة.

## 3. الصلاحيات (Define Rights) — SET ص7-9

- **نمط SYS نفسه** (متسق مع نظام 6i الموثق في system-setup/07-permissions.md): Group أو User → Sub Modules وMenu Options تحت Main Module "CARE" → Save.
- "System displays **only those Menu options for which the User has rights in CARE**" — إخفاء القوائم غير الممنوحة.
- "Within an option, **Add/Modify/Delete actions can also be controlled**" — تحكم ثلاثي العمليات داخل الخيار الواحد.
- أزرار: **Select** (تحديد الكل) / **Deselect** (إلغاء الكل) / Continue / Save.
- مصدر المجموعات والمستخدمين: "In Define Rights the **Groups & Users will be retrieved from PMS**".

## 4. تقييد التقارير (Restrict Reports) — SET ص32-34

| العمود | السلوك |
|---|---|
| Module | اسم الوحدة |
| Reports Name | كل تقارير الوحدة |
| **Spool** | Yes/No بـ double-click **أو Space أو Enter** — منح/منع التجميع |
| **Export** | Yes/No بنفس الآلية — منح/منع التصدير |
| **Excel/Direct/Open Calc** | اختيار صيغة الطباعة بالنقر على الخلية |
| شرط خارجي | "To select Excel or Open Calc, you should have **installed the third party MS Excel or Open Office** software applications" |
| Direct | "To print directly on to a printer, you should select Direct" |

> هذا هو النمط الثالث للتحكم بتقارير الوحدات بعد SYS-SSP (القيود العامة) وقيود التقارير في الوحدات نفسها — راجع system-setup/07-permissions.md §الأنماط.

## 5. بنية التصعيد القابلة للتهيئة

تُشتق من ثلاث جهات:
1. **Reporting Link** لكل Designation (SET §3) — ترتيب القفز.
2. **Escalation timeout لكل مستوى** في تعريف كل Task (SET §4) — "specify the time in minutes in which the next levels of escalations should be ESCALATED".
3. **Estimated Time for Response** لكل Sub Category (SET §4) — المهلة قبل أول تصعيد.
- التمثيل المرئي: **مستويات 1-4 بألوان مميزة** (OPR ص30) + `Esc Level: 0..4` في نص SMS (OPR ص38).

## 6. إعدادات التشغيل الضمنية (Implicit Config)

| الإعداد | القيمة/السلوك | المصدر |
|---|---|---|
| أقصى طول Special Instructions | **25 حرفاً رقمياً-حرفياً** | OPR ص36 |
| أنواع Login | Supervisor / Guest Relation Executive / Duty Manager | OPR ص19 |
| فئات التقييم | Satisfied / Not Satisfied / Not Served / Guest Unavailable | OPR ص47 |
| أنواع أماكن الشكوى | Room / Unoccupied Room / Other Area (من PMS Maintenance) | OPR ص33 |
| أولويات | High / Normal / Low | OPR ص26/30 |
| أنواع المهمة | Complaint / Request / Incident / Other | SET ص26 |
| أشكال التقارير | Summary / Details (+Chart) | REP عابر |
| أطر زمنية للتقارير | Date Range / Monthly / Yearly (+Month Wise/Day Wise في Tasks Statistics) | REP عابر |
| قيود الشبكة | Response Time Analysis: **Details غير متاحة مع Yearly** | REP ص14 |
| Task List | All Departments → **لا فلتر Main** | REP ص70 |

## 7. ملاحظات التهيئة العامة

- **لا مفاتيح INI موثقة في Care** (عكس FO/POS/BNQ/MGT/HRP) — أدلة Care لا تذكر أي مفتاح تهيئة. الاستنتاج: الوحدة الساتلية تأخذ سلوكها من PMS بالكامل تقريباً (GAP-CA-D03 يوثق غياب التوثيق الإداري).
- **لا Property Setup محلي** — اسم الخاصية يُعرض من PMS: "The Property name will be displayed on the left side of the screen" (SET ص10).
- الإصدار: أغلفة "VER 10 AUGUST" مقابل REVISION "Version 1, 9 August 2013" — راجع GAP-CA-D06.
- **Break** في Agent Console — خيار موثق بالاسم فقط (OPR ص67) دون تفصيل (GAP-CA-D07).
