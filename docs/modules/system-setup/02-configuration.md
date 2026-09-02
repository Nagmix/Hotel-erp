# 02 — الإعداد (Configuration) — وحدة System Setup

> مفاتيح الإعداد المركزية: FO Defaults + Module Attributes + INI Files + Captions + استخراج الجداول + إدارة المستخدمين. **التحذير التشغيلي الأهم في الدليل كله هنا**: "These options should be fully understood by your System Administrator... before activating any of them" (ص31).

---

## 1. Setting up FO Defaults — Ch2 §2 ص25-31

القيم الافتراضية التي تظهر آلياً في قوائم Front Office ("The default values are displayed in the respective menu options **only after** the settings are defined"):

| الحقل الافتراضي | مصدر Master الموثق | ملاحظات |
|---|---|---|
| Property Code | **System Setup → General Setup → Property Codes** | — |
| Room Type | FO → Setup → Room Type | — |
| Currency | **System Setup → General Setup → Currencies** | — |
| Market Segment | FO → Setup → Market Segments | — |
| Business Source | FO → Setup → Business Sources | — |
| Nationality | FO → Setup → Nationality | "Normally, the **nationality of the country in which the property is situated** is defined as the default nationality" (ص29) |
| Plan Code | FO → Setup → **Meal Plan** | — |
| Default Foreign Currency | **System Setup → Currencies** | عملة أجنبية افتراضية منفصلة |
| Check In | **12 Noon / 24 hour** (افتراضي 12 Noon) | "This column indicates the check-in and check-out method followed at the Hotel" (ص30) |
| Rate Table | FO → Setup → **Room Rate Master** | — |
| **Time Difference** | رقمي (يدوي) | "Every time there is a checkout the room is termed vacant. The room is normally cleaned before another check-in is recorded... you have the option to set a time difference to get the room ready for the next Guest" — **زمن تجهيز الغرفة بين الخروج والدخول** (فندق-بفندق: "each Hotel requires a different time span") |
| Billing Instruction | FO → Setup → Billing Instructions | — |
| Pay Mode | FO → Setup → Pay Modes | — |

**الدلالة المعمارية:** 14 قيمة افتراضياً موزعة المصدر بين SYS (3: Property/Currency/DFC) وFO (11) — **نمط Defaults كطبقة تحسين إدخال** (قابلة للتجاوز في الشاشات) لا قيوداً.

## 2. Module Attributes — Ch2 §3 ص31-33 ⚠️

| البند | الموثق |
|---|---|
| الوظيفة | "setting options for different modules and sub modules of Fortune PMS. **By default, the options are set to NO**" |
| الواجهة | Module dropdown → زر → شبكة سمات الوحدة → **نقر مزدوج على الخلية** للتبديل Yes/No |
| التحذير | "These options should be **fully understood** by your System Administrator, **on its functionality before activating** any of them as they will function **uniquely from the standard functionality** of relevant menu items" (ص31) |
| الحوكمة | "It is recommended that the settings are changed by your System Administrator **with the approval of the concerned authority**" (ص31) |
| **المرجعية** | "For explanation on each setting of Module Attributes, refer **System Setup – Module Attributes & INI Settings** document" (ص33) — **خارج الحزمة (GAP-SYS-D01)** |

**خريطة المفاتيح المرقمة المعروفة من باقي الوحدات (تُجمع تدريجياً):**

| الوحدة | المفتاح | الوظيفة | المصدر |
|---|---|---|---|
| FO | Attr 1-67 (جرد فهرسي) | منها: تعديل السلوك عبر شاشات FO | FOM-SET §4 |
| FO | Attribute 16 | Post History (INI موثق معها) | FOM-SET |
| POS | Attr 6 | NC Bill Print | POS-SET §15 |
| POS | Attr 29 | Common Menu / per-Outlet Menu (بنية القائمة المزدوجة) | POS-SET §24 |
| POS | Attr 32 | Network Printer | POS-SET |
| FAS | Module Attr 9 | سلوك مالي | FAS-SET |
| **INI** | 56 | **Acr2Fas: 0=مكّن (افتراضي 1=معطل!)** | ACR-SET |
| INI | 58 | Reservation Mode | FOM-SET |
| INI | 64 | مفتاح FO موثق | FOM-SET |
| INI | 74 | السماح بتعديل AR بعد الطباعة (0=يسمح) | ACR-SET |
| INI | 283 | الاستهلاك | FOM-SET |
| INI | 404 | Member Discount: 1=رئيسي فقط/0=رئيسي+ثانوي | POS-SET §41 |
| INI | 504 | الشيكات | FOM-SET |
| FAS | Switch 4 | مفتاح FAS | FAS-SET |
| INV | Switches 1/3/4 | طرق محاسبة ضريبة الشراء | FAS-SET |

## 3. Creating INI Files — Ch2 §5 ص36-37

