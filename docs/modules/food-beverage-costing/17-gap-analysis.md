# 17 — تحليل الفجوات (Gap Analysis) — وحدة FNB

> **GAP-FB-D01..D07 (توثيق) + GAP-FB-P01..P05 (عملية/وظيفة)** + **UNK-063..067** + **تناقض واحد مسجل (C-FB-01)**. الأخطر حاكياً: **سادسة بلا User Rights** وقيادة سلوك POS من مفاتيح بلا مالك موثق. الأخطر عملياً: **بوابة تفعيل بلا طريق رجعة** و**Auto Indent الخالد**.

---

## أ) فجوات التوثيق (Documentation Gaps)

### GAP-FB-D01: صلاحيات غير موثقة (السادسة)
- لا قسم User Rights في الملفات الأربعة (بعد CARE/MEM/SLM/TEL/MNT) ولا ذكر Role واحد.
- الأخطر: **Audit Date وStart Date وSWITCH 511 وAuto Indent** — أفعال قفل/تقييد/توليد خالدة بلا ضابط موثق (07 §3).

### GAP-FB-D02: لا خريطة GL ولا إقفال تحليلي
- الصفرية متعمدة (MIS — راجع 11) لكن **لا إقفال شهري للتقارير** موثق (Audit Date سقف عام فقط) — إمكانية "تحريك" جرد/استهلاك لاحق تعدل تقارير شهر مقفل = خطر اتساق تاريخي.

### GAP-FB-D03: تناقض Standard/Actual (الأول من نوعه داخل الوحدة الواحدة) ⭐
- LUK ص12: "Standard Cost **(Consumption)** and Actual Cost **(Recipe)**" — الأقواس.
- REP ص22: "Standard consumption is **based on recipe details**. Actual is arrived **based on consumption at cost centers**" — المتن.
- **المتن حاسم** والموافق لنظرية تكاليف F&B القياسية (النظري وصفي/الفعلي استهلاكي)؛ الأقواس معكوسة في كلا العنوانين. مسجل في سجل التناقضات **C-FB-01**.

### GAP-FB-D04: قيم Report Format + "potential" غير معرَّفة
- Cost Report: "Select one of the report formats from the **Report Format dropdown list**" (REP ص19) — القيم غير معدودة.
- "to know the cost, based on **consumption/kitchen/potential or recipe**" — **"potential"** رابع المنهجات بلا تعريف في 65 ملفاً (UNK-064).

### GAP-FB-D05: انفجار Auto Indent غير مرئي
- الشاشة تعرض POS Item + Qty مباشرة (COP ص17-18) — **أين تظهر مكونات الوصفة المنتفجرة؟** لا شاشة سطور مكونات موثقة. المرجع "link POS menu items with their ingredients" يفترض انفجاراً لا توثيق له.

### GAP-FB-D06: SWITCH 511 — اسم/سلوك/ملك
- اسم "autodeduction**liq**sale" (خمر) ونص عام (كل أصناف KOT!) + **أي رصيد يُفحص** (حوض FNB التحليلي أم Stock Ledger MGT؟) + قيمة افتراضية غير موثقة (UNK-063).

### GAP-FB-D07: قوائم مفتوحة بلا مالك
- NC Type: "Complimentary, Spoilage or for House Consumption **etc.**" · Session: "Breakfast / Lunch / Dinner **etc.**" — عائلتا قائمة بلا ماستر موثق الموطن (UNK-066).

## ب) فجوات العمليات والوظيفة (Process Gaps) ⭐

### GAP-FB-P01: بوابة بلا إنعاش (Disaster Recovery غائب)
- Start Date خالد خطأً = "updating the same will not be allowed" — **لا مسار تصحيح موثق** (replicate-from-scratch؟ intervention؟). أثره: بداية استخراج خاطئة تلوث كل تاريخ MIS.
- **الحل المقترح**: Singleton مع صلاحية System Manager + إجراء "Reset Activation" مُسجَّل أثره (يكسر الحرفية بسلامة تدقيق).

### GAP-FB-P02: عبء الجرد اليومي الورقي
- Kitchen Stock يدوي خالص (ملاحة أعمدة + F1 لكل صنف + Enter) — **أغلى عملية تشغيلية في الوحدة** لكل مطبخ كل يوم.
- الحل: mobile count-sheet + استيراد باركود/ميزان.

