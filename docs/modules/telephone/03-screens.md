# 03 — جرد الشاشات (Screens Inventory) — وحدة TEL

> **~40 شاشة/نافذة موزعة**: SET (17 شاشة مع نوافذ البطاقات الخمس) · CAC (6) · REP (9) · LUK (12). كل الشاشات بنمط "Enter new information / Change / Delete / Browse / Previous / Next / Save / Panel / Exit" القياسي (SET ص2).

---

## اصطلاح القياس

- **[M]** شاشة إدخال/تعديل رئيسية · **[L]** قائمة Browse/Help · **[W]** نافذة فرعية/منبثقة · **[R]** شاشة تقارير (معاينة + طباعة) · **[Q]** شاشة استعلام
- المصدر: ص رقم الصفحة في الدليل الأصلي.

## 1. قوائم TEL الرئيسية

| # | الشاشة | النوع | المصدر | مكوّناتها الوظيفية |
|---|---|---|---|---|
| 1 | Telephone Management — Setup menu | [M] | SET ص3 | نقطة الدخول: "click Telephone Management and select Setup" |
| 2 | Reports menu | [M] | REP ص2 | 8 تقارير |
| 3 | Lookups menu | [M] | LUK ص2 | 9 استعلامات |
| 4 | Call Accounting menu | [M] | CAC ص2 | 4 وظائف |

## 2. شاشات Setup (SET — 17)

| # | الشاشة | النوع | المصدر | أبرز العناصر |
|---|---|---|---|---|
| 5 | Telephone Extensions | [M] | SET ص4 | Extension# (6) · نوع (Room/Dept/Shop) · Property · Extension Info · Calculation% ×4 · Name(30) · Phone/Fax · Equipment · Location |
| 6 | Telephone Extensions Help | [L] | SET ص6 | F1/نقر مزدوج — "Select the Extension # whose details you want to modify" |
| 7 | Link Extensions | [M] | SET ص7 | Main Extension (F1) + Linked Extn Details (متعدد) + Delink All |
| 8 | Extension List (للربط) | [L] | SET ص8 | "extension numbers that you want to link to the main extension" |
| 9 | Delink All Confirmation | [W] | SET ص9 | "all the linked extension numbers will be delinked" — نافذة تأكيد |
| 10 | Holiday Table | [M] | SET ص10 | Date (> accounting date) · Day (تلقائي) · Occasion |
| 11 | Auto Generation (Weekdays) | [W] | SET ص11-13 | Week Days (Sun-Sat) + From/To + **Generate** → قائمة تواريخ اليوم المختار → نقل للجدول |
| 12 | Holiday Entry (حذف) | [W] | SET ص13 | نقر مزدوج على بند → التفاصيل تظهر → حذف |
| 13 | Telephone Revenue Posting | [M] | SET ص14-15 | Consolidate Postings Yes/No **لكل نوع** + Revenue Code (F1) لكل نوع |
| 14 | Telephone Link Setup | [M] | SET ص16-17 | EPABX Prefix · Conversion Program (7) · Uncharged Duration · Link to FO · 2-Way · Round Off Seconds/Required/Amount · Govt Tax Structure |
| 15 | Time-Rate Slabs | [M] | SET ص18-20 | Applicable From · Slab Code (F1) · Name · Currency · From/To Time → Enter×2 → **Regular/Holidays: P&T vs Hotel (Seconds+Rate)** |
| 16 | Slab List (F1) | [L] | SET ص19 | "existing Time / Rate Slab details" — سابقة فقط (لا نفس اليوم) |
| 17 | Country Codes | [M] | SET ص21-23 | Code(10) · Name(30) · Status — شراكات LCA/9999999999 |
| 18 | Area Codes | [M] | SET ص24-26 | Country · Area(10) · Name(30) · Slab (F1) · Min/Max Charge — شراكات ×3 |
| 19 | Door Lock Key Card System | [M] | SET ص26 | الواجهة الأم: New Check-In / Guest Copy / Check Out / Single Opening Card / Read a Card / Exit |
| 20 | New Check-In (Card Issue) | [W] | SET ص27-28 | Issue New Card/Copy Card/Single Open · Room#1/Room#2 · No of Nights · Today (تلقائي) · From/To · CI/CO Time · **Encode** |
| 21 | Guest Copy | [W] | SET ص28-29 | "additional card or duplicate card with the same information and access rights" |
| 22 | Check Out (Card Disable) | [W] | SET ص29-30 | Room # + تأكيد — "card reader should be attached... card inserted in the card slot" |
| 23 | Single Opening Card | [W] | SET ص30 | "only with **Onity** Based Key Card Systems" |
| 24 | Read a Card | [W] | SET ص30-31 | CI/CO Date + Time — Onity فقط |
| 25 | Call Identifier | [M] | SET ص31-32 | Code (بادئة) + Call Type — تعديل = حذف + إضافة |

