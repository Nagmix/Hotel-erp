# 16 — Seed Mapping إلى ERPNext — وحدة ACR

> تصنيف A-F: **A = مطابقة مباشرة (DocType جاهز)** · **B = تكوين كافٍ (Customize/Settings)** · **C = تخصيص حقول (Custom Fields)** · **D = تطوير جانبي (Custom App light)** · **E = تطوير كبير (بناء فوق ERPNext)** · **F = قرار معماري مطلوب**.

---

## 1. خريطة الكيانات

| كيان FortuneNext | الهدف ERPNext | التصنيف | ملاحظات التنفيذ | المصدر |
|---|---|---|---|---|
| Company Profile | **Customer** (+ Contact/Address) | **A/C** | الاسم/العنوان/جهات الاتصال جاهزة؛ حقول IATA/Pan/Holding/WatchList/BlackList → Custom | ACR-SET §5 |
| بادئة كود الشركة (TTT) | **Customer Group** (أو naming pattern) | **B** | Customer Group لكل Company Type + سلسلة تسمية `TTT####` | ACR-SET §5 ص11 |
| Market Segment / Sales Executive | **Territory / Sales Person** | **A** | ربط قياسي في ERPNext | ACR-SET §5 ص12 |
| Revenue Discount Master link | **Pricing Rule** (Discount % على أصناف إيراد) | **C** | Pricing Rule per Customer × Item Group | ACR-SET §5 ص15 |
| AR Transaction (Debit) | **Sales Invoice** | **A/C** | التلقائي من FO/POS/BQT/MEM = Sales Invoice آلي عند التسوية الائتمانية؛ outlet/property → Custom + Project/Dimension | ACR-OPR §1 |
| AR Receipt (Credit) | **Payment Entry** | **A/C** | **unallocated = Advance Payment** (reference مزدوج الوجه: https://docs: paid_amount بلا تخصيص)؛ payment_mode → Mode of Payment | ACR-OPR §1 ص4 |
| BillAllocation (المطابقة) | **Payment Entry.references[]** (تخصيص المبالغ) | **A** | allocated_amount لكل فاتورة = Adjusted Amount | ACR-OPR §2 ص11 |
| Receipts Untagging | إلغاء references + إعادة Unallocated | **C** | إجراء جانبي: فك التخصيص مع Audit |
| AdjustmentEntry (+/−) | **Journal Entry** ضد Sales Invoice | **B** | JV Debit/Credit عبر Journal Entry Account rows | ACR-OPR §1 ص8 |
| Credit Limit | **Customer.credit_limit** (+ ERPNext يمنع البيع عند التجاوز إذا مفعّل) | **A** | "credit limit... settlement not allowed" — نفس السلوك في ERPNext Sales Invoice validation | ACR-SET §5 ص14 |
| Credit Days | **Payment Terms Template** | **B** | due date آلي | ACR-SET §5 ص13 |
| Interest % (تجاوز الائتمان) | **Dunning** (ERPNext AR) | **C** | Dunning Type بعتبة أيام ونسبة — مطابقة وظيفية عالية لـ Aging with Interest | ACR-SET §3 + §5 |
| SOA (إقفال شهري) | **Accounting Period** (Closed) | **A** | نفس الدلالة: "closed... cannot be modified or deleted" | ACR-OPR §7 |
| Rollback SOA | إعادة فتح Accounting Period (uncheck Closed) | **B** | + صلاحية role صارمة | ACR-OPR §8 |
| AgingDefinition | **Aging افتراضي ERPNext** (0-30/31-60...) | **C/D** | فترات مرنة + معايير فائدة لكل فترة → تخصيص تقرير | ACR-SET §3 |
| Invoice/Reprint/Cancel | **Sales Invoice** (submit/print/cancel) | **A** | Cancel = cancel invoice (نفس البوابة)؛ Reprint = print مرة أخرى | ACR-BIL §2 |
| Reminder | **Dunning** (إشعارات الذمم) | **C** | نص التذكير بقوالب Print Format | ACR-BIL §2 ص5 |
| Receipt Voucher | Payment Entry Print Format | **A** | طباعة سند القبض | ACR-BIL §3 |
| Balance Confirmation Letter | **Print Format** (Letter) على Customer Ledger | **B** | قالب HTML Jinja | ACR-BIL §4 |
| Monthly Invoice Statement | **Print Format** مجمّع لكشوف الشهر | **B** | يعمل فوق Customer/Invoice data | ACR-BIL §1 |
| FollowUp | **Dunning/ToDo/Custom DocType "Debt Follow-Up"** | **D** | التخصيص + التعيين + الموعد التالي + Projection — لا مكافئ واحد جاهز | ACR-CRT |
| Projection Report | تقرير مخصص (Query Report) | **D** | تجميع التوقعات الزمنية | ACR-CRT ص7 |
| CCConsolidationGroup | تجميع عرضي في تقرير CC Register | **D** | group_no حقلاً على القيود + تجميع التقرير | ACR-OPR §4 |
| Travel Agent Commissions | Commission في Sales Invoice + تقرير | **C** | عمولة لكل فاتورة (update في القي) | ACR-OPR §3 |
| Cheque Deposit Statement | تقرير مخصص + Bank Deposit Entry | **C** | ERPNext فيه "Bank Deposit" لتجميع الشيكات | ACR-RPL §15 |
| ARUserAccess (user×D/C/A/Post) | **Role Permissions + User Permissions** | **C/F** | أنواع القيود = doctypes مختلفة → أدوار: AR Debit Clerk/AR Receipt Clerk؛ "Post" يتطلب صلاحية submit | ACR-SET §4 |
| ACRAuditRecord (Old/New/Del) | **Versioning** Frappe (مدمج) + audit log | **A** | نفس نمط النسختين | ACR-RPL §11 ص20 |
| IDS Report Designer | **Query Report / Report Builder** | **B** | منشئ تقارير Frappe | ACR-RPL §23 |
| Print Form Designer | **Print Format Builder** (HTML/Jinja) | **A** | قوة موازية | ACR-SET §8 |
| INI #56/#74 + Module Attr 1/2/3/6 | **System Settings/Custom Flags** | **D/F** | feature flags مركزية بدلالات إيجابية | ACR-OPR/BIL/RPL |

## 2. قرارات معمارية مفصلية (F) تفرضها AR

| # | القرار | الخياران | المرجح (وسببه) |
|---|---|---|---|
| F-AR-1 | **نمط ترحيل AR→GL:** تفاعلي عند الحفظ (كالأصل) أم مركزي batch؟ | (أ) Payment Entry/Sales Invoice تُرحّل آلياً بحساباتAccounts Receivable الافتراضية (ERPNext القياسي: Sales Invoice منفصل عن الدفع) — (ب) محاكاة الشاشة التفاعلية | **(أ)** — لأن ERPNext يفصل الفاتورة عن القبض أصلاً؛ "شاشة FA عند الحفظ" كانت حل تدوين مزدوج يلغيه النموذج الأحدث |
| F-AR-2 | **مطابقة الإيصالات:** Unallocated-as-Advance (Payment Entry بلا references) أم حساب وسيط؟ | Advance (ERPNext native) أم GL clearing | **Advance** — مطابقة أصلية |
| F-AR-3 | **تسلسل SOA مقابل Accounting Period:** تطبيق القفل على مستوى Company أم Property؟ | Accounting Period شركة/property | Company + Dimension property (قرار UNK-004 المرتبط) |
| F-AR-4 | **فائدة التقادم:** حساب عرض (كالأصل) أم Dunning فعلية؟ | تقرير فقط أم مستندات متابعة | **Dunning** (يرفع القيمة الوظيفية بنفس المنطق: عتبة أيام + نسبة) |

## 3. جرد الافتراضات المطلوب تحققها عند التنفيذ

| الافتراض | أداة التحقق | المصدر |
|---|---|---|
| Credit Limit يمنع فواتير FO/POS عبر ERPNext API | فاتورة Sales Invoice تجاوزية | ACR-SET §5 ص14 |
| سعر صرف الفاتورة يثبت عند السداد (Exchange Rate محفوظ بالفاتورة) | سيناريو عملة أجنبية + سداد لاحق | ACR-OPR §1 ص6 |
| إلغاء فاتورة ملغاة التخصيص (فك مطابقة آلي) | Cancel Invoice مربوط بـ Payment references | ACR-OPR §8 ص21 |
| إعادة الطباعة ممكنة بلا قيد جديد | Print Format | ACR-BIL §2 ص6 |
