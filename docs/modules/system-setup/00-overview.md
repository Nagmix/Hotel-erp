# 00 — نظرة عامة (Overview) — وحدة System Setup (SYS)

> **الوحدة التأسيسية المظلّة** للنظام كله: المستخدمون والصلاحيات + مفاتيح الإعداد المركزية + كل بيانات الإعداد العامة المشتركة عبر الوحدات. المقروء عميقاً كاملاً (الجلسة 5): **SYS-SSP (110 ص، 3 فصول، 19 قسماً فعلياً — §19 Group Nationality غير مدرجة في الفهرس!)**. هذه الوحدة تحسم 3 مجهولات معمارية حرجة: **UNK-004 (multi-property) وUNK-013 (نموذج الصلاحيات المظلي) وUNK-022 (مرجعية Module Attributes/INI)**.

---

## 1. حدود الوحدة

| البند | الوصف الموثق |
|---|---|
| الاسم النظامي | System Setup — "System Setup forms an important part of Fortune Next 6i. It is used to define the basic and general settings which are used across the product" (ص6 Introduction) |
| الوظيفة الجوهرية | **ثلاث وظائف طبقية**: (1) User Setup — المستخدمون وصلاحياتهم وتقاريرهم؛ (2) Supervisor — مفاتيح الإعداد المركزية (Module Attributes/INI/Captions/FO Defaults/استخراج الجداول/إدارة المستخدمين)؛ (3) General Setup — **18+ كيان إعداد مشترك** تستهلكه كل الوحدات |
| المركز المعماري | **نقطة أصل البيانات المرجعية**: العملات وأسعار الصرف والضرائب (3 طبقات) والأقسام ومراكز التكلفة والتصاريح المسموح تعديلها في كل الوحدات الأخرى تُعرَّف هنا أولاً؛ **+ نموذج الصلاحيات المظلي** فوق صلاحيات الوحدات الخاصة (AR User Access · FAS Transaction Type Rights · POS User Access · FO User Authorization) |
| نمط التشغيل | "Initially, The Service Provider creates user information for the user's System Administrator and assigns global rights for a complete access to all menu items. Using this privilege, the System Administrator can further define additional users and grant access rights accordingly" (ص6) — **سلسلة تفويض من ثلاث حلقات: مزود الخدمة → مسؤول النظام → المستخدمون** |
| النطاق | Users/Groups/Passwords · Access Rights (Add/Modify/Delete) · Menu Access + Graphs (الشاشة الرئيسية) · Report Restrictions (Spool/Export/Format) · Captions (إعادة تسمية القوائم!) · FO Defaults · Module Attributes · Extract DB Tables · INI Files · User Management · 18+ كيان General Setup (Property/Dept/CC/Designation/UOM/Reason/Currency/Exchange/Tax×3/GuestComments/PgmID/CreditCards/PrintBillMessage/Religion/Occupation/ParameterList/GroupNationality) |
| خارج النطاق | تفاصيل Module Attributes وINI **لكل مفتاح** (وثيقة منفصلة «Module Attributes & INI Settings» ليست في الحزمة — GAP-SYS-D01!)؛ Report Engine (وثيقة Getting Started غير متوفرة)؛ World Time (كذلك)؛ إعدادات الوحدات التفصيلية (لكل وحدة فصلها الخاص) |

> ⚠️ **اكتشاف جوهري:** كلا من Module Attributes (ص33: "refer System Setup – Module Attributes & INI Settings document") وINI Files (ص37 نفس العبارة) يحيلان إلى وثيقة **"System Setup – Module Attributes & INI Settings"** — ليست ضمن ملفات الحزمة الـ 65. هذا يفسر غياب مرجعية أرقام INI/Attributes الموثقة في FOM/POS/FAS: **GAP-SYS-D01** (يحسم UNK-022: المرجع خارج الحزمة قطعاً، والإحالات المرقمة في وحدات أخرى تظل مصدر المعرفة الوحيد).

## 2. جرد الوظائف الموثقة (6+6+19 = 31 وظيفة)

