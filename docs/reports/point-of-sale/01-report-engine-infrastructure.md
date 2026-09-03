# 01 — محرك التقارير والبنية التحتية (POS-REP)

> البنية المشتركة التي يقف عليها كل تقارير المنافذ الـ59: مصفوفة POS Report Options · قنوات الإخراج · Port ID · مراجع الزمن · خيارات الصفحات.

---

## 1. مصفوفة POS Report Options (النمط الأول من نوعه)

**الإجراء الموثق** (يتكرر حرفياً في ~15 موضعاً):

> "If you want to include Void and Complimentary sales in the report, you have to select the Void and Complimentary options for this report in SETUP. Under SETUP, double-click **'POS Report Options'**. In the POS Report Options screen select the Void and Complimentary options corresponding to **<اسم التقرير>** and click Save."

### 1.1 الدلالة المعمارية

| البعد | القيمة |
|---|---|
| نوع النمط | **Config-per-Report** — إعداد لكل تقرير على حدة (وليس مفتاحاً واحداً للوحدة) |
| موضع الإعداد | SETUP → POS Report Options (شاشة مصفوفة: تقارير × خيارات) |
| الخيارات الموثقة | Void · Complimentary (لكل تقرير checkbox مستقل) |
| التقارير المرتبطة (مذكورة صراحة في REP) | Sales By Item · Sales Daybook · Sales Daybook by Date · Weekly Manager Report · Sales by Table · Sales By Open Item · User Defined Sales Report · Settlement by Bill# · Settlements by Date · Cashier Summary · Cashier Summary (Group) · Cashier Report (By Type) · Discount Register (6.1) · Discount Summary · Discount Summary (Reason) · Popularity Analysis · Popularity Report (Time) · KOT Details · Tax Register (16.1/16.2/16.3) · Cover Analysis = **~20 تقريراً** |
| التقارير ذات الـcheckbox المباشر في شاشة التشغيل | 1.4 (Include NC KOTs/Void/Compl. inline) · 1.5 · 1.8 · 1.11 · 1.13 · 1.14 · 5.1 · 16.1(inline أيضاً!) · 16.5 · 22 = **مساران متوازيان لنفس الغرض** |

### 1.2 الثابت الحرفي (Invariant)

> "The Void and Complimentary sales **details will appear** in the report but the sales amount will **NOT be included in the grand total**."

- الفاتورة Void تُعرض (بعلامة `(V)` بجوار رقمها) لكن لا تدخل الإجمالي الكلي — **ظهور بلا احتساب**.
- الفاتورة Complimentary كذلك بعلامة `(C)` — مثال حرفي في Sales Daybook: **"974(V)"**.
- عدد مرات تكرار الجملة في الملف: **~25 مرة** — أعلى تكرار لجملة قاعدة واحدة في ملفات الحزمة كلها.

### 1.3 قراءة معمارية

المصفوفة تجعل Void/Complimentary **قرار تقاريري لكل تقرير** وليس قرار تشغيل (الذي يحسمه POS-SET §18 "list these cautiously" — راجع R-POS في 08-reports.md للوحدة). عند التنفيذ: **Report Options** لكل تقرير (Custom Field على إعدادات التقرير) بدل مصفوفة INI.

## 2. قنوات الإخراج (4+1)

| القناة | الشاهد الحرفي | التقارير الموثقة بها |
|---|---|---|
| **Display** | "Select one of the report output options (Display, Spool, Print or Export)" | 1.15 · 1.16 · 7.1 (+ إنفاق R-POS-09 من SET) |
| **Spool** | نفس الجملة | نفسها |
| **Print** | نفسها + Print/Preview في §10 | 1.15 · 1.16 · 7.1 · 10 |
| **Export** | نفسها — **بلا صيغة موثقة** (امتداد عائلة UNK-081 من FO) | نفسها |
| **Port ID** (خامسة ضمنية) | "Select the Port ID from the Port ID dropdown list to select the printer" | 1.5 · 5.3 · 5.4 — **POS وحدها** لديها اختيار طابعة داخل شاشة التقرير |

**أزرار الطباعة في §10 (Re-print POS Bill):** Preview (عرض بلا طباعة) → Exit → Print على "local or network printer configured" — ثلاث خطوات غرضية بدل قناة واحدة.

## 3. مراجع الزمن الثلاثة (الميراث من FO)

