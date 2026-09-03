# 00 — نظرة عامة على طبقة تقارير Financial Management (Phase 7 — 4/4 — **خاتمة الحزمة 65/65**)

> **المصدر:** FAS-REP (64 ص / 858 سطر — أصغر ملفات REP الأربعة الكبرى، لكنه **الأغنى قوانين معمارية**).
> **الموقع في المشروع:** يُكمل — ولا يكرر — `docs/modules/financial-accounting/08-reports.md`.

---

## 1. النطاق والإحصاء

| البند | القيمة |
|---|---|
| ملف المصدر | `FN6i-NT-FAS-REP.txt` (64 ص) |
| أقسام مرقّمة | **34 قسماً** (1–34) |
| بنود TOC غير مرقّمة | **6**: تحت §25 (TDS Details · Invoice/Payment Check · Advance Paid) + تحت §34 (Bank Payment · **IDS Crystal Report Designer** · **Advice/Cheque iDesigner**) |
| تقارير الأوراق الموثقة الجسم | **46 تقريراً** (34 − 4 آباء [4 Day Book · 5 Ledger Bal · 7 P&L · 9 TB · 34 User Reports] + عائلاتها [Day Book ×3 · LB ×2 · P&L ×2 · **TB ×4**] + 6 غير مرقمة − Bank Payment تحت 34) |
| **أشباح ختامية** | **2 — يُغلق بهما الملف**: IDS Crystal Report Designer + Advice/Cheque iDesigner (بنود TOC بلا جسم إطلاقاً) → **UNK-096** — **IDS Crystal شبح متكرر عبر الوحدات** (نفس الاسم ورد شبحاً في FOM-REP — UNK-078!) |
| أضخم عائلة | **TDS الهندي: 7 تقارير** (Details + 16A/26J/27/26A/26C/26K) |
| عائلة القوائم المالية | P&L ×2 + BS + **Trial Balance ×4** = 7 |
| إجمالي بنود TOC | **48 بنداً** (46 + شبحان) |
| التعريف الرسمي | "Reports under Financial Management Module is used by Users to generate various reports relating to **Ledger Balance, Profit & Loss, Balance Sheet, statements of accounts, purchase and expense registers** etc." (REP ص3) |

## 2. لماذا هذا الملف "الأثقل قوانين" رغم صغره؟

خمسة قوانين معمارية كبرى لا توجد في أي ملف REP آخر:

