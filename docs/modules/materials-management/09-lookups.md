# 09 — الاستعلامات (Lookups) — وحدة Materials Management

> LUK كامل: **20 استعلاماً** بالفلاتر والسلوك الموثق — عمليات قراءة ص instant-فورية بلا ترحيل، تخدم الإدارة اليومية للمخزون والمشتريات.

---

## 1. استعلامات دورة الطلب والشراء (10)

| # | الاستعلام | الفلاتر | العمق/السلوك | المصدر |
|---|---|---|---|---|
| 1 | **Requisition Status** | Date/Month range × Item wise/Req wise × **All/Received/Pending** | قائمة أصناف/طلبات + Print | LUK §1 ص2-4 |
| 2 | **Indent Status** | Date/Month × **Cost Center/Sub Store** × Pending/Closed/Deleted/All | نقر على indent → التفاصيل + Print | LUK §2 ص4-6 |
| 3 | **Indent Status by Item** | نفس 2 + **From/To Item** | عرض per-item | LUK §3 ص6-8 |
| 4 | **Authorization Details** | **PO/PR/Indent** × Date wise/PO wise + النطاق | نقر → تفاصيل الأصناف — **أداة تدقيق التفويض** | LUK §4 ص8-9 |
| 5 | **PO Status** | PO# (F1) | "Items ordered, and received **up to date** along with the status... Pending, Closed or Cancelled" | LUK §5 ص9-12 |
| 6 | **PO Status by Vendor** | **Supplier wise/Item wise** × تسلسل (PO date/PO no./Item) + النطاق | Pending/Closed/Cancelled/**Blank Space** (!) | LUK §6 ص12-13 |
| 7 | **Cancelled & Closed PO** | **Range/Upto Date** × All/Cancelled/Closed | مع تفاصيل الأصناف | LUK §7 ص14-15 |
| 8 | **Pending PO** | **PO/Delivery Date** × Upto Date/**Vendor Code** (نطاق) | "based on the **difference between the Ordered and Received Quantity**" — نقر → التفاصيل | LUK §8 ص15-17 |
| 9 | **SPO Status** | **SPO wise/Item wise/Supplier wise/Closed** × **Validate To/From Date** | نقر → تفاصيل | LUK §9 ص17-19 |
| 10 | **SWO Status** | Date/Month × Item/SWO wise × **Closed/Cancelled/Processed/All** | قائمة + Print | LUK §10 ص19-21 |

## 2. استعلامات المخزون والحركة (8)

| # | الاستعلام | الفلاتر | العمق/السلوك | المصدر |
|---|---|---|---|---|
| 11 | **Receipt/Issue by Group** | Store + date range | "A **consolidated figure** of the Issues and Receipts" | LUK §11 ص21-22 |
| 12 | **Store Balance by Date** | Store + date range | "consolidated summary of **all transactions in terms of value**": Receipts, Issues, Adjustments, RR, IR — نقر على Receipt → **تفتيت أصناف** | LUK §12 ص22-24 |
| 13 | **Item Stock Status** | Store + Item + **Month&Year/Up to current** | تفاصيل المعاملات — "**Click on any date** to view the details based on the **transaction type**" — تعمق بالنقر على التاريخ! | LUK §13 ص24-26 |
| 14 | **Item Stock Balance** | Store + date + **Nil Balance checkbox** × **Item Code/Item Group** (نطاق) | أرصدة ختامية + Opening + حركات — نقر صنف → Stock details | LUK §14 ص26-28 |
| 15 | **Item Balance by Date** | Store + Item + From/To | "Quantity and value details for **Opening balance, Receipts, Issue** etc" | LUK §15 ص28-30 |
| 16 | **Item Stock by CC** | **Cost Center/Room** + Item# | "stock details of a selected item **at each cost center/Room**" | LUK §18 ص34 |
| 17 | **Consumption Detail** | Store + CC + date × Selected/**Range** لـ: Item Code/Item Group/**Item Type/Group types/Vendor codes** | استهلاك مراكز التكلفة بأغنى فلاتر في الوحدة | LUK §16 ص30-31 |
| 18 | **Group Cons Month Range** | Store + CC + Item Groups + month range | **تعمق ثلاثي المستويات**: "Double-click on any item group → individual items; double-click on the items → consumption **for each month**; Double-click on the **month column** → **Item Stock Status**" (!) | LUK §17 ص31-34 |

## 3. استعلامات التحليل التوريدي (2)

| # | الاستعلام | الفلاتر | العمق/السلوك | المصدر |
|---|---|---|---|---|
| 19 | **Vendor Selection** | Store × **Vendor/Item** (نطاق) | "list of all Items received by the Suppliers... **last receipts date, last receipt rate, expiry date**" — لوحة قرار اختيار المورد | LUK §19 ص34-35 |
| 20 | **Spending Pattern** | Store + Item + Doc date × **Consumption/Purchase** | "average consumption or purchase... **comparative analysis of the current year with the previous year**" — نقر شهر → تعمق شهري | LUK §20 ص36-37 |

## 4. أنماط UX المستخلصة

1. **نمط الفلترة الموحد:** (Date/Month) × (كيان/نطاق) × (حالة) — قالب نموذجي لصفحات الاستعلام في الواجهة الجديدة.
2. **النقر المزدوج = تعمق:** النتيجة ليست نهاية — صف → عنصر → شهر → استعلام آخر (سلسلة L17 → L13 أعمق تتابع موثق في المشروع كله!).
3. **قيم حالة ثنائية+:** Pending/Closed/Cancelled/Deleted/Processed/Received + **"Blank Space"** في PO by Vendor (حالة خام غير معالجة؟) — [UNCERTAIN] دلالة الفراغ: على الأرجح لم يُستلم عليه إطلاقاً.
4. **كل شيء قابل للطباعة** — الاستعلام = تقرير خفيف (زر Print قياسي).
5. **المقارنة الزمنية مدمجة:** Spending Pattern (سنة/سنة) وSale History (شهر→يوم سنة/سنة) — أدوات تحليل اتجاهات في واجهة 90s!
