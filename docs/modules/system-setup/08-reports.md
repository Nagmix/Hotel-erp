# 08 — التقارير — وحدة System Setup

> SYS وحدة إعداد: تقاريرها الثلاثة إدارية، ومعظم مخرجاتها التشغيلية تقارير المرجعيات (List). **لا يوجد ملف SYS-REP منفصل في الحزمة** — عكس كل الوحدات الكبرى.

---

## 1. التقارير الموثقة (3)

| ID | التقرير | المدخلات | المخرجات | المصدر |
|---|---|---|---|---|
| R-SYS-01 | **List Users** | As on = **server date** (آلي) | "a list of all active users" — بيانات مرآة لـ Create User ("reflected from the data entered using the Create User") + View/Spool/Print/Export | Ch1 §5 ص20-21 (Fig9-10) |
| R-SYS-02 | **List Users Access** | Group (dropdown) **أو** User (dropdown) | "the list of access rights that have been assigned to Users or Groups... includes menu options of **all the modules** for which the User or group has access rights" + View/Print/Spool/Export | Ch1 §6 ص21-22 (Fig11) |
| R-SYS-03 | **Parameter List** | اختيار الإعدادات + **Show All Records** (Active+Passive، بدونه Active فقط) | "the settings in the system" + Print/Spool/Export — **جرد الإعدادات الشامل** (أقرب نظير: Document Audit/خصائص النظام) | Ch3 §18 ص106-107 |

## 2. Report Engine (المشترك)

- الشاشة المشتركة لكل التقارير (Fig10) — تفاصيلها في وثيقة **Getting Started [NOT DOCUMENTED — خارج الحزمة]**.
- صيغ الإخراج الثلاث المقيدة لكل مستخدم من Restrict Report Options: **Excel / Open Calc / Direct**.
- تذكير الاعتمادية: Excel/Open Calc يتطلبان تثبيت التطبيق الخارجي (V-SYS-06).

## 3. ترجمة التقارير إلى البنية الجديدة

| الأصل | النظير المقترح | ملاحظات |
|---|---|---|
| List Users | تقرير Users (Frappe User list + status + group) | مع as-on audit |
| List Users Access | **Role Permission Report** + تقرير صلاحيات الوحدات الخاصة (مدمج!) | الأهم أمنياً — راجع 07-permissions |
| Parameter List | تقرير Feature Toggles + Settings snapshot | مع إظهار Active/Passive |

> [INFERENCE] تقارير صلاحيات الوحدات الخاصة (POS User Access listing وAR access listing) ستُوثق في وحداتها — SYS يوفر المظلة فقط.