| الفصل | الوظائف | العدد | المصدر |
|---|---|---|---|
| **1. User Setup** | Creating a User · Setting up User Access · Setting up User Menu Access · Restricting Report Options · Listing Users · Listing User Access | 6 | Ch.1 TOC ص1-2 + متن ص7-22 |
| **2. Supervisor** | Changing Caption · Setting up FO Defaults · Module Attributes · Extract Database Tables · Creating INI Files · User Management | 6 | Ch.2 TOC ص2 + متن ص22-39 |
| **3. General Setup** | Property Codes · Departments · Cost Centers · Designations · Units of Measurement · Reason Code · Currencies · Exchange Entry · Tax Code · Tax Slab · Tax Structures · Guest Comments · Program ID for Print Forms · Setup Credit Cards · Print Bill Message · Religions · Occupations · Parameter List · **Group Nationality (غير مدرجة في TOC!)** | 19 | Ch.3 TOC ص2-3 + متن ص40-109 (§19 ص108-109) |

> ملاحظتان: (1) فصل User Setup يذكر "Setting World Time" في مقدمة الفصل (ص7) لكنه يحيل إلى وثيقة Getting Started — خارج الحزمة. (2) extracted-fields الآلي التقط **صفر جداول حقول** لهذا الملف (بنية الجداول مخالفة لنمط المستخرج) — الحقول كلها موثقة يدوياً من المتن أدناه.

## 3. المفاهيم الجوهرية الموثقة

