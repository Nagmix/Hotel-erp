# 06 — التحققات (Validations) — وحدة ACR

> V-AR-01..24 مع نوع كل تحقق (Prevent = يمنع الحفظ / Warn = تنبيه / System = سلوك نظامي آلي) ورسائله/آثاره الموثقة.

---

## 1. تحققات القيود والإدخال

| ID | القاعدة | النوع | الرسالة/الأثر الموثق | المصدر |
|---|---|---|---|---|
| V-AR-01 | Bill Date ≤ Current System Date | **Prevent** | رفض الإدخال | ACR-OPR §1 ص3 |
| V-AR-02 | Exchange Rate حقل للقراءة (من Exchange Entry) | System | يُعرض ولا يُحرَّر | ACR-OPR §1 ص3 |
| V-AR-03 | Value = Amount × XRate آلياً للعملة الأجنبية | System | احتساب آلي | ACR-OPR §1 ص3 |
| V-AR-04 | تفاصيل البطاقة (Type/CC#/Auth#) إلزامية لمدفوعات البطاقة | **Prevent** | إلزام موثق ("it is mandatory to specify") | ACR-OPR §1 ص3 |
| V-AR-05 | Description ≤ 100 خانة alphanumeric | **Prevent** | حد الحقل | ACR-OPR §1 ص3 |
| V-AR-06 | Doc # آلي بعد الحفظ (لا إدخال يدوي) | System | توليد آلي | ACR-OPR §1 ص2 |
| V-AR-07 | Receipt # فريد يدوياً (إذا Attr#1=No) | **Prevent** | "manually enter a **unique** number" | ACR-OPR §1 ص5 |

## 2. تحققات الائتمان والحدود

| ID | القاعدة | النوع | الأثر | المصدر |
|---|---|---|---|---|
| V-AR-08 | تجاوز Credit Limit (الفاتورة الحالية + المدين) | **Prevent عبر الوحدات** | **منع تسوية FD/POS/BQT أو الترحيل اليدوي** | ACR-SET §5 ص14 |
| V-AR-09 | Allow Credit=Yes ⇒ Credit Days مطلوب | **Prevent** | إلزام شرطي | ACR-SET §5 ص13 |
| V-AR-10 | Black List=Yes ⇒ السبب + المجيز مطلوبان | **Prevent** | شاشة إلزامية | ACR-SET §5 ص12 |

## 3. تحققات المطابقة والصرف

| ID | القاعدة | النوع | الأثر | المصدر |
|---|---|---|---|---|
| V-AR-11 | Match Bills: إيصال واحد لكل عملية | System | "only one receipt at a time" | ACR-OPR §2 ص11 |
| V-AR-12 | Adjusted Amount قابل للتحرير ضمن المعلق | System | توزيع حر متعدد الفواتير | ACR-OPR §2 ص11 |
| V-AR-13 | السداد > إجمالي المعلق ⇒ استفتاء توليد إيصال بالفارق | **Warn (Yes/No)** | رسالة خيار | ACR-OPR §1 ص7 |
| V-AR-14 | الفارق بعد المطابقة يظل unallocated | System | حمل لاحق | ACR-OPR §2 ص11 |
| V-AR-15 | سعر صرف التسوية = **سعر تاريخ الفاتورة** | System | منع Book Profit/Loss | ACR-OPR §1 ص6 |
| V-AR-16 | سعر صرف التعديل = سعر تاريخ التعديل | System | استثناء صريح | ACR-OPR §1 ص8 |

## 4. تحققات التعديلات (Adjustments)

| ID | القاعدة | النوع | الأثر | المصدر |
|---|---|---|---|---|
| V-AR-17 | التعديل على فاتورة موجودة حصراً (F1) | **Prevent** | "only on existing bills" | ACR-OPR §1 ص7 |
| V-AR-18 | لا Commission على التعديلات | **Prevent** | قيد صريح | ACR-OPR §1 ص8 |
| V-AR-19 | التعديل يُدمج مع الفاتورة كسجل واحد (JV D/C) | System | تمثيل موحَّد | ACR-OPR §1 ص8 |

## 5. تحققات القفل والإقفال

| ID | القاعدة | النوع | الأثر | المصدر |
|---|---|---|---|---|
| V-AR-20 | فاتورة مطبوعة ⇒ لا تعديل (إلا Company Name/Branch بـ INI #74=0) | **Prevent** | قفل مستندي | ACR-OPR §1 ص10 |
| V-AR-21 | SOA معالجة ⇒ لا إضافة/تعديل/حذف للشهر | **Prevent** | قفل شهري | ACR-OPR §7 ص20 |
| V-AR-22 | SOA متسلسلة — الشهر غير قابل للتحرير | System | عرض آلي للشهر التالي | ACR-OPR §7 ص21 |
| V-AR-23 | SOA مطلوبة لتعديل افتتاحيات شهر البداية: Rollback أولاً | **Prevent** | قيد Rollback | ACR-SET §2 ص3 |
| V-AR-24 | Credit Card Register: From/To **ضمن الشهر نفسه** | **Prevent** | "should be within the same month" | ACR-RPL §8 ص14 |
| V-AR-25 | Browse Transactions: الشهور **ضمن السنة المالية نفسها** | **Prevent** | "should lie within the same financial year" | ACR-RPL §20 ص31 |

## 6. تحققات الأمان والصيانة

| ID | القاعدة | النوع | الأثر | المصدر |
|---|---|---|---|---|
| V-AR-26 | AR User Access: الافتراضي **No** لكل الأنواع (deny-by-default) | System | مصفوفة المستخدم×النوع | ACR-SET §4 ص10 |
| V-AR-27 | Purge Cutoff ≥ 60 يوماً | **Prevent** | حد أدنى نظامي | ACR-SET §7 ص18 |
| V-AR-28 | Purge أثناء التشغيل: منع الإدخال اليومي | **Prevent (إجرائي)** | نافذة صيانة | ACR-SET §7 ص18 |
| V-AR-29 | Aging date ≥ تاريخ اليوم | **Prevent** | تفعيل التعريف | ACR-SET §3 ص8-9 |
| V-AR-30 | Monthly Invoice Statement بلا Pgm ID في SYS | **Prevent (صامت)** | "statement will not be printed" | ACR-BIL §1 ص2 |

## 7. مصفوفة الرسائل/الاستجابات الموثقة نصاً

| الموقف | استجابة النظام | المصدر |
|---|---|---|
| حفظ قيد ناجح | "You will get a message that the transaction was saved successfully" | ACR-OPR §1 ص7 |
| سداد > معلق | حوار Yes/No لإيصال الفارق | ACR-OPR §1 ص7 |
| فاتورة مطبوعة وتعديل مطلوب | منع (مع ثغرة INI #74 للاسم/الفرع) | ACR-OPR §1 ص10 |
| تطابق النتيجة | عمود الحالة يتغير إلى **Y** (Settled) | ACR-OPR §1 ص6 |
| Untag | عمود UnTag: No→YES | ACR-OPR §6 ص19 |

> **ملاحظة تحققية:** لا توجد تحققات موثقة لمطابقة إجمالي المبالغ (tally) كما في FO — المطابقة هنا بمبالغ Adjusted حرة قابلة للتحرير ضمن سقف المعلق. `[NOT DOCUMENTED]` سلوك تجاوز Adjusted > Outstanding.
