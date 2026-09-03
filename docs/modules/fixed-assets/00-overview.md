# 00 — نظرة عامة (Overview) — وحدة FXD (Fixed Assets)

> **الأصول الثابتة**: **سجل الأصول ومحرك الإهلاك المحاسبي** — وحدة فرعية تحت Financial Management تدير دورة حياة الأصل كاملة (تأسيس → تركيب → إهلاك → بيع/استبعاد) بمعادلتين (Straight Line / Written Down يفصل بينهما **INI #475**)، وترميز آلي هيكلي **12 حرفاً = 5(مجموعة)+3(موقع)+4(مسلسل من FIMSHTBL)**، و**جسر GL حقيقي** عبر ربط كل Sub Group بأربعة حسابات (BS Depr A/c + BS Depr S/L + PL Depr A/C + PL Depr S/L) — **البند F12 في خريطة الترحيل**: "when depreciation is posted for an asset, the relevant profit & loss and balance sheet accounts are updated". المقروء عميقاً كاملاً (الجلسة 15): **FN6i-NT-FAS-FXD (25 ص/19 وظيفة)** — آخر ملفات FAS الثلاثة غير المقروءة مع GTP.

---

## 1. حدود الوحدة

| البند | الوصف الموثق |
|---|---|
| الاسم النظامي | Fixed Assets — وحدة فرعية تحت **Financial Management Module**: "Fixed Assets is a sub-module under Financial Management Module" (ص2) |
| الوظيفة الجوهرية | **تسع وظائف طبقية**: (1) بوابة زمنية (Fixed Asset Start Date)؛ (2) خمسة ماسترات (Main Groups · Sub Groups · Locations · Components · **Fixed Asset Master** بـ~35 حقلاً)؛ (3) تهيئة (Depreciation Method بنِسب SLM/WDM)؛ (4) معاملات (Component Entry · **Transaction بيع/استبعاد**)؛ (5) محركان (Calculate Depreciation بمعادلتين + Rollback · **FI Depr Posting to FA**)؛ (6) 3 استعلامات + 5 تقارير |
| المركز المعماري | **امتداد محاسبي من الطراز الأول**: الوحيدة (مع FAS ذاتها) التي تصرح بتحديث **حسابات P&L وBalance Sheet معاً** نصاً؛ جسرها F12 موثق منذ Phase 0 من فهرس الملف؛ **ترحيل شهري بإلزام تاريخ نهاية الشهر** وبمنهج **SLM حصراً** (رغم حساب WDV!) — أضيق نافذة ترحيل في المشروع |
| نمط التشغيل | **دفعات شهرية** (Calculate → FI Posting شهرياً بتاريخ نهاية الشهر) + معاملات نادرة (شراء/إضافة مكوّن/بيع/استبعاد) + استعلامات آنية؛ **Rollback** موثق للحساب |
| النطاق | خصائص الفنادق كلها · مجموعات movable/immovable · مواقع · مكوّنات (تكاليف تركيب إضافية) · عملات بأسعار صرف آلية · كميات بوحدات قياس · ضرائب شراء · **حياة الأصل بالسنين/الأشهر** · قيمة متبقية (Residual/Scrap) · أرصدة إهلاك افتتاحية · مبيعات/استبعادات بجزئية الكمية (Sold/Disposed/Balance) |
| خارج النطاق | شراء الأصول من المورد (يُسجل مباشرة في Master بمراجع PO#/GRR#/Bill# — **لا دورة P2P هنا**) · صيانة الأصول (ملك MNT — Equipment Master!) · جرد فعلي للأصول (لا ذكر) · إعادة تقييم/تحسين (Revaluation — غائب تماماً) · صلاحيات (لا ذكر) · موظفون (لا ذكر) |

> ⚠️ **أربع ملاحظات معمارية كبرى:** (1) **بوابة أحادية الاتجاه ثانية** — "Once its saved user cannot modify the same" لـStart Date (ص3) — عائلة FNB Costing Start Date تتكرر حرفياً مع بُعد إضافي: **property-wise** (بوابة لكل فندق). (2) **الترميز الآلي الأطول في المشروع** — 12 حرفاً مركبة من ثلاث طبقات (5+3+4) بمسلسل من **FIMSHTBL** — تسريب اسم جدول تقني خام نادر (ثاني تسريب بعد جدول INI نفسه!). (3) **منهجان يُحسبان وطريق واحد يُرحَّل** — Calculate Depreciation يعمل بـSLM **وWDV** لكن FI Posting "will be done on its straight line method of depreciation **only**" (ص16) — انفصال حسابي/ترحيلي فريد. (4) **الربط الرباعي الإلزامي التماثلي** — validation حرفية: "if balance sheet a/c is linked, then profit and loss a/c must be mandatorily linked" (ص5) — كل المجموعة أو لا شيء، لكن الربط نفسه اختياري أصلاً (Unlinked = تُبرز أزرق وتُستثنى من الترحيل!).

## 2. جرد الوظائف الموثقة (19 وظيفة من TOC ص1-2)

| # | الوظيفة | النوع | المصدر |
|---|---|---|---|
| 1 | Fixed Asset Start Date | بوابة/بارامتر | §1 ص2-4 |
| 2 | Asset Main Groups | ماستر | §2 ص4 |
| 3 | Asset Sub Group | ماستر + **ربط GL** | §3 ص4-5 |
| 4 | Asset Locations | ماستر | §4 ص5-6 |
| 5 | Asset Components | ماستر | §5 ص6-7 |
| 6 | Fixed Asset Master | ماستر مركزي (~35 حقلاً + شبكتا Tax/Component) | §6 ص7-10 |
| 7 | Depreciation Method | تهيئة (نِسب SLM/WDM للمجموعة أو الأصل) | §7 ص10-11 |
| 8 | Fixed Asset Component Entry | معاملة (زيادة قيمة الأصل) | §8 ص11-12 |
| 9 | Fixed Assets Transaction | معاملة (بيع/استبعاد + ترحيل GL) | §9 ص12-14 |
| 10 | Calculate Depreciation | محرك دفعات (+Rollback) | §10 ص14-16 |
| 11 | FI Depr Posting to FA | **جسر GL** (شهري/SLM فقط) | §11 ص16-17 |
| 12 | Depreciation Details (Q) | استعلام | §12 ص18 |
| 13 | Depreciation History (Q) | استعلام | §13 ص18-19 |
| 14 | Disposal History Query | استعلام | §14 ص19-20 |
| 15 | Depreciation Details (R) | تقرير | §15 ص20-21 |
| 16 | Fixed Asset List | تقرير | §16 ص21-22 |
| 17 | Asset Transaction List | تقرير | §17 ص22 |
| 18 | Asset Ledger | تقرير | §18 ص23 |
| 19 | Asset Sales Register | تقرير | §19 ص24 |

## 3. المفاهيم الجوهرية الموثقة

| المفهوم | الدلالة | المصدر |
|---|---|---|
| **Fixed Asset Start Date** | "the date from when the fixed asset is **computerised**. The assets which are there **earlier** to this date will be considered as **opening balance assets**. Any transaction... will be greater than this date" — خط التاريخ الفاصل بين عالم الورق والعالم الرقمي؛ property-wise؛ **قفل دائم بعد الحفظ** | ص2-3 |
| **كود الأصل 12=5+3+4** | "Sub group code forms the **first 5**, location code the **next 3** and running serial will be the final 4... from **FIMSHTBL** with combination of group code and location code" — المسلسل **متغير بتغير المجموعة/الموقع** (كل توليفة عدّادها الخاص) | ص7 |
| **ربط Sub Group الرباعي** | BS Depr. A/c + BS Depr S/L + PL Depr A/C + PL Depr S/L + Cost center/department؛ حساب نوع 'sub ledger' يعرض اختيار Sub Ledger؛ **الربط اختياري** لكن التماثل إلزامي | ص5 |
| **التكامل مع Ledger Accounting** | "Asset details **integrate directly** with Ledger Accounting, so when depreciation is posted for an asset, the relevant **profit & loss and balance sheet accounts are updated**" — تصريح النوايا المؤسِّس | ص2 |
| **الإهلاك الشهري SLM فقط للترحيل** | "Posting to FA will be done on **monthly basis, where posting date will be month's end date**... on its **straight line method of depreciation only**" | ص16 |
| **الأزرق = غير مرتبط** | "If any of the subgroups is not linked, then those assets posting **will not be done** and the same will be **highlighted with blue color**" — اللون الرابع في المشروع (بعد MNT/POS/FNB) وهنا **لغة استثناء ترحيلي** | ص16 |
| **قيمة الأصل الاسمية عند التخلص** | "Often a company will **assume the value of an asset to be nil** by the end of its depreciation period, so that any amount recovered... will be classed as a **nominal profit**" — فلسفة إهلاكية كاملة في فقرتين | ص2 |
| **المكوّن (Component)** | "additional charges that are **occurred during installation or after**" — شبكتا ماستر: Tax Selection (ضمن القيمة) وComponent Selection "**excluding the asset value**" — قناتا تكلفة مختلفتان | ص6-9 |
| ** جزئية الكمية** | شبكة التفاصيل: Original – Sold – Disposed – **Balance Quantity** — بيع/استبعاد جزئي متاح وأثره محسوب | ص14 |
| **Gain/Loss الآلي** | "If the Sale amount is greater than the Asset value → Profit... lesser → Loss" + "If asset value and sales value is **equal**, then profit and loss ledger selection will be **deactivated**" — قاعدة أصلية نادرة الوضوح | ص13-14 |
| **INI #475** | "Fixed assets module will consider either Straight Line Method or **Written Down Method based on the value of INI switch #475**" — مفتاح المنهج الوحيد | ص2 |

## 4. الإحصاءات المقروءة

| المؤشر | القيمة |
|---|---|
| صفحات مقروءة عميقاً | 25 (ملف واحد — أقصر قراءة وحدة بعد GTP) |
| وظائف موثقة | 19 (5 ماسترات + 1 بارامتر + 1 تهيئة + 3 معاملات/محركات + 1 ترحيل + 3 استعلامات + 5 تقارير) |
| شاشات رئيسية + فرعية | ~21 (راجع 03) |
| قواعد عمل موثقة | BR-FX-01..22 (راجع 05) |
| قيود إدخال موثقة | V-FX-01..13 (راجع 06) |
| قيود GL | **حقيقية موجبة** — أول وحدة بعد FAS ذاتها بمسار ترحيل صريح كامل (راجع 11) |
| مفاتيح INI | **#475** (منهج الإهلاك) + إشارة "INI switch validation" غير مرقمة لحقول PO/GRR/Bill (UNK-073) |
| مجهولات جديدة | UNK-068..073 (راجع 17) |

## 5. موقعها في خريطة المشروع

- **قبلها:** FO (1) → FAS (2) → ACR (3) → POS (4) → SYS (5) → MGT (6) → BNQ (7) → HRP (8) → Care (9) → MEM (10) → SLM (11) → TEL (12) → MNT (13) → FNB (14) → **FXD (15 — هذه الوحدة)**.
- **علاقاتها الواردة:** FAS (دليل الحسابات الرباعي + Financial Year بF3 + Transaction Types) · عملات SYS · موردون (مصدر غير محسوم — عائلة UNK-058) · مراجع PO/GRR/Bill من MGT (حقول حرة) · ضرائب (نظام الضرائب العام).
- **علاقاتها الصادرة:** **F12: FI Depr Posting to FA → FAS** (شهري/SLM/نهاية الشهر + قيود بيع/استبعاد مع Gain/Loss إلى Cash/Bank) · **تقاطع كياني صامت مع MNT** (Equipment Master مقابل Fixed Asset Master — راجع 12/17).
