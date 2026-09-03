# 00 — نظرة عامة (Overview) — وحدة TEL (Telephone Management)

> **إدارة الهاتف**: محاسبة مكالمات EPABX من الاستقبال التسلسلي حتى **ترحيل الإيراد لفوليو النزيل** — بمحرك تسعير نابض (شرائح زمنية-نبضية ثنائية الأسعار P&T/فندق × أعياد × نسب حساب لكل امتداد × حدود دنيا/عليا × تقريب رباعي)، **وحدة إصدار كروت الأبواب Onity** (داخل TEL — المفاجأة المعمارية!)، ولوحة تشغيل عامل الهاتف (Guest Information برسائل/تعليمات/شكاوى/موقع النزيل + Yellow Pages). المقروء عميقاً كاملاً (الجلسة 12): **SET (32 ص/10 أقسام) + REP (20 ص/8 تقارير) + LUK (21 ص/9 استعلامات) + CAC (10 ص/4 وظائف) = 83 ص كاملة**.

---

## 1. حدود الوحدة

| البند | الوصف الموثق |
|---|---|
| الاسم النظامي | Telephone Management — قوائم فرعية: Setup / Reports / Lookups / **Call Accounting** (TOC الملفات الأربعة) |
| الوظيفة الجوهرية | **أربع وظائف طبقية**: (1) Setup — 10 أقسام تهيئة (امتدادات، روابط توائم، أعياد، ترحيل إيراد، ربط EPABX، شرائح زمنية-نبضية، أكواد دول/مناطق، **واجهة قفل الباب**، معرّف المكالمة)؛ (2) Call Accounting — 4 وظائف تشغيلية (تفعيل/إيقاف امتداد ببوابات أنواع، **تصحيح أخطاء الفوترة وإعادة الترحيل**، تحويل مكالمات بمصفوفة اتجاه، كلمة مرور الامتداد)؛ (3) Reports — 8 تقارير (بما فيها **Unbilled Call List**)؛ (4) Lookups — 9 استعلامات (بما فيها **Guest Information وحدة تحكم العامل** + Yellow Pages) |
| المركز المعماري | **وحدة بوابة العتاد المزدوجة**: القناة الوحيدة في المشروع التي تُوثّق تكامل **EPABX (منفذ تسلسلي + برنامج تحويل + Battery Reverse Signal)** و**أقفال الأبواب (Onity)** معاً — وحلقة إيراد فندقية كاملة: مكالمة → تسعير → فوليو FO → Revenue Code للنظام المالي |
| نمط التشغيل | **استقبال آني مستمر** (Serial Port → Call Records) + دورة تصحيح يدوية للمكالمات المرفوضة (Error → Repost) + دورة إقامة للبطاقات/كلمات المرور (تسجيل وصول → … → مغادرة) |
| النطاق | امتدادات الغرف/الأقسام/المتاجر · روابط غرف التوائم · تسعير نبضي زمني (عادي/أعياد) · أنواع مكالمات (Local/STD/IDD/**SPL**/Others) · حد أدنى/أقصى للوجهات · أعياد بمولد أيام الأسبوع · ترحيل موحد/تفصيلي بأكواد إيراد · تقريب (Higher/Nearer/Lower/None) · ضريبة حكومية · تحويل مكالمات (من الأقسام فقط!) · كلمات مرور حتى المغادرة · كروت Onity (إصدار/نسخ/فتح واحد/تعطيل/قراءة) · دفتر عناوين الشخصي (Yellow Pages) |
| خارج النطاق | فوترة مزوّد الخدمة نفسه (P&T = منظور تكلفة فقط) · إدارة سنترال الموظفين (لا جسر HRP!) · الرسائل الصوتية/المنبهات كوظائف (قدرة ذُكرت في 2-Way بلا شاشة — GAP-TE-D06) · أي قيود GL مسماة (عائلة الفجوة العامة) |

