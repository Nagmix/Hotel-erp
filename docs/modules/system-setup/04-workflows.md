# 04 — سير العمل (Workflows) — وحدة System Setup

> WF-SYS-01..12 خطوة بخطوة من المتن. SYS وحدة إعداد لا معاملات يومية — دوراتها كلها **دورات حياة إدارية**.

---

## WF-SYS-01 — إنشاء مستخدم جديد
**المصدر:** Ch1 §1 ص8-11.

1. System Setup → User Setup → Create User.
2. إدخال User (≤10) + Name (≤40) + Short Name (≤10).
3. اختيار Designation (من General Setup — اختياري) → **تتولد كلمة المرور آلياً فور الاختيار**.
4. اختيار/كتابة Group (إنشاء مجموعة جديد بمجرد الكتابة).
5. تحديد Supervisor Yes/No (Yes = وصول كامل لكل القوائم).
6. Password Expires (أيام ≤3 خانات).
7. Status Active/Passive → Save → Exit.
8. **متابعة إلزامية:** تعريف User Access (WF-SYS-02) إن لم يكن مشرفاً.

## WF-SYS-02 — تعريف صلاحيات مستخدم/مجموعة
**المصدر:** Ch1 §2 ص12-15.

1. User Setup → Setup User Access.
2. اختيار User Classification: **Groups** أو **Users** → تحديد الهدف.
3. Select → شاشة User/Group Operational Rights.
4. اختيار Main Module ثم Sub Module (قائمة فرعية تتبع الرئيسية).
5. تحديد عناصر القائمة من القائمة المعروضة → **انتظار** نافذة Options Rights (تظهر للعناصر المؤهلة فقط).
6. منح Add/Modify/Delete في Options Rights → Save.
7. (اختياري) De-assign all / Assign all للتبديل الجماعي.
8. Save في شاشة الحقوق → Back → Exit.

**قيد:** "The User Access rights can be defined **only for those who are not categorized as Supervisors**" (ص13).

## WF-SYS-03 — تخصيص الشاشة الرئيسية (Menu Access)
**المصدر:** Ch1 §3 ص15-17.

1. User Setup → Setup User Menu Access.
2. اختيار المستخدم من قائمة النشطين.
3. اختيار Menu Programs — **بحد أقصى 3**.
4. اختيار Graphs — **بين 3 و5** + وسم رسم واحد **Default** (بالنقر على الزاوية اليمنى).
5. checkbox Guest Information + checkbox Statistics.
6. Save → **خروج ودخول جديد لتفعيل العرض**.

## WF-SYS-04 — تقييد تقارير مستخدم
**المصدر:** Ch1 §4 ص17-19.

1. User Setup → Restrict Report Options.
2. اختيار المستخدم → عرض "module wise report options that are accessible by the selected user".
3. لكل تقرير: تبديل **Spool** Y/N و**Export** Y/ N (نقر مزدوج / Space / Enter).
4. اختيار Format: **Excel / Open Calc / Direct** (الأولان يتطلبان MS Excel أو Open Office مثبتين!).
5. Save → Back.

## WF-SYS-05 — إدارة المستخدمين من طرف المشرف
**المصدر:** Ch2 §6 ص37-39.

**إعادة توليد كلمة مرور:** User Management → اختيار المستخدم → زر Reset Password في العمود → Confirm → **النص الجديد يظهر في عمود كلمة المرور** → Save.

**تنشيط معرف خامل:** تبويب Inactive User → checkbox عمود Active → Reset Password → Save.

## WF-SYS-06 — ضبط قيم Front Office الافتراضية
**المصدر:** Ch2 §2 ص25-31.

1. Supervisor → Setup FO Defaults.
2. لكل حقل من الحقول الـ 14: نقر مزدوج/F1 → شاشة اختيار من Master المصدر (انظر 02-configuration §1) → Select.
3. Check In: 12 Noon أو 24 hour (افتراضي 12 Noon).
4. Time Difference: إدخال زمن تجهيز الغرفة (يدوي رقمي).
5. Save.

## WF-SYS-07 — تفعيل/تعطيل Module Attribute
**المصدر:** Ch2 §3 ص31-33.

1. Supervisor → Module Attributes.
2. اختيار الوحدة من dropdown → Select → شبكة سماتها (افتراضي كله NO).
3. **نقر مزدوج على الخلية** للتبديل Yes/No.
4. Update.
5. **شرط مسبق موثق:** فهم كامل للوظيفة + موافقة الجهة المعنية (حوكمة).

