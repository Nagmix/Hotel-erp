# 16 — Seed Mapping إلى ERPNext/Frappe — وحدة Materials Management

> **أعلى وحدة قابلية إسقاط مباشر على Stock/Inventory في ERPNext** — لكن بفجوات نوعية (WA/FIFO لكل مخزن · FEFO · DPR · دورة عطاءات · Vendor الغني · إقفال شهري). التصنيف: **A = مطابقة مباشرة · B = تخصيص حقل · C = DocType مخصص · D = بنية فرابي بديلة · E = هيكل مخصص · F = قرار معماري**.

---

## 1. جدول المطابقة الأساسي

| # | كيان FN6i | نظير ERPNext/Frappe | التصنيف | ملاحظات/القرار |
|---|---|---|---|---|
| 1 | Store (Main/Sub/Independent) | **Warehouse** | **B/F-MG-9** | ERPNext: Warehouse parent-child — مطابقة هيكلية ممتازة (Sub = child of Main؛ Independent = root)؛ **يضاف** `custom_store_type` + `custom_rate_calc` |
| 2 | RateCalc (WA/FIFO) | Stock Settings (valuation method **global**) | **C/F-MG-1** ⭐ | **فجوة جوهرية:** FN يجعل التقييم **خاصية مخزن**؛ ERPNext 15 خيار شامل — الحل: `custom_rate_calc` على Warehouse + Batch valuation معالجة مخصصة (FIFO/FEFO عبر Batch) |
| 3 | FIFO الأصلي (إصدار بأقرب انتهاء) | Batch/Serial Bundle | **B/F-MG-2** ⭐ | ERPNext يدعم batch+expiry؛ **إلزام FEFO الصريح** في Pick List/Issue عبر hook فرز الدفعات |
| 4 | Item | **Item** | B | + `custom_item_type` (Stockable/NonStock/Cash/Butchery → mapping إلى is_stock_item/is_purchase_item + custom) + Part# = manufacturer_part_number تقريباً |
| 5 | ItemCode رقمي ≤12 (INI 39) | Item.item_code (text) | B | قاعدة توليد رقمي تسلسلي — B/V Constraint |
| 6 | SubCode | **Item Variant** أو Item UOM conversion | **D/F-MG-10** | فرادى التعبئة/السعر — أنسب: Item مع `custom_sub_of` (بسيط) — الـ Variant أثقل من الحاجة |
| 7 | ItemGroup | **Item Group** | A | + `custom_group_type` (FNB linkage) |
| 8 | ItemLocation | Warehouse Location custom | C | `custom_item_location` (متحقق) |
| 9 | ItemStockLevel (ReorderLevel/Qty) | **Item Reorder** (Reorder level tab!) | A- | ERPNext Reorder في Item نفسه (warehouse-specific!) — مطابقة ممتازة + أعلام 3 اتجاهية custom |
| 10 | OpeningBalance | **Stock Reconciliation** (opening) + Batch | B | مع تجميد post-transaction (تحقق) |
| 11 | Vendor | **Supplier** | **B/C/F-MG-2** ⭐ | الأساس A؛ لكن 7 عائلات فرعية → `PMS Vendor Profile` child tables + custom fields (بحث §3) |
| 12 | CompanyTypes (FO) | **Supplier Group** | **F-MG-11** | قرار ملكية مشترك: Supplier Group (MGT/AR) أو تعريف FO — يُحسم في Phase 11 مع AR |
| 13 | VendorRating | Supplier custom field/rating | C | بسيط (code/seq) |
| 14 | TermsOfPayment | **Payment Terms Template** | B | + Grade Sequence custom (Vendor Analysis) |
| 15 | VendorContract | **Contract** (Frappe) | B | مع type=Purchase |
| 16 | VendorItem (Normal/Contract + LastRate آلي) | **Item Supplier** (Item-Supplier link + last purchase rate آلي!) | **A-** ⭐ | ERPNext: Item Default/Supplier جزء — last_purchase_rate يتحدث تلقائياً (مطابقة مذهلة لسلوك Normal)؛ Contract → Contract link إضافي |
| 17 | IndentTemplate | `PMS Indent Template` | C | قائمة أصناف لكل CC/Dept — لا نظير |
| 18 | PR (Purchase Requisition) | **Material Request** (type=Purchase) | **A** ⭐ | مطابقة قوية + workflow تفويض 1/2/3 (Workflow states) — F-MG-3 |
| 19 | Indent (طلب صرف CC) | **Material Request** (type=Material Issue) | A | الأدوار: PR=Purchase، Indent=Issue — كلاهما Material Request بأنواع |
| 20 | DPR (آلي من نقص) | Material Request توليدي | **E/F-MG-6** | hook: issue مع nil balance → PR — أتمتة مخصصة |
| 21 | Re-Order Process | ERPNext Reorder (في Material Request? — عبر Item Reorder) | **E/F-MG-6** | Reorder level موجود؛ **الجولة الدورية (Process # + Update + Post)** تحتاج scheduled job + زر |
| 22 | Quotation Cycle (7 وظائف) | Supplier Quotation (جزئي!) | **C/F-MG-5** | Invite/Tender/Compare موجودة جزئياً؛ Evaluation/Analysis/Close → `PMS Vendor Evaluation` مخصص |
| 23 | PO | **Purchase Order** | **A** ⭐ | + Consolidate Discount + Other Details custom + Misc Tax (Taxes child) |
| 24 | SPO | Purchase Order متكرر / **Blanket Order** | **D** | Blanket Order (Frappe) = SPO تقريباً (نطاق صلاحية + Fixed/MRP → rate rule custom) |
| 25 | SWO | **Purchase Order** (خدمة) أو Purchase Invoice service | D | items بلا مخزون (service) |
| 26 | Receipt (GR) | **Purchase Receipt** | **A** ⭐ | أنواع الثلاثة = PR/PO/SPO reference؛ **Bill# = bill_no موجود!** + DS# = custom |
| 27 | Bill#/Date → Payment Match | Purchase Invoice (bill_no) + **Payment Match** | **A** | جسر المواءمة المالي قياسي تماماً |
| 28 | Issue (Direct/Indent) | **Stock Entry** (Material Issue) | A | + Batch اختيار FEFO (F-MG-2 hook) |
| 29 | Receipt Return | Stock Entry (Material Receipt سلبية) / **Purchase Return** | D | الأنسب: Purchase Receipt return |
| 30 | Issue Return | Stock Entry (Material Receipt من CC) | B | s_batch/backdate rules |
| 31 | Adjustment | **Stock Reconciliation** / Stock Entry (Repack) | B | qty/value ± + Adjustment Type reason |
| 32 | Conversion Split/Add | **Stock Entry (Repack)** | **A-** | Repack = التحويل التصنيعي! + Yield% + Component Cost (custom) |
| 33 | Inter/Sub Store Transfer | **Stock Entry (Material Transfer)** | **A** ⭐ | مطابقة مباشرة (مع تحقق الهرمية F-MG-9) |
| 34 | Cost Center Transaction | Stock Entry مع CC dimension | B | CC = accounting dimension |
| 35 | Physical Stock Entry | **Stock Reconciliation** | **A** ⭐ | المطابقة الأقوى في الوحدة |
| 36 | Stock Variance Updation | Stock Reconciliation (post) + custom auto | **E** | "alerting checked report" + auto adjustments → `custom_variance_post` hook |
| 37 | Process Store Ledger | **Accounts Stock Balance ledger freeze** | **E/F-MG-8** | لا نظير مباشر — قرار: Period Closing + custom `custom_store_ledger_status` على Warehouse×period |
| 38 | Variance Cost Center | Warehouse → CC (variance) | B | custom: `custom_variance_cc` على Warehouse (مطابقة ERPNext stock adjustment account concept) |
| 39 | Budget | **Budget** (ERPNext) + Monthly distribution | **B** | Fixed=manual؛ **Apportion = Monthly Distribution** (موجود!) + F2/F4 (نسخ CC) → client script |
| 40 | FSN | Report مخصص | E | cut-off/fast/slow rules في `PMS FSN Rule` |
| 41 | Tax Exemption / Item Tax | **Purchase Taxes and Charges Template** + Item Tax | B | import tax variation |
| 42 | AccessRights (4D) | User Permissions + custom backdate | **C/F-MG-4** | Store=Warehouse perm؛ Option=DocPerms؛ CC=User Perm؛ Backdate=custom |
| 43 | FootNote/EmailAccess | Print Settings + **Notification** | A/D | قوالب بريد قياسية (F-MG-8) |
| 44 | Purging | **Bulk delete / auto archive** | D | + هدف "auto-generated only" (فلتر is_auto=1) |

## 2. القرارات المعمارية (F-MG-1..12)

| # | القرار | المبرر |
|---|---|---|
| **F-MG-1** ⭐ | `custom_rate_calc` على Warehouse + تقييم تنفيذي مخصص عند الإصدار (WA حسابي أو FIFO/FEFO دفعي) — **التقييم خاصية مخزن** | FN موثق: "The Rate Calculation i.e. the method of valuation **has to be specified for the defined Store**" — تعارض مباشر مع ERPNext global؛ الأمان المالي يتطلب الوفاء بنموذج FN |
| **F-MG-2** | FEFO hook إلزامي لكل عمليات إصدار الأصناف ذات Batch/Expiry (فرز بانتهاء الصلاحية تصاعدياً) | نص صريح: "prioritized to disperse based on their **expiry dates**" + "ascending order" |
| **F-MG-3** | توحيد التفويض المتدرج (0-3) لكل PR/Indent/PO في Workflow States — إسقاط INV #13/#14/#298 لصالح مفتاح متدرج واحد لكل مستند | ازدواجية FN (مفتاح متدرج لـ PR + 3 ثنائية لـ PO) — اعتماد الأنظف |
| **F-MG-4** | `custom_backdate_days` (JSON per doctype) على User/Role + `validate()` hook بالتاريخ | إحياء البعد الرابع الموثق (أيام لكل نوع معاملة) |
| **F-MG-5** | `PMS Quotation Cycle`: توسيع Supplier Quotation + `PMS Vendor Evaluation` + `PMS Quotation Comparison` | دورة العطاءات السبعية بلا تغطية قياسية |
| **F-MG-6** | hook DPR + Re-Order scheduled job (آلي: nil balance → PR؛ reorder level → PR للقسم) | أتمتة موثقة A-MG-01/02 |
| **F-MG-8** | Process Store Ledger = **Period Closing Stock** مخصص: تجميد (ledger_status per Warehouse×month) + Cancel | النمط الثلاثي للتجميد (FO يومي/FAS سنوي/MGT شهري) يتطلب مساراً موحداً بحالة مستقلة |
| **F-MG-9** | Store→Warehouse مع User Permission + تحقق الهرمية (Sub يستلم من Main فقط) في Stock Entry validate | مطابقة هيكلية + فرض قاعدة FN الدستورية |
| **F-MG-10** | SubCode = `custom_sub_of` على Item (وليس Variant) + قاعدة UOM | أخف وأمين للنموذج الأصلي |
| **F-MG-11** | Company Type (مصدر FO) → **Supplier Group** مشترك مع AR — تعريف واحد يستهلكه الموردون والشركات | توحيد كيان الكود TTT+XXXX عبر MGT/AR (يُحسم نهائياً في Phase 11) |
| **F-MG-12** | Misc Tax/أعلام الأصناف الاتجاهية (Issue/Receipt/Return Allowed) كحقول custom مع تحقق حركة | أوفياء للنموذج الأصلي بأدوات قياسية |

> **(F-MG-7 محجوز: إسقاط قاعدة "9 أيام دفع"** → Payment Schedule مخصص — يُفصّل عند قراءة FAS-TRN كاملاً في Phase 6.)

## 3. Vendor Profile الموسع (تفصيل F-MG-2)

```
Supplier (أساس قياسي)
 ├── custom fields: rating · blacklisted(+) · stop_purchase · stop_payment · category · state_type · tds_applicable
 ├── PMS Vendor Payment Details (child): credit_days · credit_limit · advance_pct · payment_type ·
 │    frequency (Adhoc/Daily/**Fixed→fixed_days JSON ≤9**) · 5 discount slabs · interest slabs
 ├── PMS Vendor Bank (child): bacs · sort_code · transaction_limit · cheque_favor
 ├── PMS Vendor Contact (child ≤2)
 ├── PMS Vendor Tax (child): tax_code · number · issue_date/place
 ├── PMS Vendor TDS (child): nature (multi) · deduction_account · PAN/GIR
 └── PMS Vendor Other (child): 20 حقلاً (org + تجاري + Penalty% ...)
```

## 4. إسقاط الترقيم (Naming Series)

| FN | Frappe Naming |
|---|---|
| PR Request# → `MAT-REQ-.YYYY.-` | Material Request قياسي |
| Indent# → `INDT-.YYYY.-` | Material Request (type=Issue) بسياق منفصل أو `PMS Indent` |
| PO#/SPO#/SWO# → `PUR-ORD-.YYYY.-` / `PUR-SPO-.YYYY.-` / `PUR-SWO-.YYYY.-` | — |
| GR#/GRR# → `MAT-RCV-.YYYY.-` + مرجع مرتجع | — |
| Quotation# → `PUR-QTN-.YYYY.-` | Supplier Quotation |
| Doc# (Issue) → `STE-.YYYY.-` | Stock Entry |

## 5. تقييم الجاهزية

- **قابلية إسقاط عالية:** PR/Indent/PO/Receipt/Issue/Transfers/Physical Stock (كل عائلة Stock Entry قياسية!).
- **تخصيص إلزامي:** التقييم للمخزن (F-MG-1) · FEFO (F-MG-2) · دورة العطاءات (F-MG-5) · الإقفال الشهري (F-MG-8) · Vendor الغني.
- **مفاجآت إسقاط إيجابية:** Item Reorder (Reorder Level/Qty per warehouse موجود!) · Item-Supplier last rate آلي · Stock Reconciliation = Physical Stock · Repack = Conversion · Payment Match/Bill# قياسي.
