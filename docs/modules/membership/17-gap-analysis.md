# 17 — تحليل الفجوات (Gap Analysis) — وحدة MEM

> **GAP-ME-D01..D07 (توثيق) + GAP-ME-P01..P05 (عملية/وظيفة)** — من بينها **أول فجوة "فهرس-بلا-جسم"** في المشروع كله (D01).

---

## أ) فجوات التوثيق (Documentation Gaps)

### GAP-ME-D01: Membership Tax Posting — وظيفة بلا جسم ⭐
- الموقع: فهرس MTR البند #11 (ص1)
- الدليل: **لا يوجد أي قسم في النص (ص15-18 تقفز من Post Subscription إلى Cover Charges)** — الوظيفة الوحيدة من 43 ملفاً مقروءاً بهذا الوضع
- الأثر المحتمل: ترحيل ضريبي مستقل (عنوانه يوحي بترحيل ضرائب العضويات إلى GL) — **UNK-045**
- المعالجة: البحث في إصدارات الدليل الأحدث/المرافقة، أو اعتبارها ميزة غير مكتملة في المنتج الأصلي

### GAP-ME-D02: لا خريطة GL موثقة
- Revenue Codes + Cover + Late كلها "posted to AR" دون أي حساب دائن/مدين مسمى
- (نفس عائلة GAP-ACR العامة — المرحلة 8 GL Mapping)

### GAP-ME-D03: Event Definition بلا جسر BNQ
- فعالية عضو (Venue/From/To/ChiefGuest) **لا تتحقق من توفر القاعة** ولا تتكامل مع Event Calendar/Block Reasons في BNQ
- خطر: **ازدواج حجز** نفس القاعة عبر مسارين — UNK-046

### GAP-ME-D04: مسار فوترة عضو F&B غير موثق
- "non-F&B services only" (MTR ص7) لكن أين يُحاسب عضو POS على حساب عضويته؟ (POS-side pending)
- الحسم متوقع من قراءة POS-REP/BOK اللاحقة

### GAP-ME-D05: لا مفاتيح INI إطلاقاً
- الوحدة الوحيدة (مع CARE) التي تعمل بلا INI — System Attributes (13) هي البديل الداخلي
- إيجابي نسبياً (أقل مفاتيح مفقودة!) لكنه يعمّق سؤال موضع التهيئة المركزية (راجع GAP-SYS-D01)

### GAP-ME-D06: طباعة كروت العضوية غير موثقة
- صورة/توقيع تُجمع للزوج والنادي — لكن **لا شاشة بطاقة عضو مطبوعة** (المفهوم الأشهر في نوادي العالم!) — استدلال: Print Forms مثل HRP أو خارج الأدلة

### GAP-ME-D07: تحقق تفرد رقم العضوية اليدوي
- سمة #1 (يدوي) بلا أي تحقق توثيقي للتكرار

## ب) فجوات العملية (Process/Functional Gaps)

### GAP-ME-P01: الإنهاء بلا تسوية مالية
- Blacklist/Termination/Resignation/Deceased تغير الحالة فقط — **لا Full&Final** (مقارنة بـ HRP التي تملك Full and Final Settlement!)
- المتبقي يظهر في Due Report — لكن العضوية "منتهية" بلا مسار تحصيل/إبراء موثق

### GAP-ME-P02: Credit Limit بلا فرض
- يُدخل عند التحويل (Allow Credit + Limit) ثم **لا يُفحص** في أي مسار لاحق داخل أدلة MEM (Service Bill/محركات الترحيل)
- (راجع V-§فجوة — نفس نقص POS Billing من جهة الحد)

### GAP-ME-P03: لا تذكير تجديد آلي
- Renewal Report (Renewed/Non-Renewed) + Member Expiry List **تقارير يدوية** — لا Scheduler تذكير (راجع POS City Ledger Statements)
- فرصة Frappe: Auto Email Report

### GAP-ME-P04: قناة البريد غير موصوفة
- زرا البريد (Verification/Birthday) دون SMTP/مزوّد/قالب — (نفس GAP-CA-D05 SMS)

### GAP-ME-P05: Refundable بلا مسار استرداد
- Revenue Code يحمل Refundable/Non-Refundable **لكن لا وظيفة Refund موثقة في الوحدة** (مقارنة بـ BNQ Deposit Refund/Retention الكاملة!)
- الافتراض: الإلغاء يتم إيصالاً عكسياً يدوياً — غير موثق

## ج) القرار المرجعي الأولويات

| الفجوة | الخطورة | المرحلة |
|---|---|---|
| D01 Tax Posting missing | متوسطة (نطاق مجهول) | UNK registry |
| D03 BNQ event overlap | **عالية** (ازدواج تشغيلي) | Design decision فور تجاوز BNQ-analysis |
| P01 لا Full&Final | **عالية** (مالية) | F-ME-8 إضافة settlement step |
| P02 Credit بلا فرض | متوسطة | F-ME-5 validation |
| P05 لا Refund | متوسطة | إضافة Credit Note مسار |

## د) ما ليس فجوة (تحليل مضاد)

- **بلا INI ليس فجوة سلبية** بل توطين تهيئة — سجلناها D05 لغرض الحصر فقط.
- **38 تقريراً بلا رسوم معقدة**: أغلبها جدولي — ليست فجوة بل عبء Phase 7.
- **بلا إقفال يومي**: الدورية شهرية بطبيعة النوادي — قرار نموذج مقبول.
