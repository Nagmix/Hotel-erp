# 00 — نظرة عامة (Overview) — وحدة Financial Management (FAS)

> الوحدة المحاسبية المركزية (General Ledger + محيطها). المقروء عميقاً (الجلسة 3): **FAS-SET (27 قسماً، 63 ص) + FAS-TRN (9 أقسام، 45 ص) + FAS-MST (4 أقسام، 33 ص) + FAS-LUK (9 وظائف، 28 ص)**. FAS-REP مؤجل لمرحلة التقارير (Phase 7).

---

## 1. حدود الوحدة

| البند | الوصف الموثق |
|---|---|
| الاسم النظامي | Financial Management (FAS) — "FINANCIAL MANAGEMENT" (FAS-TRN ص1) |
| الوظيفة الجوهرية | "recording day-to-day financial transactions in multi currency for reflection in the General Ledger" (FAS-TRN §1 ص2) |
| المركز المعماري | **قلب التكامل**: تستقبل ترحيلات من 6 وحدات (FO، POS، MM، Payroll، Membership، AR) عبر روابط إعداد معرفة (FAS-SET §6-§11) |
| النطاق | دفتر أستاذ عام + Vendor Master + PDC + تسوية بنكية + موازنات + TDS + إقفال سنوي + تقارير (REP) |

## 2. جرد الوظائف الموثقة (49 وظيفة + التقارير)

| المجموعة | الوظائف | العدد | المصدر |
|---|---|---|---|
| **Setup** | Main Heads · Sub Heads · Transaction Types · Transaction Voucher Link · Transaction Type Rights · **FO to Finance Link** · **POS to Finance Link** · **MM to Finance Link** · **Payroll to FAS Link** · **Membership to FAS Link** · **Link AR to Finance** · TDS Nature of Payment · TDS Tax Link · TDS Defaults · Print Forms · User Defined Print Forms · Create User Reports · Financial Period · Budget Types · Pre Defined Narration · Trial Balance Print Order · Link CC to Department · Link Exempt Tax to Finance · Vendor Tax Split · Retained Earning Account · Specify Aging · Print Form Designer | 27 | FAS-SET TOC |
| **Transactions** | FA Transactions (بـ 15 خياراً فرعياً A-O: Period/Master/Link/Ledger Opening Balance/Transaction Entry/PDC/**FO to FA Posting**/Purchase Journal Posting/Consolidate PJV/Consumption Posting/Membership to FA Posting/Contract Debit Note/Payroll to FA Posting/Pending Postings/Statistics) · Statistics Transaction · Bank Reconciliation · Budget · Interactive Payment Match · TDS Tagging · Cancel Cheque · Open Financial Year · Voucher Authorization | 9 (+15 فرعي) | FAS-TRN TOC |
| **Masters** | Financial Account Master (Chart of Accounts + Vendor Master + Sub Ledger + Expense Allocation) · Statistics Master · Statistics Budget Master · Cheque Book Master | 4 | FAS-MST TOC |
| **Lookups** | Ledger Balance · Day Book (Q) · Trial Balance · Profit and Loss · Balance Sheet · Payable Outstanding · Chart of Accounts List · Cash Flow Query · Transaction Search | 9 | FAS-LUK TOC |
| **Reports** | FAS-REP (~858 سطراً مستخرجاً) | — | مؤجل Phase 7 |

## 3. المفاهيم الجوهرية الموثقة

| المفهوم | الدلالة | المصدر |
|---|---|---|
| **Book Type** | هوية نوع القيد (system reserved): Receipts / Payments / Exchange (Contra) / Sales Journal / Purchase Journal / Debit Notes / Credit Notes / Transfer / Journal — **لكل منها قواعد تحقق D/C موثقة** (راجع `02-configuration.md`) | FAS-SET §3 ص7 |
| **Transaction Type (Code)** | كود 2 رقمي (حتى 99 لكل Property) يجمع: Book Type + ترقيم مستندات + طباعة Voucher + سلوك Particulars | FAS-SET §3 |
| **Chart of Accounts** | ثلاث طبقات: Main Head (3 رقمي، Category نظامي) → Sub Head (3 رقمي) → Account Head (5-8 حرفي: Group + GL Type + Account Type + PDC Type + Cost Center + Department) | FAS-SET §1-§2 + FAS-MST §1 |
| **Sub Ledger** | حسابات فرعية (7 حرفي) مرتبطة بحساب رئيسي واحد أو أكثر؛ إلزامية إذا كان الحساب Control Account | FAS-MST §1 |
| **السنة المالية** | 6-24 شهراً، تبدأ بأي شهر؛ حقل **Audited شهرياً يقفل القيد** | FAS-SET §18 |
| **الترحيل الموازن** | "The Total Debit should be equal to the Total Credit i.e., the undistributed amount must be zero" | FAS-TRN §G |
| **Suspense (No Transaction)** | نوع إيراد يوجب حساب وسيط؛ يستقبل الفروق غير الموزعة مؤقتاً | FAS-SET §6 ص14 |
| **PDC** | شيكات مؤجلة بحسابات مخصصة (PDC Receivable/Payable) تُرحَّل للبنك عند التحصيل | FAS-TRN §F |

## 4. التفاعلات مع الوحدات (موثقة نصاً)

- **استقبال (Posting in):** Sales Journal من FO/POS (بعد Day End) · Purchase Journal من MM (GRN/Service Work Orders) · Consumption (Issues) · Payroll Journal · Membership Sales · AR Receipts (مع إمكانية تعديل الحساب المرتبط بـ F5 قبل الحفظ) — FAS-TRN §E ص11.
- **إرسال:** تقارير GL لكل الوحدات؛ Aging يخدم AR وFAS (FAS-SET §26).
- **إعداد متبادل مع SYS:** Property Codes · Cost Centers · Departments · Tax Codes · Module Attributes (Switch 4 FAS "FOM to FAS Posting Required"، Switch 1/2 ترتيب الطباعة، INV Switches 1/4/3، Module Attribute 9 TDS) — FAS-SET §11/§21/§18 + FAS-TRN §H/§I + FAS-MST §1.

## 5. أهم الاكتشافات المعمارية (الجلسة 3)

1. **الروابط الست كاملة التعريف**: كل رابط يعرّف Debit + Credit Account Heads لكل كود إيراد/مجموعة، مع أنماط تحقق موثقة (راجع `11-accounting-impact.md`).
2. **آلية الفروق غير الموزعة**: أي خلل تعريف يظهر كفرق في Sales Journal → يُرحَّل تلقائياً لحساب Suspense → إصلاح التعريف → إعادة ترحيل (re-process) — نمط "التصحيح بإعادة المعالجة".
3. **قفل مزدوج للفترة**: حقل Audited الشهري + معالجة Open Financial Year (مع Rollback كآلية عكس).
4. **ترقيم الشيكات**: Cheque Book Master بتنبيه الحد الأدنى (INI 504).
5. **ثلاث مستويات تفويض للقسائم** (Voucher Authorization L1-L3).

## 6. خريطة وثائق الوحدة

`01` البيانات الرئيسية · `02` الإعداد · `03` الشاشات · `04` سير العمل · `05` قواعد العمل · `06` التحققات · `07` الصلاحيات · `08` التقارير · `09` الاستعلامات · `10` المعاملات · `11` الأثر المحاسبي (النواة) · `12` التكاملات · `13` الحالات الحدية · `14` نموذج البيانات · `15` تحليل UX · `16` ربط ERPNext · `17` تحليل الفجوات · `18` معايير القبول.
