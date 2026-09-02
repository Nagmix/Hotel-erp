# 17 — تحليل الفجوات (Gap Analysis) — وحدة FAS

## 1. فجوات التوثيق (Documentation Gaps)

| ID | الفجوة | الحالة | المصدر المتوقع |
|---|---|---|---|
| G-FA-01 | قيود Tips (QA-4) | `[NOT DOCUMENTED]` في FAS | POS/AR |
| G-FA-02 | معالجة Complimentary محاسبياً (QA-5) | `[NOT DOCUMENTED]` | — |
| G-FA-03 | تفاصيل تنسيق Audit Code (المرافق في بنود Post FO) | مذكور بلا تعريف بنية | FAS-REP/AR |
| G-FA-04 | جدول أنواع TDS Section الكامل | dropdown بلا قائمة | SYS-SSP |
| G-FA-05 | تفاصيل Voucher Authorization الثلاثة مستويات (صلاحيات كل مستوى) | مستويات مذكورة بلا تفصيل | `[NOT DOCUMENTED]` |
| G-FA-06 | سلوك re-process الكامل (هل يُعكس القيد السابق آلياً أم يُرافق؟) | "re-process" موثق؛ آلية العكس `[NOT DOCUMENTED]` | — |
| G-FA-07 | تكامل Banquets التفصيلي (غير نوع Taxes) | غير موثق في المقروء | BQT |
| G-FA-08 | FAS-REP كامل | مؤجل Phase 7 | FAS-REP |

## 2. فجوات ERPNext (Mapping Gaps)

| ID | الفجوة | درجة الخطورة | المعالجة المقترحة |
|---|---|---|---|
| GE-FA-01 | آلية undistributed→Suspense + re-process | عالية | بناء تحقق مسبق + تقرير إعداد غير مربوط قبل الترحيل (أفضل من الأصل) |
| GE-FA-02 | قواعد Book Types التسع | متوسطة | validations مخصصة على Journal/Payment Entry |
| GE-FA-03 | قفل Audited الشهري | متوسطة | Period Closing شهري + صلاحيات |
| GE-FA-04 | Sub Ledger بحسابات متعددة | متوسطة | قرار: شجرة حسابات أم Party model |
| GE-FA-05 | 9 أيام دفع Fixed للمورد | منخفضة | Payment Schedule مخصص |
| GE-FA-06 | Transaction Limit البنكي اليومي للمورد | منخفضة | تحقق إضافي |
| GE-FA-07 | مصمم التقارير العميق (Groups/Formula/Report Linking) | عالية للتكافؤ | Query Reports + Frappe framework |
| GE-FA-08 | ترقيم مستندات بدورية Restart Number | منخفضة | naming_series + hook |

## 3. قرارات معمارية مفتوحة (تُحسم في Phase 13)

1. **ترحيل FO/POS مجمّع يومي** (كما FortuneNext حرفياً) أم **فواتير تفصيلية** مع تقرير مجمّع؟ — يؤثر على: الأداء، التدقيق التفصيلي، عمق drill-down.
2. **مصير دفتر الضيوف (Guest Ledger B/F-C/F):** تمثيله كحساب سيطرة مع إقفال يومي (كما الأصل) أم نموذج ERPNext الفواتير؟
3. **نموذج Sub Ledger:** شجرة حسابات ثنائية أم Party (Customer/Supplier) — الأقرب لسلوك "Control Account → SL إلزامي".
