# 10 — المعاملات ودورات الحياة (Transactions) — وحدة ACR

> كتالوج المستندات وحالاتها والانتقالات الموثقة. **AR = أغنى وحدة في حالات القفل والإلغاء العكسي** (Untag/Cancel/Reprint/Rollback/Outstanding Update).

---

## 1. سلسلة مستندات الوحدة

| المستند | المولِّد | الترقيم | المصدر |
|---|---|---|---|
| **AR Transaction (Debit)** | Transaction Entry يدوي + **تلقائي من FO/POS/BQT/MEM** | Doc # آلي | ACR-OPR §1 ص2-4 |
| **AR Receipt (Credit)** | Transaction Entry (مطابَق أو unallocated) | Receipt # آلي (Attr#1=Yes) أو يدوي فريد | ACR-OPR §1 ص4-5 |
| **Adjustment** | Transaction Entry (على فاتورة قائمة) | Adjustment # يدوي | ACR-OPR §1 ص7-8 |
| **Opening Balance Entry** | AR Opening Balance (Debit/Credit/Adjustment) | Doc # آلي بعد الحفظ | ACR-SET §2 ص4 |
| **Invoice** | Print Invoice (BIL) | **Invoice #** (نطاقات) | ACR-BIL §2 |
| **Reminder** | Print Invoice/Reminder | بصيغة معرفة مسبقاً | ACR-BIL §2 ص5 |
| **Receipt Voucher** | Print Receipt (BIL) | بمدى أرقام الإيصالات | ACR-BIL §3 |
| **SOA** | Statement of Accounts | الشهر MMYY (متسلسل) | ACR-OPR §7 |
| **Balance Confirmation Letter** | Balance Confirmation AR | مرجع نصي/رقمي حر | ACR-BIL §4 |
| **Follow-Up Record** | Debtors Follow-Up | نشاط + موعد تالٍ | ACR-CRT ص3 |
| **CC Consolidation Group** | Credit Card Consolidation | **رقم مجموعة يدوي** في عمود Option | ACR-OPR §4 ص14 |
| **Monthly Invoice Statement** | BIL §1 | بلا رقم موثق | ACR-BIL §1 |

## 2. دورة حياة القيد المدين (Debit)

```
[تلقائي من FO/POS/BQT/MEM]──┐
                             ├──(حفظ، Doc# آلي)──> ACTIVE ──(SOA معالجة)──> CLOSED
[يدوي: CC/BoH/Company]──────┘                         │
                                                      │ (خطأ كتابي)
                                  (Rollback SOA)──────┤
                                                      ├──> تعديل جزئي (Outstanding Update:
                                                      │    Bill#/Date/Description/Bank/CC فقط)
                                                      └──> تعديل كامل يتطلب فتح سلسلة القفل
```

**الحالات الموثقة:** ACTIVE (قابل للتعديل حتى قفل ما) · INVOICED (مفوترة — قيد) · MATCHED (مطابَقة بإيصال) · CLOSED (بعد SOA).

## 3. دورة حياة الإيصال (Receipt) — الأغنى في الانتقالات

```
                         (Attr#6=Yes)                       (Attr#6=No)
 UNALLOCATED ──(Match Bills-Receipts)──> MATCHED <──(تخصيص مباشر Bill#)── DIRECT-MATCH
     │                                        │
     │ (فائض سداد > معلق)                     │ (Untagging: UnTag=YES)
     └──> surplus يظل UNALLOCATED             └──> UNALLOCATED (عودة!)
                (الجلسة التالية)
```

