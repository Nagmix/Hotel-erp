# 10 — المعاملات والقيود اليومية (Transactions) — وحدة MNT

> خمسة أنواع معاملات تشغيلية تُنشئ سجلات الأحداث: **الشكوى · Job Order · Action Taken (بتكلفته وإصلاحه) · PM Entry · Reading Entry** + تعيين ورديات. لا شيء منها يولّد قيداً مالياً (راجع 11).

---

## 1. معاملة تسجيل شكوى (Complaint) ⭐

| الحقل | النوع/القيد | المصدر |
|---|---|---|
| Complaint # | **آلي** | OPR ص3 |
| Ref. No | ≤10 ألف-رقمي (مرجع خارجي) | OPR ص3 |
| Room # / Location Code | ثنائية حصرية + F1 | OPR ص3 |
| Department | القسم الرافع | OPR ص3 |
| Complaint Type | Common / **Repeated** | OPR ص3 |
| Complaint (نص) | تفاصيل | OPR ص3 |
| Reported By | المُبلِّغ | OPR ص3 |

- **الأحداث المولَّدة:** حوار طباعة Job Request (ENG#1) — لا شيء آخر موثق (لا إشعار، لا أولوية عند التسجيل! الأولوية تُمنح لاحقاً في Job Order Generation).

## 2. معاملة Job Order ⭐

| العنصر | الوصف | المصدر |
|---|---|---|
| المصدر | انتقاء NO→YES من شبكة **شكاوى أو PM Schedules** في نطاق تاريخ | OPR ص23-24 |
| الأولوية | تُمنح لكل سجل مُنتقى (نقر مزدوج) — **الصف يتلوّن** | OPR ص24 |
| الإسناد | **Employee أو Service Provider (Vendor)** + كود → تفاصيل تظهر | OPR ص25 |
| المطبوع | Job Order (ENG#2) | OPR ص26 |
| الحالة في التقارير | Pending/Closed/All (Job Order Report) | RPL ص21 |

- **لا حقول مهلة/موعد مستهدف داخل Job Order نفسه** (المهلة تعيش في PM Schedule Entry فقط للوقائية؛ والشكاوى بلا SLA إطلاقاً).

## 3. معاملة Action Taken ⭐ (أغنى معاملة)

### 3.1 رأس المعاملة
- التوجيه: **Job Order # / Complaint # / PM Schedule #** (F1 — Job Order Help بمعايير مركبة).
- الشبكة: عمود Action Taken (نص الإجراء) + عمود Status + **Start/End Date & Time**.

### 3.2 Cost Analysis (التكلفة الخارجية/الفئات)
| الحقل | المصدر | ملاحظة |
|---|---|---|
| Complaint # | مرجع | OPR ص11 |
| Cost Category | F1 (ماستر الوحدة) | "additional charges incurred during repair" |
| Service Provider | F1 (UNK-058 المصدر) | مزوّد الخدمة |
| Amount | إدخال يدوي | يظهر في أعمدة الشاشة |

### 3.3 Repair Details (الإصلاح والاستهلاك) ⭐
| الحقل | المصدر | ملاحظة |
|---|---|---|
| Complaint # | مرجع | OPR ص13 |
| Equipment Code | مرجع معدات | — |
| Store Code | من **Engg Stores المعينة** (MGT) | I-MN-01 |
| **Item Code** | F1 من Inventory · **أو 999999999999 (مفتوح: اسم يدوي، بلا أثر مخزني)** | OPR ص13 |
| Cost Center | من Engg Cost Centers (MGT) | I-MN-02 |
| Quantity | إدخال | **القيمة تُحسب آلياً** |

> ⚠️ **لا إذن صرف/حركة مخزنية تُولَّد** من الكمية — راجع 11 §3 و17-P3.

## 4. معاملة PM Schedule Entry

| الحقل | الوصف | المصدر |
|---|---|---|
| PM Schedule # | **آلي بعد اكتمال الإلزامي** | OPR ص22 |
| Equipment Code | F1 | OPR ص22 |
| Start Date | بداية النافذة | OPR ص22 |
| **Must Complete By** | "≤ Lag days" — قيد الصرامة | OPR ص22 |
| Task | نص المهمة | OPR ص22 |
| (التواريخ) | **منتشرة آلياً من الإيقاع** | OPR ص21 |

## 5. معاملة Equipment Reading Entry

| الحقل | الوصف | المصدر |
|---|---|---|
| Equipment Code | F1 (القراءات المعرَّفة فقط) | OPR ص27 |
| Date & Time | "from when the reading entry begins" | OPR ص27 |
| Actual Value(s) | أرقام لكل قراءة معرفة | OPR ص27 |

## 6. معاملة Assign Shifts

| العنصر | الوصف |
|---|---|
| النافذة | From/To **مستقبلي ≤31 يوماً** (OPR ص16) |
| المصفوفة | تواريخ × موظفو Define Employees |
| القيمة | Shift لكل خلية (F1/نقر مزدوج) |
| التسريع | **F2 نسخ خلية · F3 نسخ صف** (OPR ص17) |

## 7. دورة حياة السجلات (المستنتجة)

```
Complaint:      [PENDING] ──(Job Order Gen)──► [ASSIGNED/JS#] ──(Action Taken/Q)──► [WIP] ──► [CLOSED]
PM Schedule:    [DEFINED] ──(Entry)──► [SCHEDULED] ──(Job Order Gen)──► [JS#] ──► [CLOSED]
Equipment:      [ACTIVE] ──(AMC expiry? لا تغيير حالة موثق!)──► [ACTIVE]
Shift Assign.:  [PLANNED ≤31d] ──(تحرير جديد بعد انقضاء النافذة)
```

> **لا فعل مالي واحد** في أي معاملة — أثبت نقاء "العمليات الصرفة": المبالغ في Cost Analysis والقيم المحسوبة في Repair Details **بيانات تحليلية** تعيش داخل MNT وتخرج فقط إلى Spares and Cost Report.
