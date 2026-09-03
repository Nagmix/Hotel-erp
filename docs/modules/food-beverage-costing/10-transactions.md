# 10 — المعاملات (Transactions) — وحدة FNB

> **T-FB-01..14** — معاملات تحليلية **لا مالية** (بلا قيد واحد): دورة الجرد اليومية، الإدخال اليدوي التعويضي (مبيعات/استهلاك منافذ غير محوسبة)، التحويلات الثلاثية، الترحيل اليومي/السنوي، والطلب الآلي العابر للحدود. **كل معاملة "رصيدية" هنا تحليلية التأثير** — تُغيّر أرقام التكلفة في التقارير ولا تلمس GL.

---

## جرد المعاملات الموثقة

| # | المعاملة | الدليل | نوعها | الأثر |
|---|---|---|---|---|
| T-FB-01 | Costing Extraction (Batch) | COP §1 | ETL دفعة | استيراد Sales/Consumption/recipe items من POS+MGT إلى نطاق FNB |
| T-FB-02 | Online Issue Transfer | INI#368 | ETL لحظي | بديل T-FB-01 للأصناف المصروفة |
| T-FB-03 | Kitchen Stock Entry (Physical/Adjustment) | COP §2 | جرد يومي | تسجيل الرصيد الفعلي (أو المستهلك) للمطبخ/الموقع |
| T-FB-04 | Kitchen Opening Stock | COP §3 | تهيئة | أرصدة افتتاحية (Pink مستخرج/Green إدخال) |
| T-FB-05 | Manual Sales Entry | COP §4 | إدخال تعويضي | مبيعات منافذ غير محوسبة (Consolidated/Item Wise · NC KOT!) |
| T-FB-06 | Manual Consumption Entry | COP §5 | إدخال تعويضي | استهلاك خارج قنوات MGT (بكلتا الوحدتين) |
| T-FB-07 | Inter Kitchen Transfer | COP §6 | تحويل كمي | مطبخ→مطبخ (صنف+كمية) |
| T-FB-08 | Inter Cost Transfer | COP §6 | تحويل تصنيفي | نوع تكلفة→نوع (From Cost = To Cost انعكاساً) |
| T-FB-09 | Value Transfer | COP §6 | تحويل قيمي | قيمة إجمالية بين مراكز/مطابخ **بلا أصناف** |
| T-FB-10 | Open/Modifier Mapping | COP §7 | ربط | إسناد أصناف POS المفتوحة/المعدِّلات لمكونات (Store/Sub Recipe) |
| T-FB-11 | Stock Balance Transfer (يومي) | COP §8 | إقفال يومي | Variance حاسوبي/فعلي → رصيد الغد الافتتاحي |
| T-FB-12 | Stock Balance Transfer (سنوي) | COP §8 | إقفال سنوي | ترحيل السنة المالية ← التالية |
| T-FB-13 | Stock Balance Cancel | COP §8 | عكس | إلغاء ترحيل الرصيد |
| T-FB-14 | Auto Indent Creation | COP §9 | **طلب عابر** | POS×وصفة → indent → **MGT** (خالد!) |

## دورة اليوم النموذجية (Composite Day)

```
06:00  T-FB-11 (نتيجة أمس): الرصيد الفعلي أصبح افتتاحي اليوم
07:00  T-FB-02 (أو مساءً T-FB-01): الاستخراج — مبيعات/استهلاك الأمس يدخلان
09:00  T-FB-05/06 (حسب الحاجة): تعويض غير المحوسب
14:00  T-FB-07/08/09: تحويلات المطابخ (بعثات/إعارات)
18:00  T-FB-14: توليد طلب آلي من مبيعات الغد المتوقعة → MGT
23:30  T-FB-03: جرد المطابخ الفعلي
23:45  T-FB-11: ترحيل أرصدة اليوم → افتتاحي الغد
```

## تحليل خصائص المعاملات

### 1. المرجعية
- Reference # (3-10 أبججدي-رقمي) في الجرد/الافتتاحي/التحويلات — **يدوي فريد** بلا ترقيم آلي موثق (مقابل Auto# في MNT Complaints وCare Task!).
- **Doc #** يظهر عند Modify في Kitchen Stock — إذن هناك رقم مستند داخلي، لكن مسار توليده غير موثق.
- Auto Indent بلا ذكر لرقم indent أصلاً (المستلم MGT يرقم؟ — غير موثق).

### 2. القابلية للعكس
| المعاملة | العكس الموثق |
|---|---|
| Kitchen Stock | **Modify بـDoc# + F5 حذف (+Yes)** — مرنة |
| Manual Sales/Consumption | Modify فقط |
| Inter Transfers | ❌ لا عكس موثق |
| Stock Balance Transfer | **Cancel** (شاشة مستقلة!) |
| Auto Indent | **ممنوع نهائياً** (خالد) |
| Kitchen Opening Stock | F5 (سطر) — كامل السجل غير واضح |

### 3. الأثر عبر الحدود
- **T-FB-14 وحدها تعبر**: "created indent can be used in inventory" — الجسر الوحيد الصاعد (FNB→MGT).
- **T-FB-02 عبْرية الاتجاه المعاكس** (MGT→FNB) لكنها ETL لا معاملة مستخدم.
- كل ما عدا ذلك: **أثر داخلي تحليلي** — أرصدة المطابخ وأرقام التقارير فقط (صفر GL — راجع 11).

### 4. السجلات النظامية المصاحبة
- User ID (Start Date فقط) · Last Updated (Start Date) · **لا Authorizer ولا User+Authorizer pair** (مقابل TEL Transfers!) — فقر تدقيق مقارن بنفس عائلة "بلا صلاحيات".
- **لا حالة حالة وثيقة (Status workflow) في أي معاملة** — لا Draft/Approved/Posted: كل شيء يُحفظ نهائياً من أول مرة (عدا قابلية Modify).

### 5. ثنائية العالَمين المخزونيين في كل معاملة رصيدية
- **Stock UOM** (المخزون) مقابل **Conversion UOM** (الصرف) — التعريف الحرفي (COP ص8) وقابلية الإدخال بالوحدتين (COP ص13).
- التقرير المقابل: Physical Stock Variance بأوضاع UOM الثلاث (stock/conversion/both).
