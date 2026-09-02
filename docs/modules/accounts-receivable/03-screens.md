# 03 — كتالوج الشاشات (Screens) — وحدة ACR

> الجرد من المسارات الوظيفية الموثقة في الملفات الخمسة. الأولوية: **P0** تشغيل يومي لا غنى عنه · **P1** أسبوعي/شهري · **P2** إداري/استثنائي. الإجمالي: **~88 شاشة** (34 شغّالة + 21 فرعية/مساعدة + 23 شاشة تقارير + 10 معاينات/مخرجات).

---

## 1. شاشات Setup (ACR-SET) — 20 شاشة

| # | الشاشة | المسار الوظيفي | الأولوية | المصدر |
|---|---|---|---|---|
| S-AR-001 | AR Start Date | Setup → AR Start Date (MMYY ذري) | **P0** (مرة واحدة) | §1 ص2 |
| S-AR-002 | AR Opening Balance (رئيسية) | Setup → AR Opening Balance | **P0** (تأسيس) | §2 ص3 |
| S-AR-003 | Opening Balance — Debit | زر Debit داخل S-AR-002 | **P0** | §2 ص4 |
| S-AR-004 | Opening Balance — Credit (نقد) | زر Credit → Cash | P1 | §2 ص4-5 |
| S-AR-005 | Opening Balance — شيك (Bank Details) | Credit → Cheque + قائمة البنوك | P1 | §2 ص5-6 |
| S-AR-006 | Opening Balance — بطاقة ائتمان | Credit → Credit Card | P1 | §2 ص6 |
| S-AR-007 | Opening Balance — Adjustment | زر Adjustment | P1 | §2 ص6-7 |
| S-AR-008 | Opening Balance — Modify + Search | معايير: Doc#/Company/Name/Bill#/Date/Receipt# | P2 | §2 ص7-8 |
| S-AR-009 | Specify Aging | Setup → Specify Aging (To فقط) | **P0** (تأسيس) | §3 ص8 |
| S-AR-010 | Aging with Interest | زر Interest داخل S-AR-009 | P1 | §3 ص9 |
| S-AR-011 | AR User Access (المصفوفة) | Setup → AR User Access | **P0** (أمن) | §4 ص9 |
| S-AR-012 | AR User Access — صفوف الصلاحيات | Double-click على مستخدم → D/C/A/Post | **P0** | §4 ص10 |
| S-AR-013 | Company Profile (رئيسية) | Setup → Company Profile — **Master مشترك** | **P0** | §5 ص11 |
| S-AR-014 | Bookers Details | زار Bookers داخل Profile | P1 | §5 ص12-13 |
| S-AR-015 | Company AR Details | زر AR (Bypass/Credit/Limit/Interest...) | **P0** | §5 ص13-14 |
| S-AR-016 | Company Contact Details | زر Contacts | P1 | §5 ص14-15 |
| S-AR-017 | ربط Revenue Discount Master | زر Discount | P1 | §5 ص15-16 |
| S-AR-018 | Blacklist Details | زار Black List (Modify فقط!) | P1 | §5 ص16 |
| S-AR-019 | Company Profile — Modify | زر Modify + F1 | P1 | §5 ص17-18 |
| S-AR-020 | Purge ACR Audit Table | Setup → Purge (≥60 يوم) | P2 | §7 ص18 |

## 2. شاشات Operations (ACR-OPR) — 27 شاشة

