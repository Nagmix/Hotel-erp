# 07 — الصلاحيات والأذون (Permissions) — وحدة System Setup ⭐

> **هذه الوثيقة تحسم UNK-013 (نموذج الصلاحيات المظلي)** — الوثيقة الأعلى أولوية في الوحدة. تصهر نموذج SYS مع صلاحيات الوحدات الخاصة الموثقة سابقاً (AR · FAS · POS · FO) في بنية واحدة.

---

## 1. النموذج الموثق الكامل (SYS-SSP Ch1)

### 1.1 الأبعاد الخمسة

| البعد | القيم | المصدر |
|---|---|---|
| **حامل الصلاحية** | Group أو User (اختيار User Classification) | ص12 |
| **النطاق الوظيفي** | Main Module → Sub Module → عنصر قائمة | ص12-13 |
| **نوع العملية** | **Add / Modify / Delete** — تظهر نافذة Options Rights "only for selected menu items" (عناصر Settings/Transaction/Master) | ص12/ص15 |
| **التقارير** | Spool Y/N · Export Y/N · Format (Excel/Open Calc/Direct) — لكل تقرير لكل مستخدم | ص17-19 |
| **التخصيص** | Menu Programs (≤3) · Graphs (3-5) · Guest Info · Statistics | ص15-17 |

### 1.2 البنية الهرمية

```
Service Provider (تفويض مطلق عند التركيب)
   └── System Administrator (Supervisor = Yes → وصول كامل لكل القوائم تلقائياً)
         ├── يمنح عبر User Access:
         │     Group (RBAC تجميعي) أو User (تفصيلي)
         │        × Main Module × Sub Module × Menu Item
         │        × Add/Modify/Delete (لعناصر Settings/Transaction/Master المؤهلة فقط)
         ├── يقيد عبر Restrict Report Options:
         │     Report × {Spool, Export, Format}
         └── يخصص عبر User Menu Access:
               Dashboard (Programs/Graphs/Info/Statistics)
```

**شرط المستوى الأدنى:** أزرار De-assign all / Assign all للمنح/السحب الجماعي (ص13).

## 2. دمج صلاحيات الوحدات الخاصة (الموثقة سابقاً) — النموذج الكلي

| الوحدة | صلاحياتها الخاصة الموثقة | طبقة إضافية فوق SYS |
|---|---|---|
| **AR** | AR User Access: مستخدم × أنواع القيود الأربعة (Debit/Credit/Adjustment/Post) — افتراضي **No** | تحكم بنوع القيد المالي |
| **FAS** | Transaction Type Rights | تحكم بأنواع معاملات FAS |
| **POS** | POS User Access (كاشير × KOT/Billing/Settlement × Regular/Touch/PDA) + **Restrict Outlet Access** (blocklist منافذ!) | 3D تشغيلي + حجب منافذ |
| **FO** | FO User Authorization الخمسية (منفذ + مصرِّح — 6 عمليات حساسة) | تفويض مزدوج للعمليات |
| **AR (إضافي)** | INI #74 (تعديل بعد الطباعة) — صلاحية سلوكية بمفتاح | مفاتيح INI كسلوك |

> **الاستنتاج المعماري (يحسم UNK-013):** النظام الأصلي **RBAC عمودي (SYS) + ACLات أفقية لكل وحدة**. صلاحيات الوحدة لا تُعرَّف من SYS بل من شاشات الوحدة نفسها — SYS يمنح الوصول للقائمة، والوحدة تحكم دقة العمليات داخلها. **القرار F-SYS-8:** في Frappe يُحاكى بـ: Role (Group) + Role Profile/User Permissions (SYS layer) + **custom per-module permission DocTypes** (POS Outlet Access / AR Voucher Types / FO Authorization) لأن Frappe Permissions القياسية لا تعرف "منفذ" أو "نوع قيد" كأبعاد.

## 3. دورة حياة كلمة المرور (الموثقة)

| الحدث | السلوك | المصدر |
|---|---|---|
| الإنشاء | توليد آلي (أبجدي-رقمي) عند اختيار Designation | ص10 |
| الانتهاء | Password Expires (أيام، ≤3 خانات) | ص10 |
| إعادة التعيين | المشرف (User Management) → Reset → **عرض النص الجديد في العمود** | ص38-39 |
| التعطيل | Status Passive → لا دخول | ص10 |
| إعادة التنشيط | تبويب Inactive → Active checkbox → Reset → Save | ص38-39 |
| التتبع | "last date the password is changed" + expiry date معروضان | ص37 |

> ⚠️ **قرار أمني F-SYS-6:** إظهار كلمة المرور بنص مكشوف وترحيلها يدوياً **ممنوع في البنية الجديدة** — Frappe Password Reset عبر رابط بريد/OTP؛ الالتزام بمبدأ التوثيق الوظيفي مع تحسين أمني صريح (يُسجل في gap-analysis).

## 4. التقارير: قيود المنافذ الثلاثة

| القيد | الأثر |
|---|---|
| Spool Y/N | حجب/تمكين إخراج التقرير للطابعة (Spool) |
| Export Y/N | حجب/تمكين التصدير |
| Format | **الصيغة الوحيدة المسموحة**: Excel / Open Calc / Direct (طابعة مباشرة) — "Click the cell to change the report formats" |

**+ تقارير SYS نفسها:** List Users (as-on server date) وList Users Access (Group/User) وParameter List — تعمل داخل Report Engine (Getting Started).

## 5. عمليات SYS الحساسة (تحتاج حوكمة في البنية الجديدة)

| العملية | خطورتها | المقترح |
|---|---|---|
| Module Attributes (تبديل سلوك غير قياسي) | عالية — "function uniquely from the standard functionality" | سجل تدقيق إلزامي + طلب موافقة (الأصل: موافقة إدارية غير مقروءة للنظام) |
| INI editing (خارج النظام!) | قصوى — تحرير ملف نصي خارجي بلا تتبع | استبدال كامل بـ Feature Toggle مع audit (F-SYS-2) |
| Extract Database Tables + Delete | عالية (حذف نهائي للأقراص المستخرجة) | Backup/Restore قياسي |
| Reset Password | متوسطة (كشف نص) | رابط آمن |
| Change Caption | منخفضة | صلاحية Manager |

## 6. تطبيق مقترح على Frappe/ERPNext (قرارات)

| مفهوم FN6i | آلية Frappe | ملاحظات |
|---|---|---|
| User | User | مباشر |
| Group | Role | مباشر |
| Supervisor=Yes | Role "System Manager" | النظير الوظيفي |
| User Access (Module/Sub/Item × Add/Modify/Delete) | Role Permissions + DocPerms (create/write/delete) | الفروق: Frappe على مستوى DocType لا بند قائمة — قاعدة تحويل بند→DocType (F-SYS-9) |
| Menu/Report restriction | Report Permission + has_permission hook | مخصص |
| Dashboard personalization | Workspace + Dashboard (مدمجة أصلاً) | أقوى من الأصل |
| Password expiry | Frappe password policy | مباشر |
