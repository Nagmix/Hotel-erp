# 00 — نظرة عامة (Overview) — وحدة Accounts Receivable (ACR)

> وحدة **متابعة الذمم المدينة (Debtors)** — الحلقة الثالثة من المنظومة المالية (FO → AR → FAS). المقروء عميقاً (الجلسة 4): **ACR-SET (8 أقسام، 19 ص) + ACR-OPR (8 أقسام، 21 ص) + ACR-CRT (قسم واحد، 8 ص) + ACR-BIL (4 أقسام، 8 ص) + ACR-RPL (23 وظيفة، 33 ص)** — القراءة الخمسة كاملة 100%.

---

## 1. حدود الوحدة

| البند | الوصف الموثق |
|---|---|
| الاسم النظامي | Accounts Receivables / Accounts Receivable (ACR) — "ACCOUNTS RECEIVABLES" (شاشة كل الملفات) |
| الوظيفة الجوهرية | "manually record account wise details of debit bills, payment receipts and adjustment transactions" + متابعة تحصيل الذمم (Debtors Follow-Up) + إغلاق شهري بـ SOA (ACR-OPR §1 ص2، ACR-CRT ص1، ACR-OPR §7 ص20) |
| المركز المعماري | **مستقبِل تلقائي** لكل التسويات الائتمانية: "All sales credited to companies are automatically posted as debit entries in the Accounts Receivable module" (ACR-OPR §1 ص4) — من FO وPOS وBanquets & Conferencing وMembership |
| النطاق | قيود مدينة/دائنة/تسوية يدوية + مطابقة إيصالات + عمولات وكلاء + تجميع بطاقات ائتمان + متابعة ومطاردة ديون + فوترة شهرية (Invoices/Reminders/SOA/Balance Confirmation) + إقفال شهري متسلسل (SOA + Rollback) + 20+ تقريراً |
| خارج النطاق | دفتر الأستاذ (FAS) — AR ترحّل إليه فقط؛ AP (Vendor) داخل FAS/MST |

## 2. جرد الوظائف الموثقة (44 وظيفة)

| المجموعة | الوظائف | العدد | المصدر |
|---|---|---|---|
| **Setup** | AR Start Date · AR Opening Balance · Specify Aging · AR User Access · Company Profile · User Defined Print Forms · Purge ACR Audit Table · Print Form Designer | 8 | ACR-SET TOC ص1 |
| **Operations** | Transaction Entry (AR) · Match Bills – Receipts · Travel Agent Commissions · Credit Card Consolidation · Outstanding Update · Receipts Untagging · Statement of Accounts · Rollback Statement of A/C | 8 | ACR-OPR TOC ص1 |
| **Credit Trace** | Debtors Follow-Up (بتبويبات: Transactions · Company Info · Follow-Up Trace · Projection Report) | 1 (4 تبويبات) | ACR-CRT TOC ص1 |
| **Billings** | Monthly Invoice Statement · Print Invoice/Reminder (طباعة + إلغاء + تذكير + إعادة طباعة) · Print Receipt · Balance Confirmation AR | 4 | ACR-BIL TOC ص1 |
| **Reports & Lookups** | Opening Balance List · Transaction List · Balance by A/C Type · Ledger Balance · Folio Outstanding · Aging Summary · A/C Balance Detail · Credit Card Register · SOA Print · Payment Follow-up Report · Transaction Audit · Commission Report · **«12123 PENDING»** (فجوة مصدر!) · Receipt Register · Cheque Deposit Statement · Monthly Summary Report · A/C Balance Query · Outstanding Snapshots · Receipts Display · Browse Transactions · Debtor Outstanding Report · Daily Receipt Register by Invoice · IDS Report Designer | 23 | ACR-RPL TOC ص1-2 |

> ⚠️ **فجوة مصدر موثقة:** البند 13 في فهرس ACR-RPL بعنوان "12123 PENDING" — عنصر نائب متروك في الدليل الأصلي بلا محتوى (ACR-RPL ص21). سُجل في `17-gap-analysis.md` (GAP-AR-D01).

## 3. المفاهيم الجوهرية الموثقة

