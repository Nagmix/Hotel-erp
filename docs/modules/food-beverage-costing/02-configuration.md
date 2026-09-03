# 02 — الإعدادات (Configuration) — وحدة FNB

> إعدادات FNB **مزدوجة المصدر**: (أ) داخلية — 4 ماسترات تهيئة (راجع 01) مع بوابتها أحادية الاتجاه؛ (ب) **مفاتيح INI/Switches عابرة للوحدات** — عادت الوحدة بمفتاحين بعد عائلة الخمسة بلا INI (CARE/MEM/SLM/TEL/MNT)، وأخطرهما **يضبط سلوك POS ذاته**. ولا توجد عائلة Module Attributes موثقة هنا (عائلات FO/POS/BNQ/SET/ENG كافية حتى الآن — لا FNB#).

---

## 1. بوابة التفعيل (Activation Gate) ⭐

**Costing Start Date** (SET §1):

1. **شرط الأهلية التشغيلية**: "It is recommended that **only when both the Point of Sale and Materials Management modules are fully operational**, the Costing Start Date should be specified, else the MIS reports will not be generated **due to insufficient details**" — أول شرط تفعيل يقيد وحدة بجاهزية **وحدتين أخريين** نصاً.
2. **الأحادية**: "CAUTION: Once the Start Date is entered, **updating the same will not be allowed**" + "You will not be able to edit the date appearing in this field **once it is created**" — لا رجعة (بلا مسار تصحيح موثق — GAP-FB-P01).
3. **الأثر**: "Based on the date specified here, the **Sales and Consumption details will get extracted** from the Point of Sales and Materials Management modules... for generation of **Sales and Cost MIS Reports**".
4. **Audit Date**: قفل المعاملات بعد تاريخ (SET ص3) — أداة الإقفال الزمني للوحدة.

## 2. مفاتيح INI وSwitches الموثقة

| المفتاح | الاسم | القيمة الموثقة | السلوك الحرفي | المصدر |
|---|---|---|---|---|
| **INI #368** | **ONLINEFBCOSTING** | =1 | "Online transfer of Issues from inventory to costing based on INI#368 settings. If INI is activated **no need to do manual extraction** for inventory issued items" + Note: "To activate costing extraction, INI switch **#368 (ONLINEFBCOSTING) to be set to 1**" | COP ص3-4 |
| **SWITCH #511** | **autodeductionliqsale** | **=0** | "if this switch is set to 0, in real time during Current stock balance will be checked **KOT punch. Items cannot be sold, if the quantity is greater than the current stock**" | COP ص3 |

> ⚠️ **قراءتان معماريتان:** (1) #368 يبدّل الوحدة من **دفعات يدوية** (Costing Extraction بشاشة وتاريخ من-إلى وزر Process) إلى **تدفق لحظي** من المخزون — أول ثنائية Batch/Online موثقة كاملة في المشروع. (2) #511 **اسمه يخص الخمر** (autodeduction**liq**sale) لكن نصه عام لكل الأصناف عند KOT — عدم تطابق اسم/سلوك + القيمة الافتراضية مجهولة (UNK-063)، وهو المفتاح الوحيد في المشروع الذي يُغيّر سلوك **وحدة أخرى (POS) من دليل وحدة ثالثة (FNB)**!

## 3. إعدادات الربط الثلاثي (SET §2)

- **Cost Type أولاً** — كل الربط داخل عائلة نوع التكلفة (Food/Liquor/Soft Drinks/Smokes).
- **Link By = Group Code أو Item Code** — دقة الربط من مجموعة POS كاملة حتى صنف واحد.
- **From/To** نطاق المجموعات/الأصناف + **Display: All/Un Tagged/Tagged** لعرض المربوط وغيره.
- **Tag Kitchen/Bar** بزر تأكيد Yes — إسناد مطبخ/بار.
- **تغيير لاحق بالنقر المزدوج** على عمود Kitchen Code → شاشة مساعدة Kitchen Code Help.
- **Defaults** — انتقاء Required Reports من Available Reports (حزمة التقارير الافتراضية للمستخدم).

## 4. إعدادات الميزانيات (SET §3)

- **النمط الشهري**: "The sales budget should be defined for given month / year and can also be **predefined for future months**".
- **الجلسة الافتراضية تنتشر سنة مالية كاملة**: قاعدة March 2007→كل 2007 (راجع 01 §2.3) — قرار "uniformity" موثق حرفياً.
- **نمطا التوزيع**: Per Day (إدخال يدوي بشبكة التقويم) / Per Month (توزيع متساوٍ آلي + عداد Difference).
- **الميزانية التكلفية**: نسبة مئوية واحدة "applicable to **all the days of the month**" قابلة للتعديل خلية-خلية.
- **التسلسل**: "define **Sales Budget figures first**, followed by the **Covers Budget**" عند إدخال الاثنين.

## 5. إعدادات الوصفات (SET §4)

- **إلزامية شرطية**: "Defining of Recipe Items is **mandatory only if the Recipe based method of Costing is followed**" — اختيار المنهج (وصفي/استهلاكي) يُقرر معمارياً هل الوصفات مطلوبة أصلاً!
- **Yield %** يُ.populate آلياً (المصدر غير موثق — UNK-067) ويُعدل "by **deleting existing %**".
- **Process Type**: None أو Add New (إنشاء قيمة جديدة inline).
- **F3** ينقل المؤشر من شبكة الوصفة إلى Cost Analysis — اختصار تدفق الإدخال الوحيد الموثق في الوحدة.

## 6. إعدادات التشغيل (COP)

| الإعداد | الوصف |
|---|---|
| **معيار الجرد** | Stock Type ثنائية: "Adjustment: Enter the amount of stock **the user has consumed**. Physical Stock: Enter the amount of **physical stock available**" — عالمان للمقارنة (COP ص5) |
| **التحويل البيني** | شاشة Transfer Options تسبق كل عملية — "Select the **type of transfer process**" (COP ص13) |
| **ترحيل الأرصدة** | خيارا Transfer/Cancel + اختيار Property (متعدد الفنادق!) — "The rest of the fields will **auto populate**" (COP ص16-17) |
| **Auto Indent** | Entry Date + Load ثم Selected POS Items — "restaurant code and the item code. The related fields appear" (COP ص17-18) |

## 7. غائبو الإعدادات

- **لا User Rights/Groups** إطلاقاً (سادسة بعد CARE/MEM/SLM/TEL/MNT — راجع 07).
- **لا مفاتيح INI أخرى** رغم ضخامة الوحدة (368/511 فقط) — لا مراقبة جودة؟ لا عتبات variance؟
- **لا إعدادات ألوان/تنسيق تقارير** موثقة (80/132 عموداً خيار عند Standard vs Actual فقط — REP ص23).
- **لا إعداد Default Costing Link** لطباعة أو Export — وPrint Buffet الوحيد ب**اختيار طابعة** من قائمة (REP ص27).
