# 11 — الأثر المحاسبي (Accounting Impact) — وحدة ACR

> المصدر: ACR-OPR §1 (ص2-10) + FAS-SET §11 (Link AR to Finance) + FAS-TRN §E. **AR هو الرابط السابع/الأخير في الخريطة المالية** — وله نمط ترحيل فريد: **تفاعلي عند الحفظ** بدلاً من الدفعات المجمعة.

---

## 1. نمط الترحيل الفريد (Interactive-at-Save)

| البند | القاعدة | المصدر |
|---|---|---|
| الشرط الأول | حسابات مرتبطة مسبقاً في **Link AR to Finance** (FAS-SET §11): **Sundry Debtors · Cash · Bank · Commission** | ACR-OPR §1 ص10 |
| الشرط الثاني | **INI #56 = 0** (منطق معكوس؛ الافتراضي 1 = معطل) | ACR-OPR §1 ص10 |
| السلوك | "while **saving the entries** in Transaction Entry... the FA Transaction screen is displayed and you are required to post the transaction to proper account codes" | ACR-OPR §1 ص10 |
| الاستجابة | يُدخل القيد لحسابات مناسبة — مثل FAS Transaction Entry (راجع `financial-accounting/10-transactions.md`) | ACR-OPR §1 ص10 |

**الفرق المعماري الحاسم عن FO/POS:**

| الوحدة | نمط الترحيل | الإيقاع | المصدر |
|---|---|---|---|
| FO/POS | دفعة مجمّعة (Post FO to Finance بعد Day End/Open New Date) | **يومي** | FAS-TRN §G |
| **AR** | **تفاعلي عند الحفظ** (شاشة FA Transaction) | **فوري لكل قيد** | ACR-OPR §1 ص10 |
| MM/Payroll/Membership | عند الطلب (PJV/Consumption/Post) | عند الطلب | FAS-TRN §H-K |

## 2. الأحداث المالية الموثقة (16 حدثاً)

