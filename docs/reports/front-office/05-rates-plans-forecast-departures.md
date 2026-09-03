# 05 — عائلة الأسعار والخطط والتوقعات والمغادرة (REP §51–71)

> ~21 تقريراً: من إشغال الخطط إلى إحصاءات الإشغال الإلزامية ودورة المغادرة — قلب Revenue Management في طبقة التقارير.

---

## 1. الأسعار والخطط (51–64)

| # | التقرير | الخصوصية الموثقة |
|---|---|---|
| 51 | **Room Plan Report** | إشغال بحسب الخطة لليوم/خطة · الخطة: "**American plan/Continental Plan or All**" · "≥ accounting date" |
| 52 | **Plan Forecast Report** | "expected number of guests who may reserve rooms... room plan wise and further **PAX count wise**" · **القاعدة: "the date range cannot exceed more than 30 days"** · Detailed/Summary · **All أو خطط محددة** · مفتاح الرموز الحرفي: "**AP – American Plan, BB – Bed and Beverages, EP – European Plan, MAP – Modified American Plan, Adt – Adult and Chd – Child**" + وضع Guest Details |
| 54 | **Room Rate for the Day** | "total rates charged... The room rates include **extra bed charges, room plan charges, the tariff rates plus the luxury taxes (LTX)**" · **قيد توليد: "can be generated only once the Tariff is posted for the day"** · ملخص: In-House Rooms/In-House PAX/Checked Out Rooms/Checked Out PAX · **Include Total** ("If this option is not checked, the totals appear only at the end") |
| 55 | **Room Wise Bill Report** | "tariff, taxes and other services... till the accounting date" |
| 56 | **Hurdle Authorization Report** | **تعريف حرفي كامل**: "Every Property sets a **minimum room rate depending on the room types, below which, a room cannot be booked**... **All the units and the central office need to follow these standard rates** on a daily basis" + المثال: "minimum rate for a Deluxe room will be Rs. 2000/-, for a Standard room the rate will be Rs. 1000/-" · Property + فترة "≤ accounting date" — **Hurdle Rate موثقة بالاسم!** |
| 57 | **Rate Posted for the Day** | "same as Room Rate For The Day Report, **but the only difference is that this report can be generated without the Tariff being posted**" + **Print Mar.Seg & Bus.Sor** ("Market Segment and Business Source") — نسخة ما قبل الترحيل |
| 58 | **IT Report** | → `03-security-statutory-reports.md` |
| 59 | **TA Commission** | عمولات وكلاء السفر · **Include In-house Guests** · "≤ current date" · F1 Company |
| 60 | **RM Type/Plan Change Report** | تغييرات النوع/الخطة · "≥ accounting date" · Room Type Wise / Plan Code Wise |
| 61 | **FNB Plan for the Day** | "standard Food & Beverage (FNB) meal plan charges for all the rooms occupied" + "plan posted for the day along with the total amount charged" |
| 63 | **Plan Bifurcation Report** | "room wise plans for food, beverages, the amount and the taxes that are posted for the day. This is done **after the tariff is posted**" |
| 64 | **Print Hotel Chart** | "list of rooms available for the selected property and the date range" · "≥ accounting date" |

## 2. التوقعات (65.x — "This option gives 4 different forecast Reports")

المقدمة الرسمية: "These reports help the **marketing department and the management** to make critical strategic plans for the property." — (TOC يعرض 3 فقط؛ الرابع غائب → UNK-078).

| # | التقرير | الخصوصية |
|---|---|---|
| 65.2 | **Forecast Breakup** | فترة مستقبلية "more than the accounting date" · **Process A.R.R** checkbox · **Include Complimentary/House Guest in ARR** |
| 65.3 | **Detailed Forecast (ARR)** | "expected arrivals, room type wise totals and **stay over** details" · Include Comp/HG in ARR |
| 65.4 | **Projected Guest Stay** | "projection of number of guests that are expected to stay" + "the expected departure date etc." · **More Details** · Property |

## 3. إحصاءات الإشغال (66–67)

| # | التقرير | الخصوصية |
|---|---|---|
| 66 | **Occupancy Statistics** | **"This mandatory report gives all the occupancy details and the tariff rates for in-house and checkout guests"** — الوصف الوحيد بكلمة mandatory في الحزمة! · خيارات: **132 Column** · Include Complimentary/House Guest **in Summary** · Include Special Room |
| 67 | **Occupancy Analysis** | "daily room sales with room type breakup with **Month-to-date** statistics" · إدراج Complimentary / House Guest |

## 4. المغادرة (68.x + 69)

| # | التقرير | الخصوصية |
|---|---|---|
| 68.1 | **Checkout for the day** | "≤ accounting date" · **Print Bookers Code only / Include Address / Include Pax Checkouts / Include Print Only Day Use Rooms** |
| 68.2 | **Expected Departures** | "≥ accounting date" · Print by: **Departure Time Wise / Room # Wise / Guest Name Wise** · Include Spl. Rooms · **Group/FIT Breakup** |
| 68.3 | **Early Departures** | "checked out from the property **earlier than the departure date they had given**" · "≤ accounting date" |
| 68.4 | **Departure Slip** | قسيمة مغادرة تُسلّم للضيف "at the time of their Checkout" · Room# lookup (نقر مزدوج كاختيار) |
| 69 | **Group Wise Checkout** | "≤ server date and **within the same month**" — يذكر server date لا accounting date (استثناء لفظي!) |
| 71 | **Arrivals (Date Range)** | "≤ server date" · تجميع: **group by Arrival Date / Company / Market Segment** — بالخيار الثالث: "Click All or select desired market segment options" |

## 5. الوصول عبر فترات (71 + Tourist 70)

- **Tourist Arrivals (70)**: شهري/سنوي بتصنيف مغلق ("system defined") — انظر ملف الأمن §2.
- **71** يوفر ثلاث زوايا تجميع لذات البيانات (تاريخ/شركة/قطاع سوق) — نمط Group-By قابل للنقل الحرفي إلى ERPNext query.

## 6. القرارات المعمارية

1. **ثلاثية تعتمد الترحيل**: 54 (بعد الترحيل فقط) · 63 (بعد الترحيل) · 57 (قبله) — التقرير يعرف موضعه من دورة Night Audit؛ أي تنفيذ: Report.availability ⊨ tariff_posted.
2. **Hurdle Rate بالاسم والوحدة المؤسسية**: 56 يوثق أن الحد الأدنى "follow"-إلزامي لكل الوحدات والمكتب المركزي — بنية Chain-level Pricing Governance (وليست قرار موضعي) — عنصر يجب أن يعلو لطبقة Domain (Pricing Policy).
3. **حد 30 يوماً للتوقع**: قيد نافذة توقع الموارد (52) مقابل 10/31 يوم في Mat./Forecast (131/132) — ثلاث عتبات زمنية مختلفة لثلاث عائلات توقع.
4. **LTX كرمز ضريبي**: 54 يذكر Luxury Tax ب اختصار **LTX** داخل مكونات السعر — يضاف لقاموس الرموز (AP/BB/EP/MAP/Adt/Chd/ADQ/ADC/ADV/POT/LTX).
5. **الدقة اللفظية للساعة**: 68.2 يفرز حسب **وقت المغادرة** — بيانات Departure Time متاحة في مستوى الاستعلام (مقابل SMS Checkouts الذي يرسل "one hour prior").
