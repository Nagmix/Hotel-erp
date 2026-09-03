# 11 — الأثر المحاسبي (Accounting Impact) — وحدة FXD

> **الوحدة الوحيدة في المشروع (بعد FAS ذاتها) بمسار ترحيل GL موجب كامل وموثق بالحسابات**: ربط رباعي لكل Sub Group (BS×2 + PL×2 + Cost Center)، ترحيل إهلاك شهري بتاريخ نهاية الشهر بمنهج SLM حصراً، وقيود بيع/استبعاد ثلاثية الأرجل (Asset ledger + Cash/Bank + P&L Gain/Loss) — **البند F12 من خريطة الترحيل المسجلة منذ Phase 0**.

---

## 1. الإعلان التأسيسي (النص الحرفي)

> "Asset details **integrate directly with Ledger Accounting**, so when depreciation is posted for an asset, the relevant **profit & loss and balance sheet accounts are updated**." (ص2)

> "If asset group linked to chart of account, then those assets transaction **will be posted to financial module also**." (ص5) — **الشرط الجامع**: لا ربط → لا ترحيل (والاستثناء يُبرز أزرق).

## 2. خريطة حسابات الوحدة (الربط الرباعي)

| الحساب (من Sub Group) | الطرف المحاسبي | يستقبل |
|---|---|---|
| **BS Depr. A/c + BS Depr S/L** | الميزانية (الالتزام/المجمع مقابل الأصل) | ترحيل الإهلاك الشهري |
| **PL Depr. A/C + PL Depr S/L** | الأرباح والخسائر (المصروف) | ترحيل الإهلاك الشهري |
| **Cost center / department** | البعد التحليلي | تصنيف كل قيد |
| (عند البيع) accumulated posting ledger | مجمع إهلاك الأصل | إطفاء قيمة الأصل المباع |
| (عند البيع) Cash أو **Bank account** | الأصول المتداولة | **مبلغ البيع credit/debit حسب الاتجاه** |
| (عند البيع) P&L ledger **حسب Gain/Loss** | نتيجة بيع الأصل | فرق البيع عن القيمة |

> عمق 'sub ledger': "Chart of account with account type '**sub ledger**', will allow to select the sub ledger" — ربط ثنائي المستوى (حساب + سجل فرعي) كعائلة FO.

## 3. قيود الإهلاك الشهرية (الدورة الاعتيادية)

```
شهرياً (FI Depr Posting to FA):
   [Load] → استثناء غير المربوط (أزرق)
   [Save] → لكل Sub Group:
        Debit:  PL Depr A/C (مصروف إهلاك الفترة)
        Credit: BS Depr A/c (مجمع الإهلاك)
   بتاريخ: **نهاية الشهر** — "posting date will be month's end date"
   بمنهج: **SLM فقط** — "straight line method of depreciation only"
   بتجميع: **Sub group wise** — "per sub group wise only"
```

**اللحظة المحاسبية الحرجة:** WDV يُحسب (Calculate) ولا يُرحَّل — إذا كان الفندق يعتمد WDV (INI #475) فالدفاتر ترى إهلاك SLM بينما التقارير الداخلية ترى WDV — **انفصال دفاتر/تحليل موثق بنيوياً** (راجع 13/17).

## 4. قيود البيع/الاستبعاد

```
Sale (الربط موجود):
        Debit:  Cash/Bank            (مبلغ البيع)
        Credit: Accumulated Asset ledger   (قيمة الأصل — "accumulated description posting ledger")
        [Gain]  Credit: P&L (Gain) ledger   — إذا Sale > Asset Value
        [Loss]  Debit:  P&L (Loss) ledger   — إذا Sale < Asset Value
        [Equal] ← لا سطر P&L أصلاً — "profit and loss ledger selection will be deactivated"

Disposal: نفس المسار بلا مبلغ بيع (أو مبلغ صفري؟) — [NOT DOCUMENTED] أثر قيمة الأصل المطفاة كاملاً (خسارة استبعاد؟)
```

**قاعدة Gain/Loss الحرفية:** "If the Sale amount is greater than the Asset value, then it would result in a **Profit** and if the Sale Amount is lesser than the Asset value, then it would result in a **Loss**." (ص14)

## 5. ما لا يُرحَّل (خريطة السلبية)

| العنصر | الحالة |
|---|---|
| إنشاء الأصل | سجل داخلي فقط (الشراء يُقيد يدوياً في FAS من الأصل النقدي عبر PO/Bill — FXD لا تولّد قيد شراء!) |
| إضافة مكوّن | تزيد القيمة داخلياً بلا قيد موثق |
| Rollback الحساب | أثره على قيود مرسلة سابقاً؟ **غير موثق إطلاقاً** — أخطر ثغرة محاسبية في الوحدة (UNK-071) |
| ضرائب الشراء (Tax grid) | تُخزن — أثر GST/VAT غير موثق |
| Depn. Op. Bal | رصيد موروث — يُستهلك حسابياً (قيد افتتاحي يُدخل في FAS يدوياً بالأصل) |
| Credit card pay mode | "provided later" — بلا قيد أصلاً |

## 6. التقييد المحاسبي عبر الوحدات

| مقارنة | الوحدة |
|---|---|
| قيود موجبة كاملة | **FAS (نفسها) + FXD** فقط |
| قيود عبر 4 حسابات مرة واحدة | FXD فريدة (ربط رباعي) |
| تاريخ ترحيل مفروض (نهاية الشهر) | FXD فريدة |
| منهج ترحيل مفروض (SLM) | FXD فريدة |
| Gain/Loss آلي بسطور تتشكل | FXD + (BNQ/POS عند التسويات — لكن هناك بالمستخدم) |

> **قرار D-FX-3:** عند إعادة البناء بـERPNext: journalEntry للإهلاك يُولَّد من Asset Depreciation Schedule (شهري/نهاية الشهر) والبيع عبر **Sales Invoice للAsset** (يولّد Gain/Losis Journal آلياً) — راجع 16.
