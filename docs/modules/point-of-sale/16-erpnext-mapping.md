# 16 — Seed Mapping إلى ERPNext — وحدة POS

> تصنيف A-F (مطابقة/تكوين/حقول/تطوير جانبي/بناء/قرار معماري). **POS هي أصعب وحدة للنقل** لأن ERPNext ليس PMS-POS فندقياً — لكن بنية Restaurant/Retail قابلة للبناء فوق Sales Invoice + POS Invoice + Item.

---

## 1. خريطة الكيانات

| كيان FortuneNext | الهدف ERPNext | التصنيف | ملاحظات | المصدر |
|---|---|---|---|---|
| Outlet | **ERPNext POS Profile** (+ Company/Dimension) | **B/C** | POS Profile يجمع: المستودع/العملة/المدفوعات/الطابعات؛ department/cost_center → Dimension | POS-SET §1 |
| Outlet Session/Link | Custom **"POS Shift/Session"** (مبني على POS Closing Shift) | **D** | ERPNext 14+ لديه POS Opening/Closing Entry — يوسَّع بالجلسات | §2/§4 |
| KOT | **Custom DocType "KOT"** (مرتبط بـ Sales Invoice POS) | **E** | لا مكافئ — نواة الفصل الثلاثي (KOT→Bill→Settle) | TS |
| KOT Type/Link | Custom (نوع مستند + ترقيم) | **D** | Standard إلزامي + Auto/Book/Manual | §3/§5 |
| KOT Book | Custom DocType (≤100 ورقة + Validate) | **D** | | §30 |
| Check (Bill) | **POS Invoice** | **A/C** | دورة الترقيم (Naming) Y/M/D/N؛ الحالات مطابقة (Draft/Submitted/Cancelled + Paid) | TS + §1 |
| Settlement | **POS Invoice.payments[]** (Mode of Payment متعدد) | **A/C** | **Balance=0 = الفاتورة المدفوعة**؛ Tips → Custom؛ Guest/Room → فوليو FO (تكامل) | TS |
| Shift (Open/Close) | **POS Opening/Closing Entry** | **A** | مطابقة عالية جداً (تفاصيل الكاشير + الفتح والإغلاق) | TS ص4/46 |
| Void | POS Invoice **Cancelled** (+ سبب) | **A/C** | سبب الإلغاء custom إلزامي | TS |
| Split Check (3) | **تقسيم POS Invoice** (بنود لفواتير متعددة) | **D** | Item-wise مباشر؛ Quantity-wise كسري يحتاج سطر بحقل كمية مكسور بالفعل (Decimals) | TS ص28-31 |
| Link Tables/Suffix | Custom (دمج طاولات/فوليوهات) | **D** | دمج في فاتورة واحدة | TS ص43-45 |
| Menu Master | **Item** (+ Item Price) | **A/C** | group/menu_type → Item Group؛ rates local/foreign → **Item Price بالعملات**؛ GL Code → Income Account للصنف!؛ available_hours/preparation → Custom | §24 |
| Menu Levels (4) | **Item Group شجري 4 مستويات** | **A** | مطابقة بنيوية تامة | §11 + TS ص13 |
| Modifiers | **Item Variants أو Custom "Modifier"** | **C/D** | additional_charge → سعر variant؛ Recipe → Custom | §26/§27 |
| Kitchens | Warehouse/Custom + **Printer** | **C/D** | "Every item tagged to kitchen" → حقل مستودع الإعداد | §15 |
| Table/L/Layout | Custom **"Restaurant Table"** + Floor | **D/E** | ألوان الحالة من بيانات حية | §12/§39 |
| Happy Hours | **Pricing Rule** (زمني + %/مبلغ) | **B/C** | Validation: P للمجموعات حصراً + منع التداخل | §31 |
| Sales Promotion | Pricing Rule/Promo (Main/Addl/Comp) | **C/D** | فئات البنود الثلاث | §32 |
| Member Discount | Pricing Rule per Member × Outlet × Menu Type | **C/D** | INI 404 → نطاق | §41 |
| Revenue/Predefined Discount | Pricing Rule (Customer-linked) | **B** | من Company Profile (ACR) | TS ص26 |
| Tax Exemption (بسبب) | **Tax Template + exemption reason** | **C** | سبب إلزامي custom | TS ص27 |
| NC | Sales Invoice **Is Return/Zero** + Department + NC Cost% | **C/D** | أقسام NC كمصروف | §7/§19 + TS |
| POS Guest History | **Customer** (+ Custom tabs) | **C/F** | **قرار التوحيد مع FO Guest (UNK-001)** — راجع أدناه | POS-GST |
| Loyalty | **Loyalty Program + Loyalty Point Entry** | **A/C** | ERPNext native loyalty! خصومات منفذ×نوع → tiers/rules | GST §2/§3 |
| Guest Survey/Comments | Custom (Feedback-like) | **D** | | §38 + GST §10-12 |
| POS User Access | **Role Permissions** (كاشير×عملية) + **custom للتطبيقات** | **C/F** | Regular/Touch/PDA → منصة واحدة (F) | §20 |
| Restrict Outlet Access | **User Permissions** (POS Profile per user) | **B** | مطابقة ERPNext User Permissions | §21 |
| Print Forms | **Print Format Builder (HTML/Jinja/WK** — راجع نقطة 3) | **A/B** | أنواع Bill/KOT/NC/Invoice | §23 |
| Parameter List | System Settings report | **B** | | §24(2) |
| Area (توصيل) | Custom/UOM-like | **D** | delivery | §21(2) |

