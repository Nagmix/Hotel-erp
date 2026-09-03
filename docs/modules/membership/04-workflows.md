# 04 — سير العمل (Workflows) — وحدة MEM

> **WF-ME-01..15**: قلب الوحدة **دورة الانضمام الرباعية المراحل** (WF-ME-02..05) و**الدورة المالية الشهرية الرباعية** (WF-ME-11..14) و**عائلة الإنهاء المتتالية** (WF-ME-07).

---

## WF-ME-01: تهيئة الوحدة (One-time)
```
[E-ME-09] Facility Codes → [E-ME-03] Service Rate Master (3 شرائح)
 → [E-ME-04] Revenue Codes (Once/Recurring) → [E-ME-05] Structure (لكل فئة + عملة)
 → [E-ME-08] Fixed Rates → [E-ME-01] Member Categories (عائلة/مرشحون/مدة)
 → [E-ME-02] Screening Details (فئة × بند + Mandatory) → [E-ME-11] Late Fee (بنية ضريبة FO)
 → [E-ME-10] Cover Charges → [E-ME-07] System Attributes (13 سمة — اعتماد مدير النظام!)
 → [E-ME-12] UDF + [E-ME-06] Complaints Categories
```

## WF-ME-02: الانضمام — الطلب
```
Corporate: Category → Add → Reference# + Validity + Organization + Financial Parameters
           (Net Worth/Turnover×2/Net Profit/IT PA#) → Address (Register/Local/Mailing+نسخ) 
           → References (Membership# لو مُحيل عضو) → Save → توليد Application#
Individual: Category → Add → 4 تبويبات (Address/Work/Birth/Other[CC+Bank+Vehicle])
           → Spouse (عام+عمل+أخرى+صورة+توقيع) → Children → Save
[سمات 2/4 مفعلة → استدعاء Revenue/Facility Entry فور SAVE!]
```

## WF-ME-03: الانضمام — الفحص
```
Application Screening → Member/Corporate + Application# (F1)
 → عرض قائمة فحص الفئة (verified/accepted checkboxes من E-ME-02)
 → Remarks → Interview Required؟
    ├─ No  → [WF-ME-05] مباشرة
    └─ Yes → [WF-ME-04]
 → (زر بريد: إرسال تفاصيل التحقق للطالب)
 → More Details: مراجعة Reference/Personal/Address/Work/Other
```

## WF-ME-04: الانضمام — المقابلة
```
Assign Interview Dates → Application# → Date/Time/Person/Remarks → Save
 → إجراء المقابلة → Interview Details → Status:
    ├─ Considered → [WF-ME-05]
    ├─ Rejected   → نهاية (التقرير Pending Applications يرصد بقاءه)
    └─ Cancelled  → إعادة جدولة أو نهاية
```

## WF-ME-05: الانضمام — التحويل إلى عضوية ⭐
```
فرد/مرشح غير مؤسسي:
 Transfer Membership Application → Application# → Member Info → تحويل
  → تبويبات الطلب مرة أخرى (تثبيت) → [Credit Limit Details: Allow Credit Y/N + Limit] → Save
شركة/مرشح مؤسسي:
 Transfer Corporate Application → Application# → Corporate Info → تحويل
  → Category + Validity (From/UP TO/Renewal — إلزامي!) → Save
  → [Membership Receipt Entry تُستدعى تلقائياً] → تحصيل رسوم الانضمام → Save
[سمة #10 مفعلة → شركة ACR تُنشأ تلقائياً (MEMC001) عند حفظ Master]
```

## WF-ME-06: الإدخال المباشر (بلا دورة انضمام)
```
Corporate/Membership Master → Category → Add → التفاصيل كاملة (نفس بنية الطلب)
 → Credit Limit → Save → [MEMC001 تلقائي + سمة 5 تستدعي الإيصال]
```

