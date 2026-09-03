# 13 — الحالات الحدية والاستثناءات (Exceptions & Edge Cases) — وحدة FNB

> 28 حالة حدية موثقة/مستنتجة من الحرفية المصدرية — أبرزها: بوابة لا تُصحَّح · جرد اللونين · تحويل بلا أصناف · وثيقة تولد خالدة · ونقطة التقاطع مع POS لحظة البيع.

---

## أ) التفعيل والبوابات

1. **[موثق] التفعيل قبل جاهزية POS/MGT**: "else the MIS reports will not be generated **due to insufficient details**" (SET ص3) — نقص بيانات صامت (أي تقارير تولد؟ فارغة؟ خطأ؟ غير محدد).
2. **[موثق] محاولة تعديل Start Date بعد الإدخال**: "updating the same **will not be allowed**" (SET ص3) — لا مسار تصحيح (تواريخ خاطئة = إعادة تدوير كاملة؟ — GAP-FB-P01).
3. **[موثق] Audit Date يقصّ الماضي**: "date beyond which the transactions are not allowed" — إدخال جرد/استهلاك لاحق للسقف مرفوض ضمنياً (رسالة الرفض غير موثقة).
4. **[مستنتج] إدخال Audit Date قبل Start Date**: علاقة الترتيب غير موثقة — سيناريو قفل فوري بعد التفعيل؟

## ب) الوصفات وPOS

