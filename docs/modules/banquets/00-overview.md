# 00 — نظرة عامة (Overview) — وحدة Banquets (BNQ)

> **وحدة أعمال الفعاليات الكاملة**: قاعات + حجز + متطلبات + تكاليف + فوترة + تسويات + ودائع + Auto Indent إلى المخازن. المقروء عميقاً كاملاً (الجلسة 7): **BNQ-SET (98 ص/20 قسماً) + BNQ-BOK (41 ص/Bookings) + BNQ-CFG (38 ص/12 قسماً) + BNQ-BIL (66 ص/13 قسماً) + BNQ-LUK (12 ص/استعلامان) = 255 ص كاملة**.

---

## 1. حدود الوحدة

| البند | الوصف الموثق |
|---|---|
| الاسم النظامي | Banquets — "Billing is used in Banquets to Make the Requirement Entry, Deposit Entry, refund retention charges entry, Print & settle the Bills. Etc." (BIL ص1) |
| الوظيفة الجوهرية | **خمس وظائف طبقية**: (1) Setup — روابط المنافذ والعملات والمرجعيات والأحداث والصلاحيات؛ (2) Configure — القاعات (6 تبويبات!) والقوائم وسياسات الإلغاء والموظفون؛ (3) Bookings — دورة حجز ثلاثية الأنماط (Inquiry/Provisional/Confirmed) + Block/Release؛ (4) Billing — Shift/Outlet + الفاتورة (3 أنماط تقسيم) + 11 نمط تسوية + الودائع والمتطلبات والتكاليف وAuto Indent؛ (5) Lookups — لوحتا التوافر |
| المركز المعماري | **وحدة هجينة FO×POS**: تحجز كـ FO (Reservation Status + Availability Chart + Market Segment من FO Defaults) وتتسوى كـ POS (Shift/Outlet/Session + أنماط تسوية شبه مطابقة + POS User Access) — **أغنى وحدة تكاملاً تشغيلياً بعد FO** |
| نمط التشغيل | منفذ Banquet يعمل بـ Sessions (9 جلسات مثلاً: Breakfast 8-11 $20/Lunch 13-16 $45/Dinner 20-23 $60 للشخص!)؛ حجز بنمطين (**Across Dates** مستمر أو فترة زمنية متعددة التواريخ)؛ إقفال يومي Shift ثم Outlet |
| النطاق | Function Rooms (6 تبويبات: Details/Features/Seating/Pictures/Layout/Location) + Associated/Sub Venues · Event Types (تصنيفات AGM/Wedding...) · Menu Cards/Package Cards · Requirement Entry (4 مسارات) · Pre Costing + **Auto Indent** · Corporate Rates · Deposits (3 وسائل + إيصالات) · Refund/Retention · Cancellation Policies · Event Calendar (مناسبات/أيام جافة/حظر حجز!) |
| خارج النطاق | معالجة إيصالات AR النهائية (تُحوَّل إليها)؛ مخزون الأصناف (MGT عبر Auto Indent)؛ وصفات FNB (تستهلك منها)؛ تقارير BNQ (لا ملف REP في الحزمة — راجع 08) |

