# 14 — نموذج البيانات (Data Model) — وحدة ACR

> 24 كياناً موثقاً + العلاقات. الكيانات بحقولها الموثقة نصاً (Field-level من الأدلة). التسمية مبدئية للنظام المستهدف (Arabic-first UI/RTL — لكن أسماء الكيانات لاتينية).

---

## 1. الكيانات الأساسية (Core)

### ARTransaction (كيان القيد الموحد)

| الحقل | النوع/القاعدة | المصدر |
|---|---|---|
| doc_no | **آلي** (بعد الحفظ) | ACR-OPR §1 ص2 |
| company_code | FK Company (F1) | ص2 |
| outlet_code | FK Outlet | ص3 |
| property_code | FK Property | ص3 |
| bill_no / bill_date | نص + تاريخ (**≤ اليوم**) | ص3 |
| currency | FK Currency | ص3 |
| exchange_rate | **قراءة فقط** (Exchange Entry) | ص3 |
| amount / value | رقم + محلي محسوب | ص3 |
| commission_pct / commission_amount | اختياري (وكلاء/بطاقات) | ص3 |
| net_amount | محسوب = value − commission | ص3 |
| cc_type / cc_no / auth_no | إلزامي إن بطاقة | ص3 |
| description | ≤100 alphanumeric | ص3 |
| entry_mode | **automatic** (FO/POS/BQT/MEM) / **manual** | ص2+ص4 |
| doc_class | **Debit / Credit / Adjustment** (أزرار الشاشة) | ص4+ص7 |
| source_doc | مرجع فاتورة المصدر (FO/POS — للعارض) | ص9 |

### Receipt (امتداد Credit)

