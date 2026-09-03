# 11 — تحويل طبقة تقارير POS إلى ERPNext + فجوات (Phase 7)

> Mapping + Gaps لطبقة تقارير POS (~57 تقريراً فريداً). مرجع الوحدة الأم: `docs/modules/point-of-sale/16-erpnext-mapping.md`.

---

## 1. جدول التحويل F-PR-1..15

| # | عنصر FN6i | مقابل ERPNext | القرار |
|---|---|---|---|
| F-PR-1 | **محرك الإخراج الرباعي + Port ID** | Query/Script Report + Print Format + Download (XLSX/CSV/PDF) + Printer Settings | Display/Spool/Print/Export = 1:1؛ Port ID → اختيار الطابعة في Print Dialog (إغلاق خامسة POS الخاصة) |
| F-PR-2 | **مصفوفة POS Report Options** (Void/Comp لكل تقرير) | Report Options (Custom Fields على تقرير/إعداد المستخدم) | **Config-per-Report** يُنقل كإعدادات عرض محفوظة — مع Invariant: عرض بلا إجمالي (AC-PR-04) |
| F-PR-3 | **عائلة المبيعات 1.1–1.16** | دمج التوائم: Daybook×2 → تقرير بوضعين · Summary×2 → تقرير بوضعين · Sales By Item/Group/Server/Table → Query Reports | ~9 تقارير حقيقية بعد الدمج (16 → 9) |
| F-PR-4 | **DS Report (1.6)** | **Dashboard يومي + Script Report**: 8 أعمدة × 11 مقياساً + APT/APC + عمود توقع الشهر | صيغ حرفية قابلة للاختبار (AC-PR-02) + DSR Session Group → Grouping إعداد |
| F-PR-5 | **F&B Menu Engineering (22)** | **Script Report فوق POS Invoice + Item**: Menu Mix% + CM (من Item Valuation/Recipe) + تصنيف STAR/PUZZLE/PLOW HORSE/DOG + Profit Factor | التاج: أصل واحد عالي القيمة؛ F&B Factor → إعداد (Feature Flag بدل INI 335)؛ Cost% من Recipe FNB إن وُجدت وإلا نسبة الصنف |
| F-PR-6 | **Popularity ×2 + Order Analysis (13/14/15)** | Query Reports بفلاتر (Cut Off · Time Slots · start/close) | Cut Off ≤ 9999 كفلتر رقمي + نسب Grand/Group |
| F-PR-7 | **Tax Register (16.1/16.2)** | Pivot على Sales Invoice taxes (أعمدة من Item Tax Template/نسب) | التوليد الديناميكي للأعمدة من نسب الضرائب — Script Report |
| F-PR-8 | **PAN (9, Switch 137)** | Custom Field PAN على POS Invoice **إلزامي شرطي** فوق عتبة إعداد + تقرير امتثال | عتبة "prescribed limit" → إعداد نقدي (إغلاق UNK-085)؛ الهند فقط → Feature Flag جغرافي |
| F-PR-9 | **KOT Audit + Bill Audit (17.2/17.5)** | Version History للتعديلات + **إعادة تسوية = فاتورة تسوية عكسية + جديدة** (amended) مع أثر mode old→new | أغنى نمو Versioning: سبب الحذف + old/new + المسؤول — يُنقل كأصل تدقيقي |
| F-PR-10 | **Cashier/Shift (5.2/5.4) + Z-Report** | **POS Shift Closing** (تقرير Z) مغلق على الوردية + نطاق أرقام الفواتير | "Closed Shifts only" = بوابة إغلاق (AC-PR-05)؛ start/end bill numbers = تدقيق تسلسل |
| F-PR-11 | **Re-print POS Bill (10)** | إعادة طباعة Print Format (Preview ثم Print) + **سجل إعادة طباعة** (مدقّق من 17.5) | وضع Month&Year للحالات المنسية → فلتر بحث مرن (يُتفوق عليه ببحث حر) |
| F-PR-12 | **Loyalty (8)** | تقرير Loyalty Program Entry (بطاقة واحدة = كشف حامل) | يقابل mapping POS-GST للولاء — لا محرك نقاط (نفس فجوة الوحدة الأم) |
| F-PR-13 | **Delivery (7.x)** | DocType طلب توصيل (Customer مولد آلياً + Area) + تقريرا Frequency/Sales | Area → Custom Field؛ Customer Id آلي = التسلسل القياسي |
| F-PR-14 | **NC (11.x) + Discount (6.x/12)** | Complimentary Invoice + تقرير Discount (Reason/Cashier/Mode) + سلسلة الخصم الرباعية | NC بأثر قسم → Cost Center على السطر المجاني؛ مسؤول السماح → حقل authorized_by |
| F-PR-15 | **KDS (24 — شبح)** | **KOT Display (شاشة مطبخ Realtime)** — [INFERENCE] | بلا جسم أصلي — يُبنى عند الحاجة ويُسجل §24 كدليل قصد تطويري (UNK-083) |