| المفهوم | الدلالة | المصدر |
|---|---|---|
| **Supervisor (علم المستخدم)** | علم Yes/No عند إنشاء المستخدم: "Yes... enables **total access to all menu items** in the product" — **تجاوز كامل لنموذج User Access**؛ لا تُعرَّف صلاحيات إلا لغير المشرفين: "The User Access rights can be defined only for those who are not categorized as Supervisors" (ص13 Note) | §Ch1/1 ص10 + ص13 |
| **Group** | تجميع صلاحيات: يعرَّف المستخدم بـ Group (حر النص — "To define a new group, type the group name in the Group field" ص9) وتُمنح الصلاحيات **للمجموعة أو للفرد** — نموذج RBAC ذو مستويي تخصيص | §Ch1/1 ص9 + §Ch1/2 ص12 |
| **Applicable From** | البعد الزمني الإصداري في **كل** كيانات General Setup تقريباً: "You must enter a date **greater than the current date** to activate the setting active for a future date" (يتكرر نصاً في 12+ كياناً) — إصدارية مستقبلية موحدة | كل §Ch3 |
| **Modify-Locked Masters** | قاعدة عامة متكررة: بعد الإنشاء **يُسمح بتعديل حالة Active/Passive فقط** (وأحياناً حقل أو حقلان إضافيان) لمعظم الكيانات — "You are allowed to modify the status of the selected X only" — **تجميد مرجعي** يمنع إفساد البيانات التاريخية | §Ch3 Notes (Property: الحالة+العنوان؛ Designation: الحالة+Guest Type؛ Currency: الحالة+Division Method؛ البقية: الحالة فقط) |
| **Status Active/Passive** | القيم الثنائية الموحدة عبر كل الإعدادات — Passive = معطل غير ظاهر (بدون حذف مادي) | Identifying Standards ص7 |
| **Password Policy** | كلمة المرور **تولَّد آلياً** (رمز أبجدي-رقمي) عند اختيار Designation (!)؛ انتهاء صلاحية بالأيام (حتى 3 خانات)؛ المشرف يعيد التوليد من User Management **والنص الجديد يظهر مكشوفاً في العمود** (ص39: "The password will be changed and the new password can be viewed in corresponding password column") | §Ch1/1 ص10 + §Ch2/6 ص37-39 |
| **Caption (إعادة التسمية)** | "change the name of the menu option... if it does not match with the local names used for the same operation. Fortune Next displays **both — the standard menu name and the new name**" + خيار تطبيق الاسم الجديد على التقارير أيضاً — **آلية تعريب/توطين شاشة بقيت من فلسفة المنتج الأصلي** | §Ch2/1 ص23-24 |
| **Round Off (الخاصية)** | تقريب فاتورة الضيف عند Check-out على مستوى **الخصيص (Property)**: None/Nearer/Higher/Lower + مبلغ التقريب — بأمثلة رقمية كاملة (أنظر BR-SYS-08) | §Ch3/1 ص42-45 |
| **محرك الضرائب الثلاثي** | Tax **Code** (نوع الضريبة × وحدات التطبيق) → Tax **Slab** (شرائح مبلغ بنِسب، تراكمي/غير تراكمي) → Tax **Structure** (بنية مركبة: Percentage/Amount/Slab × On Value/On Discounted Value/**On Tax** متسلسلة!) — تُستهلك من FO/POS/BQT/Purchase/Laundry/Restaurant/RoomService | §Ch3/9-11 ص71-83 |
| **Exchange Entry** | سعر الصرف = **سجلات زمنية متعددة** للعملة: "A **maximum of 4 entries** can be made for each type of currency code" بترقيم تسلسلي تصاعدي آلي + وقت الضبط — الأساس الذي يثبِّت عليه AR سعر تاريخ الفاتورة | §Ch3/8 ص69-71 |
| **Floor Limit (بطاقات الائتمان)** | حد أرضي لكل نوع بطاقة (12 خانة + كسران) "validates the set limit credit limit during settlement of Room, Point of Sale and Banquet bills" + واجهة أجهزة تفويض خارجية online authorization | §Ch3/14 ص93-96 |
| **Extract Database Tables** | نسخ جداول إلى `C:\PMSDATA` بامتداد **.INS**؛ History Tables (لواحق MMYY)؛ GUI Data Extraction بملف `GUI<customer code>.dat`؛ حذف نهائي للأقراص المستخرجة — **البديل الداخلي للنسخ الاحتياطي** | §Ch2/4 ص33-36 |
| **INI Files** | تُولَّد من مصدر `N6IRPRP.BAS` المرخّص؛ **إلزامية عند التركيب** ("mandatory to generate and setup the INI file")؛ لا تُولَّد إلا بعد تعريف Property Code؛ تحرير يدوي بمحرر نصوص — "Else, there could be functionality issues with the Fortune PMS product" | §Ch2/5 ص36-37 |
| **Program ID (نماذج الطباعة)** | كل نموذج طباعة له Program ID (7 خانات) + **منفذ طابعة (LPT1/LPT2/COM1-COM3/USB)**؛ USB = طباعة PDF عبر BroadgunPdfMachine/PrimoPdf؛ التسمية القياسية `FM001BL` حيث **001 = كود الزبون القياسي** وكل تخصيص يحمل كود زبون مختلفاً (`FM326BL`) | §Ch3/13 ص86-93 |
| **Bill Message (البث الفاتوري)** | رسالة تسويقية بفترة صلاحية تُطبع على فواتير الغرف والمنافذ: From/To + Subject (10 حرفاً) + Message (100 حرفاً) + اختيار المنافذ — "Respective bill printing specifications have to be modified for printing these messages" | §Ch3/15 ص96-99 |

## 4. التفاعلات مع الوحدات (موثقة نصاً)

- **SYS → كل الوحدات (بيانات مرجعية):** Departments (بفلتر Banquet/General!) · Cost Centers · Currencies + Exchange Rates · Tax Codes/Slabs/Structures · Reason Codes (بفلتر 9 وحدات: Banquets/Finance/FO/**Gift Shop**/Laundry(s)/Membership/POS/Purchase/Sales) · Designations (Guest/Others→HR/**S&M**) · UOM (→POS/MM/F&B Costing نصاً) · Religions + Occupations (→HR Payroll Master + Guest History / Guest+Staff) · Credit Cards (→FO/POS/BQT settlements) · Guest Comments (→Guest Survey Template في FO وPOS).
- **SYS → FO:** FO Defaults (14 قيمة افتراضية تُسحب من Masters الموزعة بين SYS وFO — أنظر 02-configuration) + Program IDs لنماذج FO + Round off فاتورة الضيف.
- **SYS → AR:** Program IDs لثلاث مجموعات A/C Receivables (1)(2)(3) + Laundry.
- **SYS → POS/BNQ/BQT/Purchase/Laundry/Restaurant/RoomService:** Tax engine + Reason Codes + Round Off لكل عملة (POS-SET §6 يقتبس نفس كيان Currencies).
- **SYS (Supervisor) → سلوك كل الوحدات:** Module Attributes (المفاتيح المرقمة الموثقة مبعثرة: FOM Attr 1-67 · POS Attr 6/29/32 · FAS Switches · INV Switches) + INI (58/283/504/404/Acr2Fas #56...) + Captions + INI → N6IRPRP.BAS.
- **SYS → التقارير (كل وحدة):** Restrict Report Options (Spool/Export/Format لكل تقرير لكل مستخدم) + Report Engine.
- **SYS → الأجهزة:** منافذ الطابعات LPT/COM/USB + واجهات تفويض بطاقات خارجية (online authorization).

## 5. أهم الاكتشافات المعمارية (الجلسة 5)

1. **نموذج الصلاحيات الرباعي الطبقات (يحسم UNK-013):** (أ) علم Supervisor = تجاوز كامل؛ (ب) User Access المظلي: مجموعة/مستخدم × وحدة رئيسية/فرعية × عنصر قائمة × حقوق Add/Modify/Delete **لعناصر Settings/Transaction/Master فقط** ("The Options Rights screen is displayed only for selected menu items" ص15)؛ (ج) قيود التقارير Spool/Export/Format لكل تقرير؛ (د) صلاحيات الوحدات الخاصة (AR Transaction Types · FAS Transaction Type Rights · POS User Access + Restrict Outlet · FO User Authorization الخمسية) — **طبقات متعايشة لا تُستبدل**.
2. **Personalization بلا Custom UI:** User Menu Access يحدد **برامج قوائم (حتى 3) + رسوم بيانية (3-5 مع علم افتراضي) + Guest Info + Statistics** في الشاشة الرئيسية — يحتاج **خروج/دخول** ليسري ("You have to logout... and login again" ص17) — بذور تصميم Dashboard للواجهة الجديدة.
3. **Multi-property = سجل متعدد لكن تشغيلاً أحادياً (يحسم UNK-004 جزئياً):** Property Codes تعرّف خصائص متعددة ("A property can be a Hotel, a Resort, an Inn, a Motel, a Club, a Bar or a Restaurant, a Food Court, a Hotel Management School" ص41) + FO Defaults يختار **قيمة افتراضية واحدة** منها — النموذج البياني متعدد، **لكن لا آلية موثقة لتبديل خاصية التشغيل أو مشاركة البيانات بينها** — القرار المعماري لـ Frappe (Company لكل Property) يبقى قرارنا مع [NOT DOCUMENTED] للتبديل.
4. **فجوة المرجعية الكبرى (يحسم UNK-022):** وثيقة «Module Attributes & INI Settings» **مؤكدة الوجود وخارج الحزمة** (إحالتان صريحتان ص33 وص37) — خريطة المفاتيح الكاملة مستحيلة من الحزمة؛ استراتيجية التوثيق: **جمع الإحالات المرقمة من كل وحدة أثناء قراءتها** (تم جمع: INI 56/58/64/74/283/404/504 + Switches FAS 4 + INV 1/3/4 + Attr FO×67/POS 6/29/32/Attr 9).
5. **آلية التوطين الأصلية:** Change Caption يسمح بإعادة تسمية أي بند قائمة (مع عرض الاسمين معاً!) وحتى التقارير — النظام الأصلي حُمِّل منهج «تسمية محلية» قبل أي تعريب حقيقي؛ للواجهة الجديدة Arabic-First هذا **يُستبدل جوهرياً** بـ i18n كامل (قرار F-SYS-2).
6. **العملة نظام مكتمل الملامح:** Type (Currency/Travellers Cheque) + Local/Foreign + **Standard Rate (افتراضي 1، للعملات الأجنبية وشيكات السياحة فقط)** + **طريقة التحويل ضرب/قسمة** (قسمة: 5000÷49=102! مثال الدليل) + صيغ عرض Million/Lakh + نص قبل/بعد الكسر (لـ 20 حرفاً: "US$ 150.10 cents") + **طول الكسر 0-3** — أغنى من Currency القياسية في ERPNext ويحتاج DocType مخصص.
7. **§19 Group Nationality هامشية التوثيق:** صفحة ونصف بلا جداول حقول (فحص TOC يظهر 18 قسماً فقط) — [UNCERTAIN] وظيفتها الدقيقة؛ الاسم يوحي بجنسيات جماعية للضيوف/المجموعات.

## 6. مصادر الوحدة

| الملف | الصفحات | الحالة |
|---|---|---|
| FN6i-NT-SYS-SSP.pdf | 110 | **✓ قرئ كاملاً** (متون 3 فصول + 66 شكلاً مرقماً) |
| «Module Attributes & INI Settings» (مرجع خارج الحزمة) | — | [NOT DOCUMENTED] — GAP-SYS-D01 |
| «Getting Started» (Report Engine · World Time · Print Report Options) | — | [NOT DOCUMENTED] — GAP-SYS-D02 |
