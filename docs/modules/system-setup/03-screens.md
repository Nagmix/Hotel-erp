# 03 — كتالوج الشاشات — وحدة System Setup

> 66 شاشة/شكلاً مرقماً موثقاً في SYS-SSP (Figures 1-66). الأولويات وفق الأثر المعماري على الواجهة الجديدة (P0 = لازمة للإطلاق، P1 = للإطلاق الكامل، P2 = لاحقاً/استبدال معماري).

---

## 1. User Setup (12 شاشة)

| ID | الشاشة | الشكل/الصفحة | الأولوية | الملاحظات |
|---|---|---|---|---|
| S-SYS-01 | User Setup (القائمة) | Fig1/ص14 | P0 | نقطة دخول الفصل |
| S-SYS-02 | Create User | Fig2/ص15 | **P0** | 9 حقول + توليد آلي لكلمة المرور |
| S-SYS-03 | Modify User (قائمة الاختيار) | ص11 | P0 | F1 Browse |
| S-SYS-04 | Setup User Access | Fig3/ص20 | **P0** | Groups/Users |
| S-SYS-05 | User/Group Operational Rights | Fig4/ص21 | **P0** | Main/Sub Modules + قائمة العناصر + Assign/De-assign |
| S-SYS-06 | Options Rights (Add/Modify/Delete) | ص15 | **P0** | نافذة منبثقة للعناصر المؤهلة |
| S-SYS-07 | Setup User Menu Access | Fig5/ص23 | P1 | Menu Programs (≤3) + Graphs (3-5) + Guest Info + Statistics |
| S-SYS-08 | Main Screen with Menu Programs | Fig6/ص25 | P2 | **مرجع UX للداشبورد الجديد** |
| S-SYS-09 | Restrict Report Options (Main) | Fig7/ص27 | P1 | User dropdown |
| S-SYS-10 | Restrict Report Options (User) | Fig8/ص29 | P1 | شبكة Module×Report×Spool/Export/Format |
| S-SYS-11 | List Users | Fig9/ص30 | P2 | تقرير (As on = server date) |
| S-SYS-12 | List Users Access | Fig11/ص32 | P2 | تقرير (Group/User) |

(+ Report Engine Fig10/ص31 — شاشة عامة من Getting Started.)

## 2. Supervisor (10 شاشات)

| ID | الشاشة | الشكل/الصفحة | الأولوية | الملاحظات |
|---|---|---|---|---|
| S-SYS-13 | Supervisor Setup (القائمة) | Fig12/ص35 | P0 | — |
| S-SYS-14 | Change Caption | Fig13/ص36 | P2 | قائمة عناصر + New Name + عمود التقارير |
| S-SYS-15 | Setup FO Defaults | Fig14/ص38 | **P0** | 14 قيمة افتراضية + Round-off للخصائص |
| S-SYS-16 | Module Attributes | Fig15/ص46 | **P0** | Module dropdown + شبكة Yes/No بنقر مزدوج |
| S-SYS-17 | Extract Database Tables | Fig16/ص48 | P2 | (استبدال معماري بـ Backup) |
| S-SYS-18 | Create INI Files | Fig17/ص52 | P2 | (استبدال بـ Feature Toggle) |
| S-SYS-19 | User Management (Active) | ص37-38 | **P0** | جدول المستخدمين + Reset Password |
| S-SYS-20 | User Management (Inactive tab) | ص38-39 | P0 | تنشيط المعرفات المعطلة |

## 3. General Setup — الكيانات المرجعية (44 شاشة/شكلاً)