1. **قانون طبقة النزاهة التكاملية (§19/20)**: تقارير **Unlinked/Linked Account Codes** تُدقّق اكتمال جسور FO→FAS وPOS→FAS والضرائب الشرائية والموردية — حرفياً: "Using this list, you can define Account Heads accordingly so that all figures related to Sales (Income) and Purchase Journals are **accurately reflected in the General Ledger**" — **أداة تشغيلية لضمان سلامة الترحيل التلقائي** (يغلق عملياً عائلة أسئلة جسور F من جهة المستهلك).
2. **قانون الترحيل التلقائي الموثق (§21 Auto Posted)**: "transactions that are auto posted from other modules i.e., **Front Desk, Point of Sales, Accounts Receivable, Materials Management** etc" — بأنواع **FOM / ACR / INV** — **خريطة مصادر الترحيل الآلي الرسمية الوحيدة في الحزمة** (وفاجعة: **لا HRP بينها!** → UNK-098).
3. **قانون Print Forms (3 تقارير إضافية)**: Balance Confirmation (§14: "customized format... define the relevant **Program ID**... in the Print Forms option") + Advice/Cheque (§24) + Voucher Print (§25: program IDs **"specified against the Transaction Codes in the Transaction Types parameter"") — بمجموع Print Forms الحاكم يبلغ **6 تقارير عبر MGT+FAS** + نمط تسجيل ثانٍ (ضد Transaction Codes لا قائمة مستقلة!).
4. **قانون قنوات الإخراج الأغنى**: Print/**Email**/**Spool** (16A — مع Spool بملف اسم صريح!) + **Excel** (User Reports §34: "Direct or Excel") + **80/132** (Auto Posted §21 وTB F2) — **FAS تملك 5 قنوات إخراج موثقة** — أوسع من FO (4) وPOS (4+Port) — وMGT (صفر إلكتروني) تبدو أكثر شذوذاً.
5. **قانون مسار البريد الموثق بالعتاد**: 16A بالإيميل يتطلب "**Microsoft Outlook and Broadgun PDF printer should be installed and Broadgun PDF printer should be set as default printer**" + PDF Settings "highlighted in red" — **البنية التحتية البريدية الوحيدة الموثقة بمنتَجين تجاريين بالاسم** في الحزمة كلها.

## 3. العائلات الموضوعية (خريطة الكتالوج)

| العائلة | البنود | عدد | ملف التوثيق |
|---|---|---|---|
| محرك التقارير والبنية التحتية | Print Forms ×3 + Tag/Load + F1/F3 + 5 قنوات | — | `01-report-engine-infrastructure.md` |
| دليل الحسابات واليوميات | 1, 2, 2(2), 3, 4 (×3) | 7 | `02-chart-ledger-daybooks.md` |
| الأرصدة والدفاتر | 5 (×2), 6, 17 | 4 | `03-ledger-balance-gl.md` |
| القوائم المالية | 7 (×2), 8, 9 (**TB ×4**) | 7 | `04-financial-statements.md` |
| سجلات الدائنين والمشتريات والمصروفات | 10, 11, 12, 13, 15, 16 | 6 | `05-creditors-purchase-registers.md` |
| **طبقة النزاهة التكاملية** | 18, 19, 20, 21 | 4 | `06-integration-link-reports.md` |
| المصرفية والشيكات | 23, 24, 25, 32, Bank Payment | 5 | `07-banking-cheques-pdc.md` |
| **جناح TDS الهندي + التأكيدات** | TDS Details + 26-31 + 14 | 8 | `08-tds-statutory-forms.md` |
| التدقيق والتقارير المخصصة | 33, 34, 22, Advance Paid, Invoice/Payment | 5 | `09-audit-user-reports.md` |
| مصفوفة قواعد التواريخ | — | ~22 قاعدة | `10-date-validation-matrix.md` |
| التحويل والفجوات | F-FA-1..16 + GAP + AC | — | `11-erpnext-mapping-gaps.md` |

## 4. أبرز الاكتشافات البنيوية (Session 18 — ختام)

1. **Trial Balance رباعية** (§9): TB عادي + Format 2 + **(3.3)** + رابع بتسلسل طباعة Sub group/Department/Cost Center — والأوصاف **حرفياً متطابقة ثلاث مرات** (TB/F2/3.3 — "Fill in all the fields as explained in the section Trial Balance Format 2" إحالة ذاتية!) → عائلة "Format 2" تنضم لR2 في MGT: **لاحقة التخطيط عابرة للوحدات** (MGT R2 · FAS Format 2 ×3 + (3.3)).
2. **XOR جديد في TB Format 2**: "Select **any one** option from **Zero balance or Print 132 Column**" — اختيار واحد إجباري بين إظهار الأصفار والطباعة العريضة (في FO/POS كان 80/132 محوراً مستقلاً).
3. **مثال مصرفي حرفي كامل** (Day Book Format 2 — ص12): "Account Head **A008000 (SBI Frankfurt** has a debit balance of US$ 1000 and a Receipt of US$ 500 (received from Debtors)..." — **الكود المصرفي الوحيد المسرب في الحزمة** + شرح Contra بعملية كاملة.
4. **P&L بأربع فترات**: "for the **month, year to date, and for the previous year** along with total amount" (PL by CC/Dept) — أوسع مقارنة زمنية في قوائم الحزمة.
5. **قصة Contract Debit كاملة** (§15/16): عقد بسعر ثابت → تقلب سعر/عجز مورد → شراء من السوق → **فرق السعر يُحمَّل على مورد العقد بمذكرة خصم** — ثم "deference value" (خطأ مطبعي لdifference!) بأعمدة: GRN number/date + debit value + **waive amount** (إسقاط جزء من الفرق!).
6. **نمط Tag/Load ×4**: Debit Note + Advice/Cheque (**Un Tag / TagAll / Un TagAll أزرار!**) + Voucher Print (**Toggle Tag**) + User Reports — بعد MNT (Job Order Generation): **عائلة Tag-YES عابرة للوحدات مؤكدة** (MGT §17 Load أيضاً).
7. **Voucher Print يسجل برامجه ضد Transaction Codes** (في Transaction Types parameter) — نمط تسجيل Print Forms **ثانٍ** مختلف عن MGT (القائمة المستقلة).
8. **Pending Receipts for PJV (§18)**: GRNs غير المرحّلة لقسيمة مشتريات + **Regular or Service PJVs** + **Misc. Supplier Group Summary** — يوثّق أن PJV **نوعان** (عادي/خدمي) وأن الموردين المتنوعين لهم تجميع خاص.
9. **Bank Reconciliation كعملية-تقرير**: Realized (نطاق تواريخ تحقق) مقابل Unrealized (**"Balance As Per bank Statement" يُدخل يدوياً!**) + "This forms the basis for reflection in the Bank Reconciliation **Query / Report options**" — ثلاث أدوات (عملية + استعلام + تقرير).
10. **Advance Paid Report** — "advances paid by the **guests**" — المالية تُقرر تقرير ضيوف! (جسر FAS→FO لإيداعات الضيوف).
11. **PDC Check List (§32)**: Post-Dated Cheques بثنائية **PDC Receivable (من المدينين) / PDC Payable (للدائنين)** — دورة حياة شيكات مؤجلة كاملة داخل FAS.
12. **Audit Trial ببعدي توقيت**: Transaction Date (الأول فقط) **أو** Updated Date (التعديلات/الحذف) + خيارا Modified **and/or** Deleted — أدق ضبط مدى تدقيقي في الحزمة (مع MGT §23 — نفس "Trial" الإملائية الخاطئة!).
13. **User Reports = مولد قوائم مخصصة**: من Create User Report (Setup) + **مصفوفة قيم العرض**: "absolute/round off/**(-ve) print in bracket**/include opening Balance/**Lakh/Million** or Decimal" + **Direct أو Excel** — أعمق تحكم عرض رقمي في الحزمة (علامة Lakhs الهندية تصل للتقرير النهائي).
14. **F1/F3 بمعانٍ ثابتة**: F3 = **Financial Year** help · F1 = الكيان (Account/Vendor/SL/Certificate) — أدق دلالة مفاتيح موحدة في وحدة واحدة.
15. **Form 16A بحقبة كاملة**: New/**Reprint** + Ack Num بأربعة أرباع سنة (رقم إشعار + cheque/DD لكل ربع) + Height **11 أو 12 IN** + Email/Spool/Print — **أكمل مواصفة نموذج ضريبي واحد في الحزمة**.
16. **Form 26J = Royalty**: "26J is a TDS Form pertaining to **Royalty**. It is an **annexure of Form 16A**" — علاقة تبعية نماذج موثقة.

## 5. علاقة هذه الطبقة بالوحدات الأخرى

| الجسر | الاتجاه | الشاهد |
|---|---|---|
| **FAS ← FO/POS** | ترحيل آلي | §21 Auto Posted (Type FOM = "Front Desk **and Point of Sale**") + §19 Unlinked (FO/POS Revenue/Item Groups) |
| **FAS ← ACR** | ترحيل آلي | §21 (Type ACR) + §10 Creditors (وجه الدائنين) + §14 Balance Confirmation (رسائل مدينين/دائنين) |
| **FAS ← MGT** | ترحيل آلي + مستندي | §21 (Type **INV**) + §18 PJV (GRN→قسيمة مشتريات) + §24 Advice (دفع الموردين) + Print Forms المشترك + §16 (GRN في أعمدة Debit Note) |
| **FAS ← HRP** | **غائب!** | لا نوع HRP في §21 — الترحيل الرواتب غير ممثل (UNK-098 — يلامس UNK-010 القديم) |
| FAS ← FO (ضيوف) | تشغيلي | Advance Paid (إيداعات الضيوف) |
| FAS ↔ FXD | موازنات | §22 FA Budget List (موازنة الأصول من Budget Account Codes) |
| FAS ↔ SYS | طباعة/بريد | Print Forms (§14/24/25) + Printer Settings (§25 — "All printer definitions through the **Printer Settings**") + Outlook/Broadgun (16A) |

## 6. ملاحظات الجرد (FAS-REP)

- **أعلى كثافة F-keys**: F1/F3 في 12+ موضعاً بدلالات ثابتة.
- **أخطاء تحريرية**: خطوة "8" بين 1 و3 في Voucher Print (نسخ/لصق) · "deference value" (16) · "continues" بدل continuous (24/25) · أوصاف TB الثلاث المتطابقة.
- **أضخم عتبات تحقق**: "Above"/Minimum Amount في Expense Register وDetail Register — فلاتر عتبة مبلغية (مقابل عتبات زمنية MGT).
- **كل تخطيطات المخرجات غائبة** كالعادة (الصور) — لكن FAS يعوّضها بأمثلة نصية (A008000) ومصفوفات أعمدة موصوفة (§16 Debit Note List يسرد أعمدته كاملة!).
- **الختام المزدوج**: آخر سطرين في TOC = شبحان — الحزمة تُغلق كما فتحها POS-KDS: **بنود مطموعة بلا جسم** (IDS Crystal في FO وFAS — عائلة TOC-template مشتركة تكاد تكون مثبتة).
