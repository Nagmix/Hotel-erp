# 11 — الأثر المحاسبي (Accounting Impact) — وحدة MEM

> وحدة MEM **وحدة إيراد كاملة الدورة المالية**: تحصيل (إيصالات) + فوترة (فواتير خدمية) + دورية (4 محركات) + دفاتر مساعدة (15 تقريراً مالياً) — لكن **بلا خريطة GL موثقة** (GAP-ME-D02): الأكواد موجودة والحسابات غير موثقة.

---

## 1. دورة الإيراد الموثقة (نمط AR المتأخر)

```
تحميل الحساب (Debit)                     التحصيل (Credit)
┌─────────────────────────┐              ┌──────────────────────┐
│ Process Subscription    │ ترحيل مدين → │ Membership Receipt    │
│ Process Facility Chrgs  │ ترحيل مدين → │ Entry (4 جهات +      │
│ Cover Charges Posting   │ ترحيل مدين → │ عملات + Payment Type)│
│ Posting Late Charges    │ ترحيل مدين → │                      │
│ Service Bill → AR       │ فاتورة/مدين →│ Settlement            │
└─────────────────────────┘              └──────────────────────┘
        ↓ المراقبة اليومية                      ↓ القياس الدوري
  Due Report / Settlement Query      Closing Balance + Control Report
                                          ↓ العقوبة
                                   Late Charges (الشهر التالي!)
```
- **النمط = AR City Ledger بالتوقيت النرويجي**: ترحيل أولاً (محركات شهرية) ثم تحصيل، ورسوم التأخير تُحسب على رصيد الشهر السابق (مثال 2011/2010 الموثق).
- التسوية الافتراضية للشركة (سمة #11) تجعل الفاتورة الخدمية **City-Ledger أولاً** — نفس قرار BNQ/POS (CC/Company → AR).

## 2. الأحداث المالية الموثقة (12 حدثاً)

| # | الحدث | الطرف المدين | الطرف الدائن | التوثيق |
|---|---|---|---|---|
| F1 | إيصال عضوية (أي جهة) | نقود/بنك (حسب Payment Type) | حساب عضو AR | MTR ص2-3 |
| F2 | فاتورة خدمة → AR | حساب عضو AR | إيراد الخدمة (Revenue Code) | MTR ص9 |
| F3 | فاتورة خدمة → نقد | نقود | إيراد الخدمة | MTR ص10 |
| F4 | فاتورة خدمة → CC | ذمم بطاقات (مع Authorization) | إيراد الخدمة | MTR ص11 |
| F5 | فاتورة خدمة → شيك | ذمم شيكات (Bank/Branch) | إيراد الخدمة | MTR ص12 |
| F6 | ترحيل اشتراك | حساب عضو AR | إيراد اشتراك (Recurring) | MTR ص16 |
| F7 | ترحيل مرافق | حساب عضو AR | إيراد مرافق | MTR ص16 |
| F8 | ترحيل Cover | حساب عضو AR | إيراد Cover (+ اعتبار Adjustment Debit) | MTR ص17 |
| F9 | رسوم تأخير | حساب عضو AR | إيراد رسوم تأخير (ببنية ضريبة FO!) | MTR ص18 |
| F10 | خصم فاتورة (AMOUNT/PERCENTAGE) | خصم مسموح (مع Reason) | — | MTR ص8 |
| F11 | عمولة بطاقة (تقرير فقط) | — احتساب Commission % في Credit Card Register | — | RPL ص43 |
| F12 | إلغاء ترحيل Cover | عكس F8 | عكس F8 | MTR ص17 |

> ⚠️ **كل الطرف المدين/الدائن أعلاه استدلال تحليلي** — الدليل يوثق "posted to the relevant members AR account" و"Revenue Codes for accounting the revenue" **دون تسمية حسابات GL** (GAP-ME-D02).

## 3. الضرائب الموثقة

1. **Service Rate Master** لكل شريحة سعر: "Enter the service rates **and Tax Structures** for both Adult and Children" (SET ص7) — ضريبة على مستوى السعر.
2. **Late Charge Fee**: "By Tax structure" من **بنيات FO** (SET ص15) — رسوم التأخير **تُحتسب ببنية ضريبية** وليس نسبة جاهزة — نمط فريد (راجع BR-ME-11).
3. ~~Membership Tax Posting~~: وظيفة مفهرسة بلا جسم (GAP-ME-D01/UNK-045).
4. تقرير Charges فئة إيراد + Control Report بفصل **debit/credit consolidated** (RPL ص48-49).

## 4. الدفاتر المساعدة الداخلية (Sub-Ledger)

- **دفتر عضو داخلي كامل**: Opening Balance → Transactions → Closing Balance (تقرير 30) + Due as on date (31) + Control consolidated (33) + مقابلات بنكية (Receipt Register بـ Bank Wise Breakup) + عمولات بطاقات (29).
- **فترة الدفتر شهرية** (Month/Year مدخل إلزامي في 30/31/33) — تطابق إيقاع محركات الترحيل.
- **التوازن التشغيلي**: الإلغاء الشهري لـ Cover + الثلاثية withhold/withdraw/overwrite في Post Subscription = أدوات تصحيح الدفتر دون قيود عكسية معقدة (مقارنة بـ AR Adjustments).

## 5. الفجوات المحاسبية الموثقة

| الفجوة | الوصف | التصنيف |
|---|---|---|
| لا GL mapping | Revenue Codes بلا حسابات دائنة موثقة | GAP-ME-D02 |
| Entry Fee غير مرحّلة | رسوم دخول الزيارات بلا وجهة محاسبية | UNK-047 |
| الإنهاء بلا تسوية | Blacklist/Termination/Resignation/Deceased **لا تفوّر رصيد المتبقي** ولا تعالج المستحقات | GAP-ME-P1 |
| Deposit/إيداعات | لا يوجد مفهوم إيداع مسترد موثق (رغم Refundable في Revenue Codes!) — Refund مسار غير موثق | GAP-ME-P5 |
| خصم مسموح | Discount بReason بلا دليل حسابات مخصصة | استدلالي |

## 6. العملات

- الإيصالات: عملة متعددة + **Currency Rate تلقائي** (MTR ص3).
- Membership Structure: عملة لكل فئة/إيراد + Exchange Rate تلقائي (SET ص10).
- التقارير المالية: بلا فلترة عملة موثقة (افتراض عملة الدفتر الواحدة — نفس افتراض ACR).
