# 16 — الربط مع ERPNext/Frappe (Seed Mapping) — وحدة FAS

> **تذكير معماري:** ERPNext/Frappe طبقة داخلية غير مرئية للمستخدم النهائي. هذا الربط إرشادي (Seed Mapping) لاختيار DocTypes/بنى قريبة سلوكياً — القرار النهائي في Phase 11/13.

## 1. مصفوفة الربط الأولية

| مفهوم FortuneNext | DocType/بنية ERPNext المقترحة | التصنيف | ملاحظات الفجوة |
|---|---|---|---|
| Main Head / Sub Head | **Account (root + tree)** | **A: مطابق مباشر** | ERPNext يعتمد Account tree واحد؛ التقسيم الثلاثي يُمثل بـ is_group + parent_account |
| Account Head (COA) | **Account** (leaf) | A | GL Type → `account_type` (Cash/Bank/Receivable/Payable...)؛ `account_number` (5-8) |
| Account Category (Assets/Liab/Inc/Exp) | root accounts القياسية | A | — |
| Sub Ledger | **إما حسابات فرعية في الشجرة أو Customer/Supplier كـ party** | **C: قرار تصميمي** | FortuneNext يربط SL بحسابات متعددة؛ ERPNext يربط Party بحساب سيطرة واحد |
| FATransaction | **Journal Entry (+ child lines)** | **A** | doc_no آلي بنمط naming_series (يدعم prefix/zero-fill/دوريات إعادة الترقيم جزئياً) |
| Book Types (9) | **voucher_type** (Journal Entry) مخصص | **B: تخصيص** | Receipts/Payments → Payment Entry أيضاً؛ قواعد التحقق D/C تُعاد بناؤها server-side hook |
| Receipts/Payments | **Payment Entry** | B | تحقق أول/آخر إدخال Bank/Cash يُنفذ validation مخصص |
| Purchase Journal (PJV) | **Purchase Invoice** (bill_no/date إلزامي) | **A** | Update Stock/Expense accounts من Item default — يقابل رابط MM |
| Contract Debit Note | **Purchase Invoice (is_return)** أو Debit Note | B |
| Sales Journal (من FO/POS) | **Sales Invoice مجمعة أو Journal Entry يومي** | **C: قرار معماري مركزي** | قرار المرحلة 13: ترحيل مجمّع يومي (كما FortuneNext) أم فواتير مفصلة |
| PDC | **Payment Entry مؤجلة + حالة** أو Payment Schedule | **C** | PDC Receivable/Payable → حسابات وسيطة مع سجل حالة |
| Bank Reconciliation | **Bank Reconciliation (ERPNext)** + Bank Transactions | **B** | وسم realized/unrealized يقابل matching/إلغاء matching |
| Cheque Book Master | **Cheque Book (Print Format)** | B | تنبيه الحد الأدنى custom |
| Financial Year | **Fiscal Year + Period Closing Voucher** | **A** | Audited شهرياً → Period Closing شهري (يدعم ERPNext تقنياً) |
| Open Financial Year | **Period Closing Voucher (تلقين أرصدة)** | **B** | نقل صافي P&L لـ Retained Earning آلياً في ERPNext مبسّط عن FortuneNext |
| Rollback Fin. Year | **إلغاء Period Closing (cancel)** | B | أثر مقلوب قابل للتنفيذ |
| Budget | **Budget (ERPNext)** (monthly/by CC/Dept≈Cost Center) | **B** | Apportion/Fixed يقابل التوزيع الشهري |
| Vendor Master | **Supplier** (+ Supplier Category، contacts، tax details) | **A** | Black list/Stop Purchase/Stop Payment → custom fields/state |
| TDS (Nature/Link/Defaults/Tagging) | **India-specific: Tax Withholding + Party** | **C: توطين** | النظام العربي: ضريبة استقطاع محلية — تُعاد ترجمة النموذج حسب الدولة |
| Interactive Payment Match | **Payment Reconciliation / Payment References** | **B** | Advance settle = prepayments matching |
| User Reports | **Query Report / Report Builder + Custom Script** | **B** | Group/Formula/Report Linking أقرب لـ script reports |
| Statistics Master/Txn | **نمط حسابات إحصائية** | **D: بناء خاص** | ERPNext بلا ماستر إحصاءات مكافئ (يمثل بـ KPI مخصص) |
| Revenue Type "No Transaction" (Suspense) | **حس suspense عادي** | A | نمط محاسبي قياسي |
| Round Off منفصل (Local/Foreign) | **حسابات Round Off** | A |
| Transaction Type Rights | **Role Permissions + DocType perms + custom** | B | تدرج 3 مستويات → سلسلة اعتماد ERPNext (workflow) |
| Cost Center/Department | **Cost Center + Department (ERPNext)** | A | ربط CC→Dept يقابل structure |
| Trial Balance Print Order | Print settings/custom | D |

## 2. قواعد تحقق يجب إعادة بنائها server-side (غير موجودة قياسياً في ERPNext)

1. Book Type rules (Receipts أول Bank/Cash... ) — hook `validate` على Journal Entry/Payment Entry.
2. **إلزام Sub Ledger مع Control Account** — يقابل party obligation (ERPNext يفرض party لحسابات Receivable/Payable قياسياً — نقطة قرب جيدة).
3. **قفل Audited الشهري** — Period Closing + منع التعديل (ERPNext يدعم بالـ submitted docs + accounting dimension).
4. **undistributed=0 + إعادة معالجة** — لا مكافئ مباشر؛ يُبنى كتحقق ما قبل الترحيل في طبقة التطبيق.

## 3. تصنيف A-F المستخدم

- **A مطابق مباشر** (≈30%): الشجرة، القيود، الموازنات، الموردون، السنوات.
- **B تخصيص معتدل** (≈40%): أنواع القسائم، تسوية البنك، حقوق الاستخدام.
- **C قرار معماري** (≈15%): آلية ترحيل FO/POS (مجمعة أم مفصلة!)، Sub Ledger semantics، TDS.
- **D بناء خاص** (≈10%): الإحصاءات، أوامر الطباعة، مصمم التقارير العميق.
- **E**: خارج النطاق الحالي (FAS-REP تفاصيله عند قراءتها).