> ⚠️ **الاكتشاف الحاسم (يحسم UNK-011 كاملاً):** سلسلة **Auto Indent** موثقة بالنص الكامل: Requirement Entry (يحمل عناصر الحجز) → **Pre Costing Chef Eng** ("ingredient details will be obtained from the recipe... or if the inventory items can be linked manually") → **Auto Indent** ("raise an indent in Banquet Outlet **and the Recipe**" — Work Sheet# → Department/Cost Center → "recipe details will populate based on the department selected") → MGT Indent. **الشباك البنكي للولائم يولّد طلبات مخزنية آلياً**.

## 2. جرد الوظائف الموثقة (20 + 12 + 13 + 2 ≈ 50 وظيفة)

| الدليل | الوظائف | العدد | المصدر |
|---|---|---|---|
| **BNQ-SET** (Setup) | Link Outlet-Sessions · Link Outlet-Order Types · Link Outlet Currencies · Country-State-City (3) · Property Information · Banquet Block Reasons · Floor · Item Type · Banquet Menu Groups · Setup Event Calendar · Reservation Status · Equipment Master (3) · Supplier Master (+Vendor+Contract) · Event Question Definition · Event Template Definition · Print Forms · User Defined Print Forms · Corporate Rate Master (3) · Corporate Rate Tagging · BNQ User Access | 20 (26 فرعية) | TOC SET ص1-2 |
| **BNQ-BOK** (Bookings) | Scan and Search Engine (**Search/History/Make/Amend/Cancel/Browse/Copy**) · No Show Cancellation · Block / Release Rooms | 3 (10 فرعية) | TOC BOK ص1 |
| **BNQ-CFG** (Configure) | Associated Room · Function Room Features · Function Room Setup Style · Cancellation Policy · Function Room (6 tabs) · Event Type Definition · Item Classification and Description · Menu Master · Setup Menu Card (2) · Tag Sub Venues · Banquet Staff · Service Managers | 12 | TOC CFG ص1 |
| **BNQ-BIL** (Billing) | Open Shift · Open Outlets · Banquet Bill (+3 Splits) · Banquet Settlement (11+Multiple+Resettlement) · Close Shift · Close Outlet · Reprint Invoice/Bill · Pending Invoice/Bill · Deposit (3 وسائل) · Refund/Retention Charges · Requirement Entry (4 مسارات) · Pre Costing Chef Eng · **Auto Indent** | 13 | TOC BIL ص1 |
| **BNQ-LUK** (Lookups) | Function Room Availability · Availability Chart | 2 | TOC LUK ص1 |

## 3. المفاهيم الجوهرية الموثقة

| المفهوم | الدلالة | المصدر |
|---|---|---|
| **Function Room (6 تبويبات)** | Details (location/floor/available hours/**minimum revenue**/security + Venue Dimensions) · Features · **Seating (سعة لكل نمط + صور!)** · Pictures · Layout · Location — أغنى تعريف مكان في المشروع | CFG §5 ص12-16 |
| **نمطا الحجز** | **Across Dates**: "Room is booked starting from the moment From Time and will remain occupied till the To Time is over for an entered date range... no other bookings can be taken" (احتكار مستمر) · **فترة زمنية**: قاعة لنطاق وقتي عبر تواريخ متعددة | BOK Make ص10/20 |
| **Reservation Status الملونة** | "user-defined reservation statuses... option to set **color legends**" — تُعرض في Function Room Availability وAvailability Chart؛ وفي الرسم تُدمج "compacted/combined to their basic reservation types" (Inquiry/waitlist/Provisional/Confirmed) **إلا إذا INI 408=1** | SET §11 + LUK §2 |
| **Event Calendar الحاجب** | "auspicious days, Dry days and also **restrict the booking for a particular date and particular user**... Only if the status is 'Yes', the supervisor\user is allowed to do booking on that specified date" — **بوابة تقويمية على الحجز** (Booking Made By: User/Supervisor/All) | SET §10 ص33 |
| **Payment Terms الثلاثية المرحلية** | "Pre-Function, During Function and Post-Function and the combination of all the 3 with respective percentage(s)" — جدولة مالية مرحلية للحدث | BOK Make ص9 |
| **Deposit → Refund/Retention** | ودائع بثلاث وسائل (إيصالات قابلة للتعديل/الحذف) + "You cannot cancel Bookings with **DEPOSITS**. You should make the **paid outs** first" + Retention يقتطع من الوديعة — **حلقة التزام مالي كاملة** | BIL §9-10 + BOK Cancel |
| **Requirement Entry (ورقة العمل)** | 4 مسارات (Package Menu Card/Menu Card/Items/Copy) + عناصر Open + **F11 إعادة تسمية الصنف! F12 مجاني!** + Finalize (تجميد بتحرير لاحق بتنبيه) + "Service timings... common for the entire Requirement Entry" | BIL §11 |
| **Pre-Costing → Auto Indent** | "ingredient details will be obtained from the recipe... or... inventory items can be linked manually. If it is an open item, the inventory items should be tagged" ثم Auto Indent بالوصفات حسب القسم — **قناة BNQ→MGT الموثقة** (UNK-011) | BIL §12-13 |
| **Supplementary Items** | "If you want to add any additional items to the bill... The sub menu items under the selected menu item appears... **highlighted in green color**" — إضافة على فاتورة الحدث | BIL §3 ص7-10 |
| **ب القيود المحاسبية للتسوية** | "the bills must be settled **during the same accounting date**" + Resettlement مشروط: "only if it has not been originally printed at **Front Office** and has not been settled to the **room account**... and the guest has **already checked out**" (⚠️ [UNCERTAIN] الصياغة الأخيرة ملتبسة سياقياً — الغالب: لا يمكن إعادة تسوية ما رُحِّل لغرفة ضيف غادر) | BIL §4 ص18/31 |

## 4. التفاعلات مع الوحدات (موثقة نصاً)

- **BNQ ← SYS:** المستخدمون ("Create User" — Banquet Staff) · PO Cashier grouping · User Access · Currencies (Link Outlet Currencies ← "Currencies under General Setup of System Setup") · Round Off (نفس خاصية SYS بأمثلة Property Codes!) · Reason Codes · Print Forms Program IDs.
- **BNQ ← FO (الأعمق):** Market Segment + Business Source "displayed by default as defined in the **SET UP FO defaults**" + Pay Mode كذلك (BOK ص8-9)؛ Guest Settlement → Room# + "Guest Name, Meal Plan, Pax, Birthday, Anniversary and Guest status" (قراءة ملف الضيف)؛ Resettlement يتحقق من طباعة FO.
- **BNQ → AR:** Credit Card "details... are sent to the **Accounts Receivable module** for further processing"؛ Company Settlement "will be treated as **outstanding** until payment is received"؛ Staff Settlement "saved in the **Accounts Receivables** module"؛ Blacklisted company message "along with the **authorized person's name and the reason**"؛ Available Credit (POS MA 21).
- **BNQ → MGT (Auto Indent):** Pre Costing → Auto Indent → Department/Cost Center → Recipes → indent — **يحسم UNK-011**.
- **BNQ → FNB:** Recipes ("obtained from the recipe") + Menu Items من Menu Master (TT classification) + Cost%.
- **BNQ ↔ POS (نموذج مشترك):** Shift/Outlet/Session + أنماط التسوية + POS Module Attributes (3/8/16/21/26) + POS User Access (البند 20 في SET!) + Module Attribute 29 (Menu Master بنمطين!) — **الولائم تعمل بمحرك POS كاشئ منفذ متكامل**.
- **BNQ → Finance:** رابط الترحيل BNQ→Finance ضمن الستة الموثقة في FAS-SET.

## 5. أهم الاكتشافات المعمارية (الجلسة 7)

1. **UNK-011 Resolved كاملاً:** Auto Indent موثق بالنص (BIL §13): "raise an indent in Banquet Outlet and the Recipe" — Work Sheet → Department/CC → recipes populate — **أعلى إنجاز توثيقي بالجلسة**.
2. **BNQ = FO×POS هجينة:** تحجز بعقلية FO (حالات/توافر/أسواق من FO Defaults) وتفوتر بمحرك POS (Shift/Outlet/أنماط 11/POS Attributes/POS User Access) — **قرار معماري F-BQ-1: بناء Banquet فوق نفس محرك POS المخصص بدل وحدة مستقلة**.
3. **مفاتيح تكوين جديدة:** INI **408** (توحيد حالات الرسم 0/1) + INI **409** (بنى الضرائب في الحجز) + INI **346** (تعديل Pax في Requirement) + POS MA 3/8/16/21/26 مُشارَكة — الجدول التراكمي يقفز إلى **28+ مفتاحاً**.
4. **حظر إلغاء ذي الودائع:** "You cannot cancel Bookings with DEPOSITS... make the paid outs first" — **قفل مالي وقائي** موثق.
5. **Void ممنوع في الولائم:** "In Banquets **Void Settlement is restricted**. You will get the following message" — تخصيص نمط تسوية مقارنة بـ POS (حيث Void فعال).
6. **Complimentary/NC = ليست مبيعات:** "Settlements made by this mode is **not considered as Sales** for the Hotel" — **قاعدة إيراد محاسبية صريحة** (مرحلة 6).
7. **العملة النيبالية في الأمثلة (NRS 5,976.00):** أصل السوق الهندي/النيبالي للمنتج يظهر نصاً (Multiple Settlement).
8. **لا ملف BNQ-REP في الحزمة:** التقارير (Function Prospectus/BEO/Confirmation/Cancellation Letters ذُكرت كمProgram Types في Print Forms) **بلا دليل مستقل** — GAP-BQ-D01.
9. **تصادم تسمية BNQ User Access:** البند §20 نصّه "The **POS User Access** option is used to provide/restrict user access rights for the users in the **Banquet** module" — **البرنامج نفسه** (KOT 28 عملية + Billing + Settlement 15).
10. **Tag Sub Venues:** قاعة رئيسية تستوعب فرعيات معروضة مدمجة "in Make Booking, Availability Chart and Block & Release Rooms" — نمط توريث مكاني.

## 6. مصادر الوحدة

| الملف | الصفحات | الحالة |
|---|---|---|
| FN6i-NT-BNQ-SET.pdf | 98 | **✓ قرئ كاملاً** (20 قسماً) |
| FN6i-NT-BNQ-BOK.pdf | 41 | **✓ قرئ كاملاً** (Bookings: 3 وظائف/10 فرعية) |
| FN6i-NT-BNQ-CFG.pdf | 38 | **✓ قرئ كاملاً** (12 قسماً) |
| FN6i-NT-BNQ-BIL.pdf | 66 | **✓ قرئ كاملاً** (13 قسماً + 11 نمط تسوية) |
| FN6i-NT-BNQ-LUK.pdf | 12 | **✓ قرئ كاملاً** (استعلامان) |
| BNQ-REP (تقارير الولائم) | — | **غير موجود في الحزمة** — GAP-BQ-D01 (Function Prospectus مذكور كبرنامج طباعة فقط) |