| الحقل | القاعدة | المصدر |
|---|---|---|
| receipt_no | آلي (Attr#1=Yes) أو **يدوي فريد** | ACR-OPR §1 ص5 |
| receipt_date | تاريخ | ص5 |
| allocation_state | **direct / unallocated** (Attr#6) | ص4 |
| payment_mode | **cash / cheque / card** | ص3-4 (SET §2 ص4-6 مثله) |
| bank_name / branch / place / cheque_no / cheque_date | مع الشيك (+ قائمة بنوك) | ACR-OPR §1 ص3 |
| local_vs_outstation | علم الشيك | ACR-SET §2 ص6 |
| bill_matchings[] | → BillAllocation | §2 |

### BillAllocation (المطابقة)

| الحقل | القاعدة | المصدر |
|---|---|---|
| receipt (1) × bills (N) | إيصال واحد بكل عملية | ACR-OPR §2 ص11 |
| adjusted_amount | **قابل للتحرير** | ص11 |
| calculated_amount | مكافئ محلي معروض | ص5+ص11 |
| settlement_rate | **سعر تاريخ الفاتورة** | ص6 |
| status_flag | Y عند الإتمام | ص6 |
| untagged | علم فك المطابقة | §6 ص19 |

### AdjustmentEntry

| الحقل | القاعدة | المصدر |
|---|---|---|
| adjustment_no / date | يدوي | ACR-OPR §1 ص8 |
| amount | **موقع**: + مدين / − دائن | ص8 |
| target_bill | **فاتورة موجودة حصراً** | ص7-8 |
| journal_class | **JV Debit / JV Credit** | ص8 |
| commission | **ممنوع** | ص8 |
| merge_display | يظهر مدمجاً بالفاتورة كسجل واحد | ص8 |

### CompanyProfile — راجع `01-master-data.md` §1 (33 حقلاً في 6 مجموعات)

**مفاتيح جوهرية لـ AR:** credit_limit · allow_credit · credit_days · interest_pct · bypass_invoice · invoice_currency · commission_pct · collection_executive · black_listed(+reason+authorizer) · watch_list(+to_date).

## 2. كيانات الإعداد والدورات

| الكيان | الحقول الموثقة | المصدر |
|---|---|---|
| **ARStartConfig** | start_mmyy (**immutable**) | ACR-SET §1 ص1-2 |
| **OpeningBalanceEntry** | company/outlet/property/bill/currency/xrate/amount/commission/net + doc# آلي + class D/C/A + mode (cash/cheque/card) | ACR-SET §2 ص4-6 |
| **AgingDefinition** | type=Receivable · effective_from (≥ اليوم) · periods[] {to_day, from_day آلي, interest_criterion (4 نظامية), factor, print_text} | ACR-SET §3 ص8-9 |
| **ARUserAccess** | user × {debit, credit, adjustment, post} = Yes/No (افتراضي No) | ACR-SET §4 ص9-10 |
| **SOAPeriod** | month_mmyy · status (open/closed) · **متسلسل** | ACR-OPR §7-§8 |
| **BankRef** | bank_name + branch + place | ACR-SET §2 ص6 |
| **PurgeConfig** | cutoff_days ≥ 60 | ACR-SET §7 ص18 |
| **ACRAuditRecord** | snapshot + status (Del/Old/New) + user + date | ACR-RPL §11 ص20 |

## 3. كيانات الفوترة والمتابعة

| الكيان | الحقول الموثقة | المصدر |
|---|---|---|
| **Invoice** | invoice_no (نطاقات) · company · as_on · currency · bill_spec · copies · aging_flag · email_flag · address_mode (company/billing/new) · status (billed/cancelled) | ACR-BIL §2 ص3-6 |
| **MonthlyInvoiceStatement** | company_range · as_on_mmyy · spl_instructions · (pgm_id من SYS إلزامي) | ACR-BIL §1 ص2 |
| **ReceiptVoucher** | receipt_range · receipt_date · comments ☐ · consolidate ☐ · format | ACR-BIL §3 ص6-7 |
| **BalanceConfirmation** | company_range · as_on · currency · reference_text/number · balance_options | ACR-BIL §4 ص7-8 |
| **FollowUp** | company · tagged_bills[] · activity_date · total_amount · assigned_to · remarks · next_followup (date+time) · projection_amount (قابل للتعديل) · projection_period · payment_status · status (open/closed) | ACR-CRT ص3+ص7 |
| **CCConsolidationGroup** | company (CC) · date · bills[] · group_no (يدوي) — **عرضي فقط** | ACR-OPR §4 ص13-14 |
| **CommissionSetting** | bill-level commission_pct (يحدَّث في القيد) | ACR-OPR §3 ص13 |

## 4. علاقات الكيانات (ERB)

```
CompanyProfile 1──N ARTransaction (doc_class D/C/A)
CompanyProfile 1──N OpeningBalanceEntry
CompanyProfile 1──N FollowUp
CompanyProfile 1──N Invoice
CompanyProfile N──1 CompanyType (بادئة الكود — من FO)
CompanyProfile N──1 HoldingCompany (self-ref)
CompanyProfile N──1 RevenueDiscountMaster
CompanyProfile N──1 CollectionExecutive (User)
Receipt 1──N BillAllocation N──1 ARTransaction(Debit/Bill)
ARTransaction 1──N AdjustmentEntry (مدمجة عرضياً)
SOAPeriod 1──N ARTransaction (قفل زمني)
FollowUp N──N ARTransaction (tagged_bills)
CCConsolidationGroup N──N ARTransaction (عرضي)
Invoice N──N ARTransaction (الفواتير المفوترة)
AgingDefinition 1──N AgingPeriod
User N──N ARUserAccess(محور الأنواع الأربعة)
```

## 5. قيود التصميم المستنتجة (Design Constraints)

| # | القيد | الأساس الموثق |
|---|---|---|
| C-AR-1 | **doc_no آلي غير قابل للتوليد اليدوي** — تسلسل مستمر | ACR-OPR §1 ص2 |
| C-AR-2 | **receipt_no فريد** (يدوياً أو آلياً) | ACR-OPR §1 ص5 |
| C-AR-3 | **الفاتورة الواحدة تُطبع مرة واحدة** (invoice_no unique per bills-set) | ACR-BIL §2 ص6 |
| C-AR-4 | **SOA تسلسل شهري صارم** (لا فجوات) — حالة سابقة مغلقة شرط للمعالجة | ACR-OPR §7 ص21 |
| C-AR-5 | **المطابقة: إيصال ⊆ شركة واحدة** | ACR-OPR §2 |
| C-AR-6 | **Adjustment ⊆ فاتورة موجودة** + بلا عمولة | ACR-OPR §1 ص7-8 |
| C-AR-7 | **company_code 7 خانات: 3 نوع + 4 حرة** | ACR-SET §5 ص11 |
| C-AR-8 | **Audit نسختان للمعدل** (Old + New) وحالة للمحذوف (Del) | ACR-RPL §11 ص20 |
| C-AR-9 | **دورة حياة الإيصال قابلة للعكس** (untag) — الحالة لا تُحذف بل تُعكس | ACR-OPR §6 |
| C-AR-10 | **التجميع البنكي عرضي** — لا دمج فعلي للقيود | ACR-OPR §4 ص13 |
