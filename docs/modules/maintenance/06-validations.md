# 06 — قيود الإدخال والتحقق (Validations) — وحدة MNT

> **V-MN-01..20** — عائلة قيود طولية صارمة (كود 3/6/7/8 محارف حسب الماستر + Name 30/Short 10 بحد أدنى 3) + قيود نافذة زمنية (مستقبلي ≤31) + قيد جدولة (Must Complete By ≤ Lag) + قيود انتقاء (≥1 مخزن/مركز).

---

## أ) قيود الأطوال والأنماط (موثقة حرفياً)

| ID | الحقل | القيد | المصدر |
|---|---|---|---|
| V-MN-01 | Location Code | إلزامي، **6 محارف ألف-رقمية كحد أقصى** | SET ص4 |
| V-MN-02 | Location Name / أي Name ماستر | إلزامي، 30 كحد أقصى، **حد أدنى 3 محارف** | SET ص4 |
| V-MN-03 | Location Short Name / أي Short Name | إلزامي، 10 كحد أقصى، **حد أدنى 3 محارف** | SET ص4 |
| V-MN-04 | أكواد Category/Cost/Shift/ServiceType/Rhythm/Skill/Priority | إلزامية، **3 محارف ألف-رقمية** | SET ص6/7/9/10/11/13/16 |
| V-MN-05 | Employee # | إلزامي، **7 محارف رقمية** (رفض الحروف) | SET ص14 |
| V-MN-06 | Designation | إلزامي، **3 محارف ألف-رقمية** + F1 | SET ص14 |
| V-MN-07 | Equipment Code | **8 محارف ألف-رقمية** كحد أقصى | OPR ص18 |
| V-MN-08 | Complaint Ref. No | **10 محارف ألف-رقمية** كحد أقصى | OPR ص3 |

> **النمط اللافت:** الحد الأدنى (3 محارف) للName/ShortName في كل الماسترات — منع الاختصارات أحادية/ثنائية الحرف بلا استثناء موثق.

## ب) قيود الإلزامية الشرطية

| ID | القاعدة | المصدر |
|---|---|---|
| V-MN-09 | Room # أو Location Code — **واحد منهما إلزامي** عند تسجيل شكوى (اختيار ثنائي ثم F1) | OPR ص3 |
| V-MN-10 | Department وComplaint Details وReported By — حقول الإدخال الكاملة للشكوى (سياق نموذج التسجيل) | OPR ص3 |
| V-MN-11 | PM# لا يُولَّد إلا "once **all the mandatory fields** are completed" | OPR ص22 |
| V-MN-12 | Repair Details: Equipment + Store + Cost Center + Item + Quantity قبل الحساب الآلي للقيمة | OPR ص13 |
| V-MN-13 | Cost Analysis: Complaint # + Cost Category + Service Provider (كلها F1) + Amount | OPR ص11 |

## ج) قيود النوافذ الزمنية ⭐

| ID | القيد | النص | المصدر |
|---|---|---|---|
| V-MN-14 | تعيين الورديات — مستقبلي | "The date should be a **future date**" | OPR ص16 |
| V-MN-15 | تعيين الورديات — سقف 31 يوماً | "the date range should be **within 31 days**" | OPR ص16 |
| V-MN-16 | PM — توقع الإنجاز داخل السماحية | "Expected completion date should be **less than or equal to the Lag days**" | OPR ص22 |
| V-MN-17 | قراءة المعدة — ربط زمني | "Date and Time **from when the reading entry begins**" | OPR ص27 |

## د) قيود الانتقاء والربط

| ID | القيد | النص | المصدر |
|---|---|---|---|
| V-MN-18 | مخزن واحد على الأقل | "A **minimum of one store** has to be selected" | SET ص17-18 |
| V-MN-19 | مركز تكلفة واحد على الأقل | "A **minimum of one cost center** has to be selected" | SET ص18-19 |
| V-MN-20 | قراءات مقيدة بالماستر | "readings... **specified in the Equipment Master**... only can be entered" | OPR ص26 |

## هـ) قيود مستنتجة بالنمط (غير حرفية — موسومة 🔶)

| ID | القيد | الأساس |
|---|---|---|
| V-MN-21 🔶 | كود الموقع/الفئة... ممنوع التكرار (نمط F1-list الكودية) | عائلة الماسترات الكودية عبر المشروع |
| V-MN-22 🔶 | Equipment Category اختيار إلزامي عند إنشاء المعدة ("select the equipment category from the list") | OPR ص18 |
| V-MN-23 🔶 | شكوى بلا Room/Location مزدوج معاً (الثنائية Exclusive) | صيغة "Room # **or** the Location Code" |
| V-MN-24 🔶 | الصنف 999999999999 إلزامي الاسم اليدوي | OPR ص13 ("has to be entered manually") |

## و) القيود الغائبة (رصد فجوات — راجع 17)

| الموقف المتوقع | الوثائق تقول؟ |
|---|---|
| كميات سالبة/صفرية في Repair Details؟ | لا قيد موثق |
| تكرار شكوى نفس الغرفة بنفس اللحظة؟ | لا منع تكرار (بل نوع Repeated يعترف بالظاهرة!) |
| Reading خارج Min/Max؟ | **لا تحقق ولا إنذار** (P5) |
| Lead Time سالب في Spares؟ | لا قيد |
| عملة غير معرفة لقيمة المعدة؟ | "relevant currency" بلا قيد مصدر |
| تاريخ تركيب مستقبلي؟ | لا قيد |
