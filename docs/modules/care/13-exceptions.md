# 13 — الاستثناءات وحالات الحافة (Exceptions & Edge Cases) — وحدة Care

> **E-CA-01..17**: الحالات الشاذة الموثقة نصاً (رسائل SMS الخاطئة بالحرف!) + المستنتجة بدرجات ثقة.

---

## 1. استثناءات موثقة نصياً (SMS)

| # | الحالة | السلوك الموثق |
|---|---|---|
| E-CA-01 | المنفذ يرد S لمهمة بدأت فعلاً | SMS: `TASK #1 IS ALREADY STARTED` (OPR ص40) |
| E-CA-02 | المنفذ يرد S لمهمة ليست مخصصة له | SMS: `TASK #1 IS NOT ASSIGNED TO YOU. WORK NOT STARTED` (OPR ص40) |
| E-CA-03 | المنفذ يرد C قبل أي S | SMS: `TASK #1 IS NOT YET STARTED` (OPR ص40) |
| E-CA-04 | المنفذ يرد C لمهمة مغلقة | SMS: `TASK #1 IS ALREADY CLOSED` (OPR ص43) |
| E-CA-05 | المشرف يغلق مهمة والمنفذ يعمل فيها | SMS للمنفذ: `COMPLAINT #1 CLOSED. CLOSED BY: JOHN REASON: ISSUE RESOLVED` (OPR ص43) — **سلب مباشر للملكية** |

## 2. استثناءات تشغيلية موثقة

| # | الحالة | السلوك |
|---|---|---|
| E-CA-06 | لا موظف مسجل للقسم عند رفع شكوى | Unassigned → Work Start يدوي → Assign لاحقاً (OPR ص77-80) |
| E-CA-07 | دخول بوردية غير معينة | Alert + سماح (OPR ص19) |
| E-CA-08 | دخول يوم عطلة/إجازة | Alert "holiday/leave according to the monthly roster" + Yes للسماح (OPR ص20) |
| E-CA-09 | Stop لمهمة بدأت (مقابل Cancel لما لم يبدأ) | أداة Cancel/Stop تقول "not yet started" (OPR ص49) لكن التقرير يوثق Stopped = بدأت ثم أُلغيت (REP ص64) — **مسار غير موثق للإيقاف اللاحق** (راجع BR-CA-07) |
| E-CA-10 | غرفة غير مشغولة | Pink في Guest Name (OPR ص30) + لا اسم ضيف (ص45) + Request/Incidents غير متاح (V-CA-10) |
| E-CA-11 | شكوى من منطقة أخرى | Magenta في Room# + اسم الموقع في العمود (OPR ص30/45) + لا Floor في تقارير معينة (V-CA-14) |
| E-CA-12 | SMS عالقة (لم تصل) | حالة Queued + زر **Clear Pending SMS** في Supervisor Lookup (OPR ص69) |
| E-CA-13 | روستر بلا ورديات ثم محاولة طوابق | رسالة منع (OPR ص11) |
| E-CA-14 | لا روستر للشهر | 'Schedule Not Entered' — منع الدخول (OPR ص20) |
| E-CA-15 | حذف موظف ثم الحاجة إليه | Deleted List → استرجاع (SET ص21) |

## 3. استنتاجات (بدرجات ثقة)

| # | الحالة | التحليل |
|---|---|---|
| E-CA-16 | مغادرة موظف في HRP (F&F) بينما هو حي في Care | **لا جسر** (UNK-010 محسوم بالانفصال!) — سيبقى يستلم مهام/SMS إن لم يُحذف يدوياً في Care — خلل بيانات مؤكد في الأصل؛ إعادة البناء تحله بـ Employee status موحد (F-CA-2) — ثقة عالية |
| E-CA-17 | وردية على الغرفة/الطابق خارج ملكية المنفذ | التخصيص آلي "to the concerned department's logged in User" — هل يراعي Floor assignment في الروستر؟ الدليل يقول "Based on the staff availability the task allocation would be done to the staff joining the shift" (OPR ص5) — لكن آلية اختيار الموظف بالطابق **غير موثقة** (UNK-041) — ثقة متوسطة على وجود العلاقة |
| E-CA-18 (احتياطي) | Multi Task لأقسام لا حاضرين فيها | "all the tasks defined under that department will be assigned" — بعضها Unassigned حتماً؛ لا نص يوضح — ثقة عالية على النتيجة |

## 4. جدول أخطاء التشغيل ↔ رد النظام (Quick Reference)

| خطأ المستخدم/النظام | رد Care الموثق |
|---|---|
| S مكررة | `TASK #1 IS ALREADY STARTED` |
| S من غريب | `TASK #1 IS NOT ASSIGNED TO YOU. WORK NOT STARTED` |
| C قبل S | `TASK #1 IS NOT YET STARTED` |
| C مكررة | `TASK #1 IS ALREADY CLOSED` |
| (نظام) بوابة متأخرة | Queued (ثم Delivered أو Clear Pending) |
| (نظام) لا روستر | `Schedule Not Entered` |
| (نظام) طوابق بلا ورديات | رسالة منع نصية |
| (مشرف) إغلاق فوق مهمة عاملة | SMS `CLOSED BY: ... REASON: ...` |
