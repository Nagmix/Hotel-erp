# 07 — الصلاحيات (Permissions) — وحدة Banquets

> BNQ ترث **ثلاث طبقات صلاحيات دفعة واحدة**: SYS المظلة + POS User Access (المشترك!) + تخصيص الرسم والتعديل.

---

## 1. الطبقات الثلاث الموثقة

| الطبقة | النطاق | المصدر |
|---|---|---|
| **1. SYS المظلة** | User Access (Add/Modify/Delete لعناصر Banquet) · Create User (الوجود أصلاً) · PO Cashier grouping · Restrict Report Options | BIL §§1-2 + SET §20 |
| **2. POS User Access (BNQ §20)** | "There are three options such as **KOT, Billing and Settlement**" — KOT: **28 عملية** (updation/deletion/table transfer...) · Settlement: **15 عملية** · By User/By Group · نقر مزدوج = Yes (أخضر) | SET §20 |
| **3. تخصيص الرسم/التعديل** | Make/Amend من Availability Chart: "You can make or amend booking **based on User Authorization**" · Resettle: "must be given access using the POS User Access option" · كل نمط تسوية "based on User access provided using option **POS User Access**" | LUK §2 + BIL §4 |

## 2. دور PO Cashier (جماعة SYS)

"User must be **PO Cashier** in order to open an Outlet... The User is grouped as **POCashier** using the option **Create User** under System Setup" — **تجسيد Role قياسي واحد** (مطابقة مباشرة لـ Role في Frappe).

## 3. BNQ User Access — تفاصيل الأقسام

### KOT (28 عملية)
"access rights can be provided for KOT updation, deletion, table transfer etc." — قائمة موسعة تشغيلياً (أسماء العمليات الـ 28 كاملة [NOT DOCUMENTED] — 3 مذكورة أمثلة).

### Settlement (15 عملية)
يشمل نمطاً نمطاً + Resettlement + إعادة الطباعة على الأرجح [INFERENCE من السياقات].

### Billing
البند الثالث بالاسم (بلا عدّ) — عمليات الفوترة.

## 4. صلاحيات سياقية موثقة إضافية

| الصلاحية | السياق | المصدر |
|---|---|---|
| **PDF access** | auto email لحفلة الحجز: "provided the user have an **access to PDF**" | BOK ص7 |
| **Follow up user** | Banquet Staff — فقط المختارون يظهرadmin في Make Booking | CFG §11 |
| **Supervisor vs User** | Booking Made By في Event Calendar (تقويم حاجب لكل فئة) | SET §10 |
| **User Authorization للتعديل** | Amend فقط current/future | LUK §2 |
| **Password عند الإغلاق** | Close Shift: "authenticate by entering a password" | BIL §5 |

## 5. إسقاط Frappe (تفصيل 16-erpnext-mapping)

- POS User Access = **نفس ACL DocTypes المخصصة لـ POS** (البُعد الثلاثي) — BNQ وحدة إضافية تستهلك الجدول نفسه (F-BQ-1: محرك كاشير موحد).
- PO Cashier = **Role** قياسي.
- Banquet Staff = User Permission على Banquet module + `custom_is_banquet_staff`.
- PDF access = File/Print permission قياسي.
