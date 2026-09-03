# 01 — البيانات الرئيسية (Master Data) — وحدة FXD

> **خمسة ماسترات هرمية + ماستر مركزي**: Main Groups → Sub Groups (+ربط GL الرباعي) → Locations → Components → **Fixed Asset Master** (~35 حقلاً بأطوال موثقة + شبكتا Tax/Component) — هرمية تصنيف ثلاثية المستوى (مجموعة رئيسية → فرعية → موقع) يُبنى عليها الكود الآلي 12 حرفاً، ومعها **Depreciation Method** كتهيئة نِسب مزدوجة (SLM/WDM) على مستويي المجموعة والأصل.

---

## 1. الهرمية الموثقة

```
Asset Main Group (movable/immovable — بلا Property!)
        └─ Asset Sub Group (Property-wise + ربط GL الرباعي + Cost Center)
                └─ Fixed Asset Master (كود 12 = 5 مجموعة فرعية + 3 موقع + 4 مسلسل)
                        ├─ Tax Selection Grid (ضمن القيمة)
                        └─ Component Selection Grid (خارج قيمة الأصل!)
Asset Location (مستقل عن الهرمية — يُركَّب في الكود)
Asset Component (ماستر مكوّنات مشترك لأصول متعددة)
Depreciation Method (Property + FY + Sub Group أو Asset — نِسب SLM & WDM معاً)
```

## 2. جرد الماسترات (الحقول بالأطوال الحرفية الموثقة)

### 2.1 Asset Main Groups (§2 ص4)

| الحقل | الفعل | ملاحظات |
|---|---|---|
| Main group | كود المجموعة | "Once specified, value **can't be modified**" — قفل تعديل الكود |
| Long name / Short name | الاسم الطويل/المختصر | **30 / 10** حرفاً |
| Status | active/passive | |
| User / Last Updated | أثر تلقائي | التصنيف "such as movable, immovable etc" — مثالان فقط بلا قائمة (UNK-068 جزئي) |

### 2.2 Asset Sub Group (§3 ص4-5) — ⭐ ماستر الربط المحاسبي

| الحقل | الفعل | ملاحظات |
|---|---|---|
| Property | اختيار الفندق | ماستر **Property-wise** (بعكس Main Group!) |
| Group code | اختيار المجموعة الرئيسية | |
| Long/Short name | | 30/10 حرفاً |
| Main group | عرض/إدخال | |
| **BS Depr. A/c + BS Depr S/L** | حساب الإهلاك — **الخصم/الالتزام (Balance Sheet)** | "Chart of account with account type '**sub ledger**', will allow to select the sub ledger" — عمق دليل حسابات دائم |
| **PL Depr. A/C + PL Depr S/L** | حساب الإهلاك — **الدخل والمصروف (P&L)** | نفس عمق sub ledger |
| Cost center / department | مركز التكلفة | قناة تحليلية للترحيل |

> **Validation حرفية (ص5):** "Against one sub group if **any one ledger is linked**, then program will validate to link **all the ledgers** i.e. if balance sheet a/c is linked, then profit and loss a/c must be mandatorily linked" — تماثل إلزامي؛ والربط كله اختياري أصلاً: "Linking groups to chart of account is **optional**. If asset group linked to chart of account, then those assets transaction **will be posted to financial module also**".

### 2.3 Asset Locations (§4 ص5-6)

| الحقل | الفعل | ملاحظات |
|---|---|---|
| Location Code | كود الموقع | F1 لقائمة المواقع المعرفة مسبقاً |
| Long/Short Name | | 30/10 حرفاً؛ Short Name "recorded for reflection in **certain queries and reports** where the Long Name cannot be Accommodated" |
| Status | active/passive | |
| User / Last Updated | أثر تلقائي | |

### 2.4 Asset Components (§6-7 ص6-7)

| الحقل | الفعل | ملاحظات |
|---|---|---|
| Component Code | كود المكوّن | F1 لقائمة المعرفة مسبقاً |
| Long/Short Name | | 30/10 حرفاً |
| Status | active/passive | |

> التعريف الحرفي: "Component is nothing but **additional charges that are occurred during installation or after installation**" — ماستر شفرات تكاليف التركيب (نقل/تجميع/اختبار...).