| ID | الشاشة | الأشكال/الصفحات | الأولوية | ملاحظات |
|---|---|---|---|---|
| S-SYS-21 | General Setup (القائمة) | Fig18/ص55 | P0 | 18 بنداً |
| S-SYS-22 | Property Codes | Fig19/56 + Fig20/60 + Fig21/61 | **P0** | + شاشة Round Off + شاشة Address |
| S-SYS-23 | Departments | Fig22/62 + Fig23/64 + Fig24/65 | **P0** | Module: General/Banquet |
| S-SYS-24 | Cost Centers | Fig25/66 + Fig26/68 + Fig27/69 | **P0** | — |
| S-SYS-25 | Designations | Fig28/70 + Fig29/72 + Fig30/73 | **P0** | Guest Type: Guest/Others/S&M |
| S-SYS-26 | Units of Measurement | Fig31/74 + Fig32/76 + Fig33/77 | P1 | →POS/MM/F&B |
| S-SYS-27 | Reason Codes | Fig34/78 + Fig35/80 + Fig36/81 | **P0** | 9 وحدات target + Gift Shop! |
| S-SYS-28 | Currencies | Fig37/82 + Fig38/85 + Fig39/86 | **P0** | 10 حقول (أغنى عملة) |
| S-SYS-29 | Exchange Entry | Fig40/87 + Fig41/89 | **P0** | ≤4 إدخالات لكل عملة |
| S-SYS-30 | Tax Codes | Fig42/90 + Fig43/92 + Fig44/92 | **P0** | Applicable To: FO/POS/BQT/Purchase |
| S-SYS-31 | Tax Slabs | Fig45/95 + Fig46/98 | **P0** | تراكمي/غير تراكمي + شرائح آلية |
| S-SYS-32 | Tax Structures | Fig47/100 | **P0** | On Value/Discounted/Tax |
| S-SYS-33 | Guest Comments | Fig48/103 + Fig49/104 + Fig50/105 | P1 | 1-25 نظامية غير قابلة للتعديل |
| S-SYS-34 | Program ID — Front Office | Fig51/108 | P1 | — |
| S-SYS-35 | Program ID — AR (1)(2)(3) | Fig52-54/109-110 | P1 | ثلاث مجموعات |
| S-SYS-36 | Program ID — Laundry | Fig55/110 | P1 | — |
| S-SYS-37 | Setup Credit Cards | Fig56/113 + Fig57/114 + Fig58/115 | **P0** | Floor Limit + حقلا N/A |
| S-SYS-38 | Print Bill Message | Fig59/117 + Fig60/118 + Fig61/119 | P1 | From/To/Subject/Outlet/Message |
| S-SYS-39 | Religions | Fig62/120 + Fig63/121 | P1 | — |
| S-SYS-40 | Occupations | Fig64/123 + Fig65/124 + Fig66/125 | P1 | — |
| S-SYS-41 | Parameter List | ص106-107 | P1 | Show All Records |
| S-SYS-42 | Group Nationality | ص108-109 | P1 | [UNCERTAIN] توثيق هامشي |

> **إجمالي: 66 شكلاً مرقماً (Figures 1-66) + 3 شاشات فرعية غير مرقمة (Round Off/Address/Options Rights) ≈ 42 شاشة تشغيلية فعلية.** توزيع الأولويات: **P0 = 19 · P1 = 14 · P2 = 9**.

## 4. أنماط UI الموحدة (Identifying Standards — ص6-7)

| النمط | الوصف الموثق | ترجمة الواجهة الجديدة |
|---|---|---|
| New / Modify / Delete / Browse | أزرار قياسية؛ Delete "works only for selected modules and is conditional" | CRUD قياسي مع حذف مشروط |
| Prev/Next | "enabled **only after** the user click Browse" | ترقيم صفحات |
| Save | — | حفظ |
| آخر زر | Command Window · Internode Communication · Calculator · Calendar · Scratch Pad · Yellow Pages | أدوات مساعدة (الآلة الحاسبة/التقويم **موجودة** في الواجهة الأصلية!) |
| Exit | — | خروج |
| Status | Active/Passive + "By default, the option is set to Active" | Toggle موحد |
| User | "Displays the User Name who has logged-in" | شريط علوي |
| Last Updated | "The Date and Time, Fortune Next 6i Product was last updated **by the user**" | audit مدمج بشاشة كل Master — **يتقاطع مع نمط Master Data العام** (Last Updated في كل الشاشات) |
| F1 / نقر مزدوج | استدعاء شاشات المساعدة/الاختيار في كل الحقول المرجعية | Search/Select موحد |