**التقدير الإجمالي**: ≈ **7-9 أصول مخصصة / 5-6 أسابيع** — أثقل من FNB-REP (تحليلي بحت) وأخف من FO-REP (SMS + Materialized)؛ الأصول الكبيرة: Menu Engineering (F-PR-5) + التدقيق الثنائي (F-PR-9) + Z-Report (F-PR-10).

## 2. فجوات GAP-PR-*

### فجوات تصميم (D)

| ID | الفجوة | الأثر | الشاهد |
|---|---|---|---|
| GAP-PR-D01 | **صلاحيات صفرية على ~57 تقريراً** (بما فيها ضرائب وتدقيق فواتير!) — امتداد عائلة "REP بلا صلاحيات" (10/17 بعد FO) | reproduction يفرض Report Permission Matrix | REP كله |
| GAP-PR-D02 | **عائلة same-month (~25 تقريراً)**: حبس أرشيفي يمنع النطاق العابر | يُهجر — نطاق حر مع defaults | مصفوفة §2.1 |
| GAP-PR-D03 | **80/132 بدلالة معكوسة عن FO** (POS تضيف · FO تحذف YTD) | عدم اتساق عابر للوحدات في نفس العائلة — يُوحد العرض | 14/23 vs FO 102 |
| GAP-PR-D04 | **KDS §24 شبح** — قسم بلا جسم يغلق الملف | طبقة KOT-Display غير محددة | ص157-158 |
| GAP-PR-D05 | **Discount Register مزدوج** (C-POS-01) + كتلة §6 خارج الترتيب الفيزيائي | التباس كتالوغي — يُحسم بدمج §12←§6.1 | ص96-105 |
| GAP-PR-D06 | **Export بلا صيغة** (امتداد UNK-081) | قناة رابعة غير موصوفة | 1.15/1.16/7.1 |
| GAP-PR-D07 | **KOT Books ورقية** تدار كأصل (issued to/date/used-void) مقابل KDS رقمي غير موثق | فجوة نموذج: الورق لا مقابل رقمياً له | 17.1 |

### فجوات تشغيل (P)

| ID | الفجوة | الأثر |
|---|---|---|
| GAP-PR-P01 | **قيمة عتبة PAN غير موثقة** (Switch 137) | قرار إعداد نقدي عند التنفيذ |
| GAP-PR-P02 | **F&B Factor % الافتراضي غير موثق** (Switch 335 — المثال 70%) | يحدد مباشرة تصنيف MM Class (نسبة STAR/DOG تتغير به!) |
| GAP-PR-P03 | **Time Slots يدوية غير محفوظة** (14) — لا ماستر شرائح | إعادة إدخال كل تشغيل؛ يُستبدل بماستر شرائح زمنية |
| GAP-PR-P04 | **Discount % (§12) بلا نطاق موثق** (سالب؟ >100؟) | تحقق رقمي غائب |
| GAP-PR-P05 | **إصدار دفاتر KOT يدوي** (17.1 يعرض فقط) — لا شاشة إصدار موثقة في REP | دورة حياة الدفتر مبتورة العضو التشغيلي |

## 3. مجهولات جديدة (UNK-083..088) — تُسجل في unknowns.md

| ID | السؤال | الأثر | المصدر |
|---|---|---|---|
| UNK-083 | **KDS REPORT (§24)**: عنوان بلا متن — KDS=Kitchen Display System؟ شاشاته؟ علاقته بـTouch Screen؟ | أول شبح يُغلق به ملف (ورقي→رقمي مبتور) | TOC + ص157-158 |
| UNK-084 | **مصفوفة POS Report Options**: القائمة الكاملة للتقارير القابلة للضبط (~20 مذكورة من 57؟) + خيارات غير Void/Comp؟ | نطاق طبقة الإعداد الخفية | ~20 موضعاً في REP |
| UNK-085 | **Switch 137 — قيمة العتبة** المالية لطلب PAN | امتثال هندي — قرار إعداد | §9 |
| UNK-086 | **Switch 335 — قيمة F&B Factor الافتراضية** (70% مثالاً؟) | يقلب تصنيف MM/Item Class | §22 |
| UNK-087 | **Discount Register المزدوج** (6.1/12): تقريران مختلفان أم نسختان؟ أيهما المعتمد؟ | كتالوغ + دمج | §6.1/§12 |
| UNK-088 | **Time Slots (14)**: مصدر التعريف (يدوي كل مرة؟ ماستر؟) + سقف عددها | قابلية التشغيل المتكرر | §14 |

## 4. تناقضات جديدة (C-POS-01..03) — تُسجل في contradictions.md

- **C-POS-01**: Discount Register موثق **مرتين** (§6.1 ص96 و§12 ص103) بمعايير مختلفة + كتلة §6 كلها واقعة فيزيائياً بعد §11 — يُعتمد §12 (الأغنى) مع دمج مرشح §6.1.
- **C-POS-02**: ملاحظة SETUP في Discount Summary (6.2) تُحيل إلى **"Sales By Item"** — خطأ نسخ/لصق.
- **C-POS-03**: Menu List (18) — الخطوة 3 مكررة حرفياً مرتين (ص144).

