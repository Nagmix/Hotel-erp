# 07 — قوائم الماستر: القوائم والمُعدِّلات والساعات السعيدة (§18–21)

> أربعة تقارير "مساتر معروضة": Menu List بثلاث قوائم · Happy Hours (المستقبل المسموح!) · Modifier List · TS Modifier List.

---

## 1. Menu List (§18) — القوائم الثلاث

> "gives the details of all menu items of the selected outlet, with options to view the report **by item codes or by item names**."

### 1.1 القوائم الثلاث (Selection XOR)

| القائمة | الأعمدة |
|---|---|
| **Code List** | الأصناف وأكوادها لنوع القائمة + **"the user who has updated the item along with the date the item was updated"** — ماستر بأثر تعديل! |
| **Rate List** | الأصناف تحت كل مجموعة + **portion · quantity · UOM** + **currency** + item rates + **taxes applicable** + discounts + **non chargeable %** + last updated + User |
| **Other List** | الأصناف تحت كل مجموعة + **printer · preparation time · kitchen · classification · default bill · print sequence** + User |

### 1.2 مرتبة

- **Order By: Item Code (ترتيب زمني/رقمي "chronological order") XOR Item Name (أبجدي)**.

### 1.3 C-POS-03 (خطأ تحريري)

الخطوة **"3. Select one of the Selection options: Code List, Rate List or Other List."** مكررة **حرفياً مرتين متتاليتين** (ص144) — خطأ تحريري خام (نسخ سطر) يؤكد غياب تدقيق لغوي في الوثيقة الأصلية.

### 1.4 الدلالات

- **Rate List = بطاقة صنف كاملة**: NC% (نسبة غير خاضع!) + ضرائب + خصم + UOM + عملة — أغنى صفحة مواصفات صنف خارج POS-SET نفسه.
- **Other List = بطاقة إنتاج**: طابعة + **وقت التحضير (preparation time)** + مطبخ + **default bill** + **print sequence** — الوثائق التشغيلية للطبخ والطباعة.
- ماستر Menu به **أثر تعديل (User + date)** داخل تقارير العرض — يقابل سمة Last Updated في ماسترات الوحدات الأخرى.

## 2. Happy Hours List (§19) — الاستثناء الزمني الوحيد

> "The **From date can be less than, equal to or greater than the accounting/system date** and the To Date should be **equal to or greater than the From Date**."

| البند | القيمة |
|---|---|
| المدخل | نطاق تاريخ (**مستقبلي مسموح** — الاستثناء الوحيد في مصفوفة تواريخ POS كله!) + Outlets |
| المخرجات | لكل تاريخ: **time · item code · item name · menu rate (لكل يوم أسبوع!)** + "For all the days of the week the **discount in amount and percentage**" |

**الدلالات:**

1. **تقرير قوالب مستقبلية**: Happy Hours مخطط مسبقاً — القائمة تعرض الخطة لا التاريخ — لذلك المنطق الزمني معكوس (future-friendly) بخلاف كل تقارير الوقائع (past-bound).
2. **سعر لكل يوم أسبوع** ("menu rate for each week day") — تأكيد أن Rate الحرفي متغير بيومي في نموذج FN6i (بازل FO Rate Master بـAll/Current/Past/Future).
3. الخصم يوصف بثنائية **قيمة ونسبة معاً**.

## 3. Modifier List (§20)

> "details of predefined modifiers in an outlet... Item Code, Item Name, Modifier Code, Modifier Name, and **extra charges, if any**."

- المدخل: Date + Outlet — فقط (أبسط شاشة في الملف).
- اللافت: المدخل Date موجود رغم أن المخرج ماستر — **طابع زمني للماستر (as-on)** — نفس نمط Telephone Master List الثلاثي الأنماط (Current/Past/...).
- عائلة Modifier الموازية: Modifier Sales (1.14) للوقائع مقابل Modifier List (20) للتعريفات.

## 4. Touch Screen (TS) Modifier List (§21)

> "details of predefined **touch screen** modifiers in an outlet... item code, item name, Touch Screen Modifier name, code and **rate**. **The User's name is also displayed.**"

- الانفصال البنيوي: **TS Modifier ≠ Modifier** — قائمتان منفصلتان بماسترين مختلفين (شاشة اللمس لها مُعدِّلاتها الخاصة بأسعارها) — دليل واجهات مزدوجة (Classic + Touch Screen — راجع Touch_Screen_Manual).
- الفرق الحرفي: §20 يعرض **extra charges** و§21 يعرض **rate** + **User** — اختلاف معجم بين الماسترين المتوازيين.

## 5. عائلة "قوائم الماستر" عبر المشروع (بعد POS-REP)

| الوحدة | القائمة | نمط as-on |
|---|---|---|
| POS-REP | Menu List ×3 + Modifier ×2 | تاريخ مقيد (≤ Accounting في 21) + **مستقبلي في 19** |
| TEL-REP | Telephone Master List (ثلاثي الأنماط) | Current/Past/… |
| MGT-REP | Item/Store Lists (مؤجل) | — |

> النمط العام: قوائم الماستر تُعامل كتقارير **بلحظة زمنية** — POS تضيف الحالة القصوى: قائمة **مستقبلية** (خطة Happy Hours) — أول "ماستر-تقرير مستقبلي" في الحزمة كلها.

## 6. ملاحظات تحويل سريعة

- Code/Rate/Other → ثلاث Print Format/View على Item (الأعمدة جاهزة كقائمة حقول) — لا تقرير جديد، بل **عرضان إضافيان لماستر موجود**.
- Happy Hours List → تقرير Pricing Rule (as-on + future) — ERPNext يدعم Item Price بتواريخ valid-from/to أصلاً.
- Modifier/TS Modifier → جدولان (Item Modifier + TS Modifier) كما في mapping الوحدة الأم + عرضان.