| الانتقال | الشرط | المصدر |
|---|---|---|
| UNALLOCATED → MATCHED | Match Bills–Receipts: إيصال + فواتير + Adjusted Amounts → Save | ACR-OPR §2 ص11 |
| DIRECT (Bill #) | Attr#6 = No: إدخال Bill # مباشرة في Credit Entry | ACR-OPR §1 ص4 |
| MATCHED → UNALLOCATED | **Receipts Untagging** (double-click UnTag) | ACR-OPR §6 ص19 |
| surplus إيصال | سداد > معلق → إيصال بالفارق (خيار Yes) | ACR-OPR §1 ص7 |
| حذف مطابَقة | حذف Credit transaction (للتعديل بعد Match) ثم إعادة تسجيل ومطابقة | ACR-OPR §8 ص21 |

## 4. دورة حياة الفاتورة (Invoice)

```
UNBILLED ──(Print Invoice: نطاق/شركة + As On + Bill Spec)──> INVOICED (مرقمة)
   ▲                                                              │
   │ (Cancel Invoice: نطاق أرقام — بوابة تعديل القيد)             │ (Reprint: بنطاق أرقام فقط —
   └──────────────────────────────────────────────────────────────┘  لا طباعة جديدة لنفس الفاتورة)
```

| الحالة | القيد الناتج | المصدر |
|---|---|---|
| UNBILLED | "Unbilled transactions are those for which Invoice/Statement is not printed" | ACR-RPL §2 ص4 |
| INVOICED | لا تعديل (إلا Company Name/Branch بـ INI #74=0) + لا طباعة ثانية | ACR-OPR §1 ص10 + ACR-BIL §2 ص6 |

## 5. دورة حياة الشهر المالي (SOA)

```
 OPEN ──(Statement of Accounts: الشهر آلي متسلسل)──> CLOSED ──(Rollback من cutoff حتى آخر معالج)──> OPEN*
        *شرط: القيود المفوترة تتطلب Cancel Invoice أولاً، والمطابَقة تتطلب حذف الإيصال الدائن أولاً
        ثم: تعديلات → إعادة معالجة SOA
```

| الحالة | المعنى | المصدر |
|---|---|---|
| OPEN | إضافة/تعديل/حذف متاح | ACR-OPR §7 |
| CLOSED (SOA) | "transactions for the month are closed and cannot be modified or deleted" | ACR-OPR §7 ص20 |

**قيد التسلسل:** الشهر الأول = AR Start Date؛ بعده يُعرض الشهر التالي آلياً والحقل غير قابل للتحرير (ACR-OPR §7 ص21).

## 6. دورة حياة المتابعة (Follow-Up)

```
 TAGGED (فواتير + مكلَّف + projection) ──> ACTIVE ──(موعد تالٍ)──> متابعة جديدة
                        │
                        └──(Payment Status يتحقق)──> CLOSED (قابل للفلترة "closed follow-ups")
```

المتابعة تحمل: Activity Date · Total Follow-Up Amount · Assigned To · Remarks · Next Date/Time · Projection Amount · Projection Period · Payment Status (ACR-CRT ص3).

## 7. الأحداث المؤتمتة الموثقة

| الحدث | المشغّل | المصدر |
|---|---|---|
| قيد مدينة تلقائي | تسوية ائتمانية (Company/CC/BoH) في FO/POS/BQT/MEM | ACR-OPR §1 ص2+ص4 |
| عرض سعر الصرف | اختيار العملة (من Exchange Entry) | ACR-OPR §1 ص3 |
| حساب Value/Net | الإدخال (Amount × XRate − Commission) | ACR-OPR §1 ص3 |
| فتح شاشة FA Transaction | الحفظ (إذا INI #56=0) | ACR-OPR §1 ص10 |
| عرض AR Start Date + الرصيد الختامي | شاشة Opening Balance | ACR-SET §2 ص5 |
| الترقيم الآلي لـ SOA | كل معالجة ناجحة | ACR-OPR §7 ص21 |
| تغيير الحالة إلى Y | إتمام المطابقة | ACR-OPR §1 ص6 |

## 8. معاملات "العرض فقط" (لا تنشئ مستندات)

| الوظيفة | الأثر | المصدر |
|---|---|---|
| Credit Card Consolidation | تجميع عرضي — "for the Credit Card Register **only**" | ACR-OPR §4 ص13 |
| Travel Agent Commissions | تحديث **% العمولة داخل القيود** (لا مستند) | ACR-OPR §3 ص13 |
| Outstanding Update | تصحيح حقول (لا مستند تصحيح!) — `[UNCERTAIN]` هل يترك أثر Audit | ACR-OPR §5 |
