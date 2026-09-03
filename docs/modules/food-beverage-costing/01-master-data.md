# 01 — البيانات الأساسية (Master Data) — وحدة FNB

> ماسترات FNB **أربعة فقط** (أصغر عائلة ماسترات بين الوحدات الكبرى!) — لأن الوحدة **تستعير كل شيء**: المطاعم من SYS Setup Outlet، والمطابخ والمخازن والأصناف من MGT، وأنواع KOT/الجلسات/قوائم الطعام من POS. الجديد النقي: **الوصفات** (بكيانها الفرعي نصف المصنّع Sub Recipe) و**الميزانيات** و**الربط الثلاثي**.

---

## 1. جرد الماسترات

| # | الماستر | الدليل | مفتاح/كود | الحقول الموثقة | المصدر |
|---|---|---|---|---|---|
| M1 | **Costing Start Date** | SET §1 | Singleton (لا كود) | Starting Date · User ID · Last Updated · **Audit Date** | SET ص3 |
| M2 | **Costing Link** | SET §2 | Cost Type + Res Code | Cost Type · Res Code · Cost Code/Name · Kitchen Code · Link By (Group/Item) · From/To · Tag · **Sales Tag** | SET ص3-5 |
| M3 | **Sales/Cost Budgets** | SET §3 | Month/Year + Restaurant/Kitchen + Cost Type | Month/Year · Sales Budget/Cost Budget · Restaurant/Kitchen · Cost Type · Session · Sales/Covers · Per Day/Per Month · **Difference** · شبكة التقويم اليومي | SET ص6-9 |
| M4 | **Recipe/Sub Recipe Master** | SET §4 | **Recipe Code = 6 محارف رقمية** | Type · Recipe Code · Name · Portion + 6 تابات (راجع §3) | SET ص10-14 |

## 2. الحقول بالتفصيل الموثق

### 2.1 Costing Start Date (SET ص3)

| الحقل | الوصف الحرفي | ملاحظة |
|---|---|---|
| Starting Date | "The Starting Date is entered at **first time** when the entry is made. **From next time, the date is picked from the system**" + "You will not be able to **edit** the date... **once it is created**" | كيان **Singleton** واحد للفندق — أقرب ما يكون لمفتاح تفعيل لا سجل بيانات |
| User ID | "The Login ID of the user who is logged into the application appears here" | أثر تدقيق تلقائي |
| Last Updated | "The date and time entered during the **previous entry**" | تاريخ آخر لمس |
| Audit Date | "the user can enter the date **beyond which the transactions are not allowed**" | قفل رجعي/أمامي — عائلة Audit Date المعروفة (Night Audit في FO) |

### 2.2 Costing Link (SET ص3-5)

| الحقل | الوصف الحرفي |
|---|---|
| Cost Type | "Select the Cost type from the dropdown list" — الأنواع الموثقة: **Food / Liquor / Soft Drink / Tobacco (Smokes)** (ص2 و§3) |
| Res Code | "Click on the Res Code to view the **linked group and item names** in the Link Item – Kitchen grid" + "On selection of the Cost Center the **Cost Code and Cost Name** is displayed" |
| Link By | "To link the restaurant, select any one link by options: **Group Code or Item Code**" — الربط بمجموعة قوائم POS أو بصنف واحد |
| From, To | "Enter the **range** of the Group Code or the Item Code" |
| Display | "Select one of the options: **All/Un Tagged/Tagged**" |
| Tag Kitchen/Bar | "Select the relevant **Kitchen/Bar** to tag to costing... The following screen appears: Click **Yes**" — تأكيد صريح بالنقر |
| تغيير المطبخ | "If you want to change the kitchen for the Group and the Item, **double-click under the Kitchen Code column**... The Kitchen Code **Help Screen** appears" |
| Defaults | "From the **Available Reports**, select the reports you need and click **Add**. The selected reports will move under **Required Reports**" — تخصيص حزمة تقارير الوحدة! |

### 2.3 Sales/Cost Budgets (SET ص6-9)

| الحقل | الوصف الحرفي |
|---|---|
| Month/Year | "Enter the month and the year... can also be **predefined for future months**" |
| Sales Budget / Cost Budget | خيار ثنائي — البيعي بالقيمة/الPAX والتكلفي **بنسبة مئوية** |
| Restaurant/Kitchen | "Click on Restaurant and a list of all Restaurants defined in the **Setup Outlet under the System**... Click on Kitchen... **Kitchens option under the Materials Management module**" — مصدران مستعاران صريحان |
| Cost Type + Cost Centers | "Click Enter to display all the **pre – defined Cost Centers**... Double Click or press Enter on the row to select" |
| Session | "Budgets can be defined for **any specific session. By default budgets are defined for all sessions**. Once budget of a particular month / year is defined... **the same holds good for the rest of the months in the Financial year**... uniformity... For e.g., if the option for **March 2007 is selected as 'All'** then the option by default remains the same for **any other month in the year 2007**" — انتشار جلسة السنة المالية كلها! |
| Sales/Covers | "Select Sales and enter the **Amount**... or select Covers and enter the number of **PAX**... For entering **both**, you have to define **Sales Budget figures first, followed by the Covers Budget**" — تسلسل إلزامي |
| Per Day | "you have to **manually enter** the Amount or Covers... where the **Calendar Days of the Month** are displayed" |
| Per Month | "the Amount or Covers specified will get **equally distributed**" |
| Difference | "This is **not an entry field**... If some changes are made to the figures distributed, the **Difference is reflected**" — عداد انحراف التوزيع اليدوي |
| Cost % | "You have to enter the Cost % information. The Percentage... **applicable to all the days of the month**" (تملأ الشبكة وتعدل خلية-خلية) |
| Variance | "If the **Actual Cost Percentage calculated is greater than the Budgeted Percentage**, then the Variance will reflect as **minus** and if... **lesser**... as **plus**" — إشارة سالبة = تجاوز التكلفة |

