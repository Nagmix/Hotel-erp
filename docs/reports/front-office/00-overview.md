# 00 — نظرة عامة على طبقة تقارير Front Office (Phase 7)

> **المصادر:** FOM-REP (120 ص / 4,507 أسطر — أضخم ملف تقارير في الحزمة) + FOM-SMS (14 ص — نظام تنبيهات SMS).
> **الموقع في المشروع:** هذه الطبقة تُكمل — ولا تكرر — `docs/modules/front-office/08-reports.md` (الذي وثّق 10 مخرجات تشغيلية من REG/CAS قبل قراءة REP).

---

## 1. النطاق والإحصاء

| البند | القيمة |
|---|---|
| ملف المصدر الرئيسي | `FN6i-NT-FOM-REP.txt` (120 ص) |
| ملف المصدر الثانوي | `FN6i-NT-FOM-SMS.txt` (14 ص) |
| عدد بنود القائمة المرقّمة | **135 بنداً** (مع فجوات ترقيم: 19، 34، 53، 62 غائبة من TOC وال متن — تقارير تاريخية حُذفت) |
| بنود فرعية مرقّمة | 23.1–23.7 (الأمن) + 31.1–31.8 (التدقيق) + 46.1–46.3 (حالة الغرف) + 65.2–65.4 (التوقعات) + 68.1–68.4 (المغادرة) + 113.1–113.3 (غسيل) = **28 تقريراً فرعياً** |
| بنود غير مرقّمة في المتن | Guest Reg. Card · Occupancy Report · Guest Ledger Breakup · Cancellation/No Shows · User Defined C Form — **5 بنود** |
| بنود TOC بلا متن | **Report Designer + IDS Crystal Report Designer** (في الفهرس فقط — الجسم ينتهي عند User Defined C Form → UNK-078) |
| تقدير إجمالي التقارير الموثقة فعلياً | **~135 تقريراً/مخرجاً قابلاً للتوليد** |
| إجمالي صفحات الوثيقة | 134 ص (أضخم من HRP-REP 133 ص) |

**التعريف الرسمي للوحدة** (REP ص5 — حرفياً):

> "Reports is a sub-module under Front Office Module... Reports is used by Front Office to get instant access to information and print the information for documenting or auditing purposes. The reports can be generated in four different options like **display, print, spool or export**."

الجملة الأخيرة هي **المفتاح المعماري لكل التقارير**: قناة إخراج رباعية موحدة (Display / Print / Spool / Export) تنطبق على ~135 تقريراً عبر قائمة Option dropdown + زر Continue — نمط توحيد قسري لا مثيل له في الوحدات التشغيلية.

## 2. العائلات الموضوعية (خريطة الكتالوج)

| العائلة | البنود | عدد | ملف التوثيق |
|---|---|---|---|
| الحجوزات والوصول | 1–23 + Cancellation/No Shows | ~24 | `02-reservation-arrival-reports.md` |
| الأمن والامتثال النظامي | 23.1–23.7 + 48 + 50 + 58 + 70 + 93 + 94 + 96 + 97 + 119 | ~15 | `03-security-statutory-reports.md` |
| الإشغال والمقيمون والتدقيق | 24–50 (باستثناء الأمن/الإحصائي) | ~27 | `04-occupancy-inhouse-audit.md` |
| الأسعار والخطط والتوقعات والمغادرة | 51–71 | ~21 | `05-rates-plans-forecast-departures.md` |
| المالية والقيود والدفاتر | 72–106 + Guest Ledger Breakup | ~32 | `06-financial-ledger-reports.md` |
| الدعم التشغيلي (HK/غسيل/مفقودات/تسلسل) | 107–114 | ~11 | `07-operations-support.md` |
| MIS والتحليل الإداري | 115–135 | ~21 | `08-mis-analytics.md` |
| محرك التقارير والبنية التحتية | — (عرضي) | — | `01-report-engine-infrastructure.md` |
| مصفوفة قواعد التواريخ | — (عرضي) | ~25 قاعدة | `09-date-validation-matrix.md` |
| تنبيهات SMS | FOM-SMS §1–3 + 8 خدمات | 8 خدمات | `10-sms-alerts.md` |

## 3. أبرز الاكتشافات البنيوية (Session 16)