| المرجع | الاستخدام في POS | أمثلة |
|---|---|---|
| **Accounting Date** | المرجع الغالب (~30 تقريراً) | 1.1 · 1.4 · 1.6 · 2 · 3 · 5.1 · 6.x · 11.x · 16.x · 17.x · 21 · 22 · 23 |
| **Server Date** | نادر — تقريران | 1.2 Sales Daybook · 1.3 Daily Sales |
| **Current Date** | ~10 تقارير | 1.7 · 1.13 · 1.16 · 5.6 · 7.x · 12 · 13 · 17.4 |
| **Month/Year** (رابع خاص) | التقرير الشهري للتوصيل | 7.3 (≤ Current Month/Year) |

**اللافتة الصارمة في §3:** "The date entered should be **less than** the Accounting date" — **أقل строгоً** (وليس ≤) — التقرير الوحيد بصيغة الاستبعاد الصارمة للتاريخ نفسه.

التفاصيل الكاملة (same-month · ≤7 أيام · ≤30 يوماً · المستقبل المسموح في 19) → `10-date-validation-matrix.md`.

## 4. خيارات الصفحات والتجميع

| الخيار | الوظيفة | التقارير |
|---|---|---|
| **Skip Page Required / Page Skip Required** | كل منفذ يبدأ صفحة جديدة | 1.2 · 2 · 3 · 16.2 |
| **Print Consolidated** | نسخة مجمعة | 5.1 |
| **Print Day Total** | إجمالي المنفذ/نوع القائمة — **يتعطل مع تعدد الاختيار** ("If you select multiple outlets/menu types this option will not be available") | 1.1 |
| **Session Breakup / Item Consolidation / Require Group Total** | تفكيك الجلسة/دمج الصنف/إجمالي المجموعة | 1.1 |
| **Print KOT Total** | إجماليات KOT داخل تقرير NC | 11.2 |
| **Server Summary** | ملحق تفصيل النُدُل | 5.6 |
| **Print Item Value** | قيم الأصناف (بدونها كميات فقط) | 1.5 |

## 5. حقول المساعدة (Help) الموثقة في REP

| الحقل | الآلية | التقرير |
|---|---|---|
| Menu Master list | نقرة مزدوجة في Start/Ending Item | 1.1 |
| Shift Help | F1 أو نقرة مزدوجة | 5.2 |
| Currency Help | نقرة مزدوجة في Cur | 5.5 |
| Customer Id Help | F1 أو نقرة مزدوجة — **"system generated when a customer places an Order for delivery"** | 7.2 |
| Loyalty Card Help | نقرة مزدوجة في CARD# | 8 |
| Bill# Help | نقرة مزدوجة — **تتكيف مع وضع البحث** (Specific Date → فواتير اليوم · Month & Year → فواتير الشهر كاملة) | 10 |

## 6. التبعيات الإعدادية (Setup Gates)

| التبعية | النص الحرفي | الأثر |
|---|---|---|
| **DSR Session Group** | "In SETUP, DSR Session Group has to be defined for this option to work" | DS Report (1.6) لا يعمل بدون تعريف تجميعات الجلسة (Breakfast/Lunch/Dinner ← جلسات فعلية) — موثق في POS-SET §36 |
| **POS Report Options** | §6.1/§1.1/… | مصفوفة Void/Comp (أعلاه) |
| **Sales Report Definition** | "You can define the sales report using Sales Report Definition under Setup" | User Defined Sales Report (1.16) — POS-SET §16 (7 أنواع أعمدة) |
| **INI Switch 137** | "This is affected by Switch 137" | Print PAN Information (9) — عتبة طلب PAN |
| **INI Switch 335** | "F&B Factor % defined in INI switch no 335" + معروض في شاشة التقرير | Menu Engineering (22) — عامل تصنيف MM Class |

## 7. ما يميز بنية POS-REP عن FOM-REP

| البعد | FOM-REP | POS-REP |
|---|---|---|
| توحيد قنوات الإخراج | رباعي معلن في التعريف الرسمي (135 تقريراً) | رباعي موثق في 3 تقارير فقط + Port ID (خامسة) في 3 أخرى — **توثيق أرق لكن نفس المعجم** |
| طبقة التخصيص | Report Designer + IDS Crystal في TOC (UNK-078) | User Defined Sales Report **بحرارة تعريف كاملة** من SET (لا شبح) |
| مفاتيح INI | 63 (playlist) | **137 + 335** (عتبة قانونية + عامل تحليلي) |
| ملفات على الخادم | PMSPOL.INI → POL.SPC | لا شيء — POS نظيفة ملفياً |
| دفتر ورقي جنائي | — | KOT Books Usage (17.1) — كتيّبات مرقمة تُدار كأصل مادي |