### 2.5 Fixed Asset Master (§6 ص7-10) — ⭐ الماستر المركزي

| الحقل | الفعل | ملاحظات حرفية |
|---|---|---|
| Property | اختيار | |
| Sub Group code | F1 | **5 محارف** |
| Location | من Location Master | |
| **Asset code** | **آلي** | "comprises of **12 characters**... Sub group code the first 5, location code the next 3 and running serial the final 4... from **FIMSHTBL** with combination of group code and location code" |
| Long name | | **70** حرفاً (أطول اسم في الوحدات!) |
| Short name | | 10 حرفاً |
| Manufacturer | | **60** حرفاً |
| Date installation | تاريخ بدء الاستخدام | "**Should be less than or equal to server date**" |
| Currency | F1 | "By default, the **local currency** will be loaded" |
| Currency rate | آلي | "as per selected currency factor" |
| Quantity | رصيد افتتاحي | |
| U.M.O | F1 وحدة قياس | |
| Item price / Qty | سعر الوحدة | |
| **Total Value** | **آلي** | "Total Value = **Quantity X Item Price**" |
| Residual Value / Qty | قيمة متبقية للوحدة | "scrap value or **final value** of an asset" |
| **Depn. Op. Bal** | رصيد إهلاك افتتاحي | "should be defined **if depreciation start date is less than then fixed asset start date**" — جسر عالم ما قبل التحنيط! |
| Life span Value | + year/month | |
| PO #, PO date, Grr #, Grr date, Bill #, Bill date | حقول حرة | "can be defined as **mandatory, with INI switch validation**" (رقم غير موثق — UNK-073) |
| Supplier code | F1 | |
| Remarks | | |
| Asset Insurer | مؤمن الأصل | حقل نصي حرة |
| Asset maintenance | صيان الأصل | حقل نصي حرة — **بلا ربط MNT!** (راجع 12) |
| Asset status | اختيار من قائمة | قائمة القيم غير موثقة (UNK-068) |
| Start date depn | بدء الإهلاك | |
| **Last date depn** | **عرض فقط** | "not a user define field... visible in **modify and browse mode**" |
| **Current closing details** | عرض تاريخي | "quantity balance, **net book value**, total depreciation etc" |

**شبكتا الاختيار (Double-click grids):**

| الشبكة | الحقول | الدلالة |
|---|---|---|
| **Tax Selection** | Tax Code (F1) · Currency (F1) · Amount | "For a asset if **any tax was applied during purchase time**" — ضريبة ضمن بنية الأصل |
| **Component Selection** | Component Code (قائمة) · Currency (F1) · Amount | "component details to be maintained separately (**which are excluding the asset value**)" — خارج القيمة! |

### 2.6 Depreciation Method (§7 ص10-11)

| الحقل | الفعل | ملاحظات |
|---|---|---|
| Property | اختيار الفندق | |
| Financial Year | **F3** لفترات Financial Year Parameter | ثالث استخدام موثق لـF3 (بعد FAS/HRP) |
| Sub Group / Asset code | مستويان | "factor... either for **over all group asset** or **individual asset wise**" |
| Straight line method | % | النسبة المئوية |
| Written down method | % | النسبة المئوية — **تُعرَّف معاً دائماً** (المستعمل يقرره INI #475!) |

> التداخل: "To define factor for overall asset group... double click on sub groups **from first screen**... If a user wants to specify asset wise for selected sub group, then click on **detail**" — شاشتان متتاليتان (قائمة فرقية → تفصيل أصول).

## 3. العائلات عبر الوحدات

| العائلة | عضو FXD | ملاحظة |
|---|---|---|
| قفل الكود بعد الإنشاء | Main Group | نفس نمط HRP/MEM (الكود خالد) |
| Status active/passive | 4 ماسترات | النمط الأم |
| أثر User/Last Updated | كل الماسترات | تلقائي صامت |
| Property-wise | Sub Group + Method + كل المعاملات | مقيمة بالفندق (Main Group وLocation **ليستا كذلك** — غريب!) |
| Long/Short 30/10 | 4 ماسترات | النمط الموحد |
| **بوابة تاريخ أحادية** | Start Date | عائلة FNB — property-wise هنا |
| **تسريب اسم جدول** | FIMSHTBL | نادر جداً (مع جدول INI) |
