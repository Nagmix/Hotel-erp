# 15 — تحليل تجربة الاستخدام (UX Analysis) — وحدة Materials Management

> أنماط التفاعل الموثقة في الواجهة الأصلية واستخلاصها للواجهة الجديدة (RTL Arabic-First). MGT نموذج **واجهات كثيفة الحقول بشبكات عمل يومي** — أثقل وحدة إدخالاً بعد FOM.

---

## 1. الأنماط الموثقة الأصلية

### 1.1 لوحة العمليات اليومية (أفضل ممارسة أصلية)

**شاشة Transactions الرئيسية (DNT ص31):** "The main screen... displays information such as **pending Indents, expected Receipts (for 7 days), expiring items, items whose stocks are below minimum level** and Inter Store transfers requisitions. The status bar of the screen also displays information such as **number of** Pending Indents, Store Transfers, Items below Minimum Level, Expiring Items and Expected Receipts."

**الاستخلاص للواجهة الجديدة:** صفحة رئيسية للمخازن بعدادات حية + بطاقات إنذار (تنتهي صلاحية/تحت الحد/متوقع) — **أول KPI Dashboard عملي موثق في المشروع قابل للترجمة مباشرة إلى مكون React**.

### 1.2 أنماط الإدخال الشبكي

| النمط | الموثق | الاستخلاص |
|---|---|---|
| **إدخال أعمدة-مراكز** | Indent: "All the chosen cost centers are shown here, enter the actual required quantity **for the item**" (الأعمدة = CC!) | جدول pivot (صف=صنف، عمود=مركز) — مكون قابل للتطبيق مع RTL |
| **Batch Help التفاعلي** | "The Batch Help screen also helps to have any **last minute modifications** in the quantities selected" (DNT ص38) | محرر دفعات inline قبل الحفظ |
| **الحفظ متدرج** | Receipt: شاشة رئيسية → صفوف (نقر مزدوج) → تفاصيل → Confirm → Save + **View Entries قبل الحفظ** | Wizard ثلاثي الخطوات مع معاينة |
| **Load قبل العمل** | "Click Load to display all selected item value, code, rate and quantity" (Physical Stock) + Inter Store Requisition | زر تحميل صريح (fetch-on-demand) |

### 1.3 اختصارات لوحة المفاتيح الموثقة

| الاختصار | الوظيفة | المصدر |
|---|---|---|
| **F1** | كل قوائم المساعدة (Store/Item/Vendor/Contract/GRR/PR#...) — نمط موحد | كل الوحدة |
| **F2** | (الموازنة) نسخ سنة مركز | SET §22 |
| **F3** | Stock Locator (في Inter Store Requisition) + (الموازنة) اختيار Fin. Year | DNT §9 + SET §22 |
| **F4** | (الموازنة) لصق لمركز آخر | SET §22 |
| **F7** | **Sale History** (شهر → يوم، سنة/سنة) | DNT §9 ص62-63 |
| **Enter/نقر مزدوج** | تفعيل Tag (Yes/No) — Tax Exemptions | SET §16 |
| **Space/نقر مزدوج** | تبديل قيمة tag | DNT §7 |

### 1.4 أنماط التعمق (Drill-down)

- **Group Cons Month Range:** مجموعة → (نقر مزدوج) أصناف → (نقر مزدوج) شهر → (نقر مزدوج على عمود الشهر!) → **Item Stock Status** (LUK §17 ص33) — **أعمق سلسلة تنقل موثقة في المشروع**.
- **Spending Pattern:** سنة/سنة → شهر (نقر مزدوج) → يومية.
- **Item Stock Status:** "Click on any date to view the details based on the transaction type" — **النقر على خلية تاريخ** يفتح نوع المعاملة.

### 1.5 الحوار والحماية

- **تأكيد مزدوج للإلغاء:** SWO Cancel → "You will get a confirmation message" → Confirm (DNT ص29-30).
- **تنبيه إجرائي:** Stock Variance: "alerting if the Physical Stock Variance report **has been checked**" — سؤال تحقق بشري قبل فعل لا رجعة فيه (DNT ص72).
- **منع ما بعد الحفظ:** Store/Opening Balance — الرسائل غير موثقة لكن المنع موثق.

## 2. عيوب UX الموثقة (تُصلح في الجديد)

| العيب | الدليل | الإصلاح المقترح |
|---|---|---|
| **منطق Stop Payment المعكوس** | "select NO to stop... YES to allow" تسمية ملتبسة (SET ص28) | تسمية "السماح بالدفع" الصريحة — يُسجل كقرار توضيح |
| **7 شاشات فرعية للمورد** | TDS/Payment/Bank/Contact/Tax/BlackList/Other أزرار متتالية | Tabs واحدة صفحة Supplier موحدة |
| **إدخال Bill# يدوي مع كونه جسر المطابقة المالي** | بلا تحقق ذكي من التكرار [NOT DOCUMENTED] | اقتراح ومطابقة عند الإدخال |
| **توزيع Manual في Batch Help** | تعديل لحظي كميات الدفعات | عرض FEFO التلقائي مع override موثق |
| **لا رسائل خطأ موثقة** | المنع يوثق دون النص | نظام Toast عربي شامل |

## 3. توصيات الواجهة الجديدة (Arabic-First RTL)

1. **صفحة "عمليات المخازن اليومية"** (ترجمة شاشة Transactions): 5 عدادات + 5 بطاقات قوائم (معلقات/متوقع7أيام/منتهيات/تحت الحد/تحويلات) — تنبيهات حية.
2. **معالج استلام ثلاثي الخطوات** (نوع ← مستندات ← أصناف) مع شريط Bill# بارزاً (جسر المطابقة) وفحص القواعد الزمنية الثلاث (GR≤Expiry إلخ) فورياً.
3. **جدول Indent المحوري** (صنف×مركز) بإدخال كمية لكل خلية + Row totals.
4. **محدد دفعات FEFO** مكون منفصل يعرض الدفعات بأقرب انتهاء أولاً (وضوح آلية FIFO الأصلية).
5. **صفحة مورّد واحدة بتبويبات** السبع + إنذار Stop/Blacklist بشارة واضحة.
6. **شاشة إقفال شهري** (Physical → Variance → Ledger) بـ Stepper يعرض حالة كل خطوة + زر Cancel Ledger بحوار تحذير.
7. **الموازنة**: شبكة CC×شهر مع F2/F4 (نسخ/لصق) معاد اختراعها بأزرار ظاهرة + توزيع Apportion بنمط قابل للمعاينة قبل التطبيق.
8. **حقول البحث F1 → Combobox عربي** مع بحث نصي (الاسم/الكود).
9. **الاستعلامات العشرون** → صفحة "استعلامات المخازن" واحدة بفلاتر ديناميكية (النمط الموحد: تاريخ/شهر × كيان × حالة) + Drill-down بالنقر الموحد.
10. **عرض حالات ملونة**: Pending/Closed/Cancelled/Processed + Blank (بدل الفراغ) بشارة "لم يُستلم".
