# 04 — سير العمل (Workflows) — وحدة FAS

> المصادر: FAS-TRN (كامل) + FAS-MST. المعرفات WF-FA-XX.

---

## WF-FA-01: إدخال معاملة مالية يدوية (Transaction Entry)

1. **F2: Period** → Property + نطاق تاريخ.
2. اختيار Transaction Code → **Transaction Date**: أي سنة مالية **مفتوحة** (المغلقة تُرفض) → Document No (آلي إذا Automatic).
3. Account Name (F1؛ مع Sub Ledger إن وجد) → Currency → Bill# (اختياري) → Amount → Confirm.
4. **القاعدة الحاكمة: "The Debit and Credit amounts should tally to save the transaction"** (FAS-TRN §E ص13).
5. أدوات داخلية: **JOURNALS** (Normal قابل للتعديل؛ **Recurring يُؤكد للتاريخ الحالي فقط**؛ **Reversal: يُعكس Debit↔Credit** للحسابات) · **ALLOCATION** (تخصيص مصروف بطريقة apportion من Expense Allocation) · **LEDGER BALANCE** (استعلام رصيد الشهور ثم تفاصيل اليوم) · **TDS QUERY** (خصومات سابقة للمورد).

## WF-FA-02: رصيد افتتاحي (Ledger Opening Balance)

1. يُفتتح **بنوع Journal voucher آلياً**؛ Document No آلي.
2. Type (Debit/Credit → قائمة حسابات) → الحساب (+Sub Ledger آلي) → Currency (افتراضي مع معدل، قابل للتغيير F1) → Bill# + Amount + Narration → Confirm (صف grid).
3. تعديل بالـ Double-click على الصف؛ حذف بـ **F5**؛ تنقّل grid/entry بـ **F4**.
4. **القاعدة:** الأرصدة الافتتاحية للأصول والالتزامات فقط — **الدخل والمصروف عبر Transaction Entry (Journal)** (FAS-TRN §D ص10).

## WF-FA-03: Post FO to Finance (قلب الترحيل اليومي) ⭐

**المتطلبات الإلزامية قبل التنفيذ (FAS-TRN §G ص17):**
1. Transaction Type بنوع Book Type **Sales** معرف.
2. Financial Year معرفة.
3. **Link FOM to Finance**.
4. **Link POS to Finance**.

**التدفق:**
1. Transaction Code (آلي = كود Book Type Sales).
2. **Effective Date** — "Normally the date entered is a day prior to the Current System Date" (الترحيل اليوم السابق).
3. تُعرض البنود: Account Heads + Revenue Code + **Audit Code** + Debit/Credit Account Head + Debit/Credit Sub Ledger + المبالغ.
4. **التوازن الإلزامي: Total Debit = Total Credit (undistributed = 0)** → Save → يُرحَّل إلى GL.
5. **فرع الفرق:** إن وُجد فرق → شاشة → Yes → **يُرحَّل الفرق آلياً لحساب موسوم بنوع "No Transaction"** → معناه خلل تعريف روابط → تصحيح التعريفات → **إعادة ترحيل (re-process)**.

**الزناد الموثق (FAS-SET §6 ص12):** "Once the Day End processes is carried out in the Front Office module and a New Date is commenced, the Post FO to Finance operation has to be executed for posting the daily sales."

## WF-FA-04: Purchase Journal (Regular PJV)

**المتطلبات (FAS-TRN §H):** FY + Transaction Type (Book Type **Purchase**) + Link Purchase to Finance + Link Exempt Tax + Vendor Tax Split.

1. اختيار Regular PJV → Continue.
2. Property + Currency (أو All) + Vendor (F1 → الاسم آلي) + المعيار: **Grr Date أو Grr No** + النطاق.
3. **Bill No & Bill Date إلزاميان** ("mandatory to enter the Vendor Bill reference").
4. GRN Details → بنود (Serial/Item/Grr/Qty الأصلية والمفوترة/العملة/السعر/القيمة)؛ Tag All أو Double-click لاختيار بند.
5. **Post كلي أو جزئي** (Bill Quantity قابلة للتحديد) → حساب Debit يظهر من رابط الشراء (قابل للتغيير؛ **Open Item يوجب حساباً**) → Control Account → Sub Ledger (F1) → Confirm (يحسب qty × rate آلياً).
6. ربط PJV بـ **Payable Control Account Head** → Transaction Code (نوع Purchase) + Effective Date (**≤ تاريخ النظام**).
7. Service PJV: من Service Work Orders (PO No/Date + Bill)؛ **بند الخدمة: كود 99999999 + طبيعة الخدمة + القيمة**.

## WF-FA-05: Consolidate PJV