| ID | الحدث | الطبيعة المحاسبية | المصدر |
|---|---|---|---|
| F-AR-01 | قيد مدينة يدوي (فاتورة شركة) | مدين Sundry Debtors / دائن حسب الإيراد | ACR-OPR §1 ص4 |
| F-AR-02 | قيد مدينة تلقائي (تسوية FO/POS/BQT/MEM ائتمانية) | "All sales credited to companies are automatically posted as debit entries" | ACR-OPR §1 ص4 |
| F-AR-03 | قبض نقدي مطابَق | دائن Sundry Debtors / مدين Cash | ACR-OPR §1 ص3 (Cash خيار) |
| F-AR-04 | قبض بشيك | دائن Sundry Debtors / مدين Bank (+ تفاصيل الشيك Local/Outstation) | ACR-OPR §1 ص3 |
| F-AR-05 | قبض ببطاقة | دائن Sundry Debtors / مدين البطاقة (Company/Type/CC#/Auth#) | ACR-OPR §1 ص3 |
| F-AR-06 | إيصال غير مخصص (unallocated) | **قبض مقدم** — دائن Sundry Debtors حتى المطابقة | ACR-OPR §1 ص4 |
| F-AR-07 | مطابقة (Match Bills–Receipts) | تخصيص — **لا قيد جديد** (تعديل ارتباط) | ACR-OPR §2 |
| F-AR-08 | Untagging | عكس تخصيص — لا قيد | ACR-OPR §6 |
| F-AR-09 | Adjustment موجب | **Journal Voucher Debit** على الفاتورة | ACR-OPR §1 ص8 |
| F-AR-10 | Adjustment سالب | **Journal Voucher Credit** على الفاتورة | ACR-OPR §1 ص8 |
| F-AR-11 | عمولة وكيل/بطاقة | خصم من Net — دائن **Commission** | ACR-OPR §1 ص3 + Link AR |
| F-AR-12 | فرق عملة عند السداد | **يُمنع تصميمياً** — سعر تاريخ الفاتورة معتمد (منع Book P/L) | ACR-OPR §1 ص6 |
| F-AR-13 | إيصال الفارق (Overpayment) | قبض جديد بالمتبقي | ACR-OPR §1 ص7 |
| F-AR-14 | تحديث عمولة CC Register | "Update Commission Amount in Transactions" — يعدّل القيود | ACR-RPL §8 ص14 |
| F-AR-15 | Opening Balance | أرصدة ما قبل التشغيل (Sundry Debtors افتتاحي) | ACR-SET §2 |
| F-AR-16 | فائدة التقادم | **حساب فقط** (Aging with Interest) — لا قيد آلي موثق | ACR-SET §3 ص9 |

## 3. بنية الحسابات المرتبطة (من Link AR to Finance — FAS-SET §11)

> الوثائق المرجعية الأعمق في `financial-accounting/02-configuration.md` §"Link AR to Finance". ما يخص AR هنا:

| العنصر | الحساب المطلوب تعريفه | الاستخدام في AR |
|---|---|---|
| Sundry Debtors | حساب الذمم المدينة الرئيسي | طرف كل قيود AR |
| Cash | النقد | قبض نقدي |
| Bank | البنك | قبض شيكات/تحويلات |
| Commission | عمولات الوكلاء/البطاقات | خصم العمولة |

**إسناد أنواع Client المذكورة في FAS:** أنواع × Cash/Bank/Others (راجع FAS-TRN §E — "AR Receipts فورية مع تعديل F5").

## 4. التقاطع مع دورة Night Audit (FO)

- تسويات FO الائتمانية (Company/CC/BoH) تظهر هنا **كقيود مدينة تلقائية** خلال/بعد Night Audit — الدليل: "view and partially amend debit transactions that are auto posted (bills settled on credit) from the Front Desk..." (ACR-OPR §1 ص2).
- عارض فاتورة المصدر (زر FO Bill Details) متاح **للفواتير التلقائية من FO/POS فقط** (ACR-OPR §1 ص9) — تتبع مستندي عكسي.

## 5. الإقفال المالي المتدرج (منظور AR)

| الطبقة | الأداة | الأثر المحاسبي | المصدر |
|---|---|---|---|
| 1. مستند | Invoice مطبوعة | تجميد القيد (تعديل محدود INI #74) | ACR-OPR §1 ص10 |
| 2. شهر | SOA | إقفال نهائي متسلسل | ACR-OPR §7 |
| 3. سنة | Open Financial Year (FAS) + **قفل Audited الشهري** (FAS) | يتعامل مع السنة كلها | FAS-SET §18 + FAS-TRN §8 |

> **تنبيه تكامل:** SOA (AR) وAudited (FAS) **آليتا إقفال مستقلتان** — الرجوع في FAS (Rollback FY) لا يوثّق تفاعله مع SOA — راجع `13-exceptions.md` E-AR-16.

## 6. أسئلة محاسبية معلقة (تُحسم في Phase 6 — Accounting)

| # | السؤال | الحالة |
|---|---|---|
| QA-AR-1 | هل يرحَّل كل قيد AR **بشاشة FA واحدة** أم يجمع بالجلسة؟ — النص: "while saving the entries... the FA Transaction screen is displayed" (مفرد لكل حفظ) | `[INFERENCE]` لكل قيد |
| QA-AR-2 | حساب عمولة البطاقة: خصم **وقت القبض** أم عند CC Register (Update ☐)؟ | `[NOT DOCUMENTED]` — النمطان موثقان كخيار |
| QA-AR-3 | هل قيود Opening Balance تُرحَّل لـ FAS؟ (لا ذكر لشاشة FA في شاشات SET §2) | `[NOT DOCUMENTED]` |
| QA-AR-4 | توقيت قيد فائدة التقادم (Aging with Interest) — حساب عرض فقط أم ترحيل دوري؟ | `[NOT DOCUMENTED]` |