## WF-SYS-08 — توليد ملف INI وتحريره
**المصدر:** Ch2 §5 ص36-37.

1. **شرط مسبق:** تعريف Property Code أولاً.
2. Supervisor → Create INI Files → زر التوليد (المصدر N6IRPRP.BAS).
3. التحرير بمحرر نصوص (NotePad/WordPad) — "carefully... Else, there could be functionality issues".
4. مرجع كل مفتاح: وثيقة Module Attributes & INI Settings [خارج الحزمة].

## WF-SYS-09 — استخراج جداول قاعدة البيانات
**المصدر:** Ch2 §4 ص33-36.

1. Supervisor → Extract Database Tables.
2. اختيار جداول من Table Summary أو Select All.
3. (اختياري) Include History Tables + Month_Year (MMYY) لأرشيف شهري.
4. (تقني) GUI Data Extraction: إنشاء `GUI<customer code>.dat` بـ CMD (`Copy con` + CTRL+Z) → زر الاستخراج → يُدرج سلسلة PR تلقائياً.
5. Extract → الملفات إلى **C:\PMSDATA** بامتداد **.INS**.
6. Delete (عند الحاجة) — حذف نهائي للمستخرج.

## WF-SYS-10 — إضافة عملة + سعر صرف
**المصدر:** Ch3 §7-8 ص64-71.

1. General Setup → Currencies → New.
2. Code (≤3) + Name + Short Name + Type (Currency/Travellers Cheque) + Local/Foreign.
3. إن كانت Foreign أو Travellers Cheque: Standard Rate (افتراضي 1).
4. Million/Lakh + Text before/after Decimal (≤20) + Decimal Length (0-3) + Division Method.
5. Save.
6. General Setup → Exchange Entry → New → Currency Code → Serial (آلي ≤4) + Time + Rate → Save.

## WF-SYS-11 — بناء بنية ضريبية (Code → Slab → Structure)
**المصدر:** Ch3 §9-11 ص71-83.

1. **Tax Code:** New → Code/Name/ShortName + Applicable To (checkboxes: FO/POS/Banquet/Purchase) → Save.
2. **Tax Slab:** New → Module (من 7) + Slab Code + Description + Tax Code (F1) + Cumulative Yes/No + بنود الشرائح (Amount To يدوي؛ From آلي متصل) + Cal.Type + Factor → Save.
3. **Tax Structure:** New → Module + Code + Description → بنود: Tax # (آلي) + Tax Code + Calculation Type (Percentage/Amount/Slab) + Factor (أو Slab #) + اختيار الوعاء: **On Value / On Discounted Value / On Tax** (مع الأخير: إدخال Tax # للضريبة السابقة) → Save.

## WF-SYS-12 — إعادة تسمية بند قائمة (Caption)
**المصدر:** Ch2 §1 ص23-24.

1. Supervisor → Change Caption.
2. اختيار بند القائمة → إدخال New Name.
3. إن كان بند تقرير: يجيب النظام عن تطبيق الاسم على التقرير (عمود اختيار).
4. Save — يظهر الاسمان (القياسي + الجديد) معاً أثناء الاستخدام.

---

## سلاسل الاستئناف (بدء التشغيل — Bootstrap)

| الترتيب | الخطوة | لماذا |
|---|---|---|
| 1 | Property Code (WF يتبع §Ch3/1) | شرط توليد INI |
| 2 | Currencies + Exchange | شرط FO Defaults والعملات |
| 3 | Generate INI (WF-SYS-08) | "mandatory during installation" |
| 4 | Departments/CC/Designations/UOM/Reasons | المرجعية المشتركة |
| 5 | Tax engine (WF-SYS-11) | قبل تعريف Outlets/Room Rates |
| 6 | Credit Cards + Program IDs + FO Defaults (WF-SYS-06) | قبل بدء FO |
| 7 | Users/Groups/Access (WF-SYS-01/02) | قبل التشغيل الفعلي |
| 8 | Menu Access (WF-SYS-03) | تخصيص الداشبورد |

> [INFERENCE] الترتيب أعلاه مُستنتج من التبعيات الموثقة (INI بعد Property · FO Defaults بعد Masters) وليس فصلاً مرقماً في الدليل.
