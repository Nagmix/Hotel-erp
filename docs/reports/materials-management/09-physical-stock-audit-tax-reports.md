# 09 — الجرد المادي والدفاتر والتدقيق والضرائب — MGT-REP (Phase 7)

> §18.1–18.4 Physical Stock & Stores Ledger + §23 Audit Trial + §24.1–24.2 Tax (+ إحالة 4.3 Capital Goods) = 7 تقارير — حلقة إقفال المخزون والامتثال.

---

## 1. §18.1 Physical Stock Variance — التقرير المقيّد بالبيانات

**الوصف الحرفي:** "view the stock variances in comparison with the **Physical Stock balances and the Stock existing in the System**, along with the Rate, Variance Quantity & Value. The report can be generated **only for dates on which the Physical Stocks were entered**."

**النقاط البنيوية:**
- **بوابة بيانات زمنية (أول من نوعه)**: النطاق الزمني للتقرير = **مجموعة تواريخ إدخال الجرد المادي فقط** — لا يمكن طلب Variance لتاريخ لم يُجرَ فيه جرد — التقرير يرث مجاله من وجود بيانات مصدره (Data-Gated Domain) — نمط جديد تماماً مقابل بوابات future-only/past-only في FO.
- **المعادلة**: Variance = Physical − System (كمية) × Rate → قيمة — مع Rate صريح.
- الجسر الإجرائي الموثق سابقاً (DNT §14): "**alerting if the Physical Stock Variance report has been checked**" — شرط قبل تحديث الفروقات: **يجب مراجعة هذا التقرير أولاً** — التقرير **عقدة دورة موافقة** لا مجرد مخرج (نفس منطق "This mandatory report" في FO — لكن هنا الإلزامية إجرائية داخلية).
- يقابل FNB "Physical Stock Variance" (REP هناك) — نفس الاسم عبر وحدتين (عائلة أسماء مطابقة ثالثة بعد CC Consumption/Conversion).

## 2. §18.2 Physical Stock Valuation

- "details based on the data entered in the **Physical Stock entry** for a Store **as on a specified Date**" — تقييم الجرد المُدخل (لا الفروق) — الجانب "ما وجدناه" مقابل "كم اختلف" في 18.1.

## 3. §18.3 Negative Variance Report — مرونة التوقيت

**الوصف الحرفي:** "details of Items with **Negative Variances** as on a specified date. The report is processed **after the posting of Physical Stock** for Items. The report can be processed **before or after Stock Variance Update**."

- **سالب التباين** = النظام يقول أكثر مما وُجد فعلاً — **المؤشر الخطِر**: فقد/سرقة/تسريب تسجيل — لذا له تقرير مستقل بالإشارة السالبة وحدها.
- **مرونة التوقيت الموثقة حرفياً**: "before **or after** Stock Variance Update" — التقرير يعمل قبل ترحيل الفروق (وضع اكتشاف) وبعده (وضع ما بعد التصحيح) — نافذة مرونة زمنية فريدة (تقارير FO كلها بعد-الترحيل).
- تسلسل الدورة: Physical Entry → Posting → **[18.1/18.3 هنا]** → Variance Update → (مغلق).

## 4. §18.4 Print Stores Ledger — دفتر المخزن المعالَج

**الوصف الحرفي:** "view the **Stores Ledger after the Process Stores Ledger operation is completed** for a Store. The Stores Ledger displays **Item Code wise Opening / Closing Stock Balances** along with transaction details such as Receipts, Issues etc., **in a Ledger format** and can be printed for a **month or range of months**."

**النقاط البنيوية:**
- **معالجة مسبقة إلزامية**: يُطبع **فقط بعد Process Stores Ledger** (DNT §15: الغرض المعلن من العملية هو "enable the printing of Stores Ledger") — **عملية+تقرير = كيان وظيفي واحد موزع على وحدتي الدليل**.
- **شكل الدفتر**: Item-wise Opening/Closing + الحركات بينهما — **مثل General Ledger لكن للمواد** (FAS GL ledger-حسب-حساب ↔ MGT Stores Ledger-حسب-صنف — توازٍ بنيوي معلن).
- **شهر أو مدى شهور** — النطاق الشهري للطباعة (لا نطاق تواريخ حر!) — دفتر بفترات محاسبية.

## 5. §23 Audit Trial Report — التدقيق الذي يعرض المحذوفات

**الوصف الحرفي:** "view the audit trial made for **transactions, PO, SPO, Indent, and Purchase Requisition** for a specified period. The user can **include all modified and deleted details** in the report."

**النقاط البنيوية:**
- **نطاق التدقيق = مستندات المشتريات الخمسة**: المعاملات + PO + **SPO** + Indent + PR — كل دورة الشراء تحت المرآة.
- **"modified AND deleted"** — التقرير الوحيد في الحزمة الموثق بعرض **السجلات المحذوفة** — مدى تدقيقي أوسع من:
  - FO Audit ×8: old/new + المستخدم المخوّل (لكن للموجود)
  - POS Bill/KOT Audit: أسباب + old/new
  - **هنا: المحذوف نفسه يظهر** — أثراً عكسياً (الفارق الوحيد القابل للمقارنة: Watch List بذاكرة unmarking).
