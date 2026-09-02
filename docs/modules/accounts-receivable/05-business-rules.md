# 05 — قواعد العمل (Business Rules) — وحدة ACR

> 14 مجموعة قواعد (BR-AR-01..14) — كل قاعدة بمصدرها النصي. هذه القواعد **تشريع ملزم** للنظام المستهدف.

---

## BR-AR-01 · قواعد تفعيل الوحدة والتأسيس

| # | القاعدة | المصدر |
|---|---|---|
| 1 | AR Start Date (MMYY) يُدخل **مرة واحدة** ولا يُعدَّل أبداً | ACR-SET §1 ص1 |
| 2 | Module Attribute #3 (Audit trail) يجب أن يكون **YES قبل** أي إدخال قيود أو أرصدة افتتاحية | ACR-SET §2 ص3 |
| 3 | أرصدة الافتتاح تتطلب Company Profile مسجلاً مسبقاً | ACR-SET §2 ص2 |
| 4 | **يُوصى نصاً** بتسجيل الافتتاحيات بالفاتورة (Bill#/Date) لا مجمعة — لتسهيل مطابقة السداد لاحقاً | ACR-SET §2 ص2 |
| 5 | أرصدة الافتتاح **تُقفل** بمعالجة SOA لشهر البداية — والتعديل يتطلب Rollback SOA ثم إعادة المعالجة | ACR-SET §2 ص3 |

## BR-AR-02 · قواعد كود الشركة (Company Code)

| # | القاعدة | المصدر |
|---|---|---|
| 1 | الطول **≤ 7 خانات alphanumeric** | ACR-SET §5 ص11 |
| 2 | **أول 3 خانات = Company Type** (معرَّف في FO Setup — مولّد البادئة) | ACR-SET §5 ص11 |
| 3 | الخانات الأربع التالية: تركيبة alphanumeric حرة | ACR-SET §5 ص11 |

## BR-AR-03 · قواعد الائتمان (Credit Rules)

| # | القاعدة | المصدر |
|---|---|---|
| 1 | Allow Credit = Yes ⇒ إدخال **Credit Days** إلزامي | ACR-SET §5 ص13 |
| 2 | **تجاوز Credit Limit يمنع تسوية** فاتورة FD/POS/Banquet أو الترحيل اليدوي — "settlement... or manual posting of the bill is not allowed" | ACR-SET §5 ص14 |
| 3 | Interest % يطبَّق على الفواتير المتجاوزة لمدة الائتمان | ACR-SET §5 ص13 |
| 4 | Bypass Invoice = Yes ⇒ لا تولد فاتورة للحساب | ACR-SET §5 ص13 |
| 5 | Commission %: للوكلاء وشركات البطاقات | ACR-SET §5 ص14 |

## BR-AR-04 · قواعد الوصم (Watch List / Black List)

| # | القاعدة | المصدر |
|---|---|---|
| 1 | Black List = Yes ⇒ **السبب + اسم المجيز إلزاميان** | ACR-SET §5 ص12 |
| 2 | تفاصيل القائمة السوداء تُعرض في **وضع Modify فقط** | ACR-SET §5 ص16 |
| 3 | Watch List + To Date ⇒ يُغذي تقرير Watch List Companies (S&M) | ACR-SET §5 ص11-12 |

## BR-AR-05 · قواعد القيود (Transaction Entry)

| # | القاعدة | المصدر |
|---|---|---|
| 1 | Bill Date **≤ تاريخ النظام الحالي** | ACR-OPR §1 ص3 |
| 2 | سعر الصرف من Exchange Entry — **حقل غير قابل للتحرير** | ACR-OPR §1 ص3 |
| 3 | القيمة (Value) تُحسب آلياً = Amount × Exchange Rate للعملات الأجنبية | ACR-OPR §1 ص3 |
| 4 | Description ≤ **100 حرف alphanumeric** | ACR-OPR §1 ص3 |
| 5 | تفاصيل البطاقة **إلزامية** إن كانت التسوية بطاقة | ACR-OPR §1 ص3 |
| 6 | Net Amount = القيمة − العمولة (إن وجدت) — وعليه يُحسب المدين | ACR-OPR §1 ص3 |
| 7 | Doc # **يولَّد آلياً** بعد الحفظ (مرجع التعديل/التصفح/الحذف) | ACR-OPR §1 ص2 |

## BR-AR-06 · قواعد نمط استلام الإيصالات (Receipt Pattern)

| # | القاعدة | المصدر |
|---|---|---|
| 1 | نمط الاستلام محكوم بـ **Module Attribute #6**: No = ترحيل مباشر على فاتورة؛ Yes = تسجيل unallocated ثم مطابقة لاحقة | ACR-OPR §1 ص4 |
| 2 | Attr#1=Yes ⇒ Receipt # **آلي**؛ No ⇒ إدخال يدوي **فريد** | ACR-OPR §1 ص5 |
| 3 | سداد أكبر من المعلق ⇒ خيار توليد **إيصال للفارق** (Yes/No) | ACR-OPR §1 ص7 |
| 4 | الفارق غير المخصص يبقى **unallocated** ويُعرض في الجلسة التالية | ACR-OPR §2 ص11 |
| 5 | المطابقة: **إيصال واحد** في كل عملية × **فواتير متعددة** | ACR-OPR §2 ص10-11 |

## BR-AR-07 · قاعدة سعر الصرف عند السداد (Bill Exchange Rate)

> "the exchange rate, which existed on the date of billing, will be considered at the time of settlement also. The current exchange rate... will not be considered" — لتفادي ربح/خسارة الصرف الدفترية (Book Profit/Loss). (ACR-OPR §1 ص6)

**الاستثناء:** سعر صرف **التعديل (Adjustment)** يُعتمد فيه **سعر تاريخ التعديل** (ACR-OPR §1 ص8) — لا سعر الفاتورة.

## BR-AR-08 · قواعد التعديلات (Adjustments)

| # | القاعدة | المصدر |
|---|---|---|
| 1 | على **فاتورة موجودة فقط** (F1 إلزامي) | ACR-OPR §1 ص7-8 |
| 2 | موجب = قيد مدين JV Debit (يُضاف)؛ سالب = دائن JV Credit (يُخصم) — يظهر **كسجل واحد مدمج** مع الفاتورة | ACR-OPR §1 ص8 |
| 3 | **ممنوع إسناد Commission** للتعديلات | ACR-OPR §1 ص8 |
| 4 | القيود اليدوية (التعديلات) قابلة للتحديث/الحذف | ACR-OPR §1 ص8 |

## BR-AR-09 · قواعد القفل متعدد الطبقات (Lock Cascade)

| # | القاعدة | المصدر |
|---|---|---|
| 1 | طباعة الفاتورة ⇒ **لا تعديل للقيد** — إلا Company Name/Branch إذا INI #74 = 0 (الافتراضي) | ACR-OPR §1 ص10 |
| 2 | الفاتورة المطبوعة **لا تُطبع مرة أخرى** — Reprint حصراً بنطاق أرقام | ACR-BIL §2 ص6 |
| 3 | SOA معالَجة ⇒ **الشهر مقفل** (لا إضافة/تعديل/حذف) | ACR-OPR §7 ص20-21 |
| 4 | Rollback يفتح من شهر القطع **حتى آخر شهر معالج** (مدى لا نقطة) | ACR-OPR §8 ص21 |
| 5 | بعد Rollback: القيود المفوترة تحتاج Cancel Invoice، والمطابَقة تحتاج حذف الإيصال الدائن ثم إعادة التسجيل والمطابقة | ACR-OPR §8 ص21 |
| 6 | SOA **متسلسلة شهرياً** — الشهر الأول من AR Start Date والحقل بعدها غير قابل للتحرير | ACR-OPR §7 ص21 |

## BR-AR-10 · قواعد الترحيل المحاسبي (AR→FAS)

| # | القاعدة | المصدر |
|---|---|---|
| 1 | الرابط يعمل فقط بـ **INI #56 = 0** (منطق معكوس؛ الافتراضي 1 = معطل) | ACR-OPR §1 ص10 |
| 2 | حسابات Sundry Debtors/Cash/Bank/Commission معرفة مسبقاً في Link AR to Finance (FAS-SET §11) | ACR-OPR §1 ص10 |
| 3 | الترحيل **تفاعلي عند الحفظ** (شاشة FA Transaction تنبثق) | ACR-OPR §1 ص10 |
| 4 | القيود التلقائية من FO/POS/التلقائية اليدوية — **جميعها يجب أن تُرحَّل لتنعكس في الدفاتر** | ACR-OPR §1 ص10 (Important Note) |

## BR-AR-11 · قواعد التجميع البنكي للبطاقات

| # | القاعدة | المصدر |
|---|---|---|
| 1 | التجميع برقم مجموعة في عمود Option — فواتير المجموعة تُرسل **كفاتورة واحدة** لشركة البطاقة | ACR-OPR §4 ص13-14 |
| 2 | **حصرياً لـ Credit Card Register** — "In all other transactions these bills are considered as multiple entries" | ACR-OPR §4 ص13 |
| 3 | Credit Card Register: مدى التاريخ **ضمن الشهر نفسه** | ACR-RPL §8 ص14 |
| 4 | Update Commission ☐: بدونها يُطبع بالنسبة **دون تحديث القيود** | ACR-RPL §8 ص14 |

## BR-AR-12 · قواعد التقادم (Aging)

| # | القاعدة | المصدر |
|---|---|---|
| 1 | الأساس = **Bill Date** | ACR-SET §3 ص8 |
| 2 | إدخال **To فقط** — From آلي (ابتداء 0) | ACR-SET §3 ص9 |
| 3 | تاريخ التعريف ≥ اليوم للتفعيل | ACR-SET §3 ص9 |
| 4 | معايير الفائدة الأربعة النظامية: % Closing / Amount / None / % Opening — **لكل فترة على حدة** | ACR-SET §3 ص9 |
| 5 | Print Text = اسم العمود في Aging Summary | ACR-SET §3 ص9 |
| 6 | التعريف **مشترك** مع FAS ("Accounts Receivable and Financial Management module") | ACR-SET §3 ص8 |

## BR-AR-13 · قواعد المتابعة والتحصيل (Follow-Up)

| # | القاعدة | المصدر |
|---|---|---|
| 1 | متابعة واحدة: فواتير متعددة (Tagged) لمستخدم واحد + موعد تالٍ (تاريخ/وقت) | ACR-CRT ص3 |
| 2 | Projection Amount افتراضي = الإجمالي — **قابل للتعديل** | ACR-CRT ص3 |
| 3 | Payment Status قيمة من قائمة | ACR-CRT ص3 |
| 4 | التتبع يدعم فلترة **المغلق** وProjection Mode | ACR-CRT ص7 |

## BR-AR-14 · قواعد الصيانة والتدقيق

| # | القاعدة | المصدر |
|---|---|---|
| 1 | Purge ACR Audit: Cutoff **≥ 60 يوماً** | ACR-SET §7 ص18 |
| 2 | قبل Purge: توليد كل التقارير ذات الصلة + **منع الإدخال اليومي أثناءها** | ACR-SET §7 ص18 |
| 3 | Audit يسجل **Del** (محذوف) و **Old→New** (معدَّل بنسختين) — فقط إذا Attr#3 = Yes | ACR-RPL §11 ص20 |
| 4 | Receipts Untagging يعمل بمعايير بحث (Receipt Date مدى / Bill #) | ACR-OPR §6 ص17-18 |
| 5 | Browse Transactions: مدى الشهور **ضمن السنة المالية نفسها** | ACR-RPL §20 ص31 |
| 6 | طباعة Monthly Invoice Statement تتطلب **Pgm ID** معرفاً في SYS — وإلا **لا تُطبع** | ACR-BIL §1 ص2 |
