# أدوار المستخدمين الفندقيين (Hotel Roles)

> **المرحلة:** Phase 1 — الأدوار المكتشفة نصاً في الوثائق (ليست تخميناً). مصفوفة الصلاحيات التفصيلية تُبنى في Phase 8.

---

## الأدوار الموثقة نصاً

| الدور (EN) | الدور (AR) | ورد في | مهامه الموثقة |
|---|---|---|---|
| **Night Auditor** | مدقق الليل | FOM-DEP ص6 | ينفذ Day End Process، يطلب من الكاشير تسوية الفواتير المعلقة، يتابع Night Report (Excess/Short=0) |
| **Cashier (Outlet)** | كاشير المنفذ | BNQ-BIL ص2، FOM-DEP | يفتح Shift قبل أي معاملة، يسوي الفواتير المعلقة، يغلق الوردية/المنفذ |
| **Cashier (FO)** | كاشير الاستقبال | FOM-CAS | Postings، Deposits، Settlements، Checkout |
| **Front Office Executive / Receptionist** | موظف استقبال | FOM-RES/REG | الحجوزات، الوصول، معلومات النزلاء ( Likes/Dislikes "all Front Office executives should be aware") |
| **Housekeeping Staff** | فريق الإشراف الفندقي | FOM-HSK, FOM-SET §39 | تنظيف الغرف وتحديث الحالة، جداول التنظيف |
| **Laundry Staff** | فريق الغسيل | FOM-HSK | قيود الغسيل وطباعة فواتيره |
| **Concierge** | الكونسيرج | FOM-CRG | الأمتعة، الطرود، التذاكر، صف السيارات |
| **Guest (indirect)** | النزيل (غير مستخدم مباشر) | — | يستفيد من SMS وTrace |
| **Finance Department** | القسم المالي | FOM-DEP ص11 (Night Audit Adjustments "useful for the finance department"), FAS | التعديلات المالية، القيود، التسويات البنكية |
| **Sales Executive** | مندوب مبيعات | FOM-SET §22, SLM-PRF/SLT | عقود الشركات، مكالمات المبيعات، التنبؤ |
| **Collection Executive** | مندوب تحصيل | FOM-SET §23, ACR-CRT | متابعة المدينين (Debtors Follow-Up) |
| **HOD (Head of Department)** | رئيس قسم | HRP-SET (HOD Definition), HRP-RQP (HOD Status) | اعتمادات التوظيف، هيكل التقارير |
| **Chef / Chef Engineer (Pre-Costing)** | الشيف (التكلفة التقديرية) | BNQ-BIL §12 | Pre-Costing لمتطلبات المناسبة |
| **Store Keeper** | أمين مخزن | MGT | الاستلام/الإصدار/التحويلات |
| **Maintenance Technician / Runner** | فني الصيانة | Care-REP (Task by Runner/Technician), MNT | تنفيذ المهام/أوامر العمل |
| **Care Agent (Console)** | موظف خدمة الضيوف | Care-Ops (Agent Console) | استقبال الشكاوى وتوزيع المهام |
| **Care Supervisor** | مشرف الخدمة | Care-Ops (Supervisor Lookup) | الإشراف وإغلاق المهام |
| **Membership Officer** | موظف العضويات | MEM-MPF/MMN/MTR | الطلبات، الفحص، الإيصالات |
| **System Administrator** | مدير النظام | SYS-SSP | المستخدمون، الصلاحيات، الإعدادات العامة |
| **Night Auditor Boss/Manager** | مدير العمليات | FOM-SET (Manager Reports), FOM-REP | تقارير المديرين |

---

## ملاحظات

- **الفئات الثلاث الكبرى (لأغراض UX لاحقاً):** تشغيل لحظي (Reception/Cashier/Waiter — شاشات سريعة كثيفة لوحة مفاتيح/لمس)، إشراف يومي (Night Auditor/Supervisor — شاشات تحقق وتقارير)، إدارة وإعداد (Admin/Finance — نماذج كاملة).
- الأدوار تظهر أيضاً في بنية الصلاحيات: FO User Authorization، POS User Access + Restrict Outlet Access، AR User Access، Transaction Type Rights، Payroll User Rights، Care Define Rights — **نموذج صلاحيات لكل شاشة/عملية/نوع مستند** [يُفصَّل في Phase 8].
- غياب موثق: لا يوجد "Revenue Manager" كدور مستقل؛ مهامه موزعة (Hurdle Rate في REG، Rev. Management Tool في LUK).
