# 18 — معايير القبول (Acceptance Criteria) — وحدة SLM

> **10 مجموعات اختبار / 46 معياراً** — تغطي القواعد المالية الحاجمة والبنى والقيود الموثقة. كل معيار مصدره النص الأصلي (تتبع قابل للتدقيق).

---

## AC-01 — دورة Prospect → CGR (الهوية والترميز)

| # | المعيار | المصدر |
|---|---|---|
| AC-01-1 | إنشاء Prospect بحقول كاملة (CEO/holding/competitors/turnover/Frequent Travelers) يحفظ ويعرض في قائمة Transfer | SLT §4 |
| AC-01-2 | التحويل يولد كوداً ببنية TTT+حرف+مسلسل: لـ"Alpha Travels" (وكالة) → TAGA### متسلسل من آخر TAGA | SLT §10 |
| AC-01-3 | مسلسل مستقل لكل (نوع+حرف): TAGA### ≠ COMA### — عدّان منفصلان | SLT §10 (V-SM-03) |
| AC-01-4 | الشركة المحولة تظهر في Company Master وSM Tool فوراً (كيان FO/AR/POS/BNQ/MEM) | SLT §10 + PRF ص9 |
| AC-01-5 | لا عكس للتحويل (Customer→Lead) — مفهوم غائب أصلاً | E-SM-02 |
| AC-01-6 | يدوي الكود في شاشة التحويل: إما مقفول أو يمر بفحص فريدية — القرار D-SM-3 | R-SM-1 |

## AC-02 — القفل الائتماني (القاعدة الأعنف)

| # | المعيار | المصدر |
|---|---|---|
| AC-02-1 | شركة Credit Limit=1000 ومديونية حالية 1200 → تسوية ائتمانية في FO **ممنوعة** | PRF §7 |
| AC-02-2 | ذات الحالة → تسوية POS ممنوعة | PRF §7 |
| AC-02-3 | ذات الحالة → تسوية BNQ ممنوعة | PRF §7 |
| AC-02-4 | ذات الحالة → الترحيل اليدوي للفاتورة ممنوع | PRF §7 |
| AC-02-5 | السماح الائتماني = No → لا تسوية ائتمانية أصلاً (كل تسوية فوري) | PRF §7 |
| AC-02-6 | تعديل الحد = سجل تدقيق (قرار P-SM-4) | R-SM-2 |

## AC-03 — شروط AR داخل Profile

| # | المعيار | المصدر |
|---|---|---|
| AC-03-1 | Credit Days لا يقبل قيمة إلا إذا Allow Credit=Yes | V-SM-18 |
| AC-03-2 | Invoice Currency تظهر على طباعة فاتورة AR لتلك الشركة | PRF §7 |
| AC-03-3 | Blacklist=Yes يستوجب reason+authorizer قبل الحفظ | V-SM-19 |
| AC-03-4 | عرض تفاصيل Blacklist متاح في Modify فقط | E-SM-08 |
| AC-03-5 | Watch List+To Date تظهر الشركة في تقرير Watch List "Falling in month" الصحيح | PRF §7 + REP §6 |

## AC-04 — Revenue Discount Master

| # | المعيار | المصدر |
|---|---|---|
| AC-04-1 | Discount ID رقمي ≤4 خانات (رفض alpha) | V-SM-05 |
| AC-04-2 | Active Date < اليوم → رفض (اليوم أو أحدث، ddmmyy) | V-SM-07 |
| AC-04-3 | كود F&B: خصم FOOD=10%/LIQUOR=5% منفصلان يطبقان كل على باكسه في فاتورة POS | PRF §5 |
| AC-04-4 | خصم منتهي (Expiry ماض) لا يطبق | PRF §5 |
| AC-04-5 | ربط Master بحساب شركة → الخصم يظهر في أسعار LUK §3 ("Discount applicable... reflected") | PRF §7 + LUK §3 |

## AC-05 — الوكلاء (Allocation/Forecast/Release)

| # | المعيار | المصدر |
|---|---|---|
| AC-05-1 | From Date للتخصيص يفتح بتاريخ المحاسبة (قابل للتحرير) | BR-SM-13 |
| AC-05-2 | Over-book 20% مع 10 غرف → 12 غرف قابلة للحجز قبل التنبيه | PRF §12 |
| AC-05-3 | Module Attribute #8=YES → Day Access (تخصيص يومي)؛ NO → Week Access | BR-SM-11 |
| AC-05-4 | Release Dates: From مولد آلياً من start + cutoff days لكل مدى | PRF §14 |
| AC-05-5 | بعد فتح تفعيل Cutoff: طلب حجز يجاوز cutoff → prompt Inside/Outside | BR-SM-14 |
| AC-05-6 | Forecast يخالف Allocation → تحذير (لا قفل) | V-SM-24/D-SM-4 |

## AC-06 — Executive Planner

| # | المعيار | المصدر |
|---|---|---|
| AC-06-1 | دخول user/password يفشل لمستخدم غير مربوط بـSales Executive (قبل تفعيل التعميم) | V-SM-22 |
| AC-06-2 | Appointments: reschedule/cancel/transfer كل يستوجب reason (وTransfer يحدد مندوباً) | BR-SM-17 |
| AC-06-3 | Things To Do: مهمة Important في خانة 10:00 تظهر مصنفة وتُوسم completed | BR-SM-18 |
| AC-06-4 | زر غير المكتمل يعرض المهام الباقية فقط | SLT §9 |
| AC-06-5 | Logout ينهي جلسة الـPlanner تحديداً (لا النظام كله) | E-SM-06 |

