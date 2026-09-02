# 04 — سير العمل (Workflows) — وحدة ACR

> 15 سير عمل موثقاً (WF-AR-01..15) مرتبة على دورة حياة الذمم: تأسيس → قيود → مطابقة → فوترة → تحصيل → إقفال. كل خطوة بمصدرها.

---

## WF-AR-01 · تفعيل الوحدة (مرة واحدة)

1. **AR Start Date**: إدخال MMYY — يُقبل **مرة واحدة** ولا يُعدَّل (ACR-SET §1 ص1-2).
2. تسجيل Company Profiles (شرط مسبق) — عبر Company Profile option (ACR-SET §2 ص2).
3. تأكيد **Module Attribute #3 = YES** قبل أي إدخال (ACR-SET §2 ص3).
4. تعريف Aging (فترات To + فائدة اختيارية) بتاريخ ≥ اليوم (ACR-SET §3 ص8-9).
5. **AR Opening Balance**: إدخال أرصدة الدين (Debit بفاتورة/مجمع) والائتمان (نقد/شيك/بطاقة) والتعديلات (ACR-SET §2 ص2-7).
6. أول SOA يُشتق آلياً من AR Start Date (ACR-OPR §7 ص21).

**قاعدة:** القيد الزمني — "Opening Balance amounts can be entered **after** commencement of transaction posting for the required month & year" لكن **يُقفل بمجرد** معالجة SOA لشهر البداية (ACR-SET §2 ص3).

## WF-AR-02 · قيد مدينة يدوي (Debit Entry)

