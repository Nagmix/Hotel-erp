# 12 — التكاملات (Integrations) — وحدة MEM

> **I-ME-01..12**: وحدة العضويات عقدة إيراد طرفية — **لا تستهلك بيانات من أي وحدة تشغيلية** (باستثناء بنيات FO الضريبية) و**تغذي AR بخمسة مسارات**. الوحدة الوحيدة التي تربط هوية العضو بحساب AR **آلياً**.

---

## 1. الجسور الموثقة

### I-ME-01: MEM → AR — إنشاء شركة تلقائي (MEMC001) ⭐
"Use last name for company code generation: Yes - The ACR company code has to be created by prefixing... **a company master is automatically created as MEMC001** where 'C' is the first letter of the Surname" (SET ص12).
- **الاتجاه**: MEM → AR عند حفظ Membership Master.
- **المحتوى**: كود شركة ACR جديد لكل عضوية (MEM + حرف + تسلسل).
- **الشروط**: سمة #9 (Surname إلزامي) + سمة #10 مفعلة (ولا رجعة!).
- **الأثر**: العضو يظهر في AR كشركة قابلة للفوترة City-Ledger — الجسر **الوحيد في المشروع** الذي ينشئ كيان AR من هوية طرف داخل وحدة أخرى **تلقائياً** (قارن: Vendor TTT+XXXX في MGT يدوي الأسرة نفسها).

### I-ME-02: MEM → AR — محركات الترحيل الأربعة
"subscription charges are subsequently **posted to the relevant members AR account**" (Subscription ص16) + Facility (ص16) + Cover "post the cover charges of the members to the relevant members AR account" (ص17) + Late "post it to **ACR Module**" (ص18).
- أربع قنوات تحميل شهرية على حساب الشركة (I-ME-01).
- Cover قابل للإلغاء؛ Subscription انتقائي (withhold/withdraw/overwrite).

### I-ME-03: MEM ← FO — بنيات الضرائب
"The Description column will display all the Active Tax Structure description **available in the Front office module**" (SET ص15 — Late Charge Fee Definition) — MEM **تستهلك** تعريف FO الضريبي دون تكراره (نفس عائلة POS/BNQ).

### I-ME-04: MEM ← FO — التاريخ المحاسبي
"Link FO to membership: Yes - The Front Office module will be linked to Membership module. The **Accounting date is picked up by default** in the Service Bill Entry" (SET ص12) — يعني وجود تاريخ محاسبي مركزي في FO تتبعه MEM.

### I-ME-05: MEM × POS — الحدود الصريحة
Service Bill: "used for **non-Food and Beverage (F&B) services only**" (MTR ص7) — F&B محجوز لـ POS. **لا جسر فوترة عضو POS موثق في هذه الأدلة** (GAP-ME-D04 — هل يُخصم من حساب عضو AR عند POS؟ يستدل من POS-side لاحقاً).

### I-ME-06: MEM × BNQ — تشابه بلا جسر (سلبية)
Event Definition (Venue/From-To/Chief Guest) تُغطي حجز قاعات الأعضاء **بمعزل عن BNQ** (MTR ص14-15) — لا توجد إشارة تحقق توفر القاعة أو ربط بالتقويم/Block Reasons — **قناتان متوازيتان لحجز الفعاليات** (GAP-ME-D03 → UNK-046).

### I-ME-07: MEM → البريد الإلكتروني (قناتان)
- "Click [Email] to **email the verification details to the applicant**" (MPF ص18)
- "Click **Send Email to send birthday wishes** to the member by email" + تحديث العنوان بالنقر المزدوج (RPL ص33)
- المزوّد/القناة غير موثقين (GAP-ME-P4).

### I-ME-08: MEM × العملات (نظام عام)
عملات متعددة + Exchange Rates تلقائية في Structure/Receipts (SET ص10/MTR ص3).

### I-ME-09: MEM × SYS — سمات بدل INI
الوحدة لا تستهلك INI keys إطلاقاً — System Attributes داخلي + تقييد القوائم من SYS العام (راجع 07 §2).

### I-ME-10: MEM ← PMS/FO — لا استهلاك مباشر
على خلاف Care (7 قنوات واردة) — وحدة MEM **مكتفية بذاتها بيانياً** (أعضاؤها سجلاتها الخاصة) — لا تقرأ Guests/Folio/Rooms.

### I-ME-11: MEM → التقارير المالية المشتركة (افتراض عائلة ACR)
تقارير Receipt Register/Closing Balance/Due/Control بنفس مصطلحات ACR = التكامل **عبر الاصطلاح** (راجع 08 §4).

### I-ME-12: MEM × HR — لا جسر
لا وظائف/رواتب للموظفين ولا قراءة Personnel — كوادر النادي خارج نطاق الوحدة (HRP تغطي).

## 2. مصفوفة التدفق الكلية

```
                    ┌─── FO ───┐
                    │ Tax Str. │→ (I-ME-03/04) ─┐
                    └──────────┘                │
                                              [MEM]
 POS ←─ (F&B حصراً — I-ME-05 سلبي)           /  |  \
BNQ ∥ (فعاليات متوازية — I-ME-06 سلبي)     /   |   \
                                        AR    Email  Reports
                                    (I-ME-01/02) (I-ME-07) (داخلية)
```

## 3. رتبة الاعتماد/التأثير

| الوحدة | اتجاه | القوة |
|---|---|---|
| AR | MEM → AR | **عالية (خمسة مسارات + إنشاء كيان)** |
| FO | FO → MEM | متوسطة (ضرائب + تاريخ محاسبي) |
| POS | حدود | سلبي-صريح |
| BNQ | توازٍ | سلبي (خطر ازدواج) |
| SYS | عامة | ماسترات + صلاحيات |

> **الخلاصة المعمارية:** MEM هي وحدة **"AR-front لنادي"** — هويتها المالية AR بالكامل، وهويتها التشغيلية ذاتية. في إعادة البناء: A = Customer في Frappe (F-ME-1/9) والمحركات = Scheduled Jobs تُنشئ Sales Invoices (F-ME-3/5/8).
