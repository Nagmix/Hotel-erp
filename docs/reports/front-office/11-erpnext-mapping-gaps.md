# 11 — تحويل طبقة تقارير FO إلى ERPNext + فجوات (Phase 7)

> Mapping + Gaps لطبقة التقارير (135 تقريراً + SMS). مرجع الوحدة الأم: `docs/modules/front-office/16-erpnext-mapping.md`.

---

## 1. جدول التحويل F-FOR-1..14

| # | عنصر FN6i | مقابل ERPNext | القرار |
|---|---|---|---|
| F-FOR-1 | **محرك الإخراج الرباعي** (Display/Spool/Print/Export) | Query/Script Report + Print Format (HTML) + "Download" (XLSX/CSV/PDF) | 1:1 — Display=شاشة العرض، Spool=جدولة الطباعة (Print Queue)، Print=Format، Export=زرو التصدير الأصلي (أغنى من الأصل!) |
| F-FOR-2 | **~135 تقريراً** | تُقسم: Query Report (فلترة SQL) للمخزنية/الإحصائية + Script Report للمالية المعقدة | بناء Report Layer واحد لكل عائلة (9 عائلات → ~40 تقريراً حقيقياً بعد دمج التوائم 80/132) |
| F-FOR-3 | **Reports in Sequence Print** (INI 63) | **Print Bundle / Report Book** (طباعة دفعة) أو Script Report مجمّع + Print | أصل واحد ~2 أسبوع: قائمة مخصصة تُحفظ (Playlist) بدل تحرير INI يدوياً |
| F-FOR-4 | **PMSPOL.INI → POL.SPC** (نموذج شرطة) | Print Format مخصص (Jinja) على نفس DocType | تحرير من الواجهة بدل ملف dll — إغلاق UNK-079 |
| F-FOR-5 | **Guest Ledger Balance / Oneline GL / GLB** | Ledger (GL) + تقرير Account Balance مخصص + Print Format سطر واحد | الأصعب: GL الربط مع FoFolio — يبنى فوق Payment/Invoice (راجع 16-erpnext للوحدة) |
| F-FOR-6 | **صيغة Room Balance** (75) | حقل محسوب (Server Script) أو Formula Field في التقرير | نقل حرفي قابل للاختبار الرقمي (AC) |
| F-FOR-7 | **Night Report (Oprn) / N/A Adjustment** | **قفل يومي (Day Close) + تقرير إغلاق** + Journal الإقفال | يعتمد على أصل Night Audit المصمم في الوحدة الأم؛ تقارير الليل تُولّد من حالة القفل |
| F-FOR-8 | **MIS /A /B /DMY /DateRange / Company Contribution / Hotel Statistics** | Dashboard + Query Reports على Booking/Guest/Segment | الأبعاد الأربعة (Nationality/MarSeg/BusSrc/Company) = **Dimensions/Custom Fields** موحدة |
| F-FOR-9 | **Budgets + FO Budget Report + Budget Variance** | ERPNext Budget (ضد Cost Center/Account) + تقرير Variance | مطابقة عالية؛ إضافة بُعد Segment كCustom Field |
| F-FOR-10 | **Managers/MIS Revenue/Comparative MIS + Creation (135)** | **Report Builder محفوظ + Scheduled Generation** (Materialized: جدول مُلء دفعياً) | نمط Prepared Report — يحتاج Job + Last Processed Date |
| F-FOR-11 | **SMS الثماني + Department Alert** | **Notification** (Email/SMS/Webhook) + SMS Settings/Gateway + قوالب Jinja | الإخطار الحدثي (New Check-in/Room Transfer/High Bill/Complaint) عبر hooks الموثقة |
| F-FOR-12 | **Watch List + Audit** | Custom DocType (Watch Log) + Versioning | unmark = إدخال عكسي — لا Boolean |
| F-FOR-13 | **HK Item/Consumption (109/110)** | Stock Balance + Stock Ledger (استهلاك Issue/Return) | جسر جاهز من mapping MGT |
| F-FOR-14 | **Laundry/Lost&Found/Coupons/Reg Cards** | Print Format + DocTypes موجودة (فوق mapping الوحدة الأم) | أصوات طباعة أكثر منها تقارير |

