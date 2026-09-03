# 01 — محرك التقارير والبنية التحتية (FOM-REP)

> كل تقارير FO تشترك في خط إنتاج واحد. هذا الملف يوثق المحرك والبنية التحتية العرضية التي تعمل عليها ~135 تقريراً — وهي أغلى نتيجة معمارية في REP.

---

## 1. خط الإنتاج الموحد (Universal Report Pipeline)

```
نقر مزدوج على بند التقرير
   ↓
شاشة المعايير (From/To · Options · Checkboxes · F1 lookups)
   ↓
Ok
   ↓
شاشة الإخراج: Option dropdown (Display / Spool / Print / Export) + Continue / Cancel
   ↓
Continue → شاشة "report processing status"
   ↓
الناتج (شاشة / طابعة / ملف Spool / تصدير)
```

**القواعد الحرفية:**

- الجملة التأسيسية (REP ص5): "The reports can be generated in four different options like **display, print, spool or export**."
- الذيل الموحد في ~100 تقرير: "Select one of the report output options (Display, Spool, Print or Export)... Click Cancel to terminate the process."
- الإحالة الطباعية: "For complete information on printing the report refer **Getting Started manual**." — **مرجع خامس خارج الحزمة الـ65** (بعد Windows/Network/PMS/POSgeneric في وحدات أخرى) → يُدرج في UNK-079.

## 2. معرّفات البرامج (Program IDs)

- كل تقرير له Program ID داخلي يظهر في نافذة منبثقة بعد فتح بند التقرير والضغط على Enter (أحياناً مرتين).
- **المثال الموثق**: `FOMRR15` ("FOMRR15 is the ProgramID in this case" — REP ص95) → اصطلاح التسمية المستنتج: `FOM-RR-##` = Front Office Module – Report ##.
- Program ID هو مفتاح التسجيل في INI Switch 63 (طباعة التسلسل — §4) وفي PROGRAM ID FOR PRINT FORMS (SYS).

## 3. تخصيص الطباعة عبر Setup (بوابات إعداد عابرة للوحدات)

التقارير "ذات النماذج الخاصة بالعميل" (Customer-specific forms) تتطلب إعدادين مسبقين **حرفياً في كل مرة**:

| البند | الموضع | يخدم |
|---|---|---|
| PROGRAM ID FOR PRINT FORMS | SYS → GENERAL SETUP | Reservation Guest Message Print (6) · Print Voucher (8) · Coupon Printing (24) · Message Printing (25) |
| USER DEFINED PRINT FORMS | FO → SETUP | نفس البنود أعلاه (تعريف مواصفات النموذج) |

وتوجد **عائلة تقارير معرّفة من المستخدم** تتطلب Setup مسبقاً في FO SETUP:

| التقرير | الإعداد المطلوب (حرفياً) |
|---|---|
| Managers Report (126) | "The report specifications have to be defined under **SETUP MANAGER REPORTS**" |
| Comparative MIS Report (127) | "defined under **COMPARATIVE MIS SPEC**" |
| MIS Revenue Report (128) | "**MIS Revenue Grouping**... + **SETUP MIS REVENUE**" |
| Oneline GL Print (101) | "defining the column specifications... in the **Setup Guest Ledger Report**" |
| User Defined Report (104) / FO Budget Report (106) | تقرير برقم Report# معرف مسبقاً (F1 help) |
| Manager Report Creation (135) | "Once this setting is done, the **MANAGER REPORT CREATION** application can be run" — معالجة دفعية تُنشئ البيانات قبل توليد Managers Report |

**النمط المعماري**: التقرير الحاصل (Report) يُفصل عن مصدر بياناته الجاهز (Creation/Setup) — نمط ETL دفعي (يظهر مجدداً في 135: "After the data processing is complete, click Exit").

## 4. طباعة التقارير المتسلسلة (Reports in Sequence Print — 107)

**الغرض**: طباعة قائمة طويلة من التقارير اليومية بنقرة واحدة ("This option is helpful to the User where he wants to print a long list of various reports on a daily basis").

**خطوات التعريف (كما وردت حرفياً — REP ص95-96):**

1. استخراج Program IDs لكل التقارير المطلوبة (فتح البند → Enter/Enter → قراءة النافذة المنبثقة).
2. فتح **ملف INI** في مجلد منتج Fortune PMS على الخادم ("Locate and open the INI File located in the Fortune PMS product folder in your computer server").
3. الانتقال إلى **Switch No. 63**.
4. إدخال Program IDs مفصولة بفواصل.
5. Save + Close.
6. من شاشة Reports in Sequence Print: زر **Execute** يولّد ويطبع التقارير واحداً تلو الآخر → Exit.

