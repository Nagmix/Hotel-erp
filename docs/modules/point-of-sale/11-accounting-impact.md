# 11 — الأثر المحاسبي (Accounting Impact) — وحدة POS

> المصدر: FAS-SET §7 (POS to Finance Link) + FAS-TRN §G + POS-SET (Tax/GL) + TS (Settlements) + ACR-OPR (القيود التلقائية). POS = **رابط ترحيلي مزدوج الوجه: FAS مباشرة + AR للتسويات الائتمانية.**

---

## 1. رابط POS → Finance (الروابط الست — البند الثاني)

| البند | الموثق | المصدر |
|---|---|---|
| بنية الرابط | **Restaurant × Menu Group → حسابات D/C** — "مبيعات Credit / خصومات Debit" | FAS-SET §7 + FAS-TRN §G |
| الإيقاع | **دفعة مجمعة بعد Day End/Open New Date** (مثل FO — Post FO to Finance) | FAS-TRN §G |
| الفروق غير الموزعة | → حساب **No Transaction (Suspense)** مؤقتاً → إصلاح → **إعادة ترحيل** | FAS-TRN §G |
| حقول البند (شاشة Post) | Account/Revenue/**Audit Code** + D/C + SL | FAS-TRN §G |

## 2. الأحداث المالية الموثقة (18 حدثاً)

| ID | الحدث | الطبيعة | المصدر |
|---|---|---|---|
| F-POS-01 | مبيعات نقدية | إيراد + نقد | TS Settlements |
| F-POS-02 | **مبيعات ائتمانية (Guest→Room)** | إيراد + **City Ledger (فوليو الغرفة)** | TS ص36 |
| F-POS-03 | **مبيعات ائتمانية (AR/Company/BoH)** | إيراد + **قيد AR تلقائي** ("All sales credited to companies are automatically posted as debit entries in the Accounts Receivable module") | TS ص36 + ACR-OPR §1 |
| F-POS-04 | Void | **عكس مبيعات** + سبب | TS + POS-SET §18 |
| F-POS-05 | Complimentary/Promo | **قيمة صفر للضيف** — للتحليل (Comp cost) | TS ص21-22 |
| F-POS-06 | **NC (قسم)** | غير محاسب للضيف + **NC Cost %** لكل نوع قائمة (مصروف) | POS-SET §19 + TS |
| F-POS-07 | Tips (CC/شيك/Guest) | **حقول تسوية مستقلة** | TS ص34-36 |
| F-POS-08 | Coupon/Gift Voucher | تسوية بقسيمة (خصم/هدية) | TS ص35 |
| F-POS-09 | Discounts (Manual/Predefined/Happy/Member) | **خصم Debit** في رابط POS→FAS | TS + FAS-SET §7 |
| F-POS-10 | **Tax Exemption (بسبب)** | ضريبة = 0.00 | TS ص27 |
| F-POS-11 | **All-Inclusive** (ضريبة داخل السعر) | أسعار شاملة | POS-SET §1 |
| F-POS-12 | Round Off (None/Nearer/Higher/Lower + Amount) | **تقريب نظامي للفاتورة** | POS-SET §1/§6 |
| F-POS-13 | Foreign Exchange settlement | تسوية بعملة | POS-LUK §5 |
| F-POS-14 | **Open Item بـ GL Code** (Per-Outlet Menu) | توجيه محاسبي للصنف | POS-SET §24 ص74 |
| F-POS-15 | A/C Group أعمدة تقرير المبيعات | تصنيف GL للتقارير | POS-SET §16 |
| F-POS-16 | Resettlement | **إعادة تسوية بوضع آخر** (أثر مالي معكوس+جديد) | TS ص36 |
| F-POS-17 | Provisional Bill | **بلا رقم — بلا أثر** | TS ص24 |
| F-POS-18 | Post Guest History | تشغيلي (لا مالي) | POS-GST §4 |

## 3. التسويات — الخريطة المحاسبية العابرة للوحدات

```
                    POS CHECK (Net = Bill - Discount + Taxes)
                                    │ Balance must = 0
   ┌────────────┬────────────┬──────┴─────────┬─────────────┬───────────┐
   Cash         CC           Cheque          Coupon        Guest(Room#)   Void
   │            │            │               │             │             │
   نقد مباشر    بوابة CC     Bank/تحصيل      قسيمة/هدية    ┌─ Room→FO Folio
   (Print Bill  (Swipe+Tips) (تفاصيل+Tips)   (رقم+ملاحظة)  ├─ AR/Company → قيد AR تلقائي
   يسوّي نقداً                                           └─ BoH → AR كذلك
   تلقائياً!)
```

## 4. خصائص محاسبية مميزة

1. **طباعة الفاتورة = تسوية نقدية تلقائية** (Print Bill) — سلوك فريد يختصر خطوة (TS ص24).
2. **Guest Settlement يعمل برقم الغرفة** → الضيف من جدول FO (In-house) — أي أن POS يقرأ بيانات إقامة FO لحظياً (TS ص36).
3. **أنماط التسوية الستة الفاعلة حصراً** + "Others will not work" — قيد تكويني على الرغم من وجود أنماط أخرى في الأدلة (مثل City Ledger في FO) — عبر Guest/AR تحقق الائتمان.
4. **الأثر التفاضلي للخصومات:** كل الخصومات (Manual/Revenue/Happy/Member/Loyalty) تظهر **Debit** في رابط POS→FAS.
5. **الضرائب:** Tax Structure لكل صنف/منفذ + إعفاء لكل ضريبة بسبب + All-Inclusive + Tax Currency للمنفذ — أربع طبقات ضريبية.
6. **الإيراد الموجه:** GL Code للصنف (Per-Outlet) + A/C Group في تقارير المبيعات — توجيه دقيق للـ GL.

## 5. الإقفال اليومي مقابل الترحيل

| البعد | POS | المصدر |
|---|---|---|
| إقفال تشغيلي | Close Shift/Outlet (**يحجبه المعلقات**) | TS ص46 |
| ترحيل محاسبي | **Post (POS→Finance) بعد Day End** — دفعة | FAS-TRN §G |
| إغلاق مالي شهر | SOA (AR) / Audited (FAS) | ACR/FAS |

> **تنبيه تكاملي:** ترتيب **Close Outlet مقابل Day End مقابل Post to Finance** غير موثق تسلسلياً في POS — `[INFERENCE]` Close أول ثم Day End (FO) ثم Post — يُحسم في Phase 6.

## 6. أسئلة محاسبية معلقة

| # | السؤال | الحالة |
|---|---|---|
| QA-POS-1 | هل Void يرحَّل كعكس مستند أو بند سالب في Sales Journal؟ | `[NOT DOCUMENTED]` — يُحسم في FAS-REP/Phase 6 |
| QA-POS-2 | أثر Tips محاسبياً (حساب؟ توزيع؟) | `[NOT DOCUMENTED]` |
| QA-POS-3 | تفاصيل أنواع Client في رابط AR (Cash/Bank/Others) مع أنماط POS؟ | FAS-TRN §E (راجع FAS) — مطابقة كاملة في Phase 6 |
| QA-POS-4 | هل Resettlement يولّد قيد عكس أم يعدّل؟ | `[NOT DOCUMENTED]` — نمط "re-process" FAS يرجَّح |
| QA-POS-5 | Coupon/قسيمة: حسابات التصفية؟ | `[NOT DOCUMENTED]` |
