# 02 — الإعدادات والتخصيص (Configuration) — وحدة Materials Management

> مفاتيح Module Attributes/INI الموثقة في MGT (الأكبر تراكماً بعد FOM) + Access Rights الرباعية التبويبات + Email Access Rights + أدوات الحياة (Purging) + Foot Notes + Print Forms.

---

## 1. مفاتيح الإعداد الموثقة في وحدة MGT (الجدول التراكمي يُوسَّع)

### 1.1 مفاتيح INI (ملف نصي — تُستبدل بـ Feature Toggle وفق F-SYS-1/2)

| المفتاح | الاسم/الوظيفة | القيم | المصدر |
|---|---|---|---|
| **INI #39** | طول كود الصنف | رقم (افتراضي **12**)؛ "can be modified as required **only by IDS Customer Service Engineers or by authorized EDP personnel** at the Property" — **يُجمَّد بعد بدء التشغيل** | SET §5 ص10 |
| **INI #131** | تشغيل Sub Cost Centre | "functional **only when the switch number 131... is set to zero**" — قيمة 0 = مفعل (نمط معكوس!) | SET §13 ص42 |
| **INI #245** | Barcode Link | "**BEV, FB, or LQ**" حسب المخازن المفعّل فيها الباركود (متعدد القيم!) | SET §5 Barcode ص14 |
| **INI #355** | INVPURREQAUTHORISATION — درجات تفويض طلبات الشراء | "**0** (افتراضي: لا إلزام) / **1** = Level One / **2** = Level Two / **3** = Level Three" — مفتاح **متدرج القيمة** لا ثنائي | DNT §1 ص5 |

### 1.2 مفاتيح Module Attributes (الوحدة INV — Module Attributes تحت System Setup)

| المفتاح | النص الأصلي للوظيفة | القيمة/الأثر | المصدر |
|---|---|---|---|
| **INV #3** | "The Bill # and Bill date is mandatory" | YES → إلزام Bill#/Date في Receipt | DNT §6 Receipt ص32 |
| **INV #5** | "In Receipt / PO Indent is not mandatory" | YES → تمكين الاستلام المباشر (Direct) بلا PR/PO؛ **نفس المفتاح يفعّل SPO**: "To activate SPO, Switch #8 should get set... Serial No. 5 'In Receipt / PO Indent is not mandatory' to 'Yes'" ⚠️ [UNCERTAIN] الترقيم: النص الأول يقول #5 والثاني يسميه Switch #8 Serial 5 — يُوثَّق بالتسمية النصية لا بالرقم فقط | DNT §6 ص31 + §4 ص21 |
| **INV #6** | Indent Authorization One | YES → إلزام تفويض المستوى الأول للـ Indent | DNT §2 ص15 |
| **INV #7** | Indent Authorization Two | YES → إلزام المستوى الثاني | DNT §2 ص15 |
| **INV #13** | Purchase Order Authorization One | YES → إلزام تفويض PO مستوى 1 | DNT §3 ص21 |
| **INV #14** | Purchase Order Authorization Two | YES → مستوى 2 | DNT §3 ص21 |
| **INV #298** | Purchase Order Authorization Three | YES → مستوى 3 | DNT §3 ص21 |

> **نمط معماري جديد (يُضاف لقرار F-SYS-1):** مفتاح INI 355 يعمل **بنظام قيمة متدرجة (0/1/2/3)** بدل Yes/No — تصميم `Hotel Feature Toggle` يحتاج حقل قيمة نصية/رقمية عامة لا علم ثنائي فقط، مع تفسير دلالي لكل قيمة في الوصف.

### 1.3 الإعدادات المرجعية المستهلكة (من SYS)

| الإعداد | الاستهلاك في MGT |
|---|---|
| Cost Centers (SYS) | Indent Templates + Variance CC + Link CC to Dept + كل معاملات CC |
| Reason Codes (SYS) | "Reasons are displayed from the **Reasons Definition option under System Setup module**" (DNT ص40) |
| Tax Code/Slab/Structure (SYS) | PO / SPO / Item Taxes / Item Master by Vendor / Misc Tax |
| UOM (SYS) | كل الأصناف (Issue UOM / Conv UOM) |
| Currencies + Exchange (SYS) | Vendor Currency / PO Currency / Receipt Exc. Rate |
| Company Types (SYS) | ⚠️ الدليل يقول "Company Types option **under the Front Desk module**" (SET ص22) — [UNCERTAIN] مالك الكيان: FO أم SYS؟ (الأنماط السابقة ترجّح تعريفاً في FO واستهلاكاً عاماً) |

---

## 2. Access Rights (صلاحيات الوحدة — أربع ركائز)

**المصدر:** MGT-SET §24 ص61-65.

**النموذج الرباعي المخصص للوحدة:** "You can provide access rights Store wise, **option wise**, Department/Cost Centre wise or to **update backdated transactions**" (ص61) — بُعدان غير قياسيين فوق نموذج SYS المظلي:

