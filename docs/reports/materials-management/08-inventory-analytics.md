# 08 — تحليلات المخزون (Inventory Analytics) — MGT-REP (Phase 7)

> §11 ABC + §12 FSN + §13 Slow Moving + §14 Non Moving + §20 Conversion Checklist + §21 Efficiency = 6 تقارير — **أثقل كتلة تحليلية في MGT** ومنهجيات إدارية كلاسيكية موثقة حرفياً.

---

## 1. §11 ABC Analysis (Always Better Control) — Pareto المخزون

**الوصف الحرفي:** "analyze the consumption of Items in a Store based on **Quantity or Value** specifications."

**المعايير (ص70-71):**

| # | المعيار | القيم |
|---|---|---|
| 1 | Date range | — |
| 2 | Store | — |
| 3 | **% by Store Value / % by Group Value** (+ Groups إن اختير الثاني) | **مجال نسبة الإسناد** |
| 4 | **%Cumulative / % Consumption** | طريقة الترتيب |
| 5 | **A% Class و B% Class** | **صنفان يعرّفهما المستخدم** |

**القاعدة الحرفية (Note ص71):** "The classifications of Items is **based on the total consumption** and are categorized accordingly into **A and B categories which are User defined**. And the analysis report is generated **Class wise**."

**تفكيك المنهجية:**
- **أساس التصنيف = الاستهلاك الكلي** (لا الرصيد!) — الأصناف تُرتّب بمدى مساهمتها في الاستهلاك.
- **A وB عتبتان يحددهما المستخدم** (مثال كلاسيكي: A=70%, B=20%) — **C ضمنية** (الباقي) — تصنيف ثلاثي بعتبتين معلنتين.
- **% by Store Value / % by Group Value** — نسب الإسناد: قيمة المخزن ككل أم قيمة المجموعة (تصنيف ABC داخل كل مجموعة!) — تحليل هرمي.
- **%Cumulative (تراكمي — منحنى باريتو) / %Consumption (فردي)** — طريقتا الحساب.
- Quantity XOR Value — تصنيف بالكمية أو بالقيمة.

**الموقع في الحزمة:** بعد Menu Engineering في POS (Kasavana-Smith) — هذه **ثاني منهجية إدارية كلاسيكية كاملة** في المرحلة 7 (Pareto/ABC) — MGT وPOS تتقاسمان "التقارير التي تُصنّف وتُوصي" بينما FO/FNB تقيسان وتعرضان.

## 2. §12 FSN Analysis (Fast, Slow, Non-Moving) — بمعامل مُعرَّف داخل الشاشة

**الوصف الحرفي:** "The user can view if the items in a Store are Fast, Slow or Non Moving items **based on a specified cutoff days**. This is computed based on the specifications defined in the option **Define FSN parameter**, where the **Cut off Days and Fast, Slow quantity specifications** for the required Items have to be defined. These details will then reflect in the report."

**آلية الإدخال الفريدة (ص74):**
1. اختيار Store — **"The item Groups will be displayed below"** (الشبكة تعرض المجموعات فوراً).
2. **"Double-click on the Days column"** → شاشة FSN Specifications → إدخال → Save.
3. "Enter the FSN details **for all the groups** of items" — معاملات **لكل مجموعة على حدة**.
4. Date range + خيارات.

**النقاط البنيوية:**
- **الإدخال المدمج**: تعريف المعامل يحدث **داخل شاشة التقرير** (خلية عمود Days) — لا Setup مستقل — أول نمط "Parameter-in-Grid" في الحزمة.
- **المعاملات المزدوجة**: Cut off Days (عتبة الحركة) + **Fast/Slow quantity specifications** (كميات تحدد التصنيف) — FSN الكمي لا الزمني فقط.
- **لكل مجموعة**: حساسية مختلفة لكل عائلة أصناف (مواد سريعة التلف ≠ عتاد).
- يقابل النص المؤسس: MGT-SET §18 "Classify Items as Fast, Slow and Non-Moving in the FSN analysis report" (BR-MG-18) — **التقرير والماستر يشتركان في نفس الشاشة؟** → UNK-094 (أين تُخزَّن المعاملات ومن يملك الشاشة الأم؟).
- العلاقة مع §13/§14: §12 التحليل الشامل، بينما §13 (بPercentage) و§14 (بCut Off Days) استعلامات أحادية أبسط — **ثلاث تقارير لنفس الطيف** (تعدد بوابات منهجي).

## 3. §13 Slow Moving Items

