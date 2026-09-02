# 03 — كتالوج الشاشات (Screens) — وحدة POS

> الجرد من POS-SET (42) + POS-GST (12) + POS-LUK (7) + TS (العمليات). الأولوية: **P0** تشغيل يومي · **P1** دوري · **P2** إداري. الإجمالي: **~95 شاشة** (SET 55 + GST 22 + LUK 8 + TS عمليات 10 بمساراتها).

---

## 1. شاشات Setup (POS-SET) — 55 شاشة

| # | الشاشة | الأولوية | المصدر |
|---|---|---|---|
| S-POS-001 | Setup Outlets (رئيسية + Additional Options) | **P0** | §1 ص5-9 |
| S-POS-002 | Outlet Modify + سجل مستقبلي | **P0** | §1 ص9-11 |
| S-POS-003 | Outlet Sessions | **P0** | §2 ص11-13 |
| S-POS-004 | Outlet Order Type (KOT Types) | **P0** | §3 ص14-16 |
| S-POS-005 | Link Outlet Sessions (وقت/حد أدنى/أيام) | **P0** | §4 ص17-20 |
| S-POS-006 | Link Outlet Order Types (KOT # Type) | **P0** | §5 ص20-23 |
| S-POS-007 | Link Outlet Currencies (Round Off لكل عملة) | **P0** | §6 ص23-25 |
| S-POS-008 | Departments for NC | **P0** | §7 ص25-28 |
| S-POS-009 | Menu Groups | **P0** | §8 ص28-31 |
| S-POS-010 | Servers (+Employee #) | **P0** | §9 ص31-34 |
| S-POS-011 | Server Outlet Mapping | P1 | §10 ص34-35 |
| S-POS-012 | Menu Levels | **P0** | §11 ص35-37 |
| S-POS-013 | Restaurant Table Master | **P0** | §12 ص37-39 |
| S-POS-014 | Item Hot Keys | P1 | §13 ص39-41 |
| S-POS-015 | Touch Screen Groups | **P0** | §14 ص41-44 |
| S-POS-016 | Kitchens (+Network Printer) | **P0** | §15 ص44-47 |
| S-POS-017 | Sales Report Definition (أعمدة مخصصة) | P1 | §16 ص47-49 |
| S-POS-018 | **Outlet Settlements** | **P0** | §17 ص50-52 |
| S-POS-019 | POS Report Options (Void/Comp) | P1 | §18 ص52-54 |
| S-POS-020 | Open Items Definition (+طابعات المطابخ) | P1 | §19 ص54-56 |
| S-POS-021 | **POS User Access (×Regular/Touch/PDA)** | **P0** أمن | §20 ص56-58 |
| S-POS-022 | Setup Area (مناطق التوصيل) | P2 | §21(2) ص58-60 |
| S-POS-023 | Restrict Outlet Access | **P0** أمن | §22 ص60-61 |
| S-POS-024 | **User Defined Print Forms** (مصمم كامل: Project/PageLayout/ToolBox/F4/F3/Body/Logo/UserText/Active) | P1 (9 شاشات فرعية) | §23 ص61-68 |
| S-POS-025 | Parameter List → IDS Report Engine | P2 | §24(2) ص69-71 |
| S-POS-026 | **Menu Master — Common** (Attr 29=Yes) | **P0** | §24 ص71-73 |
| S-POS-027 | **Menu Master — Per-Outlet** (+Local/Foreign tabs) | **P0** | §24 ص73-75 |
| S-POS-028 | POS Rate Master (تحديث + نقل بين منافذ) | **P0** | §25 ص75-79 |
| S-POS-029 | Modifier Master | **P0** | §26 ص79-82 |
| S-POS-030 | Touch Screen Modifiers (Modifier + Group + Link) | **P0** (3 شاشات) | §27 ص82-89 |
| S-POS-031 | Quick Menu Update (Option 1/2) | **P0** | §28 ص89-91 |
| S-POS-032 | Batch Rate Change (All/Range + Tax) | **P0** | §29 ص91-93 |
| S-POS-033 | **Issue KOT Book** (≤100 ورقة) | **P0** | §30 ص93-95 |
| S-POS-034 | Happy Hours Definition (+Modify بالنِسب) | **P0** | §31 ص95-98 |
| S-POS-035 | Sales Promotion Master (Main/Addl/Comp) | P1 | §32 ص98-102 |
| S-POS-036 | Central KOT Definition | P1 | §33 ص102-104 |
| S-POS-037 | Bill Printer Selection (متعدد) | P1 | §34 ص104-106 |
| S-POS-038 | DSR Session Group (≤3) | P1 | §36 ص106-108 |
| S-POS-039 | Purge KOT Books | P2 | §37 ص108-109 |
| S-POS-040 | Guest Survey Template | P1 | §38 ص109-111 |
| S-POS-041 | **Design Table Layout** (مصمم مرئي + Floor + نسخ) | **P0** | §39 ص111-115 |
| S-POS-042 | Update NC Change | P1 | §40 ص115-116 |
| S-POS-043 | **Member Discount Defn.** (Member × Outlet × Menu Type) | **P0** | §41 ص116-122 |
| S-POS-044 | Taxcode Mapping — **فارغ في المصدر!** | — | §42 ص122 |

## 2. شاشات Guest History (POS-GST) — 22 شاشة

| # | الشاشة | الأولوية | المصدر |
|---|---|---|---|
| S-POS-045 | Guest Master — اختيار المنفذ ثم الرئيسية | **P0** | §1 ص3-4 |
| S-POS-046 | Guest Contact (Company F1) | P1 | §1 ص5 |
| S-POS-047 | Passport Details | P1 | §1 ص6 |
| S-POS-048 | Personal Details (+Children +Privilege Card) | P1 (3 شاشات) | §1 ص7-11 |
| S-POS-049 | **Visit Details (+Breakup أصناف!)** | **P0** | §1 ص11-13 |
| S-POS-050 | Likes & Dislikes | P1 | §1 ص13-14 |
| S-POS-051 | Comments | P1 | §1 ص15 |
| S-POS-052 | Complaint Details (Department+Nature) | P1 | §1 ص15-16 |
| S-POS-053 | Visual (صورة الضيف) | P2 | §1 ص16-17 |
| S-POS-054 | Preferences (من FO + Activities) | P1 | §1 ص17-18 |
| S-POS-055 | Setup Loyalty Cards | P1 | §2 ص18-19 |
| S-POS-056 | **Setup Loyalty Master** (+Discount Info/Covers) | **P0** | §3 ص19-24 |
| S-POS-057 | Post Guest History (+بحث +إنشاء جديد) | **P0** | §4 ص24-28 |
| S-POS-058 | Anniversary List (+More criteria) | P1 | §5 ص28-33 |
| S-POS-059 | Birthday List (Guest/Spouse DOB) | P1 | §6 ص33-36 |
| S-POS-060 | Mailing Labels (2/3 أعمدة) | P2 | §7 ص36-40 |
| S-POS-061 | Mailing Letters (Letter Path) | P2 | §8 ص40-44 |
| S-POS-062 | Repeat Guest List | P1 | §9 ص44-49 |
| S-POS-063 | Guest Comments Entry (تصنيف التقييم) | P1 | §10 ص49-52 |
| S-POS-064 | Guest Comment Report | P1 | §11 ص52-54 |
| S-POS-065 | Guest Comment Analysis (Acceptance Audit) | P1 | §12 ص54-56 |

## 3. شاشات Lookups (POS-LUK) — 8 شاشات

| # | الشاشة | الوظيفة | المصدر |
|---|---|---|---|
| S-POS-066 | Pending KOTs | KOTs بانتظار الفوترة (بالكميات والإجماليات) | §1 ص2-3 |
| S-POS-067 | Pending Bills | الفواتير بانتظار التسوية + التفاصيل | §2 ص3-5 |
| S-POS-068 | **Table Booking Status** | حجوزات الطاولات بتاريخ + Defined tables | §3 ص5-7 |
| S-POS-069 | Browse KOTs | شهر/سنة × KOT# أو Bill# | §4 ص7-8 |
| S-POS-070 | **Settlement Summary** | التسويات بأنماطها (cash/credit/cheque/forex/coupon) + الصافي لكل نمط | §5 ص8-10 |
| S-POS-071 | **Session Statistics** (+NC KOT/KOT Audit/Happy Hours/Void-Comp-BOH/Table Booking/Menu Movement) | إحصاءات الجلسة + **Average Per Check = Settlement Amount / No. of Bills** + Covers | §6 ص10-13 |
| S-POS-072 | Consolidated Sales | نوع قائمة × تحصيل (Cash/Credit) | §7 ص14 |

## 4. شاشات العمليات (Touch Screen) — مسارات العمل اليومية

| # | المسار | المكونات | المصدر |
|---|---|---|---|
| S-POS-073 | **Login** (اختيار DB: PMS/Dummy + Online Keyboard) | Userid/Password | TS ص1-3 |
| S-POS-074 | **Open Shift** (لكل كاشير) + Preview | Restaurant + Shift | TS ص4 |
| S-POS-075 | **Open Outlet** (شخص واحد) + تغيير Session | Accounting Date + Session | TS ص5-6 |
| S-POS-076 | **Order Entry** (Steward + Table + 4 مستويات قائمة + QTY) | Main Screen (Status: منفذ/جلسة/كاشير/تاريخ/طاولة/نادل) | TS ص7-15 |
| S-POS-077 | **Modify/Void** (أسباب معرفة/جديدة) + Modifiers/Chasers + Open Items + Promo/Comp + Repeat | TS ص16-22 |
| S-POS-078 | **Check Printing** (Print Bill/Provisional/Discount/Tax Exempt/View KOT) | TS ص23-27 |
| S-POS-079 | **Split Check** (Equal/Item/Quantity) | TS ص28-31 |
| S-POS-080 | **Settlement** (Cash/CC/Cheque/Coupon/Guest/Void + Resettle + Balance=0) | TS ص32-36 |
| S-POS-081 | **NC Operations** (NC KOT Details + NC Bill Print + NC Tips) | TS ص37-40 |
| S-POS-082 | **النقل والربط** (T.Trnf + S.Trnf + Link Tables + Table Suffix) + **Reprint قبل التسوية** | TS ص41-45 |
| S-POS-083 | **Day Closing** (Close Shift لكل كاشير + Close Outlet) | TS ص46 |

> **إحصاء:** 83 مساراً/شاشة موثقة + 9-12 فرعية داخل المصمم الطباعي والقوائم ≈ **95 شاشة** — الأكبر بين الوحدات المحللة حتى الآن (FO 193 شاشة تشمل المسارات الفرعية).