## WF-ME-07: عائلة الإنهاء الأربعة (نمط موحد)
```
Blacklist / Termination / Resignation / Deceased:
 Membership# (F1) → عرض Name/Category + قائمة أفراد العضوية
 → Double-click عمود الحالة للفرد المطلوب (Yes/No)
 → Authorized Person + Reason (+ Cause of Death للوفاة)
 → Save
 [تتالٍ هابط: إصابة Primary تلقياً تُصيب spouse+children+additional؛ إصابة فرد لا تُصيب Primary]
 [الوفاة فقط: Primary متوفٍ → شاشة خلافة: اختيار بديل من العائلة أو None (إزالة الجميع!)]
 [الاسترجاع: نفس الشاشة بخيار Revoke المقابل لكل نوع]
```

## WF-ME-08: التجديد
```
Renewal Entry → Corporate/Individual → Membership# (F1)
 → عرض صلاحية العضوية → تاريخ التجديد الجديد (UPTO) + Remarks → Save
 → (Member More Info للتفاصيل) → [رسمياً: إيصال التجديد عبر Membership Receipt Entry]
```

## WF-ME-09: نقل الفئة + تغيير العنوان
```
Category Transfer: Membership# → Old Category (تلقائي) → New Category + Remarks
   → (يربط بشاشة الطلب/Credit Limit)
Address Change: Membership# → Address Type (Residential/Work/Abroad)
   → تعديل → وسم mailing → Save
```

## WF-ME-10: الفوترة الخدمية اليومية (Service Bill)
```
Service Bill Entry → Acc.Date (تلقائي لو سمة #12) → Service Type → Confirm
 → Membership/Affiliated Billing → Membership#/Affiliated# (F1)
 → Service Code (من Rate Master) + عدد بالغين/أطفال (السعر تلقائي من الماستر)
 → Discount (NONE/AMOUNT/PERCENTAGE + Reason) → جدول الفواتير
 → Settlement: [سمة #11: تسوية Company/Member تلقائية] أو أزرار أخرى:
    ├─ AR (ترحيل لحساب العضو)
    ├─ CASH
    ├─ CREDIT CARD (Type + Company + Card# + Authorization)
    └─ CHEQUE (# + Date + Bank + Branch)
 [سمة #8: العضو المدرج بالقائمة السوداء يُمنع من المرافق قبل البدء!]
```

## WF-ME-11: الدورة الشهرية — الاشتراكات
```
Process Subscription → From/To → حساب أسعار كل عضو من الماسترات
 → Post Subscription to AR → عرض قائمة الأعضاء + checkboxes
   (الكل افتراضياً — إلغاء اختيار = withhold؛ آلية withdraw/overwrite متاحة)
 → Save → ترحيل لحسابات AR للأعضاء المختارين
```

## WF-ME-12: الدورة الشهرية — رسوم المرافق
```
Process Facility Charges → From/To (From ≤ اليوم) → حساب → ترحيل AR
 [المصدر: وسوم Revenue/Facility Entry + Fixed Rates]
```

## WF-ME-13: الدورة الشهرية — رسوم Cover
```
Cover Charges Posting → Process (أو Cancel!) → Month/Year → تنفيذ
 [المصدر: Cover Charges Setup + Senior Citizen Exemption + Adjustment Debit]
 [الإلغاء: نفس الشاشة بخيار Cancel لنفس الشهر]
```

## WF-ME-14: الدورة الشهرية — رسوم التأخير ⭐
```
Posting Late Charges → Late Fee Posting Month (مثال: January-2011)
 → النظام يحسب رصيد كل عضو كما في **آخر يوم من الشهر السابق (December-2010)**
 → الرصيد Debit (مدين)؟ → احتساب Late fee وفق بنية الفئة (بنية ضريبة FO)
 → Post Transaction → الترحيل إلى ACR
 [دليل رقمي موثق حرفياً — MTR ص18]
```

## WF-ME-15: الشكاوى والفعاليات
```
Register Complaints → من عضو/ضد عضو → Nature + Priority + Assigned To → Save
 → Attend Complaints → اختيار → Action By + Remarks → إغلاق
Event Definition → Membership# → وصف + Venue + From/To(DateTime) + Contact
 + Chief Guest → Save
```

> **الرسم الكلي:** الدورة الشهرية (WF-ME-11→14) = "الإقفال الدوري" الخاص بالوحدة — بلا شاشة إقفال موحدة، أربع محركات مستقلة تعمل بالتتابع، وكلٌّ يرحّل مباشرة إلى AR (راجع 11-accounting-impact).
