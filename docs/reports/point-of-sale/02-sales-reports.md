# 02 — تقارير المبيعات (§1.1–1.16 + §13/14/15)

> عائلة المبيعات: 16 تقريراً مرقماً (أكبر عائلة فرعية في الحزمة) + تحليلات Popularity/Order المرتبطة موضوعياً. مرجع أرقام المتن محفوظ للرجوع.

---

## 1. جرد العائلة

| # | التقرير | المدخل المميز | المخرجات المميزة |
|---|---|---|---|
| 1.1 | **Sales By Item** | Normal/Happy Hour/Both · Start/Ending Item (من Menu Master) · Session · Print Day Total | إجماليات Qty/Rate/Value لكل صنف + إجماليات المجموعات/الأنواع/المنافذ |
| 1.2 | **Sales Daybook** | Date واحدة · Skip Page | أرقام الفواتير + مبالغها لكل جلسة/منفذ + تفكيك نوع القائمة + علامات **(V)/(C)** — مثال: 974(V) |
| 1.3 | **Daily Sales Report** | Date + Outlets + Session | لكل فاتورة: Detail+Summary · ضرائب · تسوية · Covers · PaidOut · Tips — **أغنى تقرير يومي** |
| 1.4 | **Sales By Group** | **حد 8 منافذ** ("Maximum 8 outlets can be processed and printed at a time") · Include NC KOTs/Void/Compl. | مبيعات كل مجموعة (Qty+Value) + إجماليات المنافذ |
| 1.5 | **Summary By Item** | **Port ID** (طابعة!) · Print Item Value | أصناف كل مجموعة + الإجمالي |
| 1.6 | **DS Report** | Option: By Group/By Menu Type · **Week Beginning dropdown** · YTD checkbox | مصفوفة 8×11 Amount+% + عمود التنبؤ العامي (انظر §3) |
| 1.7 | **Sales Daybook by Date** | نطاق تاريخ (نفس الشهر) | مبيعات كل نوع قائمة لكل تاريخ + خصم كل يوم |
| 1.8 | **Summary by Date** | نطاق + Incl. Void/Comp | ضرائب · cash vs credit (credit = "كل ما عدا النقد!") · Tips · ملخص ثلاثي |
| 1.9 | **Summary by Shift** | **Accounting date XOR Shift Date** · Consolidated XOR By Date | مبيعات كل نوع لكل وردية/يوم + أنماط التسوية الخمسة (cash/card/room/company/**others**) |
| 1.10 | **Weekly Manager Report** | **≤7 أيام** ("End date not greater than 7 days from the Start Date") | Gross/Net · taxable/non-taxable · خصومات · تسويات · ضرائب · Round Off · **"total income earned after making all the necessary deductions"** |
| 1.11 | **Sales by Server** | Server checkboxes · By Date/By Session | مبيعات كل نادل يومياً + كفاءة الأداء |
| 1.12 | **Sales by Table** | Table # أو All · Date XOR Session | Checks/Covers/Sales لكل طاولة + إجماليات الجلسات |
| 1.13 | **Shop Sales Report** | **≤30 يوماً** · Incl. Void/Comp | أصناف المتاجر (gift/flower/books/toys) بالمجموعات |
| 1.14 | **Modifier Sales** | نطاق + Void/Comp | Bill/KOT/Item/Modifier/Qty/Rate/Value + إجماليات يومية — "More spicy or less spicy sandwich, juice with less sugar" |
| 1.15 | **Sales by Open Item** | نطاق + 4 قنوات إخراج معلنة | الصنف المفتوح (خارج القائمة) + **User who has generated the KOT** |
| 1.16 | **User Defined Sales Report** | يستهلك **Sales Report Definition** (POS-SET §16) · Settlement Mode | أعمدة يختارها المستخدم (فواتير/جلسات/تسويات/خصم/ضريبة/بقشيش/ساعات سعيدة) |

## 2. الأنماط العابرة في العائلة

- **علامات الفواتير**: `(V)` Void و`(C)` Complimentary بجوار رقم الفاتورة — معجم عرض موحد (1.2 وأثره على 2).
- **تعريف Credit الحرفي** (1.6): "The settlement amount **other than Cash, Void, Complimentary and Non Chargeable**" — Credit = كل شيء ليس نقداً/إلغاءً/مجانيةً/NC (بما فيها بطاقة/شيك/غرفة/شركة).
- **تعريف others الحرفي** (1.9): "In 'others' column, all other settlement modes other than cash, credit card, room and company are covered" — قائمة مفتوحة ضمنية للأنماط المخصصة.
- **Tip المستثنى**: DS Report تحسب "Total Tip **other than the Complimentary bill tip** amount" — بقشيش المجانيات خارج المجموع.
- **YTD مشروط** (1.6): عمود YTD لا يظهر إلا بتحديد "Include YTD Sales" — "sales from the fiscal year to given date" مع مثال سنة يناينوية.

## 3. DS Report — التقرير الأم (1.6)

**البنية**: 8 أعمدة زمنية × 11 مقياساً، كل عمود ينشطر **Amount و%**:

| الأعمدة الزمنية | الحساب الحرفي (مثال 5 يناير 2011) |
|---|---|
| BREAKFAST/LUNCH/DINNER | مبيعات فئات DSR Session Group كما عُرّفت في SETUP (الجلسات تُجمع في الفئات الثلاث) |
| FOR THE DAY | كل الجلسات ليوم 5 يناير |
| LAST WEEK | "sales of **last Wednesday** (29th Dec 2010)" — نفس يوم الأسبوع من الأسبوع الماضي |
| WEEK TO DATE | من بداية الأسبوع (وفق Week Beginning المختار — مثال: Monday → 3 أيام: 3/4/5) |
| MTD | من 01 يناير حتى 5 يناير |
| YTD | من بداية السنة المالية (شرطي بـcheckbox) |

| المقاييس الـ11 | الصيغة/التعريف |
|---|---|
| SALES | إجمالي المبيعات |
| TRANSACTIONS | "Valid bill count" — عدد الفواتير الصالحة |
| **APT** | **SALES ÷ TRANSACTIONS** (Average per Transaction) |
| COVERS | عدد الأشخاص |
| **APC** | **SALES ÷ COVERS** (Average per Cover) |
| TOTAL TAX | إجمالي الضريبة المحصلة |
| CASH COLLECTION / TRANSACTION | مبالغ وعدد فواتير النقد |
| CREDIT COLLECTION / TRANSACTION | "modes **other than** Cash, Void, Complimentary and Non Chargeable" |
| TOTAL TIP | "other than the Complimentary bill tip" |

**التنبؤ العامي** (اسم العمود حرفياً):
> **"Where are we headed with this average?"** = "(Total MTD Sales / 31) * 5" — أي (متوسط MTD اليومي) × عدد أيام الشهر المنقضية: توقع إغلاق الشهر.

**ملاحظة تسمية**: جداول الحقول تستخدم BREAKFAST بينما خلاصة الأعمدة تكتب "Morning" — عدم اتساق تحريري طفيف (لا يرقى لتناقض — يُسجل هنا).

**الاختبار الرقمي**: AC-PR-02 يختبر (MTD=31000, 5 يناير) → 31000/31×5 = **5000**.

## 4. Popularity Analysis (§13) — عتبة القطع

| البند | القيمة |
|---|---|
| **Cut Off Quantity** | أدنى كمية بيع ليظهر الصنف — **أقصى قيمة 9999** |
| خيارات المعاملات | Only Standard · Only NC Settlements · **Standard and NC Settlements both together** |
| نسبة Grand Total | **(Item Total ÷ Restaurant Total) × 100** |
| نسبة Group Total | **(Item Total ÷ Group Total) × 100** |
| الترتيب | "Items are listed in the **decreasing order** of sales within a group" |

## 5. Popularity Report (Time) (§14) — الشرائح الزمنية

- مدخلات **Time Slot يدوية متسلسلة**: "The time slot entered should be **greater than the previous** time slot entered and **none of the fields should be left blank**" — تحقق تسلسلي صارم.
- **'Print 132 Column'**: "if you want to view the **amount details**" — أي 80 عموداً = كميات فقط، و132 = كميات + مبالغ (عائلة 80/132 بدلالة الإضافة — عكس FO!).
- الغرض المعلن: "analyze **in which time slot more sales are happening**" — تحليل ذروة الطلب.

## 6. Order Analysis by Time (§15) — زمن دورة الطلب

لكل فاتورة: **start time وclose time للطلب** + bill/table/Pax/server/net/settlement mode/User — قياس "the time taken to complete each order" — **تقرير زمن الخدمة** (Service-time analytics) الوحيد في الحزمة الذي يقيس دورة طلب من البداية للإغلاق.

## 7. ملاحظات تحويل سريعة (تفصيل كامل في 11)

- 1.2+1.7 (Daybook ×2) و1.8+1.9 (Summary ×2) توائم دمج طبيعية → تقريران بوضعين.
- DS Report → Dashboard يومي + Script Report (صيغ APT/APC/التنبؤ قابلة للنقل الحرفي).
- 1.15/1.16 يستهلكان بنى POS-SET (Open Item + Report Definition) — لا يُبنيان من الصفر.
