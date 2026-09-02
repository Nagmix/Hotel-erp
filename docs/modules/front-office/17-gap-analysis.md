# 17 — تحليل الفجوات (Gap Analysis) — وحدة Front Office

> فجوات **التوثيق** (ما لم تجده الوثائق) + فجوات **ERPNext** (من `16-erpnext-mapping.md`). التحليل الرسمي الشامل في Phase 12.

---

## فجوات التوثيق (Documentation Gaps) لوحدة FO

| # | الفجوة | الحالة | خطة الحسم |
|---|---|---|---|
| G-1 | أطراف القيود D/C لكل معاملة FO | `[NOT DOCUMENTED]` | FAS-TRN (Phase 6) |
| G-2 | جرد INI Switches الكامل + أثر كل واحد | جزئي (64 + Foreex voucher) | FOM-SET/SYS-SSP |
| G-3 | جرد FO Module Attributes الكامل | جزئي (16 فقط) | FOM-SET |
| G-4 | بنية Rate Master الحقولية الوظيفية | جداول آلية فقط | FOM-SET §7 قراءة عميقة |
| G-5 | بنية Room Master الحقولية الوظيفية | جداول آلية فقط | FOM-SET §8 قراءة عميقة |
| G-6 | التقارير الرسمية (REP) — كتالوج كامل | فهرس فقط | FOM-REP (Phase 7) |
| G-7 | Guest History — هيكل كامل | مقاطع متفرقة | FOM-GST |
| G-8 | Housekeeping — التكامل الكامل | فهرس فقط | FOM-HSK |
| G-9 | Charge Groups/بنية CRG | فهرس فقط | FOM-CRG |
| G-10 | صلاحيات FO الرسمية (من SYS) | سلوكيات فقط | SYS-SSP (Phase 8) |
| G-11 | تفاصيل Night Balance المحاسبية (UNK-006) | مبدأ فقط | FAS + DEP merge |
| G-12 | سلوك Part Settlement مع بقاء الإشغال — القيود | موثقة السلوك دون قيد | Phase 6 |
| G-13 | آلية Agent Allocation (زر RES) | اسم فقط | RES/SLM |
| G-14 | Daywise Plan Definition (زر RES) | اسم فقط | FOM-SET |

## فجوات ERPNext الأولية (من Seed Mapping)

| الفجوة | الفئة | التأثير |
|---|---|---|
| محرك PMS كله (Reservation/Folio/Night Audit/Room Status) | D/E | Custom App أساسي |
| أتمتة Folio→Invoice→Settlement→AR | C | Workflow/Server Scripts |
| هيكل Rate (Type×Plan×Currency×Date) | C | DocType خاص |
| التسويات الفندقية (9 أنماط + Bill on Hold/Foreex) | C/D | Payment modes موسعة |
| Room Rack UI | E | Frontend مخصص (Next.js) |
| تفويض مزدوج (منفذ/مصرِّح) | C | نمط Workflow |
