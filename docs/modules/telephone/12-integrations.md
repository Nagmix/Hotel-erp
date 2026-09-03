# 12 — التكاملات (Integrations) — وحدة TEL

> **I-TE-01..13** — أعلى وحدة **تكامل عتاد** في المشروع (EPABX + أقفال Onity) + حلقة FO المزدوجة الاتجاه (بيانات داخل / إيراد خارج) + تفويض SYS لسمة العرض + **تفويض FO حرفي** لIn-House Statistics. لا جسر HRP (المشغلون ضمن FO الضمني).

---

## 1. TEL ← EPABX (استقبال المكالمات) ⭐

| البند | النص الموثق |
|---|---|
| القناة | "data transfer that happens between **EPABX and the Serial Port**" (CAC ص4) |
| المفسّر | Conversion Program — "a code set to post the call made by the Guest, **sensing the information sent to the EPABX**" (SET ص16) |
| إشارة الرد | **Battery Reverse Signal** — "a facility provided by the Local Telephone Exchange, which gives you the time elapsed to connect a call" (SET ص16) |
| البادئة | EPABX Prefix — "displayed along with the extension number" (عرض) (SET ص16) |
| **الاتجاه العكسي (2-Way)** | "activate / de-activate the **phones, voice mails, wake-up calls and room status**" (SET ص16) |

- **الدلالة:** قناة ثنائية الاتجاه فعلية — TEL تستقبل بيانات المكالمات **وتكتب أوامر** للـEPABX (تحكم فيزيائي بالخطوط!) — أعمق تكامل عتاد موثق في المشروع.

## 2. TEL → أقفال الأبواب Onity ⭐

| البند | النص الموثق |
|---|---|
| القناة | "the information... will be **saved in the backend, read by the door lock interface program and send to the device**" (SET ص27) |
| الأنماط | New Card / Copy Card / Single Open Card (**Onity فقط**) / Check Out (تعطيل) / Read a Card (**Onity فقط**) |
| بيانات الكرت | "the guest stay details on the key card at the time of check-in to enable opening the door **only during the guest stay period**" (SET ص26) |
| شرط التعطيل | "the card reader should be attached to the system and the card should be inserted in the card slot" (SET ص29) |

## 3. TEL → FO (حلقة الإيراد)

| البند | النص |
|---|---|
| الترحيل | "Link to Front Office... post the calls made by the guest to front office and will be **charged to guest port folio**" (SET ص16) |
| التوحيد | Consolidate Yes/No لكل نوع (SET ص14-15) |
| الظهور | "these entries will appear on the **guest bill**" (SET ص15) |

## 4. TEL ← FO (بيانات الإقامة) — خمس قنوات واردة

| القناة | الاستخدام في TEL | المصدر |
|---|---|---|
| **الغرفة/الإشغال** | فحص Room vacant (خطأ!) + Guest List + بطاقات الباب | CAC ص5 + REP/LUK |
| **Registration #** | كلمة المرور (Reg# F1) + طباعة الفاكورة Registration# wise | CAC ص8 + REP ص6 |
| **بيانات النزيل** | Guest Information (تعليمات/شكاوى/رسائل/موقع) + Guest Search | LUK ص9-14 |
| **تحويلات الغرف + تمديد الإقامة** | View Transfers/Extensions — "old room numbers and the new room numbers" + "earlier departure date and time and the new..." + **User + Authorizer** | LUK ص20-21 |
| **In-House Statistics** | **تفويض حرفي**: "refer CHAPTER – LOOKUPS of MODULE – FRONT OFFICE" | LUK ص14-15 |

## 5. TEL → النظام المالي (Revenue Posting)

- Revenue Code لكل نوع مكالمة (Local/STD/IDD/Other) + Government Tax Structure + Round Amount — أربع قنوات إيراد مستقلة الحساب.
- (لا أسماء GL — عائلة الفجوة.)

## 6. TEL ↔ SYS

