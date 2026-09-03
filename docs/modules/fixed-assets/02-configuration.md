# 02 — التهيئة والإعدادات (Configuration) — وحدة FXD

> **تهيئة نحيلة بقرارات ثقيلة**: بارامتر واحد (Start Date — بوابة أحادية property-wise) + نِسب الإهلاك المزدوجة (SLM/WDM) + مفتاح INI #475 الذي يقرر المنهج المعتَمد + إشارة INI غير مرقمة تجبر حقول PO/GRR/Bill. **لا Module Attributes · لا System Attributes · لا INIs أخرى** — أصغر ملف تهيئة في وحدة محاسبية.

---

## 1. Fixed Asset Start Date (§1 ص2-4) — ⭐ البوابة الزمنية

| الحقل | الفعل | ملاحظات |
|---|---|---|
| Property Code | اختيار الفندق | "User has to define **property wise** start dates" — بوابة لكل فندق |
| **Start Date (MMYY)** | شهر+سنة بدء التحنيط | "**Once specified, date can't be changed**" — قفل دائم حرفي |
| User | آخر مستخدم | عرض تلقائي |
| Last Updated | وقت الحفظ | عرض تلقائي |

**الدلالات المعمارية الموثقة:**

- "the date from when the fixed asset is **computerised**" — عالم ما قبل التاريخ = "opening balance assets" وDepn. Op. Bal في Master.
- "Any transaction of fixed asset will be **greater than this date**" — حاجز زمني سفلي لكل المعاملات (قاعدة عمل — راجع 05 BR-FX-02).
- غياب أي مسار تعديل/إلغاء (مطابق حرفياً لبوابة FNB Costing Start Date — GAP-FB-P01 يقابلها هنا).

## 2. Depreciation Method — نِسب المنهجين (§7 ص10-11)

**نمط التعريف المزدوج:** لكل (Property × Financial Year × Sub Group أو Asset) تُدخل **نسبتان معاً**:

```
Straight line method: ____ %    (مثال: 10% سنوياً)
Written down method:  ____ %    (مثال: 40% من WDV)
        ↓
المستعمل في الحساب يقرره INI #475 — وليس شاشة النسب!
```

- **المستوى الافتراضي**: Sub Group (double-click من الشاشة الأولى).
- **الاستثناء الفرعي**: زر **detail** → شاشة أصول المجموعة لنِسب أصل-بأصل.
- الفترة: Financial Year عبر **F3** من Financial Year Parameter (FAS) — ربط تهيئي موثق.

> ⚠️ النسب معرفة لـ**سنة مالية بعينها** — ماذا بعد انتهاء السنة؟ لا آلية تجديد/نسخ موثقة (UNK-070 — هل تُعاد النسب كل FY؟).

## 3. مفاتيح INI الموثقة

| المفتاح | الوظيفة | المصدر | الحالة |
|---|---|---|---|
| **#475** | "Fixed assets module will consider either **Straight Line Method or Written Down Method based on the value** of INI switch # 475" | ص2 | قيمه غير موثقة (أي قيمة = أي منهج؟ — UNK-068) |
| **غير مرقم** | حقول PO #, PO date, Grr #, Grr date, Bill #, Bill date: "can be defined as **mandatory**, with **INI switch validation**" | ص9 | رقم المفتاح مجهول (UNK-073) |

> عائلة "بلا INI" (CARE/MEM/SLM/TEL/MNT) تنكسر هنا كما انكسرت في FNB — التراكمي يصبح **35+** (#368 و#511 من FNB + #475 هنا).

## 4. الربط بتهيئة النظام الأوسع

| المعتمد عليه | الاستخدام | المصدر |
|---|---|---|
| Financial Year Parameter (FAS) | F3 في Method + FI Posting + كل التقارير | ص10/16/18 |
| Chart of Accounts (FAS) | الربط الرباعي في Sub Group + 'sub ledger' | ص5 |
| Cost Centers | حقل Sub Group | ص5 |
| Currencies (SYS) | Master/Component/Transaction بأسعار آلية | ص7/12/13 |
| دليل الملكية عبر الوحدات | السؤال المفتوح: أين تُدار "Asset status" وقائمة قيمها؟ | UNK-068 |

## 5. ما ليس له شاشة تهيئة (غيابات بنيوية)

| الغياب | الدلالة |
|---|---|
| لا Module/System Attributes | الوحدة السابعة بلا سمات (بعد CARE/MEM/SLM/TEL/MNT/FNB) |
| لا إعدادات ترحيل منفصلة | الترحيل كله يُشتق من ربط Sub Group — لا Voucher Link ظاهر (هل يمر عبر Voucher Link في FAS-SET؟ [UNCERTAIN] — راجع 11/12) |
| لا حدود دوران أرقام | المسلسل من FIMSHTBL بلا سياسة reset موثقة |
| لا إعدادات Rollback | "The calculated depreciation can be rolled back **with roll back options**" بلا مواصفة (UNK-071) |
