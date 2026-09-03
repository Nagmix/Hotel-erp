# 02 — التهيئة (Configuration) — وحدة MEM

> وحدة MEM لا تستخدم **مفاتيح INI إطلاقاً** — كل التهيئة عبر 12 ماستر + **عائلة System Attributes بـ13 سمة** (نمط مميز عن FO/POS/BNQ/HRP/MGT). "Only a 'Yes' or 'No' response is accepted... It is advisable to describe these attributes with utmost caution. It is important that the **System Administrator certifies the setting**" (SET ص10).

---

## 1. خريطة التهيئة المنطقية

```
تسلسل التهيئة الموصى به (من تحليل التبعيات):
Facility Codes (E-ME-09)  ←—┐
   ↓                        │ يستدعي
Service Rate Master (E-ME-03) — 3 شرائح × Adult/Children
   ↓                        │
Membership Revenue Codes (E-ME-04: Once/Recurring)
   ↓
Membership Structure (E-ME-05: أسعار Primary/Adult/Child + Currency)
   ↓
Facility Fixed Rates (E-ME-08: 5 أدوار × 5 فترات)
   ↓
Member Categories (E-ME-01) ←— Screening Details (E-ME-02 تربط فئة×بند)
   ↓                        ←— Late Charge Fee (E-ME-11: فئة × بنية ضريبة FO)
Cover Charges (E-ME-10: فئة × فترة × Amount)
   ↓
System Attributes (E-ME-07: 13 سمة — يجب أن تُضبط قبل أي معاملة!)
   ↓
Member UDF (E-ME-12) + Complaints Categories (E-ME-06)
```

## 2. عائلة السمات الثلاث عشرة (SET ص10-12) — الحصر الكامل

| # | السمة | Yes | No | الاعتماد |
|---|---|---|---|---|
| 1 | Membership number is manually entered | رقم العضوية يدوي | **توليد تلقائي** | — |
| 2 | Call Receipt Entry from Corporate Application | استدعاء Revenue/Facility Details **عند SAVE** من طلب شركة | لا استدعاء | عائلة 2-5 |
| 3 | Call Receipt Entry from Corporate Master | استدعاء عند SAVE من Corporate Master | لا | عائلة 2-5 |
| 4 | Call Receipt Entry from Membership Application | استدعاء عند SAVE من طلب عضوية | لا | عائلة 2-5 |
| 5 | Call Receipt Entry from Membership Master | استدعاء عند SAVE من Membership Master | لا | عائلة 2-5 |
| 6 | Receipt number is system generated | رقم إيصال تلقائي في Revenue/Facility | **يدوي** | — |
| 7 | Receipt number is separate for application | **سلسلة منفصلة** للأعضاء والطالبين | سلسلة واحدة | — |
| 8 | Do not allow blacklist members for facilities | المدرجون بالقائمة السوداء **يُمنعون من المرافق** | يسمح لهم | منطق معكوس في الصياغة! |
| 9 | Last name is mandatory | حقل Surname إلزامي في Membership Master | اختياري | شرط لسمة 10 |
| 10 | Use last name for company code generation | كود شركة ACR = حرف الاسم الأخير الأول (مثال MEMC001 من CRAIG) | حرف الاسم الأول | **"This flag is activated only if flag # 9 is activated"** + **"If flag # 10 is activated this flag cannot be de-activated"** (لا رجعة!) |
| 11 | Set default settlement to Company | Service Bill يُسوَّى لحساب Company/Member | لا تسوية تلقائية | — |
| 12 | Link FO to membership | ربط FO — **التاريخ المحاسبي يُجلب تلقائياً** في Service Bill | التاريخ إدخال يدوي | — |
| 13 | Primary Member Validity Checking Required | حقل **UPTO إلزامي** في Membership Master | UPTO يمكن أن يبقى فارغاً | — |

> ⚠️ **نمط فريد:** (أ) عائلة الاستدعاء 2-5 = نفس السلوك من **أربع نقاط حفظ مختلفة** — أبسط شكل لنمط "نقاط استدعاء متعددة"؛ (ب) تبعية 10←9 مع **قفل لا-رجعي** على 10 — أول قيد تهيئة غير قابل للعكس في المشروع (قارن مع Applicable From المستقبلي في FO/POS).

## 3. قواعد التواريخ المستقبلية (Future-Only)

- Service Rate Master: "Date should be **greater than or equal to the current system date**" (SET ص6) — والتعديل: "You can modify a record only if the date in the 'Applicable From' field is **greater than the current date**" (SET ص8).
- Facility Fixed Rates: "The date entered should be **greater than or equal to Current date**" (SET ص12).
- Membership Structure: Application Date بداية السريان.
- Membership Tax Posting: **بدون توثيق** (جسم مفقود).

> **عائلة سادسة للتواريخ المستقبلية** في المشروع (FO/POS/BNQ/MGT/HRP سابقاً) — التعديل مسموح فقط قبل بدء السريان، وهذا نمط إصدار سعر Price-Versioning مبكر.

## 4. التهيئات المحيطة بالوحدات الأخرى

| التهيئة | الوحدة المصدر | الاستخدام في MEM |
|---|---|---|
| Tax Structures | **FO** | Late Charge Fee Definition: "The Description column will display all the Active Tax Structure description available in the **Front office module**" (SET ص15) |
| Currencies + Exchange Rates | النظام العام | Membership Structure والإيصالات ("The Exchange Rate will be displayed automatically") |
| Company/شركة ACR | **AR** | الهدف التلقائي لسمة #10 (MEMC001) |

## 5. أصوات تحذيرية موثقة

- "The data entered will be **lost if the changes are not saved**" (SET ص8) — تحذير فقدان بيانات الأسعار.
- "It is important that the **System Administrator certifies the setting** in this option" (SET ص10) — توصية اعتماد رسمي للسمات.
- منع فك سمة 10 بعد تفعيلها (SET ص11-12 Note).

## 6. إعدادات الفترات (التقويم المالي للوحدة)

أربع عائلات فترات تتكرر عبر الماسترات والمعاملات:
- **Revenue Charges Period**: monthly / quarterly / yearly / half yearly / **none** (MTR ص4)
- **Facility payment periods**: Once / Annual / Half Yearly / Quarterly / Monthly (SET ص12)
- **Cover Charges period**: Monthly / Quarterly / Half year / Annual (SET ص14)
- **Late Fee**: شهري بإزاحة **الشهر السابق** (MTR ص18)

> وحدة MEM **لا تملك إقفالاً/تجميداً موثقاً** (لا يوجد аналог Daily Close/Year End) — الترحيلات الدورية قابلة للإلغاء فقط عبر Cover Process/Cancel و آلية withhold/withdraw في Post Subscription — انظر 13-exceptions §4.
