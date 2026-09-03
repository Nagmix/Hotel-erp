# 12 — التكاملات (Integrations) — وحدة HRP

> **I-HR-01..16** — مع جسر AR العكسي الموثق حديثاً وتحديث Knowledge Graph.

---

## A. تكاملات موثقة نصاً

| # | التكامل | الاتجاه | النص/القرينة | التصنيف |
|---|---|---|---|---|
| **I-HR-01** | **AR → Payroll Transfer** | AR→HRP | "the amount has to be charged to the payroll, then it goes to the accounts receivable... transferred to the Payroll so that the relevant amount is deducted from the employee's pay" + ربط company code (PNT §22) | **جسر عكسي جديد — يُرسم في KG** |
| **I-HR-02** | RQP → Personnel Master | داخلي | "Details of the candidate who has accepted the offer will be displayed" + Salary Template عند العرض (PNT §1 + RQP §7) | أتمتة |
| **I-HR-03** | Payroll → Finance | HRP→FAS | الرابط السادس من روابط FAS-SET الستة | ترحيل |
| **I-HR-04** | Attendance Device → HRP | خارجي→HRP | Flat file PYATYYMM.DAT (PMS\Interface) — "[Applicable to Fortune Enterprise Only]" | واجهة ملف |
| **I-HR-05** | HRP → البنوك | HRP→خارجي | Branch folio + Challans (Cheque/Draft بتفاصيل) + Statements Transfer | صرف |
| **I-HR-06** | SYS → HRP (بنية) | SYS→HRP | Properties + Round Off الثلاثي المتطابق + Users + Print Forms | بنية |
| **I-HR-07** | HRP ↔ BNQ | ثنائي | Banquet Staff + Service Managers ككيانات موظفين (BNQ-SET) + Pre Costing labor؟ [UNCERTAIN — BNQ يوثق الموظفين لا تكلفتهم من HRP] | مرجع |
| **I-HR-08** | POS → (AR) → HRP | عبر AR | POS Staff Settlement → AR → I-HR-01 (حلقة مغلقة) | حلقة |
| **I-HR-09** | FO → (AR) → HRP | عبر AR | FO Paid Out للموظفين بنفس النمط | حلقة |

## B. تكاملات مستنتجة (عالية الثقة — تُتحقق في مرحلة لاحقة)

| # | التكامل | الدليل الاستنتجي |
|---|---|---|
| I-HR-10 | HRP → MGT (توزيع تكلفة الموظفين على المخازن/الأقسام) | Costing Group بتجميع Dept/CC — يقابل بنية MGT |
| I-HR-11 | HRP → FNB (تكلفة وجبات الموظفين) | [ضعيف — لا نص] يُترك للمرحلة 7 |
| I-HR-12 | HRP → SYS Employee ↔ SYS User | "employee number... Press F1 to view a list of Employees" في HOD — والوحدة نفسها تستخدم User IDs — **العلاقة Employee↔User غير موثقة صراحة** (UNK) |

## C. تحديث Knowledge Graph (العلاقات الجديدة/المحدّثة)

| العقدة/الحافة | قبل الجلسة 8 | بعد الجلسة 8 |
|---|---|---|
| **AR →(deducts_via)→ HRP** | ❌ غير موجودة | ✅ **موثقة (I-HR-01)** |
| RQP(Recruitment) →(feeds)→ Employee | ضمنية | ✅ موثقة |
| Payroll →(posts_to)→ Finance | موثقة (FAS) | مؤكدة من طرفين |
| POS/BNQ Staff consumption → AR → HRP deduction | نصف حلقة | ✅ **حلقة مغلقة كاملة** |

> 📌 يُحدَّث `docs/domain/entity-relations.md` بعلاقة **S10 (AR→HRP)** في المرحلة التالية من Phase 1 الموسعة.

## D. مواصفات الواجهة الخارجية (Interface Contract)

| البند | الموثق |
|---|---|
| الملف | `PMS\Interface\PYATYYMM.DAT` (YY/MM موشّران بالاسم!) |
| الصيغة | "Flat Line Sequential file... delimited by a comma (,)" |
| البنية | EMP#(7,N) + DATE(8,N YYYYMMDD) + CODE(3,A) + DAYS(5,2,N) |
| أمثلة موثقة | `1,20000414,WRK,1` — ونصف يوم: WRK .5 + ABS .5 — و OVT بالساعات: `1,20000414,OVT,2` |
| **الحوكمة** | "Any change... intimated... at least **two weeks in advance**" + "**confirm in writing directly to IDS Bangalore**" — **عقد مستوى خدمة مضمّن في الدليل!** |
| القيود | كودات الحضور يجب أن تكون مسبقة التعريف في النظام |

## E. أولويات التنفيذ في المنصة الجديدة

| الأولوية | التكامل | الاستبدال المقترح |
|---|---|---|
| P0 | I-HR-03 (Finance) | Salary JE generator (Payroll Entry → Journal) — Frappe HRMS قياسي |
| P0 | I-HR-01 (AR) | **Additional Salary من AR invoice للموظف** — hook مخصص |
| P1 | I-HR-04 (Attendance) | **Employee Checkin API + biometric connector** — يلغي flat file |
| P1 | I-HR-02 | Job Offer → Employee (قياسي HRMS) |
| P2 | I-HR-05 | Bank API/SEPA/شيكات طباعة |
| P2 | I-HR-07 | Shared Employee master (قياسي — كيان واحد) |
