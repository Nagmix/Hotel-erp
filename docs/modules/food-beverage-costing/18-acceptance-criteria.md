# 18 — معايير القبول (Acceptance Criteria) — وحدة FNB

> **10 مجموعات / 48 معياراً** + **Smoke Test من 26 خطوة** — التركيز على: البوابة الأحادية · معادلة COST% (قابلة للاختبار الرقمي!) · دورة الجرد → افتتاحي الغد · XOR الربحية · خلود Auto Indent · وعدم تسرب أي قيد مالي.

---

## المجموعات

### AC-01: بوابة التفعيل (5)
1. لا يمكن حفظ Start Date والPOS غير جاهزة/بلا بيانات إلا بتحذير/منع موثق السلوك (التطابق مع "recommended" الأصلية قراراً).
2. بعد الحفظ الأول: **أي محاولة تعديل starting_date تُرفض** برسالة (الأصل: صمت الحقل — نفعّل الرسالة).
3. user_id وlast_updated يُسجلان آلياً عند كل لمسة.
4. Audit Date تحظر المعاملات بعدها (رفض موثق السلوك).
5. Singleton: لا يوجد سجل ثانٍ ممكن للفندق.

### AC-02: الربط الثلاثي (5)
6. Cost Centers متعددة → Kitchen واحد مسموح؛ عكسها يُقيَّد.
7. Sales Tag يعزل منافذ Non-Revenue في كل تقارير التكلفة.
8. تجميع كل التقارير البيعية/التكلفية على **Kitchen** (وليس Restaurant).
9. تعديل مطبخ صف/مجموعة بالنقر المزدوج يعمل ويسجل.
10. حزمة Required Reports تُحفظ لكل إعداد وتظهر افتراضياً.

### AC-03: الميزانيات (6)
11. اختيار Session لشهر ينتشر افتراضياً لبقية السنة المالية (حرفياً: مارس 2007→كل 2007).
12. Covers لا تُقبل قبل Sales Budget (التسلسل الموثق).
13. Per Month يوزع بالتساوي و**Difference يظهر** عند أي تعديل يدوي للتوزيع.
14. Cost% واحدة تنطبق على كل أيام الشهر (وتقبل تعديل خلية).
15. إشارة التباين: فعلي>ميزانية → **سالب** (والعكس موجب).
16. Sales Analysis يعرض الثلاثي يوم/شهر/سنة + Budget + Variance.

### AC-04: محرك الوصفات (7)
17. Recipe Code: 6 رقمي إلزامي (رفض غير المطابق).
18. Portion نص حر يُخزن ويُعرض ("2 vegetable rolls").
19. مكون Store Item يظهر desc+UOM آلياً من MGT (F1).
20. Sub Recipe مشترك في وصفات متعددة بكميات مختلفة.
21. POS Item يقبل **وصفة واحدة فقط** (محاولة ثانية تُرفض).
22. وصفة واحدة تخدم Res Codes/POS Items متعددة.
23. عند سعر بيع < تكلفة: يظهر "Warning!! Item Price is less than the Cost price" — **والحفظ ينجح** (غير حاجب).

### AC-05: الاستخراج والتدفق (5)
24. Batch: Date Range + Process يعمل ويرفض نطاقاً يسبق Start Date.
25. INI#368=1: Issues تنتقل لحظياً بلا Batch يدوي.
26. COST% المحسوب: **COST % = Cost per Portion / PRICE × 100** — اختبار رقمي: تكلفة 60 وسعر 200 → 30%.
27. SWITCH 511=0: KOT بكمية > الرصيد الحالي **يُرفض** في POS.
28. SWITCH 511=1 (أو غير مفعّل): البيع يمر بلا فحص رصيد.

### AC-06: دورة الجرد (6)
29. Kitchen Stock: Reference# 3-10 أبججدي-رقمي (رفض خارج النطاق).
30. Physical يُدخل المتاح وAdjustment يُدخل المستهلك (عالمان منفصلان).
31. الافتتاحي: سجلات MGT تظهر Pink، والصفرية Green.
32. الإدخال متاح على Green فقط (double-click) + rate يدوي للأصناف بلا سعر.
33. Stock Balance Transfer (Transfer): الرصيد الفعلي اليوم = افتتاحي الغد.
34. الترحيل السنوي ينقل FY→FY دون فقد أرصدة (وCancel يعكس اليوم).

### AC-07: الإدخال اليدوي والتحويلات (5)
35. Manual Sales: Consolidated = قيد واحد؛ Item-wise = سطر لكل صنف.
36. Manual Consumption: UOM مقفل من ماستر MGT + الكمية بوحدتي Stock/Conversion.
37. Value = Qty × Rate يُحسب آلياً.
38. Inter Kitchen Transfer بين مطبخين بصنف وكمية وRemarks.
39. Value Transfer ينقل قيمة إجمالية **بلا أصناف** (لا أثر على تقارير الأصناف).