> ⚠️ **ملاحظتان معماريتان كبريتان:** (1) **واجهة قفل الباب تسكن TEL** — ترميز كرت الإقامة عند تسجيل الوصول عملٌ هاتفي-تقني في هذا النظام (مع Onity كنظام وحدي موثق!) — يُنقل تصميمياً إلى خدمة تكامل مستقلة عند إعادة البناء (F-TE-8). (2) **لا مفاتيح INI في الوحدة كلها** (الثالثة بعد CARE وMEM) — إعدادات السلوك تُدار عبر Telephone Link Setup الداخلي + إحالة وحيدة إلى **Module Attributes** (عرض المدة بالثواني/الدقائق — فصل SUPERVISOR في SYS).

## 2. جرد الوظائف الموثقة (10 + 4 + 8 + 9 = 31 وظيفة/تقريراً/استعلاماً)

| الدليل | الوظائف | العدد | المصدر |
|---|---|---|---|
| **TEL-SET** (Setup) | Telephone Extensions · Link Extensions · Holiday Table (بمولد أيام الأسبوع!) · Telephone Revenue Posting (موحد/تفصيلي!) · Telephone Link Setup (EPABX!) · Time-Rate Slabs (نبض ثنائي الأسعار!) · Country Codes (بشراكات إلزامية) · Area Codes (بحدود دنيا/عليا) · **Door Lock User Interface (Onity!)** · Call Identifier (بادئة أصفار) | 10 | TOC SET ص1 |
| **TEL-CAC** (Call Accounting) | Activate-Deactivate Extension (بوابات أنواع لكل امتداد!) · View-Update Telephone Error (4 حالات خطأ + إعادة ترحيل!) · Call Transfer (مصفوفة اتجاه) · Extension Password Setup (حتى المغادرة) | 4 | TOC CAC ص1 |
| **TEL-REP** (Reports) | List All Calls · Print Telephone Bill · Call Summary by Department · Transferred Call List · Extension Wise All Calls · Telephone Master List (3 أنماط!) · Unbilled Call List · Guest List | 8 | TOC REP ص1-2 |
| **TEL-LUK** (Lookups) | View Unbilled Calls · Room Calls Query · Dial Code Search · **Guest Information** · Guest Search · In-House Statistics (مفوَّضة لـFO!) · Create Address Book · Print Yellow Pages · View Transfers/Extensions (تحويلات غرف + تمديدات إقامة!) | 9 | TOC LUK ص1 |

## 3. المفاهيم الجوهرية الموثقة

