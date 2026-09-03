# 16 — الموائمة مع ERPNext/Frappe (ERPNext Mapping) — وحدة FXD

> **F-FX-01..11** — **أنقى تطابق كيان-بأصل في المشروع بأكمله**: ERPNext Asset Module يغطي دورة الحياة حرفياً (Asset + Category + Location + **Depreciation Schedule بمنهجي SLM/WDM معاً!** + إهلاك شهري تلقائي بقيد نهاية الشهر + بيع عبر Sales Invoice بGain/Loss آلي + Scrap/Disposal أصلية!) — الوحدة الوحيدة التي يحتاج فيها "التخصيص" لملء فجوات الدليل (الربط الرباعي والعملة) لا لبناء الماهية. التقدير: **~4 أصول مخصصة / 2-3 أسابيع** (أسرع وحدة تحويل بعد SLM).

---

## 1. الخريطة العامة

| مكون FXD | الأصل Frappe/ERPNext | الحالة | القرار |
|---|---|---|---|
| Fixed Asset Master (35 حقلاً) | **Asset** doctype | ✅✅ جاهز قوي | F-FX-1 |
| Asset Main/Sub Groups | **Asset Category** (مستويان: Category + Sub) | ✅✅ | F-FX-2 |
| Asset Locations | **Location** (الأصلية في Assets) | ✅✅ | F-FX-3 |
| Asset code 12=5+3+4 | naming_series مخصص | 🔧 مخصص بسيط | F-FX-4 |
| **الربط الرباعي BS/PL** | **Asset Category Accounts** (fixed_asset_account · accumulated_depreciation_account · depreciation_expense_account + Company defaults) | ✅✅ **بنيوي حرفي!** | F-FX-5 |
| Depreciation Method (SLM%/WDM%) | **Depreciation Schedule** ( Straight Line / **Written Down** أصلية!) | ✅✅ | F-FX-6 |
| Calculate Depreciation + Rollback | تسجيل القيود من Schedule (posting_dates نهاية الشهر!) + cancel | ✅✅ | F-FX-6 |
| FI Depr Posting (شهري/SLM) | **Asset Depreciation Entry** آلي شهرياً | ✅✅ | F-FX-7 |
| FA Transaction (Sale) | **Sales Invoice للAsset** (+Gain/Loss Journal آلي) | ✅✅ | F-FX-8 |
| FA Transaction (Disposal) | **Asset Scrap/Disposal** | ✅✅ | F-FX-8 |
| Fixed Asset Start Date | تاريخ أول Schedule / opening | 🔧 مخصص بسيط | F-FX-9 |
| Asset Tax/Component grids | Tax Table في Purchase / **Asset Repair + تكلفة** | ✅/🔧 | F-FX-10 |
| Component Entry (زيادة قيمة) | Asset Repair (تكلفة) أو تعديل Value | 🔧 مخصص | F-FX-10 |
| 3 استعلامات + 5 تقارير | Script/Query Reports | 🔧 مخصص | F-FX-11 |
| التقاطع مع MNT Equipment | **Asset Maintenance** (الأصلية!) — تُصان الأصول ذاتها | ✅✅ (يربط I-FX-09!) | F-FX-9 |

## 2. القرارات التفصيلية

### F-FX-1: Asset doctype = Fixed Asset Master ⭐
- الحقول القياسية: asset_name (70) · manufacturer (60) · location · purchase_date/tanggal التركيب (item_code) · gross_purchase_amount · **opening_accumulated_depreciation = Depn. Op. Bal حرفياً!** · residual/expected value · useful_life (سنين/أشهر ✓) · **status** (قائمة قيم جاهزة: Draft/Submitted/Partially Depreciated/fully/Sold/Scrapped — يسد UNK-068!) · custodian/insurance (Asset Insurer!) · remarks.
- إضافات مخصصة: supplier_code (Link Vendor) · PO/GRR/Bill مراجع حرة · UMO/Qty (كمية متعددة = إنشاء n أصول بنفس التكوين — قراري).

