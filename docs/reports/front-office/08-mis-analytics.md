# 08 — عائلة MIS والتحليل الإداري (REP §115–135)

> ~21 تقريراً استراتيجياً: مقارنات سنوية، مساهمات شركات، موازنات، وتقارير تُبنى دفعياً. عائلة "قرارات الإدارة" التي ذُكرت حرفياً: "These reports help the marketing department and the management to make critical strategic plans."

---

## 1. عائلة MIS الأساسية (115–119)

| # | التقرير | الخصوصية |
|---|---|---|
| 115 | **MIS Report / A** | Segments: "Nationality, Market Segment, Business Sources, Corporate etc." · **نطاق MM/YY بدء/انتهاء** (عبر الشهور والسنوات) · أنواع الضيوف: **Local Nationals / House Guest / Complimentary** · المقاييس: **PAX / ARR / Room Nights / ARP** |
| 116 | **MIS Report / B** | نفس الشرائح بتاريخ **As On** + "**Month to Date (MTD) and Year to Date (YTD)**" — بلا نطاق |
| 117 | **M.I.S (DMY) Format** | "Date, Month and Year ranges across Months and Years" — الشكل الممتد |
| 118 | **MIS Date Range Report** | "an intermediate period across Months and Years" · Segment من dropdown |
| 119 | **Nationality Report / C** | PAX/إشغال قومياً لشهر/سنة · استثناء LN/HG/Comp |

**تسمية البُعد الموحد**: Segments الثابتة عبر العائلة = **Nationality · Market Segment · Business Source · Corporate/Company** — أربعة محاور تحليل تظهر أيضاً في 120-122/124/127/130 — تُصهر في Dimension موحد عند التنفيذ.

## 2. مساهمات الشركات (120–121)

| # | التقرير | الخصوصية |
|---|---|---|
| 120 | **Company Contribution / C** | نطاق MM/YY · Comp/HG · **PAX / ARR / Room Count / ARP** · **Market Segment أو Business Source** ثم "select **all the segments** from the dropdown" — استيعاب كامل للشريحة |
| 121 | **Company Contribution / D** | نفس 120 لكن **As On + MTD/YTD** — نسخة لحظية |

## 3. الإحصاءات والمقارنات (122–125)

| # | التقرير | الخصوصية |
|---|---|---|
| 122 | **Hotel Statistics** | "occupancy statistics with option to view Business Source wise or Market Segment wise occupancy with **ARR, ARP and other room type wise analysis**" + "**arrivals and Hotel positions for the next 15 days**" — نافذة توقع 15 يوماً! · Day wise + MTD + YTD |
| 123 | **Room Sales** | مبيعات الغرف As On + Comp/HG |
| 124 | **Comparative Sales Analysis** | "**last year with the current year**" · المحور: **Room Type / Market Segment / Nationality / Business Source** · Comp/HG |
| 125 | **Budget Variance** | "budget figures **verses** actual figures" · **شرط مسبق: "the budgets should be defined using the FO budgets menu option"** · المحور: MarSeg/BusSrc/Nationality/Room Type · **Month/Year + Cur** (سعر الصرف آلي) |

## 4. التقارير المعرّفة من المستخدم (126–128 + 135)

| # | التقرير | الإعداد المطلوب | الخصوصية |
|---|---|---|---|
| 126 | **Managers Report** | SETUP MANAGER REPORTS (FO Setup) | "for the Current Year and for the Last Year (day wise, month wise and year wise)" · Report# (F1) + Report Date "≤ accounting date" · Include Comp & HG |
| 127 | **Comparative MIS Report** | COMPARATIVE MIS SPEC (FO Setup) | Report No. = "the one that you have assigned to the **Group**" · فترة "≤ accounting date" · House Guest/Complimentary ("to view the **revenue %** from this source") |
| 128 | **MIS Revenue Report** | **MIS Revenue Grouping + SETUP MIS REVENUE** (FO Setup) | Group dropdown + Report# · **Display revenues in Lakhs** — وحدة Lakhs الهندية (100 ألف)! · Include Comp & HG |
| 135 | **Manager Report Creation** | SETUP MANAGER REPORTS | **"Enter the date in the Creation Date field... Once you click OK, you get the **data processing message**... After the data processing is complete, click Exit"** + "Last processed date is also displayed by default" — **معالجة دفعية بحالة** |

**النمط ETL الدفعي**: 135 يجهّز بيانات 126 — الفصل بين التحضير والاستهلاك مع ذاكرة (Last processed date) — يقابله ERPNext Scheduled Report Generation + Materialized View.

## 5. التوقعات والإيرادات (129–134)

| # | التقرير | الخصوصية |
|---|---|---|
| 129 | **Revenue Report (Nation)** | "Nation wise" · "≤ accounting date" · Comp/HG |
| 130 | **Revenue Report (Market Segment)** | "similar to the Revenue (Nation) report" — النسخة القطاعية |
| 131 | **Mat. / Forecast Rev. Report** | "(Materialized / Forecast Reservation Report)" · **"the date difference... should be **maximum 10 days only**"** — أضيق نافذة في المشروع! |
| 132 | **Mat. / Forecast Room Report** | "Materialized and Forecast report of occupancy" · **≤ 31 days** |
| 133 | **Reservation Rate by Date** | "Reservation No., Guest Name and Reservation Status **along with the rates offered**" · Property · **Include Waitlist + Include Provisional** — الأسعار تشمل غير المؤكد! |
| 134 | **Group Revenue Report** | "revenue generated from a Group" · same month · **Detailed / By Day** |

## 6. القرارات المعمارية MIS

1. **Lakhs كوحدة عرض** (128): الطبقة التحليلية تقدم Scaling Indien (Lakh = 10⁵) — يضاف لقرارات العرض (In Thousands 106) — أي reproduction عربي يحتاج Unit-of-display pluggable.
2. **Materialized كمصطلح رسمي** (131/132): "Materialized / Forecast" — الدليل يميز المحقق عن المتوقع بالاسم — مقابل ERPNext Forecast/Actual.
3. **نوافذ التوقع المتدرجة**: 10 أيام (131) · 15 يوماً (122) · 30 يوماً (52) · 31 يوماً (132) — أربع عتبات لأربع أغراض (إيراد حجز فوري / موقف تشغيلي / خطة طعام / إشغال).
4. **Revenue % من Comp/HG** (127): فلسفة تقرير مقارن يعرض حصة الإشغال المجاني من الإيراد — مقياس تكلفة الضيافة الداخلية.
5. **المعالجة الدفعية بآخر تاريخ معالجة** (135): تحسب قابلية الاختبار: تشغيل Creation بتاريخ ثم توليد Report — تسلسل التبعية الموثق أثمن مخرجات هذه العائلة لخطة الترحيل.
6. **Private Reporting Layer**: كل من 126/127/128/135 + 104/106 يتطلب تعريفات Setup — خمس "أدوات إبلاغ شخصية" تجعل FO Reporting Layer قابلاً للتخصيص دون كود — يقابلها ERPNext: Report Builder + Dashboard Charts + Query Reports.