**التقدير الإجمالي**: طبقة التقارير كاملة ≈ **8-10 أصول مخصصة / 5-7 أسابيع** بعد استقرار DocTypes الوحدة الأم — أثقل من أغلب الوحدات التشغيلية لأنها تُبنى فوق كل شيء (طبيعة Display Layer).

## 2. فجوات GAP-FOR-*

### فجوات تصميم (D)

| ID | الفجوة | الأثر | الشاهد |
|---|---|---|---|
| GAP-FOR-D01 | **صلاحيات صفرية على التقارير**: لا ذكر User/Role على أي من الـ135 — وحدة بالكامل بلا صلاحيات (ال9/17 كذلك كنمط، لكن هنا أشد لأن التقارير تشمل الشرطة/الضرائب/الأرصدة) | أي reproduction يجب أن يفرض Report Permission Matrix (Dashboard/Role) | REP كله |
| GAP-FOR-D02 | **month-boundary الـ15 تقريراً** قيود أرشيفية تمنع التاريخ العابر للشهر | تعارض مع متطلبات التقارير الحديثة (نطاق حر) | مصفوفة §3 |
| GAP-FOR-D03 | **80/132 XOR المعكوس** (102: 132 بلا خيار YTD!) | سلوك غير بديهي موثق لكنه يربك المستخدم — يُهجر مع إبقاء YTD دائماً | 102/104 |
| GAP-FOR-D04 | **Report Designer + IDS Crystal** في TOC بلا متن | طبقة تخصيص غير موثقة (Crystal Report — خط تقني مغلق) | TOC vs جسم |
| GAP-FOR-D05 | **Export بلا صيغة موثقة** | لا CSV/XLS محدد في REP (مقابل Excel موثق في MNT/MGT) | قناة الإخراج الرابعة |
| GAP-FOR-D06 | **PMSPOL/INI تحرير ملفات على الخادم** = صلاحيات خادم مطلوبة لمستخدم أعمال | مخاطرة تشغيلية وأمنية (قابل للاستغلال) | 23.4 + 107 |
| GAP-FOR-D07 | **الطباعة الفيزيائية كقناة أولى** (Spool/Notepad/80-132) | بيئة ورقية تقاوم الرقمنة — UX خلف عصر متطلبات الوصول | 1/6/102 |

### فجوات تشغيل (P)

| ID | الفجوة | الأثر |
|---|---|---|
| GAP-FOR-P01 | **Guest Watch List بلا تدقيق من خلف صلاحيات** — من يعلّم ضيفاً للمراقبة؟ (أثر مستخدم غير موثق هنا، خلافاً ل31.4) | تتبع مسؤولية المراقبة |
| GAP-FOR-P02 | **Show Only Deleted Records (87)** يفترض soft-delete في FX — بلا واجهة استرجاع موثقة | استرجاع مدخل FX محذوف غير معروف |
| GAP-FOR-P03 | **SMS بلا بوابة/queue/فشل إرسال** (UNK-082) | مركز إشعارات بلا مصدر إرسال موثق |
| GAP-FOR-P04 | **Lakhs/Thousands** وحدتا عرض هنديتان بلا وحدة عربية (ألف/مليون) | قرار تعريب العرض مطلوب |
| GAP-FOR-P05 | **Program IDs يدوية** (استخراج Enter-Enter + تحرير INI 63) | إعداد إنتاجية هش — يقابله playlist UI |

## 3. مجهولات جديدة (UNK-078..082) — تُسجل في unknowns.md

| ID | السؤال | الأثر | المصدر |
|---|---|---|---|
| UNK-078 | **Report Designer + IDS Crystal Report Designer**: بنود TOC بلا متن + التقرير الرابع Forecast غائب ("gives 4" لكن 3 موثقة) | طبقة تخصيص مجهولة التقنية | FOM-REP TOC/ص58 |
| UNK-079 | **PMSPOL.INI/POL.SPC**: موضع dll الفعلي + صيغة القيم + هل يوجد ملفات .SPC أخرى؟ | تكامل نظامي مع الشرطة | REP ص25-26 |
| UNK-080 | **INI Switch 63**: صيغة القيمة الكاملة (فواصل فقط؟ حد الطول؟) وقائمة Program IDs الصالحة | تشغيل Sequence Print | REP ص95-96 |
| UNK-081 | **Export**: الصيغة/الامتداد/الهدف (ملف؟ تطبيق؟) | قناة الإخراج الرابعة | REP عموماً |
| UNK-082 | **بوابة SMS**: المزود/البروتوكول/Queue/إعادة المحاولة — بلا وثائق (توازي SMS Queued في Care) | قرارات تكامل خارجي | FOM-SMS كله |

