# 04 — سير العمليات (Workflows) — وحدة MNT

> **WF-MN-01..13** — أربعة أنهار رئيسية (الشكوى · الوقائية · القراءات · الورديات) تتقاطع عند **جهاز الإسناد المشرفي (Job Order Generation)** وتصب جميعها في Action Taken ثم التقارير. الوحدة نموذج "الأحداث تُولَّد والإشراف يوجه".

---

## WF-MN-01: دورة حياة الشكوى (Complaint) ⭐

```
[أي قسم] Register Complaints
   رقم آلي · Ref No (10) · Room أو Location (F1) · Department
   · نوع Common/Repeated · تفاصيل · Reported By
        │ Save
        ▼
   حوار طباعة Job Request؟ (Yes/No — بوابـة ENG#1='YES')
        │
        ▼
(شكوى PENDING في القائمة) ──► [WF-MN-06] Job Order Generation
        │
        ▼
   Action Taken (مسار Complaint # / Job Order #)
   ├── نص الإجراء (نقر مزدوج)
   ├── Status: Pending → WIP → Closed (نقر مزدوج)
   ├── Start/End Date+Time
   ├── Cost Analysis (فئة+مزوّد+مبلغ)          [WF-MN-07]
   └── Repair Details (معدة+مخزن+صنف+مركز+كمية) [WF-MN-08]
        │ Save
        ▼
   التقارير: Complaints List · Status (Q) · Resolution Time · Employee Wise
```

- **قواعد العبور:** الترقيم آلي؛ الحالة تُغيَّر من مسارين (Action Taken أو Complaint Status Q)؛ **لا مسار موثق للعودة بعد Closed** (لا إعادة فتح! — راجع 17-P6).
- نوع **Repeated** يُسجَّل عند الدخول فقط — لا يغيّر أي مسار لاحق موثق.

## WF-MN-02: دورة الصيانة الوقائية (PM) ⭐

```
Equipment Master (معدة + AMC + Spares + Standard Readings + Remarks)
        │
        ▼
PM Schedule Master
   Equipment (F1) · Service Provider (F1)
   · صفوف: Service Type + Service Rhythm + AMC Y/N (آلي من المعدة!)
   · Start Date + Lag (أيام السماح) + Task
        │ (تعديل موثق قبل/بعد الحفظ عبر Modify)
        ▼
PM Schedule Entry
   PM# آلي بعد اكتمال الإلزامي
   · Start Date · Must Complete By (≤ Lag!) · Task
   · "The dates are automatically calculated based on the frequency"
        │
        ▼
[WF-MN-06] Job Order Generation (اختيار PM Schedules + نطاق تاريخ)
        │
        ▼
Action Taken (مسار PM Schedule #) → إغلاق بتكلفة تحليلية
        │
        ▼
التقارير: PM Schedule List · Action Taken Report · Job Order Report
```

- **القلب الحسابي:** Rhythm (أيام) → توليد التواريخ آلياً؛ وLag يحدد نافذة "Must Complete By" — **قيد الصرامة الوحيد في الجدولة**.
- AMC ينساب: معدة → PM Master (auto populate) — بلا أي تنبيه انتهاء موثق (GAP-MN-P2).

## WF-MN-03: دورة القراءات (Equipment Readings)

```
Equipment Master → Standard Readings (Min/Max + UOM)
        │ (يعرّف أي قراءات مسموحة للمعدة)
        ▼
Equipment Reading Entry
   Equipment (F1) · Date+Time (منه يبدأ الرصد) · Actual Value
        │ Save
        ▼
Equipment Readings List (نطاق تاريخ)
```

- **قيد النافذة:** قراءة لا يعرفها الماستر **لا تُقبل** حرفياً.
- **لا إنذار تجاوز** Min/Max في أي ملف — القراءة أرشيف قياس لا بوابة إنذار (GAP-MN-P5 — فرصة أتمتة ذهبية).

## WF-MN-04: دورة الورديات (Roster)

```
Define Shifts (أوقات+ترتيب) + Define Employees (مهارات)
        │
        ▼
Assign Shifts
   From/To (مستقبلي، ≤31 يوماً) → Enter
   → شبكة تواريخ × موظفين
   → لكل خلية: Shift (نقر مزدوج/F1)
   → F2 نسخ الخلية السابقة · F3 نسخ الصف السابق
        │ Save
        ▼
Duty Chart (تقرير الروزنامة)
```

- **عائلة القيود الزمنية:** مستقبلي فقط + أقصى 31 يوماً — أبسط نافذة تخطيط في المشروع مقابل روزنامة HRP الكاملة (روستَر مصغّر).

## WF-MN-05: تهيئة الوحدة (One-time)

```
SYS: تعريف ENG Attributes (#1/#2)
MGT: Store code Definition + cost center code Definition (Customize)
        │
        ▼
MNT Setup: 9 ماسترات كودية → موظفو هندسة → أولويات ملونة
   → Identify Engg Stores (checkbox ≥1) → Identify Engg Cost Center (≥1)
        │
        ▼
UDFP: تصميم نماذج Job Request/Job Order (اختياري لكن عملياً ضروري للورق)
```

## WF-MN-06: جهاز الإسناد المشرفي (Job Order Generation) ⭐

