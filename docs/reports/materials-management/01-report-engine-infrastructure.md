# 01 — محرك التقارير والبنية التحتية — Materials Management (Phase 7)

> تُوثّق هنا أنماط التوليد المشتركة لكل تقارير MGT-REP (~53 فريداً) — بعيداً عن تفاصيل كل عائلة.

---

## 1. النمط التفاعلي: الخطوتان الموحدتان (Preview → Generate)

كل تقرير — بلا استثناء واحد في 112 ص — يتبع نفس الحركة:

```
شاشة المعايير → "Click [زر] to view the below screen" (معاينة شكل التقرير)
              → "Click [زر] to generate the report" (التوليد الفعلي)
```

- **الخطوة الأولى = معاينة شكل التقرير** (Format Preview) قبل التوليد — نفس نمط FNB "Preview→Generate" (12/13 تقريراً هناك).
- **الخطوة الثانية = توليد/طباعة** — الأزرار في النص المستخرج بلا تسميات (صور)، لكن الأفعال الموثقة: *view → generate* (الأغلبية) · *view → print* (عائلة 15 و16.2/18.x الجزئية) · *view → Load* (§17 وحده!).
- **الفعل "Load"** في Re-Order Level Items (ص94): "click **Load** to view the below screen" — ثالث فعل إخراجي في MGT (view/generate/load مقابل print) — **إن Load هنا يجلب بيانات ديناميكية** (رصيد اللحظة) لا أرشيفاً — دليل لغوي على as-of-now semantics.

**المقارنة عبر المرحلة 7:**

| الوحدة | النمط الغالب | قنوات الإخراج الموثقة |
|---|---|---|
| FO (135 تقريراً) | معايير → توليد مباشر | **4 قنوات موحدة**: display, print, spool, export + Print or Email |
| POS (~57) | معايير → توليد | 4 + **Port ID** (خامسة خاصة) |
| **MGT (~53)** | **خطوتان Preview→Generate** | **طباعة ومعاينة فقط — صفر Spool/Export في النص كله** |

**الدلالة:** MGT تفتقد قناة التصدير الإلكتروني الموثقة (رغم أن UNK-081 سجل "Excel موثق في MNT/MGT" من ملفات أخرى — Parameter Listing في MNT-RPL) — في طبقة REP نفسها **لا قناة إلكترونية**. هذا يجعل MGT أكثر وحدات المرحلة 7 "ورقية" — يتسق مع اكتشاف 15.x: أشكال الطباعة برامج لكل عميل.

## 2. أزرار الطابعة و"القائمة المعرفة مسبقاً"

- في 15.1/15.3/15.4: "**Select the Printer from the pre-defined list**" — قائمة طابعات معرفة مسبقاً تظهر في شاشة الطباعة.
- مصدر القائمة غير موثق في REP (MGT-SET؟ SYS؟ FAS؟) → **UNK-093**.
- FO كشفت Port ID كطبقة أجهزة؛ MGT تكشف **طبقة قوائم طابعات** أعمق (أكثر من مجرد منفذ) — عائلة أجهزة الطباعة تتوسع بعنصر ثالث.

## 3. القانون الأكبر في الوحدة: Print Forms عبر FAS (اعتماد تكويني عابر للوحدات)

النص الحرفي (يتكرر 3 مرات — 15.3 و15.4 و15.6):

> "To print the Purchase Order, **the name of the Purchase Order print program has to be specified in the Print Forms parameter under the Financial Management module**. The definition of the program name is **mandatory** for printing... as **customized programs are developed for each client** as per their specifications to print either on **pre-printed or plain continuous or cut stationery**."

**تفكيك القانون:**