1. Property + GRR (Date أو Number) + النطاق → GRR Details → Save ("Records Updated Successfully").
2. Auto PJV Posting → **Effective Date (≥ GRR Date)** → Confirm → Narration.
- **شرط:** INV Switch 3 (Bill Mandatory in Receipts) = Yes.

## WF-FA-06: Consumption Posting (استهلاك المخزون)

Property + Store + Month/Year + Transaction Code → Load → Confirm → تفاصيل Credit → Confirm → Narration → Save.
- **الإيقاع:** INI 283 (1=شهري، 2=يومي).

## WF-FA-07: Membership/Payroll to FA Posting

Property + Transaction Code + التاريخ → (Load) → Save. (نمط موحد بسيط — FAS-TRN §K/§M).

## WF-FA-08: Contract Debit Note

1. عرض GRRs (بتاريخ أو نطاق) → اختيار بند → تفاصيل الاستلام.
2. اختيار المورد المتعاقد → يظهر **رقم/سعر/قيمة العقد** + العملة + سعر الصرف → **Diff Amt = قيمة الاستلام − قيمة العقد**.
3. **Debit Amount = كامل الفرق أو جزءه (الباقي يعدّ waived off)** → OK → Transaction Entry (D/C) → Save + طباعة Debit Note/Voucher.
- **الشرط:** استخدام Standing Purchase Order؛ يمكن الخصم جزئياً من عدة موردين متعاقدين؛ **GRR منفصل لحساب Debit Notes**.

## WF-FA-09: PDC (الشيكات المؤجلة)

1. عند الاستلام: قيد عادي يخصم مبلغ الشيك على حساب موسوم **PDC Receivable**.
2. **PDC Transactions:** Account (يعرض حسابات PDC فقط) + نطاق تاريخ الشيك + (Post أو Deletion) → Load.
3. اختيار الشيك المحقق → Debit Account Head (**يقبل GL Type Cash/Bank فقط** — F1) → التفاصيل (SL/العملة/المبلغ/Cheque#/Cash Flow) → Confirm → يُعرض D/C → Save → يُسجل في GL.
- **الشرط:** حسابان بـ Account Type Receivables/Payables + PDC Type مطابق (FAS-MST).

## WF-FA-10: Bank Reconciliation

Property + Bank A/c (+SL) + From/To Doc Date → عرض معاملات البنك → Tag: **realized** (→ تاريخ/وقت التحصيل) أو **unrealized** (→ **سبب إلزامي**) → أساس استعلامات/تقارير التسوية.

## WF-FA-11: Budget (الموازنة)

Budget Type (F1) + FY + Currency + Account + Department + Cost Center → **Apportion** (المبلغ الكلي يُوزَّع بالتساوي على شهور السنة) أو **Fixed** (قيمة لكل شهر يدوياً) → Actuals تُحتسب آلياً من المعاملات المرحّلة.

## WF-FA-12: TDS Tagging

untagged + نطاق التاريخ + Property + **Bank + Challan No + Challan Date** → Load → وسم السجلات (مسافة على tick) → Save → أساس **Form 16A**.

## WF-FA-13: Cancel Cheque

Property + Transaction Code + Doc Date/# → تفاصيل الشيك (آلية) → **Reason** → Cancel.
- **القاعدة:** بعد طباعة الشيك **يُمنع تعديل/حذف قيد الدفع** — الإلغاء هو الطريق الوحيد.

## WF-FA-14: Open Financial Year (إقفال وافتتاح السنة) ⭐

**المتطلبات المسبقة:** Financial Year + Retained Earning Account معرفان.

**ما تنفذه العملية (موثق حرفياً — FAS-TRN §8):**
1. **أرصدة إقفال كل حسابات الأصول والالتزامات في السنة السابقة → أرصدة افتتاحية في السنة الحالية.**
2. **صافي ربح/خسارة السنة السابقة (الدخل − المصروف) → حساب/حسابات الأرباح والخسائر المحددة في Retained Earnings Account (بنسب التوزيع)؛ "This remains constant in the Current Financial Year till the Year End process is done for that Year".**

**العكس (Rollback Fin. Year):** اختيار Property → العام يُلتقط آلياً → Process → لإجراء تعديلات → **ثم إعادة تنفيذ Open Financial Year إلزامياً**.

## WF-FA-15: Interactive Payment Match

Property + Account + Vendor + Currency → عرض قيود الدفع → **Yes/No tag لربط فواتير المورد بقيود الدفع** (+ إجماليات Bill#/Actual/Balance) → Save.
- **القاعدة الموثقة:** "If bills are settled (When you give advance payment) in this option tag the amount and settled bills to YES".

## WF-FA-16: Voucher Authorization

إنشاء مستويات تفويض للمستخدمين لمعالجة القسائم **ضمن نطاق تاريخ** — **ثلاثة مستويات: Level 1 / Level 2 / Level 3** (FAS-TRN §9 ص45).