| التبويب | الآلية | تفاصيل موثقة |
|---|---|---|
| **1. Store** | مستخدم × مخزن | "Select the username... Select the Store name for which you want to provide access" — عزل مخزني صريح |
| **2. Option** | مستخدم × وظيفة | "list of functions will be displayed. Double-click on the **Access Rights column**... **Press F2 to provide/restrict access at once for all functions**" — تبديل جماعي |
| **3. Department/Cost Centre** | مستخدم × قائمة | "Double-click on the **Authorized column**" لكل Department/CC — قوائم إذن |
| **4. Backdate Trn. Access** | مستخدم × نوع معاملة × أيام | "provide access to different types of Transaction **for a specified number of days**" — **نافذة رجعية رقمية** (أيام) — إبداع حوكمة توثيقي فريد |

> **أثر معماري:** النافذة الرجعية (أيام محددة لكل نوع معاملة) **لا نظير مباشر لها في Frappe Permissions** — تحتاج حقل `custom_backdate_days` على User/Role + تحقق في التحقق من الصحة لكل DocType معاملة (قرار F-MG-4).

---

## 3. Email Access Rights (بريد الوحدة)

**المصدر:** MGT-SET §25 ص65-67.

**البنية:**
- توجيه **User/Group**: "Click User/Group based on which you want to tag the email ids" — اسم + بريد + موبايل المُرسِل.
- قائمة Mail ID مع وسم **CC أو BCC** لكل مستخدم (checkbox).
- **قوالب بريد لكل Program Type**: "Select the Module and the Program Type" → Template Name + Subject + content + **"Set up Default Template"** (قالب افتراضي واحد لكل برنامج).

**الاستهلاك الموثق:** تُرسل بها مخرجات مثل PR ("Print/Email/Print and Mail the Purchase Requisition" DNT ص7) — **آلية إشعارات الوحدة الأصلية** → تُستبدل بـ Notification + Email Template القياسية في Frappe (قرار F-MG-8).

---

## 4. Indent Purging (تنظيف الطلبات التوليدية)

**المصدر:** MGT-SET §26 ص67. الخيارات: **Days أو Date** كأساس + "Cut-off days or the date upto which you want to purge" — **"purge auto-generated requisitions. The data pertaining prior to the cut off days will be purged"** — أي أن التطهير يستهدف **الطلبات الآلية (Re-Order/DPR)** تحديداً!

## 5. Purge PO/SPO

**المصدر:** MGT-SET §27 ص67-68. النوع (PO/SPO) + نطاق تاريخ From/To → عرض القائمة → **checkbox لكل PO أو الكل** → Purge — حذف انتقائي مدقق.

## 6. Foot Notes (حاشيات التقارير الهرمية)

**المصدر:** MGT-SET §23 ص59-60.

**البنية:** Type (فئة التقرير) × **Note 1/2/3** — "The hierarchy-based designation is entered in Note1, 2 & 3, where **1 being the lowest designation**".

**مثال الدليل:**

| Type | Note 1 (الأدنى) | Note 2 | Note 3 |
|---|---|---|---|
| Food Cost Report | General Manager | Food & Beverage Operations | Food & Beverage Cost Controller |
| Purchase Order Print | General Manager | Finance Manager | Purchase Manager |
| Vouchers | Financial Controller | Accounts Manager | Accountant |

> [UNCERTAIN] الترتيب الهرمي في المثال (GM كـ Note 1 = "الأدنى"؟) يوحي أن الترقيم قد يعكس **ترتيب التوقيع لا التسلسل الوظيفي** — يُنقل كما هو مع التمييز.

## 7. User Defined Print Forms

**المصدر:** MGT-SET §28 ص68. "customize the format of bills, vouchers, slips... column width, page properties and other parameters" — **يحيل كلياً** إلى "User Defined Print Forms in **Getting Started document**" (خارج الحزمة — GAP-SYS-D02). نمط POS Print Designer نفسه يظهر هنا مفاهيمياً.

## 8. Store Start Date كإعداد تشغيلي (ضبط البدء)

- Month/Year **≤ الشهر الحالي** (اتجاه معاكس لـ Applicable From — إعداد تاريخي لا مستقبلي).
- **شرط تعاقدي:** تعريفه يفتح Opening Balance؛ وبدء المعاملات يجمّد الرصيد الافتتاحي نهائياً.

## 9. مصفوفة الأعلام السلوكية للأصناف (Inventory Master)

الأعلام الثلاثة لكل صنف×مخزن تتحكم في الاتجاهات المسموحة: **Issue Allowed** (إصدار لمخزن آخر) / **Receipt Allowed** (استلام من مخزن آخر) / **Receipt Return** — تُقرأ مع قيود نوع المخزن (Sub يستلم من Main فقط) لتشكيل **مصفوفة حركة داخلية كاملة** (راجع 05-business-rules BR-MG-03).
