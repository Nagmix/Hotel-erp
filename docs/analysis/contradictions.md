# سجل التناقضات (Contradiction Register)

> عند اكتشاف تعارض بين وثيقتين: سُجِّل (المصدر أ، المصدر ب، التعارض، التفسير المحتمل، القرار الموصى به).
> **الحالي: 3 تناقضات مسجلة (C-FB-01 · C-FO-01 · C-FO-02 — الثلاثة الأخيرة من الجلسة 16/Phase 7).**

---

## C-FO-01: Guest Photo Reg. Card موثق مرتين بنطاقين مختلفين (داخل FOM-REP)

| البند | التفصيل |
|---|---|
| المصدر أ | FOM-REP §23.1 تحت Security (ص22-23): "print the registration card **for inhouse guests** with the Guest's photo" |
| المصدر ب | FOM-REP نفس البند 23.1 بعد "under Registrations" (ص23-24): "print the registration card **for inhouse guests as well as expected arrival's** with photograph" |
| التعارض | النطاق الأول: المقيمون فقط · الثاني: المقيمون **+ الوصول المتوقع** — والوصف الثاني أوسع وأغنى ("as an agreement... with unique registration number") |
| التفسير المحتمل | إعادة تحرير متأخرة للبند أُدرجت دون حذف الأولى (نمط ازدواج تحريري شائع في دليل REP الطويل) |
| القرار الموصى به | **يُعتمد النطاق الأوسع** (inhouse + expected arrival — الخياران موثقان في شاشة الثانية: "Choose either Inhouse or Expected Arrival option")؛ الإصدار الأول يُحفظ كاقتباس تاريخي |
| المصدر التكميلي | docs/reports/front-office/03-security-statutory-reports.md §1 |

## C-FO-02: تسمية المنتج "Fortune Next Enterprise 2.0" مقابل "FortuneNext 6i" (FOM-SMS vs الحزمة)

| البند | التفصيل |
|---|---|
| المصدر أ | FOM-SMS §1 Mobile Master (ص2): "SMS to be sent by **Fortune Next Enterprise 2.0** for events such as..." |
| المصدر ب | كل عناوين الحزمة الـ65: "FN6i-" prefix + غلاف "FORTUNE NEXT 6i" |
| التعارض | إصداران مختلفان للمنتج نفسه في نفس الحزمة (2.0 vs 6i) |
| التفسير المحتمل | وحدة SMS كُتبت/كُتب دليلها في حقبة "Enterprise 2.0" ثم حُزمت مع 6i دون تحديث — **بقايا تحريرية تكشف أقدمية الوحدة النصية** |
| القرار الموصى به | يُعتمد 6i كهوية الحزمة المرجعية؛ يُسجل "Enterprise 2.0" كأثر جيولوجي توثيقي (يستعمل في تحليل النشأة لا في المواصفة) |
| المصدر التكميلي | docs/reports/front-office/10-sms-alerts.md §رأس |

---

## C-FB-01: أقواس Standard/Actual معكوسة عن المتن (داخل FNB)

