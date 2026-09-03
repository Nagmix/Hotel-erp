# 10 — المعاملات (Transactions) — وحدة TEL

> **T-TE-01..14** — وحدة "المعاملات" هنا غير تقليدية: أغلبها **أحداث استقبال آلية** من العتاد أو **أفعال تحويل حالة** (YES/NO) أكثر منها إدخالات. المعاملات المالية الفعلية: ترحيل الفوليو (موحد/تفصيلي) + إعادة الترحيل من الأخطاء.

---

## أ) معاملات الاستقبال والتسعير

### T-TE-01: التقاط المكالمة (EPABX → سجل)
- **المصدر:** "data transfer that happens between **EPABX and the Serial Port**" (CAC ص4).
- **الوسيط:** Conversion Program "to post the call made by the Guest, **sensing the information sent to the EPABX**" (SET ص16).
- **الناتج:** Call Record خام (رقم/امتداد/مدة/زمن).

### T-TE-02: تسعير المكالمة ⭐ (الحدث الحسابي المحوري)
- **المدخلات:** معرّف المكالمة (بادئة) → Country/Area → Slab (+Min/Max) → Holiday Table → Calculation% → Round Off.
- **المخرجات المزدوجة:** P&T Charge (تكلفة على الفندق) + Guest Charge (إيراد النزيل).
- **الصيغة المركبة:** `pulses = duration ÷ slab.seconds` → `charge = pulses × slab.rate` → `× calc%` → `[min, max]` → `تقريب` → `+ tax`.

### T-TE-03: فحص الاعتراضات (4 حالات)
- امتداد غير معرف / غرفة فارغة / مدة ≤ Uncharged Duration / Bad records — أيٌّ منها → **Call Error Record** (بلا فوترة).

### T-TE-04: ترحيل الفوليو — التفصيلي
- "post **each call entry separately** to the guest folio, and these entries **will appear on the guest bill**" (Consolidate = No).

### T-TE-05: ترحيل الفوليو — الموحد
- "**one entry for the day for each category** of calls in the guest folio" (Consolidate = Yes) — بأربع قنوات مستقلة (Local/STD/IDD/Other) و**Revenue Code لكل نوع**.

## ب) معاملات التصحيح

### T-TE-06: إعادة الترحيل من الأخطاء ⭐ (الحدث المالي اليدوي الوحيد)
- "Under the Select column double-click... to change the status to **YES**. (YES means the calls will be **reposted** to the Guest/Room folio for billing)" → Save (CAC ص6).
- أثرها: تحويل سجل مرفوض إلى قيد فوليو — **بدون** إعادة احتساب موثقة (تُرحّل القيم المحسوبة أصلاً؟ غير مصرح).

### T-TE-07: تحويل مكالمة
- From (قسم حصراً) → To (قسم/غرفة/متجر) → قائمة المكالمات → Select YES → Save.
- الأثر: إعادة إسناد المكالمة (وفوترتها) للامتداد الهدف — يُتتبع في Transferred Call List.

## ج) معاملات دورة الإقامة

### T-TE-08: كلمة مرور الامتداد
- "when a Guest registration is done... valid till the Guest checkouts" — إنشاء مشروط بتسجيل FO، انتهاء بالمغادرة (أرقام ≤10).

### T-TE-09: تفعيل/إيقاف + بوابات الأنواع
- Function (Activate/De-activate) + Local/STD/IDD Yes/No — **ثلاث درجات حجب** (خط كله / نوع / نوعين).

### T-TE-10: ترميز كرت الباب
- Encode: "card information... transferred to the key card system, **saved in the backend, read by the door lock interface program and send to the device**" (SET ص27).
- الأنماط: New / Copy / **Single Open (Onity)** / Check Out (تعطيل) / Read (Onity).

## د) معاملات ماستر

### T-TE-11: إصدار شريحة زمنية
- سجل جديد بنفس الكود + Applicable From أحدث — "latest applicable from date" يحكم (لا تعديل/حذف).

### T-TE-12: توليد الأعياد الأسبوعية
- Auto Generation: يوم أسبوع + مدى → Generate → إدراج جماعي في Holiday Table.

### T-TE-13: ربط/فصل امتدادات
- Link (فردية) / Delink (فردي) / **Delink All** (بنافذة تأكيد) — لأجل فوائد غرف التوائم.

### T-TE-14: إدخال دفتر العناوين
- فئة رئيسية/فرعية + اسم + عنوانين + قنوات الاتصال → Save — تراكمي ("previous saved categories are displayed").

## هـ) الأحداث الآلية (Automation Events) ⭐

| # | الحدث | المحفّز | المصدر |
|---|---|---|---|
| E-1 | التقاط المكالمة | وصول بيانات EPABX للمنفذ التسلسلي | CAC ص4 |
| E-2 | التسعير اللحظي | إنشاء Call Record | (استنتاج من WF-01) |
| E-3 | فحص الإشغال | وصول مكالمة من غرفة | CAC ص5 |
| E-4 | حجز الخطأ | إخفاق أي شرط من الأربعة | CAC ص4-5 |
| E-5 | **توجيه لأغلى شريحة** | وجهة غير معرفة (شراكة 9999999999) | SET ص22/25 |
| E-6 | انتهاء كلمة المرور | مغادرة النزيل | CAC ص7 |
| E-7 | وصول بيانات الكرت للجهاز | Encode | SET ص27 |
| E-8 | إخفاء الرسالة المبلّغة | Tag YES + Save | LUK ص12-13 |
| E-9 | إخفاء موقع النزيل بعد الوجدان | Tag YES + Save | LUK ص13 |
| E-10 | ملاحقة البطاقات | CI/CO في FO (مشغّل TEL ينفّذ) | SET ص26-30 |

## و) مصفوفة الأثر المالي

| المعاملة | مدين | دائن | الوقت |
|---|---|---|---|
| T-04 (تفصيلي) | فوليو النزيل (AR) | كود إيراد النوع | لحظة المكالمة |
| T-05 (موحد) | فوليو النزيل (AR) | كود إيراد النوع | **نهاية اليوم** (تجميع) |
| T-06 (إعادة) | فوليو النزيل | كود إيراد النوع | لحظة Select YES |
| الضريبة | ضمن الفوليو | Government Tax Structure | مع الترحيل |
| التقريب | — | — | "read at the time of billing" |
| P&T | **لا قيد موثق** (منظور تكلفة فقط) | — | — |

> ⚠️ **لا أسماء حسابات GL موثقة** — عائلة الفجوة العامة (GAP-TE-D02)؛ P&T كتكلفة بلا مسار قيد (منظور إداري فقط).

## ز) التكرارية والحجم

- **T-01/02/03/04/05:** مستمرة على مدار الساعة (أعلى معاملات تكراراً في الفندق بعد POS!).
- **T-06/07:** عند الحاجة (تشغيلية).
- **T-08/10:** بمعدل CI/CO.
- **T-11/12/13/14:** نادرة (ماستر).
