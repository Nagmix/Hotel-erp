# 18 — معايير القبول (Acceptance Criteria) — وحدة FAS

> معايير تُشتق منها اختبارات القبول الوظيفية للنظام الجديد. كل معيار بمصدره الموثق.

## AC-FA-01: هيكل دليل الحسابات

- [ ] شجرة ثلاثية (رئيسي/فرعي/حساب) مع فئات نظامية (Assets/Liabilities/Income/Expense). [FAS-SET §1-§2]
- [ ] Account Code (5-8) + Short Name إلزامي (20) + GL Type (CASH/BANK/OTHERS) + Account Type (Client/Payables/Sub ledger) + PDC Type. [FAS-MST §1]
- [ ] ربط CC/Dept متاح لحسابات الدخل والمصروف فقط. [FAS-MST §1]
- [ ] لا تعديل لكود حساب عليه معاملات؛ ولا للرؤوس المولدة نظامياً. [FAS-LUK §7 + FAS-SET §1]

## AC-FA-02: إدخال القيود

- [ ] التحقق بقواعد Book Types التسع عند الإدخال (أول/آخر D/C بحسب النوع). [FAS-SET §3]
- [ ] منع الحفظ إذا D≠C. [FAS-TRN §E]
- [ ] تاريخ المعاملة داخل سنة مفتوحة فقط. [FAS-TRN §E]
- [ ] ترقيم تلقائي/يدوي بكل خيارات (prefix/zero-fill/دورية/starting/restart). [FAS-SET §3]
- [ ] Reversal يعكس D/C؛ Recurring يُثبّت للتاريخ الحالي. [FAS-TRN §E]
- [ ] Narration (250) + Pre Defined Narration (F1). [FAS-SET §3/§20]

## AC-FA-03: ترحيل FO/POS (السيناريو الحاسم)

- [ ] checklist المتطلبات الأربعة (Sales type + FY + رابطان) قبل التمكين. [FAS-TRN §G]
- [ ] الزنار: متاح بعد Day End/Open New Date فقط. [FAS-SET §6]
- [ ] عرض البنود: Account + Revenue Code + Audit Code + D/C + SL + المبالغ. [FAS-TRN §G]
- [ ] الفرق ≠ 0 → قرار → ترحيل للـ No Transaction Suspense مؤقتاً + تقرير سبب + إعادة معالجة بعد الإصلاح. [FAS-SET §6 + FAS-TRN §G]
- [ ] B/F دائن وC/F مدين لدفتر الضيوف؛ التسويات Debit فقط. [FAS-SET §6]

## AC-FA-04: الشراء والاستهلاك

- [ ] PJV يتطلب Bill No/Date؛ كلي أو جزئي؛ حساب Debit من الرابط (قابل للتغيير). [FAS-TRN §H]
- [ ] مثالا الضريبة الموثقان (Purchaser: D100/C99+Tax1؛ Vendor: D100+1/C101) يمرّان بنجاح. [FAS-TRN §H]
- [ ] Consolidate PJV متعدد GRR بشرط Effective ≥ GRR. [FAS-TRN §I]
- [ ] الاستهلاك شهري/يومي (INI 283). [FAS-TRN §J]

## AC-FA-05: الشيكات

- [ ] Cheque Book (تنبيه الحد الأدنى) + ترقيم تلقائي. [FAS-MST §4]
- [ ] الشيك المطبوع مقفل — Cancel Cheque بسبب إلزامي. [FAS-TRN §7]
- [ ] PDC: حسابات PDC Rcv/Pay + ترحيل التحصيل إلى Bank/Cash فقط. [FAS-TRN §F]

## AC-FA-06: الفترة والسنة

- [ ] FY من 6-24 شهراً من أي شهر. [FAS-SET §18]
- [ ] Audited الشهري يقفل الإدخال. [FAS-SET §18]
- [ ] Open FY: أرصدة→افتتاحية + صافي P&L→Retained Earnings (بنسب)؛ ثم مقفل. [FAS-TRN §8]
- [ ] Rollback ثم إعادة Open. [FAS-TRN §8]
- [ ] سنة جديدة بلا ترقيم → منع القيد. [FAS-SET §3]

## AC-FA-07: التسوية والتقارير

- [ ] Bank Rec realized (تاريخ/وقت) / unrealized (سبب). [FAS-TRN §3]
- [ ] drill-down الموحد: تقرير→سجل→معاملة→تعديل (بصلاحية). [FAS-LUK]
- [ ] Payable Outstanding مع aging. [FAS-LUK §6]

## AC-FA-08: التفويض

- [ ] Transaction Type Rights (مستخدم × كود معاملة). [FAS-SET §5]
- [ ] Voucher Authorization 3 مستويات بنطاق تاريخ. [FAS-TRN §9]