| المفهوم | الدلالة | المصدر |
|---|---|---|
| **SOA (Statement of Accounts)** | "the last and final financial statement that is processed for a month" — معالجتها = إغلاق الشهر ومنع أي تعديل/حذف؛ متسلسلة شهرياً (الشهر الأول من AR Start Date، حقل غير قابل للتحرير بعدها) | ACR-OPR §7 ص20-21 |
| **Rollback SOA** | آلية العكس: إلغاء SOA من شهر قطع (MM/YY) حتى آخر شهر معالَج للسماح بالتعديل ثم إعادة المعالجة | ACR-OPR §8 ص21 |
| **Unallocated Receipt** | إيصال يُسجل بدون تخصيص لفاتورة ("The system identifies this amount as unallocated") ثم يُطابق لاحقاً عبر Match Bills–Receipts — يعتمد على Module Attribute #6 | ACR-OPR §1 ص4 |
| **Aging (بالفائدة)** | فترات تقادم الذمم أساس **تاريخ الفاتورة**؛ مع معيار فائدة لكل فترة (4 أنواع نظامية)؛ **تعريف مشترك يخدم AR وFAS** ("Certain queries and report options in the Accounts Receivable and Financial Management module is based on this definition") | ACR-SET §3 ص8 |
| **Credit Limit (حاجب تسوية)** | "If the current bill and/or the amount receivable exceed the specified credit limit, settlement of the Front Desk, Point of Sale or Banquet bill or manual posting of the bill is not allowed" — قيد عبور وحدات! | ACR-SET §5 ص14 |
| **Book Profit/Loss (FX)** | ربح/خسفة الصرف عند التسوية — يتجنبه النظام باعتماد **سعر صرف تاريخ الفاتورة** عند السداد ("bill exchange rate at the receipt level") | ACR-OPR §1 ص6 |
| **Opening Balance** | أرصدة ما قبل تشغيل الوحدة (Debit/Credit/Adjustment) — بفاتورة أو مجمع؛ تُقفل بعد معالجة SOA لشهر البداية (Rollback ثم إعادة) | ACR-SET §2 ص2-3 |
| **Black List / Watch List** | وصم حساب الشركة (سبب + مجيز إلزاميان للوصم) / قائمة مراقبة لغرض تقرير S&M — يقعان في Company Profile المشترك | ACR-SET §5 ص12 |
| **AR Start Date** | شهر تفعيل الوحدة (MMYY) — **يُدخل مرة واحدة ولا يُعدَّل أبداً** | ACR-SET §1 ص1 |

## 4. التفاعلات مع الوحدات (موثقة نصاً)

- **استقبال تلقائي (Debit):** تسويات FO الائتمانية + POS + Banquets & Conferencing + Membership → قيود مدينة تلقائية قابلة للعرض والتعديل الجزئي (ACR-OPR §1 ص2).
- **إرسال محاسبي (AR→FAS):** عند الحفظ تفتح شاشة FA Transaction للترحيل — مشروط بـ INI #56 = 0 (ممكَّن) + تعريف حسابات Sundry Debtors/Cash/Bank/Commission في "Link AR to Finance" (FAS-SET §11) (ACR-OPR §1 ص10).
- **بيانات مشتركة:** Company Profile واحد يخدم Front Desk وS&M وPOS وAR وBanquets وConferencing وMembership (ACR-SET §5 ص10-11)؛ وأنواع الشركة (أول 3 خانات من الكود) معرَّفة في **FO Setup → Company Types** (ACR-SET §5 ص11).
- **مفاتيح نظامية من SYS:** Module Attributes (#1 #2 #3 #6) + INI (#56 #74) + Pgm ID for Print Forms (إلزامي لطباعة Monthly Invoice Statement) (ACR-OPR ص4/5/20 + ACR-BIL §1 ص2).

## 5. أهم الاكتشافات المعمارية (الجلسة 4)

1. **إقفال شهري متسلسل ذو آلية عكس مزدوجة:** SOA يقفل الشهر تسلسلياً (لا قفز للشهور)؛ Rollback يفتح من شهر القطع حتى آخر شهر معالج؛ والقيود المفوترة/المطابَقة تتطلب **إلغاء الفواتير أو حذف القيود الدائنة أولاً** قبل التعديل — سلسلة "فتح مشروط" من ثلاث طبقات (SOA → Invoice → Matching).
2. **منطق INI معكوس:** INI #56 `ACR2FAS`: **0 = ممكَّن** و1 = معطَّل (والافتراضي 1 = معطَّل!) — عكس غالبية المفاتيح؛ وINI #74 `ACRALLOWUPDATION`: 0 = يسمح بتعديل اسم الشركة/الفرع بعد طباعة الفاتورة (الافتراضي)، 1 = يمنع (ACR-OPR §1 ص10).
3. **حاجب Credit Limit عابر للوحدات:** حدّ ائتمان الشركة في Profile يمنع تسوية فواتير FD/POS/Banquet **قبل حدوثها** — نمط تحقق مركزي upstream (ACR-SET §5 ص14).
4. **نمط الاستلام-المطابقة (Receive–Match):** إيصال غير مخصص → Match Bills–Receipts → Untagging عند الخطأ — دورة حياة إيصال كاملة بثلاث حالات (unallocated → matched → untagged) (ACR-OPR §1/§2/§6).
5. **Credit Card Consolidation تجميع عرضي فقط:** "These bills are consolidated for the Credit Card Register only. In all other transactions these bills are considered as multiple entries" — تجميع للسجل والمراسلة فقط لا للقيود (ACR-OPR §4 ص13).
6. **تقادم بفائدة بأربعة معايير نظامية:** % على الرصيد الختامي / مبلغ ثابت / لا شيء / % على الرصيد الافتتاحي — لكل فترة على حدة (ACR-SET §3 ص9).
7. **مرجعية تاريخية:** نص ACR-RPL §11 يذكر "Fortune Enterprise 2.0" (اسم منتج أقدم من IDS!) كعائلة النظام — مؤشر نَسَب تطوري للكود الأساس (ACR-RPL ص20).

## 6. خريطة وثائق الوحدة

`01` البيانات الرئيسية · `02` الإعداد · `03` الشاشات · `04` سير العمل · `05` قواعد العمل · `06` التحققات · `07` الصلاحيات · `08` التقارير · `09` الاستعلامات · `10` المعاملات · `11` الأثر المحاسبي · `12` التكاملات · `13` الحالات الحدية · `14` نموذج البيانات · `15` تحليل UX · `16` ربط ERPNext · `17` تحليل الفجوات · `18` معايير القبول.
