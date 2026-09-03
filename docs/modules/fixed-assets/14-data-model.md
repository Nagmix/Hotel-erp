# 14 — نموذج البيانات (Data Model) — وحدة FXD

> **10 كيانات / ~90 حقلاً / 3 جداول أبناء** — هرمية نظيفة بلا تعقيد HRP: ماسترات تصنيف + ماستر مركزي بشبكتي أبناء (Tax/Component) + معاملتان + جدولا ذاكرة (Calc/Post) + جدول تسلسل مسرب الاسم (FIMSHTBL).

---

## 1. مخطط الكيانات (ERD نصي)

```
Property ──< AssetMainGroup (بلا property! وأقسام movable/immovable)
Property ──< AssetSubGroup >── AssetMainGroup
AssetSubGroup >── COA: BS_D depr + BS_S/L + PL_D depr + PL_S/L + CostCenter  [ربط ررباعي اختياري]
Property ──< AssetLocation (بلا property)
             AssetComponent (بلا property — ماستر شفرات)
Property ──< FixedAssetMaster >── AssetSubGroup + AssetLocation + Currency + Supplier[?]
                ├──< AssetTaxLine        (TaxCode, Currency, Amount)         [ضمن القيمة]
                ├──< AssetComponentLine  (ComponentCode, Currency, Amount)   [خارج القيمة]
                └──< CurrentClosing      (QtyBalance, NBV, TotalDepn — آلي)
Property × FY × SubGroup/Asset ──< DepreciationMethod (SLM%, WDM%)
Property × FY × Asset ──< FAComponentEntry (Date, ComponentCode, Currency, Amount) → يزيد قيمة الأصل
Property × FY × Asset ──< FATransaction (Type: Sale/Disposal, Date, Qty, Currency, PayMode, SaleAmount, GainLoss, NBV)
Property × MMYY ──< DepreciationCalc (لكل أصل — قابل للRollback) → DepHistory
Property × MMYY ──< FIDeprPosting (TransactionType, PostDate=نهاية الشهر — SLM/SubGroup) → FAS
FIMSHTBL (مسلسل 4 أرقام لكل توليفة SubGroup×Location)
FixedAssetStart (Property, StartMMYY — singleton مقفل)
```

## 2. جرد الكيانات والحقول

| الكيان | الحقول الأساسية (الأطوال) | مفاتيح/علاقات |
|---|---|---|
| **FixedAssetStart** | Property · StartDate(MMYY) · User · LastUpdated | PK: Property · **مقفل بعد الحفظ** |
| **AssetMainGroup** | MainGroup(code) · LongName(30) · ShortName(10) · Status · User · LastUpdated | code غير قابل للتعديل |
| **AssetSubGroup** | Property · GroupCode · LongName(30)/Short(10) · MainGroup · **BSDeprAc, BSDeprSL, PLDeprAc, PLDeprSL (COA+SubLedger)** · CostCenter | **validation تماثلي** · PK مركب |
| **AssetLocation** | LocationCode · Long(30)/Short(10) · Status · User/LastUpdated | Short Name للاستعلامات/التقارير |
| **AssetComponent** | ComponentCode · Long(30)/Short(10) · Status | مشترك بين أصول |
| **FixedAssetMaster** | Property · SubGroupCode(5) · Location · **AssetCode(12 آلي)** · LongName(70) · ShortName(10) · Manufacturer(60) · DateInstallation · Currency · Rate · Quantity · UMO · ItemPrice/Qty · **TotalValue(آلي)** · ResidualValue/Qty · **DepnOpBal** · LifeSpan+UOM(year/month) · PO#/PODate/Grr#/GrrDate/Bill#/BillDate · SupplierCode · Remarks · AssetInsurer · AssetMaintenance · AssetStatus · StartDateDepn · **LastDateDepn(RO)** | الكود: 5+3+4 من FIMSHTBL |
| AssetTaxLine | TaxCode · Currency · Amount | ابن Master (ضمن) |
| AssetComponentLine | ComponentCode · Currency · Amount | ابن Master (خارج!) |
| **DepreciationMethod** | Property · FY · SubGroup أو AssetCode · SLM% · WDM% | نِسب ثنائية دائمة |
| **FAComponentEntry** | Property · FY · AssetCode · Date · ComponentCode · Currency · ExchangeRate · Amount(→Exchange آلي) | **يزيد AssetValue** |
| **FATransaction** | Property · FY · AssetCode · Type(Sale/Disposal) · Date · Quantity · Currency · Rate · PayMode(Bank/Cash) · SaleAmount · **LocalAmount(آلي)** · **AssetValue(آلي)** · **NBV(آلي)** · **GainLoss(آلي)** · OriginalQty/SoldQty/DisposedQty/BalanceQty · Remarks | يفتح FA Posting عند الربط |
| DepreciationCalc/History | Property · AssetCode · FY · Month · Amount(بالمنهج المعتمد INI#475) · Method | **Rollback متاح** |
| FIDeprPosting | Property · TransactionType · MMYY · FY · **LastDepPostDate** · **LastDepCalcDate** · GroupBy | قيود FAS شهرية |
| FIMSHTBL | (SubGroup+Location → Serial) | **تسريب اسم الجدول** |

## 3. قواعد التكامل المرجعي (عبر FK مفترضة)

| المرجع | إلى | سلوك الغياب |
|---|---|---|
| COA (BS/PL) | FAS | الترحيل يُستثنى (أزرق) |
| Financial Year | FAS FY Parameter | F3 حصرياً |
| Currency/Rate | SYS | "local currency" افتراضي |
| Supplier | [مصدر غير محسوم] | F1 فقط |
| Tax Code | نظام الضرائب العام | F1 |
| UMO | ماستر الوحدات العام | F1 |

## 4. أسرار البيانات الموثقة

| السر | الشاهد |
|---|---|
| **FIMSHTBL** | اسم جدول المسلسل مقروء حرفياً — نادر جداً (مع INI switch numbering) |
| Right-hand auto-amount | "Exchange amount will be displayed in **right hand side** automatically" — تلميح تخطيطي شاشة |
| Current closing details | حقول NBV/QtyBalance/TotalDepn **آلية عرض** في Master — تجميع لحظي من جداول الحركة |
| **لا تاریخ انتهاء (Applicable From)** | كل الماسترات خالدة زمنياً (عائلة HRP/MEM/BNQ/TEL) — لا إصدارية |
| تعديل القيمة الحرة | ItemPrice وQuantity قابلة للتعديل اليدوي — لا سجل تعديل أسعار (Version) |
| Current closing / DepHistory كتجميعين متوازيين | نفس المعلومة لحظية (Master) وتاريخية (History) — جدولان لشيء واحد |
