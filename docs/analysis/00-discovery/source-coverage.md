# PHASE 0 — تتبع تغطية المصادر (Source Coverage)

> **القاعدة:** لا يُعتبر المشروع مكتملًا قبل تحقيق تغطية 100% أو تسجيل سبب واضح لكل استثناء.
> **التحديث:** تُحدَّث هذه الوثيقة بعد كل جلسة عمل.

**حالة كل ملف:**

| الحالة | المعنى |
|---|---|
| `discovered` | اكتُشف اسمه ومساره فقط |
| `indexed` | أُضيف للجرد مع الصفحات والنوع والفهرس |
| `text-extracted` | استُخرج نصه الكامل إلى `extracted-text/` |
| `toc-analyzed` | حُلِّل فهرسه وأُضيفت موضوعاته لخريطة الوثائق |
| `read` | قُرئ المحتوى الفعلي (Deep Read) |
| `analyzed` | استُخرجت المعرفة الوظيفية إلى `docs/modules/...` |
| `cross-referenced` | رُبطت معرفته بالوحدات الأخرى (workflows/accounting) |
| `verified` | راجعها فحص الجودة (Quality Gate) |

---

## ملخص التغطية الحالية

| المؤشر | القيمة |
|---|---|
| إجمالي الملفات | 65 |
| discovered → indexed | **65 / 65 (100%)** ✅ |
| text-extracted | **65 / 65 (100%)** ✅ |
| toc-analyzed | **65 / 65 (100%)** ✅ |
| field-extracted (جداول الحقول آلياً) | **13 ملف إعدادات — 2,099 حقلاً** ✅ |
| read (قراءة عميقة) | **13/65** — FO: DEP/RES/REG/CAS/SET/LUK/CRG/HSK/GST + FAS: SET/TRN/MST/LUK (نهاية الجلسة 3) |
| analyzed | **13 ملفاً → 8 وحدات فرعية** (FO 19 ملفاً + FAS 18 ملفاً → وحدتا modules) |
| cross-referenced | 0 / 65 |
| verified | 0 / 65 |

> ✅ **النتيجة المهمة:** جميع الملفات الـ 65 نصوصها قابلة للاستخراج آلياً — لا يوجد أي ملف يتطلب OCR. عدد الصور المضمنة ~7,763 (لققطات شاشة) متاحة للتحليل البصري عند الحاجة عبر PyMuPDF.

---

## جدول التغطية التفصيلي

> يُحدَّث عمود "Deep Read" مع تقدم المراحل. الرموز: **✓ = كامل | ◐ = جزئي (مع النسبة) | – = لم يبدأ**. ترتيب الأولويات مبني على وثيقة module-inventory §5.

