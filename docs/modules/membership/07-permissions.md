# 07 — الصلاحيات والأدوار (Permissions & Roles) — وحدة MEM

> توثيق صريح **شحيح** (كما في أغلب الوحدات التشغيلية) — الصلاحيات تُستنتج من ثلاثة مستويات: توصية اعتماد مدير النظام + سمة تقييد التقارير (عبر SYS العام) + مسار التدقيق الداخلي (Authorized Person/Reason).

---

## 1. مستوى التوثيق الصريح

### 7.1 — اعتماد مدير النظام للسمات
"It is advisable to describe these attributes with utmost caution. It is important that the **System Administrator certifies the setting** in this option" (SET ص10) — النص الوحيد الموثق المتعلق بالصلاحيات، ويعني أن System Attributes خلفية إدارية وليست تشغيلية.

### 7.2 — متطلب المستخدم في تقارير المساءلة
Transaction Check List: "Select the **User (User id of users who have performed the transactions)**" (RPL ص40) — وجود فلترة بالمستخدم = وعي بمساءلة المستخدم (راجع HRP Payroll Audit بنمط old/new values — وحدة MEM أضعف: تعرض المنفذ دون القيم القديمة).

### 7.3 — طبقة مسؤول التغيير (Authorized Person)
كل عمليات الإنهاء الأربعة + القائمة السوداء تتطلب حرفياً:
- "Enter the name of the **authorized person** who has blacklisted/revoked the member" (MMN ص5)
- نفس النص في Termination (ص8) وResignation (ص10) وDeceased (ص11)
- **إقرار مسؤولية شخصية مسجل بالبيانات** — نمط توقيع إلكتروني مبكر داخل السجل نفسه.

## 2. الأدوار المستنتَجة (غير الموثقة صراحة)

| الدور المستنتج | الأدلة | الصلاحيات المتاحة |
|---|---|---|
| System Administrator | توصية SET ص10 | System Attributes + كل الماسترات |
| Membership Clerk | شاشات MPF/MTR اليومية | طلبات/فحص/إيصالات/فواتير خدمية |
| Membership Supervisor | MMN كاملة (إنهاء/تجديد) + محركات الترحيل | عمليات تغيير الحالة + الترحيلات الشهرية |
| Finance/AR Clerk | تقارير RPL المالية (17 تقريراً) + Post Subscription | مراجعة الأرصدة والترحيل |
| Marketing | Birthday/Mailing (4 تقارير + بريد) | قوائم المراسلة والتهاني |

> ⚠️ لا توجد شاشة "Payroll User Rights" مثل HRP ولا "User Access" مثل BNQ=POS — تقييد القوائم يتم عبر **SYS العام** (Module Attributes + Supervisor) — راجع docs/modules/system-setup/07-permissions.md (نموذج الطبقات الأربع الموثق في UNK-013).

## 3. قيود الوصول الفعلية المشتقة من البيانات

1. **السمة #8 كصلاحية سلبية**: منع القائمة السوداء من المرافق — قيد سلوكي وليس شاشة دخول.
2. **فصل الأدوار المالي**: محركات الترحيل (MTR 8-13) تُرحّل إلى ACR — أي أن مستخدمها يمس دفاتر AR؛ الاستدلال: تُدار بواسطة دور مالي.
3. **التصعيد غير موجود**: لا موازنات/اعتمادات متعددة المستويات (مقارنة بـ MGT PR بثلاث درجات INI 355) — الاعتماد الوحيد: اسم الشخص المصرح.
4. **Restrict Reports العام**: نمط SYS المعمم (Spool/Export/Excel/OpenCalc/Direct) يسري على تقارير MEM ضمن نمط المنصة (راجع SYS §General Setup).

## 4. أنماط التدقيق (Audit Trail) داخل الوحدة

| الحدث | أثر المساءلة الموثق |
|---|---|
| Blacklist/Terminate/Resign/Decease | Authorized Person + Reason (+ Cause of Death) داخل السجل |
| Interview | Interview Person + Remarks + Status |
| Service Bill Discount | **Reason إلزامي مع كل خصم** (MTR ص8) |
| Screening | Remarks + حالة التحقق لكل بند |
| المعاملات (تقارير) | فلترة User id في Transaction Check List |
| Revoke كامل | نفس حقول المسؤولية عند الاسترجاع |

> **خلاصة معمارية:** وحدة MEM تعتمد **مساءلة بالبيانات** (من فعل وماذا ولماذا في السجل) بدل **بوابات صلاحيات** — قرار F-ME-10 في إعادة البناء: تحويل حقول Authorized Person إلى روابط User حقيقية مع صلاحيات Frappe.