| البند | التفصيل |
|---|---|
| المصدر أ | FNB-LUK ص12 (Standard Vs. Actual Q): "analysis in terms of **Standard Cost (Consumption) and Actual Cost (Recipe)**" |
| المصدر ب | FNB-REP ص22 (Standard vs. Actual R): "analysis is made in terms of standard cost (consumption) and actual cost (recipe)... **Standard consumption is based on recipe details. Actual is arrived based on consumption at cost centers**" |
| التعارض | الأقواس في العنوانين تسند Standard إلى Consumption وActual إلى Recipe، بينما متن REP الحاسم يعكسها: **Standard = الوصفة (النظري)** و**Actual = استهلاك مراكز التكلفة (الفعلي)** |
| التفسير المحتمل | صياغة عنوان رديئة تكررت في الملفين؛ المتن في REP هو الدلالة المقصودة — وهو الموافق لنظرية تكاليف F&B القياسية (Theoretical/Standard cost من الوصفات مقابل Actual من الاستهلاك الفعلي) |
| القرار الموصى به | **يُعتمد المتن**: Standard = recipe-based، Actual = consumption-based؛ تُوثق الأقواس الأصلية كاستثناء صياغي (GAP-FB-D03 + UNK-065) ولا يُبنى على الأقواس أي عمود تقريري |
| المصدر التكميلي | docs/modules/food-beverage-costing/13-exceptions.md (الحالة #26) + 17-gap-analysis.md (GAP-FB-D03) |



---

## الجلسة 17 — POS-REP (تناقضات 3 جديدة — الإجمالي 6)

| ID | الوصف | المصدر | القرار |
|---|---|---|---|
| **C-POS-01** | **Discount Register موثق مرتين بمعايير مختلفة**: §6.1 (ص96-98: نطاق ≤ Accounting + Settlement Mode) و§12 (ص103-105: Discount% + Session + By Bill/Date + Summary By Reason/Cashier/Mode) — نفس الاسم، جسمان مختلفان. **مضاعَف**: كتلة §6 كلها (ص96-103) واقعة فيزيائياً بعد §11 (ص88-95) خلافاً لترتيب TOC (دليل إدراج/إعادة ترتيب لاحقة) | POS-REP §6.1/§12 + ترتيب الصفحات | يُعتمد §12 (الأغنى) مع دمج مرشح Settlement Mode من §6.1 — UNK-087 يسجل الغموض |
| **C-POS-02** | ملاحظة SETUP في **Discount Summary (6.2)** تُحيل إلى **"Sales By Item"**: "select the Void and Complimentary options corresponding to **Sales By Item**" — خطأ نسخ/لصق من 1.1 (الصواب المنطقي: Discount Summary) | POS-REP §6.2 ص99 | تصحيح تحريري — الإحالة الصحيحة = Discount Summary |
| **C-POS-03** | **Menu List (18)**: الخطوة "3. Select one of the Selection options: Code List, Rate List or Other List." **مكررة حرفياً مرتين متتاليتين** (ص144) | POS-REP §18 ص144 | خطأ تحريري خام (سطر منسوخ) — يُحذف التكرار |

> ملاحظة تحت مستوى التناقض (تُوثق في `reports/point-of-sale/02` §3): DS Report — جدول الحقول يسمي العمود **BREAKFAST** بينما الخلاصة تكتب **"Morning"** (انحراف تسمية). وتُلاحَظ صياغة §11.3 "within **any** month" مقابل "within the **same** month" في 11.1/11.2 (غموض نطاق — UNK-088).

---

## الجلسة 18 — MGT-REP + FAS-REP (تناقضات 6 جديدة — الإجمالي 12)

### MGT-REP (تناقضات 3)

| ID | الوصف | المصدر | القرار |
|---|---|---|---|
| **C-MR-01** | **القسم 6 مرقّم مرتين**: TOC والجسم معاً يحملان "6. Item & Vendor List" **و** "6. Closing Stock by Type" — ازدواج رقم قسم بلا إعادة تسلسل لاحقة + بند TOC مكسور الترميز "6._Item___Vendor_List" (شرطات سفلية بدل المسافات) | MGT-REP TOC ص2 + الجسم ص45/ص55 | خطأ ترقيم هيكلي — يُعاد الترقيس (Closing Stock = 7 منطقياً) أو يوثّق الشذوذ كما هو (المعتمد توثيقياً) |
| **C-MR-02** | **§6.1 نسخة حرفية كاملة من §1**: نفس الوصف والخطوات والمعايير كلمة بكلمة (Inventory Item List مرتين تحت رقمين وقسمين مختلفين) | MGT-REP §1 ص4-7 + §6.1 ص46-48 | تكرار كتالوغي صريح — يُدمجان (تقرير واحد بإدخالين) — يقابل C-POS-01 (لكن هنا متطابقان حرفياً لا مختلفان!) |
| **C-MR-03** | **§24.2 Tax Report وصفه حرفياً مطابق لـ§24.1 VAT Report** (جملة-بجملة: "a list of all taxes that are incorporated during receipt of Items... posted in the Receipt entry...") رغم أنهما تقريران بشاشتين مختلفتين | MGT-REP §24 ص107-111 | غموض توأمية — يُرجّح تكرار وصف (تقريران فعليان أم واحد؟) — UNK-090 |

> (MGT — دون مستوى التناقض: "Sun Cost Center" بدل Sub (§16 ص90) · "Audit **Trial**" بدل Trail (§23 — يتكرر في FAS §33!) · "comments of **customer**" في سياق مخزني (4.1) · أخطاء ترقيم خطوات: 5.1 تقفز 4→"3" و4.6 تقفز 4→6.)

### FAS-REP (تناقضات 3)

| ID | الوصف | المصدر | القرار |
|---|---|---|---|
| **C-FA-01** | **حديقة أسماء الجسور**: نفس منظومة جسور FO/POS↔المالية بثلاث اصطلاحات مختلفة — §19 "**POS to Finance Defn**" مقابل §20 "**FOS to FA**" (FOS لا تُعرَّف في أي مكان!) مقابل §21 "**FOM**" (نوع واحد يشمل "Front Desk **and** Point of Sale") — مع FO/FOM/FOS/POS/FA/Finance قاموس مترادفات غير معلن | FAS-REP §19/§20/§21 | يُبنى جدول مرادفات موحد عند التحويل (F-FA-12) — FOS الأرجح = Front Office System (POS?) |
| **C-FA-02** | **أوصاف Trial Balance الثلاثة متطابقة حرفياً** (TB / TB Format 2 / TB (3.3)) — والثالث نصه كله: "Fill in all the fields **as explained in the section 'Trial Balance Format 2'**" (إحالة ذاتية بلا جسم) | FAS-REP §9 ص24-29 | أكبر عائلة نسخ-نص في وحدة واحدة — تُدمج ×4 في تقرير واحد بوضعيات عرض (UNK-099) |
| **C-FA-03** | **عنقود أخطاء تحريرية في أعمدة وخطوات حساسة**: "**deference value**" بدل difference (أعمدة Contract Debit Note List §16) · "continues" بدل continuous (§24/§25 في قانون Print Forms!) · خطوة مرقمة **"8"** بين 1 و3 في Voucher Print (§25) | FAS-REP §16/§24/§25 | تصحيحات تحريرية — تُنقل بالأسماء الصحيحة مع توثيق الأصل |

> (FAS — دون مستوى التناقض: "Trial" بدل Trail ثانية (§33 — خطأ منسوخ عبر MGT+FAS!) · أوصاف 26C/26K شبه متطابقة · "stuffs" (§15 — عامية) · الترقيم داخل خطوات 16A يقفز 6→7→"10".)