| القناة | التفصيل |
|---|---|
| **Module Attributes** | "If you want the call duration to be printed in minutes, then change the settings in Module Attributes. (Refer **CHAPTER SUPERVISOR under MODULE SYSTEM SETUP**)" (REP ص6) — سمة عرض (ثوانٍ/دقائق) |
| Property list | تعيين الامتدادات (SET ص4) |
| Currency Codes | عملة الشريحة (F1 — SET ص19) |
| Panel العام | "Command Window, Inter Node Communication, Calculator, Calendar, Scratch Pad, and **Yellow Pages**" (SET ص2) — Yellow Pages تظهر كأداة نظامية عامة! |
| Room/Dept Help | F1 قوائم FO/ SYS |

## 7. TEL ↔ الوحدات الأخرى (سلبيات)

| الوحدة | العلاقة الموثقة |
|---|---|
| HRP | **لا شيء** — لا موظفو هاتف ولا سنترال (الرابع في عائلة UNK-038 المتسعة) |
| POS | لا شيء مباشر (Extension Type يشمل Shop/Public — فوترة المتاجر موثقة ضمن TEL لا POS) |
| BNQ | Link Extensions تشمل "Banquets" — امتدادات قاعات البنوك تفوتر عبر TEL (جسر ضمني بلا تفصيل) |
| MNT | لا شيء (رغم الاشتباه الطبيعي: أعطال الخطوط!) |
| MEM | لا شيء |
| GATE | لا شيء |

## 8. مصفوفة التكامل الكاملة (I-TE-01..13)

| ID | من → إلى | النوع | الحدث |
|---|---|---|---|
| I-TE-01 | EPABX → TEL | عتاد/بيانات | التقاط المكالمات (Serial Port) |
| I-TE-02 | TEL → EPABX | **عتاد/تحكم** | 2-Way: هاتف/بريد صوتي/منبه/حالة الغرفة |
| I-TE-03 | TEL → Door Lock | عتاد/بيانات | Encode البطاقات (Onity) |
| I-TE-04 | Door Lock → TEL | عتاد/قراءة | Read a Card (Onity) |
| I-TE-05 | TEL → FO | **مالي** | ترحيل الفوليو (موحد/تفصيلي + Rev Code) |
| I-TE-06 | FO → TEL | بيانات | الغرفة/الإشغال (Room vacant check) |
| I-TE-07 | FO → TEL | بيانات | Reg# + بيانات النزيل الكاملة |
| I-TE-08 | FO → TEL | بيانات | الرسائل/تعليمات/شكاوى/موقع |
| I-TE-09 | FO → TEL | بيانات/تدقيق | تحويلات الغرف + تمديدات الإقامة (User+Authorizer) |
| I-TE-10 | FO → TEL | **تفويض** | In-House Statistics (مرجع حرفي) |
| I-TE-11 | TEL → FAS | مالي (مفوَّض) | Revenue Codes + Tax Structure |
| I-TE-12 | SYS → TEL | تهيئة | Module Attributes (المدة) + عملات + عقارات |
| I-TE-13 | TEL → SYS/عام | أدوات | Yellow Pages عبر Panel (وصول شامل) |

## 9. أرصدة التكامل (Compelling Observations)

1. **نمط الوسيط المعياري:** كلا التكاملين العتاديين بنفس العمارة: (شاشة → **حفظ في backend** → **برنامج وسيط يقرأ** → **جهاز**) — قابل للتعميم لأي عتاد مستقبلي (POS printers,-door locks أخرى, call accounting خارجي).
2. **استهلاك بلا كتابة لبيانات FO:** كل استعلامات النزيل للقراءة + أنماط Tag YES (استثناء صغير: تحديث حالة الرسالة!) — TEL تكتب حالة إبلاغ في بيانات رسائل FO.
3. **امتداد المتاجر (Shop/Public):** TEL تفوتر مكالمات المتاجر — احتمال قناة إيراد Tenant (غير موثقة الوجهة المالية!).
4. **Banquets في Link Extensions:** إشارة وحيدة لامتدادات القاعات — الربط الفعلي بفواتير BNQ غير موثق.
5. **"Conferencing" لا يظهر هنا:** كل قنوات SLM لا تمر في TEL — التكامل مستقل تماماً.
