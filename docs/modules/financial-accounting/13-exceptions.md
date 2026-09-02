# 13 — الحالات الحدية (Exceptions & Edge Cases) — وحدة FAS

> معرفات E-FA-XX.

| ID | الحالة | المعالجة الموثقة | المصدر |
|---|---|---|---|
| E-FA-01 | ترحيل FO وفيه أكواد غير مربوطة | الفرق → حساب No Transaction (Suspense) مؤقتاً → إصلاح → إعادة ترحيل | FAS-SET §6 |
| E-FA-02 | فرق مستخدم اختار No في شاشة الفرق | يُمنع الحفظ (التوازن شرط) | FAS-TRN §G |
| E-FA-03 | قيد بتاريخ سنة مقفلة | **مرفوض** ("will not be accepted") | FAS-TRN §E |
| E-FA-04 | تعديل شهر موسوم Audited | ممنوع — يُرجع Audited=No أولاً | FAS-SET §18 |
| E-FA-05 | تعديل بعد Open Financial Year | Rollback Fin. Year → تعديل → **إعادة Open إلزامية** | FAS-TRN §8 |
| E-FA-06 | سنة جديدة بلا Document Number | **منع كامل لإدخال المعاملات** | FAS-SET §3 |
| E-FA-07 | شيك مطبوع بحاجة لتعديل | **Cancel Cheque** بسبب إلزامي ثم إعادة القيد | FAS-TRN §7 |
| E-FA-08 | PDC مطلوب ترحيله لحساب غير بنكي | **مرفوض** (Cash/Bank فقط) | FAS-TRN §F |
| E-FA-09 | PJV بلا Bill No/Date | **مرفوض** (إلزامي) | FAS-TRN §H |
| E-FA-10 | PJV بكمية جزئية | مسموح — Bill Quantity تُحدد | FAS-TRN §H |
| E-FA-11 | Consolidate PJV بلا INV Switch 3 | فواتير الاستلام لا تظهر (شرط Bill Mandatory) | FAS-TRN §I |
| E-FA-12 | Effective Date للمجمعة < تاريخ GRR | **مرفوض** (≥ GRR إلزامي) | FAS-TRN §I |
| E-FA-13 | صرف لمورد Stop Payment=No | **النظام يمنع الدفع** | FAS-MST §1 |
| E-FA-14 | شراء من مورد Stop Purchase=Yes | يُمنع الشراء (الحقل موثق) | FAS-MST §1 |
| E-FA-15 | مورد blacklisted | يُسجل من أدرجه + السبب (تاريخي قابل للعرض) | FAS-MST §1 |
| E-FA-16 | شيكات الشيك-بوك شارفت على النهاية | **تنبيه عند بلوغ Minimum Cheques** | FAS-MST §4 |
| E-FA-17 | تعديل Account Code عليه معاملات | **ممنوع** (Chart of Accounts List) | FAS-LUK §7 |
| E-FA-18 | تعديل Main Head مولّد نظامياً | **ممنوع** | FAS-SET §1 |
| E-FA-19 | فرق عقد بخصم جزئي | المتبقي يُعدّ **waived off** | FAS-TRN §L |
| E-FA-20 | Journal بحساب Restrict Journal=Yes | **ممنوع** القيد بنوع Journal | FAS-MST §1 |
| E-FA-21 | قيد لحساب Stop Posting=Yes | **معطّل الترحيل** | FAS-MST §1 |
| E-FA-22 | Contract Debit Note بلا Standing PO | **غير قابل للتطبيق** ("applicable only if SPO in use") | FAS-TRN §L |
| E-FA-23 | TDS Applicable بلا Module Attribute 9 | الخيار غير متاح | FAS-MST §1 |
| E-FA-24 | Recurring journal يعدَّل | **ممنوع** — تأكيد للتاريخ الحالي فقط | FAS-TRN §E |
| E-FA-25 | خسارة سنة (صافي سالب) | يُرحَّل لـ Retained Earnings بنفس الآلية (P&L Head) | FAS-TRN §8 |
| E-FA-26 | التعديل على TB Print Order غير معرف | **Chart of Accounts List لا تُعرض في Reports/Lookups** | FAS-SET §21 Note |
| E-FA-27 | دفعة مقدمة تسوي فواتير | وسم Payment Match Yes للفواتير والمبلغ | FAS-TRN §5 |
| E-FA-28 | شيك غير محصل (unrealized) | **سبب إلزامي** في Bank Rec | FAS-TRN §3 |