1. Transaction Entry → زر **Debit** → Add (ACR-OPR §1 ص2-4).
2. إدخال: Company (F1) · Outlet · Property · Bill #/Date (**≤ تاريخ اليوم**) · Currency (سعر صرف Exchange Entry — غير قابل للتحرير) · Amount → Value آلي.
3. Commission %/Amount إذا الشركة وكيل سفر/بطاقة (Net = المتبقي).
4. تفاصيل البطاقة إذا كانت تسوية بطاقة (Card Type/CC #/Auth #) — **إلزامية** (ACR-OPR §1 ص3).
5. Description (≤100 حرف alphanumeric) (ACR-OPR §1 ص3).
6. Save → **FA Transaction screen** (إذا INI #56=0) → ترحيل لحسابات مناسبة (ACR-OPR §1 ص10).

**الحالة النموذجية:** القيود المدينة "All sales credited to companies are **automatically posted** as debit entries" من FO/POS/BQT/MEM — اليدوي للفواتير خارج هذه المنافذ (Online bills: Credit Card, Bills on Hold, Company Settlements) (ACR-OPR §1 ص4).

## WF-AR-03 · قسيمة قبض مطابَقة مباشرة (Method 1)

**الشرط: Module Attribute #6 = No** (ACR-OPR §1 ص4).

1. Transaction Entry → زر **Credit**.
2. Company/Outlet/Property/Currency/XRate/Amount Paid/Value.
3. **تحديد Bill #** من الفواتير المعلقة للشركة (F1 يعرض فواتير الشركة) + Receipt #/Date (رقم آلي إذا Attr#1=Yes، وإلا يدوي فريد).
4. Save (+ شاشة FA Transaction للترحيل).

## WF-AR-04 · قسيمة قبض غير مخصصة (Method 2) ثم المطابقة

**الشرط: Module Attribute #6 = Yes** (ACR-OPR §1 ص4).

**أ. التسجيل:**
1. زر Credit → إدخال التفاصيل **بدون Bill #** → رقم إيصال وتاريخ ومبلغ فقط.
2. النظام يصنّفه **unallocated** (ACR-OPR §1 ص4).

**ب. المطابقة (Match Bills–Receipts):** (ACR-OPR §2 ص10-11)
1. اختيار الشركة (F1) + العملة → Selection Criteria (Property + Invoice #) → تحميل الإيصالات والفواتير.
2. اختيار **إيصال واحد** (double-click → Option=Yes) — "You can select only one receipt at a time".
3. اختيار **فواتير متعددة** (Option=Yes لكل فاتورة).
4. جدول: Bill Amount · Adjusted Amount (قابل للتعديل) · Equivalent Local.
5. تعديل Adjusted Amount حسب التوزيع المطلوب → Save.
6. الفائض يبقى **unallocated** للجلسة القادمة (ACR-OPR §2 ص11).

## WF-AR-05 · تسوية فواتير متعددة بمبلغ واحد (Multiple Bill Settlement)

(ACR-OPR §1 ص4-7)

1. شاشة Credit → تحديد الشركة → زر **POST**.
2. Property + Invoice # → عرض الفواتير (Bill date/# · Outlet · Currency · XRate · Exchange paid · Bill/ Settled/Receipt/Adjust/Balance Amount).
3. زر Adjust → اختيار الفواتير المستهدفة.
4. تعديل Adjusted Amount لكل فاتورة (Calculated Amount = المكافئ المحلي).
5. **سعر الصرف المعتمد = سعر تاريخ الفاتورة** ("bill exchange rate at the receipt level") لتفادي ربح/خسارة الصرف (ACR-OPR §1 ص6).
6. Commission Amount (للوكلاء) → Save → عمود Y للمطابَقة.
7. بنك/شيك إن لزم → زر Bank.
8. **إذا المبلغ > إجمالي المعلق:** خيار Yes/No لتوليد **إيصال بالفارق** (ACR-OPR §1 ص7).

## WF-AR-06 · قيد تسوية/صحوة (Adjustment)

(ACR-OPR §1 ص7-8)

1. زر **Adjustment** → Company (F1).
2. F1 في حقل Bill Number → **فاتورة موجودة حصراً** ("Adjustments can be done only on existing bills").
3. Adjustment # + Date + Currency (سعر صرف **تاريخ التعديل**) + Amount:
   - فاتورة أقل من الحقيقة (800 صحيح، رُحّل 750) → **+50** = قيد مدينJV Debit، يُضم للفاتورة كسجل واحد.
   - فاتورة أكثر من الحقيقة (800 صحيح، رُحّل 850) → **−50** = قيد دائن JV Credit.
4. **ممنوع إسناد Commission للتعديلات** (ACR-OPR §1 ص8).
5. القيود اليدوية (ومنها التعديلات) **قابلة للتعديل والحذف** (ACR-OPR §1 ص8).

## WF-AR-07 · طباعة الفواتير والتذكيرات

(ACR-BIL §1-§2)

**أ. Monthly Invoice Statement (شهري/كشوف مجمعة):** نطاق شركات + As on MMYY + Spl. Instructions → طباعة — **يستلزم Pgm ID معرفاً في SYS مسبقاً** وإلا لا تُطبع (ACR-BIL §1 ص2).

**ب. Print Invoice:**
1. Attr#2=Yes → شركة واحدة + نطاق فواتيرها / Attr#2=No → نطاق شركات + كل الفواتير (ACR-BIL §2 ص4).
2. As On (حد الفواتير المعلقة) + Remarks + Currency + عنوان (Company/Billing/جديد).
3. مواصفات: User Defined Bill Spec + No. of Copies + **Aging ☑** (أيام التقادم) + **Email ☑** (ACR-BIL §2 ص5).
4. Print → الفاتورة تُرقَّم. **بعد الطباعة لا يُعاد الطبع لنفس الفاتورة** — Reprint بنطاق أرقام فقط (ACR-BIL §2 ص6).

**ج. Cancel Invoice:** نطاق From/To Invoice # → إلغاء — البوابة الوحيدة لتعديل قيود مفوترة (ACR-BIL §2 ص5).

**د. Reminder:** يرسل تذكيراً بالذمم — **يستلزم صيغة معرفة في User Defined Print Forms مسبقاً** (ACR-BIL §2 ص5).

## WF-AR-08 · الإقفال الشهري (SOA) — الدورة المتسلسلة

(ACR-OPR §7 ص20-21)

1. اكتمال قيود الشهر (يدوي + تلقائي).
2. Statement of Accounts → **الشهر الأول يؤخذ من AR Start Date**، وما بعده يُعرض تلقائياً (الحقل غير قابل للتحرير — تسلسل إجباري).
3. المعالجة = **إغلاق نهائي**: "transactions for the month are closed and cannot be modified or deleted".
4. الطباعة/العرض عبر **SOA Print** في RPL (شهر + نطاق شركات + خيارات عنوان وفصل صفحات) (ACR-RPL §9 ص15-17).

## WF-AR-09 · فتح الشهر للتصحيح (Rollback SOA)

(ACR-OPR §8 ص21)

1. Rollback Statement of A/C → Cutoff MMYY (مثال: SOA مُعالجة لمارس وأبريل 2007 → إدخال 0307 يلغي مارس→أبريل).
2. **قيدات مقاومة للتعديل حتى بعد الفتح:**
   - قيود **مفوترة** → يجب **Cancel Invoice** أولاً (عبر Billings) (ACR-OPR §8 ص21).
   - قيود دائنة **مطابَقة** → **حذف** Credit transactions عبر Transaction Entry → تعديل → إعادة تسجيل → إعادة Match Bills–Receipts.
3. بعد التعديلات → **إعادة معالجة SOA** لإغلاق الشهور مجدداً.

**سلسلة القفل الثلاثية:** SOA (شهر) → Invoice (مستند) → Matching (إيصال) — كل طبقة تفتح التي تحتها فقط.

## WF-AR-10 · تصحيح محدود بعد الإقفال (Outstanding Update)

(ACR-OPR §5 ص14-16)

1. Operations → Outstanding Update → Company (F1) → قائمة القيود.
2. تعديل **حصرياً**: Bill Number/Date · Description · Bank Details/Credit Card Details.
3. Save — "modify the required details" للأخطاء الكتابية **دون فتح SOA**؟ `[UNCERTAIN]` النص يصفها لتصحيح "clerical mistake" مثل تاريخ/رقم فاتورة خاطئ بعد معالجة SOA — يبدو أنها آلية تصحيح موازية للـ Rollback للحقول البياناتية فقط (لا مبالغ). راجع `13-exceptions.md` E-AR-06.

## WF-AR-11 · عمولات وكلاء السفر (Travel Agent Commissions)

(ACR-OPR §3 ص12-13)

1. Company (F1) + مدى تاريخي (**≤ اليوم**) + Currency.
2. فلترة بـ Commission % محدد (زر) أو **عرض الكل**.
3. Load → جدول الفواتير (مع/بدون العمولة).
4. إدخال **% لكل فاتورة على حدة** ("different commission % for different bills") → Save → يحدَّث في القيد المعني.

## WF-AR-12 · تجميع بطاقات الائتمان وسجلها

(ACR-OPR §4 + ACR-RPL §8)

**أ. التجميع (Consolidation):** CC Consolidation → شركة بطاقة (F1) + تاريخ → عرض فواتير اليوم (Doc#/Bill/Outlet/Card/Amount) → إدخال **رقم مجموعة** في عمود Option → الفواتير المرقمة 1 تُرسل كفاتورة واحدة لشركة البطاقة (ACR-OPR §4 ص13-14). **التجميع عرضي فقط** — "In all other transactions these bills are considered as multiple entries".

**ب. السجل (Credit Card Register):** شركة + مدى **ضمن الشهر نفسه** + Commission % + Summary ☐ + **Update Commission in Transactions ☐** (إن لم يُفعل: يطبع بالنسبة دون تحديث القيود) → خطاب تغطية + Charge Slips (خصم العمولة) (ACR-RPL §8 ص13-15).

## WF-AR-13 · مطاردة الذمم (Debtors Follow-Up)

(ACR-CRT كاملاً)

1. Credit Trace → Debtors Follow-Up → Company (أو عرض الكل) + **Advanced Search** (أولويات).
2. تبويب Transactions: قيود الشركة → **double-click** للتنقيب: قيد → مدين/دائن → الضيف → **تقسيم المبالغ** (ص2-4).
3. **Follow-Up Entry:** تحديد فواتير (☑ Tagged Bills) → Activity Date + المبلغ (آلي) → **تعيين لمستخدم** → Remarks → **موعد المتابعة التالي (تاريخ+وقت)** → **Projection Amount** (افتراضي الإجمالي، قابل للتعديل) → **Projection Period** → Payment Status → Save (ص3).
4. **Follow-Up Trace:** تتبع بالشركة/المكلَّف/Projection Mode + عرض المغلق → التاريخ بالنقر المزدوج (ص6-7).
5. **Projection Report:** مدى + Status → الفترات والمبالغ المتوقعة والفواتير والأرصدة → طباعة (ص7-8).
6. Aging + الإيصالات غير المخصصة تُعرض في قسم Aging (ص3).

## WF-AR-14 · فك مطابقة إيصال (Receipts Untagging)

(ACR-OPR §6 ص16-19)

1. Receipts Untagging → Company Code (F1) → Currency.
2. Receipt # مباشرة أو عبر **Receipt Help** (بحث بـ Receipt Date مدى أو Bill #) → اختيار من النتائج.
3. Load → تفاصيل الإيصال.
4. Double-click في عمود **UnTag** → YES.
5. Save — الإيصال يعود **غير مطابق**.

## WF-AR-15 · تنقية سجل التدقيق (Purge ACR Audit)

(ACR-SET §7 ص17-18)

1. توليد **كل التقارير ذات الصلة مسبقاً**.
2. تجميد الإدخال اليومي (نافذة صيانة).
3. Purge ACR Audit Table → Cutoff Days (**≥60**) → Save.
4. القيود المحذوفة/المعدلة الأقدم من الحد تُمحى من ACR Audit Table.
