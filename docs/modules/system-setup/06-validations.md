# 06 — التحقق (Validations) — وحدة System Setup

> V-SYS-01..22 — قيود إدخال وسلوك رفض موثقة نصاً.

---

| ID | القيد | النص/السياق | المصدر |
|---|---|---|---|
| V-SYS-01 | User: أبجدي-رقمي ≤10 · Name ≤40 · Short Name ≤10 | حدود الحقول | ص9 |
| V-SYS-02 | Password Expires: رقمي ≤3 خانات | أيام | ص10 |
| V-SYS-03 | لا صلاحيات لمستخدم Supervisor | "User Access rights can be defined **only** for those who are **not** categorized as Supervisors" | ص13 Note |
| V-SYS-04 | Menu Programs ≤3 | "maximum of three menu programs only" | ص16 |
| V-SYS-05 | Graphs بين 3 و5 إلزاماً | "minimum three and a maximum of five graphs only" | ص16 |
| V-SYS-06 | Excel/Open Calc يتطلبان تثبيت التطبيق الخارجي | "To select Excel or Open Calc, you should have **installed** the third party MS Excel or Open Office software applications" | ص19 |
| V-SYS-07 | Property Code ≤3 · Name ≤30 · Short ≤10 | — | ص42 |
| V-SYS-08 | Applicable From: > تاريخ اليوم (وإلا يبقى افتراضياً اليوم) | يتكرر في كل Ch3 — إدخال تاريخ مستقبلي مقبول فقط | كل Ch3 |
| V-SYS-09 | Department Code ≤4 · CC Code ≤4 · Designation ≤3 | — | ص47/ص51/ص54 |
| V-SYS-10 | UOM ≤3 + Unit Name ≤15 | — | ص57-58 |
| V-SYS-11 | Reason Code ≤3 + Description ≤20 + Module من 9 | — | ص61-62 |
| V-SYS-12 | Currency Code ≤3 · Text before/after ≤20 · Decimal Length ∈ {0,1,2,3} | — | ص64-66 |
| V-SYS-13 | Standard Rate حكر على Foreign أو Travellers Cheque | "applicable, only if you select Foreign... or if you select Travelers Cheque" | ص64 |
| V-SYS-14 | Exchange Entry: Serial آلي + **≤4 إدخالات** | — | ص70 |
| V-SYS-15 | Tax Code ≤3 + Applicable To ∈ {FO, POS, Banquet, Purchase} | — | ص72 |
| V-SYS-16 | Tax Slab: Code رقمي ≤4 + Module من 7 | — | ص76-77 |
| V-SYS-17 | Tax Structure: رقمي ≤3 + Factor يُلغى مع Slab + Slab # مع Slab فقط + On Tax يلزم Tax # | ترابط الحقول الثلاثة | ص81-82 |
| V-SYS-18 | Guest Comments: التعديل ≥26 فقط | 1-25 نظامية | ص85 |
| V-SYS-19 | Program ID: أبجدي-رقمي ≤7 + منفذ ∈ {LPT1,LPT2,COM1,COM2,COM3,USB} | — | ص88 |
| V-SYS-20 | Credit Card Type ≤10 · Floor Limit رقمي 12+2 | "Ex: 100000000000.00" | ص94 |
| V-SYS-21 | Print Bill Message: Subject ≤10 · Message ≤100 + To Date إلزامي | — | ص97 |
| V-SYS-22 | Religion/Occupation: Code ≤2 · Description ≤30 | — | ص100/ص104 |

## مصفوفة الرسائل/الاستجابات الموثقة

| الحدث | الاستجابة الموثقة |
|---|---|
| حفظ تعديل مستخدم | "a message prompting the user to redefine Access Rights" (ص11) |
| تعيين Designation لمستخدم | "the password generates automatically in the password field" (ص10) |
| اختيار بند تقرير في Change Caption | "Fortune Next queries if the new name has to be applied for the report" (ص24) |
| Save في User Management (Reset) | "The password will be changed and the new password can be viewed in corresponding password column" (ص39) |
| INI محرر خطأً | "there could be functionality issues with the Fortune PMS product" (تحذير لا رسالة) (ص37) |
| Delete بغير شرط | "This button works only for selected modules and is conditional" (زر الحذف العام — ص6) |

> ملاحظة: **لا توجد رسائل رفض صريحة (Error Messages) موثقة في SYS-SSP** — عكس ACR/POS؛ قيود الأطوال هي حواجز الإدخال. النمط العام للوحدات: التحقق عند الحفظ.
