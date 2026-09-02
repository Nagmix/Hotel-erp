# 02 — الإعداد (Configuration) — وحدة ACR

> المرجع: ACR-SET (8 أقسام كاملة) + مفاتيح SYS المذكورة نصاً في ACR-OPR/BIL/RPL. **ACR هي أكثر الوحدات اعتماداً على مفاتيح SYS نسبةً لحجمها** (Module Attributes ×4 + INI ×2 + Pgm IDs).

---

## 1. إعدادات التفعيل والتشغيل

### 1.1 AR Start Date — ACR-SET §1 ص1-2

| القاعدة | النص/الشرح |
|---|---|
| الصيغة | **MMYY** (شهر + سنة) |
| الغرض | "the debtors closing balances and other information can be recorded" — نقطة الصفر الزمنية للذمم |
| **القيد الحاسم** | "You can enter the AR Start Date **only once** and you will **not be allowed to update** the date" — تكوين ذري immutable |
| الأثر اللاحق | أول شهر SOA يُشتق منه آلياً (ACR-OPR §7 ص21) + الافتراضي في تقرير Opening Balance List (ACR-RPL §1 ص3) |

### 1.2 Module Attributes الخاصة بـ ACR (SYS)

| # | الاسم النصي | القيم والسلوك | المصدر |
|---|---|---|---|
| **1** | Require Receipt Number Generation for Credit Entries | Yes: رقم الإيصال **يولَّد آلياً** / No: **إدخال يدوي لرقم فريد** | ACR-OPR §1 ص5 |
| **2** | Require Bill Selection for ACR Invoice Printing | Yes: **شركة واحدة** + نطاق فواتيرها / No: **نطاق شركات** + كل الفواتير تُطبع تتابعياً | ACR-BIL §2 ص4 |
| **3** | Require Audit trail for Transactions | Yes: كل Modify/Delete في Transaction Entry يُخزَّن في **ACR Audit Table** (نسخة Old/New أو Del) / No: لا تتبّع — **وإلزامي = YES قبل إدخال قيود/افتتاحيات** (ذكران: ص3 SET + ص20 RPL) | ACR-RPL §11 ص20 + ACR-SET §2 ص3 |
| **6** | Activate Invoice Matching | No: الإيصال يُرحَّل **مباشرة** على فاتورة (تحديد Bill #) / Yes (else): تسجيل **unallocated** ثم المطابقة لاحقاً عبر Match Bills–Receipts | ACR-OPR §1 ص4 |

### 1.3 INI Switches الخاصة بـ ACR (Base Default File — SYS)

| # | الاسم | **منطق معكوس!** | الافتراضي | المصدر |
|---|---|---|---|---|
| **56** | `ACR2FAS` | **0 = الرابط ممكَّن** / 1 = معطَّل — "set setting # 56 'ACR2FAS' To 0, which indicates the Link has been **enabled**" | **1 (معطَّل)** | ACR-OPR §1 ص10 |
| **74** | `ACRALLOWUPDATION` | **0 = يسمح** بتعديل Company Name/Branch **بعد طباعة الفاتورة** / 1 = يمنع | 0 (يسمح) | ACR-OPR §1 ص10 |

> ⚠️ **قرار تصميمي للنظام المستهدف:** هذه منطقة "ألغام" معرفية — أي فريق ينقل الإعدادات حرفياً سيقلب المعنى. يُقترح في المعمارية الجديدة اعتماد دلالات إيجابية صريحة (`enable_ar_to_gl_link = true`).

### 1.4 شرط الترحيل المحاسبي (AR→FAS) — ACR-OPR §1 ص10

متطلبان معاً:
1. **تعريف الحسابات** في "Link AR to Finance" تحت FAS-SET §11: Account Codes لـ **Sundry Debtors, Cash, Bank, Commission**.
2. **INI #56 = 0** (تمكين الرابط — انظر أعلاه).

النتيجة: "while saving the entries in Transaction Entry... the **FA Transaction screen is displayed** and you are required to post the transaction to proper account codes" — الترحيل **تفاعلي عند الحفظ** (وليس دفعات مجمّعة مثل FO/POS).

## 2. إعدادات التشغيل

### 2.1 Specify Aging — راجع `01-master-data.md` §3 للبنية الكاملة

| البند | القيمة |
|---|---|
| الوصول | Setup → Specify Aging |
| النوع | Receivable |
| الفترات | To فقط؛ From آلي؛ From الابتدائي = 0 |
| الفائدة | 4 معايير نظامية لكل فترة |
| الحماية | التاريخ ≥ تاريخ اليوم |

### 2.2 AR User Access — ACR-SET §4 ص9-10

| البند | الوصف |
|---|---|
| النموذج | مصفوفة **مستخدم × نوع قيد** |
| أنواع القيود الأربعة | **Debit · Credit · Adjustment · Post (Online Bill wise Receipt posting)** — "allow or restrict user access to transaction types... in the Transaction Entry menu option" |
| الافتراضي | **No** (ممنوع) لكل المستخدمين — نمط deny-by-default |
| التعديل | Double-click/Enter على الصف للتبديل |

### 2.3 User Defined Print Forms — ACR-SET §6 ص17

- تخصيص نماذج: **invoices, reminders, payment receipts, balance confirmation letters** — عمودية العرض وأبعاد الصفحة.
- **لا تُعرَّف هنا** — مرجع دائري إلى "User Defined Print Forms in **Getting Started document**" (وثيقة عامة خارج حزمة 65 PDF؟ `[NOT DOCUMENTED]` في المجموعة الحالية — راجع `17-gap-analysis.md` GAP-AR-D02).

### 2.4 Purge ACR Audit Table — ACR-SET §7 ص17-18

| القاعدة | النص |
|---|---|
| الحد الأدنى | "cut-off days... should not be less than **60 days**" |
| قبل التنفيذ | "All related reports have to be generated prior to purging" |
| أثناء التنفيذ | "**No daily entries to be made during purging**" — نافذة صيانة |

### 2.5 Print Form Designer — ACR-SET §8 ص19

قسم عنواني في الدليل (بلا متن موثق في هذه الصفحة — راجع Getting Started/SYS). `[NOT DOCUMENTED]`

### 2.6 Pgm ID for Print Forms (شرط طباعة!) — ACR-BIL §1 ص2

> "To print an invoice statement it is **mandatory to define the print program ID** in the 'Pgm ID for Print Forms' option under **System Setup** module **without which the statement will not be printed**"

قيد تكامل حاسم: طباعة كشوف الفواتير الشهرية تفشل صمتاً إن لم يُعرَّف Pgm ID مسبقاً في SYS.

## 3. خريطة التكوين الكاملة (مصفوفة القراءة السريعة)

| الإعداد | النوع | القيمة/النطاق | أين يُستهلك | قابلية التغيير لاحقاً |
|---|---|---|---|---|
| AR Start Date | تكوين ذري | MMYY | SOA الأولى + تقارير الافتتاح | ❌ أبداً |
| Module Attribute 1 | مفتاح | Yes/No | توليد رقم الإيصال | ✔ |
| Module Attribute 2 | مفتاح | Yes/No | نطاق طباعة الفواتير | ✔ |
| Module Attribute 3 | مفتاح | Yes/No | Audit Trail (شرط ما قبل الإدخال) | ✔ (بحذر) |
| Module Attribute 6 | مفتاح | Yes/No | نمط المطابقة (مباشر/مؤجل) | ✔ |
| INI 56 | مفتاح | 0/1 (**معكوس**) | رابط AR→FAS | ✔ |
| INI 74 | مفتاح | 0/1 | تعديل بعد الطباعة | ✔ |
| Specify Aging | بيانات | فترات + فائدة | تقارير AR + FAS | ✔ (بشرط تاريخ ≥ اليوم) |
| AR User Access | صلاحيات | مستخدم × 4 أنواع | Transaction Entry | ✔ |
| Link AR to Finance | تكامل | 4 حسابات (FAS-SET §11) | الترحيل عند الحفظ | ✔ |
| Pgm ID for Print Forms | تكامل | SYS | طباعة BIL | ✔ إلزامي قبل الطباعة |
| Purge Cutoff | صيانة | ≥ 60 يوم | جدول التدقيق | ✔ |
