# 18 — معايير القبول (Acceptance Criteria) — وحدة FXD

> **9 مجموعات / 44 معياراً + Smoke Test من 22 خطوة** — التركيز على: البوابة الأحادية property-wise · الكود 12=5+3+4 · تماثل الربط الرباعي · الترحيل الشهري بأربع قواعد صلبة (شهر/نهاية شهر/SLM/SubGroup) · أرجل قيود البيع الثلاثة وتعطيل التساوي · معادلات قابلة للاختبار الرقمي بأمثلة الدليل الأصلية (£10,000→£800 و40% WDV).

---

## المجموعات

### AC-01: البوابة والهرمية (5)
1. Start Date تُحفظ مرة لكل Property؛ أي تعديل لاحق **يُرفض** برسالة.
2. أي معاملة بتاريخ ≤ Start Date تُرفض (حاجز BR-FX-02/V-FX-11).
3. Main Group code غير قابل للتعديل بعد الإنشاء؛ Long/Short ≤ 30/10.
4. Location/Component ماسترات مستقلة تعمل قبل أي Sub Group (ترتيب حر لكن الكود يركّب الموجود فقط).
5. Dep Method تُحفظ **بنسبتين معاً** (SLM% + WDM%) لكل (Property×FY×SubGroup/Asset).

### AC-02: الكود الآلي (4)
6. Asset code يُولَّد 12 محرفاً: أول 5 = SubGroup، التالي 3 = Location، الأخيرة 4 = مسلسل.
7. مسلسل مستقل لكل توليفة (SubGroup×Location): A×L=0001 وB×L=0001 كلاهما صحيح.
8. Sub Group code يقبل 5 محارف فقط (رفض السادس).
9. لا إدخال يدوي للكود ممكن أصلاً.

### AC-03: الربط الرباعي (5)
10. حفظ Sub Group بحساب واحد مربوط (BS بلا PL مثلاً) **يُرفض** — "must be mandatorily linked".
11. حساب نوع 'sub ledger' يعرض اختيار Sub Ledger (العمق الثنائي).
12. Sub Group غير مربوط يُقبل حفظه (اختيارية الربط) لكن أصوله تُبرز **أزرق** في FI Posting وتُستثنى من الترحيل.
13. Cost Center يُخزن مع الربط ويظهر في القيود.
14. تقرير/عرض يوفر قائمة Sub Groups غير المربوطة (بديل تقريري للأزرق — GAP-FX-P03).

### AC-04: الماستر المركزي (6)
15. Total Value = Quantity × Item Price يُحسب آلياً عند تغيير أي طرف.
16. Date installation > server date يُرفض.
17. العملة الافتراضية محلية والسعر يُحمَّل آلياً بالعامل.
18. Depn. Op. Bal يُقبل فقط عند start date depn < FA Start Date (وإلا يُحجب/يُصفَّر).
19. شبكة Tax تُفتح بdouble-click وتخزن (TaxCode, Currency, Amount) — ضمن القيمة.
20. شبكة Component تخزن سطوراً **خارج** قيمة الأصل، وCurrent closing تعرض (Qty balance, NBV, Total Depn) آلياً.

### AC-05: الحساب والمنهجين (6) — أمثلة الدليل الرقمية
21. INI#475=SLM: أصل 10,000 بـfinal 2,000 عبر 10 فترات → **800/فترة** حرفياً (مثال الدليل).
22. INI#475=WDV: 75,000 بـ40% → التسلسل **30,000/18,000/10,800/6,480/3,888** حرفياً (مثال الدليل).
23. Residual Value يُخصم من قاعدة SLM (نمط final value).
24. Rollback يسترجع حساب الشهر/الفترة **مع معكوس أي قيد مرسل** (GAP-FX-D03 — معيار الصفر المسموح).
25. تبديل INI#475 بعد أول ترحيل **يُمنع** (قرار D-FX حسم UNK-073).
26. Last Dep. Calc Date تتقدم بعد كل حساب ناجح، وLast Dep. **Post** Date تتقدم بعد كل ترحيل فقط (التمييز محفوظ).

