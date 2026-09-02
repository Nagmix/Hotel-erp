# 09 — الاستعلامات (Lookups) — وحدة FAS

> FAS-LUK كاملة (9 وظائف) — قراءة عميقة الجلسة 3.

| # | الاستعلام | التدفق والخصائص الموثقة | المصدر |
|---|---|---|---|
| 1 | **Ledger Balance** | **F3 = قائمة السنوات المالية** → Account Code + Sub Ledger (إن وجد) → Load → Double-click السجل → كل المعاملات المطابقة بالنarration | §1 ص2-3 |
| 2 | **Day Book (Q)** ⭐ | F3 السنة → A/C Name (F1؛ مع SL) + Currency → Load → **أرصدة شهرية** → Double-click شهر → **تفصيل يومي (+إجماليات)** → Double-click سجل → **Transaction Entry** → **تعديل مباشر** (Update → Confirm → Save → رسالة → Ok) | §2 ص3-4 |
| 3 | **Trial Balance** | F3 السنة + نطاق تاريخ → Main Head → Sub Head (drill-down)؛ **Modify Column** (Property+نطاق → مواصفات العمود) | §3 ص4-6 |
| 4 | **Profit and Loss** | مثل TB؛ drill ثلاثي المستويات؛ Modify Column | §4 |
| 5 | **Balance Sheet** | مثل TB؛ Modify Column | §5 |
| 6 | **Payable Outstanding** | FY + Account (أو All/نطاق موردين) → Load → إجمالي المورد → **Double-click → فواتيره** (bill no/date/amount/payment/balance/**aging**) → drill للمعاملة والقسيمة | §6 ص6-7 |
| 7 | **Chart of Accounts List** | عرض **group wise** → Double-click → **تعديل أونلاين**: Group code + Name + Currency + Cash Flow Group + Restrict Journal + Stop Posting → Save (**ممنوع إذا عليه معاملات**) | §7 ص7 |
| 8 | **Cash Flow Query** | "inflow and outflow of cash between two Balance Sheet dates" (Cash = نقدي+بنك) → drill **شهري أو برقم القسيمة**؛ تفاصيل Main/Sub Head؛ **أعمدة قابلة للإضافة/التعديل/الحذف/التنظيم** | §8 ص8 |
| 9 | **Transaction Search** | FY (Enter) → **Search Records**: حقل + مقارنة + قيمة (معايير متعددة) → OK → النتائج مع **Grand Total**؛ **Ctrl+F** بحث سريع (المطابق يظهر **بنفسجي**) → Double-click تفاصيل؛ drill حتى Transaction Entry لغير المرحّل آلياً | §9 ص8-9 |

**ملاحظات UX موثقة:**
- F3 للسنوات المالية (نمط موازٍ لـ F1 للمasters).
- تدرّج drill-down موحد: تقرير → سجل → معاملة → قيد (حتى التعديل!).
- التعديل عبر Day Book وTransaction Search — **استعلام يفتح الإدخال** (نمط تصميمي مهم).