## 4. تناقضان جديدان (C-FO-01/C-FO-02) — يُسجلان في contradictions.md

- **C-FO-01**: Guest Photo Reg. Card (23.1) موثق مرتين — نطاق Security (inhouse) ثم Registrations (inhouse **+ expected arrival**) — يُعتمد الأوسع.
- **C-FO-02**: "Fortune Next Enterprise 2.0" (FOM-SMS) vs "FortuneNext 6i" (كل الحزمة) — تسريب إصدار تاريخي (وحدة SMS أقدم؟).

## 5. معايير قبول مختارة (AC — عينة قابلة للتوسيع)

1. **AC-FOR-01** (صيغة): On Line Room Balance لغرفة برصيد افتتاحي 1000 + تعرفة 500 + LTX 50 = **1550** حرفياً.
2. **AC-FOR-02** (XOR): Night Report بصيغة 80 يعرض خيار YTD؛ بصيغة 132 يُقفل الخيار — يُعكس القرار: YTD دائم.
3. **AC-FOR-03** (بوابة): Room Rate for the Day يرفض التوليد قبل ترحيل التعرفة ("only once the Tariff is posted").
4. **AC-FOR-04** (حد): Mat./Forecast Rev. يرفض فترة > 10 أيام.
5. **AC-FOR-05** (وضع الدفع): Res. Advance List (Checklist) يعرض ADQ/ADC/ADV/POT كمعجم مغلق.
6. **AC-FOR-06** (SMS): checkout SMS يُرسل قبل ساعة من Checkout Time المفهرس — قابل لاختبار زمني.
7. **AC-FOR-07** (إحصاء): Hotel Statistics SMS يحتوي الرموز السبعة (Occ/Rm Rev/FB Rev/Non-FB/Tel/Bnq/Coll).
8. **AC-FOR-08** (تدقيق): Room Transfer Audit يعرض old/new + **المستخدم المخوّل**.
9. **AC-FOR-09** (دفعي): Manager Report Creation بلا تشغيل مسبق → Managers Report فارغ/محجوب؛ بعد التشغيل بتاريخ D يعرض Last processed date = D.
10. **AC-FOR-10** (وثيقة): Guest Watch List يميّز الحاليين عن سجل Audit (بما فيه unmark).

## 6. Smoke Test (خطة 18 خطوة لطبقة التقارير)

1. سلّم غرفة → Operational Report (All) يعرض Amendment/Cancellation/Day Use.
2. حجز مستقبلي → Expected Arrivals (80) يقبل تاريخاً مستقبلياً فقط.
3. No Show بفترة Stay Period → يظهر إيراد الفترة كاملة.
4. Print Voucher (Cancellation) → مرشحات Mem. ID/Arrival معطلة (Res# فقط).
5. إدخال Cut Off في Re-Confirm → Save ثم Print.
6. وصول ضيف أجنبي → Foreigners In-House (Summary) تجميع قومي.
7. PMSPOL مقابلة → Police Report يحمل To/From/Subject (Print Format بدل INI).
8. Mark ضيف في Watch List → Audit يظهر الإدخال + unmark → يظهر الثاني.
9. تعديل سعر غرفة → Room Rate Audit يعرض old/new.
10. Transfer غرفة → Room Transfer Audit يعرض المستخدم.
11. ترحيل التعرفة (Night Audit) → Room Rate for the Day يفتح (قبلها محجوب AC-03).
12. High Bills بـCut Off → يعرض متجاوزي الحد فقط.
13. Night Report 80/132 → سلوك YTD الموثق.
14. التقرير 104 Print Net Values → يقفل 80/132.
15. Sequence Print playlist → Execute يطبع الدفعة بترتيب الحفظ.
16. Room Verification → تناقر FO/HK مصطنع يظهر في Discrepancies Only.
17. Checkin ضيف عيد ميلاد + Mobile Master → SMS Greeting Type = Birthday.
18. Check-out بعد ساعة → وصل SMS Checkout قبلها بـ60 دقيقة + وصل Department Alert للإدارات.
