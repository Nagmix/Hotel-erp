# 18 — معايير القبول (Acceptance Criteria) + Smoke Test — وحدة HRP

> **10 مجموعات / 46 معياراً** قابلة للتحقق آلياً/يدوياً، + Smoke Test من 28 خطوة.

---

## AC-01 — محرك الأجور (ED Engine) 🔴
1. يُعرَّف ED Code بكل نمط من الستة ويُطبع payslip بترتيب Print sequence.
2. **الشريحة Normal تعطي 500.00 للمثال الموثق (2500×20%)** — اختبار رقمي بالوثيقة.
3. **Cumulative تعطي 350.00** (100/150/100).
4. **Step Over تعطي 400.00** (300+100).
5. **Eligibility: ≤6500 Eligible / >6500 Not** وتُعطّل حقول Amount/Min/Max.
6. Min/Max clamp يعمل عند تجاوز النطاق.
7. Test Equation يرفض معادلة غير صالحة قبل الحفظ.
8. تعريف Temporary لا يظهر في payslip ويُستخدم في معادلة Basic الموثقة.

## AC-02 — الخصومات بالأولوية (BR-HR-06) 🔴
1. خصمان بأولويتين → يُنفذ الأدنى أولاً.
2. F3-equivalent يعيد الترتيب.
3. **Partial=Yes + أرباح 1500 وخصم 1700 → الخصم كامل 1700.**
4. **Partial=No → صفر خصم.**
5. Carry Forward=Yes → الباقي أولوية الشهر التالي.
6. Take Home%=20 → الخصومات تقتطع من 80% كحد أقصى.

## AC-03 — دورة الفترة (Starting Period) 🟠
1. Daily/Weekly/Fortnightly/Monthly تحسب To date الموثقة.
2. **From=21-Dec → To=20-Jan** (متدحرج عبر السنة).
3. Preview قبل الحفظ.
4. أول إقلاع يقفز للشهر التالي.
5. Transaction خارج الفترة تُعالج ضمن فترتها.

## AC-04 — الحضور 🟠
1. مصفوفة الأعلام الخمسة تُفسر الأكواد (Overtime بالساعات — Working يوم).
2. نصف يوم (.5) يقبل في WRK وABS.
3. استيراد flat file بالبنية (EMP7/DATE8/CODE3/DAYS5,2) للترحيل.
4. كود غير معرّف → سجل رفض (قرار تصميمي موثق).

## AC-05 — المعالجة والإقفال 🔴
1. Payroll Run ينفذ لكل فئة بإيقاعها.
2. ACCEPT values تُطلب **قبل** التنفيذ (pre-run) وتُطبق على الفئة.
3. موظف بلا حضور → لا يستفيد من FDA/Accept.
4. Round الثلاثي للصافي (2516.65/.50 → 2516.50/2517.00/2516).
5. **Closed حبيبي (قسم واحد)** يجمد ذلك القسم فقط.
6. Cancel يعيد الفتح للمعالجة.

## AC-06 — الإجازات 🟢
1. Leave Ledger يعرض prev/curr opening وclosing محسوب.
2. نصف يوم عبر منتقي (بديل F6).
3. Leave Posting يخصم المستحقة بموازاة Attendance Code.
4. Carry-forward قياسي HRMS.

## AC-07 — القروض 🟢
1. القسط يُحسب آلياً من Principal/Installments.
2. **الأصل غير قابل للتعديل بعد الإنشاء** (submit semantics).
3. Return مبكر يقلل الرصيد.
4. تقرير Statement بـ opening/collection/closing.

## AC-08 — AR→Payroll 🔴
1. فاتورة AR لموظف (من POS Staff) → تظهر في Transfer queue.
2. ربط company code ثم Save.
3. الدورة التالية تحمل خصماً بالمبلغ.
4. تقرير Additional Salary يعكسها.

## AC-09 — الإجرائية (PF/ESI/PT) 🟡
1. Statutory Rule Set قابل للتهيئة ببلد غير الهند دون أخطاء.
2. Supplementary PF/ESI/PT تُسجل وتظهر في Check List بفئة Non Employee.
3. PF split يظهر مساهمة صاحب عمل (admin+EDLI×2).
4. Bonus بـ4 نسب يحسب للمثالين (≤cutoff / >7500) وRT PT يعيد الاحتساب.

## AC-10 — الأمن والتدقيق 🟠
1. User Permission على Category يقيد مستخدماً من فئة أخرى.
2. Payroll Audit يعرض old/new لسجل معدّل ووسم Deleted.
3. لا تعديل على مغادر.
4. F&F يطبع Final/Vacation مع Indemnity اختياري.

---

## Smoke Test (28 خطوة — مسار تشغيل 10 دقائق)

| # | الخطوة | النجاح |
|---|---|---|
| 1 | إنشاء Category (Monthly, Take Home 20%, Round Nearer .50) | يُحفظ |
| 2 | إنشاء ED Codes: BAS (Earning) + PT (Regular Deduction) | نوعان صحيحان |
| 3 | ED Calculation لـ BAS: Calculate From=Master + معادلة Basic×Days/Total | Test ينجح |
| 4 | ED Calculation لـ PT: Slab Cumulative بأشرطة الوثيقة (10%/15%/20%) | يُحفظ |
| 5 | Starting Period للفئة (Monthly من 1 الشهر) | To = آخر الشهر + Preview |
| 6 | توظيف: Job Opening → Applicant → Offer (Template) → Employee | سلسلة متصلة وEMP# auto |
| 7 | Rate Master للموظف (BAS=1000) + Leave Group | الإجمالي الحي = 1000 |
| 8 | Attendance: 30 Working | مصفوفة تُفسر |
| 9 | Default Post للفئة (30) | يُقبل (≤نطاق) |
| 10 | Payroll Run للفئة → pre-run ACCEPT فارغ (لا Accept codes) | يعمل |
| 11 | النتيجة: BAS=1000 (30/30) | ✓ |
| 12 | PT Cumulative على 1000: 100 (شريحة1) | ✓ (500 مثال/2500 — تناسب) |
| 13 | صافٍ = 900 + Round .50 | 900.00 |
| 14 | Salary Abstract + Details | يظهران بنفس الأرقام |
| 15 | إجازة نصف يوم → إعادة المعالجة | days تتغير |
| 16 | Take Home: أضف خصماً 1700 على أرباح 1500 (Partial=Yes) | خصم 1700 (اختبار الوثيقة) |
| 17 | Partial=No → إعادة | صفر خصم |
| 18 | قرض 5000/10 قسط | القسط 500 auto |
| 19 | معالجة تالية تخصم 500 | ✓ |
| 20 | Loan Return 200 | الرصيد ينقص |
| 21 | AR فاتورة موظف 150 → Transfer → link | في queue |
| 22 | معالجة تالية تحمل 150 | ✓ |
| 23 | Bonus Run (Ext 8.35% مثال) + RT PT | يعيد PT |
| 24 | Closing لقسم واحد فقط | حبيبية تعمل |
| 25 | Statements Cash + Denomination | كسر صحيح |
| 26 | Payroll Audit: عدّل BAS ثم استعرض | old/new ظاهران |
| 27 | Payroll User Rights: قصر مستخدماً على فئة | المنع يعمل |
| 28 | F&F لمغادر + طباعة Vacation | تقرير يطبع |

> معايير الرجوع: أي فشل في الخطوات 2-4/11-12/16-17 = **عيوب محرك (P0)** — تعود إلى AC-01/02.
