# 07 — الصلاحيات (Permissions) — وحدة FNB

> ⚠️ **الوحدة السادسة بلا أي قسم User Rights موثق** (بعد CARE/SLM/MEM/TEL/MNT) — 76 صفحة بلا ذكر Group/User/Rights مرة واحدة. الأدوار **مستنتجة تماماً** من طبيعة الوظائف، مع خطورة خاصة: **إعادة الجرد وترحيل الأرصدة والطلب الآلي أفعال خالدة/عارضة للحدود بلا أي ضابط موثق**.

---

## 1. ما هو موثق (شبه لا شيء)

| العنصر | الحالة |
|---|---|
| قسم User Rights / Define Rights | ❌ غير موجود في الملفات الأربعة |
| ذكر Groups أو User IDs | حقل User ID واحد في Costing Start Date (أثر تدقيق سلبي فقط — SET ص3) |
| دور مسمى (مثل Supervisory User في MNT) | ❌ لا شيء |
| قيد ملكية (مثل User-specific في TEL Address Book) | ❌ لا شيء |

## 2. الأدوار المستنتجة (للاعتماد في مرحلة التصميم)

| الدور المستنتج | الأساس الوظيفي | أخطر صلاحياته |
|---|---|---|
| **F&B Controller / Cost Accountant** (مالك الوحدة) | الميزانيات + Cost Report + Profitability + الترحيل السنوي | Stock Balance Transfer السنوي (ترحيل FY!) · Audit Date (قفل المعاملات!) |
| **Executive Chef / Kitchen Manager** | الوصفات + Sub Recipes + الإنتاج | Recipe Master (تسعير تحذيري!) · Auto Indent (وثيقة خالدة!) |
| **Store Keeper / Inventory Clerk** (مستعير من MGT) | Kitchen Stock اليومي + الافتتاحي | Adjustment vs Physical (تعديل الرصيد الحاسوبي ضمنياً عبر الفعلي!) |
| **Outlet/Restaurant Manager** | Manual Sales + عرض التقارير | Manual Sales Entry (بيع غير محوسب بإيصال واحد Consolidated!) |
| **Auditor/Comptroller** (قراءة) | كل التقارير والاستعلامات | Read-only بطبيعتها |

## 3. نقاط الخطورة بلا ضابط

1. **Costing Start Date + Audit Date**: قفل دائم وسقف معاملات — **من يملك كتابتهما؟** بلا User Rights = أي مستخدم يصل للشاشة نظرياً (GAP-FB-D01).
2. **Auto Indent خالد** (لا modify/delete): إن ولّده مستخدم خطأً بالكمية الخاطئة → indent خاطئ **لا يُصحَّح** ويستقبله MGT! (اقتران GAP-FB-D01 + P03).
3. **Stock Balance Transfer** (يومي/سنوي + Cancel): Cancel يلغي الترحيل — **أي رصيد افتتاحي للغد معلّق على إجراء بلا توثيق ضابط**.
4. **SWITCH 511 يمنع البيع في POS**: من يبدّله؟ (حاجب تشغيلي على وحدة أخرى من إعداد FNB!)
5. **Modify-by-Doc#** في الجرد (F5+Yes للحذف) — أدوات كتابة على أرصدة التكلفة اليومية بلا توزيع أدوار.
6. **Open/Modifiers Items**: صيانة الربط تتم من شاشة استعلام (Lookup-as-Editor) — مستخدمو "العرض فقط" نظرياً يملكون **بناء ربط** — نفس نمط Complaint Status (Q) في MNT (معدِّل من استعلام) لكن هنا للتكلفة.

## 4. قرار إعادة البناء المقترح

- أدوار Frappe قياسية: **F&B Controller** (كل الوحدة) · **Chef** (Recipe/Production doctypes فقط) · **Stock User** (Kitchen Stock/KOT حاجب) · **Accounts User** (قراءة).
- قفل خاص: Costing Start Date/Audit Date/Switch 511 لحصر **System Manager + F&B Controller** (workflow خاص بأثر تدقيق).
- Auto Indent: حالة Draft قابلة للإلغاء قبل التقديم (يكسر الخلود الأصلي بأمان — قرار تصميمي D-FB-3) مع سجل مَن ولّده.
