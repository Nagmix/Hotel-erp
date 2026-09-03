# 03 — عائلة الأمن والامتثال النظامي (REP §23.x + التقارير النظامية)

> أثقل عائلة من حيث الأثر القانوني: تقارير تُرسل دورياً للحكومة/الشرطة/البنك المركزي/مصلحة الضرائب. التعريف الحرفي لمجموعة Security (REP ص22): "reports which may be required to be sent to the **Government or police officials** on routine basis."

---

## 1. مجموعة Security (23.1–23.7)

| # | التقرير | الخصوصية الموثقة |
|---|---|---|
| 23.1 | **Guest Photo Reg. Card** | طباعة بطاقة تسجيل **بالصورة** للضيف المقيم: "Front Office issues the Guest Photo Reg. Card **as an agreement** with all details about the guest as well as the stay with unique registration number" · حقل **Baggage** يدوي بعد الاسترجاع · **موثق مرتين بنطاقين مختلفين** → C-FO-01 |
| 23.2 | **Foreigners In-House** | أجانب اليوم الحالي · **Details (تفصيل فردي) / Summary (عدد بحسب الدولة)** · **Todays Arrival Only** · Include Special Rooms |
| 23.3 | **Scanty Baggage** | "list of all scanty baggage of the Guests that have been checked on the current date" — أمتعة ناقصة عند الدخول (مؤشر أمني فندقي كلاسيكي) · تاريخ آلي |
| 23.4 | **Police Report** | نموذج معرف مسبقاً للشرطة: "details of all checked in (**new arrivals**) **foreigners on a daily basis**" · تخصيص عبر **PMSPOL.INI → POL.SPC** (To/From/Subject/footer — حفظ في dll folder) — انظر `01-report-engine-infrastructure.md` §5 |
| 23.5 | **User Defined C Form** | "individual guest details that are **sent to the police**" · أزرار: Print / **Spool** ("save... with an appropriate name to a desired location for future references") / Exit |
| 23.6 | **Guest Watch List** | "keep under observation any Guest... whom the User suspects to be involved in any kind of **fraudulent act**" · Select All checkboxes + Save · **Watch List Audit**: "all Guests who were marked (**or later unmarked**)" — سجل تدقيق للمراقبة (تشغيل وإلغاء!) · Watch List Guests (الحاليون فقط) |
| 23.7 | **First Time Guest List** | ضيوف أول مرة (عملاء جدد) · Room # Wise / Guest Name Wise · تاريخ آلي |

**C-FO-01 (تناقض جديد — توثيق مزدوج):** 23.1 ورد أولاً تحت Security (REP ص22-23: نطاق **inhouse** فقط) ثم أعيد بوصف مطول تحت Registrations (ص23-24: "**inhouse guests as well as expected arrival's** with photograph"). النطاقان مختلفان والمتن الثاني أوسع — يُعتمد الأوسع (كلاهما) مع تسجيل الازدواج.

## 2. التقارير النظامية خارج مجموعة Security

| # | التقرير | الجهة/الغرض | الخصوصية |
|---|---|---|---|
| 48 | **Guest Visit by Nation** | إحصائي/تأشيرات | PAX بحسب الدولة · القاعدة: "< accounting date" + **same month and year** · **checkboxes لاستثناء**: Complimentary / House Guest / Day Use |
| 50 | **Foreigners Verification** | أمني | "vital information about the guests" · **All / International / Domestic** · **same month** إلزامي |
| 58 | **IT Report** | **مصلحة الضرائب** (Income Tax) | فواتير FO+POS فوق حد: "if bills generated at the Front Office and Point of Sale outlets are more than the specified amount" · **minimum bill Amount** (مثال: حد 1000 → فاتورة 1500 تدخل التقرير) · الدفع: **All / Cash Only / Credit Only** · اختيار Outlets |
| 70 | **Tourist Arrivals** | وزارة السياحة (نمطياً) | شهر/سنة "≤ Current Month/Year" · تصنيف **system defined**: "Companies, Travel Agent, Government, Airlines, Tour Operators, Individuals" — قائمة مصادر سياحية مغلقة! |
| 93 | **Tax Report** | ضريبي | حسب Tax Code (F1): "TAX charged maybe **Service Charge, VAT or Luxury Tax**" · "< accounting date" + same month+year |
| 94 | **Consolidated Tax Register** | ضريبي موحد | "all the rooms in the property and **Front Office or Point Of Sale outlets**" · نوع الضريبة + **checkboxes لكل من FO وPOS** — جسر ضريبي FO↔POS الوحيد في REP |
| 96 | **CC Encashment Report** | بنكي | صرف الشيكات/بطاقات الائتمان · same month |
| 97 | **RLM Report** | **البنك المركزي (RBI)** | "**Government statutory Foreign Encashment Report that has to be submitted to the Bank (RBI) while exchanging the foreign currency with the local currency**" · فترة عبر الشهور "≤ accounting date" — صيغة تشريعية هندية صريحة (Regulated Legal Money Exchange) |
| 119 | **Nationality Report / C** | إحصائي | PAX/إشغال بحسب الجنسية شهر/سنة · استثناء Local Nationals/HG/Comp |

## 3. User Defined C Form (ختام المتن)

تقرير خارج التسلسل: "This report produces the list of **foreign nationals**" — قائمة جنسيات (checkboxes) + زر — ثم جسم المتن ينقطع (الفقرة التالية نص مكرر من No Shows — خلل تحريري في الدليل الأصلي). **Report Designer وIDS Crystal Report Designer** في TOC بلا متن → UNK-078.

## 4. القرارات المعمارية المستخلصة

1. **خريطة الامتثال الهندية كاملة**: الشرطة (23.4/23.5/50) + RBI (97) + الضرائب (58/93/94) + C-Form (خارجية للنزلاء الأجانب — نمط هندي موثق في 23.5) + السياحة (70) — أي reproduction عربي-أولاً يحتاج طبقة Statutory pluggable (كل جهة بنموذجها).
2. **المراقبة ككائن بذاكرة تدقيق**: Watch List (23.6) يميّز الحالة الراهنة (Watch List Guests) عن الأثر التاريخي (Watch List Audit — بما فيه **unmarking**) — يتطلب جدول مراقبة + سجل تغييرات، لا مجرد علم Boolean على الضيف.
3. **العتبة المالية كمعيار إدخال**: IT Report بحد فاتورة قابل للضبط (مثال 1000/1500) — أول threshold رقمي موثق في طبقة التقارير (يوازي Cut Off Amount في High Bills 77 — عتبة تشغيلية).
4. **الاستثناءات الثلاثية الموحدة**: Complimentary/House Guest/Day Use تُستثنى أو تُدرج عبر checkboxes في 48/65/66/115-125 — البنية الضريبية والإحصائية تعامل الثلاثة كـ"إشغال غير مُدرّ".
5. **Scanty Baggage كمؤشر ميل مقيمين**: يوثّق عند الدخول ويُستدعى عند الشطب/الخروج — أداة إجرائية كلاسيكية تستحق Entity مخصصة عند التنفيذ.