1. **قناة إخراج رباعية موحدة**: Display / Spool / Print / Export + Continue/Cancel + شاشة "report processing status" — خط إنتاج واحد لـ135 تقريراً.
2. **بنية تحتية ملفية مسربة ثالثة**: `PMSPOL.INI` → يُحفظ كـ `POL.SPC` في مجلد dll لتخصيص تقرير الشرطة (To/From/Subject/footer) — بعد FIMSHTBL (FXD) وPMSPROD.INI.
3. **INI Switch No. 63** لطباعة التقارير المتسلسلة (Program IDs مفصولة بفواصل مثل `FOMRR15`) — سلسلة INI تتوسع (368/475/511 → 63).
4. **"This mandatory report"** — Occupancy Statistics التقرير الوحيد الموصوف رسمياً بـ"إلزامي" في كل الحزمة.
5. **صيغة حسابية حرفية موثقة**: "Room Balance = Previous Opening Balance + Current Tariff Charge + Luxury Tax" (On Line Room Balance).
6. **عائلة قواعد تواريخ كثيفة**: ~25 قاعدة صريحة (future-only / past-only / same-month / ≤31 يوم / ≤30 يوم / ≤10 أيام!) — أغلى مصفوفة تحقق في المشروع → `09-date-validation-matrix.md`.
7. **XOR أعمدة**: Night Report (80 عموداً = يوم+شهر مع YTD اختياري · 132 = يوم+شهر+سنة مع YTD معطّل!) — منطق حصري معكوس غير بديهي.
8. **بوابات إعداد عابرة للوحدات**: 6 تقارير "معرّفة من المستخدم" تتطلب Setup مسبقاً في FO SETUP (Manager Reports / Comparative MIS Spec / MIS Revenue Grouping / Setup MIS Revenue / Setup Guest Ledger Report / User Defined Print Forms) + PROGRAM ID FOR PRINT FORMS في SYS GENERAL SETUP.
9. **أول بريد إلكتروني موثق في التقارير**: Print Voucher يوفر "Print or **Email**" — قناة إرسال رقمية.
10. **تناقضان جديدان**: C-FO-01 (Guest Photo Reg. Card موثق مرتين بنطاقين مختلفين) + C-FO-02 (تسمية "Fortune Next Enterprise 2.0" في FOM-SMS مقابل FortuneNext 6i) — الثاني/الثالث في السجل بعد C-FB-01.

## 4. علاقة هذه الطبقة بالوحدات الأخرى

| الجسر | الاتجاه | الشاهد |
|---|---|---|
| FO → TEL | استهلاك | Guest Telephone Bill (79): تفصيل مكالمات "without any consolidation" عبر Reg# |
| FO → POS | استهلاك | Consolidated Tax Register (94): FO + POS معاً · Misc Sales Register (80): POS dropdown |
| FO → MGT | استهلاك | HK Item Check List (109): مخازن · HK Consumption (110): Manual/Inventory rate types |
| FO ↔ HK | تشغيلي | Room Verification (108): مطابقة حالة الغرف FO-vs-HK + Discrepancies Only |
| FO → SYS | اعتماد | PROGRAM ID FOR PRINT FORMS + INI Switch 63 + دليل Getting Started (مرجع خامس!) |
| FO → Guest History | استهلاك | GH Arrivals (17) + Birthday List (47): "has to be linked to the Guest History" |
| SMS → Care | توازٍ | عائلة SMS ثانية بعد SMS Queued في Care — UNK-082 (آلية البوابة غير موثقة في كليهما) |

## 5. ملاحظات الجرد (FOM-REP)

- **فجوات الترقيم** (19/34/53/62): بنود في TOC لا متن لها — أدلة حذف تاريخي لتقارير، لا تعارضاً.
- **الترتيب ليس مجموعات**: الترقيم متسلسل لكن التجاور غير موضوعي دائماً (Security رقم 23 بين بطاقات التسجيل والكوبونات) — العائلات في هذه الطبقة أعيد تجميعها موضوعياً مع الإبقاء على أرقام المتن للرجوع.
- **الحزمة تذكر 4 تقارير Forecast في المقدمة** ("This option gives 4 different forecast Reports") لكن TOC يعرض 3 فقط (65.2/65.3/65.4) — الرابع غائب (ترقيم 65.1 محذوف) — يُسجل ضمن UNK-078.