| # | الوحدة | الملف | الصفحات | indexed | text | toc | deep-read | analyzed | x-ref | verified |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Front Office | FN6i-NT-FOM-SET.pdf | 145 | ✓ | ✓ | ✓ | **✓ كامل (67 قسماً + مصفوفة التعديل 48 Note)** | **✓ → modules/front-office/** | – | – |
| 2 | Front Office | FN6i-NT-FOM-REP.pdf | 120 | ✓ | ✓ | ✓ | – (مؤجل Phase 7) | – | – | – |
| 3 | Front Office | FN6i-NT-FOM-REG.pdf | 105 | ✓ | ✓ | ✓ | **✓ كامل (28 وظيفة، ص1-105)** | **✓ → modules/front-office/** | – | – |
| 4 | Front Office | FN6i-NT-FOM-CAS.pdf | 95 | ✓ | ✓ | ✓ | **✓ كامل (20 وظيفة، ص1-95)** | **✓ → modules/front-office/** | – | – |
| 5 | Front Office | FN6i-NT-FOM-LUK.pdf | 51 | ✓ | ✓ | ✓ | **✓ كامل (22 وظيفة)** | **✓ → modules/front-office/ (09)** | – | – |
| 6 | Front Office | FN6i-NT-FOM-GST.pdf | 57 | ✓ | ✓ | ✓ | **✓ كامل (17 وظيفة + الولاء)** | **✓ → modules/front-office/ (04/05)** | – | – |
| 7 | Front Office | FN6i-NT-FOM-HSK.pdf | 59 | ✓ | ✓ | ✓ | **✓ كامل (18 وظيفة + دورة الغسيل)** | **✓ → modules/front-office/ (04/05)** | – | – |
| 8 | Front Office | FN6i-NT-FOM-RES.pdf | 68 | ✓ | ✓ | ✓ | **✓ كامل (7 وظائف رئيسية، ص1-68)** | **✓ → modules/front-office/** | – | – |
| 9 | Front Office | FN6i-NT-FOM-SMS.pdf | 14 | ✓ | ✓ | ✓ | – | – | – | – |
| 10 | Front Office | FN6i-NT-FOM-CRG.pdf | 19 | ✓ | ✓ | ✓ | **✓ كامل (Concierge — 5 وظائف)** | **✓ → modules/front-office/ (04)** | – | – |
| 11 | Front Office | FN6i-NT-FOM-DEP.pdf | 14 | ✓ | ✓ | ✓ | **✓ كامل** | **✓ → modules/front-office/** | – | – |
| 12 | Point of Sale | FN6i-NT-POS-SET.pdf | 122 | ✓ | ✓ | ✓ | – | – | – | – |
| 13 | Point of Sale | FN6i-NT-POS-REP.pdf | 158 | ✓ | ✓ | ✓ | – | – | – | – |
| 14 | Point of Sale | FN6i-NT-POS-GST.pdf | 56 | ✓ | ✓ | ✓ | – | – | – | – |
| 15 | Point of Sale | FN6i-NT-POS-LUK.pdf | 14 | ✓ | ✓ | ✓ | – | – | – | – |
| 16 | Materials Management | FN6i-NT-MGT-REP.pdf | 112 | ✓ | ✓ | ✓ | – | – | – | – |
| 17 | Materials Management | FN6i-NT-MGT-DNT.pdf | 75 | ✓ | ✓ | ✓ | – | – | – | – |
| 18 | Materials Management | FN6i-NT-MGT-SET.pdf | 68 | ✓ | ✓ | ✓ | – | – | – | – |
| 19 | Materials Management | FN6i-NT-MGT-LUK.pdf | 38 | ✓ | ✓ | ✓ | – | – | – | – |
| 20 | Banquets | FN6i-NT-BNQ-SET.pdf | 98 | ✓ | ✓ | ✓ | – | – | – | – |
| 21 | Banquets | FN6i-NT-BNQ-BIL.pdf | 66 | ✓ | ✓ | ✓ | – | – | – | – |
| 22 | Banquets | FN6i-NT-BNQ-BOK.pdf | 41 | ✓ | ✓ | ✓ | – | – | – | – |
| 23 | Banquets | FN6i-NT-BNQ-CFG.pdf | 38 | ✓ | ✓ | ✓ | – | – | – | – |
| 24 | Banquets | FN6i-NT-BNQ-LUK.pdf | 12 | ✓ | ✓ | ✓ | – | – | – | – |
| 25 | HR & Payroll | FN6i-NT-HRP-REP.pdf | 133 | ✓ | ✓ | ✓ | – | – | – | – |
| 26 | HR & Payroll | FN6i-NT-HRP-PNT.pdf | 47 | ✓ | ✓ | ✓ | – | – | – | – |
| 27 | HR & Payroll | FN6i-NT-HRP-SET.pdf | 42 | ✓ | ✓ | ✓ | – | – | – | – |
| 28 | HR & Payroll | FN6i-NT-HRP-RQP.pdf | 31 | ✓ | ✓ | ✓ | – | – | – | – |
| 29 | Financial Management | FN6i-NT-FAS-REP.pdf | 64 | ✓ | ✓ | ✓ | – (مؤجل Phase 7) | – | – | – |
| 30 | Financial Management | FN6i-NT-FAS-SET.pdf | 48 | ✓ | ✓ | ✓ | **✓ كامل (27 قسماً — الروابط الست)** | **✓ → modules/financial-accounting/** | – | – |
| 31 | Financial Management | FN6i-NT-FAS-TRN.pdf | 45 | ✓ | ✓ | ✓ | **✓ كامل (9 أقسام + FO/POS/PJV posting)** | **✓ → modules/financial-accounting/** | – | – |
| 32 | Financial Management | FN6i-NT-FAS-MST.pdf | 33 | ✓ | ✓ | ✓ | **✓ كامل (COA + Vendor + ChequeBook)** | **✓ → modules/financial-accounting/** | – | – |
| 33 | Financial Management | FN6i-NT-FAS-LUK.pdf | 28 | ✓ | ✓ | ✓ | **✓ كامل (9 استعلامات)** | **✓ → modules/financial-accounting/** | – | – |
| 34 | Care | FORTUNE CARE v6 - OPERATIONS.pdf | 80 | ✓ | ✓ | ✓ | – | – | – | – |
| 35 | Care | FORTUNE CARE v6 - REPORTS & LOOKUPS - VER 10 AUGUST.pdf | 73 | ✓ | ✓ | ✓ | – | – | – | – |
| 36 | Care | FORTUNE CARE v6 - SETUP - VER 10 AUGUST.pdf | 34 | ✓ | ✓ | ✓ | – | – | – | – |
| 37 | Membership | FN6i-NT-MEM-RPL.pdf | 56 | ✓ | ✓ | ✓ | – | – | – | – |
| 38 | Membership | FN6i-NT-MEM-MPF.pdf | 30 | ✓ | ✓ | ✓ | – | – | – | – |
| 39 | Membership | FN6i-NT-MEM-MTR.pdf | 18 | ✓ | ✓ | ✓ | – | – | – | – |
| 40 | Membership | FN6i-NT-MEM-SET.pdf | 16 | ✓ | ✓ | ✓ | – | – | – | – |
| 41 | Membership | FN6i-NT-MEM-MMN.pdf | 13 | ✓ | ✓ | ✓ | – | – | – | – |
| 42 | System Setup | FN6i-NT-SYS-SSP.pdf | 110 | ✓ | ✓ | ✓ | – | – | – | – |
| 43 | Sales & Marketing | FN6i-NT-SLM-PRF.pdf | 42 | ✓ | ✓ | ✓ | – | – | – | – |
| 44 | Sales & Marketing | FN6i-NT-SLM-SLT.pdf | 29 | ✓ | ✓ | ✓ | – | – | – | – |
| 45 | Sales & Marketing | FN6i-NT-SLM-REP.pdf | 22 | ✓ | ✓ | ✓ | – | – | – | – |
| 46 | Sales & Marketing | FN6i-NT-SLM-LUK.pdf | 10 | ✓ | ✓ | ✓ | – | – | – | – |
| 47 | Accounts Receivales | FN6i-NT-ACR-RPL.pdf | 33 | ✓ | ✓ | ✓ | – | – | – | – |
| 48 | Accounts Receivales | FN6i-NT-ACR-OPR.pdf | 21 | ✓ | ✓ | ✓ | – | – | – | – |
| 49 | Accounts Receivales | FN6i-NT-ACR-SET.pdf | 19 | ✓ | ✓ | ✓ | – | – | – | – |
| 50 | Accounts Receivales | FN6i-NT-ACR-BIL.pdf | 8 | ✓ | ✓ | ✓ | – | – | – | – |
| 51 | Accounts Receivales | FN6i-NT-ACR-CRT.pdf | 8 | ✓ | ✓ | ✓ | – | – | – | – |
| 52 | Telephones | FN6i-NT-TEL-SET.pdf | 32 | ✓ | ✓ | ✓ | – | – | – | – |
| 53 | Telephones | FN6i-NT-TEL-LUK.pdf | 21 | ✓ | ✓ | ✓ | – | – | – | – |
| 54 | Telephones | FN6i-NT-TEL-REP.pdf | 20 | ✓ | ✓ | ✓ | – | – | – | – |
| 55 | Telephones | FN6i-NT-TEL-CAC.pdf | 10 | ✓ | ✓ | ✓ | – | – | – | – |
| 56 | Maintenance | FN6i-NT-MNT-RPL.pdf | 29 | ✓ | ✓ | ✓ | – | – | – | – |
| 57 | Maintenance | FN6i-NT-MNT-OPR.pdf | 28 | ✓ | ✓ | ✓ | – | – | – | – |
| 58 | Maintenance | FN6i-NT-MNT-SET.pdf | 24 | ✓ | ✓ | ✓ | – | – | – | – |
| 59 | F&B Costing | FN6i-NT-FNB-REP.pdf | 28 | ✓ | ✓ | ✓ | – | – | – | – |
| 60 | F&B Costing | FN6i-NT-FNB-COP.pdf | 19 | ✓ | ✓ | ✓ | – | – | – | – |
| 61 | F&B Costing | FN6i-NT-FNB-LUK.pdf | 15 | ✓ | ✓ | ✓ | – | – | – | – |
| 62 | F&B Costing | FN6i-NT-FNB-SET.pdf | 14 | ✓ | ✓ | ✓ | – | – | – | – |
| 63 | (root) | Touch_Screen_Manual.pdf | 46 | ✓ | ✓ | ✓ | – | – | – | – |
| 64 | Fixed Assets | FN6i-NT-FAS-FXD.pdf | 25 | ✓ | ✓ | ✓ | – | – | – | – |
| 65 | Gate Passes | FN6i-NT-FAS-GTP.pdf | 13 | ✓ | ✓ | ✓ | – | – | – | – |

---

## استثناءات مسجلة

- **فهارس Care وTouch Screen:** استُخرجت بأنماط مختلفة ودقتها أقل — عولجت بقراءة الصفحات الأولى يدوياً. لا يوجد ملف ناقص.
- **لا توجد ملفات تتطلب OCR** — استثناء OCR غير مطلوب إطلاقاً.
- **مسار مجلد "Accounts Receivales"** فيه خطأ إملائي في المصدر الأصلي (Receivales بدل Receivable) — يُترك كما هو في المصدر ويُصحح في docs.
