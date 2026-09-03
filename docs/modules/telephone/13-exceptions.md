# 13 — الحالات الحدّية والاستثناءات (Edge Cases) — وحدة TEL

> **33 حالة موثقة أو مستنتجة من النص الحرفي** — أبرزها **سباق تسجيل الوصول الجماعي** (مفاتيح بلا PMS!) · الشراكة الدفاعية بأغلى تعرفة · سجلات Bad Records بمحارف دخيلة · ازدواج مصطلح Transfer داخل الوحدة · 0% الممنوعة · والغرفة المزدوجة بامتدادين.

---

## أ) حالات الفوترة المرفوضة (خطأ → مصير)

| # | الحالة | النص الموثق | المصير |
|---|---|---|---|
| 1 | امتداد غير معرف | "If a call is made to an extension that is not defined" | Error Record → إصلاح يدوي (YES) |
| 2 | **غرفة "فارغة" والنزيل فيها** | "group check-in. The keys were given to the guest and the guest checked-in to the room and started using the phone **but the same check-in is not recorded in the PMS**" | Error → Repost بعد إصلاح FO |
| 3 | مكالمة قصيرة | "duration of the call is less than or equal to... **uncharged duration**" | Error (مجانية بالتعريف) |
| 4 | بيانات فاسدة | "01/@2/99 instead of 01/02/99... **an unidentified character**" | Error (سجل ميت — لا إصلاح موثق!) |
| 5 | خط مفعّل بنوع ممنوع | "though the telephone line is activated, you cannot make any local calls" | منع عند المصدر (EPABX) — لا سجل أصلاً |

## ب) حالات التسعير الحدية

| # | الحالة | السلوك الموثق |
|---|---|---|
| 6 | وجهة بلا كود | الشراكة 9999999999 → "highest IDD slab" — أغلى تعرفة |
| 7 | بلد معروف بلا منطقة | الشراكة C (فارغ/9999999999) → "highest STD slab" |
| 8 | 0% لSTD/IDD | **غير مقبولة** — "0% is applicable for all call types **except STD and IDD**" |
| 9 | 0% Others | مجانية كاملة: "Hotel offers this facility free of charge... 00.00 %" |
| 10 | 150%/200% | "one and a half time" / "double" — مثال 60c → 90c/120c |
| 11 | Min > ناتج الشريحة | "minimum rate charge... will **overwrite the Slab code**" — رفع للمينيمم |
| 12 | Max < ناتج الشريحة | تسقيف للماكسيمم |
| 13 | مكالمة عيد | أسعار Holidays — "different rate during Holidays than the Regular days" |
| 14 | يوم أسبوع مخفّض | عبر Auto Generation — "a day where **discounted call charges** are applied" |
| 15 | تعديل شريحة | **مستحيل** — سجل جديد بكود نفسه + تاريخ أحدث يفوز |
| 16 | شريحتان بتاريخين | المثال الحرفي: كود 1 → 18-Dec-2011 + 1-Jul-2012 → **2012** |
| 17 | شريحة بتاريخ اليوم | لا اختيار — "cannot select a slab code that was **created on the same date**" |
| 18 | تقريب None | "you need not enter the amount" (حقل المبلغ يعطّل) |
| 19 | مكالمة قسم | "charged at the normal Service Provider's rates" — بلا ربح |
| 20 | زمن الاتصال لا يُحتسب | Matured Call — "time taken to connect... is not considered" |

## ج) حالات العلاقات التشغيلية

| # | الحالة | السلوك |
|---|---|---|
| 21 | تحويل من غرفة | **ممنوع** — "does not allow... from a room or a shop" |
| 22 | تحويل غرفة→غرفة / متجر→متجر | ممنوع (مصفوفة CAC ص6) |
| 23 | امتدادان لغرفة توأم | **إلزامي** الربط — "must be linked... to avoid errors during billing" |
| 24 | Delink All | نافذة تأكيد — "all the linked extension numbers will be delinked" |
| 25 | كلمة مرور لغرفة فارغة | مرفوضة — "only **occupied rooms**" |
| 26 | كلمة مرور بعد المغادرة | منتهية تلقائياً — "valid till the Guest checkouts" |
| 27 | رسالة مبلّغة | Tag=YES → "will not show in the Guest Page Messages again" |
| 28 | نزيل وُجد | Tag=YES → إخفاء الموقع |
| 29 | تعارض SL# | **زر إداري** — "resolve SL# mismatch issues" (SysAdmin فقط) |
| 30 | Single Open لغير Onity | **غير متاح** — "only with Onity Based Key Card Systems" |
| 31 | Check Out بلا كرت في القارئ | شرط موثق — "card reader should be attached... card inserted" |
| 32 | تعديل كود دولة | **ممنوع** — "cannot modify the Country Code" |
| 33 | تعديل Call Identifier | حذف + إعادة إدخال (لا تعديل موضعي) |

## د) التناقضات والغموضات الموثقة

| الموضع | التفصيل |
|---|---|
| **ازدواج "Transfer"** | View Transfers/Extensions (LUK) = تحويلات **غرف** FO · Call Transfer (CAC) + Transferred Call List (REP) = تحويل **مكالمات** — نفس الكلمة لمعنيين في وحدة واحدة! |
| **حقل Others أمبلغ أم نسبة؟** | "specify the **amount**" في حقل Calculation % (نسبة!) — GAP-TE-D04 |
| **SPL في التقارير فقط** | List All Calls يذكر SPL ("Special numbers like Toll Free") — لا مسار تعريف SPL في SET ولا في Call Identifier (Local/STD/IDD/others)! |
| **فاكورة By Reg#** | خيار Registration# wise بلا شرح متى يختلف عن Room# wise (نفس الغرفة بامتدادات مرتبطة؟ إقامتان؟) |
| **"Extension" في View Transfers/Extensions** | تسمية خادعة: خيار Extension = **تمديد الإقامة** (Stay Extension) لا الامتداد الهاتفي — ثالث معنى لكلمة واحدة! |

## هـ) السباق الزمني (Race Conditions) — الجوهر التشغيلي

```mermaid
sequenceDiagram
    participant G as النزيل (مجموعة)
    participant K as المفاتيح/الغرفة
    participant E as EPABX
    participant P as PMS (FO)
    G->>K: تسجيل وصول جماعي (استلام مفاتيح)
    K->>G: دخول واستخدام الهاتف
    G->>E: مكالمة (قبل تحديث PMS!)
    E->>P: سجل المكالمة
    Note over P: الغرفة "vacant" في FO
    P->>P: Error: Room vacant ✗
    Note later: FO يسجل الوصول
    P->>P: Repost: Select YES ✓
```

- **الحل الموثق:** إصلاح لاحق يدوي — لا طابور انتظار تلقائي (GAP-TE-P01: لا معالجة pending-folio آلية).

## و) سيناريوهات الفشل المركّبة

| السيناريو | التسلسل | النتيجة |
|---|---|---|
| عيد + وجهة مجهولة + حد أعلى | holiday rate × أعلى IDD × max | فاتورة قصوى — نزيل غاضب محتمل |
| غرفة توأم بلا ربط | امتدادان بفوليوين | فوترة مشتتة + "errors during billing" (تحذير الدليل الحرفي) |
| بيانات فاسدة يوم عيد | Bad record | فقد السجل كلياً (لا إصلاح موثق!) |
| شريحة بأزمنة متداخلة | From/To متقاطعة بين سجلين | لا قاعدة فض clash موثقة — الأولى بالترتيب؟ |
| حذف شراكة LCA | مسحها من الماستر | كل المكالمات المحلية → أغلى تعرفة (كارثة صامتة!) |
