# 06 — تقارير التدقيق (§17.1–17.5) — KOT والفواتير

> خمسة تقارير تدقيق: دفاتر KOT الورقية · تعديلات/حذف KOT · تفاصيل KOT · KOTs بالفاتورة · **تدقيق الفواتير المعاد طباعتها/تسويتها** — الطبقة الجنائية لطبقة تقارير POS.

---

## 1. KOT Books Usage (§17.1) — الدفتر الورقي كأصل

> "This option is to view the usage of KOT books... You can view the usage of KOT Books for **each KOT type separately**."

| البند | القيمة |
|---|---|
| المخرجات | **Starting & ending numbers of the KOTs** · **KOT Book issued date** · **name of the person to whom the KOT was issued** |
| التصنيفات | All / **Used** ("KOTs printed") / **Unused** ("KOTs that are not used") / **VOID** ("KOTs that are made void") — لكل فئة نطاق بداية/نهاية + العدد |
| المدخل | نطاق (≤ Accounting) + Outlet + **KOT Type** |

**الدلالة الجنائية:** أرقام KOT تُدار **كتتاب مسلسل فيزيائي** (Book) يُصدر لشخص بتاريخ — فجوة رقم غير مطبوع = شك حذف. هذا آخر بقايا النموذج الورقي في قلب الوحدة الأكثر رقمنة، ويقابل (ويُسقط الضوء على) **KDS الشبح في §24**: النظام يتحول من دفتر ورقي إلى Kitchen Display System غير موثق.

## 2. KOT Audit (§17.2) — التعديل والحذف بأثر قبل/بعد

> "view all the details of the KOTs that are **modified**... details of items that were **modified or deleted for existing KOTs**."

| البند | القيمة |
|---|---|
| المخرجات | date · session · KOT# · Bill# · **Time** · Server · Table# · الأصناف · **status** · **User name** |
| **عمود status** | "If any items were deleted, the status column shows **delete and the reason for deletion is mentioned**. If the quantity of the items was modified, the status column shows **old and new** and the old and new quantity of the items is displayed under the quantity field." |
| المرشحات | All / **Deleted** / **Modified** |
| قيد تفاعلي | "If you select **All** under Restaurant dropdown list, then you will **not have the option to select the Table number**. This option is available only when you select any particular outlet" — **الجدول مشروط بالمنفذ** (XOR تفاعلي مرئي) |

**الدلالة:** تعديل كمية صنف في KOT مسجل بثنائية old→new + حذف صنف بسبب حرفي — **أغنى سجل تعديل كميات في المشروع** (يضاهي Payroll Audit في HRP-REP بقيم old/new).

## 3. KOT Details (§17.3) — الشكلان

- **Expanded XOR Compressed**: "If you select Expanded, the report will be displayed in **two columns**, and if you select Compressed... in **one column**. **The information will be the same in both the formats**."
- لكل KOT: # · name · qty · rate · bill# · User + إجمالي المنفذ = **Total value + Total Roundoff + Total Taxes** (ثلاثية الإغلاق!).
- Round Off داخل إجمالي KOT — التقريب عنصر هيكلي (يقابل "amounts rounded off to" في 16.3/5.3).

## 4. KOTs by Bill No (§17.4) — الأفقي

> "Note: If there are more than one KOTs per bill, then all such additional KOT details will **appears horizontally** in the report."

- لكل فاتورة: bill# · table# · **كل KOTsها أفقياً** · bill amount · qty/value لكل صنف.
- إجماليات لكل جلسة + الإجمالي العام.
- **الدلالة:** العلاقة Bill→KOT هي **1:N** والعرض المدمج أفقي — تصميم طباعة يحمل معلومة نموذج البيانات (جدول KOT تابع للفاتورة).

## 5. Bill Audit (§17.5) — إعادة الطباعة وإعادة التسوية

> "to view all the bills that are **re-settled and re-printed (Duplicate bills)**... for a given date range (**across months**)."

| البند | القيمة |
|---|---|
| الأنماط | **Re Printed Bill** ("if a duplicated bill request was made") XOR **Re Settled Bill** ("If the **mode of bill payment was changed by the customer**, then the bill settled earlier will be resettled by a new mode of payment") |
| Re Printed | "Amounts of each bill settlement, the **date and time of bills reprinted**" |
| **Re Settled** | "For the resettled bills, the **old mode and amount of settlement and the new mode and amount of settlement**" |
| المدخل | نطاق (≤ Accounting · **across months**) + Outlets |

**الدلالات المعمارية (أغنى اكتشافات الملف):**

1. **إعادة التسوية ظاهرة أولى موثقة**: "re-settled" = تغيير نمط الدفع **بعد** التسوية الأولى — لها تقرير تدقيق مخصص يعرض **الزوج القديم→الجديد كاملاً** (mode+amount معاً).
2. **إعادة الطباعة مُدقّقة بتاريخ ووقت** — كل Duplicate Bill تطلب = حادثة مسجلة (يقابل GAP-GP-D02 في Gate Passes حيث إعادة الطباعة **بلا** تدقيق — التقابل يؤكد أن POS أكثر نضجاً تدقيقياً).
3. عبور الشهور ("across months") — تدقيق يمتد عبر حدود شهرية بينما التقارير التشغيلية محبوسة في الشهر: **قاعدة جديدة: التدقيق أوسع زمنياً من التشغيل**.

## 6. الأنماط العابرة في العائلة

| النمط | الشاهد | التقارير |
|---|---|---|
| **old→new** | كمية KOT · mode+amount التسوية | 17.2 · 17.5 |
| **سبب الحذف** | "the reason for deletion is mentioned" | 17.2 |
| **أثر المستخدم** | User name في كل شيء | 17.2 · 17.3 (و1.15) |
| **Round Off عنصراً هيكلياً** | إجماليات ثلاثية (value+roundoff+taxes) | 17.3 |
| **عبور الشهور للتدقيق** | "across months" | 17.5 (+§9 PAN) |
| **XOR تفاعلي** | Table# يختفي مع All-outlets | 17.2 |
| **عتبات العرض** | أفقية عند تعدد KOT | 17.4 |

## 7. عائلة "تقارير التعديل" عبر المشروع (تحديث الخريطة)

| الوحدة | التقرير | بنية old/new |
|---|---|---|
| **POS-REP** | KOT Audit (17.2) | كمية old/new + سبب الحذف |
| **POS-REP** | **Bill Audit (17.5)** | **mode+amount old→new** — الأول بنية مزدوجة كاملة |
| HRP-REP | Payroll Audit | قيم old/new |
| FO-REP | Room Transfer/Rate Audit ×8 | old/new + المستخدم المخوّل |
| MNT-RPL | Complaint Status (Q) | تعديل حالة تفاعلي |

> POS تضيف النموذج الأكمل (عنصران معاً) وتؤكد الاتجاه العام: **FN6i يسجل التعديلات الموثوقة بثنائية قبل/بعد مع مسؤول** — نمط Versioning جاهز للنقل إلى ERPNext (مقابل F-PR-9).
