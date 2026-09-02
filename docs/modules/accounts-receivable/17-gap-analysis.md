# 17 — تحليل الفجوات (Gap Analysis) — وحدة ACR

> فئتان: **D = فجوات توثيق المصدر** (نقص في أدلة IDS نفسها) و**E = فجوات ERPNext** (ما لا يغطيه الهدف بدون تطوير).

---

## أ. فجوات توثيق المصدر (D)

| ID | الفجوة | الدليل | الأثر | المعالجة المقترحة |
|---|---|---|---|---|
| **GAP-AR-D01** | التقرير 13 في ACR-RPL بعنوان **"12123 PENDING"** — عنصر نائب بلا متن | ACR-RPL ص21 | تقرير غير معروف الوظيفة من أصل 23 | `[NOT DOCUMENTED]` — يُترك معلقاً؛ إن ظهر في التقارير الحية يُوثق ميدانياً |
| **GAP-AR-D02** | **User Defined Print Forms** و**Print Form Designer** يحيلان لـ"Getting Started document" — **ليس ضمن حزمة الـ65** | ACR-SET §6 ص17 + §8 ص19 | بنية تعريف نماذج الطباعة غير معروفة من الحزمة | الاكتفاء بمعرفة الوظيفة (أشكال: invoices/reminders/receipts/confirmation) — التفاصيل من Print Format Builder في الهدف |
| **GAP-AR-D03** | لا توثيق لسلوك **Black List** التشغيلي (هل يمنع التسوية الائتمانية؟) | ACR-SET §5 ص12 | سلوك وصم غير محدد | `[NOT DOCUMENTED]` — افتراض منع الائتمان (الأرجح وظيفياً) يُتحقق عند التنفيذ |
| **GAP-AR-D04** | **صلاحيات العمليات الخطرة**: Rollback SOA وCancel Invoice بلا تقييد موثق | ACR-OPR §8 + ACR-BIL §2 | خطر إجرائي غير مؤمَّن | في الهدف: أدوار صريحة (قرار معماري) |
| **GAP-AR-D05** | تحقق **Adjusted > Outstanding** في المطابقة غير موثق | ACR-OPR §2 ص11 | ثغرة إدخال محتملة | التحقق مطلوب في الهدف إلزاماً |
| **GAP-AR-D06** | تفاعل **SOA (AR) ↔ Audited (FAS)** لقفل الشهر نفسه | ACR-OPR §7 + FAS-SET §18 | ترتيب إقفال غير محدد | قرار معماري (E-AR-17) |
| **GAP-AR-D07** | هل **Outstanding Update** يترك أثراً في Audit؟ (تصحيح بعد SOA دون Rollback) | ACR-OPR §5 | ازدواج مسارات تصحيح | Versioning إلزامي في الهدف |
| **GAP-AR-D08** | **"Fortune Enterprise 2.0"** تُذكر في ACR-RPL §11 كعائلة النظام — أثر تسمية قديمة | ACR-RPL ص20 | دلالة نَسَب فقط | توثيق تاريخي (لا أثر وظيفي) |
| **GAP-AR-D09** | سلوك **NDE** للفائدة: Aging with Interest لا يوثّق ترحيلها | ACR-SET §3 ص9 | فائدة حسابية بلا قيد | F-AR-4 (Dunning) |
| **GAP-AR-D10** | نطاق **AR User Access للعرض** (وليس الإدخال) وشمولها Property | ACR-SET §4 | غموض صلاحيات | توضيح تصميمي في الهدف |

## ب. فجوات ERPNext (E)

| ID | الفجوة | لماذا لا يغطيها ERPNext القياسي | المعالجة |
|---|---|---|---|
| **GAP-AR-E01** | **Debtors Follow-Up** (متابعة/تعيين/موعد/Projection/Trace) | لا DocType "مطاردة ديون" ميدانية (Dunning محاسبية فقط) | Custom App: DocType `Debt Follow-Up` + لوحة + تقرير Projection |
| **GAP-AR-E02** | **فترات Aging مرنة + فائدة لكل فترة + Print Text** | تقادم ERPNext قياسي ثابت (0-30/31-60/61-90/91-120) في AR Summary | Query Report مخصص + حقول تعريف Period |
| **GAP-AR-E03** | **CC Consolidation groups** + خطاب تغطية بـ Charge Slips | لا تجميع عرضي لفواتير شركة بطاقة | تقرير/إجراء مخصص |
| **GAP-AR-E04** | **Cheque Deposit Statement** بديل نماذج الإيداع (Local/Outstation + 3 تلخيصات) | Bank Deposit قريب لكن مختلف الشكل | تقرير مخصص |
| **GAP-AR-E05** | **ارتباط Workhorse متعدد المنافذ**: تلقي فواتير من FO/POS/BQT/MEM مع عارض مصدر | تحقق عبر تكاملات الوحدات نفسها (المرحلة 10) | روابط الوحدات + source_doc |
| **GAP-AR-E06** | **سعر صرف الفاتورة يثبَّت للسداد** (منع Book P/L) | ERPNext يعيد التقييم بالسعر الجاري في بعض المسارات | سياسة صرف صريحة + اختبار |
| **GAP-AR-E07** | **INI معكوسة/Module Attributes** → feature flags مركزية | إدارة ميزات موحدة | System Settings مخصصة بدلالات إيجابية |
| **GAP-AR-E08** | **صلاحية "Post"** (online bill-wise posting) كمستوى granular | صلاحيات ERPNext على مستوى doctype/submit | role فرعية + أذونات مخصصة |
| **GAP-AR-E09** | **متعددية Property داخل قيد واحد** (property حقل في كل AR Transaction) | يُحل بـ Dimension + Company (UNK-004) | القرار المعماري الأب |
| **GAP-AR-E10** | **"12123"** — تقرير مفقود المصدر | لا مقابل | لا إجراء (معلق) |

## ج. فجوات عكسية (ميزات ERPNext تفوق الأصل — فرص)

| الميزة | الأصل | الربح |
|---|---|---|
| Versioning تلقائي لكل تعديل | Attr#3 اختياري (قد يُفقد Audit) | أمان بيانات أعلى |
| إلغاء/تعديل بآلية cancel/re-submit قياسية | سلسلة فتح ثلاثية يدوية | بساطة تشغيلية |
| Dunning بمستندات متابعة | فائدة حسابية بلا مستند | قيمة تحصيل أعلى |
| Payment Reconciliation Tool | Match/Untag يدوي محدود | مطابقة أسرع |
| تخصيص تلقائي Multi-currency محكم | قاعدة سعر الفاتورة يدوية المنطق | اتساق أصلي |
