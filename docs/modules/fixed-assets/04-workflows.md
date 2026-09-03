# 04 — تدفقات العمل (Workflows) — وحدة FXD

> **WF-FX-01..12** — دورة حياة الأصل الحرفية من غلاف الدليل: **تأسيس (مرة واحدة) → تسجيل أصل (مع مكوّناته وضرائبه) → دورة شهرية أبدية (حساب إهلاك → ترحيل GL) → خروج جزئي أو كامل (بيع/استبعاد) → استعلام**. الدورة الوحيدة في المشروع التي يعلّن فيها الدليل عن **Rollback** كوظيفة من الدرجة الأولى، والتي يفصل فيها بين **حساب** الوحدتين المنهجيتين و**ترحيل** واحد منهما.

---

## WF-FX-01: تأسيس الوحدة (Foundation) — مرة واحدة لكل فندق

```
[دليل حسابات FAS + Cost Centers + Financial Year جاهزة]
        ↓
تحديد Fixed Asset Start Date (Property-wise — MMYY)
        ↓
⚠️ "Once its saved user cannot modify the same" (قفل دائم)
        ↓
Asset Main Groups (movable/immovable...) → Asset Locations → Asset Components
        ↓
Asset Sub Group + الربط الرباعي (BS Depr A/c + BS Depr S/L + PL Depr A/C + PL Depr S/L + Cost Center)
        ↓ [قرار ربط]
مربوط → أصول المجموعة تُرحَّل للمالية | غير مربوط → تُبرز أزرق عند الترحيل وتُستثنى
        ↓
Depreciation Method: نسب SLM% وWDM% (Sub Group level أو asset-wise عبر detail) لكل FY
```

- **مخرجات**: بنية تصنيف جاهزة + قناة GL محددة.
- **نقاط الفشل**: نسيان ربط PL مع BS → validation تمنع الحفظ؛ بدء Start Date خاطئ بلا مسار تصحيح (GAP-FX-P01).

## WF-FX-02: تسجيل أصل جديد (Asset Creation)

```
Fixed Asset Master → Property + Sub Group (F1) + Location
        ↓
[Asset code آلي: 5(فرعية)+3(موقع)+4(مسلسل FIMSHTBL)] — لا يُدخل يدوياً
        ↓
Long name (70) + Short (10) + Manufacturer (60)
        ↓
Date installation (≤ server date) + Currency (افتراضي محلي) + Rate آلي
        ↓
Quantity + UMO + Item price/Qty → [Total Value = Qty × Price آلي]
        ↓
Residual Value/Qty + Life span (سنة/شهر) + Start date depn
        ↓ [أصل ما قبل التحنيط؟]
Start date depn < FA Start Date → إدخال Depn. Op. Bal (رصيد إهلاك موروث)
        ↓
PO#/GRR#/Bill# (+INI validation اختيارية) + Supplier (F1) + Insurer + Maintenance + Asset status
        ↓
شبكة Tax Selection (ضمن القيمة) + شبكة Component Selection (خارجها!)
        ↓
Save → أثر User/Last Updated
```

## WF-FX-03: إضافة مكوّن لأصل قائم (Component Entry) — زيادة القيمة

```
Fixed Asset Component Entry → Property + Financial Period (F3)
        ↓
Asset Code (F1) + Date شراء المكوّن
        ↓
Component Code (F1) + Currency + [Exchange Rate آلي] + Amount
        ↓
[Exchange amount يظهر آلياً] → Save
        ↓
الأثر: "The component added **will increase the asset value**" (ص11)
```

- ⚠️ لا مواصفة لأثر المكوّن على قاعدة/مدة الإهلاك (UNK-070).

## WF-FX-04: حساب الإهلاك الدوري (Calculate Depreciation) — ⭐ المحرك الشهري

```
Calculate Depreciation → "till specified month and year"
        ↓
INI #475 يقرر المنهج:
   ├── Straight-line: (Initial − Final)/Periods  أو  %×القيمة كل فترة
   │     مثال الدليل: £10,000 → £2,000 عبر 10 فترات = £800/فترة
   └── Written Down: %×WDV المتناقص
         مثال الدليل: آلة £75,000، residual £10,000، 5 سنوات، 40%:
         2003:30,000→WDV 45,000 | 2004:18,000→27,000 | 2005:10,800→16,200
         | 2006:6,480→9,720 | 2007:3,888→5,832
        ↓
[ناتج قابلة للـRollback: "can be rolled back with roll back options"]
```

