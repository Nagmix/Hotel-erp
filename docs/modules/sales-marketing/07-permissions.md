# 07 — الصلاحيات (Permissions) — وحدة SLM

> **⚠️ الوحدة الوحيدة في 48 ملفاً مقروءاً بلا أي قسم صلاحيات موثق** — لا User Access، ولا Define Rights، ولا قائمة عمليات مقيَّدة. التوثيق الوحيد ذو الصلة: **قفل الهوية في Executive Planner** (سلوك حماية ضمني لا نظام صلاحيات).

---

## 1. ما هو موثق فعلاً (حماية الهوية الوحيدة)

| البند | النص الحرفي | الدلالة |
|---|---|---|
| **Executive Planner Login** | "This option is **password protected** and can be executed **only by sales executives who have been mapped to a user id** using the Map User Id option" (SLT §9) | حماية بيانات اعتماد SYS + شرط ربط Executive↔User |
| **تعميم الاختصاص** | "This option can be used either by Sales Executives or can be **activated for all Users defined in the system** based on the **INI Setting # 239**" (PRF §16) | مقبض نطاق الوصول الوحيد في الوحدة |
| **Blacklist: مصرّح فقط** | إدخال "the name of the **person who authorized** the blacklist" (PRF §7) | مساءلة فردية — لكن دون قيد صلاحيات رسمي |
| **Authorizer للإعلانات/الهدايا** | "Enter the Name of the **person who authorizes**" (SLT §7) | مساءلة موثقة داخل الصف |
| **logout صريح** | "This logs out the user that is logged into the Executive Planner" (SLT §9) | جلسة مستقلة داخل التطبيق (sub-session) |

## 2. المقارنة مع عائلة الصلاحيات في المشروع

| الوحدة | نمط الصلاحيات الموثق | SLM؟ |
|---|---|---|
| SYS | Define Rights (Group/User × Menu × Add/Modify/Delete) | ✗ لا يُذكر |
| POS/BNQ | User Access بقائمة عمليات (28 KOT/15 Settlement في BNQ!) | ✗ لا يُذكر |
| HRP | Payroll User Rights **لكل فئة صفّياً** (row-level!) | ✗ لا يُذكر |
| MEM/CARE/FAS/AR | صلاحيات موثقة بأنماط متفاوتة | ✗ لا يُذكر |
| **SLM** | **لا شيء — قيد كامل** | — |

> **الاستنتاج الموثق (GAP-SM-D04):** إما أن SLM ترث صلاحيات القوائم العامة من SYS حصراً (كل مستخدم له قائمة Sales & Marketing يراها!)، أو أن التوثيق أهمل القسم. **المرجح الأول** لأن نص PRF §16 يشير صراحة لـUser Setup تحت SYS — أي أن الوصول يدار من قوائم SYS فقط.

## 3. مخاطر الصلاحيات الكامنة (تحليل موثق المصدر)

| الخطر | السبب | الأثر |
|---|---|---|
| **Update Company Profile بلا حاجز** | أداة Old→New Value تعدّل بِنى أسعار **جماعياً** بلا معاينة ولا توثيق صلاحية | تغيير أسعار شركات بالجملة بخطأ واحد (R-SM-2) |
| **Transfer Prospects يفتح AR** | إنشاء Company Master = فتح حساب ائتماني | إدخال عميل بلا اعتماد مالي |
| **حدود الائتمان (Credit Limit) نفسها** | من يملك تعديلها غير موثق | تغيير القفل المالي BR-SM-01 بلا أثر مساءلة |
| **بيانات تنافسية حساسة** | Competitors في Prospects + Market Share | تسريب تجاري إن غاب تقييد القراءة |
| **Blacklist بدون دور** | سبب + مصرّح نصيان فقط | لا قيد على من يفعل |

## 4. قرار إعادة البناء (Permissions Specification)

1. **P-SM-1 — قياس الدور الرسمي:** إنشاء Roles: `Sales Manager` / `Sales Executive` / `Collection Executive` / `Sales Admin` — مع ربط `User↔Sales Person` (يعيد إنتاج Map Users/Sales Exec بأصل Frappe).
2. **P-SM-2 — صلاحيات مزدوجة القياس:** قراءة الموازنات/الأسعار/الأداة لكل فريق المبيعات؛ **الكتابة** (Company Profile المالي + Transfer + Update Company Profile) لـSales Manager/Admin فقط.
3. **P-SM-3 — Executive Planner:** افتراضياً owner-only (بيانات المندوب نفسه فقط) — يُعمم بقرار مركزي واحد (يعادل INI #239 بـrole setting قابل للتدقيق بدل INI خام).
4. **P-SM-4 — حقول مالية مقفلة:** Credit Limit/Interest %/Commission % — permission منفصلة `sales Credit Terms Edit` (لأن أثرها ثلاثي الوحدات).
5. **P-SM-5 — مسار تدقيق:** كل Update Company Profile / Transfer Prospects / Blacklist = Version Log (نمط Payroll Audit الموثق في HRP-REP).

> **قاعدة ذهبية مستخلصة:** غياب التوثيق ≠ غياب الحاجة — هنا يُستكمل بحسب مبدأ "الأثر المالي يستوجب صلاحية" المكرس في 7 وحدات سابقة.
