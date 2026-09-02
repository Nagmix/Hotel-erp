# 09 — الاستعلامات واللوحات (Lookups) — وحدة ACR

> ACR-RPL يميز تقارير من استعلامات تفاعلية؛ وهنا تجريد الاستعلامات التفاعلية والنوافذ المساعدة (Help) الموثقة في كل الملفات الخمسة. **ملاحظة معمارية:** استعلامات ACR تفاعلية التنقيب (drill-down) — عمق 4 مستويات في Debtors Follow-Up.

---

## 1. الاستعلامات التفاعلية (من RPL)

| ID | الاستعلام | السلوك التفاعلي الموثق | المصدر |
|---|---|---|---|
| L-AR-01 | **A/C Balance Query** | اختيار شركة → عرض شهري (افتتاحي/مدين/دائن/إجمالي) + أنواع I/R/A + **زر Merge** لتوحيد الفواتير بسند واحد | ACR-RPL §17 ص26-27 |
| L-AR-02 | **Outstanding Snapshots** | عرض: Opening/Debit/Credit/Closing/Credit Limit/**Variance** لكل حساب أو نوع مجمَّع | ACR-RPL §18 ص27-29 |
| L-AR-03 | **Receipts Display** | قسمان: **Credit** (الإيصالات) فوق و**Debit** (الفواتير المطابَقة) تحت — أو عرض الدفعات المقدمة | ACR-RPL §19 ص29-30 |
| L-AR-04 | **Browse Transactions** | بحث بـ 8 معايير + تنقل **Prev/Next** بين القيود | ACR-RPL §20 ص30-32 |

## 2. نافذة التنقيب العميق (Debtors Follow-Up Drill) — ACR-CRT

> **أعمق سلسلة تنقيب موثقة في النظام حتى الآن (4 مستويات):**

| المستوى | العنصر | الفعل | المصدر |
|---|---|---|---|
| 1 | قائمة قيود الشركة | عرض Transactions | CRT ص2 |
| 2 | قيد/فاتورة | Double-click → تفاصيل مدين/دائن | CRT ص3 |
| 3 | بند داخل الفاتورة | Double-click → تفاصيل القيد + **اسم الضيف** | CRT ص4 |
| 4 | المبلغ | Double-click → **تقسيم الشحنات (Charge Break-up)** | CRT ص4 |

**تبويبات إضافية:** Company Info (جهات اتصال + Add) · Follow-Up Trace (تاريخ المتابعات) · Projection Report (ص5-7).

## 3. نوافذ المساعدة (Help Windows) الموثقة

| النافذة | الاستدعاء | المحتوى | المصدر |
|---|---|---|---|
| Company Help (F1) | حقل الشركة (كل الشاشات) | قائمة الشركات + اختيار | ACR-OPR §6 ص16-17 |
| Receipt Help | حقل Receipt # في Untagging | بحث **Receipt Date (مدى)** أو **Bill #** + نتائج + اختيار | ACR-OPR §6 ص17-18 |
| Advanced Search (Debtors Follow-Up) | زار Show Advanced Search | **أولويات بحث قابلة للتخصيص** | ACR-CRT ص2 |
| Bank Details List | زر قرب حقول الشيك | قائمة Bank/Branch/Place (مُعرَّفة مسبقاً) | ACR-SET §2 ص6 + ACR-OPR §1 ص3 |
| Receipts/Bills في Match | F1/Selection Criteria | إيصالات الشركة + فواتيرها المعلقة | ACR-OPR §2 ص11 |
| FO/POS Bill Viewer | زر من Transaction Entry | **فاتورة المصدر** للقيود التلقائية (من FO أو POS فقط) | ACR-OPR §1 ص9 |
| Company Details Viewer | زر من Transaction Entry | تفاصيل الشركة + جهات الاتصال | ACR-OPR §1 ص9 |

## 4. معايير البحث الموثقة في Browse/Modify

| الشاشة | المعايير | المصدر |
|---|---|---|
| Transaction Entry — Browse | Document Number · Company · Company Name · Bill # · Bill Date · Receipt # | ACR-OPR §1 ص8 |
| Opening Balance — Modify | نفس الستة | ACR-SET §2 ص7 |
| Browse Transactions (RPL) | Bank Name · Bill #/Date · Branch · Card Number · Cheque #/Date · Receipt #/Date · Reg # | ACR-RPL §20 ص31 |

## 5. لوحات عمل المستخدم (زوايا العرض)

| الزاوية | الاستعلام | مصدرها |
|---|---|---|
| الشركة | A/C Balance Query · Ledger Balance · Folio Outstanding | RPL §17/§4/§5 |
| نوع الحساب | Balance by A/C Type · Outstanding Snapshots (Display Type) | RPL §3/§18 |
| مندوب المبيعات | Debtor Outstanding Report (Sales Exec) · Aging Summary (Sales Executive) | RPL §21/§6 |
| القطاع | Aging Summary (Sector) | RPL §6 |
| البنك | Receipt Register (Bank-wise) · Cheque Deposit Statement (Bank & Branch-wise) | RPL §14/§15 |
| المسؤول عن التحصيل | Follow-Up Trace (Assigned To) | CRT ص7 |