## AC-07 — أداة 360° والاستعلامات

| # | المعيار | المصدر |
|---|---|---|
| AC-07-1 | عرض Reservations يظهر Current+Cancelled+No-Show وPast بإcheckbox | SLT ص12 |
| AC-07-2 | عرض Receivables: opening/charges/payment/closing بتاريخ قطع=Accounting date | BR-SM-29 |
| AC-07-3 | عروض Activity/Entertainment/Guest Viss افتتاحياً للشهر السابق | BR-SM-30 |
| AC-07-4 | General Information لا تقبل تحريراً | E-SM-05 |
| AC-07-5 | Browse Company بمدى Credit Limit 1000-2000 → شركات داخل المدى فقط | LUK §1 |
| AC-07-6 | Hotel Position: نقر room type=Horly؛ Over Booking checkbox يظهر الفائض | S-SM-16 |

## AC-08 — التقارير (قيود المعالجة)

| # | المعيار | المصدر |
|---|---|---|
| AC-08-1 | Market Share بمدى عابر لشهرين → رفض (شهر واحد) | V-SM-09 |
| AC-08-2 | Sales Performance Report بمدى 40 يوماً → رفض (31) | V-SM-12 |
| AC-08-3 | Contribution Datewise عابر للشهور → رفض | V-SM-14 |
| AC-08-4 | Business Lost بTo مستقبلي → رفض | V-SM-08 |
| AC-08-5 | كل تقرير: خيارات Display/Spool/Print/Export + Cancel | REP عائمة |
| AC-08-6 | Company Contribution: CGR/NON-CGR مفصولان + F&B breakup بأعمدة مخصصة (column#/heading) | REP §16 |

## AC-09 — قنوات التسويق

| # | المعيار | المصدر |
|---|---|---|
| AC-09-1 | Company Letters بdesignation=CEO → مرسل=بريد الشركة؛ بغيره → قائمة contacts | BR-SM-33 |
| AC-09-2 | Birthday List: فترة MM/YY مع Prospect محدد → أعياد contacts + Frequent Travelers معاً | REP §5 |
| AC-09-3 | Labels بم53 أعمدة يطبع بالتنسيق الصحيح | REP §11 |
| AC-09-4 | (منصة) إرسال Newsletter عبر SMTP يعوض Outlook بمرفقات + Subject | F-SM-5 |

## AC-10 — سلبية وأداء

| # | المعيار | المصدر |
|---|---|---|
| AC-10-1 | لا قيد GL يولد من أي معاملة SLM (كل الأثر مفوض) | 11 §4 |
| AC-10-2 | Budget لا يشمل Prospects (CGR فقط) | BR-SM-07 |
| AC-10-3 | Update Company Profile: معاينة عدد المتأثرين قبل الحفظ (قرار R-SM-2) | GAP-SM-P5 |
| AC-10-4 | صورة Hotel Profile بغير BMP → رفض (أو: قبول صيغ حديثة بقرار بديل موثق) | V-SM-28 |
| AC-10-5 | Daily Occupancy: إدخال backdated يظهر في تقارير MIS للسنة المالية | SLT §1 |

---

## خارطة اختبار دخان (Smoke Test) — 26 خطوة

1. إنشاء Prospect → حفظ ✓
2. Daily Sales Call للـProspect + follow-up غداً ✓
3. Follow-up/Schedule Report يعرض الغد ✓
4. Entertainment Entry (Type=Entertainment + Outlet) ✓
5. Business Loss Entry (competitor + reason) ✓
6. Business Lost Report (Reason Wise) ✓
7. Transfer Prospects → كود TAGA### ✓
8. فتح Company Profile للمحولة: AR Terms (Limit/Days/Interest) ✓
9. Blacklist شركة → reason+authorizer ✓
10. Watch List تقرير "Falling in month" ✓
11. ربط Revenue Discount (F&B menu-wise) بعميل ✓
12. Link Rates (Non-rack + Exclude tax) ✓
13. Company Rates-Datewise يعرض الخصم ✓
14. Agent Allocation (From=Accounting date) + Over-book% ✓
15. Agent Forecast مطابق ثم مخالف (تحذير) ✓
16. Release Dates (cutoff) + (منصة) تفعيل INI مماثل ✓
17. تخطي حد ائتماني → محاولة تسوية FO/POS/BNQ → منع ✓✓✓
18. Map Users/Sales Exec → دخول Planner ✓
19. موعد + reschedule بسبب + transfer لمندوب ✓
20. TODO مهم 10:00 → complete → عرض غير المكتمل ✓
21. Sales Manager Tool: 10 عروض + Position ساعي + Yearly/Overbook ✓
22. Browse Company بمدى Credit ✓
23. Market Share (شهر واحد) ✓ / رفض شهرين ✓
24. Company Contribution بأعمدة مخصصة ✓
25. Company Letters: CEO vs contact (SMTP) ✓
26. Birthday List MM/YY لـProspect ✓

> **بوابة النجاح:** 42/46 من AC إلزامية قبل الاعتماد (تُستثنى AC-01-6/AC-02-6/AC-09-4/AC-10-4 كقرارات تأجيل موثقة).