| البند | الموثق |
|---|---|
| المصدر | "create INI setting files based on the **N6IRPRP.BAS** file which is part of the licensed product. The source file N6IRPRP.BAS gives a brief description of setting options" |
| الإلزامية | "During the initial process of Installation and Setup of Fortune 6i at the Property, it is **mandatory** to generate and setup the INI file. This process is carried out by the System Administrator... in consultation with the respective Heads of Departments. The setting should be done **only after clearly understanding each option**" |
| التوقيت | "You can generate this file **after defining the Property Code** setting under General Setup" |
| التحرير | "use Windows Note Pad, Word Pad or any Text Editor. This should be **carefully** done. **Else, there could be functionality issues** with the Fortune PMS product" |
| طبيعة الملف | "A file name with an extension INI is a **plain text file containing configuration information** to save your preferences. Normally, it is compatible to older or newer versions of Fortune Enterprise products" |
| المرجعية | نفس وثيقة GAP-SYS-D01 |

## 4. Changing Caption — Ch2 §1 ص23-24

- **الغرض:** "change the name of the menu option... **if it does not match with the local names** used for the same operation" — توطين تسميات.
- **السلوك:** "Fortune Next displays **both – the standard menu name and the new name** by which you would like to call it during operations".
- **للتقارير:** "If the menu option selected is a **report option**... queries if the new name has to be applied for the report" + عمود اختيار "if you wish the new caption to appear on the reports instead of the standard menu name".
- **محدودية:** "The new name... can be seen immediately after the change is recorded. But this is **not displayed in the list of menu options**" (ص24 Note) — [UNCERTAIN] دلالة هذه العبارة (يُعرض أين إذن؟ في الاستخدام وليس القوائم).

## 5. Extract Database Tables — Ch2 §4 ص33-36

| الخيار | الوظيفة | ملاحظات |
|---|---|---|
| Table Summary | قائمة كل الجداول / Select All | — |
| Include History Tables | جداول "created and identified accordingly to record information **prior to the current date**" | تاريخية بلاحقة MMYY |
| Month_Year | MMYY — "extract the tables **suffixed with MMYY**" | أرشفة شهرية |
| GUI Data Extraction | "extract specific tables based on the **assigned Customer Code** for system analysis, trouble shooting and maintenance by your authorized service provider" — بملف **GUI<customer code>.dat** (يُنشأ بـ `Copy con` في CMD!) | "along with information containing **PR table series by default**" |
| File | مثل السابق لكن بـ <filename>.dat عام | — |
| Delete | "permanently **deletes all tables** that have been extracted and located in the default directory" | حذف نهائي |
| الوجهة | **C:\PMSDATA** بامتداد **.INS** | "can be used to be inserted into a database in an eventuality or inserted to another database for **analytical purposes**" |

## 6. User Management (المشرف) — Ch2 §6 ص37-39

- **عرض:** المستخدمون + معرفاتهم + المجموعة + حالة المعرف (نشط/لا) + **تاريخ انتهاء كلمة المرور + آخر تاريخ تغيير**.
- **Reset Password:** اختيار مستخدم → زر العمود → Confirm → "The password will be changed and the **new password can be viewed in corresponding password column**, which the user can use as the new password for his next logins" (ص39) — **إظهار كلمة المرور بنص مكشوف**.
- **Activate Inactive User:** تبويب Inactive User → checkbox في عمود Active → Reset Password → Save.

## 7. تقييم معماري: SYS-Configuration مقابل Frappe

| مفهوم FN6i | نظير Frappe/ERPNext | القرار المقترح |
|---|---|---|
| Module Attributes | `System Settings` + custom `Feature Toggle` DocType | **قرار F-SYS-1:** جدول موحد `Hotel Feature Toggle` (module, key, value, description) بذات دلالة Yes/No المزدوجة، مع UI نقر مزدوج ↔ Switch مألوف |
| INI Files | Site Config + System Settings | **قرار F-SYS-2:** لا توجد ملفات نصية؛ كل مفتاح = سجل في `Feature Toggle` (نفس الجدول أعلاه) + استيراد/تصدير JSON بدل .INI — **يحل مشكلة التحرير اليدوي الخطر** |
| Changing Caption | `__traslate__`/Custom Translation DocType | **قرار F-SYS-3:** أسماء الواجهة الجديدة من قاموس ترجمة i18n كامل (ar/en) — Caption الأصلي **يُستنسخ مفهومه لا آليته** (عرض الاسمين معاً يُسقط) |
| FO Defaults | Defaults per Company / user | **قرار F-SYS-4:** DocType `PMS Defaults` (property, module, field, value) — قيم قابلة للتجاوز في الشاشات |
| Extract DB Tables | Database Backup (Bench) | **قرار F-SYS-5:** يُستبدل بـ Backup/Restore القياسي + Data Export JSON؛ GUI .dat غير قابل للاستنساخ ولا مطلوب |
| User Management | User/Password Reset في Frappe | مقابلة مباشرة؛ إظهار كلمة المرور المكشوفة **يُمنع** (قرار أمني F-SYS-6) |
