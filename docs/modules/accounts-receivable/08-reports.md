# 08 — التقارير (Reports) — وحدة ACR

> المصدر: ACR-RPL كاملاً (23 وظيفة، 33 ص). **بما أن ACR-RPL يخلط Reports وLookups**، جُردت هنا كلها ككتالوج واحد بإشارة النوع. خيارات المخرجات النمطية: **Display · Spool · Print · Export** (ACR-RPL §1 ص3).

---

## 1. جدول التقارير الكامل (23)

| # | التقرير | النوع | المدخلات الموثقة | الخيارات الجوهرية | الصفحات |
|---|---|---|---|---|---|
| R-AR-01 | **Opening Balance List (ACR)** | Report | Property · O/S As on MMYY (افتراضي = AR Start Date) | مخرجات نمطية | ص2-3 |
| R-AR-02 | **Transaction List** | Report | مدى تاريخي · Document Type (Debit/Credit/Adjustment) · Property · معيار اختيار | **Billed/Unbilled/Both** · **Automatic/Manual/Both** · **All/Unadjusted Credits** · ترتيب Company/Date | ص3-5 |
| R-AR-03 | **Balance by A/C Type** | Report | MMYY · Property · Currency · Company Type · Line Spacing ☐ | رصيد افتتاحي + يومي مدين/دائن + ختامي | ص5-6 |
| R-AR-04 | **Ledger Balance** | Report | Property · مدى · Currency · نطاق شركات | **8 خيارات**: Running Balance · Opening Balance · Debit only · Credit only · No-Transaction Companies · Summary Company Breakup · Exclude Nil Balance · Skip Page per Company · ترتيب Transaction/Bill Date | ص6-8 |
| R-AR-05 | **Folio Outstanding** | Report | Property · نطاق شركات · Currency · Cut Off (≤ اليوم) | Credits up to (Entered/Current Yes/No) · Print Company Address · Skip Page · Print Nil Balance | ص8-10 |
| R-AR-06 | **Aging Summary** | Report | Outstanding As of (≤ نهاية الشهر الحالي) · Process Receipts Upto Yes/No | معيار **Folio/Sector/Sales Executive** · Detail/Summary · **5 خيارات**: Company Address · Line Spacing · Exclude Nil · Credit limit not required · Closing balance بجوار الاسم + **تعديل فترات التقادم** | ص10-11 |
| R-AR-07 | **A/C Balance Detail** | Report | Property · نطاق شركات · Currency · **Outstanding over (أيام)** · Amount | فواتير متقادمة فوق العتبة والمبلغ | ص11-13 |
| R-AR-08 | **Credit Card Register** | Report | شركة بطاقة (F1) · مدى **ضمن نفس الشهر** · Commission % | Summary Required ☐ · **Update Commission Amount in Transactions ☐** (بدونها: طباعة بلا تحديث) — مخرج: **خطاب تغطية + Charge Slips** | ص13-15 |
| R-AR-09 | **SOA Print** | Report | شهر · نطاق شركات | Print Company Address · Skip Page on Company Change | ص15-17 |
| R-AR-10 | **Payment Follow-up Report** | Report | Property · As on · Company Type | Bill Details/Consolidated · Net Balance (All/Debit/Credit) · Print Address · Print Contact Person | ص17-19 |
| R-AR-11 | **Transaction Audit** | Report | مدى · All/Company/User | **حالات: Del (محذوف) · Old→New (نسختان للمعدَّل)** — يعمل فقط إذا Attr#3=Yes | ص19-20 |
| R-AR-12 | **Commission Report** | Report | **Credit Card/Travel Agent/All** · نطاق شركات · مدى · Currency | ترتيب Company/Bill Date · Details/Summary | ص20-22 |
| R-AR-13 | ~~"12123"~~ | **فجوة مصدر** | **PENDING — عنصر نائب بلا محتوى في الدليل الأصلي** | — | ص21 |
| R-AR-14 | **Receipt Register (ACR)** | Report | Property · مدى · **Cash / Cheque&CC** | Receipt# Consolidation ☐ · ترتيب Receipt#/Receipt Date/Bill# · **Bank-wise breakup** Yes/No · CC Settlement by companies ☐ | ص22-23 |
| R-AR-15 | **Cheque Deposit Statement** | Report | Property · **Cheque Date/Transaction Date wise** · مدى · **Local/Outstation/Both** | تلخيص: Date-wise · Bank & Branch-wise · Cheque Type-wise (مع Both فقط) · Line Skip | ص23-25 |
| R-AR-16 | **Monthly Summary Report** | Report | Property · Company Type/All · مدى | — | ص25-26 |
| R-AR-17 | **A/C Balance Query** | Lookup | Company (F1) · Property · Currency | **All/Unmatched Transactions** · مدى شهور (للكل) أو Cut Off (لغير المطابق) + Credits upto Yes/No · **Merge** (دمج بفاتورة/إيصال واحد) — عرض أنواع: **I (Invoice)/R (Receipt)/A (Adjustment)** | ص26-27 |
| R-AR-18 | **Outstanding Snapshots** | Lookup | Property · Currency · مدى · **High Balance Range** · A/C Type | Display Only Nil Balance ☐ · **Display Code/Display Type** — يعرض: Opening/Debit/Credit/Closing/Credit Limit/**Variance** | ص27-29 |
| R-AR-19 | **Receipts Display** | Lookup | Property · Company · معيار (Receipt#/Receipt Date/Bill#/Bill Date) + مدى | **Billed (مطابَق)** / **Credit & Advance payments** — قسم Credit فوق وDebit (الفواتير) تحته | ص29-30 |
| R-AR-20 | **Browse Transactions** | Lookup | مدى **MMYY ضمن نفس السنة المالية** | معايير: Bank Name · Bill#/Date · Branch · Card Number · Cheque#/Date · Receipt#/Date · Reg # + تصفح Prev/Next | ص30-32 |
| R-AR-21 | **Debtor Outstanding Report** | Report | Property · Sales Executive/All · Cut off · Yes/No (لقراءة الشاشة) | — | ص32-33 |
| R-AR-22 | **Daily Receipt Register by Invoice** | Report | Property · From/To · Company Types/All · Mode of payment/All | يومي إجمالي بالإيصال | ص33 |
| R-AR-23 | **IDS Report Designer** | أداة | مصمم تقارير مخصص | `[NOT DOCUMENTED]` متن فارغ في الدليل | ص33 |

## 2. التقارير الداعمة للفوترة (مخرجات Billings — راجع BIL)

| المخرج | الطريق | المصدر |
|---|---|---|
| Monthly Invoice Statement | BIL §1 | ص2 |
| Invoice (+Aging عمود تقادم) | BIL §2 | ص3-6 |
| Reminder (بصيغة معرفة مسبقاً) | BIL §2 | ص5 |
| سند القبض (Print Receipt + Comments/Consolidate/Format) | BIL §3 | ص6-7 |
| خطاب تأكيد الرصيد (Balance Confirmation) | BIL §4 | ص7-8 |

## 3. أنماط التقارير الملحوظة (قرارات تصميم للنظام الجديد)

1. **فلتر billed/unbilled/auto/manual** في Transaction List — تصنيف مصدري للقيود (من وحدات أخرى أم يدوي) — **يجب أن يظل سمة استعلام أساسية** (ACR-RPL §2 ص4).
2. **Aging Summary بثلاث زوايا** (Folio/Sector/Sales Executive) + تعديل الفترات وقت التشغيل — مرونة استثنائية (ACR-RPL §6 ص10).
3. **تقريران ماليان بديلان للإيداع البنكي**: Cheque Deposit Statement "replaces the number of deposit forms the Cashier will have to fill in" — توفير عملي موثق (ACR-RPL §15 ص23).
4. **Transaction Audit كضريبة Audit Trail** — نسختا Old/New للمعدَّل — نموذج Frappe Versioning مطابق تماماً (ACR-RPL §11 ص20).
5. **Outstanding Snapshots** بفلتر **High Balance Range** — عتبة مادية للرصد الاستباقي (ACR-RPL §18 ص27).
6. **A/C Balance Query** بعرض أنواع موحّد I/R/A + **Merge** — أبسط ت representations لحركة الحساب (ACR-RPL §17 ص27).
7. **فجوة "12123 PENDING"** — عنصر فهرس متروك في الدليل — يوثق أن السلسلة الرسمية للوحدة فيها فجوة مراجعة (راجع `17-gap-analysis.md`).