### AC-06: الترحيل الشهري (6) — القواعد الأربع الصلبة
27. قيود FI Posting تُنشأ **شهرياً** وبـposting date = **اليوم الأخير من الشهر**.
28. القيد **SLM فقط** — حتى لو كان الحساب WDV (اختبار مزدوج المنهج).
29. التجميع/الترحيل **Sub group wise** حتى لو العرض asset-wise.
30. كل قيد يلمس حسابي المجموعة: **Debit PL Depr / Credit BS Depr** (الربط الرباعي يعمل).
31. غير المربوط لا يولّد قيداً ويُبرز أزرق عند Load.
32. (Property × MMYY) لا تُرحَّل مرتين — منع ازدواج (سلوك الذاكرة Post Date).

### AC-07: البيع/الاستبعاد (7)
33. Type افتراضي Sale؛ Disposal مسار موازٍ.
34. Quantity > Balance Quantity يُرفض (الجزئية متاحة بالحد).
35. Local Amount = Sale × Rate وAsset Value = Qty × Item Price آليان.
36. Gain/Loss يتحدد بالاتجاه ويعرض قبل الحفظ.
37. أرجل القيد: Asset ledger + **Cash/Bank حسب PayMode** + P&L (Gain Credit / Loss Debit).
38. **التساوي حرفياً (الاختبار الحاسم):** Sale = Asset Value → لا سطر P&L أصلاً (الحقل معطَّل — E-FX-02).
39. بطاقة الائتمان: PayMode الحالي Bank/Cash فقط (GAP موثق — لا اختبار فشل).

### AC-08: المكوّنات (2)
40. Component Entry يزيد قيمة الأصل المضافة إليه (يظهر في Current closing/تقرير List).
41. مكوّن بعملة أجنبية: Rate آلي وExchange amount = Amount × Rate (يمين الشاشة).

### AC-09: التقارير والاستعلامات (3)
42. Fixed Asset List يتيح الثلاثية Asset/SubGroup/Location By + **Zero Quantity checkbox** مع أصول مستنفدة.
43. Dep Details (Q) بمدى FY يعمل **بلا Property** (السلوك الموثق) والتقارير كلها عبر F3.
44. Asset Sales Register يفصل Sales/Disposal بخيار صريح؛ وAsset Ledger يعرض "Actual Asset value as on date".

## Smoke Test (22 خطوة)

```
1.  حفظ Start Date (P1, 012026) → محاولة تعديل → رفض ✓(AC1)
2.  Main Group MV (Movable) + Location K01 + Component INSTL
3.  Sub Group MV001 مربوط (BS,BS-SL,PL,PL-SL,CC) → حفظ ✓
4.  Sub Group MV002 بحساب واحد → رفض ✓(AC3)
5.  Sub Group MV003 بلا ربط → حفظ ✓
6.  Dep Method: FY2026 — MV001: SLM 10% / WDV 40%
7.  أصل: MV001+K01 → كود MV001K010001 آلي ✓(AC2)
    Qty=1, Price=10,000, Residual=2,000, Life=120 شهر
8.  أصل ثانٍ: MV003+K01 → MV003K010001 (غير مربوط)
9.  Calculate Dep (12 شهراً): 800/شهر ×12 (SLM بFlag=SLM) ✓(AC5-21)
10. FI Posting 012026 → Load: MV001 ✓ / MV003 أزرق ✓
11. Save → قيد 31-01-2026: Dr PL / Cr BS بمبلغ MV001 فقط ✓(AC6)
12. إعادة Save لنفس الشهر → لا قيد جديد ✓(AC6-32)
13. Component Entry (نقل 500) → قيمة الأصل 10,500 (Display) ✓(AC8)
14. Calculate 022026 → FI Posting 28-02-2026 ✓
15. Rollback 022026 → الحساب يُلغى + قيد معكوس ✓(AC5-24)
16. بيع نصف كمية أصل ثالث (Qty 2 من 4) → Balance=2 ✓(AC7-34)
17. بيع 2,600 مقابل Asset Value 2,000 → Gain 600 يظهر ✓(AC7-36)
18. حفظ البيع → قيد 3 أرجل (Bank 2,600 / Asset 2,000 / P&L Gain 600) ✓(AC7-37)
19. بيع أصل رابع بمبلغ = قيمته بالضبط → P&L معطل + قيد سطرين ✓(AC7-38)
20. Disposal لأصل خامس → مسار Scrap ✓(AC7-33)
21. Fixed Asset List + Zero Quantity → المستنفد يظهر ✓(AC9-42)
22. Sales Register (Sales) + (Disposal) + Asset Ledger as-on ✓(AC9-44)
```
