# 10 — المعاملات (Transactions & Document Lifecycle) — وحدة FAS

> دورات حياة المستندات المالية الموثقة.

---

## 1. دورة قيد GL (FA Transaction)

```
إدخال (Transaction Entry) → توازن D=C → حفظ → GL
   ├── Normal Journal: قابل للتعديل
   ├── Recurring: يُؤكد للتاريخ الحالي فقط (دورية)
   └── Reversal: نسخة معكوسة D↔C للحسابات
```
- **الحالات الموثقة implicitly:** مسودة grid قبل Confirm → محفوظ؛ حذف الصف F5 قبل الحفظ؛ **لا حذف بعد الحفظ إلا عبر آليات خاصة** (الشيك المطبوع: Cancel Cheque؛ العام المقفل: Rollback FY).

## 2. دورة PDC

```
استلام الشيك → قيد عادي (Debit: PDC Receivable) → [انتظار التحصيل]
   → PDC Transactions (تحديد + Post) → Debit: Bank/Cash / Credit: PDC Receivable → GL
   (أو Deletion من قائمة PDC)
```

## 3. دورة Sales Journal اليومية (FO/POS)

```
Day End في FO → Open New Date → (يدوياً) Post FO to Finance
   → عرض مجمعة (Account/Revenue/Audit Code + D/C + SL + Amounts)
   → توازن (فرق=0) → Save → GL
   └─ فرق ≠ 0 → Yes → Suspense (No Transaction) مؤقتاً → إصلاح الروابط → re-process
```

## 4. دورة Purchase Journal

```
GRN/Service Work Order (في MM) + Bill No/Date → PJV (Regular/Service)
   → تحديد الكميات (كلي/جزئي) → حسابات Debit (من الرابط، قابلة للتغيير)
   → Payable Control Account → Save → GL → أساس دفع الموردين
   └─ Consolidate PJV: عدة GRR في قيد واحد (شرط INV Switch 3)
```

## 5. دورة الشيك الصادر

```
Cheque Book Master (توليد أرقام بحالة open)
   → Payment Entry (رقم آلي إذا INI 504=0) → طباعة → **قفل القيد**
   → Cancel Cheque (سبب إلزامي) للتراجع
   → Bank Reconciliation: realized/unrealized (سبب) عند كشف البنك
```

## 6. دورة السنة المالية

```
تعريف FY (6-24 شهراً) → قيد طبيعي (شهر بشهر) → Audited=Yes شهرياً (قفل تدريجي)
   → Open Financial Year: أرصدة إقفال → افتتاحية + صافي P&L → Retained Earnings
   → [مقفل] — التعديل فقط عبر Rollback Fin. Year ثم إعادة Open
```

## 7. حالات موثقة أخرى

| المستند | الحالات/الأحداث | المصدر |
|---|---|---|
| Vendor Bill | فاتورة → موسومة بـ Payment Match (Yes) → مسواة | FAS-TRN §5 |
| TDS Entry | قيد خصم → untagged → وسم (Challan) → Form 16A | FAS-TRN §6 |
| Budget | تعريف (Apportion/Fixed) → Actuals تلقائية | FAS-TRN §4 |
| Contract Debit Note | GRR فرق سعر → Debit كامل/جزئي (الباقي waived) | FAS-TRN §L |
| Pending Postings | معلّق → Regular/Service PJV → Post | FAS-TRN §1N |