### GAP-FB-P03: Auto Indent الخالد
- "not allowed to modify or delete" فور التوليد — خطأ كمية → طلب خاطئ يستهلك دورة MGT ولا يُصحح.
- الحل: Draft قابل للإلغاء قبل التقديم (F-FB-7/D-FB-3) — نفس مستوى الحماية بلا الفخ.

### GAP-FB-P04: سلوك رفض KOT غير موثق
- الحاجب يمنع البيع (V-FB-07) لكن **رد فعل POS عند الرفض** (رسالة؟ منتج بديل؟ جزء شيك؟) غير موثق في FNB ولا POS المقروء — أخطر ثغرة UX تشغيلية عابرة للوحدتين.

### GAP-FB-P05: لا لقطات تاريخية للتكلفة الوصفية
- أسعار الأصناف متغيرة (MGT) والوصفة بلا إصدارية (لا Applicable From!) — **COST% التاريخي غير قابل لإعادة الإنتاج** بعد تغير الأسعار (نمط الخلود الزمني غائب تماماً من الوحدة).
- الحل: BOM Versioning في ERPNext (is_default + تواريخ) — مجاني.

## ج) المجهولات الجديدة (UNK-063..067)

| ID | السؤال | الأثر | المصادر | المسار |
|---|---|---|---|---|
| **UNK-063** | دلالة SWITCH 511 الكاملة: نطاق المنع (كل الأصناف أم الخمر فقط كما يوحي الاسم؟) · أي رصيد يُفحص (FNB أم MGT) · القيمة الافتراضية · وسلوك POS عند الرفض | حاجب بيع لحظي بلا مواصفة سلوك رفض — يقرر عمق الفحص في إعادة البناء | COP ص3 + POS المقروء (لا ذكر للسويتش هناك!) | [NOT DOCUMENTED — GAP-FB-D06] قرار Feature Flag كامل المواصفة (F-FB-11) |
| **UNK-064** | قائمة قيم Report Format في Cost Report + تعريف منهج "potential" | التقرير الجامع (الأثقل) غير قابل للتطابق الحرفي بلا قيمه | REP ص19-20 | [NOT DOCUMENTED] تُستقرأ من فروع Consumption/Kitchen/Potential/Recipe الأربعة المذكورة؛ Potential = تكلفة نظرية من سعر البيع؟ (استنتاج F&B معياري يُعتمد قراراً) |
| **UNK-065** | هل أقواس Standard/Actual في LUK/REP تسمية معكوسة فقط أم منهجان مختلفان فعلاً (Q مقابل R)؟ | سلامة أعمدة أهم تقريرين تحليليين | LUK ص12 + REP ص22 | [CONTRADICTION C-FB-01] المرجح: تسمية رديئة والمتنان متطابقان (Standard=Recipe) — يُعتمد المتن ويوثق الاستثناء |
| **UNK-066** | موطن ماسترات NC Type وSession وMenu Type وKOT Type المستهلكة في FNB (etc. مفتوحة) | 4 قوائم مدخل تشغيلي بلا بيت | COP ص10 + LUK ص6 + POS المقروء | [INFERENCE] POS-SET الأرجح (قوائم/جلسات) وSYS للبقية — يُحسم عند POS-SET النهائي/findex كاملة |
| **UNK-067** | مصدر auto-populate لـYield% وProcess Type الافتراضي في بنود الوصفة | قيم افتراضية تُسبق إدخال المستخدم — من أين؟ | SET ص12 | [INFERENCE] ماستر صنف MGT أو Process ماستر غير مرئي — يقرر حقلاً default في BOM |

## د) المقارنة العائلية الختامية

| العائلة | حالة FNB |
|---|---|
| بلا User Rights | **السادسة** (CARE/MEM/SLM/TEL/MNT/FNB) — عائلة "الجيل الأحدث" شبه كاملة |
| بلا INI | **انكسرت!** — FNB تعيد مفاتيح #368/#511 بعد خمسة أعضاء (أول عودة) |
| صفر قيود GL | **العضو الأنقى** (بيانات مالية شكلاً بلا قيد واحد) |
| شرِكات الهروب | **لا شيء** — أول وحدة "مخزنية" بلا قيمة سحرية (الاستبدال البنيوي: Missing Recipe List) |
| الخلود الزمني | **غائب كلياً** — لا Applicable From في أي ماستر (فجوة P05) |
| Lookup-as-Editor | **الثالثة** (Open/Modifier) بعد TEL/MNT |
| اللون حالة | **الثالثة** (Pink/Green) بعد POS/MNT — وهنا "دعوة كتابة" |