- "list of items that are Slow Moving in a specified Store for a specified period and **for a specified percentage**" (ص76).
- معيار **النسبة** — هنا التعريف البديل: البطء = نسبة (من الاستهلاك؟ من الرصيد؟) — **غير موصّف المرجع** (D-level gap).
- يوصف بأنه "**lookup**" في النص ("In this **lookup**, the user can view...") — تسرّب تسمية LUK إلى REP!

## 4. §14 Non Moving Items

- "items that are Non-Moving in a specified Store for a **specified Group range**. The Items are classified as Non Moving based on the **Cut Off Days specified**" (ص78).
- **Cut Off Days + Group range** — بلا نطاق تاريخ (الجمود يُقاس منذ آخر حركة) — أبسط الثلاثة.

**مصفوفة عائلة الحركة الثلاثية:**

| التقرير | معيار التصنيف | النطاق |
|---|---|---|
| §12 FSN | Cut off Days + **Qty specs (لكل مجموعة)** | Date range |
| §13 Slow | **Percentage** | Date range |
| §14 Non | Cut off Days | **بلا نطاق** (منذ آخر حركة) |

## 5. §20 Item Conversion Checklist

- "list of items that are **transferred** for a given date range and for a specified Store. The list can be processed based on **Conversion Split or Conversion Add**" (ص100).
- **ثنائية التحويل من MGT-TRN**: Split (تفكيك صنف لمكونات — الجزّارة) / Add (تجميع مكونات لصنف — الإعداد المسبق) — نفس ثنائية FNB Conversions — الآن بتقرير كشف مستقل.
- يقابل FNB "Item Conversion" في COP — **التحويلات معمارية عبر وحدتين** (MGT يشغّل، FNB يحلّل التكلفة).

## 6. §21 Efficiency Report — تحليل العائد (Yield) الأصيل

**الوصف الحرفي (كامل — ص101):** "In this report, you can arrive at the **yield percentage** of items that are split or converted. Item details are reflected based on the information recorded in the **Conversion (Add)** option. **When an Item is split, the quantity or yield of the converted items can be less than the quantity of the From Item resulting in a variance**. The report reflects details of the quantity, rate and value of the **FROM and TO Item** along with the **variance and efficiency percentage**."

**تفكيك المنهجية:**

```
From Item: Qty × Rate = Value  ──(Split/Add)──→  To Item(s): Qty × Rate = Value
                              Δ Variance = From − To
                              Efficiency % = To / From × 100 (نسبة العائد)
```

- **أزواج FROM/TO** بثلاثة مقاييس (كمية/سعر/قيمة) + التباين + النسبة — **أكمل تحليل قبل/بعد في الوحدة** (بعد old/new في POS Bill Audit وFO Room Transfer — لكن هنا **بقيَم مادية** لا حالات).
- **الاقتصاد المخزني للتحويل**: يكشف الفاقد (جزّارة: 10كغ لحم ← 8كغ شرائح = كفاءة 80% وفاقد 2كغ).
- "can be **less than**" — التوقع المعلن: الفاقد طبيعي (وقد يكون موجباً في Add؟ — التركيب قد يضيف قيمة).
- **من Conversion (Add)** حصراً — سجل الإضافة هو مصدر الأزواج.

**الجسر الأعمق في الملف:** هذا التقرير = الوجه المادي لـ**Recipe Yield في FNB** (Yield field في Recipe Master) — FNB تسأل "ما عائد الوصفة القياسي؟" (معيار) وMGT-21 يجيب "ما العائد الفعلي الذي حدث؟" (فعلي) — **Standard vs Actual للعائد موزعان على وحدتين!**

## 7. موقع التحليلات بين الوحدات

| الوحدة | المنهجية التحليلية | قرارها التوصي |
|---|---|---|
| POS (Menu Eng.) | Kasavana-Smith 2×2 | STAR يُبقى · DOG يُحذف |
| **MGT (ABC/FSN/Eff.)** | **Pareto ABC + FSN + Yield** | **A يُراقب · Non-Moving يُصفّى · العائد يُحسَّن** |
| FNB (Cost Rep.) | Standard vs Actual | الفرق يُستنكر |
| FO (Forecast) | إسقاط إشغال | التوقع يُسعَّر |

**الخلاصة:** MGT تمتلك **أثقل ثلاثية منهجية تشغيلية** (تصنيف قيمة + تصنيف حركة + كفاءة تحويل) — وهي المنهجيات التي بُنيت عليها صناعة إدارة المخزون الحديثة — موثقة بأربع جمل حرفية مكتملة المعنى (أدق وصف منهجي في MGT-REP كله).
