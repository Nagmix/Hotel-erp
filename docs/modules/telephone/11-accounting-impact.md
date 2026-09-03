# 11 — الأثر المحاسبي (Accounting Impact) — وحدة TEL

> **حلقة إيراد فندقية نموذجية مصغّرة:** مكالمة → تسعير → **فوليو النزيل (AR)** بكود إيراد لكل نوع × توحيد اختياري × ضريبة حكومية × تقريب — و**منظور تكلفة P&T بلا قيد موثق**. الوحدة مصدر إيراد Guest Charge صافي؛ لكن بلا أي أسماء حسابات (عائلة الفجوة GL العامة).

---

## 1. قناة الإيراد الموثقة (الفوليو)

| العنصر | التفصيل الموثق |
|---|---|
| **الصمام الرئيس** | Link to Front Office = Yes/No — "to post the calls made by the guest to front office and will be **charged to guest port folio**" (SET ص16) |
| **التقسيم** | 4 أنواع × Revenue Code مستقل — "select the revenue code to which the revenue generated from **each call type** can be posted" (SET ص14) |
| **التوحيد** | Yes = "one entry for the day for each category of calls in the guest folio" / No = "each call entry separately... **will appear on the guest bill**" (SET ص14-15) |
| **الضريبة** | Government Tax Structure — "the tax structure decided by the Government. Example: **Sale Tax**... only to those countries where **telephone sales are taxed**" (SET ص17) |
| **التقريب** | Round Amount "read at the time of billing" + Round Sec (60) في الفاكورة (SET ص17 + REP ص6) |

### شكل القيدين (الاستنباط الموثق بالصياغة)

| النمط | القيد (استنتاجي — الأسماء غير موثقة!) |
|---|---|
| **تفصيلي** (لكل مكالمة) | مدين: فوليو النزيل (AR) / دائن: كود إيراد Local-STD-IDD-Other |
| **موحد** (نهاية اليوم لكل نوع) | مدين: فوليو النزيل (AR) / دائن: كود إيراد النوع — ببندٍ واحد |
| مع الضريبة | + مدين: فوليو / دائن: Tax (ضمن البنية الحكومية) |

## 2. منظور التكلفة (P&T) — بلا قيد

- "The rate charged by the **Service Provider** is for **all the calls made from the Property** and will be **charged to the Property**" (SET ص18).
- **كل وجود P&T الموثق:** أعمدة تقارير (List All / Extension Wise / Room Calls Query) + خيار P&T Charge — **لا قيد مصروف** ولا فاتورة مزوّد ولا مقاصة موثقة في TEL.
- **الاستنتاج:** فاتورة مزوّد الخدمة تدخل خارجياً (FAS/Vendor؟) — التطابق مع سجلات TEL غير موثق (مرشّح: Utilities/Telephone Expense في FAS عند قراءة القسم المالي النهائية).

## 3. قاعدة التسعير الكاملة (أساس المبالغ المرحّلة)

```
pulse = duration ÷ slab.seconds           [Round Off Seconds: Higher/Nearer/Lower/None]
gross = pulse × slab.rate                  [عادي أو Holiday حسب جدول الأعياد]
guest = gross × ext.calc% / 100            [لكل (امتداد، نوع) — 100=أصلي]
guest = clamp(guest, area.min, area.max)   ["overwrite the Slab code"]
guest = round(guest, round_amount)         [إذا ليس None]
net   = guest + tax(govt_structure)        [بلدان الضرائب فقط]
```

- **أمثلة الدليل الحرفية:** 60c عند 100% → 60c؛ 150% → "one and a half time"؛ 200% → "double"؛ **0% → "uncharged call" (ممنوعة لSTD/IDD)** (SET ص4-5).
- **الأعياد:** "All the calls (Local / STD / IDD) have a **different rate during Holidays** than the Regular days" (SET ص10).

## 4. إعادة الترحيل (Correction Posting)

