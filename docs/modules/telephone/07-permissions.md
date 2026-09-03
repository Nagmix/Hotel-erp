# 07 — الصلاحيات (Permissions) — وحدة TEL

> **الأنحف في المشروع بعد SLM:** لا قسم User Rights في أي ملف من الأربعة — الصلاحيات الموثقة **استنتاجية من مواضع ثلاثة فقط**: زر SL# الإداري (System Administrator حصراً) + التفويض الظاهر في View Transfers/Extensions (Authorizer!) + التحذير العام "administrative purposes only". GAP-TE-D03.

---

## 1. الصلاحيات الموثقة صراحة (مواضع الثلاثة)

| الموضع | النص الحرفي | الدلالة |
|---|---|---|
| **زر SL#** (Guest Information) | "for **administrative purposes only** and used only by the **System Administrator** to resolve SL# mismatch issues" | الوحيد بتقييد دور مسمّى — موجود أسفل نافذة معلومات النزيل |
| **معتمد التمديد** (View Transfers/Extensions) | "The User who has **worked** on this request and the person who **authorized** this request is also displayed" | دليل على صلاحية اعتماد منفصلة عن التنفيذ (دور Authorizer ضمن FO) |
| **تعديل/حذف الشراكات** | لا قيد موثق على من يعدل LCA/9999999999 | فجوة حرجة (حذفها يكسر التسعير الدفاعي!) |

## 2. الأدوار الضمنية (استنتاج تشغيلي)

| الدور | الأدلة الموثقة |
|---|---|
| **عامل السنترال (Telephone Operator)** | Guest Information/Room Calls Query/Guest Search/Dial Code/Yellow Pages — طبيعة الاستعلامات + قوائم REP/LUK الاستهلاكية |
| **موظف الاستقبال (FO Clerk)** | كرت الباب عند CI/CO + كلمة المرور "when a Guest registration is done" + فوترة الهاتف Room# wise |
| **مشرف الهاتف (Tel Supervisor)** | View-Update Telephone Error (إعادة الترحيل المالي!) + Call Transfer + Activate/Deactivate |
| **مدخل الماسترات** | كل SET (شرائح/أكواد/امتدادات) |
| **مدير النظام (SysAdmin)** | زر SL# + (تقاطع SYS: Module Attributes للمدة) |

> ⚠️ **هذه الأدوار غير معلنة في الدليل** — بنيت من طبيعة الوظائف فقط (P-TE-1 تصميم الصلاحيات عند إعادة البناء).

## 3. الصلاحيات عبر الوحدات (Delegated)

| الوظيفة | من يملكها فعلياً |
|---|---|
| تعديل Module Attributes (عرض المدة) | فصل **SUPERVISOR** في SYS — "Refer CHAPTER SUPERVISOR under MODULE SYSTEM SETUP" (REP ص6) |
| Room/Department/Currency Help | ماسترات SYS/FO — TEL مستهلك |
| بيانات النزيل/الرسائل/الشكاوى | FO (TEL تعرض فقط — لا تحرير موثق) |
| إصدار/تعطيل كلمة المرور | TEL (لكن مشروط بتسجيل FO) |

## 4. عناصر التحكم الوصولية الموثقة

- **Panel → Yellow Pages:** متاح من أي شاشة ("Access other menu options... and Yellow Pages") — لكن Print Yellow Pages نفسه بلا قيد موثق.
- **الإحالة عبر الملكية:** لا مفهوم Owner/Department-level security في أي ملف TEL (مقارنة بـPayroll User Rights per-category في HRP أو BNQ=POS Access).
- **Status Active/Passive:** التحكم بالإتاحة موجود على مستوى الماستر (Country Code "If Passive... cannot be used") — بديل تخزيني للصلاحيات.

## 5. فجوة الصلاحيات (GAP-TE-D03)

- **لا قسم User Rights في SET/CAC/REP/LUK إطلاقاً** — ثاني وحدة بعد SLM (الرابعة بلا INI: CARE/MEM/SLM/TEL — التقارب غير مفاجئ).
- **الأثر العملي:** إعادة الترحيل (Select YES) فعل مالي بلا ضابط موثق — أي مستخدم يملك شاشة Error يستطيع تحويل مكالمات للفوليو!
- **المعالجة التصميمية:** P-TE-1 — أدوار: Tele Operator / Tel Supervisor (إعادة ترحيل) / SysAdmin (SL# + شراكات) + قيد تعديل الشراكات بدور فائق.

## 6. مصفوفة الفعل × الدور المقترحة (من السلوك الموثق)

| الفعل | Operator | FO Clerk | Tel Supervisor | SysAdmin |
|---|---|---|---|---|
| Guest Information/استعلامات | ✓ | ✓ | ✓ | ✓ |
| Print Telephone Bill | ✓ | ✓ | ✓ | ✓ |
| كلمة مرور امتداد | – | ✓ | ✓ | – |
| كرت باب (إصدار/تعطيل) | – | ✓ | ✓ | – |
| Call Transfer | – | – | ✓ | – |
| Activate/Deactivate + بوابات | – | – | ✓ | – |
| **Error Repost (مالي!)** | – | – | ✓ | – |
| زر SL# | – | – | – | ✓ |
| تعديل الشراكات/الشرائح | – | – | – | ✓ (مقترح) |
