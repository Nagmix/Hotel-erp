# 16 — Seed Mapping إلى ERPNext/Frappe/HRMS — وحدة System Setup

> الفصل الأكثر كثافة قرارات في المشروع حتى الآن: SYS يحدد **هيكل الموقع/الشركة/العملة/الضرائب/الصلاحيات** — أي أساس Frappe نفسه. التصنيف: **A = مطابقة مباشرة · B = تخصيص حقل · C = DocType مخصص · D = بنية فرابي بديلة · E = هيكل مخصص · F = قرار معماري مؤجل**.

---

## 1. جدول المطابقة الأساسي

| # | كيان FN6i | نظير ERPNext/Frappe | التصنيف | ملاحظات/القرار |
|---|---|---|---|---|
| 1 | User | **User** | A | direct + auth منفصلة |
| 2 | UserGroup | **Role** | A | المجموعات = أدوار |
| 3 | Supervisor=Yes | Role **System Manager** | B | + إدارة الفندق |
| 4 | UserAccess (module/sub/item × A/M/D) | Role Permissions + DocPerms | **C/F-SYS-9** | بند قائمة → DocType: قاعدة تحويل (كل شاشة FN ≈ DocType) |
| 5 | UserMenuAccess | **Workspace + Dashboard** | D | أقوى من الأصل — تخصيص per-user قياسي |
| 6 | ReportAccess (spool/export/format) | Report permission + has_permission | C | hook مخصص (format يعاد تعريفه PDF/XLSX) |
| 7 | Password policy | Frappe password policy | A | — |
| 8 | Property Code | **Company** (Frappe) | **F-SYS-11** ⭐ | قررنا: Company لكل Property — **يحسم UNK-004**: النموذج البياني FN متعدد الخصائص يساوي شركات فرابي متعددة بموقع واحد؛ التبديل غير الموثق أصلاً = Company switch + User Permissions |
| 9 | Property Round Off | custom field + `custom_round_off_*` | C | على Company/Property Settings |
| 10 | Department | **Department** | A | + custom: `module` (General/Banquet filter) |
| 11 | Cost Center | **Cost Center** | A | accounting_dimension مفعلة |
| 12 | Designation | **Designation** (HRMS) | B | + `guest_type` enum |
| 13 | UOM | **UOM** | A | — |
| 14 | ReasonCode | **Reason** custom? — C | C | `PMS Reason Code` (module enum ×9) — لا نظير مباشر (Cancellation Reason جزئي) |
| 15 | Currency (10 حقول) | **Currency** | **B/C** | Frappe: code/name/symbol/precision — المفقوب: type (TravellersCheque!) · Local/Foreign · standard_rate · Million/Lakh (يُستبدل) · division_method · text_before/after |
| 16 | ExchangeRate (≤4 زمنية) | **Exchange Rate** (Frappe) | B | valid_from موجود؛ **قيد 4 إدخالات يُسقط** (بلا مبرر وظيفي — F-SYS-12) |
| 17 | TaxCode | **Sales Taxes and Charges Template** / Item Tax | C | بنية فرابي أنعم — code كـ tax rate entry |
| 18 | TaxSlab | **C — PMS Tax Slab** (rows: from/to/factor/cumulative) | C | لا نظير قياسي للشرائح! حساب مخصص في tax calc hook |
| 19 | TaxStructure (On Value/Discounted/**Tax**) | Sales Taxes/Charges مع **included** + ترتيب | **C/F-SYS-7** ⭐ | On Tax يُحاكى بترتيب البنود + custom calc — الشرائح المزدوجة (cumulative/non) تتطلب محرك حساب مخصص `pms_tax_engine.py` |
| 20 | GuestComment (1-25) | `PMS Guest Comment` seeded | C | seed ثابت 1-25 + ترجمة |
| 21 | CreditCardType + FloorLimit | `PMS Credit Card Type` | C | POS payment types لا تحمل floor limit |
| 22 | PrintBillMessage | `PMS Bill Message` | C | — |
| 23 | Religion/Occupation | `PMS Demographic` pair | C | HRMS لا يشملها |
| 24 | ProgramID + Printer Ports | **Print Format** + Print Settings | D | USB-PDF = Print to PDF القياسي — المنافذ الفيزيائية تنتهي (شبكة) |
| 25 | FO Defaults (14) | `PMS Defaults` (module defaults) | C | — |
| 26 | Module Attributes | **`Hotel Feature Toggle`** | **F-SYS-1** | جدول موحد module/key/value/desc/risk-level + audit |
| 27 | INI Files | نفس الجدول أعلاه + import/export JSON | **F-SYS-2** | يُستأصل ملف النص |
| 28 | Changing Caption | **Translation** (ar/en) | **F-SYS-3** | i18n قياسي |
| 29 | Extract DB Tables | Bench Backup + Data Export | D | وظيفة إدارية قياسية |
| 30 | User Management | User list + reset link | B | **منع العرض المكشوف — F-SYS-6** |
| 31 | Parameter List | System Settings report + Feature Toggle report | C | — |
| 32 | Group Nationality | [UNCERTAIN] — يؤجل | F | بعد اكتشاف وظيفته |

## 2. القرارات المعمارية المسجلة (F-SYS-1..12)

| # | القرار | المبرر |
|---|---|---|
| F-SYS-1 | `Hotel Feature Toggle` DocType موحد لكل Module Attributes (module, key, value, description, risk_level, requires_approval) | يعكس دلالة Yes/No الأصلية + يضيف الحوكمة الغائبة |
| F-SYS-2 | INI → سجلات Feature Toggle + JSON import/export (بلا ملفات نصية) | إزالة نقطة الفساد E-SYS-18 |
| F-SYS-3 | Captions → Translation DocType قياسي (ar أولاً + en) — إسقاط "عرض الاسمين" | Arabic-first يجعلها أساسية لا اختيارية |
| F-SYS-4 | `PMS Defaults` (module, field, value, company) قابل للتجاوز شاشياً | مثلث Defaults الأصلي |
| F-SYS-5 | Extract → Backup/Restore + JSON export | الاستبدال التام |
| F-SYS-6 | كلمات المرور: hash + reset link — **لا عرض نصي أبداً** | أمن (الأصل يعرضها!) |
| F-SYS-7 | محرك ضريبي مخصص `pms_tax_engine` (cumulative/non + slabs + On-Tax chaining) فوق Sales Invoice/POS Invoice hooks | لا تغطية قياسية للثلاثية |
| F-SYS-8 | صلاحيات الوحدات الخاصة = DocTypes ACL مخصصة (POS outlet blocklist / AR voucher types / FO authorization) | الأبعاد غير القياسية |
| F-SYS-9 | قاعدة تحويل: كل شاشة FN6i ≈ DocType واحد؛ صلاحيات A/M/D = create/write/delete | ملاءمة DocPerms |
| F-SYS-10 | مسار استرداد مشرف مضمون (Frappe Administrator خارج نطاق الفندق) | E-SYS-01/02 |
| **F-SYS-11** | **Property = Company** (multi-property = شركات بموقع واحد) — **يحسم UNK-004** | أقرب نظير معماري؛ سلوك التبديل الأصلي غير موثق أصلاً |
| F-SYS-12 | إسقاط قيد "≤4 أسعار صرف" (بلا مبرر) مع الإبقاء على الإصدارية الزمنية | تحديث سياسة عملة واقعي |

## 3. Seed Data المطلوب عند التركيب (Bootstrap)

| الترتيب | العنصر | المحتوى |
|---|---|---|
| 1 | Company (Property) + عملة محلية + Exchange | WF-SYS-10 |
| 2 | Feature Toggles defaults | **الكل No** (مثل الأصل!) |
| 3 | Departments seed (Finance/HR/S&M/FO — أمثلة الدليل ص48) | 4 |
| 4 | Guest Comments 1-25 | مع الترجمة |
| 5 | Program IDs → Print Formats للنماذج الـ 20 الموثقة | FM001BL... |
| 6 | UOM قياسية (POS/MM) | Kg/L/PCS... |
| 7 | Roles قياسية الفندق | من domain/hotel-roles (20 دوراً موثقاً) |
| 8 | Reason Codes أولية لكل 9 وحدات | إلزامية التبرير |

## 4. صلاحيات فرابي مقابل النموذج الأصلي (جدول الفروق)

| بعد الصلاحية | FN6i | Frappe | الجسر |
|---|---|---|---|
| حامل | Group/User | Role/User | مباشر |
| نطاق | Module→Sub→MenuItem | DocType/Module | قاعدة F-SYS-9 |
| عمليات | Add/Modify/Delete | create/write/delete/cancel/amend | +submit/cancel لحراسة إقفال FO/AR |
| تقارير | Spool/Export/Format | has_permission | C-hook |
| مشرف | Supervisor bool | System Manager | — |
| تفويض مزدوج | FO Authorization | **Workflow + approver** | D — Frappe Workflow أساس جاهز |
| حجب منفذ | Restrict Outlet Access | User Permissions (Outlet dimension) | B — ممتاز! |

> User Permissions بفرابي (حسب Company/Outlet) يغطي **بأناقة** حجب المنافذ multi-property — أقوى من blocklist الأصلي.

## 5. تقييم النضج للتنفيذ

- **جاهز فوراً:** Users/Roles/Departments/CC/UOM/Currency(أساسي)/Designation/Workspaces/Print Formats/Translations — **معظم SYS!**
- **يحتاج عملاً مخصصاً:** محرك الضرائب (F-SYS-7) · صلاحيات خاصة (F-SYS-8) · Feature Toggles (F-SYS-1/2).
- **مؤجل:** Group Nationality (بعد MGT/BNQ قراءة) · طباعة المنافذ الفيزيائية (نُذر انتهاء المفهوم).
