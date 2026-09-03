# 18 — معايير القبول (Acceptance Criteria) — وحدة MEM

> **10 مجموعات / 48 معياراً** مشتقة حرفياً من السلوكيات الموثقة (كل معيار بمرجعه)، + **اختبار دخان (Smoke Test) من 26 خطوة** يحاكي شهر تشغيلي كاملاً لوحدة نادٍ.

---

## AC-ME-01: التهيئة والسمات (من SET)
1. تاريخ Application Date في Service Rate Master أقل من اليوم يُرفض (SET ص6).
2. تعديل سعر سارٍ (Applicable From ≤ اليوم) ممنوع (SET ص8).
3. تفعيل سمة #10 يتطلب سمة #9 مفعلة (SET ص12).
4. سمة #10 لا تُلغى بعد التفعيل (SET ص11).
5. الرسوم الثابتة تدعم 5 أدوار × 5 فترات (SET ص12).
6. Screening checklist يعرض فقط بنود الفئة المختارة مع Mandatory الملونة (SET ص5-6).

## AC-ME-02: كود الإيراد والهيكل (من SET)
7. Revenue Code Once يظهر في Revenue/Facility Entry؛ Recurring لا يظهر (SET ص9).
8. Membership Structure يسحب Exchange Rate تلقائياً مع Currency (SET ص10).
9. Cover Charges تحفظ Senior Citizen Exemption + Adjustment Debit (SET ص15).
10. Late Charge Fee يعرض بنيات FO الضريبية النشطة فقط (SET ص15).

## AC-ME-03: دورة الانضمام (من MPF)
11. حفظ Corporate Application يولد Application# (MPF ص5).
12. المرشحون Corporate nominees يدخلون عبر Membership Application (MPF ص5).
13. Address copy button ينسخ بين Register/Local/Mailing (MPF ص4).
14. Screening بلا Internet Required يمر للتحويل مباشرة (MPF ص13).
15. Interview Status محصور بثلاث: Considered/Rejected/Cancelled (MPF ص21).
16. Transfer Corporate بلا Validity يُرفض (MPF ص23).
17. Transfer Membership يعرض Credit Limit Details (Allow Y/N + Limit) (MPF ص26).

## AC-ME-04: الاستدعاء والتوليد (سمات 2-7 + MEMC001) ⭐
18. سمة #4 Yes تستدعي Revenue/Facility فور حفظ Membership Application (SET ص11).
19. سمة #3 Yes تستدعيها فور حفظ Corporate Master (SET ص11).
20. سمة #7 Yes تولد سلسلتي إيصالات منفصلتين للأعضاء والطالبين (SET ص11).
21. سمة #10 Yes + حفظ Membership Master ينشئ شركة ACR ببادئة MEM وحرف الاسم الأخير الأول (DAVID S CRAIG → MEMC001) (SET ص12).
22. سمة #1 No يولد رقم العضوية تلقائياً (SET ص11).

## AC-ME-05: الإنهاء والتتالي (من MMN) ⭐
23. إدراج Primary بالقائمة السوداء يسودّ العائلة تلقائياً (MMN ص6).
24. إدراج زوج/ابن بالقائمة السوداء لا يمس Primary (MMN ص6).
25. نفس الثنائية 23/24 تتكرر حرفياً في Termination (ص8) وResignation (ص10).
26. وفاة Primary تفتح شاشة خلافة، واختيار None يزيل كل أعضاء العضوية (MMN ص11).
27. كل إنهاء يطلب Authorized Person + Reason (وبند Cause of Death للوفاة) (MMN ص5-12).
28. Revoke Deceased يسترجع عضواً أُدخل وفاةً بالخطأ (MMN ص11).
29. Category Transfer يعرض Old Category تلقائياً ويطلب New + Remarks (MMN ص12).

## AC-ME-06: الفوترة الخدمية (من MTR)
30. Service Bill يرفض F&B (non-F&B only) بالتصميم (MTR ص7).
31. السعر يُسحب تلقائياً من Service Rate Master حسب شريحة (Members/Guest/Affiliated) والفئة العمرية (MTR ص7-8).
32. خصم AMOUNT/PERCENTAGE يطلب Reason (MTR ص8).
33. سمة #11 Yes يجعل التسوية الافتراضية لحساب Company/Member (SET ص12).
34. سمة #12 Yes يملأ Accounting Date من FO (SET ص12).
35. تسوية CC تسجل Type/Company/Card#/Authorization (MTR ص11).
36. العضو المدرج بالقائمة السوداء يُمنع من المرافق لو سمة #8 Yes (SET ص12).

