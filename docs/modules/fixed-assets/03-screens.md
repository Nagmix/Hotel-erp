# 03 — فهرس الشاشات (Screens Catalog) — وحدة FXD

> **~21 شاشة** (11 رئيسية + 10 فرعية/نوافذ مدمجة) — نمط "Field / Action / Points to Note" الجدولي الفريد لأدلة FN6i؛ لا شاشة واحدة مرسومة بمعمارية مختلفة عن النمط؛ كثافة شاشة Master (35 حقلاً + شبكتان) تعادل كثافة شاشات HRP.

---

## 1. الجرد الكامل

| # | الشاشة | النوع | الوصول | المصدر |
|---|---|---|---|---|
| S-FX-01 | Fixed Asset Start Date | بارامتر (Property + MMYY + أثر) | Double-click من القائمة | §1 ص3-4 |
| S-FX-02 | Asset Main Groups | ماستر | Double-click | §2 ص4 |
| S-FX-03 | Asset Sub Group | ماستر + ربط GL | Double-click | §3 ص4-5 |
| S-FX-04 | Asset Locations | ماستر | Double-click | §4 ص5-6 |
| S-FX-05 | Asset Components | ماستر | Double-click | §5 ص6-7 |
| S-FX-06 | **Fixed Asset Master** | ماستر مركزي (35 حقلاً + شبكتا Tax/Component + Current closing) | Double-click | §6 ص7-10 |
| S-FX-06a | Tax Detail (popup) | فرعية | Double-click على شبكة Tax Selection | ص9 |
| S-FX-06b | Component Detail (popup) | فرعية | Double-click على شبكة Component Selection | ص9-10 |
| S-FX-07 | Depreciation Method (قائمة فرقية) | تهيئة | Double-click | §7 ص10 |
| S-FX-07a | Asset-wise Detail | فرعية | زر **detail** | ص10 |
| S-FX-08 | Fixed Asset Component Entry | معاملة | Double-click | §8 ص11-12 |
| S-FX-09 | **Fixed Assets Transaction** (بيع/استبعاد) | معاملة + ترحيل | Double-click | §9 ص12-14 |
| S-FX-09a | FA Posting Screen | فرعية (عند ربط الأصل) | تلقائية عند البيع | ص13 |
| S-FX-10 | Calculate Depreciation | محرك | Double-click | §10 ص14 |
| S-FX-11 | **FI Depr Posting to FA** | جسر GL | Double-click | §11 ص16-17 |
| S-FX-12 | Depreciation Details (Q) | استعلام | Double-click | §12 ص18 |
| S-FX-13 | Depreciation History (Q) | استعلام | Double-click | §13 ص18-19 |
| S-FX-14 | Disposal History Query | استعلام | Double-click | §14 ص19-20 |
| S-FX-15 | Depreciation Details (R) | تقرير | Double-click | §15 ص20-21 |
| S-FX-16 | Fixed Asset List | تقرير | Double-click | §16 ص21-22 |
| S-FX-17 | Asset Transaction List | تقرير | Double-click | §17 ص22 |
| S-FX-18 | Asset Ledger | تقرير | Double-click | §18 ص23 |
| S-FX-19 | Asset Sales Register | تقرير | Double-click | §19 ص24 |

## 2. تحليل أنماط التفاعل الموثقة

| النمط | الشاشات | ملاحظات |
|---|---|---|
| **F1 (قائمة مساعدة)** | Locations · Components · Sub Group (Master) · Currency · UMO · Supplier · Asset Code (في المعاملات والتقارير) | سائد كالمعتاد |
| **F3 (فترة مالية)** | Method · FI Posting · 4 استعلامات/تقارير | ثالث وحدة تعتمده بعد FAS/HRP |
| **حقول آلية** | Total Value (Qty×Price) · Currency rate · Exchange amount · Local Amount (Sale×Rate) · Asset Value · Gain/Loss · Asset code (12 محرفاً) | 8 حقول آلية — أعلى كثافة حسابية بعد HRP-PNT |
| **حقول عرض فقط (Browse/Modify)** | Last date depn · Current closing details · Installation Date (في Transaction) · User/Last Updated | التاريخ لا يُدخل إلا في الماستر |
| **Double-click على الشبكة** | Tax Selection · Component Selection (يفتح popup) | النمط المزدوج المعروف |
| **أزرار تحكم موثقة** | Load · Save (في FI Posting) · Order-style في التقارير | Load قبل Save إلزامي في FI Posting |
| **الاختيار من قائمة/نافذة ثم إدخال** | Receive نمط غير موجود هنا — المعاملات مباشرة الحقول | |

## 3. شاشة FI Depr Posting to FA بالتفصيل (أهم شاشة تشغيلية)

| الحقل | الفعل | ملاحظات |
|---|---|---|
| Property | اختيار | |
| Transaction Type | اختيار من قائمة | **قائمة القيم غير موثقة!** (UNK-069) |
| Date [MMYY] | شهر+سنة | |
| Financial Year | F3 | |
| Last Dep. Post Date | عرض | ذاكرة آخر ترحيل |
| Last Dep. Calc Date | عرض | ذاكرة آخر حساب — **التمييز Post/Calc مرئيان معاً!** |
| Group by | **Sub group wise / Asset wise** | "Displays grid values as per the definition" لكن "**Posting will be done as per sub group wise only**" — العرض مرن والترحيل جامد (راجع 05 BR-FX-16) |
| Load | عرض التفاصيل | |
| Save | الترحيل إلى Financial Module | |

## 4. ملاحظات UX مقتبسة

- "Double–click ... to view the following screen" — وصول موحد عبر القائمة الكلاسيكية (لا شاشة لمس — الوحدة إدوية بحتة).
- الشاشات غير مصورة في المستخرَج النصي كلها لوحظت بأسمائها في TOC فقط (Depreciation Details Q وAsset Transaction List وAsset Ledger — شاشات معايير واحدة).
- لا نافذة تأكيد واحدة موثقة سوى FI Posting (Load→Save ثنائية) — نعومة خطر في وحدة ترحيل GL (راجع 15/17).