## 3. شاشات Call Accounting (CAC — 6)

| # | الشاشة | النوع | المصدر | أبرز العناصر |
|---|---|---|---|---|
| 26 | Activate-Deactivate Extension | [M] | CAC ص2-4 | Room/Extension (راديو) + Function (Activate/De-activate) + Local/STD/IDD (Yes/No لكل) |
| 27 | View-Update Telephone Error | [M] | CAC ص4-6 | Accounting Date + System Date (تلقائي) + Error Type (قائمة) + **Select (نقر مزدوج→YES = إعادة ترحيل!)** |
| 28 | Call Transfer | [M] | CAC ص6-7 | From Extension (**قسم فقط!**) + To Extension (قسم/غرفة/متجر) → قائمة المكالمات → Select → Save |
| 29 | Extension Password Setup (Room) | [M] | CAC ص7-8 | Room # (غرف **مشغولة فقط**) + Reg# (F1) + Password (أرقام ≤10) |
| 30 | Extension Password Setup (Extension) | [M] | CAC ص8-9 | Extension # (F1) + Location (تلقائي) + Password |
| 31 | Calls List (Transfer/Error) | [L] | CAC ص6-7 | قائمة مشتركة بنمط Select/YES |

## 4. شاشات Reports (REP — 9)

| # | الشاشة | النوع | المصدر | أبرز خياراتها |
|---|---|---|---|---|
| 32 | List All Calls | [R] | REP ص2-5 | Date range (≤ اليوم، **نفس الشهر**) · Call types (All/IDD/**SPL**/STD/Local) · Rooms/Extensions (الكل/غرف فقط/امتدادات فقط) · P&T/Guest Charge · Include Taxes · Time range (يوم واحد فقط!) · Order By (Extension#/Date&Time/Trunk Line) |
| 33 | Print Telephone Bill | [R] | REP ص5-8 | For the Date (≤ accounting date) · All/Specific Rooms · Include Taxes · **Round Sec (60)** · Room# wise / Registration# wise |
| 34 | Call Summary by Department | [R] | REP ص8-10 | Date range (نفس الشهر) · All/Specific Departments (F1) |
| 35 | Transferred Call List | [R] | REP ص10-11 | Date (≤ accounting) · Extn to Extn / Extn to Room / All · Include Taxes |
| 36 | Extension Wise All Calls | [R] | REP ص12-15 | All/Guest/Other Extension · Date Range أو **Extension Range** · Call types (checkboxes) · P&T/Guest · Include Tax · **Page Skip By Extension** · **Summary wise Extension** |
| 37 | Telephone Master List — Extension | [R] | REP ص15-16 | Extension type (قائمة) → قائمة الامتدادات + أسعار الأنواع |
| 38 | Telephone Master List — Area Code | [R] | REP ص16-17 | Country (قائمة) → كل أكواد المناطق + الشرائح + Min/Max |
| 39 | Telephone Master List — Rate List | [R] | REP ص16-17 | Slab + Currency (قائمتان) → الشرائح وأسعار P&T/الفندق |
| 40 | Unbilled Call List + Guest List | [R] | REP ص18-20 | Unbilled: Date (≤ accounting) + Include Taxes · Guest: By Name/By Room + **Print All Room/Billing Instruction/Floorwise** |

## 5. شاشات Lookups (LUK — 12)

| # | الشاشة | النوع | المصدر | أبرز العناصر |
|---|---|---|---|---|
| 41 | View Unbilled Calls | [Q] | LUK ص2-4 | Date (افتراضي Accounting Date) + **Error Type** (قائمة) + Load/Enter×2 → التفاصيل |
| 42 | Room Calls Query | [Q] | LUK ص4-7 | Extension# (F1) + From/To Time (24h) + include taxes + P&T/Guest → سجل + **Summary (عدد/إجمالي لكل نوع)** |
| 43 | Dial Code Search | [Q] | LUK ص7-9 | تبويب البحث: **Dial #** أو **Place Name** → Country/Area/Min/Max/Slabs |
| 44 | Guest Information | [Q] | LUK ص9-13 | Name/Room# (F1) + أزرار: **Instructions / Complaints / Messages / Guest Location** + زر إداري (SL#) |
| 45 | Room Help | [L] | LUK ص9-10 | "Room Help/Room# Help Screen" — نقر مزدوج = اختيار |
| 46 | Messages | [W] | LUK ص12 | "View All Messages" + **Tag → YES (أُبلّغ)** → "will not show in the Guest Page Messages again" |
| 47 | Guest Location | [W] | LUK ص13 | **Tag → YES (وُجد)** → يخفي من Guest Page Messages |
| 48 | Guest Search | [Q] | LUK ص13-14 | "in-house guests, reserved guests and checked out guest... Room History" |
| 49 | In-House Statistics | [Q] | LUK ص14-15 | **مفوَّضة**: "refer CHAPTER – LOOKUPS of MODULE – FRONT OFFICE" — الإشغال pax-wise (نوع/حالة/خطة/جنسية/شركة/سعر + واصلون اليوم) |
| 50 | Create Address Book | [M] | LUK ص15-17 | Main/Sub Category + Prefix/Name + Residence/Office (9 حقول لكل) + Remarks(200) |
| 51 | Print Yellow Pages | [R] | LUK ص18-19 | Main Category (قائمة) → مطابقات + طباعة |
| 52 | View Transfers/Extensions | [Q] | LUK ص19-21 | Date (≤ اليوم) + راديو **Transfer** (تحويلات غرف: قديم→جديد + أسماء) / **Extension** (تمديد إقامة: مغادرة قديمة/جديدة + **User + Authorizer!**) |

## 6. عناصر UX العابرة (موثقة في SET ص2 — Identify Standards)

| العنصر | الوظيفة الموثقة |
|---|---|
| Click (New) | "Enter new information" |
| Change | "Change/update existing information" |
| Delete | "works only **conditionally**" |
| Browse | "View/browse existing information" |
| Previous / Next | "enabled only after you click Browse" |
| Save | "Save new or modified information" |
| Panel | "Command Window, Inter Node Communication, Calculator, Calendar, Scratch Pad, and **Yellow Pages**" |
| Status | Active/Passive — "If Passive... cannot be used" |
| User | "name of the user logged in" |
| Last Updated | "date and time when the user last updated" |

> **ملاحظة:** Yellow Pages داخل قائمة Panel العامة — دفتر العناوين متاح من أي شاشة في النظام (قناة وصول شاملة لبيانات TEL!).

## 7. إحصاء

| الدليل | الشاشات | منها نوافذ |
|---|---|---|
| SET | 17 | 6 (Delink + AutoGen + 4 بطاقات) |
| CAC | 6 | 1 (قائمة مشتركة) |
| REP | 9 | 0 |
| LUK | 12 | 3 (Messages + Location + Room Help) |
| **الإجمالي** | **~40** | **10** |
