# 07 — الدعم التشغيلي: طباعة متسلسلة، مطابقة، HK، مفقودات، غسيل (REP §107–114)

> ~11 تقريراً تربط FO بالإدارات الخلفية (HK/MGT) وتبني أدوات الإنتاجية اليومية.

---

## 1. Reports in Sequence Print (107) — أداة الإنتاجية القصوى

(البنية التحتية الكاملة في `01-report-engine-infrastructure.md` §4 — INI Switch 63 + Program IDs بفواصل + Execute.)

الجوهر التشغيلي: "This option is helpful to the User where he wants to print **a long list of various reports on a daily basis**... At the end of the day he can select this quick option to print all the required reports." — **آلية Playlist يومية** تقابلها ERPNext في Report Book/Print Bundle.

## 2. Room Verification Report (108) — الضابط التشغيلي

- "generated to **tally the rooms' status report given by the House Keeping with that of Front Office**" — توثيق رسمي للمطابقة الثنائية المصدر (FO vs HK).
- الخيارات الثلاث: **Include Dummy Rooms** ("rooms which will not be given to guests, they will be **for demo purposes only**") · **Display House Keeping Status Only** · **Discrepencies Only** ("only the discrepencies in the rooms statuses given by Front Office and House keeping").

**الأثر**: الحالة الموثوقة ثنائية — Discrepancy ككيان تشغيلي أول (يُحل بـ Room Reconciliation عند التنفيذ).

## 3. تقارير House Keeping المخزنية (109–110) — جسر MGT

| # | التقرير | الخصوصية |
|---|---|---|
| 109 | **HK Item Check List** | "list of items available at **all the stores** like the House Keeping Store, Beverage Store, Food Store, Stationery Store etc... view the stock status of all the items and **order the required stock**" · Store dropdown · مرشح: **By Item Group / Classification / Rate Type** — استهلاك مباشر لماسترات MGT |
| 110 | **HK Consumption Report** | **Date Wise (DDMMYY) / Month Wise (MMYY)** — صيغ إدخال مختصرة نادرة! · نوع المعاملة: **All / Issue / IssueReturn** ("only those transactions where the **excess issued items were retuned back**") · **Floor Man** dropdown (من نفّذ!) · Transaction To: **All / Room / Other Place** · Room Types + **Floors + Blocks** (نقر اختيار متعدد) · **Rate Type: All / Manual / Inventory** · Order By: Item Group/Classification/Room No/User (+ فلترة Transaction Date في الوضع الشهري) · **Print Room Status** |

**القراءة البنيوية**: 110 أغنى تقرير تشغيلي معايير في REP (12 بعداً) — يكشف أن استهلاك HK يُسجل بعمال الأدوار وأماكن غير الغرف (Other Place) وبمعدلين (يدوي/مخزني) — يقابل ERPNext Stock Issue/Return مع Dimension تحليلية.

## 4. Lost & Found Article (111) — سبع زوايا استرجاع

الخيارات الحرفية: **All** (لا تظهر الخيارات الفرعية!) · **Lost Details** (Article + فترة + مكان الفقد) · **Found Details** (نفس الحقول) · **Guest Details** (Room#/Reg#/Guest Name — "**Atleast one field should be entered**"!) · **Article** (اسم + Room/Ref#) · **Ref./Room#**.

**القراءة**: بحث مقيد بالحد الأدنى (validation صريحة) — النموذج يستوعب دورة فقد→وجدان كاملة بحقل مكان، والمخرَج قابل للتصفية بكل زاوية استرجاع.

## 5. عائلة الغسيل (112–114)

| # | التقرير | الخصوصية |
|---|---|---|
| 112 | **Laundry Master List** | "laundry master for the given date" · **Service Type**: "Dry Cleaning and Pressing" (+ الغسيل) — ماستر الخدمات الثلاث |
| 113.1 | **Sales by Item** | "≤ accounting date" + same month · **Bill To: Guest A/C أو Ledger A/C** (ذمم!) · **By Item Consolidated: Yes/No** |
| 113.2 | **Sales Report** | + **Include Void amount in Total** — إبطالات الغسيل تُحتسب في الإجمالي عند الطلب |
| 113.3 | **Detailed Sales** | "across months" · **checkboxes لأنواع الخدمة** · **Item Range From/To** · Detailed/Consolidated |
| 114 | **Re-Print Laundry Bills** | "after all settlements are done at the Front Office" · **Specific date أو Month & Year** · Bill# (F1/Help) |

**ملاحظة تكاملية**: الغسيل فاتورة داخل FO (Bill#) بتسوية FO — يؤكد أن Laundry outlet كامل داخل حدود FO (مثل CAS) لا وحدة مستقلة.

## 6. خلاصة الجسور التشغيلية في هذه العائلة

| الجسر | الشاهد | الاتجاه |
|---|---|---|
| FO → MGT (مخازن/أصناف) | 109 stores + Item Group/Classification | استهلاك ماستر |
| FO → MGT (حركة) | 110 Issue/IssueReturn + Inventory rate | استهلاك حركات |
| FO ↔ HK (حالة الغرف) | 108 مطابقة + Discrepancies | ثنائي |
| FO → SMS/TEL | 107 playlist لا يرتبط — (بلا) | — |
| التشغيل الداخلي | 111/112-114 دورة مفقودات/غسيل | داخلي FO |

واللافت: **لا يوجد تقرير PKI/POS مباشر هنا** (تقارير POS مؤجلة في POS-REP) — جسور POS المالية تظهر فقط في 80/94 (Misc Sales/Consolidated Tax).
