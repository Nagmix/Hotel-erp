# 18 — معايير القبول (Acceptance Criteria) — وحدة Care

> **10 مجموعات / 42 معياراً** مشتقة حرفياً من السلوكيات الموثقة (كل معيار مرجعه)، + **اختبار دخان (Smoke Test) من 24 خطوة** يحاكي يوماً تشغيلياً كاملاً.

---

## AC-CA-01: الهوية والهيكل (من SET)
1. لا يمكن إنشاء مستخدم داخل Care — فقط ربط مستخدم PMS موجود (SET ص5).
2. تعيين Agent يمنع رؤية عمليات Supervisor Lookup الأربع (Close/Transfer/Extend/Assign) (SET ص5).
3. شجرة Org Structure تعرض Property ثم Department ثم Designation — كلها تُجلب من PMS (SET ص10-13).
4. حذف موظف يضعه في Deleted List ويُسترجع منه (SET ص20-21).
5. لا تعديل لاسم موظف قائم (SET ص24).
6. Reporting To يعيد توجيه سلسلة التصعيد فوراً (SET ص18-19).

## AC-CA-02: تعريف المهام (من SET)
7. Sub Category تحمل: Est Time (دقائق) + Designation + Type + Charges + Feedback + Priority + 4 EscTimeout (SET ص26).
8. Multi Task تجمع مهاماً من أقسام متعددة (SET ص29).
9. اختيار Multi Task في Manual Entry يولد رقم شكوى مستقلاً لكل مهمة مكونة (SET ص31).

## AC-CA-03: الروستر (من OPR)
10. Month/Year أقل من الحالي يُرفض (OPR ص6).
11. سحب وردية على الموظف يملأ الشهر؛ على تاريخ = يوم واحد (OPR ص7/9).
12. Weekly Off على يوم يعمم على كل مماثلات اليوم (OPR ص10).
13. حذف وردية لتاريخ ماضٍ ممنوع (OPR ص9).
14. تعديل الطوابق متاح للمستقبل فقط (OPR ص14).
15. تعريف طوابق قبل ورديات يعرض رسالة منع (OPR ص11).

## AC-CA-04: الدخول/الخروج (من OPR)
16. دخول بلا روستر = 'Schedule Not Entered' (OPR ص20).
17. وردية/عطلة مخالفة = تنبيه مع سماح (OPR ص19-20).
18. F1 في الخروج يعرض المسجلين فقط (OPR ص28).
19. الخروج يتطلب تأشير استرداد Mobile/Pager (OPR ص28).
20. الموبايل يظل متاحاً لموظف الوردية التالية بالقسم (OPR ص19).

## AC-CA-05: آلة المهمة وSMS (من OPR) ⭐
21. زر Thank You هو من يبدأ المؤقت (وليس Confirm) (OPR ص36).
22. SMS التخصيص يحمل: Complaint# + Room# + Task + Spe.Ins + Est. Time + Priority + **Esc Level: 0** (OPR ص38).
23. رد `1 S` ينقل لحالة Work in Progress (OPR ص41).
24. رد `1 C` يغلق (أو Awaiting Feedback إذا Feedback=Y) (OPR ص44).
25. رد `C` قبل `S` = `TASK #1 IS NOT YET STARTED` (OPR ص40).
26. رد `S` لمهمة غير مخصصة = `TASK #1 IS NOT ASSIGNED TO YOU. WORK NOT STARTED` (OPR ص40).
27. إغلاق مشرف أثناء عمل المنفذ يرسل `COMPLAINT #1 CLOSED. CLOSED BY: <NAME> REASON: <R>` (OPR ص43).

## AC-CA-06: التصعيد (من SET/OPR)
28. تجاوز Est Time دون إغلاق يرفع Esc Level وفق سلسلة Reporting بترتيبها (SET ص18).
29. مهلة كل مستوى مأخوذة من Task Definition (SET ص26).
30. تقرير Escalation يعرض: level + escalated to + closed date (REP ص57).

