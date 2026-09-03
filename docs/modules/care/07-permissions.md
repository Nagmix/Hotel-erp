# 07 — الصلاحيات والأدوار (Permissions) — وحدة Care

> نمط صلاحيات ثلاثي الطبقات فريد: (1) **مجموعة تشغيلية عالمية** (Agent/Supervisor) تحمل الصلاحيات الوظيفية عند التعيين، (2) **صلاحيات قوائم SYS-النمط** (Define Rights)، (3) **تقييد تقارير** (Spool/Export/Format) — كلها فوق هوية PMS.

---

## 1. طبقة المجموعة التشغيلية (من User Creation) — SET ص5

| المجموعة | الصلاحيات الموثقة نصاً |
|---|---|
| **Agent** | "can **only log the Complaints**" — رفع فقط |
| **Supervisor** | "can log the Complaints, **Extend, Transfer and Close** the Complaint (in **Supervisor Lookup** program.)" |

> **ملاحظة معمارية**: المجموعة تُحمل في ربط المستخدم (Belongs To → Supervisor Group → Department) وتحدد الوظائف الجوهرية، بينما Define Rights يحدد القوائم المرئية — فصل الوظيفة عن الوصول.

## 2. طبقة أنواع الدخول التشغيلي (Login Types) — OPR ص19

| النوع | السلوك |
|---|---|
| Supervisor | يسترجع وردية الموظف من الروستر + كل عمليات Supervisor Lookup (بعد صلاحية المجموعة) |
| Guest Relation Executive | "Anyone can login" — مستوى حاضر مجاني |
| Duty Manager | مثله |

- قيد: "Users created through Organizational Structure can login with Guest Relation Executive and Duty Manager" — أي أن أي موظف معرف في الهيكل يستطيع الدخول بمستوى GRE/DM (ليس فقط المشرفين!).
- **رؤية أقسام غير بديهية (BR-CA-18)**: "A Supervisor can view the tasks of the departments **by selecting** the Department... Normal login users can view the status **for all the departments**" (OPR ص68) — المشرف أضيق (قسمه) من المستخدم العادي (الكل)!

## 3. طبقة قوائم Define Rights — SET ص7-9

- **النمط SYS المتطابق**: Groups/Users (من PMS!) → Sub Modules → Menu Options تحت Main Module "CARE" → Save.
- التحكم الثلاثي داخل الخيار: **Add / Modify / Delete** — "Within an option, Add/Modify/Delete actions can also be controlled".
- الإخفاء التلقائي: "System displays **only those Menu options for which the User has rights** in CARE".
- أزرار Select/Deselect (كل/لا شيء).

## 4. طبقة تقييد التقارير (Restrict Reports) — SET ص32-34

| البُعد | القيم | الأثر |
|---|---|---|
| Spool | Yes/No | منح/منع تجميع التقرير |
| Export | Yes/No | منح/منع التصدير |
| Format | **Excel / Open Calc / Direct** | قناة الطباعة المسموحة |
| شرط Software | "you should have installed the third party **MS Excel or Open Office**" | اعتماد أدوات خارجية |

> **النمط الثالث للتحكم التقاريري في المشروع** بعد قيود SYS-SSP العامة وقيود التقارير داخل الوحدات (مثل HRP Payroll User Rights per-Category وBNQ=POS User Access) — راجع `system-setup/07-permissions.md`.

## 5. مصفوفة الأدوار × العمليات (الموثقة)

| العملية | Agent | Supervisor | GRE/DM | مستخدم عادي |
|---|---|---|---|---|
| رفع شكوى (Manual Entry) | ✓ | ✓ | ✓* | بحق Define Rights |
| Thank You (بدء المؤقت) | ✓ | ✓ | ✓* | بحق |
| Feedback Cancel (تسجيل تقييم) | ✓ (وكيل) | ✓ | ✓* | بحق |
| Cancel/Stop Task | ✓ (بطلب ضيف/مشرف) | ✓ | ✓* | بحق |
| Work Start يدوي | ✓ | ✓ | ✓* | بحق |
| Group SMS / Lost & Found | ✓ (من Agent Console أيضاً) | ✓ | ✓ | بحق |
| **Close task** | ✗ | ✓ (Lookup) | ✗ | ✗ |
| **Transfer task** | ✗ | ✓ (Lookup) | ✗ | ✗ |
| **Extend Est. Time** | ✗ | ✓ (Lookup) | ✗ | ✗ |
| Assign (Unassigned) | ✗ | ✓ (Lookup + WIP) | ✗ | ✗ |
| رؤية كل الأقسام | — | قسمه (dropdown) | — | **✓** (انعكاس BR-CA-18) |
| Clear Pending SMS | — | ✓ (Lookup) | — | — |

\* GRE/DM "Anyone can login" مع ملاحظة أن العمليات الكاملة تحتاج الصلاحية.

## 6. ملاحظات الأمان التحليلية

1. **لا مالكيات على مستوى الصفوف (record-level) موثقة**: أي وكيل يرى شبكة المهام ويستطيع Cancel/Feedback لأي مهمة (بحسب الأدلة) — الفرق الوحيد الموثق على مستوى الوظيفة. قرار إعادة البناء: إضافة ownership (F-CA-8).
2. **هوية خارجية واحدة**: كل دخول عبر مستخدمي PMS — لا مستخدمين محليين، مما يجعل PMS نقطة فشل وحيدة للتحكم.
3. **Employee (Org Structure) ليس مستخدماً بالضرورة**: الموظف المعرف قد لا يملك حساب دخول أصلاً (المستخدمون من PMS) — كيانان منفصلان تماماً (راجع UNK-038 في HRP — نفس المشكلة العابرة للوحدات).
4. **آثار Restrict Reports على المخرجات**: منع Spool/Export لا يمنع عرض الشاشة — قناة تسريب معلومات بصرية بلا تصدير (ملاحظة تحليلية، ليست موثقة).