- "Audit **Trial**" (لا Trail!) — خطأ إملائي صارخ متكرر عبر الحزمة (FAS-REP §33 يحمل نفس "Audit Trial Report"!) — **خطأ نسخ عابر للوحدات** يوثق دون مستوى تناقض (يكرر نفسه في تسمية الطابعة: "Sun" في 16.3 — عائلة أخطاء مطبعية منهجية).

## 6. §24.1 VAT Report — تقرير الامتثال الضريبي الاستلامي

**الوصف:** "view a list of all taxes that are **incorporated during receipt of Items**. Taxes on items received are posted in the **Receipt entry** under Transactions option. The information can be processed for a range of Vendors and for a specific date range. The report can be generated based on **Tax, Group and Stores**."

**المعايير (ص107-109 — أغنى شاشة مركّبة في الوحدة):**

| الشاشة | # | المعيار |
|---|---|---|
| الأولى | 1 | Date Range |
| | 2 | All / **Range** (نمطا الانتقاء) |
| | 3 | Range + **F1** لGrr. Range |
| | 4 | **VAT Rates** متعددة |
| | 5 | Groups (التي عليها الضريبة) |
| | 6 | Stores |
| الثانية | 8 | **"Company details for assessment of a year"** |
| | 9 | Include Open Items / **Print Sequence PJV Wise** |
| | 10 | **Summary / Details / Both** |

**النقاط البنيوية:**
- **شاشة إعداد امتثال ثانية كاملة**: بيانات الشركة + سنة التقييم (assessment year — مصطلح ضريبي هندي رسمي!) — التقرير يُصمَّم **للتقديم لسلطة الضرائب** (يقابل نموذج TDS Forms في FAS-REP §26-31).
- **Print Sequence PJV Wise** — ترتيب الطباعة حسب **PJV** (Purchase Journal Voucher — مفهوم FAS؛ مؤكد بقوة في FAS-REP §18 "Pending Receipts for PJV") — خيار ترتيب **حسب المستند المحاسبي الأم** — جسر ترتيبي MGT→FAS.
- **Summary/Details/Both** — ثلاثية عمق الإخراج (نفس عائلة FO/POS Detail/Summary + ثالثة Both).
- ضريبة الاستلام (Input VAT — ضريبة مدخلات) — الوجه المشتري من ضريبة POS (Output VAT على المبيعات) — الثنائية الضريبية الكاملة عبر الوحدتين.

## 7. §24.2 Tax Report — التوأم النصي (C-MR-03)

**الوصف الحرفي لـ24.2 (قارن سطراً بسطر مع 24.1):**

> "In this report, you can view a list of all taxes that are incorporated during receipt of Items. Taxes on items received are posted in the Receipt entry under Transactions option. The information can be processed for a range of Vendors and for a specific date range. The report can be generated based on Tax, Group and Stores."

**مطابقة 100% حرفياً** مع وصف 24.1 — ثم الشاشة: "Enter the appropriate options from the relevant fields **based on you selection criteria**" (أفق عام + "you" بلا r — أخطاء مطبعية).

- **لا يميزهما شيء في النص** — فهل: نسخة كتالوغية مكررة (كDiscount Register في POS)؟ أم تقرير "Tax" عام غير-VAT (ضرائب أخرى) فشل وصفه؟ → **UNK-090** (الأرجح الأول بقرينة نمط POS C-POS-01 لكن الفيصل يحتاج الشاشات).
- يقابله في FAS-REP: **Purchase Tax Register (§11)** — الوجه المالي لنفس المجال — ثلاثي "VAT/Tax/Purchase Tax Register" عبر الوحدتين.

## 8. 4.3 Capital Goods Receipt (إحالة من 05)

سجل استلام **البضاعة الرأسمالية بتفاصيل VAT** — نقطة الالتقاء: MGT (استلام) × FXD (أصل) × FAS (VAT مدخلات أصول رأسمالية) — توثّق تفاصيلها في `05-transaction-receipt-reports.md` §3.

## 9. خريطة الامتثال والتدقيق عبر المرحلة 7 (تحديث)

| الوحدة | أداة الامتثال | النطاق |
|---|---|---|
| FO | Police/C-Form + RBI-RLM + IT + Watch List | ضيف/نقد أجنبي |
| POS | Tax Register + **PAN (Switch 137)** | مبيعات/تسويات |
| **MGT** | **VAT (assessment year + PJV) + Capital Goods VAT + Audit Trial بالمحذوفات** | **استلام/ضريبة مدخلات/تدقيق مستندي** |
| FAS (القادمة) | TDS Forms 16A/26J/27/26A/26C/26K + Purchase Tax Register | مصدر/مصروف |

**التجميع:** MGT تغطي **امتياز الامتثال من جهة الشراء** — وتكشف أن أضلاع مثلث الامتثال الهندي (شراء/بيع/مصدر) موزعة على MGT/POS/FAS — الحزمةكلها مصممة لسوق هندي (كل المؤشرات: PAN · TDS · assessment year · Lakhs · C-Form).
