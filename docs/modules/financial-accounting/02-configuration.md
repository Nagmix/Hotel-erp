# 02 — الإعداد (Configuration) — وحدة FAS

> المصدر الرئيسي: FAS-SET (27 قسماً). الأهم معمارياً: **Transaction Types §3 (قواعد Book Type) + الروابط §6-§11 (تفصيلها في `11-accounting-impact.md`) + Financial Period §18**.

---

## 1. Transaction Types — قواعد Book Type الموثقة حرفياً (FAS-SET §3)

> **هذا الجدول هو قلب التحقق المحاسبي للنظام** (قواعد القبول عند إدخال القيود):

| Book Type | قاعدة التحقق الموثقة (الإدخال الأول Debit / اللاحق Credit) |
|---|---|
| **Receipts** | الإدخال الأول (Debit) = **حساب أصل GL Type Bank أو Cash حصراً**؛ اللاحق (Credit) = أي حساب **غير** Bank/Cash |
| **Payments** | الأول (Debit) = أصل/التزام/مصروف **غير Bank/Cash**؛ اللاحق (Credit) = **حساب أصل GL Type Bank/Cash** |
| **Sales** | الأول (Debit) = أصل أو التزام؛ اللاحق = **حساب دخل** وغير بنكي |
| **Purchase** | الأول = **التزام** غير Bank/Cash؛ اللاحق = **مصروف** غير Cash/Bank |
| **Journals** | لا قواعد محددة **عدا رفض حسابات Cash/Bank** |
| **Debit Notes / Credit Notes** | لا قواعد تحقق |
| **Exchange (Contra)** | **كل الإدخالات Cash أو Bank فقط**؛ "All the withdrawal of cash and cheque should be routed through this transaction type only" (CONTRA) |

**خصائص Transaction Code (§3 ص6-10):**

| الخاصية | الموثق |
|---|---|
| الكود | 2 رقمي فريد، **حتى 99 لكل Property** |
| التعديل | Name + Short Name + Print Details فقط؛ **كل الحقول فقط إذا لم تُدخل معاملات (أو أُدخلت ثم حُذفت جميعها)** |
| الترحيل | "Transaction Types for new fin year will be auto generated based on user selection during the creation of financial year" |
| Book Types الإلزامية | "Define Transaction Types for all the Book Types" (Note) |

## 2. ترقيم المستندات (Document Number) — FAS-SET §3

| الإعداد | الموثق |
|---|---|
| النمط | **Automatic (موصى به) أو Manual** |
| Automatic | Prefix (مثال Jan/Apr) + **Prefill with Zeroes** + **Initialization Period: Weekly/Monthly/Quarterly/Half Yearly/Yearly (شهري موصى به)** + Starting Number (8 حرف؛ فارغ = يبدأ من 1) + Restart Number |
| Manual | Prefix/Suffix فقط (10 حرف) |
| **قاعدة إلزامية** | "When a new financial year is defined, it is **mandatory** that the Document Number Type be specified for all existing Transaction Types for the new financial year **without which entry of transactions will not be allowed**" |

## 3. سلوك الطباعة والنصوص (§3)

- Print Voucher (Y/N) + **Voucher Form ID** (برنامج مخصص، مثال موثق: FA001VP) + Voucher Print Option (منفذ الطابعة LPT/USB أو اسم شبكة ≤8).
- **Particulars Required for each entry** (لكل سطر) vs للقيد كله؛ **Particulars Mandatory** (Y/N)؛ حد 250 حرفاً.

## 4. Transaction Voucher Link — §4 (ص10-11)

ربط أكواد المعاملات بأنواع القسائم **إلزامي للطباعة**: "This is a mandatory menu option because only after you link the transaction types to the relevant voucher types you will be able to print the vouchers".

## 5. مفاتيح الإعداد الموثقة الأخرى

| المفتاح | القيمة/الأثر | المصدر |
|---|---|---|
| **FAS Module Switch # 4** | "FOM to FAS Posting Required" = Yes → يفعّل تحققات Link AR (Sundry Debtors = Client/Others...) | FAS-SET §11 ص24-25 |
| **SYS Switch # 1 / # 2** | "Income to be Printed/Displayed first" / "Asset to be Printed/Displayed first" — ترتيب TB/BS الافتراضي | FAS-SET §21 ص42 |
| **Trial Balance Print Order §21** | BS: Assets/Liability أو العكس؛ P&L: Income/Expense أو العكس؛ **بدونه لا تُعرض قائمة Chart of Accounts في Reports/Lookups** | FAS-SET §21 |
| **INV Switches 1+4** | طريقة ضريبة الشراء (المشتري يتحملها/البائع) — راجع `11-accounting-impact.md` §5 | FAS-TRN §H ص22-23 |
| **INV Switch 3** | "Bill No. & Bill Date is Mandatory In Receipts" = Yes → شرط PJV المجمعة | FAS-TRN §I ص23 |
| **INI 283 `INV2FASCONSPOSTING`** | 1 = ترحيل استهلاك شهري، 2 = يومي | FAS-TRN §J ص26 |
| **INI 504 `FASTRANSAUTOCHEQUENO`** | 0 = تفعيل الترقيم التلقائي للشيكات (Cheque Book Master) | FAS-MST §4 ص31 |
| **Module Attribute 9 (TDS not Mandatory)** | Yes = يسمح باختيار TDS Applicable يدوياً للمورد | FAS-MST §1 ص11 |
| **INI 58 = 0** (FOM) | تفعيل Reservation Mode — من قراءة FOM-SET | FOM-SET |

## 6. Financial Period — §18 (ص37-39)

| الإعداد | الموثق |
|---|---|
| مدة السنة | **6-24 شهراً**؛ تبدأ بأي شهر تقويمي (Starting Month/Year → Ending يولد آلياً)؛ Starting/Ending Date قابلان للإدخال (تقويمات دول مختلفة) |
| **Audited (شهر بسطر)** | افتراضي No؛ Yes → **يُمنع إدخال/تعديل معاملات الشهر**؛ للتعديل يجب إرجاعه No |
| حذف/تعديل الجدول المالي | قبل بدء المعاملات فقط |

## 7. روابط الصلاحيات والتكامل — §5/§22

- **Transaction Type Rights §5**: Property + User (F1) → Tag Yes (أو Select All) → صلاحية استخدام كود المعاملة. راجع `07-permissions.md`.
- **Link CC to Department §22**: Department (F1) → Cost Centers → LINK? Yes → "any transactions made to the cost center will automatically reflect in the Department".