| المفهوم | الدلالة | المصدر |
|---|---|---|
| **ثنائية الأسعار P&T / Hotel** | "The rate charged by the **Property** is for calls made from a Room or an Outlet and will be charged to the guest. The rate charged by the **Service Provider** is for all the calls made from the Property and will be charged to the Property" — كل شاشات التقارير والاستعلامات تعرض الخيارين معاً (P&T = تكلفة على الفندق، Guest = إيراد من النزيل) | SET ص18 + REP/LUK |
| **المكالمة الناضجة (Matured Call)** | "The time taken to connect a call is not considered while calculating the call charges. The actual call charge is calculated when the called number responds" — و**Battery Reverse Signal** "is a facility provided by the Local Telephone Exchange, which gives you the time elapsed to connect a call" — عدّ زمن الاتصال يبدأ من الرد الفعلي لا من طلب الرقم | SET ص16 |
| **نسبة الحساب Calculation %** | "If the Service Provider's rate for a single call is 60c, and if 100% is mentioned, then the original rate, which is 60c, is retained. If 150%... one and a half time... 200%... double. **If 0.00% is specified, then it is considered as an uncharged call (0% is applicable for all call types except STD and IDD)**" — مضاعف تسعير لكل امتداد × لكل نوع | SET ص4-5 |
| **المكالمات الأخرى (Other Calls)** | "All calls other than the Local, STD and IDD... **Toll free numbers, calls made from a Calling Card, AT&T calls** etc. If the Hotel decides to charge a certain minimum amount... specify the amount in this field. If the Hotel offers this facility free of charge... specify 00.00 %" | SET ص5 |
| **معرّف المكالمة (بادئة الأصفار)** | "Called numbers with **one zero** at the beginning are STD, **two zeroes** are IDD and **no zeroes** are Local calls. 09986056565, 005674486754, 9980688744" — تصنيف القمة الحرفي لسلسلة الرقم المطلوب | SET ص31 |
| **الشراكات الإلزامية (Sentinels)** | Country Codes: **LCA** (محلي) و**9999999999 "Country Code Not Defined"** — Area Codes: (A) LCA/LCA/LOCAL CALL بشرائح محلية؛ (B) 9999999999/9999999999 **بأعلى شريحة IDD**؛ (C) بلد فارغ/9999999999 "Area Code Not Defined" **بأعلى شريحة STD** — توجيه المكالمات غير المعرفة لأغلى تعرفة (حماية إيراد!) | SET ص22 + ص25 |
| **عدم قابلية الشرائح للتعديل** | "You **cannot Modify or Delete** a time rate slab record... you have to **Add a new record with the same slab code but with a new applicable from date**... it will consider the call rates from the record that has the **latest applicable from date**" — مثال رقمي: شريحة 1 بتاريخ 18-Dec-2011 و1-Jul-2012 → تُستخدم 2012 | SET ص20 |
| **ترحيل موحد/تفصيلي** | "If the user select option **YES** for Consolidate Postings, then... **one entry for the day for each category** of calls in the guest folio. If **NO**... post each call entry separately... these entries will appear on the guest bill" + **Revenue Code لكل نوع** | SET ص14-15 |
| **حالات الخطأ الأربع** | "Extension not defined" · "**Room vacant** — This situation might occur when there is a group check-in. The keys were given to the guest and the guest checked-in... but the same check-in **is not recorded in the PMS**" · "Call Duration ≤ uncharged duration" · "**Bad records** — if the data captured is 01/@2/99 instead of 01/02/99, since there is an unidentified character (@)" | CAC ص4-5 |
| **مصفوفة تحويل المكالمات** | مسموح: **Department→Room / Department→Shop / Department→Department**. ممنوع: Room→Department / Shop→Department / **Room→Room / Shop→Shop** — "The extension from where the call is getting transferred should **always be a department**" | CAC ص6 (جدول حرفي) |
| **بوابات الأنواع لكل امتداد** | "The user can assign Activate or Deactivate status to an extension and **allow or block call types Local, STD or IDD for each active extension**... though the telephone line is activated, you cannot make any local calls" | CAC ص3 |
| **كلمة مرور الامتداد** | "set up a password to a Room or Departmental Telephone extension **when a Guest registration is done. This password will be valid till the Guest checkouts**... only numbers and maximum of 10 digits... only **occupied rooms**" | CAC ص7-9 |
| **تقريب رباعي** | "Round Off Required... **Higher, Nearer, Lower or None**... Round Amount... will be read at the time of billing" + **Round Off Seconds** للمدة نفسها | SET ص16-17 |
| **الربط بـFO الرئيس** | "Link to Front Office — This option is to post the calls made by the guest to front office and will be charged to guest port folio. Select the option YES if the calls need to be posted to front office" + **2-Way Communication** "activate / de-activate the phones, voice mails, wake-up calls and room status" | SET ص16 |
| **كرت الباب (Onity)** | "encodes the guest stay details on the key card at the time of check-in **to enable opening the door only during the guest stay period**" — 4 أنماط: New Card / Copy Card / **Single Open Card** (مندوب الفندق يفتح مرة واحدة!) / Check Out (تعطيل) + Read (Onity فقط للقراءة والفتح الواحد) | SET ص26-31 |
| **Yellow Pages** | "record and save frequently called telephone numbers and create your own Yellow Pages" — Main/Sub Category (Hotels/Restaurants/Resorts/Hospitals/Cab Services…luxury-budget…) + عنوانان (إقامة/عمل) + Pager (20 محرفاً!) — عنصر إنتاجية شخصي داخل وحدة تشغيلية | LUK ص15-17 |

## 4. التفاعلات مع الوحدات (موثقة نصاً)