## AC-CA-07: عمليات المشرف (من OPR)
31. Close يطلب Reason + Approximate Cost (OPR ص72).
32. Transfer يعرض مسجلي القسم نفسه فقط (OPR ص73).
33. Extend (D/H/M) يتمدد Elapsed تلقائياً (OPR ص76).
34. مهمة Work Start يدوية تظهر بـ Assigned To فارغ ثم Assign يخصصها (OPR ص77-79).

## AC-CA-08: التقييم والإلغاء (من OPR/REP)
35. التقييم بأربع قيم فقط: Satisfied/Not Satisfied/Not Served/Guest Unavailable (OPR ص47).
36. Cancel/Stop يعمل على غير المبدوءة + Notes إلزامية السلوك (OPR ص49).
37. تقرير Cancelled/Stopped يميز Cancelled (لم تبدأ) عن Stopped (بدأت) (REP ص64).

## AC-CA-09: المفقودات والبث (من OPR)
38. Lost & Found يعرض بيانات PMS ويضيف سجلات محلية بـ Module=outlet (OPR ص60/64).
39. Group SMS يقبل أرقاماً خارج النظام + رسالة تصل للحالة SMS Sent (OPR ص58-59).

## AC-CA-10: التقارير والصلاحيات (من REP/SET)
40. Drilldown Tasks Statistics يصل لسجل يحمل Check-in/Check-out dates (REP ص25).
41. Response Time Analysis لا تعرض Details مع Yearly (REP ص14).
42. Restrict Reports يمنع Spool/Export حسب المستخدم ويحدد Format (Excel/OpenCalc/Direct) (SET ص33).

---

## اختبار الدخان (Smoke Test — 24 خطوة)

| # | الخطوة | النتيجة المتوقعة |
|---|---|---|
| 1 | ربط مستخدم PMS كمجموعة Supervisor بقسم HK | يُحفظ ويظهر |
| 2 | بناء شجرة HK→Housekeeping Staff→Employee (بموبايل) | موظف بصورة |
| 3 | Reporting To: Staff→Supervisor→Manager→FOM→GM→MD | السلسلة تُعرض |
| 4 | تعريف Main "Room Related" + Sub "Towel" Est=10m Pri=High Esc=[5,10,15,20] Feedback=Y | محفوظ |
| 5 | روستر الشهر الحالي: General على الموظف + طوابق 1-2 | شبكة ممتلئة |
| 6 | محاولة حذف وردية أمس | **مرفوض** |
| 7 | Login الموظف بموبايله (وردية صحيحة) | ناجح بلا تنبيه |
| 8 | Login بموبايل مخالف للوردية | تنبيه + سماح |
| 9 | Manual Entry: Room 101 (مشغولة) | بيانات الضيف فوراً |
| 10 | اختيار Towel + Spe.Ins 30 حرفاً | **قطع عند 25** |
| 11 | Confirm ثم Thank You | مؤقت يبدأ + SMS Queued→Delivered |
| 12 | SMS صادر يحمل كل الحقول السبعة | النص الحرفي |
| 13 | رد `1 S` من رقم المنفذ | WIP + `TASK #1 WORK STARTED` |
| 14 | رد `1 S` مرة ثانية | `ALREADY STARTED` |
| 15 | رد `1 C` | Awaiting Feedback (لأن Y) |
| 16 | تقييم Satisfied + ملاحظة | محفوظ |
| 17 | شكوى ثانية بلا موظف مسجل (قسم آخر) | Unassigned |
| 18 | Work Start يدوي | WIP بلا Assigned To |
| 19 | Login فني القسم + Assign | تخصيص + SMS |
| 20 | Extend بـ 15m + Reason | Elapsed تمتد |
| 21 | Close من Supervisor بـ Reason + Cost=50 | إغلاق + SMS للحاضر |
| 22 | انتظار 10 دقائق على شكوى عالية الأولوية | Esc Level 1 → SMS للمستوى |
| 23 | Supervisor Lookup: Clear Pending SMS | قائمة الانتظار تفرغ |
| 24 | تقارير: Tasks Statistics drilldown + Shift List (SMS Queued) + Feedback Stats | البيانات صحيحة |

> نجاح الاختبار = التحقق الحي من AC-CA-01..10 (عدا 1/31/41 تُختبر إدارياً).