5. **[موثق] سعر بيع أقل من التكلفة**: "Warning!! Item Price is less than the Cost price" (SET ص12) — **تحذير غير حاجب** — البيع الخاسر جائز (نمط POS.
6. **[موثق] POS Item بلا وصفة**: Missing Recipe List يرصدها (REP ص13) + "If the recipe is not defined, then you **cannot view the details**" (LUK ص5) — البيع مستمر والتحليل الوصفي يتعطل فقط.
7. **[موثق] نصف مصنّع بنفسه مكوناً**: Sub Recipe داخل Sub Recipe؟ غير موثق (النص: sub recipe في recipe — التداخل الأعمق مفتوح).
8. **[مستنتج] دورة وصفة ذاتية**: Recipe A مكونها Sub Recipe S، وS مكونها A؟ لا كشف دورات موثق (BOM-cycle!).
9. **[موثق] معدِّلات بلا ربط**: Open/Modifier Items تسرد ثم **تبني الربط من الشاشة نفسها** (COP ص15-16) — قناة ترميم موثقة.
10. **[موثق] Yield% مصدره مجهول**: "The yield % and quantity **auto populate**" (SET ص12) — من أين؟ (UNK-067).

## ج) المخزون والجرد

11. **[موثق] صنف بلا سعر في الافتتاحي**: "It will allow to enter the rate of the items **which do not have rates**" (COP ص8) — قناة سعر يدوي استثنائية.
12. **[موثف] Adjustment مقابل Physical**: "Enter the amount of stock **the user has consumed**" مقابل "the amount of **physical stock available**" (COP ص5) — إدخال Consumption كعائلة جرد (وليس استهلاك MGT!) — ثنائية دلالية موثقة.
13. **[موثق] سجل Pink (مستخرج من MGT) يظهر في الافتتاحي**: التداخل مع رصيد MGT نفسه — هل يُعدَّل؟ (النص يوجه الإدخال للGreen فقط — تعديل المستخرج غير موثق).
14. **[مستنتج] جرد يوم مزدوج**: Reference# فريد لكن هل يُمنع تاريخ مكرر لنفس مطبخ/نوع؟ غير موثق.
15. **[موثق] Cancel لترحيل الرصيد**: شاشة Cancel كاملة (COP ص16) — ما مصير يوم بلا افتتاحي بعد الإلغاء؟ (سلسلة تقارير اليوم التالي).
16. **[موثق] ترحيل سنوي بخصائص يومية**: نفس الأداة تنقل FY→FY — سيناريو منتصف السنة/ترحيل جزئي غير موثق.
17. **[مستنتج] رصيد سالب**: لا معالجة موثقة لعجز فعلي > حاسوبي عند الترحيل (Variance سالبة فقط؟ أم رفض؟).

## د) الإدخال اليدوي والتحويلات

18. **[موثق] منفذ غير محوسب يبيع عبر Supplying Restaurant**: "Select the **Supplying Restaurant** from the list provided where the manual sales has taken place" (COP ص10) — ثنائية مطعم/مجهّز في البيع اليدوي (صياغة المصدر تكرر نفسها حرفياً للاثنين — غموض: هل المبيعات حيث حدثت أم حيث جهّزت؟).
19. **[موثق] N C KOT في مبيعات يدوية**: "It can be Standard KOT or **N C KOT**" (COP ص10) — غير محصَّل يدوياً يمر بقناة القيمة نفسها — أثره في NC Query.
20. **[موثق] Value Transfer بلا أصناف**: "you have to enter the **Value** under the Value column" (COP ص14) — نقل رقم بين مراكز بلا أثر صنفي/كمي (نظافة تقارير الأصناف مقابل مراكز التكلفة!).
21. **[موثق] To Cost يُرصد آلياً**: "The To Cost will reflect the same option" (COP ص14) — تحويل بين نوعين مختلفين يبدو غير مدعوم من الواجهة (نمط واحد لكل قيد).
22. **[مستنتج] كمية تحويل > الرصيد**: لا تحقق رصيد موثق للتحويلات البينية (مقابل حاجب KOT!).

## هـ) الطلب الآلي والحدود العابرة

23. **[موثق] Auto Indent خطأ**: "Once the indent is generated, **it will not be allowed to modify or delete**" (COP ص19) — الخطأ خالد؛ هل indent جديد يعوّض؟ (غير موثق — GAP-FB-P03).
24. **[موثق] KOT block لحظي (SWITCH 511=0)**: "Items cannot be sold, if the quantity is greater than the current stock" (COP ص3) — منتصف إعداد طعام بوفيه والصنف ينتهي: **رفض كبس KOT** — سلوك POS عند الرفض (رسالة؟ بديل؟) غير موثق في أي من الدليلين (UNK-063) — أخطر حالة حدية تشغيلية.
25. **[مستنتج] جرد أثناء INI#368 Online**: استخراج يدوي متزامن مع تدفق لحظي — تكرار/ازدواج؟ غير موثق.

## و) التقارير والاستعلامات

26. **[موثق] تناقض تسمية Standard/Actual**: LUK ص12 "Standard Cost (Consumption) and Actual Cost (Recipe)" مقابل REP ص22 "**Standard consumption is based on recipe details. Actual is arrived based on consumption at cost centers**" — الأقواس تعكس المتن (C-FB-01 مسجل).
27. **[موثق] نهاية التنقيب معلنة**: "No Drill Down Available for this Category" (LUK ص15) — سلوك نظيف موثق.
28. **[موثق] XOR الربحية**: Issue Based بلا Restaurant وRecipe Based بلا Kitchen (LUK ص14) — طلب تحليل "جميع المطابخ وصفياً" مستحيل من الواجهة (لا يمكن: Recipe+Restaurant معاً).

---

## شرِكات الهروب وقيمها الخارقة (مقارنة عائلية)

| الوحدة | الشرِكة | الدلالة |
|---|---|---|
| TEL | 9999999999 (9 تسعات ×3) | أعلى تعرفة للمجهول |
| MNT | 999999999999 (12 تسعة) | صنف مفتوح بلا أثر مخزني |
| **FNB** | — | **لا شرِكة واحدة!** أول وحدة مخزنية-تحليلية بلا قيمة هروب — الاكتمال يأتي من Missing Recipe List/الربط اليدوي بدل الأكواد السحرية |

## عائلات الأنماط الحاضرة/الغائبة

- **حاضرة**: Lookup-as-Editor (ثالث وحدة) · اللون حالة (ثالثة) · خلود وثيقة (Auto Indent مع MEM Post/TEL slabs) · XOR قيود (جديدة كلياً!) · Preview→Generate (تقريرية).
- **غائبة**: لا إصدارية زمنية (لا Applicable From — أول ماستر مشروع بلا عائلة خلود زمني!) · لا ترقيم آلي موثق · لا Authorizer pairs · لا رسائل رفض — **خمس غيابات عائلية دفعة واحدة** (أكبر "عجز عائلي" في وحدة واحدة حتى الآن).
