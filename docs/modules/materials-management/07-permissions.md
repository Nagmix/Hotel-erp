# 07 — الصلاحيات والتفويض (Permissions) — وحدة Materials Management

> أغنى وحدة في أنماط الصلاحيات المتخصصة: **4 أبعاد وصول + 3 مستويات تفويض مستندي + بوابة إصدار بالمخزون** — طبقة فوق النموذج المظلي SYS (راجع system-setup/07-permissions.md).

---

## 1. نموذج الوصول الرباعي (MGT Access Rights)

**المصدر:** MGT-SET §24 ص61-65.

| البُعد | النطاق | الآلية | نظير Frappe |
|---|---|---|---|
| **Store** | مستخدم × مخزن | اختيار اسم + مخزن → Confirm | Custom multi-select على User (`allowed_stores`) + فلترة كل شاشات المخزن |
| **Option** | مستخدم × **وظيفة داخل الوحدة** | "Double-click on the Access Rights column corresponding to the appropriate function... **F2 لتبديل الكل**" | Role Permissions على DocTypes الوحدة (لكل وظيفة ≈ DocType — F-SYS-9) |
| **Department / Cost Centre** | مستخدم × قائمة أقسام/مراكز | "Double-click on the **Authorized column**" | Dimension filters (Accounting Dimension + User Permission على Cost Center) |
| **Backdate Trn. Access** | مستخدم × **نوع معاملة × عدد أيام** | "Enter the **No. of Days**" لكل نوع | **لا نظير قياسي** — قرار F-MG-4 (حقل + تحقق server-side بتاريخ المستند) |

> **التقاطع مع النموذج المظلي:** هذا النموذج يعمل **تحت** SYS User Access (وحدة Materials Management في الشجرة × Add/Modify/Delete) — أي أن الوصول للوحدة يمنح من SYS، ثم **نطاقها الداخلي** يضبط هنا — نفس عائلة POS Restrict Outlet / AR Transaction Types.

## 2. التفويض المستندي (Authorization 1/2/3)

**المصدر:** DNT §1 ص5-7 + §2 ص15 + §3 ص21 + LUK §4.

### 2.1 مصفوفة التفعيل

| المستند | المستوى 1 | المستوى 2 | المستوى 3 | مفتاح التفعيل |
|---|---|---|---|---|
| Purchase Requisition | ✓ | ✓ | ✓ | **INI 355 INVPURREQAUTHORISATION** = 1/2/3 (قيمة متدرجة!) |
| Indent | ✓ | ✓ | — | INV #6 / INV #7 (مفتاحان ثنائيان) |
| Purchase Order | ✓ | ✓ | ✓ | INV #13 / INV #14 / INV #298 (ثلاثة مفاتيح مستقلة!) |

> **نمطان مختلطان للوظيفة نفسها:** PR يستخدم **مفتاحاً واحداً متدرج القيمة**؛ PO يستخدم **ثلاثة مفاتيح ثنائية مستقلة** — [UNCERTAIN] تعارض تصميمي داخلي؛ للتنفيذ الجديد نعتمد النموذج المتدرج الأنظف (قرار F-MG-3).

### 2.2 القواعد الحاكمة

1. **حاجب الإصدار:** "If authorizations are not made, **requisition issues are not allowed**" — التفويض شرط تشغيلي لا شكلي.
2. **التسلسل الإلزامي:** "Level one authorization... is **mandatory before receiving the Level 2**".
3. **مسؤول التفويض موثق بالاسم:** "The Requisition that is generated has to be approved by an authorized person for e.g. a **Store Manager**. This enables you to have control over the goods that are purchased and thereby **restricts unnecessary accumulation or misuse of stock balance**" (DNT ص5) — الغرض الرقابي منصوص.
4. **التدقيق:** Lookup Authorization Details يعرض تفويضات PO/PR/Indent (تاريخ أو رقم) — سجل مساءلة جاهز.

## 3. قواعد امتداد من الوحدات الأخرى (تطبق على MGT)

| المصدر | القاعدة الممتدة |
|---|---|
| SYS Supervisor | علم Supervisor = "total access to all menu items" — يتجاوز كل القيود أدناه |
| SYS User Access | منح/منع Materials Management كوحدة + Add/Modify/Delete لكل عنصر قائمة فيها |
| SYS Report Restrictions | Spool/Export/Format لكل تقرير من تقارير MGT |
| SYS Module Attributes | مفاتيح INV (كل سلوك التفويض أعلاه) |

## 4. سيناريوهات صلاحيات موثقة

| السيناريو | التسلسل | الأثر |
|---|---|---|
| أمين مخزن فرعي | Store = مخزنه فقط + Option = Transactions + Backdate = 0 | يعمل داخل نطاق ضيق بلا رجعية |
| مسؤول مشتريات | Option = PR/PO/Quotation + Dept/CC = المشتريات + Backdate = N أيام | دورة شراء كاملة بنافذة تصحيح محدودة |
| مراقب تكاليف (شهر) | Store = الكل + Option = Physical/Variance/Ledger + Backdate = أيام الشهر | إغلاق شهري فقط |
| Store Manager (مفوِّض) | Authorization One لكل PR/Indent/PO | بوابة المستوى الأول |

## 5. قرارات التنفيذ المسجلة هنا (تفصيل 16-erpnext-mapping)

- **F-MG-3:** توحيد نمط التفويض المتدرج (قيمة 0-3) لكل مستندات المشتريات في `Hotel Feature Toggle` — إسقاط ازدواجية INV #13/#14/#298.
- **F-MG-4:** `custom_backdate_days` (JSON: نوع المعاملة → أيام) على User/Role + تحقق `validate()` في كل DocType معاملة — إحياء البعد الرابع.
- **F-MG-9:** صلاحيات المخزن = User Permission على **Warehouse** (Frappe) — مطابقة شبه مباشرة للبُعد الأول.