``
[Supervisory User] اختيار المصدر: Complaint أو PM Schedules + نطاق تاريخ
        │
        ▼
شبكة المرشحين: Select = NO → (نقر مزدوج) → YES   [BR-MN-10]
        │ Generate
        ▼
شاشة الأولويات: Priority (نقر مزدوج) → مستوى
   → الصف يتلوّن بلون الأولوية فوراً                [BR-MN-11]
        │
        ▼
الإسناد: Employee أو Service Provider (Vendor) + كود
   → "respective details appear on the screen"
        │
        ▼
حوار طباعة Job Order؟ (بوابة ENG#2='YES')
```

- **المبدأ الموثق:** "prioritize and allocate the complaints/PM Tasks to different employees **based on their skills and availability**" — لكن **لا منطق اقتراح آلي موثق** (المهارة والتوافر معرفة المشرف بالعين — راجع 17-P4).
- اختيار Vendor = مسار **الإسناد الخارجي** (التعاقد من الباطن) الوحيد الموثق في الوحدة.

## WF-MN-07: التقاط التكلفة التحليلية (Cost Analysis)

```
Action Taken → Cost Analysis
   Complaint # + Cost Category (F1) + Service Provider (F1) + Amount
   → "The details appear on the respective columns"
        │
        ▼
Spares and Cost Report (تكلفة قطع + تكاليف أخرى لكل شكوى/PM)
```

- **لا ترحيل لأي دفتر** — الرقم يعيش هنا ويُقرأ في التقارير فقط (راجع 11).

## WF-MN-08: تفاصيل الإصلاح والاستهلاك (Repair Details)

```
Action Taken → Repair Details
   Complaint # + Equipment Code + Store Code + Cost Center
   + Item Code (F1 من Inventory) أو 999999999999 (صنف مفتوح)
       ├── صنف مفتوح → اسم يدوي + "will not affect Inventory stores"
       └── صنف مخزني → Quantity → "value will be auto calculated"
        │ Save
        ▼
Spares and Cost Report / Equipment Details List
```

- **⚠️ الفجوة الكبرى:** لا **إذن صرف مخزني** (Material Issue) يوثق خصم الكمية من رصيد MGT — راجع 17-P3 (أخطر فجوة عملية في الوحدة).

## WF-MN-09: تعديل الحالة من الاستعلام (Complaint Status Q)

```
اختيار Pending/WIP/Closed → قائمة → نقر مزدوج على سجل
   → Complaint Information (تفاصيل)
   → تغيير Status + إدخال Action Taken + اختيار Priority
        │ Save → رسالة تأكيد
```

- **"استعلام يحرّر"**: الوحيدة في المشروع بعد TEL Error View التي تسمح **بتعديل حالة من شاشة تقرير** — نمط Query-as-Console (راجع 15 §3).

## WF-MN-10: طباعة مستندات العمل (Print Engine)

```
Job/Complaint Print Engine
   ├── Complaint → بالرقم أو نطاق تاريخ
   └── Job Order → (Complaint أو PMS) + (بJS# أو بتاريخ)
        + اختيار Printer → Ok
   "The print format is based on the user specifications" → UDPF
```

## WF-MN-11: إعادة طباعة الطلب الأولي

- Job Request يُطبع **فور التسجيل فقط** (حوار ENG#1) — لا مسار إعادة طباعة موثق له؛ بديله العملي: Print Engine (بمخرجات Job Order/Complaint).

## WF-MN-12: تصميم نموذج طباعة (UDPF)

```
New Project → Module/Restaurant → Program Type → Printer Type
   → Description → Save → Make Project Active
   → Tool Box (اختيار حقول بنقر مزدوج + سحب)
   → F4 (خصائص الحقل: Line/Left/Width/Align/PrintFrom-To/LastPage)
   → Body Details (F4: TopLine/Left/Rows/Columns) + F3 (عرض عمود/Bold)
   → Logo (نقر يمين: Caption/Width/Height/Picture)
   → Page Layout (Header/Footer rows — 6 rows = 1 inch)
   → Match Samples (معايرة) → Print Preview → Print
```

## WF-MN-13: تصدير البارامترات العابر للوحدات (Parameter Listing)

```
"Select the Parameter" → "The details are displayed in the form of MS-Excel reports"
```

- تقرير **عابر للوحدات يسكن MNT**: يقرأ "all the parameters defined by the user in **various modules**" — أداة تدقيق تكوين شاملة بمخرج Excel (راجع 08 §15 و12 §7) — نطاقه الدقيق UNK-062.

---

## مصفوفة تدفق الحالات (المستنتجة من التقارير)

| الحالة | الوصول إليها | الدلالة في التقارير |
|---|---|---|
| Pending | افتراضية بعد التسجيل (تقرير 1/3/5/11) | غير مسندة/قيد الانتظار |
| WIP | تغيير يدوي (Action Taken أو Q) | جارية |
| Closed | تغيير يدوي بالمثل | منجزة (مذكورة صراحة في 3 و11) |

> ⚠️ قائمة الحالات الثلاث مستنتجة من فلاتر التقارير (لا لقطة نصية لخيارات عمود Status في Action Taken — **UNK-059**: هل حالة رابعة كـ"Registered" موجودة؟).