### F-FX-2: Category/SubCategory
- Asset Category حقل category في Asset؛ **Main Group** = تصنيف أعلى (Category parent مخصص بسيط أو Value يمثل المستويين).

### F-FX-5: الربط الرباعي = Asset Category Accounts ⭐⭐ (أثقل تطابق)
```
FN6i:  BS Depr A/c      ↔  accumulated_depreciation_account
       BS Depr S/L       ↔  sub-ledger: account + cost_center dims
       PL Depr A/C       ↔  depreciation_expense_account
       PL Depr S/L       ↔  (نفس الحساب + Cost Center)
       Cost center       ↔  finance_book/cost_center dimension
```
- **validation التماثل** (BR-FX-05) = on_validate على child table: أي حساب معبأ → الثلاثة إلزامية — **نفس منطق ERPNext الأصلي** (Accounting Columns إلزامية عند أول تعبئة!).
- غير المربوط = Category بلا Accounts → تُبرز/تُستثنى — يُنفذ E-FX-01 بتقرير "Assets without Accounts".

### F-FX-6: المنهجان والجدولة
- Depreciation Schedule: **Straight Line وWritten Down Value أصلية** — لكن FN6i يقرر بواحد (INI #475): يُبنى **Finance Book واحد بالمنهج المختار** + حقل إعدادي للمنهج الثاني (عرض WDV تحليلي بلا ترحيل — يحافظ على انفصال الحساب/الترحيل الموثق BR-FX-11!).
- Rollback = cancel Asset Depreciation Entries (أثر GL يُلغى آلياً بسطور معكوسة — **يسد أخطر ثغرة UNK-071**).

### F-FX-7: الشهرية = نمط ERPNext الأصلي حرفياً
- "Make Journal Entry for each asset monthly" مع posting date نهاية الشهر = **سلوك Asset Depreciation Borders الأصلي** (schedule_dates = month-end!) — مطابقة 1:1 مع BR-FX-10.

### F-FX-8: البيع/الاستبعاد
- Sales Invoice مع Asset (asset_link) → يولّد: خروج الأصل + Gain/Loss Journal — **بسطور مطابقة لقسم 11 حرفياً**؛ Scrap = Disposal. التساوي → ERPNext يولّد سطرين (لا Gain/Loss) — **E-FX-02 مطابق أصلاً!**

### F-FX-9: توحيد MNT+FXD (أكبر فوز معماري)
- Equipment Master (MNT) تُبنى كلها على **Asset واحد** + Asset Maintenance/Repair للصيانة — يغلق I-FX-09 والتقاطع الصامت ويوحد الكيان المادي.

### F-FX-10: المكوّنات
- Asset Repair بـrepair_cost يزيد القيمة (capitalize repairs) — أقرب نمط؛ أو Stock Entry-into-asset. شبكة Tax = شراء عبر Purchase Receipt/Invoice ثم ربط بالأصل (أصلاً أنظف من FN6i!).

### F-FX-11: التقارير
- Asset Balance · Asset Depreciations Ledger · Asset Sales Register (reports أصلية!) + Fixed Asset List (Zero-Quantity = status filter!) + مخصص: "Unlinked/Rejected posting report".

## 3. ما يُسقط كلياً (لا يستحق بناء)

| مكوّن FN6i | لماذا يسقط |
|---|---|
| FIMSHTBL | naming_series `.{subgroup:5}.{location:3}.####` يغنيه |
| Blue highlight | Validation/tقرير يغني عن الأثر البصري |
| INI #475 | Feature Flag في Company/Asset Settings — لحظة واحد |
| بطاقة الائتمان المؤجلة | Payment Gateway أصلية عند الحاجة |

## 4. الخلاصة

> **أقل مجهود تحويل في المشروع** (~4 أصول مخصصة): FIMSHTBL naming · Component capitalize · تقارير مخصصة (2-3) · فحص تماثل Category Accounts. كل شيء آخر **اصلي بالمنصة** — أنقى من SLM (CRM) وFNB (BOM) لأن ERPNext يملك **تطبيق Assets مكتمل المنهجين**.
