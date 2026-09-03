# 10 — مصفوفة قواعد التواريخ (POS-REP)

> ~20 قاعدة حرفية عبر 59 بنداً: مراجع زمن ثلاثة + قيود نطاق + استثناءات. النمط العام: **POS ماضوية** (وقائع مالية) — باستثناء وحيد (§19).

---

## 1. مراجع الزمن

| المرجع | التقارير |
|---|---|
| **Accounting Date** (الغالب) | 1.1 · 1.4 · 1.6 · 2 (≤) · 3 (**<**) · 5.1 · 5.3 · 5.4 · 5.5 · 6.1 · 6.3 · 8 · 9 · 10 · 11.1 · 11.2 · 11.3 · 11.4 · 13 (≤ Current!) · 14 · 16.1 · 16.2 · 16.3 · 16.4 · 16.5 · 17.1 · 17.2 · 17.3 · 17.5 · 21 · 22 · 23 |
| **Server Date** | 1.2 · 1.3 |
| **Current Date** | 1.7 · 1.13 · 1.16 · 5.6 · 7.1 · 7.2 · 12 · 13 · 17.4 |
| **Current Month/Year** | 7.3 |
| **(حر — بلا قيد صريح)** | 18 · 20 (Date بلا تحقق موثق) |

## 2. القواعد الحرفية

### 2.1 السقوف والنوافذ

| القاعدة | النص الحرفي | التقرير |
|---|---|---|
| **≤ 7 أيام** | "The End date entered should **not be greater than 7 days** from the Start Date and the date should be less than or equal to the accounting date **within the same month**" | 1.10 Weekly Manager |
| **≤ 30 يوماً** | "the date difference should be **maximum 30 days**" | 1.13 Shop Sales |
| **نفس الشهر** (العائلة الكبرى) | "within the same month" | 1.8 · 1.9 · 1.10 · 1.11 · 1.12 · 1.14 · 1.15 · 1.16 · 4 · 5.5 · 5.6 · 6.1 · 6.2 · 6.3 · 11.1 · 11.2 · 12 · 13 · 14 · 15 · 16.1 · 16.2 · 16.3 · 16.4 · 16.5 · 17.2 |
| **نفس الشهر (نطاق متعدد منافذ)** | "within a month" | 3 · 7.2(لا!) |
| **عبور الشهور مسموح** | "across months" | **9 PAN** · **17.5 Bill Audit** (+ 11.3 "within **any** month" — صياغة أوسع غامضة) |
| **الاستبعاد الصارم** | "The date entered should be **less than** the Accounting date" | 3 Settlements by Date |

### 2.2 المستقبل (الاستثناء الوحيد)

| القاعدة | النص الحرفي | التقرير |
|---|---|---|
| **From حر زمنياً** | "The **From date can be less than, equal to or greater than** the accounting/system date and the To Date should be **equal to or greater than the From Date**" | 19 Happy Hours List |

### 2.3 قيود أخرى

| القاعدة | النص | التقرير |
|---|---|---|
| **≤ Current Month/Year** | "The Month/Year entered should be less than or equal to the Current Month/Year" | 7.3 |
| **تسلسل الشرائح** | "The time slot entered should be **greater than the previous** time slot entered and **none of the fields should be left blank**" | 14 Popularity (Time) |
| **فترة واحدة (Date واحدة)** | Date مفردة | 1.2 · 1.3 · 2 · 5.2 · 5.3 · 5.4 · 17.3 · 17.4 · 18 · 20 · 21 · 23 |

## 3. عتبات العرض والمعالجة (جوار التواريخ)

| العتبة | السلوك | التقرير |
|---|---|---|
| **> 7 منافذ** | "print the report using **132 column format**" (إجباري) | 11.4 NC Outlet Summary |
| **≤ 8 منافذ** | "Maximum 8 outlets can be processed and printed at a time" | 1.4 Sales By Group |
| **Print Day Total** | "If you select **multiple** outlets/menu types this option will **not be available**" | 1.1 |
| **Table# مشروط** | "If you select **All**... you will **not have the option to select the Table number**" | 17.2 KOT Audit |
| **Cut Off Quantity** | "The maximum quantity you can enter is **9999**" | 13 Popularity Analysis |

## 4. المقارنة مع مصفوفة FO (الوحدتان REP المكتملتان)

| البعد | FO (~25 قاعدة) | POS (~20 قاعدة) |
|---|---|---|
| **اتجاه الزمن** | مستقبلي واسع (Expected Arrivals/Cancellations + Forecast 10-15-31) + ماضوي | **ماضوي شبه كامل** — مستقبلي واحد (Happy Hours) |
| **مرجع الغالب** | Accounting/Current | Accounting (أغلبية أوضح) |
| **نفس الشهر** | ~15 تقريراً | ~25 تقريراً — **أثقل تركيزاً** |
| **نوافذ الأيام** | 10/15/30/31 | **7/30** |
| **عتبة عمود إجبارية** | — | **>7 منافذ → 132** |
| **الاستبعاد الصارم (<)** | — | **§3** (وحيدة) |
| **استثناء future** | متعددة | **واحد** (Happy Hours — لكنه تقرير ماستر/خطة لا وقائع) |

> **القاعدة الاستنتاجية**: القيود تعكس **طبيعة البيانات**: FO (حجوزات مستقبلية) تفتح المستقبل؛ POS (وقائع مبيعات مسواة) تحبسه — ما عدا خطط الأسعار (Happy Hours) فتنفتح لأنها template. عند التنفيذ: **قيود same-month تُهجر** (تقارير حرة) ويُحتفظ بالسقوف التحليلية (7/30) كـdefaults ذكية.

## 5. قواعد المرجع الزمني المزدوج

| التقرير | الاختيار |
|---|---|
| 1.9 Summary by Shift | **Accounting date XOR Shift Date** |
| 5.1 Collection Summary | **Bill Date XOR Shift Date** |

> ثنائية مرجع التاريخ (فاتورة/وردية) — مفهوم محاسبي (recognition vs collection window) يظهر مرتين: نفس الشكليات في FO Cashier (shift-wise 24h).
