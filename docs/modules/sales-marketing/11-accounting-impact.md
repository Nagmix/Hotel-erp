# 11 — الأثر المحاسبي (Accounting Impact) — وحدة SLM

> **قاعدة الوحدة الجوهرية: لا قيد GL واحد يولد من داخل SLM.** كل الأثر المحاسبي **مفوَّض عبر الحدود**: شروط ائتمان تُنفذها FO/POS/BNQ/AR، خصومات تُطبقها POS/FO، ورسوم سياسات تحصّلها FO. هذه الوثيقة تجرد "الأثر دون القيد" — وهي الأدق لإعادة البناء.

---

## 1. مصفوفة الأثر عبر الحدود

| المحرك في SLM | القناة المنفذة | نوع الأثر | التوثيق |
|---|---|---|---|
| **Credit Limit** (Company Profile) | FO / POS / BNQ / Manual posting | **منع تسوية/ترحيل عند التجاوز** (قفل تشغيلي لا قيد) | PRF §7 |
| **Interest %** (Company Profile) | AR (المفترض) | فائدة على تجاوز Credit Days — **آلية الاحتساب/الترحيل غير موثقة** (GAP-SM-P1) | PRF §7 |
| **Commission %** (Company Profile) | AR/مالية الوكلاء | عمولة وكلاء سفر/بطاقات — الاحتساب خارج التوثيق | PRF §7 |
| **Bypass Invoice** (Company Profile) | AR | توليد/عدم توليد فاتورة للحساب | PRF §7 |
| **Revenue Discount Master** | POS (F&B bills) + FO (transactions) | **تخفيض إيراد عند الفوترة** — menu-type wise | PRF §5 |
| **Retention Policy** | FO "Retention-Cancel/No show option" | إيراد احتفاظ من No-Show بنسبة السعر المتفق | PRF §10 |
| **Cancellation Policy** | FO (رسوم الإلغاء) | إيراد إلغاء بنسبة + مدى أيام قبل الوصول | PRF §11 |
| **CGR Rates** (Link Rates) | FO (فوترة الغرف) | سعر غرفة متفاوض بدل الراك | PRF §9 |
| **Entertainment/Gift Amount** | **؟ غير موثق** | "Expenses incurred... **need to be accounted** by the Sales Executives" — بلا مسار GL (GAP-SM-P2 → UNK-050) | SLT §7 |
| **Transfer Prospects** | AR | فتح حساب عميل (أثر مستقبلي على أرصدة) | SLT §10 |

## 2. عناصر التسوية الائتمانية (شروط داخل كيان العميل)

| العنصر | قيمته | أثره عند التسوية |
|---|---|---|
| Allow Credit | Yes/No | تقييد التسوية الائتمانية أصلاً |
| Credit Days | عدد أيام | عمر الدين المسموح قبل الفائدة |
| Credit Limit | مبلغ | القفل الثلاثي + اليدوي (V-SM-17) |
| Invoice Currency | عملة | عملة طباعة فاتورة AR |
| Collection Executive | شخص | مسؤولية التحصيل (توزيع عمل لا قيد) |

> **موضع غريب معمارياً:** هذه الحقول = إعدادات AR كاملة تسكن ماستر وحدة تسويقية — تاريخياً لأن Company Profile وُلد هنا ثم استهلكته الوحدات (راجع 12 §1.3). في إعادة البناء: الكيان Customer واحد والتحرير المالي مقيد بصلاحية (P-SM-4).

## 3. الموازنات والانحراف (قياس لا قيد)

- **Company Budgets**: Room Nights متوقعة + إيراد متوقع — **أرقام تخطيطية** لا تلمس دفاتر.
- **Sales Performance (Budget)**: Budget Variance = (فعلي − متوقع) للأسابيع/الشهور — تحليل فقط.
- **Company Prod. Variance**: سنة حالية vs سابقة (Room Nights/ARR/Revenue) — مقارنة تحليلية.
- **Company Contribution/Sales/Productivity**: إيراد فعلي **مجمَّع من FO/POS/AR** — عرض لا توليد.

## 4. أين "إيراد" SLM إذن؟ (الجواب: لا مكان)

| العنصر الذي قد يبدو إيراداً | حقيقته الموثقة |
|---|---|
| Entertainment/Gift Amount | مصروف تسويقي موثق كمبلغ يُصرّح به (Authorizer) — **لا مسار قيد** |
| F&B Promotion total amount | "total amount that **may be spent** on the event" — تقدير إنفاق ترويجي |
| Cover Charges/Subscription (تناظر MEM) | ✗ لا وجود — SLM ليست وحدة فوترة |
| رسوم الدخول (تناظر MEM Guest Visit) | ✗ لا وجود |

> **الخلاصة المحاسبية:** SLM وحدة **صفر-قيود** — جميع أرقامها إما (أ) شروط تحكم سلوك الفوترة في وحدات أخرى، أو (ب) بيانات تحليلية/تخطيطية، أو (ج) مبالغ موثقة بلا قيد (Entertainment). أي تنفيذ يولّد GL من SLM يخالف النموذج الأصلي.

## 5. قرارات إعادة البناء المحاسبية

| # | القرار | المبرر |
|---|---|---|
| AC-R-1 | Customer credit terms = حقول Customer/Company القياسية في ERPNext (credit limit/days مباشرة!) | ERPNext ينفذ القفل الائتماني Sales Invoice أصلاً — يمتد بالتخصيص لفوليو FO/POS/BNQ |
| AC-R-2 | Interest % = Interest on overdue (Frappe HR لا؛ ERPNext: Custom App أو Scheduled Job) | مسار غير موثق أصلاً → حرية تصميم |
| AC-R-3 | Entertainment/Gift = Entry بمصروف اختياري (Expense Claim-like) أو تسجيل صرف | سد GAP-SM-P2 بقرار صريح |
| AC-R-4 | Revenue Discount = Pricing Rule (discount %) على صنف الإيراد + menu-type كشروط | تطابق بنيوي حرفي مع ERPNext |
| AC-R-5 | Retention/Cancellation = Sales Taxes and Charges قالب FO عند No-Show/إلغاء | تحاكي "تحصّل عبر FO" |