**الأثر المعماري**: عائلة INI تتوسع (SYS: 368 ONLINEFBCOSTING · FXD: 475 DepMethod · POS: 511 autodeductionliqsale · **FO-REP: 63 SequencePrint**) — و`63` أول مفتاح يُعرّف به **محتوى قائمة تشغيل** (playlist) وليس سلوكاً واحداً → UNK-080.

## 5. تقرير الشرطة المخصص بملف (PMSPOL.INI → POL.SPC)

أغرب آلية تخصيص في الحزمة (Police Report 23.4 — REP ص25-26):

1. "Locate and open the **PMSPOL.INI** file located in the **Fortune PMS product folder** in your computer server."
2. تعبئة To / From / Subject Line / footer.
3. "On the file menu click **Save As** and save the file as **POL.SPC** in the same **dll folder**."

**التحليل**: تخصيص نموذج نظامي (شرطة) عبر ملف نصي يُحفظ بامتداد .SPC بجوار الـ DLLs — بعد FIMSHTBL (FXD — اسم جدول مسرب) هذه **ثالث بنية تحتية ملفية مسربة**؛ تكشف أن طبقة التقارير القديمة file-driven وليست DB-driven بالكامل → UNK-079.

## 6. أنماط التفاعل الموحدة (Interaction Patterns)

| النمط | الاستخدام | الشواهد |
|---|---|---|
| **F1 / نقر مزدوج / زر Help** ثلاثي القنوات للاسترجاع | اختيار كود (Company/Group/Tax/Bill/Room/Res) | عشرات التقارير ("Alternatively you can press F1 on the keyboard") |
| **النقر المزدوج كاختيار** | "double-click on the desired room #" (68.4) · "Double-click to select the desired phone number" (SMS) | اختيار من نافذة Help |
| **Enter كمؤشر تقدم** | "Hit Enter on your keyboard to move the cursor to the Date field" (22) — الحقول تتوالى بالـEnter | 84/92/98/125 |
| **Auto-populate عند الاختيار** | Reg# → Guest Name/Arrival/Departure (79) · Group Code → Name (75) · Report# → Name (128) | ربط UI-بياني |
| **Deactivate عند القفل** | "the other two options will be deactivated" (104 Print Net Values) · Cancellations → Mem. ID/Arrival Date معطلة (8) | XOR بصرّي |
| **Print Status screen** | "you can view the report processing status" (1) | شاشة معالجة موحدة |
| **Skip One Line / Skip Rows** | Wakeup Call (32 "Skip One Line") · HRP Signature List | طباعة متوازنة |
| **80/132 عموداً** | 13 تقريراً على الأقل (Expected Arrivals/Occupancy Statistics/Night Report/MIS/Settlement Summary/User Defined/FO Budget...) | قوالب طباعة ورقية |
| **Print or Email** | Print Voucher (8) — القناة الرقمية الوحيدة | بريد فقط لا شبكات |

## 7. معايير الفرز والتجميع المتكررة (Parameter Vocabulary)

- **Sort by**: Guest Name Wise / Reservation # Wise (12-13) · Room # Wise / Time Wise / Company Wise (14) · Res No. / Arrival Date / Group / Company (18) · Departure Time/Room#/Guest Name (68.2) · First Name **or Middle Name** (95 — اختيار عرض الاسم!) · Dept/Code/Item Group/Classification/Room No/User (110).
- **Details / Summary**: 15 · 18 · 23.2 · 52 · 65 · 113.3 · 134 + **Summary at the end** (44).
- **Include Special Room(s)**: 1 · 23.2 · 31.1 · 43 · 72 · 74 · 76 · 68.2 — عائلة مرشح متكررة (الغرف الخاصة = OOO/Dummy/تجهيز).
- **Include Complimentary / House Guest**: عائلة إحصائية متكررة (65.2 · 66 · 67 · 115-132) — قراري إدراج في ARR/الإشغال.
- **Guest Status / Guest Classification**: مرشح تصنيفي متكرر (23.1 · 36 · 40 · SMS).
- **Property dropdown**: متكرر في كل التقارير متعددة الفنادق (5 · 10 · 11 · 12-14 · 17-18 · 56 · 64 · 65.4 · 122 · 133) — يؤكد البنية متعددة المنشآت.

## 8. علاقة الإخراج بالأرشفة

- **Spool** موثق كخيار أولي في معظم التقارير و"save the C form with an appropriate name to a desired location **for future references**" (23.5) — Spool = أرشفة إلكترونية يدوية.
- **Export** خيار رابع دون تفصيل صيغة التصدير في REP (لا CSV/XLS محدد) → UNK-081.
- في SMS/Message Printing: "Display to view the messages **on a notepad**" (6) — العرض النصي عبر Notepad (تسريب تقني لبيئة سطح مكتب Windows).
