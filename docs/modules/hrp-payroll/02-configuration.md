# 02 — التهيئة والإعدادات (Configuration) — وحدة HRP

> خريطة التهيئة الكاملة: مفتاح INI موثق واحد جديد (220) + بنية الإعدادات الإجرائية + الكتل المرجعية التي تعمل كإعدادات فعلية (Slab Tables + Statutory Definitions + Category defaults).

---

## 1. مفاتيح INI / Switches الموثقة في HRP

| المفتاح | القيمة الموثقة | الوظيفة | المصدر |
|---|---|---|---|
| **INI 220** | **0 = مفعّل** (منطق معكوس!) | تفعيل Leave Group Parameter: "To activate this parameter the INI Switch No. 220 should be set to **0**" | SET §15 ص31 |

> 📌 **عائلة INI المعكوسة تتوسع:** 56 (AR — 0=ممكن) · 74 (AR) · **220 (HRP)** — الجدول التراكمي في `docs/analysis/` يُحدَّث إلى **29+ مفتاحاً** (راجع §5).

لا تُوثّق HRP أي Module Attributes — الوحدة تعتمد تهيئتها على كياناتها المرجعية (عائلة "التهيئة كبيانات رئيسية"):

## 2. التهيئة-كبيانات (Configuration-as-Master-Data) — نمط HRP الغالب

| الكيان | يعمل كإعداد لـ | القاعدة الحاكمة |
|---|---|---|
| **Category Code** | إيقاع الدورة + التقريب + سقف الخصم | Cal Method + Round type/Amount + **Take Home %** |
| **Starting Period** | نافذة المعالجة لكل فئة | التواريخ المحسوبة + "All the reports will be based on the period specified here only" |
| **Property Attendance Matrix** | دلالة كل كود حضور | 5 أعلام (Leave/Paid/Hourly/Wrkday) — BR-HR-04 |
| **ED Calculation + Tables** | معادلات وشرائح كل كود | 4 Slab types + 4 Calculate From + تراكم |
| **Statutory Deduction Defn.** | نسب PF/ESI/PT/LWF | "as per government norms" + Print Program IDs |
| **Denomination** | كسر النقد للصرف | قيم تنازلية Notes/Coins |
| **Payroll User Rights** | صلاحيات فئوية | per User × per Category |

## 3. الإعدادات الإجرائية الهندية (Statutory) — البنية الكاملة

| البرنامج | مكوّنات التعريف | أثر محاسبي |
|---|---|---|
| **PF** | PF code + FPF (Family Pension) + VPF (Voluntary) + Minimum pensionable gross + Pension % + Round off + Calculating % + **Admin charges + EDLI charges + EDLI admin** | خصم موظف + مساهمة صاحب عمل (نصف/نصف موثقة في ED Code §5) |
| **ESI** | ESI code + Employer share % + Round off + ESI % | أهلية عتبة 6500 (Eligibility slab) |
| **PT** | code + Print Program ID | شرائح Normal Slab |
| **LWF** | code + Employer share + Print Program ID | مساهمة سنوية |

> ⚠️ **قرار F-HR-3:** هذه البنية هندية-مركزية ("ESI slabs are set as per the government norms" + PYINDSP "only for Indian clients") — في ERPNext العربي-أولاً تُبنى كـ **Statutory Rule Set قابل للتهيئة جغرافياً** (Country field على المستوى) لا كمنطق مدمج.

## 4. إعدادات الطباعة والتقارير

| الإعداد | الوصف الموثق |
|---|---|
| **Print sequence** (ED Code) | ترتيب مكونات Payslip — قاعدة تبادل earning↔deduction ممنوعة بين deduction types |
| **User Defined Report Definition** (SET §20) | Report # (auto) + Name + **Paper: 80/132 columns** + Left/Center/Right headers + Select Column (حقول HR) + **Formula builder (Column Name + type + Check Formula!)** + Column Detail (Width/Alignment/Total=True) + Break & Sort (+Group Total) |
| **User Defined Print Forms** (SET §21) | مشروع طباعة كامل: New/Open/Delete/Browse/Save/Print/Preview + **Page layout: "The sum of Header rows, Footer rows, body rows must be equal to the total length of the stationery (6 rows = 1 Inch)"** + Match Samples + Tool Box + Scales/Grid/Lock controls (F4 = Property) + **نوع البرنامج: Bill print / KOT Print / NC Bill Print / Invoice Print** + Printer Type (Normal/Slip) + Logo insertion |
| Payslip Printing (REP §11) | Paymode selection + Selection order (Dept/Grade/CC/Emp#) + **user definition option من dropdown** |

## 5. الجدول التراكمي — مستجدات HRP

| النوع | المفتاح | الوحدة المكتشِفة |
|---|---|---|
| INI | 220 (Leave Group، 0=مفعل) | HRP (هذه الجلسة) |
| INI | 56 · 74 | AR (سابقاً) |

> المجموع التراكمي الموثق عبر المشروع (INI + Module Attributes + Inventory keys): **29+** — المرجع الكامل: `docs/analysis/00-discovery/analysis-status.md` والجداول في وثائق SYS/MGT.

## 6. إعدادات أمنية

| الإعداد | الوصف |
|---|---|
| **Payroll User Rights** (SET §23) | "supervisor-user can grant access rights to different User ids to **different employee groups**" — نطاق البيانات (Category) لا الشاشات فقط — انظر 07-permissions |
| وظيفة Modify المقيدة | Job Requirements: "The user can modify only the **authentication status and Remarks**" — تجميد حقول التشغيل |
| Payroll Audit | تتبع Modified/Deleted بقيم old/new — انظر 08 §19 |
