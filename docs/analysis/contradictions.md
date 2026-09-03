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