- **التعليق الحرفي النادر**: "these two methods simply provide an **alternative way of allocating** the total depreciation charge over several accounting periods" — الدليل يشرح المفهوم المحاسبي نفسه (نمط تدريبي)!
- مقارنة الدليل: 40% WDV أول 3 سنوات = £58,800 مقابل £39,000 لو SLM — الوعي بالفوارق الجوهرية موثق.

## WF-FX-05: الترحيل إلى المالية (FI Depr Posting to FA) — ⭐ جسر F12

```
FI Depr Posting → Property + Transaction Type + Date[MMYY] + FY (F3)
        ↓
[عرض Last Dep. Post Date + Last Dep. Calc Date — ذاكرتا الفصل]
        ↓
Group by: Sub group wise / Asset wise (عرض فقط)
        ↓
Load → الشبكة
   ├── Sub Groups مربوطة → قابلة للترحيل
   └── Sub Groups غير مربوطة → **تُبرز أزرق** وتُستثنى من الترحيل
        ↓
Save → الترحيل إلى Financial Module
        ↓
⚠️ قواعد الترحيل الصلبة:
   - شهري: "posting date will be month's end date"
   - SLM فقط: "posting... on its straight line method of depreciation only"
   - Sub group wise فقط (عرض asset-wise لا يغير الترحيل)
```

## WF-FX-06: بيع/استبعاد أصل (Fixed Assets Transaction)

```
Transaction → Property + FY + Asset Code (F1) → [Installation Date يعرض]
        ↓
Type: Sale (افتراضي) / Disposal
        ↓
Date + Quantity (جزئية مسموحة) + Currency + Rate
        ↓
Pay Mode: **Bank أو Cash** (بطاقة ائتمانية "will be provided later"!)
        ↓
Sale Amount → [Local Amount = Sale × Rate آلي]
        ↓
[شبكة التفاصيل التاريخية: Original – Sold – Disposed – Balance]
[Asset Value = Qty × Item Price آلي] + [Net Book Value] + [Gain/Loss آلي]
        ↓
[الأصل مربوط بـLedger؟]
   ├── نعم → FA Posting Screen → قيود: accumulated posting ledger (من ربط Sub Group)
   │         + Sale Amount → Cash/Bank account
   │         + P&L ledger (Gain أو Loss حسب المقارنة)
   │         + [Sale = Asset Value → اختيار P&L ledger يُعطَّل!]
   └── لا → سجل محلي بلا ترحيل
        ↓
Save + Remarks
```

## WF-FX-07: الاستعلام اليومي (Queries)

```
Dep Details (Q): FY range → Load (كل أصول الفندق)
Dep History (Q): Property + FY + Location + From/To[MMYY] + From/To Asset
Disposal History: Property + FY + From/To Date + Location + Asset Code
```

## WF-FX-08..12 (ملخصات إجرائية)

| # | التدفق | الخطوات الموثقة |
|---|---|---|
| WF-FX-08 | تقرير Dep Details (R) | FY → From/To[MMYY] → نوع (Asset/Group/Location) → زر الطباعة → طريقة الطباعة |
| WF-FX-09 | تقرير Fixed Asset List | From/To Date → List Type (Asset By/Sub Group By/Location By) → **checkbox 'Zero Quantity Required'** → طباعة |
| WF-FX-10 | تقرير Asset Transaction List | FY → عرض |
| WF-FX-11 | تقرير Asset Ledger | FY → Location أو By Group → عرض ("vital information... Actual Asset value as on date") |
| WF-FX-12 | تقرير Asset Sales Register | FY → **Sales أو Disposal** → عرض |

## الاعتمادات المتقاطعة (Cross-flow Dependencies)

```
FAS (COA + FY + Transaction Types) ──→ كل التهيئة والترحيل
SYS (Currency) ──→ Master/Component/Transaction
[Vendor Master؟] ──→ Supplier code (مصدر غير محسوم — عائلة UNK-058)
MGT (PO/GRR/Bill) ──→ حقول مرجعية حرة فقط (لا ربط نصي)
MNT (Equipment) ──→ تقاطع كياني صامت (راجع 12/17)
```