- "YES means the calls will be **reposted to the Guest/Room folio for billing**" (CAC ص6).
- **حالة المحاسبة:** قيد متأخر (مكالمة يوم سابق تُرحّل عند التصحيح) — تاريخ القيد = تاريخ المعالجة أم تاريخ المكالمة؟ **غير موثق** (نفس عائلة أسئلة accounting-date pickup الموثقة في FO/MEM).

## 5. كشف التدفقات المالية

| التدفق | مالك القيد | كود الإيراد | التوقيت |
|---|---|---|---|
| مكالمة عادية | فوليو النزيل (عبر FO) | Rev Code للنوع | لحظي/نهاية يوم |
| مكالمة موحدة | فوليو النزيل | Rev Code للنوع | نهاية اليوم |
| مكالمة مصححة | فوليو النزيل | Rev Code للنوع | عند Select YES |
| مكالمة غير مفوترة | — (تبقى Unbilled) | — | — |
| مكالمة 0% | — ("uncharged call") | — | مجانية |
| مكالمة قسم | "normal Service Provider's rates" — **تكلفة على الفندق** | غير موثق | غير موثق |
| تحويل مكالمة | إعادة إسناد للامتداد الهدف (فوليو الغرفة/القسم الجديد) | Rev Code للنوع | عند Save |

## 6. عناصر موثقة بلا أثر مالي

| العنصر | الوضع |
|---|---|
| كلمات المرور | تشغيلية بحتة |
| كروت الباب | تشغيلية (أمن) |
| Activate/Deactivate | تشغيلي (بوابة إيراد سلبية: منع = إيراد مفقود) |
| Address Book | إنتاجية |
| الرسائل/الموقع | خدمة نزلاء |
| تقرير Guest List / In-House Stats | معلوماتي |

## 7. الفجوات المحاسبية (GAP-TE-D02 + الملخصة)

| الفجوة | التفصيل |
|---|---|
| **لا خريطة GL** | لا حساب مدين/دائن مسمى — Revenue Codes مفاتيح فقط (كل الوحدات الفندقية بنفس العائلة — حسم المرحلة 8) |
| **P&T بلا مسار** | منظور تكلفة بلا فاتورة/قيد/مقاصة داخل الوحدة |
| **كلفة شراء الشريحة** | لا اهتلاك/تسوية فروق تعرفة (فرق P&T vs المفوتر للنزيل = هامش غير محسوب!) |
| **تاريخ القيد المتأخر** | إعادة الترحيل لأيام سابقة — قاعدة غير موصوفة |
| **إيراد الغرف المعرفة بلا امتداد؟** | المكالمات من "extensions that are not defined" — إيراد ضائع قابل للتحصيل يدوياً فقط |
| **الشراكة الدفاعية** | أعلى شريحة للمجهول = إيراد زائد محتمل للنزيل — بلا سياسة إشعار/تعديل موثقة |

## 8. مقارنة عابرة للوحدات (الإيراد الفندقي)

| الوحدة | قناة الإيراد | كود الإيراد | توحيد |
|---|---|---|---|
| **TEL** | فوليو FO مباشر | لكل نوع مكالمة | **Yes/No لكل نوع** (أدق تفويض!) |
| POS | Bill → Settlement | رأس لكل Outlet | بالفاتورة |
| BNQ | Banquet Bill | Menus/GL Code | بالفاتورة/المكمل |
| MEM | Post Subscription/Facility | Revenue Codes Once/Recurring | بالعملية الشهرية |
| FO | Post to Folio | Tax Structures/Rev | — |
| SLM | **صفر** (مفوَّض) | — | — |

> **ملاحظة:** TEL تملك **أدق تحكم توحيد** في المشروع — قرار لكل نوع مكالمة على حدة (قبل MEM بـwithhold/withdraw/overwrite الذي يفوقها في عمق الاشتراكات).