- **TEL ← EPABX (العتاد):** "All the call details are captured from **data transfer that happens between EPABX and the Serial Port**" + Conversion Program (كود ≤7 محارف) "to post the call made by the Guest, **sensing the information sent to the EPABX**" — الاستقبال الآلي الوحيد الموثق في المشروع.
- **TEL → FO (حلقة الإيراد):** Link to Front Office = Yes → ترحيل لفوليو النزيل (موحد/تفصيلي بأكواد إيراد) + 2-Way (هواتف/بريد صوتي/منبهات/حالة الغرفة).
- **TEL ← FO (بيانات الإقامة):** رقم الغرفة والإشغال (Room vacant error!) · Registration # (فوترة الكرت وكلمة المرور) · Guest Information/Instructions/Complaints/Messages/Location · Guest Search (in-house/reserved/checked-out + Room History) · **View Transfers/Extensions** (تحويلات الغرف + تمديدات الإقامة بمعتمِد!) · **In-House Statistics مفوَّضة حرفياً**: "refer CHAPTER – LOOKUPS of MODULE – FRONT OFFICE".
- **TEL → النظام المالي:** Revenue Codes لكل نوع مكالمة + Government Tax Structure (ضرائب هاتف بلدية) + تقريب مبلغ الفوترة.
- **TEL ↔ SYS:** Module Attributes (عرض المدة ثوانٍ/دقائق — فصل SUPERVISOR) · Property list · Currency Codes للشرائح · Room/Department Help.
- **TEL → أقفال الأبواب (Onity):** "the information that has to be transferred to the key card system will be **saved in the backend, read by the door lock interface program and send to the device**" — نمط البرنامج الوسيط نفسه كـEPABX.
- **TEL ↔ HRP (غياب!):** لا ذكر لموظفي الهاتف/سنترال في أي ملف — مشغّلو الوحدة ضمن طاقم FO الضمني (راجع عائلة UNK-038 متسعة).

## 5. أهم الاكتشافات المعمارية (الجلسة 12)

1. **بوابة عتاد مزدوجة فريدة:** TEL هي الوحيدة التي تُوثّق تكاملين عتاديين حرفيين (EPABX بالمنفذ التسلسلي + أقفال Onity ببرنامج وسيط يقرأ الـbackend) — ما يجعلها المرجع المعياري لكل تكاملات العتاد في إعادة البناء (نمط: حفظ خلفي + برنامج وسيط + جهاز).
2. **سباق تسجيل الوصول الجماعي موثق كحالة خطأ:** "المفاتيح سُلّمت والنزيل يستخدم الهاتف لكن تسجيل الوصول غير مسجل في PMS" — توثيق مبكر نادر لـrace condition بين القنوات الفيزيائية والمنطقية — يُعاد بعلم حالة pending-folio في Frappe.
3. **شرائح غير قابلة للتعديل بتوابُت زمنية:** عائلة "immutable + Applicable From يفوز بالأحدث" (انضمت لـRate Master في HRP وService Rate في MEM) — بنية الإصدار الزمني الرابعة الموثقة؛ ERPNext: Item Price بصلاحية أو DoType مخصص.
4. **الحماية بأغلى تعرفة:** الشراكات الثلاث للمكالمات غير المعرفة تُوجه لأعلى شريحة IDD/STD — قاعدة إيراد دفاعية صريحة (النزيل يدفع كاملاً حتى تُعرَّف الوجهة!).
5. **وحدة تحكم عامل الهاتف (Operator Console):** Guest Information يجمع تعليمات الغرفة/الشكاوى/الرسائل/موقع النزيل بأنماط Tag-YES (أُبلّغ/وُجد) + زر إداري وحيد لحل تعارض **SL#** — نمط مكالمات الفنادق الكلاسيكي كاملاً.
6. **SMS شبح:** مقدمة CAC تذكر "record and save **standard SMSs** to be sent to the guests on various occasions like **checkins, anniversaries** etc." — لا قسم لها في TOC ولا جسم (GAP-TE-D01 + UNK-054) — ثاني "وظيفة مقدمة-بلا-جسم" بعد Membership Tax Posting.
7. **عرضٌ للـPMS من نافذة الهاتف:** View Transfers/Extensions يعرض تحويلات الغرف (قديم→جديد) وتمديدات الإقامة (مغادرة قديمة/جديدة + **المنفذ والمعتمِد!**) — TEL تستهلك تدقيق FO.
