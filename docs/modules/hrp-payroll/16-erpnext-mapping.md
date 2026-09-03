# 16 — الإسقاط إلى ERPNext/Frappe (ERPNext Mapping) — وحدة HRP

> **F-HR-1..12** — قرارات معمارية + Seed Mapping إلى Frappe HRMS.

---

## A. القرارات المعمارية (F-Decisions)

### F-HR-1 — محرك أجور مخصص فوق Salary Structure ⭐
**المشكلة:** ED Calculation (معادلات tokens + 4 مصادر + شرائح 4 أنواع + تراكم 3 أنواع + Priority/Partial/CarryForward + Take Home% + Specific Months + Special Program) أوسع بكثير من Salary Component/Formula القياسي.
**القرار:** Salary Structure يستوعب الهيكل والمكونات؛ ويُبنى **Payroll Engine Extension** (Python) ينفذ: جدول شرائح مخصص (doctype ED Slab بأربعة modes) + مصدر Accept (wizard) + منفذ معادلات آمن + سمات Priority/Partial/CF على Deduction rows. **الشرائح الإجرائية تُنفَّذ برمجياً لا بـ flexi**.
**الأثر:** أصل مخصص قابل للاختبار وحدةً (unit-testable) — متطلب قبول AC-01.

### F-HR-2 — Payroll Run Wizard بحقوق ديناميكية
**المشكلة:** ACCEPT يظهر أثناء الاحتساب (شاشة إدخال للفئة).
**القرار:** Payroll Entry → خطوة "Accept Values" قبل التنفيذ (قائمة ED ذي calc_from=Accept) ثم تشغيل غير متوقف. **لا توقف منتصف المعالجة**.

### F-HR-3 — Statutory كطبقة قابلة للتهيئة جغرافياً
**المشكلة:** PF/ESI/PT/LWF هندية-مدمجة (PYINDSP "only for Indian clients" + "as per government norms" + نماذج رسمية).
**القرار:** doctype **Statutory Rule Set** (country-scoped) + طباعة النماذج كـ print formats مخصصة قابلة للتمكين حسب الدولة. المنصة العربي-أولاً تشحن مجموعة GOSI/مكافأة نهاية الخدمة السعودية-اليمنية لاحقاً من نفس البنية.

### F-HR-4 — AR→Payroll عبر Additional Salary
**المشكلة:** خصومات AR للموظفين تُستورد وتخصم في الدورة.
**القرار:** hook على Sales Invoice لموظف → إنشاء **Additional Salary** (deduction) مرتبطاً بالدورة التالية. يستكمل الحلقة الرابعة (POS→AR→HRP).

### F-HR-5 — Take Home % كقاعدة معالجة
**القرار:** حقل على Employment Type/Category + منطق clamp في المحرك (F-HR-1) — **غير موجود قياسياً**.

### F-HR-6 — إيقاع الدورة لكل فئة
**القرار:** Salary Structure frequency + Payroll Entry per group — قياسي HRMS يستوعب Monthly/Weekly/Fortnightly/Daily (ب Starting Period متدحرج عبر-subscription).

### F-HR-7 — Attendance من Employee Checkin
**القرار:** flat file يُستبدل بـ Employee Checkin + Biometric connector (shift assignment) — ملف PYATYYMM.DAT يبقى فقط كاستيراد ترحيلي (migration adapter).

### F-HR-8 — تقرير كسر النقد (Denomination)
**القرار:** report view مخصص يقرأ currency denominations settings — للفنادق التي تصرف نقدياً (شائع!).

### F-HR-9 — F&F مباشر من HRMS
**القرار:** Full and Final Statement القياسي يغطي (شطب مستحقات/إجازة غير مستخدمة/تعويض) — **إسقاط مباشر عالي الجودة** + Indemnity كأداة حساب (تنبيه: صيغ التعويض تختلف جغرافياً — طبقة F-HR-3).

### F-HR-10 — Audit بالـ Versioning
**القرار:** Frappe Version/Activity Log + report "Payroll Changes" (old/new) — يطابق REP §19.

### F-HR-11 — Payroll User Rights → User Permissions
**القرار:** User Permission على Employee Group/Category — قياسي Frappe — يمنح row-level أمن مطابقاً للأصل.