### AC-08: الطلب الآلي (3)
40. توليد Auto Indent من Restaurant+Item+Qty ينتج طلباً قابلاً للاستخدام في MGT.
41. **أي modify/delete بعد التوليد يُرفض** (في الأصل) — في Frappe: يُلغى قبل التقديم فقط (D-FB-3).
42. rate/value تتولد آلياً عند إدخال الكمية.

### AC-09: الاستعلامات والتقارير (5)
43. Profitability: اختيار Issue Based **يقفل** Restaurant؛ Recipe Based **يقفل** Kitchen (XOR حرفي).
44. Drill-down ينتهي بـ"No Drill Down Available for this Category" عند الحد.
45. Missing Recipe List يسرد أصناف POS بلا وصفة بدقة.
46. Standard vs Actual: **Standard من الوصفة وActual من استهلاك مراكز التكلفة** (المتن لا الأقواس!).
47. Recipe–Ingredient: زر Consolidate يجمع المكونات عبر الوصفات.

### AC-10: العزل المالي (1)
48. **أي فعل في الوحدة لا يولّد قيداً واحداً في GL** — فحص كامل سجل Journal بعد Smoke Test (راجع 11).

---

## Smoke Test (26 خطوة — يوم تكلفة كامل)

| # | الخطوة | المجموعة | المتوقع |
|---|---|---|---|
| 1 | (تجهيز) التأكد من POS+MGT ببيانات | AC-01 | جاهزية |
| 2 | إدخال Costing Start Date = أول الشهر | AC-01 | حفظ نجح |
| 3 | محاولة تعديل التاريخ | AC-01 | **رفض** |
| 4 | Costing Link: ربط مطعم Breakfast بمطبخ Main (Group Code) | AC-02 | "Records Saved Successfully" |
| 5 | وسم منفذ Staff Canteen بSales Tag=Non-Revenue | AC-02 | حفظ |
| 6 | Defaults: انتقاء 3 تقارير مطلوبة | AC-02 | تظهر لاحقاً افتراضياً |
| 7 | Sales Budget مارس (Per Month=31,000) + Session=All | AC-03 | توزيع 1,000/يوم |
| 8 | تعديل يوم 15 إلى 500 | AC-03 | **Difference=+500** |
| 9 | Cost Budget=30% | AC-03 | كل الأيام 30 |
| 10 | Recipe كود 100001 "Veg Roll" حصة "2 vegetable rolls" | AC-04 | حفظ |
| 11 | مكون: Store Item دقيق 1kg (F1) + Sub Recipe صوص طماطم 150g | AC-04 | desc/UOM/قيمة آلية |
| 12 | Cost Analysis: ربط POS Item "VegRoll-BF" + إدخال سعر أقل من التكلفة | AC-04 | **التحذير الظاهر + نجاح الحفظ** |
| 13 | Kitchen Opening Stock: مطبخ Main — إدخال Green صنف الأرز 20kg | AC-06 | rate/value آلية |
| 14 | Costing Extraction (Batch) نطاق أول الشهر | AC-05 | رسالة اكتمال |
| 15 | تفعيل INI#368 + إدخال Stock Entry صرف في MGT | AC-05 | وصول لحظي لحوض FNB |
| 16 | تفعيل SWITCH 511=0 ومحاولة KOT بكمية > رصيد | AC-05 | **رفض البيع في POS** |
| 17 | Manual Sales (Consolidated) منفذ ورقي 2,500 جلسة Dinner | AC-07 | قيد واحد |
| 18 | Manual Consumption: مركز Banquet استهلاك 3kg بوحدتي UOM | AC-07 | Value=Qty×Rate |
| 19 | Inter Kitchen: Main→Banquet 5kg أرز | AC-07 | سجل + Remarks |
| 20 | Value Transfer 1,200 من Liquor إلى Food | AC-07 | قيمة بلا أصناف |
| 21 | Kitchen Stock (Physical) نهاية اليوم | AC-06 | Reference# مقبول |
| 22 | Stock Balance Transfer (Transfer) | AC-06 | افتتاحي الغد = فيزيائي اليوم |
| 23 | Auto Indent: VegRoll-BF بكمية 40 | AC-08 | indent في MGT + **محاولة حذف تُرفض** |
| 24 | Profitability (Recipe Based) ومحاولة اختيار Kitchen | AC-09 | **مقفول** (XOR) |
| 25 | Sales Analysis اليوم + Cost Report (Detail) + Missing Recipe List | AC-09/AC-16 | أرقام يوم/شهر/سنة + ميزانية |
| 26 | فحص GL بعد كل ما سبق | AC-10 | **صفر قيود** |