### 2.4 Reference# المشترك (COP)

- Kitchen Stock: "Enter a unique Reference #... maximum of **10 alphanumeric characters and minimum of 3**" (COP ص5).
- Kitchen Opening Stock / Inter Kitchen Transfers: "Enter a unique reference number" (COP ص7/ص13) — نفس العائلة بلا أطوال موثقة هناك.

## 3. Recipe/Sub Recipe Master بالتفصيل (SET ص10-14) ⭐

### 3.1 رأس الوصفة

| الحقل | الوصف الحرفي |
|---|---|
| Type | "Select **Recipe or Sub Recipe** from the Type dropdown option" |
| Recipe Code | "It can be **six numeric characters** long. This is a **mandatory field**" — نمط 6-رقمي (أقصر من POS Item الأطول) |
| Name | "Description is normally the **name of the Recipe as it appears in the Menu list**" — تطابق تسمية القائمة |
| Portion | "Enter the portion of the recipe... **Like 2 vegetable rolls etc.**" — الحصة نصية حرة وليست رقمية! |

### 3.2 التابات الست

| التاب | المحتوى الموثق |
|---|---|
| **Recipe** | صفوف المكونات: Type (**Store Items** من "Inventory Master option of Material Management" / **Sub Recipe Item**) · Store number · Code (F1 — description+UOM auto) · **Actual Quantity** (القيمة تُعرض فور الإدخال) · **Process Type** (None/Add New) · **Yield %** (auto-populate وقابل للتعديل "by deleting existing %") |
| **Cost Analysis** | "Restaurant Code – Select the restaurant that will be **consuming** the recipe. Item Code – Press F1..." + شاشة الكمية والسعر + **المعادلة**: COST % = Cost per Portion / PRICE × 100 |
| **Production Req** | "specify the any special production requirements in the space provided" — نص حر |
| **Preparation Method** | "specify the **procedure to prepare** the recipe" |
| **Service Method** | "specify **how and when the recipe will be served**" |
| **Pictures** | "select and display the **pictures of the items** used in the recipe" — وصفة مصورة! |

### 3.3 قواعد الربط الموثقة (SET ص12 — Notes 1..4)

1. "**POS Item can tag for only one Recipe**" (N:1 من طرف POS).
2. تحذير غير حاجب: "If the selected POS item **Rate is Less than Recipe COST**, then it will display warning message saying **'Warning!! Item Price is less than the Cost price'**" — إنذار تسعير خاسر.
3. "**One Recipe can tag to Multiple Res Codes and for multiple POS Items**" (1:N من طرف الوصفة).
4. المعادلة: "**COST % = Cost per Portion / PRICE × 100**".

### 3.4 Sub Recipe — نصف المصنّع (SET ص12)

- "items that are used to **prepare main items**. They can be **tomato sauce**; ... frequently used sub recipes / **semi finished items** which will be used in a recipe".
- "**One sub recipe can be used / linked to multiple recipes** and the quantity of use of the sub recipe **varies based on the recipe requirement**".
- "They may be **accompaniments** to the main items" — المرافقات (الصوصات المشتركة).
- في REP: "SUB RECIPE will generate the details **only based on SUB ITEMS created**" (REP ص3).

## 4. ماسترات مستعارة (لا تُعرَّف هنا — تُستهلك فقط)

| الكيان | المالك الحقيقي | الدليل النصي |
|---|---|---|
| Restaurants/Outlets | **SYS** (Setup Outlet) | SET ص7: "all Restaurants defined in the **Setup Outlet under the System**" |
| Kitchens | **MGT** (Kitchens option) | SET ص7: "Kitchens defined in the **Kitchens option under the Materials Management module**" |
| Items + UOM | **MGT** (Inventory Master) | SET ص11 + COP ص12: "This data is defined in the **Master Entry in Material Management**" |
| Stores | MGT | COP ص5 (قائمة المخازن عند الجرد) |
| Cost Centers | MGT (Customize) | SET ص7 (pre-defined Cost Centers) |
| Sessions / KOT Types / Menu Types | POS (ضمنياً) | COP ص10: "It can be Breakfast / Lunch / Dinner etc." + "Standard KOT or N C KOT" + "the section under which the item is categorized" — **لا إحالة نصية لمالك** (UNK-066) |
| POS Items | POS | SET ص12 (POS Item tags) |

## 5. ملاحظات نمذجة

- **لا إصدارية زمنية في أي ماستر FNB** — لا Applicable From ولا أسرة خلود (مقابل عائلات INI/الشرائح/الأسعار المؤرخة في TEL/MEM/HRP!). أثره: تغير أسعار الأصناف يغيّر تكلفة الوصفة **صامتة** بلا لقطة تاريخية (GAP-FB-P05).
- **Sales Tag** (Revenue/Non-Revenue) علمٌ واحد يميّز المنافذ في كل تقارير التكلفة — أبسط ثنائية إيرادية في المشروع بعد قفل AR.
- **Default Reports** (Required Reports) داخل Costing Link — أول "حزمة تقارير مستخدم" قابلة للتخصيص في المشروع (نمط Dashboard SYS لكن بتقارير التكلفة).