### F-HR-12 — Recruitment من Job Applicant/Offer القياسي
**القرار:** RQP يطابق Job Opening→Applicant→Interview (Interview app?)→Offer (ب Salary Template → **custom field salary structure preview**) — توافق ممتاز.

## B. Seed Mapping (كيان → Doctype)

| HRP الأصلي | ERPNext/HRMS | الجودة | ملاحظات |
|---|---|---|---|
| Employee (+EMP# 7) | Employee | 🟢 عالية | recode map للترقيم |
| Candidate/Application | Job Applicant | 🟢 | الحقول الديموغرافية configurable |
| Offer Letter | Job Offer | 🟢 | + Template preview |
| Job Requirement | Job Opening | 🟢 | |
| Salary Template | (custom) Salary Structure Template | 🟡 | doctype بسيط أو Template |
| ED Code | Salary Component | 🟡 | + ED type mapping: Earning→Component؛ Loan Deduction→deduction + loan link؛ **Number Deduction → statutory accounts** (statutory_domain field!)؛ Temporary → **exclude_from_total**؛ Cumulative YTD → **statistical component** |
| ED Calculation | (custom) ED Formula + ED Slab | 🔴 مخصص | F-HR-1 |
| Category | Employment Type + custom fields | 🟡 | cal_method/takehome/round |
| Starting Period | Payroll Period + frequency | 🟢 | متدحرج عبر Periods |
| Attendance Entry | Attendance | 🟢 | نصف يوم قياسي |
| Attendance Interface | Employee Checkin + connector | 🟢 | استبدال معماري |
| Payroll Processing | Payroll Entry | 🟢 | + wizard F-HR-2 |
| Payslip | Salary Slip | 🟢 | + Accept values injection |
| Payroll Transaction | Additional Salary | 🟢 | متغيرات موجبة/سالبة |
| Supplementary | Additional Salary (statutory) | 🟡 | خارج الدورة |
| Leave Master/Transaction | Leave Allocation/Application/Ledger | 🟢 | + carry-forward قياسي |
| Leave Group/Details | Leave Policy + Leave Period | 🟢 | INI 220 يلغى (ممكن دائماً) |
| Loan | **Employee Loan (HRMS)** | 🟢 | الأصل مقفل عبر submit/cancel semantics |
| Loan Return | Additional Salary repayment | 🟡 | سلوك custom |
| Bonus Period/Run | Additional Salary bonus batch | 🟡 | 4 نسب منطق مخصص |
| AR Transfer | F-HR-4 hook | 🔴 مخصص | |
| F&F | Full and Final Statement | 🟢 | Indemnity طبقة جغرافية |
| Denomination | (custom) Cash Denomination Report | 🔴 مخصص | F-HR-8 |
| PF/ESI/PT/LWF | Statutory Rule Set (custom) + print formats | 🔴 مخصص | F-HR-3 |
| HOD | Department head (قياسي) | 🟢 | |
| Staff Budget | (custom) Staffing Plan — **موجود في HRMS!** | 🟢 | Staffing Plan/Detail يطابق |
| Costing Group | Cost Center mapping | 🟢 | |
| Bank/Branch | Bank/Account | 🟢 | |
| UDR | Report customization | 🟡 | Query Report builder |
| Print Forms | Print Format (custom HTML) | 🟢 | بدل مصمم stationery |
| Payroll Audit | Version + Activity Log | 🟢 | F-HR-10 |
| User Rights | User Permission | 🟢 | F-HR-11 |

## C. مؤشر جاهزية الإسقاط

| الفئة | العدد | النسبة |
|---|---|---|
| 🟢 مباشر/قياسي | 24 | 55% |
| 🟡 تخصيص خفيف | 10 | 23% |
| 🔴 بناء مخصص | 9 | 21% |

> **الخلاصة:** التوظيف/الإجازات/الرواتب الأساسية/القروض/التسوية النهائية/الأمن — إسقاط ممتاز قياسي. المحرك الحسابي العميق (شرائح/تراكم/أولويات) + الإجرائية الهندية + AR-hook + كسر النقد = **أربعة أصول برمجية مخصصة يجب التخطيط لها مبكراً**.