| # | الشاشة | المسار الوظيفي | الأولوية | المصدر |
|---|---|---|---|---|
| S-AR-021 | Transaction Entry (AR) الرئيسية | Operations → Transaction Entry | **P0** يومي | §1 ص2 |
| S-AR-022 | Debit Entry (+ تفاصيل بطاقة/شيك) | زر Debit → Add | **P0** | §1 ص3-4 |
| S-AR-023 | Credit Entry — مباشر على فاتورة | زر Credit (Method 1 — Attr#6=No) | **P0** | §1 ص4 |
| S-AR-024 | Credit Entry — Unallocated | زر Credit (Method 2 — Attr#6=Yes) | **P0** | §1 ص4 |
| S-AR-025 | **Multiple Bill Settlement** | Credit → POST → شركة/عقار/فاتورة | **P0** | §1 ص4-5 |
| S-AR-026 | تفاصيل المطابقة (أعمدة الفاتورة) | جدول: Bill#/Outlet/Property/Currency/XRate/Exchange paid/Bill Amt/Settled/Receipt/Adjust/Balance | **P0** | §1 ص5 |
| S-AR-027 | Bank Details (شيك أثناء التسوية) | زر Bank | **P0** | §1 ص6 |
| S-AR-028 | خيار إيصال الفارق (Overpayment) | "generate a Receipt for the Balance amount" Yes/No | **P0** | §1 ص7 |
| S-AR-029 | Adjustment Entry | زر Adjustment (فاتورة قائمة فقط) | **P0** | §1 ص7-8 |
| S-AR-030 | Browse / Search Criteria | زر Browse (6 معايير) | **P0** | §1 ص8 |
| S-AR-031 | عارض فاتورة FO/POS المصدر | زر عرض تفاصيل فاتورة FO | P1 | §1 ص9 |
| S-AR-032 | عارض تفاصيل الشركة | زر Company | P1 | §1 ص9 |
| S-AR-033 | FA Transaction (نافذة الترحيل) | تفتح عند الحفظ (INI #56=0) — **شاشة FAS مستدعاة** | **P0** | §1 ص10 |
| S-AR-034 | Match Bills–Receipts (رئيسية) | Operations → Match Bills–Receipts | **P0** (Attr#6=Yes) | §2 ص10 |
| S-AR-035 | Selection Criteria (عقار/فاتورة) | زر Selection | P1 | §2 ص11 |
| S-AR-036 | جدول المطابقة (إيصال × فواتير) | اختيار إيصال واحد + فواتير متعددة + Adjusted Amount | **P0** | §2 ص11 |
| S-AR-037 | تأكيد حفظ المطابقة | Save | P1 | §2 ص11 |
| S-AR-038 | Travel Agent Commissions | Operations → TA Commissions | P1 | §3 ص12 |
| S-AR-039 | TA Commissions — التفاصيل والنِسب | جدول الفواتير + إدخال % لكل فاتورة | P1 | §3 ص12-13 |
| S-AR-040 | Credit Card Consolidation | Operations → CC Consolidation | P1 | §4 ص13 |
| S-AR-041 | CC Consolidation — تجميع (Option #) | ترقيم المجموعات في عمود Option | P1 | §4 ص14 |
| S-AR-042 | Outstanding Update | Operations → Outstanding Update | P1 | §5 ص14-15 |
| S-AR-043 | Receipts Untagging | Operations → Receipts Untagging | P2 | §6 ص16 |
| S-AR-044 | Company Help (F1) | نافذة مساعدة الشركات | P2 | §6 ص16-17 |
| S-AR-045 | Receipt Help (بحث بتاريخ/فاتورة) | معايير Receipt Date/Bill # + النتائج | P2 | §6 ص17-18 |
| S-AR-046 | تحميل تفاصيل الإيصال + Untag | Double-click في عمود UnTag → YES | P2 | §6 ص19 |
| S-AR-047 | **Statement of Accounts (SOA)** | Operations → SOA (MMYY متسلسل) | **P0** شهري | §7 ص20 |
| S-AR-048 | **Rollback Statement of A/C** | Operations → Rollback (Cutoff MMYY) | **P0** استثنائي | §8 ص21 |

## 3. شاشات Credit Trace (ACR-CRT) — 11 شاشة

| # | الشاشة | المسار الوظيفي | الأولوية | المصدر |
|---|---|---|---|---|
| S-AR-049 | Debtors Follow-Up (رئيسية) | Credit Trace → Debtors Follow-Up | **P0** (تحصيل) | ص1 |
| S-AR-050 | Advanced Search | زار Show Advanced Search (أولويات البحث) | P1 | ص2 |
| S-AR-051 | Transactions (عرض القيود) | التبويب الافتراضي | **P0** | ص2-3 |
| S-AR-052 | Follow-Up Entry | اختيار فواتير (Tagged Bills) + نشاط + تعيين + بروقكت | **P0** | ص3 |
| S-AR-053 | Bill Details (مدين/دائن) | Double-click على قيد → الدائن والمدين | P1 | ص3-4 |
| S-AR-054 | تفاصيل القيد + الضيف | Double-click + Guest name | P1 | ص4 |
| S-AR-055 | Charge Break-up | Double-click على المبلغ | P1 | ص4 |
| S-AR-056 | Company Info Tab | التبويب + إضافة جهات اتصال | P1 | ص5-6 |
| S-AR-057 | Follow-Up Trace | التبويب (شركة/مكلَّف/وضع/مغلق) | **P0** | ص6-7 |
| S-AR-058 | Projection Report | التبويب (مدى + وضع + تفاصيل) | **P0** | ص7 |

## 4. شاشات Billings (ACR-BIL) — 10 شاشات

| # | الشاشة | المسار الوظيفي | الأولوية | المصدر |
|---|---|---|---|---|
| S-AR-059 | Monthly Invoice Statement | Billings → Monthly Invoice (From/To Company + MMYY) | **P0** شهري | §1 ص2 |
| S-AR-060 | Print Invoice (الرئيسية) | Billings → Print Invoice/Reminder | **P0** | §2 ص3 |
| S-AR-061 | Invoice Options (Req. Inv Selection...) | Attr#2 + نطاق + As On + عملة + عنوان | **P0** | §2 ص4 |
| S-AR-062 | عنوان جديد للفاتورة | زر New Address | P1 | §2 ص4 |
| S-AR-063 | مواصفات الطباعة (Bill Spec/نسخ/Aging/Email) | User Defined Bill Spec + Copies + Aging ☑ | **P0** | §2 ص5 |
| S-AR-064 | **Cancel Invoice** (نطاق أرقام) | زر Cancel → From/To Invoice # | **P0** استثنائي | §2 ص5 |
| S-AR-065 | **Reprint Invoice** | زر Reprint → نطاق أرقام | P1 | §2 ص6 |
| S-AR-066 | Print Receipt | Billings → Print Receipt (مدى + تاريخ + خيارات) | P1 | §3 ص6-7 |
| S-AR-067 | معاينة سند القبض | Output | P1 | §3 ص7 |
| S-AR-068 | Balance Confirmation AR | Billings → Balance Confirmation | P1 | §4 ص7-8 |

## 5. شاشات Reports & Lookups (ACR-RPL) — 23 شاشة (+ معاينات مخرجاتها)

| # | الشاشة/التقرير | المدخلات الجوهرية | الأولوية | المصدر |
|---|---|---|---|---|
| S-AR-069 | Opening Balance List | Property + O/S As on MMYY (افتراضي Start Date) | P2 | §1 ص2-3 |
| S-AR-070 | Transaction List | مدى + نوع (D/C/A) + billed/unbilled + auto/manual + unadjusted | **P0** | §2 ص3-5 |
| S-AR-071 | Balance by A/C Type | MMYY + عقار + عملة + نوع شركة | P1 | §3 ص5-6 |
| S-AR-072 | Ledger Balance | مدى + نطاق شركات + **8 خيارات طباعة** + ترتيب (Trans/Bill Date) | **P0** | §4 ص6-8 |
| S-AR-073 | Folio Outstanding | Cut Off + Yes/No (credits up to) + خيارات | **P0** | §5 ص8-10 |
| S-AR-074 | Aging Summary | As of + Folio/Sector/Sales Exec + Detail/Summary + **5 خيارات** + تعديل فترات | **P0** | §6 ص10-11 |
| S-AR-075 | A/C Balance Detail | Outstanding over (أيام) + Amount | P1 | §7 ص11-13 |
| S-AR-076 | Credit Card Register | شركة CC + مدى **ضمن نفس الشهر** + Commission% + Summary + Update ☑ | **P0** | §8 ص13-15 |
| S-AR-077 | SOA Print | شهر + نطاق شركات + عنوان + صفحة لكل شركة | **P0** | §9 ص15-17 |
| S-AR-078 | Payment Follow-up Report | As on + نوع شركة + Bill/Consolidated + Net Balance (All/D/C) | **P0** | §10 ص17-19 |
| S-AR-079 | Transaction Audit | مدى + All/Company/User — **حالات Del/Old/New** | **P0** (تدقيق) | §11 ص19-20 |
| S-AR-080 | Commission Report | CC/TA/All + مدى + ترتيب + Detail/Summary | P1 | §12 ص20-22 |
| S-AR-081 | ~~"12123"~~ | **PENDING في المصدر — لا شاشة موثقة** | — | §13 ص21 |
| S-AR-082 | Receipt Register (ACR) | Cash/Cheque&CC + ترتيب (Receipt#/Date/Bill#) + بنك | P1 | §14 ص22-23 |
| S-AR-083 | Cheque Deposit Statement | Cheque/Trans Date wise + Local/Outstation + 3 أنماط تلخيص | **P0** (إيداع) | §15 ص23-25 |
| S-AR-084 | Monthly Summary Report | Property + نوع شركة + مدى | P1 | §16 ص25-26 |
| S-AR-085 | A/C Balance Query | شركة + All/Unmatched + مدى شهور + **Merge** | P1 | §17 ص26-27 |
| S-AR-086 | Outstanding Snapshots | مدى + **High Balance range** + A/C Type + Display Code/Type | P1 | §18 ص27-29 |
| S-AR-087 | Receipts Display | billed / credit&advance + معايير 4 | P1 | §19 ص29-30 |
| S-AR-088 | Browse Transactions | مدى MMYY **ضمن نفس السنة المالية** + 8 معايير | P1 | §20 ص30-32 |
| — | Debtor Outstanding Report | Property + Sales Exec + Cut off | P1 | §21 ص32-33 |
| — | Daily Receipt Register by Invoice | مدى + أنواع شركات + وسيلة دفع | P1 | §22 ص33 |
| — | IDS Report Designer | مصمم تقارير مخصص | P2 | §23 ص33 |

> **إحصاءات كتالوج الوحدة:** 88 شاشة موثقة (SET 20 · OPR 27+1 مستدعاة من FAS · CRT 10 · BIL 10 · RPL 23 مع 10 معاينات موثقة كسطور إخراج). أنماط مساعدة عامة: Browse/Add/Modify/Delete/Prev/Next/Save/Exit + F1 lookups + Double-click تنقيط (ACR-SET ص1-2 "Identifying Standards").
