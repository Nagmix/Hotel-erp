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