| العنصر | المعنى المعماري |
|---|---|
| "specified in the Print Forms parameter **under the Financial Management module**" | برنامج الطباعة يُسجَّل في **FAS-SET §15** (مؤكد: "To set Pgm.ID for Print Forms" — FAS-SET ص1069) — MGT تستهلك تكوين وحدة أخرى |
| "The definition... is **mandatory**" | بلا تسجيل البرنامج **لا تعمل الطباعة أصلاً** — أعلى درجة اعتماد (Hard Dependency) |
| "customized programs are developed **for each client**" | طبقة الطباعة **ليست منتجاً معيارياً** بل كود لكل عميل — يفسر غياب أي تخطيط مطبوع في 65 ملفاً! |
| "pre-printed or plain continuous or cut stationery" | **ثلاثية الورق**: ورق مطبوع مسبقاً (نماذج جاهزة) · ورق متصل عادي (Continuous) · ورق مقطوع (Cut Sheet) — إرث عتاد طباعة الثمانينيات/التسعينيات موثق حرفياً |

**الأثر على فهم الحزمة كلها:**
1. **غلق جزئي للغيب البنيوي**: لماذا لا توثق الأدلة أشكال المطبوعات؟ لأنها **كود مخصص لكل تثبيت** — الوثيقة العامة لا تستطيع توثيق ما يختلف عميلاً عن عميل.
2. **عائلة بنية تحتية رابعة**: بعد FIMSHTBL (جدول مسرب) وPMSPOL.INI→POL.SPC (ملف تخصيص) وIDS Crystal Report Designer — الآن **Print Forms Pgm.ID** طبقة رابعة: سجل برامج طباعة مخصصة عبر FAS.
3. **MGT-SET §28 User Defined Print Forms شيء آخر**: SET يحيل إلى Getting Started (خارج الحزمة — GAP-SYS-D02) بينما REP يحيل إلى FAS-SET §15 — **مصدران مختلفان لاسمين متشابهين** (يُفرّق بينهما في 04).

## 4. الإدخال المدمج للمعاملات (FSN — نمط تفاعلي فريد)

النص الحرفي (§12 ص74): "Double-click **on the Days column** to view the below screen. Enter the FSN Specifications as shown below and click [Save]."

- تعريف معاملات التحليل (Cut off Days + Fast/Slow quantities) يتم **داخل شاشة اختيار التقرير نفسها** عبر خلية عمود Days — وليس من Setup مستقل.
- ثم: "Enter the FSN details **for all the groups** of items" — المعاملات **لكل مجموعة أصناف** (Grid of parameters).
- يقابل مصدراً رسمياً آخر: MGT-SET §18 "Define FSN parameter" — فأيهما الشاشة الأم؟ (REP يعيد تعريفها من داخل التقرير!) → تقاطع تكويني يُسجل في UNK-094.

## 5. الصلاحيات: صفر مطلق — الوحدة 11/17

لا ذكر واحد لصلاحية/مستخدم/دور في 112 ص (عدا أثر المستخدم الضمني في Audit Trial). عائلة "REP بلا صلاحيات" تتوسع:

FO (9) → POS (10) → **MGT (11)** → (FAS التالية 12/17؟)

**خطورة أعلى هنا من POS:** تقارير MGT تشمل **Audit Trial بالمحذوفات** و**VAT لسنة التقييم** — بلا أي ضابط وصول.

## 6. ملاحظات المحرك الختامية

- **لا Program IDs ولا INI switches**: على عكس FO (FOMRR15 + Switch 63) وPOS (137/335) — MGT-REP **لا يضيف أي مفتاح INI جديد** (عائلة INI تتجمد عند 63/137/335/368/475/511) ولا يكشف تسمية برامج تقارير — الوحدة الأكثر "صمتاً" تقنياً في المرحلة 7.
- **الفلاتر الثابتة القابلة للاختبار**: Passive records (§1) · Open Items (4.4/4.5/9.1/VAT) · Contract/Open (6.2) · Stockable/Direct (5.2) — معجم فلاتر الأصناف الأغنى في الحزمة (كلها انعكاس ماستر MGT-SET).
- **ثلاثية Complimentary** (4.2): Inclusion / Exclusion / **reflection of only** — نفس بنية Void/Comp في POS لكن بثلاث حالات صريحة.
- **Store Break** (4.2): "To reflect each Store on a new Page" — تحكم ترقيم صفحات حسب المتجر — عنصر Layout نادر التوثيق.
- **التسلسل بميتاداتا**: §1 يتيح الترتيب بـ**Last Updated** و**Physical Location** — تسلسل بميتاداتا التحرير والموقع الفيزيائي (فريد).