> (ملاحظة دون مستوى التناقض: جدول DS يستخدم BREAKFAST وخلاصة الأعمدة "Morning" — انحراف تسمية موثق في `02` §3.)

## 5. معايير قبول (AC — عينة قابلة للتوسيع)

1. **AC-PR-01** (Menu Engineering — مثال الدليل حرفياً): Total Menu CM=2000, Qty=20 → العتبة 100؛ Item CM=120 → **HIGH** · Item CM=90 → **LOW**.
2. **AC-PR-02** (MM Class حرفياً): 10 أصناف, Factor=70% → العتبة (100/10)×0.7 = **7**؛ Menu Mix=10 → HIGH · =5 → LOW.
3. **AC-PR-03** (Profit Factor): MenuCM=80, Total=500, Items=10 → 500/10=50 → **1.6**.
4. **AC-PR-04** (Invariant Void/Comp): فاتورة 974(V) تظهر بالتفاصيل والإجمالي الكلي **لا يتغير**.
5. **AC-PR-05** (بوابة الوردية): Cashier Summary يرفض وردية **مفتوحة** (Closed only).
6. **AC-PR-06** (نافذة 7): Weekly Manager يرفض 8 أيام.
7. **AC-PR-07** (نافذة 30): Shop Sales يرفض 31 يوماً.
8. **AC-PR-08** (المستقبل الوحيد): Happy Hours يقبل From > اليوم؛ كل عائلة same-month ترفضه.
9. **AC-PR-09** (132 المضيف): Cover Analysis بوضع 132 يعرض نوع "Others" + عمود Total؛ NC Outlet Summary بـ8 منافذ يجبر 132.
10. **AC-PR-10** (Bill Audit): إعادة تسوية Cash 500 → Card 500 تعرض **الوضعين والمبلغين معاً**.
11. **AC-PR-11** (Pivot الضرائب): VAT بنسبتي 10/12 → عمودان + عمود إجمالي.
12. **AC-PR-12** (KOT Audit): تعديل كمية 2→3 يعرض status "old 2 / new 3"؛ حذف يعرض السبب.
13. **AC-PR-13** (Cut Off): 9999 مقبول · 10000 مرفوض.
14. **AC-PR-14** (التسلسل): Time Slot أصغر من سابقه → رفض؛ خانة فارغة → رفض.
15. **AC-PR-15** (DS تنبؤ): MTD=31000 بتاريخ 5 يناير → "Where are we headed" = **5000**.

## 6. Smoke Test (خطة 20 خطوة لطبقة تقارير POS)

1. فاتورة Void مفعّلة في POS Report Options → Sales Daybook يعرض 974(V) بلا دخول الإجمالي (AC-04).
2. إغلاق AC-04: تعطيل الخيار في المصفوفة → الفاتورة تختفي كلياً.
3. DS Report قبل تعريف DSR Session Group → لا يعمل؛ بعد التعريف → 8 أعمدة (AC-15 لاحقاً).
4. DS بأسبوع يبدأ Monday بتاريخ الأربعاء → WTD = 3 أيام حرفياً.
5. Weekly Manager بنطاق 8 أيام → رفض (AC-06).
6. Sales By Group بـ9 منافذ → رفض المعالجة (حد 8).
7. Tax Register (VAT 10+12) Bill-wise → عمودان+إجمالي (AC-11).
8. Non-Taxable Turnover وضع City Ledger → فواتير المدين فقط + تعريف AR في التوثيق.
9. Tax Exemption بإعفاء VAT → فاتورة الإعفاء بمبلغ الإعفاء لكل ضريبة.
10. Print PAN بعد تجاوز عتبة Switch 137 → تقرير الاسم/العنوان/PAN (AC جغرافي: الهند فقط).
11. Settlement by Bill# وضع Cancelled → الفاتورة الملغاة + رقم البديلة + المستخدم.
12. إعادة تسوية فاتورة (Cash→Card) → Bill Audit/Re Settled يعرض old/new (AC-10).
13. إعادة طباعة فاتورة (Month&Year mode) → تظهر في Re Printed بتاريخ ووقت (ثنائية 10+17.5).
14. KOT: تعديل كمية صنف 2→3 → KOT Audit بثنائية old/new (AC-12)؛ حذف صنف بسبب → delete+reason.
15. KOTs by Bill لفاتورة بـ3 KOTs → عرض أفقي ثلاثي.
16. Cashier Summary على وردية مفتوحة → رفض (AC-05)؛ بعد الإغلاق → تقرير بنطاق أرقام الفواتير (من 5.4).
17. Foreign Exchange بعملة USD → كشف بسعر الصرف وفرق الصرف (5.2).
18. Tips Statement + Server Summary → البقشيش بوضع الاستلام.
19. Menu Engineering ببيانات المثال (CM 120/90 · Mix 10/5 · Factor 70) → HIGH/LOW ثم STAR/PUZZLE/PLOW HORSE/DOG + Profit Factor 1.6 (AC-01/02/03).
20. Cover Analysis 80→4 أنواع ثم 132→5+Total (AC-09) · NC Outlet بـ8 منافذ → 132 إجباري.
