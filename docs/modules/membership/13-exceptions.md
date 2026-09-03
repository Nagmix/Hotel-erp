# 13 — الاستثناءات والحالات الحدية (Exceptions & Edge Cases) — وحدة MEM

> **33 حالة حدية** موثقة/مستنتجة — أثقلها عائلة **الإنهاء الأربعة** (تتالٍ/خلافة/استرجاع) وعائلة **الترحيل الدوري** (إلغاء/حجب/تعارض زمني).

---

## 1. عائلة الإنهاء (12 حالة)

| # | الحالة | السلوك الموثق |
|---|---|---|
| X1 | إدراج Primary بالقائمة السوداء | "additional members, spouse, and children... are **automatically blacklisted**" (MMN ص6) |
| X2 | إدراج زوج/طفل بالقائمة السوداء | "the primary member is **not affected** and he can continue his club membership" |
| X3 | إنهاء Primary | تتالٍ تلقائي كامل (X1 بنفس النص) |
| X4 | إنهاء فرد فرعي | لا يمس Primary |
| X5 | استقالة Primary | تتالٍ تلقائي |
| X6 | استقالة فرد فرعي | لا يمس Primary |
| X7 | وفاة Primary | **شاشة خلافة** تُفتح (اختيار بديل) |
| X8 | خلافة = None | "**all the members of the membership will be removed**" (MMN ص11) — إتلاف العضوية كاملة |
| X9 | وفاة فرد فرعي | لا تمس Primary + سماحية الاسترجاع |
| X10 | إدخال وفاة بالخطأ | "If you have **accidentally** entered a member as deceased... select the Revoke the Decease Member option" (MMN ص11) + استرجاع بالنقر المزدوج من القائمة |
| X11 | سحب القائمة السوداء | نفس شاشة Revoke + شخص مسؤول + سبب |
| X12 | رصيد متبقٍ عند الإنهاء | **لا مسار تسوية موثق** (GAP-ME-P1) — العضوية تُنهى والع mdlجوبة تظهر في Due Report فقط |

## 2. عائلة الترحيل الدوري (8 حالات)

| # | الحالة | السلوك |
|---|---|---|
| X13 | عضو محدد بلا اختيار في Post Subscription | **حجب ترحيله** (withhold) رغم استحقاقه (MTR ص17) |
| X14 | إعادة تشغيل Post Subscription | "withhold, withdraw, or **overwrite**" — نمط إعادة تشغيل محسوم |
| X15 | إلغاء Cover بعد الترحيل | خيار **Cancel** لنفس الشهر (MTR ص17) |
| X16 | From Date مستقبلي في Process Facility | مرفوض: "From Date should be **less than or equal to current date**" (MTR ص16) |
| X17 | رصيد Credit (دائن) عند Late Fee | **لا رسوم** — "if the outstanding amount is **Debit** amount" فقط (MTR ص18) |
| X18 | رسوم التأخير بشهر = يناير | تحتسب رصيد **ديسمبر السابق** (المثال الرقمي — إزاحة شهر دائماً) |
| X19 | عضو بلا وسوم Revenue/Facility | المحركات تجاهله (لا إيراد يُولد — استنتاج من البنية) |
| X20 | تعارض تعديل سعر ساري | ممنوع: "modify... only if 'Applicable From' **greater than current date**" (SET ص8) |

## 3. عائلة الفوترة والتسوية (7 حالات)

| # | الحالة | السلوك |
|---|---|---|
| X21 | عضو مدرج بالقائمة السوداء يطلب خدمة | **منع من المرافق** لو سمة #8 Yes — "will not be able to avail any facilities" (SET ص12) |
| X22 | خدمة بلا سعر في Rate Master | **انعدام القدرة على الفوترة** — "mandatory for the Service Bill Entry" (SET ص7) |
| X23 | خصم بلا سبب | حقل Reason مع كل خصم (MTR ص8) — توثيق إلزامي |
| X24 | تسوية Company الافتراضية | سمة #11 تجعل الفاتورة على الحساب دون سؤال (SET ص12) |
| X25 | تعديل تاريخ محاسبي | لو سمة #12 No — "The Accounting date is **required to be provided**" (يدوي) |
| X26 | ضيف غير عضو يستخدم مرافق | Guest Rates (الشريحة الثانية) + Guest Visit Entry بـ non-member A/C Entry Fee |
| X27 | عضو نادٍ متفق معه | Affiliated Billing + شريحة Affiliated Rates (MTR ص7) |

## 4. عائلة الهوية والتوليد (6 حالات)

| # | الحالة | السلوك |
|---|---|---|
| X28 | سمة #10 مفعلة ثم محاولة إلغائها | **ممنوع**: "this flag cannot be de-activated" (SET ص11) |
| X29 | سمة #10 بدون سمة #9 | غير قابلة للتفعيل: "activated **only if flag # 9** is activated" |
| X30 | عضوية مؤبدة (Lifetime) | Tenure غير منطبق (SET ص4) — وسمة #13 تفرض UPTO لغيرها |
| X31 | رقم عضوية مكرر (وضع يدوي) | **لا تحقق توثيقي** (سمة #1 تكشف قيمة النمط — فجوة منصة) |
| X32 | طلب صلاحيته منتهٍ | Application Date/Valid until تسجل — **لا سلوك موثق لانتهائها** (استدلال: يبقى في Pending Applications) |
| X33 | بريد إلكتروني عضو غير محدث | Birthday List: "double click the email address to **update**" — تحرير داخل التقرير (RPL ص33) |

## ملاحظات تحليلية

1. **الاسترجاع الشامل**: كل حالة سلبية لها Revoke مقابل (Blacklist/Terminated/Resignation/Deceased/Cover-Posting) — فلسفة "قابل للعكس" تشغيلياً حتى في الحالات الحساسة.
2. **الرصيد الدائن آمن**: X17 يحمي العضو من رسوم تأخير على رصيد لصالحه — قاعدة عدلية نادرة التوثيق.
3. **الإتلاف الكامل مشروط بقرار صريح**: X8 (None) لا يحدث ضمنياً بل بخيار مستخدم — تصميم حذر.
4. **بلا حالات تزامن**: لا توثيق لحدوث محركين معاً أو مستخدمين على نفس الفاتورة — فجوة منصة عامة (كل الوحدات).
