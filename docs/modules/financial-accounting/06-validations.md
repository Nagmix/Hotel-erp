# 06 — التحققات (Validations) — وحدة FAS

> معرفات V-FA-XX. التمييز: تحقق قبول (يُرفض الإدخال) vs تحقق توازن (يُرفض الحفظ) vs تحقق هيكلي (يمنع العملية).

| ID | التحقق | النوع | الرسالة/السلوك الموثق | المصدر |
|---|---|---|---|---|
| V-FA-01 | Receipts: أول إدخال أصل Bank/Cash | قبول | يعرض قائمة الحسابات المفلترة | FAS-SET §3 |
| V-FA-02 | Payments: آخر إدخال أصل Bank/Cash | قبول | — | FAS-SET §3 |
| V-FA-03 | Sales: آخر إدخال دخل غير بنكي | قبول | — | FAS-SET §3 |
| V-FA-04 | Purchase: أول التزام / آخر مصروف (بلا Cash/Bank) | قبول | — | FAS-SET §3 |
| V-FA-05 | Journal يرفض Cash/Bank | قبول | — | FAS-SET §3 |
| V-FA-06 | Exchange: Cash/Bank فقط | قبول | — | FAS-SET §3 |
| V-FA-07 | **D = C لكل قيد** | توازن | يُمنع الحفظ | FAS-TRN §E |
| V-FA-08 | **undistributed = 0 في Post FO** | توازن | شاشة فرق → Yes → Suspense | FAS-TRN §G |
| V-FA-09 | تاريخ المعاملة داخل سنة مفتوحة | هيكلي | "will not be accepted" | FAS-TRN §E |
| V-FA-10 | Control Account → Sub Ledger إلزامي | قبول | في الروابط الستة | FAS-SET §6-§11 |
| V-FA-11 | روابط POS/MM/Membership: **بلا Cash/Bank** | قبول | "Only non-Bank or Cash Account Heads are accepted" | FAS-SET §7/§8/§10 |
| V-FA-12 | رابط الشراء: أصل للشراء/مصروف للاستهلاك (+CC/Dept) | هيكلي | Note §8 | FAS-SET §8 |
| V-FA-13 | Link Exempt Tax: **التزام/مصروف فقط، بلا Cash/Bank** | قبول | — | FAS-SET §23 |
| V-FA-14 | AR: Sundry Debtors = Client/Others (مع ACR: Client/GENERAL) | هيكلي | يُفعّل بـ FAS Switch 4 | FAS-SET §11 |
| V-FA-15 | PDC: القبول **Cash/Bank فقط** عند الترحيل | قبول | — | FAS-TRN §F |
| V-FA-16 | **Bill No/Date إلزاميان في PJV** | هيكلي | "mandatory" | FAS-TRN §H |
| V-FA-17 | PJV: Effective ≤ اليوم؛ المجمعة: ≥ GRR Date | هيكلي | — | FAS-TRN §H/§I |
| V-FA-18 | **Audited=Yes يقفل شهر القيد** | هيكلي | — | FAS-SET §18 |
| V-FA-19 | الشيك المطبوع غير قابل للتعديل/الحذف | هيكلي | Cancel Cheque فقط | FAS-TRN §7 |
| V-FA-20 | سنة جديدة بلا Document Number Type → **منع القيد** | هيكلي | "without which entry of transactions will not be allowed" | FAS-SET §3 |
| V-FA-21 | حساب Account Code عليه معاملات → **لا تعديل الكود** | هيكلي | — | FAS-LUK §7 |
| V-FA-22 | Vendor Stop Payment=No → **يمنع الدفع** | هيكلي | "the system will not allow you to make any payments" | FAS-MST §1 |
| V-FA-23 | TDS Applicable الاختياري يتطلب **Module Attribute 9 = Yes** | هيكلي | — | FAS-MST §1 |
| V-FA-24 | Short Name إلزامي في Account Head | قبول | "The entry of the Short Name... is mandatory" | FAS-MST §1 |

## مصفوفة رسائل موثقة

| السياق | النص/السلوك |
|---|---|
| Post FO بفرق | شاشة الفرق → **Yes → يرحّل للـ Suspense** |
| Consolidate PJV نجاح | "Records Updated Successfully" |
| الترقيم الفارغ | يبدأ من 1 (مع أصفار إذا Prefill=Yes)؛ Starting=1 → يبدأ من 2 |
