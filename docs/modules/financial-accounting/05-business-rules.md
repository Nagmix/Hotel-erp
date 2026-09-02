# 05 — قواعد العمل (Business Rules) — وحدة FAS

> معرفات BR-FA-XX. كل قاعدة بمصدرها.

---

## BR-FA-01: قواعد التوازن والفروق

| القاعدة | المصدر |
|---|---|
| **المدين = الدائن إلزاماً في كل قيد** ("should tally to save") | FAS-TRN §E ص13 |
| **Post FO to Finance: الفرق غير الموزع = صفر** | FAS-TRN §G ص18 |
| الفرق يُرحَّل مؤقتاً لحساب **No Transaction** (إلزامي تعريفه) | FAS-SET §6 ص14 |
| وجود الفرق = خلل تعريف → **تصحيح + إعادة ترحيل** | FAS-SET §6 ص14-15 |

## BR-FA-02: قواعد Book Types (تحقق القبول)

راجع الجدول الكامل في `02-configuration.md` §1 — ملخص القيود الصلبة:
- Receipts يبدأ بأصل Bank/Cash؛ Payments ينتهي بأصل Bank/Cash؛ Sales ينتهي بدخل؛ Purchase يبدأ بالتزام وينتهي بمصروف؛ **Journal يرفض Cash/Bank**؛ **Exchange/Contra: Cash/Bank فقط** (كل السحب النقدي عبره) — FAS-SET §3 ص7.

## BR-FA-03: قواعد الفترة والقفل

| القاعدة | المصدر |
|---|---|
| تاريخ المعاملة: **أي سنة مفتوحة فقط** (المغلقة تُرفض) | FAS-TRN §E ص12 |
| **Audited=Yes للشهر → يُمنع الإدخال/التعديل** (للتعديل يُرجع No) | FAS-SET §18 ص38 |
| السنة 6-24 شهراً من أي شهر بداية | FAS-SET §18 |
| **بعد Open Financial Year: لا تغيير على معاملات العام المعالج** — العكس فقط عبر Rollback ثم إعادة التنفيذ | FAS-TRN §8 ص44 |
| حذف/تعديل الجدول المالي قبل بدء المعاملات فقط | FAS-SET §18 Note |
| **سنة مالية جديدة بدون تحديد Document Number لكل Transaction Type → يُمنع إدخال المعاملات** | FAS-SET §3 ص8-9 |

## BR-FA-04: قواعد الشيكات وPDC

| القاعدة | المصدر |
|---|---|
| **طباعة الشيك تقفل القيد** (لا تعديل/حذف) — التراجع عبر Cancel Cheque بسبب | FAS-TRN §7 |
| تنبيه الحد الأدنى للشيكات المتبقية (Minimum Cheques) | FAS-MST §4 |
| حسابات PDC: **Account Type Receivables/Payables + PDC Type** | FAS-TRN §F |
| ترحيل PDC المحصل: **GL Type Cash/Bank فقط** | FAS-TRN §F |
| الترقيم التلقائي للشيكات: **INI 504 = 0** | FAS-MST §4 |

## BR-FA-05: قواعد الشراء والضريبة

| القاعدة | المصدر |
|---|---|
| **Bill No & Bill Date إلزاميان** لكل PJV | FAS-TRN §H ص21 |
| PJV كلي أو **جزئي** (Bill Quantity) | FAS-TRN §H |
| Effective Date للـ PJV **≤ تاريخ النظام**؛ وللمجمعة **≥ تاريخ GRR** | FAS-TRN §H/§I |
| ضريبة البائع/المشتري بـ INV Switches 1+4 وVendor Tax Split (راجع أمثلة `11-accounting-impact.md` §4) | FAS-TRN §H |
| Contract Debit Note: **فقط مع Standing PO**؛ الخصم الجزئي يعدّ المتبقي **waived off** | FAS-TRN §L |
| الشراء → **أصل**؛ الاستهلاك → **مصروف** (+CC+Dept) | FAS-SET §8 |

## BR-FA-06: قواعد الاستهلاك والموازنات

| القاعدة | المصدر |
|---|---|
| استهلاك المخزون: **شهري (INI 283=1) أو يومي (=2)** | FAS-TRN §J |
| الموازنة **Apportion** (توزيع بالتساوي) أو **Fixed** (يدوي شهرياً)؛ Actuals آلية من المرحّلات | FAS-TRN §4 |

## BR-FA-07: قواعد البنك والتسوية

| القاعدة | المصدر |
|---|---|
| Bank Rec: realized → **تاريخ/وقت**؛ unrealized → **سبب إلزامي** | FAS-TRN §3 |
| Payment Match: الدفعات المقدمة تسوّي الفواتير → **وسمها Yes** | FAS-TRN §5 |
| TDS Tagging: **Bank + Challan No + Date دقيقة** (شرط Form 16A) | FAS-TRN §6 |

## BR-FA-08: قواعد التعديل والهيكل

| القاعدة | المصدر |
|---|---|
| Transaction Type: تعديل Name/Short/Print فقط (أو الكل إذا لا معاملات/محذوفة كلها) | FAS-SET §3 |
| **Account Code لا يُعدل إذا عليه معاملات** (Chart of Accounts List) | FAS-LUK §7 |
| **لا تعديل للرؤوس المولدة نظامياً** (Main Heads) | FAS-SET §1 |
| Reversal journal: **يعكس D↔C**؛ Recurring: تأكيد للتاريخ الحالي فقط | FAS-TRN §E |
| AR: تغيير الحساب المرتبط بـ **F5** قبل حفظ قيد AR | FAS-SET §11 |

## BR-FA-09: قواعد ترحيل الوحدات (موحدة)

| القاعدة | المصدر |
|---|---|
| FO/POS Sales Journal **بعد Day End + Open New Date**؛ Effective = عادة الأمس | FAS-SET §6 + FAS-TRN §G |
| AR receipts فورية عند الحفظ | FAS-SET §11 |
| Payroll/Membership عند الطلب | FAS-TRN §K/§M |
| **Cash/Bank ممنوعان** في روابط POS/MM/Membership D/C | FAS-SET §7/§8/§10 |