## 2. القرارات المعمارية المفصلية (F)

| # | القرار | الخياران | المرجح |
|---|---|---|---|
| **F-POS-1** | **نموذج KOT: مستند منفصل أم حالة POS Invoice؟** | (أ) DocType KOT منفصل يُجمَّع في POS Invoice عند الطباعة (ب) POS Invoice Draft = KOT (بنود تتغير حتى الطباعة) | **(أ)** — يطابق الفصل الثلاثي الأصلي + تعديلات بأسباب على KOT دون مساس بالفاتورة + مطابقة دورة الحياة |
| **F-POS-2** | **Guest Model الموحد** (UNK-001) | (أ) Customer واحد للجميع (FO+POS) مع حقول موسعة (ب) كيانان: Guest (إقامة) وCustomer (ذمة) | **(أ) مع توصيف دقيق** — الأصل فيه قاعدتان منفصلتان تشاركان Preferences؛ في الهدف: Customer واحد + Contact يغلف الاثنين (قرار Phase 13) |
| **F-POS-3** | **الأرضية/الطاولة** | (أ) Custom Table/Floor + ربط بالفاتورة (ب) Web View فقط بلا نموذج | **(أ)** — Table Booking Status والـ Layout يستحقان البيانات |
| **F-POS-4** | **تعدد المنصات (Regular/Touch/PDA)** | (أ) تطبيق Next.js واحد متجاوب (Touch-first) (ب) مسارات منفصلة | **(أ)** — صلاحيات على العمليات لا المنصة |
| **F-POS-5** | **دورة الترقيم Y/M/D/N** | (أ) Series حسب Naming Rule لكل POS Profile (ب) ترقيم مركزي | **(أ)** — autonomy للمنافذ |

## 3. ملاحظات تنفيذية جوهرية

1. **POS Invoice vs Sales Invoice:** منافذ البيع اليومية = **POS Invoice** (المدفوعة فوراً + التسويات المتعددة payments[])؛ الفواتير الائتمانية (Guest/AR/BoH) = **Sales Invoice** مرتبطة بالفوليو/AR — **التسوية الائتمانية تحول المسار** (قرار فني دقيق يُحرر في Phase 11).
2. **Balance=0:** POS Invoice المدفوعة تفرض تقارب المدفوعات مع الإجمالي — مطابقة أصلية.
3. **Tips:** لا DocType native — custom "Tips" (توزيع لاحق HR) — GAP-POS-E03.
4. **Round Off:** ERPNext يجبر بـ "rounding" لكل فاتورة — مطابقة None/Nearer/Higher/Lower بالتكوين + Round Off Amount لكل عملة.
5. **Swipe CC:** يُستبدل ببوابة دفع/قارئ USB في المتصفح (تطوير جانبي).
6. **Print:** طابعات KOT للشبكة = طباعة خام (Raw) عبر خادم طباعة — ERPNext Print Format يدعم طباعة الطابعات الحرارية (Slip).