## AC-ME-07: المحركات الدورية (من MTR) ⭐
37. Process Subscription يرحّل من الماسترات لحسابات AR للأعضاء (MTR ص16).
38. Process Facility يرفض From Date مستقبلي (MTR ص16).
39. Post Subscription يعرض checkboxes لكل الأعضاء افتراضياً وإلغاء اختيار عضو يحجب ترحيله (MTR ص17).
40. Cover Charges Process ثم Cancel لنفس الشهر يعكس الترحيل (MTR ص17).
41. Late Charges بMonth=Jan-2011 يحسب رصيد آخر يوم Dec-2010، ويرحّل فقط لو Debit، إلى ACR (MTR ص18).

## AC-ME-08: الشكاوى والفعاليات (من MTR)
42. الشكوى تُسجل من عضو أو ضد عضو، بPriority وAssigned To (MTR ص12-13).
43. Attend Complaints يغلق بAction By (MTR ص13-14).
44. Event Definition يسجل Venue/From-To DateTime/Chief Guest (MTR ص14-15).

## AC-ME-09: الإيصالات والزيارات (من MTR)
45. Receipt Entry يدعم الأربع جهات (Membership/Corporate/Application/Member) بعملة وسعر صرف تلقائي (MTR ص2-3).
46. Guest Visit يدخل مرافقين بInsert Guest Details وEntry Fee بفئة member أو non-member A/C (MTR ص5-6).

## AC-ME-10: التقارير والاستعلامات (من RPL)
47. Birthday List يسمح بتحديث البريد بالنقر المزدوج + Send Email (RPL ص33).
48. Membership Summary يحفر: عدادات → سجلات → Member Information (RPL ص33-34) وSpending Pattern يصل للفاتورة (RPL ص55).

---

## اختبار الدخان (Smoke Test — 26 خطوة)

```
شهر تشغيلي كامل لنادٍ:
 1. تهيئة: Facility Code (BOAT) → Service Rate 3 شرائح Adult/Child
 2. Revenue Code JOIN (Recurring) + INIT (Once, Refundable)
 3. Structure لفئة GOLD بعملة + Primary/Adult/Child
 4. سمة #1=No، #6=Yes، #7=Yes، #9=Yes، #10=Yes (رصد قفلها!)
 5. Category GOLD (Corporate + 3 nominees + Age 18 + Ref 2)
 6. Screening: بندين (Contact mandatory + Photo optional)
 7. طلب شركة + 3 مرشحين → Application# تولد
 8. فحص طلب: تحقق + Interview=Yes → جدولة → Considered
 9. Transfer Corporate بValidity → Receipt Entry تستدعى → تحصيل INIT
10. [تحقق] شركة MEM+حرف تظهر في AR (جسر #21)
11. طلب فردي (زوج بصورة وتوقيع + طفلان) → فحص → تحويل بCredit Limit 5000
12. Service Bill: بالغان 2 + أطفال 1 لعضو (أسعار الشريحة) → خصم 10% بReason → AR
13. [تحقق] الفاتورة على حساب العضو لا نقد
14. Guest Visit: عضو + 3 مرافقين + Entry Fee non-member A/C
15. Revenue Tag شهري لعضو (Recurring) + Facility Tag Fixed شهري
16. Process Subscription للشهر → Post to AR (كل الأعضاء checkboxes)
17. [تحقق] حجب عضو واحد بإلغاء checkbox — رصيده لم يتحرك
18. Process Facility Charges (From ≤ اليوم)
19. Cover Posting: Process للشهر → [تحقق] رسوم كبار السن مستثناة
20. Cover Posting: Cancel لنفس الشهر → [تحقق] عكس الترحيل
21. Late Charges بMonth=Current → [تحقق] رصيد آخر يوم من الشهر-1 فقط للمدينين
22. شكوى من عضو (Priority High) → Attend → إغلاق
23. Blacklist Primary → [تحقق] العائلة سوداء تلقائياً والPrimary مستمر لو عكسنا
24. وفاة Primary → خلافة: الزوج Primary جديداً
25. تقرير Birthday List → Send Email لشهر جارٍ
26. Spending Pattern بAfter Service → حفر للفاتورة رقم 12
```

> **معيار النجاح الإجمالي:** كل [تحقق] يطابق حرفياً السلوك المرجعي الموثق — أي انحراف = قيد ملاحظة في 17-gap (إن كان نقص توثيق أصلي) أو عيب تنفيذ (إن كان كسر قاعدة).
