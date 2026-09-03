# 04 — عائلة طباعة المستندات (Print Family) — MGT-REP §15 (Phase 7)

> 15.1–15.7 = **7 مستندات تُطبع** — أكبر عائلة طباعة مستندات في الحزمة + القانون المعماري الأهم في الوحدة (Print Forms عبر FAS).

---

## 1. قانون Print Forms (المشترك الحاكم لـ15.3/15.4/15.6)

النص الحرفي (يتكرر بصيغ شبه موحدة 3 مرات):

> "To print the Purchase Order [Standing PO / GRN], **the name of the Purchase Order print program has to be specified in the Print Forms parameter under the Financial Management module**. The definition of the program name is mandatory for printing the [PO/SPO/GRN] as **customized programs are developed for each client** as per their specifications to print either on **pre-printed or plain continuous or cut stationery**."

| البند | التفصيل | المصدر |
|---|---|---|
| أين يُعرَّف اسم البرنامج؟ | **FAS → Setup → Print Forms (SET §15 — "To set Pgm.ID for Print Forms")** | FAS-SET ص1051-1069 + REP 15.3/15.4/15.6 |
| هل هو اختياري؟ | **إلزامي** — "mandatory for printing" — بلا تسجيل لا طباعة | REP حرفياً |
| طبيعة برامج الطباعة | **مخصصة لكل عميل** (customized per client) | REP حرفياً |
| الورق المدعوم | **ثلاثية**: pre-printed (نموذج مطبوع سلفاً) · plain continuous (ورق متصل) · cut (ورق مقطوع) | REP حرفياً |
| أين User Defined Print Forms؟ | **مصدر آخر مختلف**: MGT-SET §28 / FAS-SET §16 — يحيلان إلى Getting Started (خارج الحزمة — GAP-SYS-D02) | SET كلا الوحدتين |

**التمييز الحاسم (يمنع الالتباس):**
- **Print Forms (FAS-SET §15)**: سجل **Pgm.ID** — برامج مخصصة مكتوبة لكل عميل — يستهلكها MGT-REP (15.3/15.4/15.6).
- **User Defined Print Forms (SET §28 في MGT و§16 في FAS)**: **تخصيص من الواجهة** ("customize the format of bills, vouchers, slips... column width, page properties") — يحيل إلى دليل Getting Started غير المتوفر.
- الطبقتان متجاورتان رقمياً في FAS-SET (§15→§16) — ثنائية "كود مخصص / تخصيص مستخدم" موثقة لأول مرة بوضوح.

**الأثر المعماري الشامل:** غياب تخطيطات المطبوعات في الحزمة كلها لم يعد غياب توثيق فحسب — إنه **تصميم منتج**: الشكل النهائي للمستند = دالة في (برنامج الطباعة المسجل لكل عميل + نوع الورق) — لا يمكن توثيته مركزياً لأنه يختلف بين التثبيتات.

## 2. §15.1 Print Purchase Requisition

- **مفتاحان**: Date range **أو** DPR# range — (ثنائية استرجاع).
- Department من قائمة.
- **Printer من pre-defined list** (ص81) — قائمة طابعات معرفة سلفاً (UNK-093).
- يقابل DNT §1: PR له ثلاث إصدارات إلكترونية ("Print/Email/**Print and Mail**") — REP-15.1 هو الوجه الورقي الصريح.

## 3. §15.2 Print Indent — المستند ذو التنسيقين

**الوصف الحرفي:** "Indent received from stores are printed here for reference purpose. Indents can be generated based on the **Indent Format or Contract Format**. **If the Indent Format is selected, by default, the Print Indent will be processed through Cost Center wise**."

**المعايير (ص81-82):**

| # | المعيار |
|---|---|
| 1 | **Indent Format / Contract Format** |
| 2 | From/To date |
| 3 | **Cost Center / Sub Store** |
| 4 | **Authorization choice** (من قائمة — مستويات التفويض!) |
| 5 | Cost Center + Detail option |
| 6 | Value to be printed · 1-line space · item summary |

**النقاط البنيوية:**
- **تنسيقان لمستند واحد**: Indent Format (تشغيلي داخلي — افتراضياً عبر مراكز التكلفة) مقابل **Contract Format** (نسخة تعاقدية — الطلب يُصاغ بلغة العقد/الأسعار التعاقدية) — المستند الواحد بوجهين لجمهورين (مخزن داخلي / مورد متعاقد).
- **Authorization choice** — طباعة حسب مستوى التفويض — أول تقرير يوثق معيار تفويض في MGT (يقابل منظومة التفويض LUK "Authorization Details").
- خيارات تنسيق دقيقة: قيمة مطبوعة؟ سطر فارغ بين البنود؟ ملخص الصنف؟ — تحكم Layout حبيبي.

## 4. §15.3 Print Purchase Order

- **ثلاثية تسلسل**: Date / PO# / **Vendor Sequence** + النطاق.
- **Discount Summary + Tax Summary** — خيارا تضمين ملخصي الخصم والضريبة (فاتورة PO بملحقاتها المالية).
- Printer selection.
- **محكوم بقانون Print Forms** (§1 أعلاه).
- الفاتورة الشرائية بملخصي Discount/Tax = مستند تجاري كامل الأركان (ليس مجرد قائمة أصناف).

## 5. §15.4 Print Standing PO

- نفس ثلاثية التسلسل (Date / Standing PO / Vendor) + Printer + **نفس القانون الحرفي** لPrint Forms.
- Standing PO = التعهد اليومي (متكرر البنود للتعهدات اليومية) — مطبوعه جزء من دورة المواد سريعة التلف (يقفل الدائرة مع §10 Supplier Bill: "daily and contracted items normally perishables").

## 6. §15.5 Print Service Work Order

- "raised for all or specified Departments" — أمر الخدمة (خدمات لا أصناف) — أقرب جسر مستندي إلى MNT (Service Work Order كنوع) وSLM.
- ص87-88: "Select appropriate options from relevant fields based on your selection criteria and click [Print]" — أفق عام (بلا تفصيل معايير — الوصف الأضعف في العائلة).

## 7. §15.6 Print GRN — المستند العابر للوحدات

**الوصف الحرفي:** "you can print **on-line printing of Goods Receipt Notes (GRN)**, normally used to **issue an acknowledgement to the Vendor** for goods received, and to **forward a copy to the Finance department for making payments accordingly**."

**تفكيك الدورة المستندية:**
1. **GRN = إيصال استلام** يُسلَّم للمورد (Acknowledgement) — الوجه التجاري.
2. **نسخة إلى المالية** "لإجراء الدفعات وفقاً له" — الوجه المحاسبي — **المستند الورقي الحامل لعبور MGT→FAS** (المسار المادي للمعلومات قبل أي ترحيل إلكتروني).
3. **محكوم بقانون Print Forms** — برنامج GRN Print مسجل في FAS.
4. "on-line printing" — طباعة فورية (من شاشة المعاملة على الأرجح — لا دفعية).

**الجسر الكامل للمستند (من الطبقة والمصادر الأخرى):**

| المرحلة | الأداة | المصدر |
|---|---|---|
| استلام | GRN entry (Transactions) | MGT-TRN |
| طباعة الإيصال + نسخة المالية | **15.6 Print GRN** (Print Forms عبر FAS) | MGT-REP |
| تسجيل ضرائب الاستلام | VAT on receipts → 24.1 VAT Report | MGT-REP |
| التحقق من فاتورة المورد | §10 Supplier Bill | MGT-REP |
| الدفع | PJV (Purchase Journal Voucher) — Pending Receipts for PJV | FAS-REP §18 |

## 8. §15.7 Print Transactions

- **أنواع المعاملات القابلة للطباعة** (حرفياً): "Issue Indent **Issue Direct**, Issue Return, Adjustment or Receipt Return" — خمسة أنواع.
- لكل منها: Store + Date range.
- **ليس Receipt!** — الاستلام له GRN مستقله (15.6) — التقسيم المنهجي: المستند المالي الكبير (GRN) منفصل عن معاملات المخزن اليومية (الإصدار/المرتجع/التسوية).
- "Issue Indent Issue Direct" بلا فاصلة في الأصل — ثنائية الإصدار (بطلب/مباشر) ملتصقة نصياً — إسقاط تحريري ثانوي.

## 9. جدول العائلة

| # | المستند | المفتاح | خاصية مميزة | Print Forms؟ |
|---|---|---|---|---|
| 15.1 | PR | Date/DPR# | Department + Printer list | لا |
| 15.2 | Indent | **تنسيقان** | **Authorization choice** + CC/Sub Store | لا |
| 15.3 | PO | Date/PO#/Vendor | **Discount/Tax Summary** | **نعم (إلزامي)** |
| 15.4 | Standing PO | Date/SPO/Vendor | دورة المواد اليومية | **نعم (إلزامي)** |
| 15.5 | SWO | Department | أضعف توثيقاً | لا |
| 15.6 | GRN | Receipt | **نسخة إلى Finance + Acknowledgement للمورد** | **نعم (إلزامي)** |
| 15.7 | Transactions | 5 أنواع | **بلا Receipt** (له 15.6) | لا |

**الملاحظة الختامية:** ثلاثة فقط من السبعة (PO/SPO/GRN) محكومة بقانون Print Forms — **المستندات ذات الأثر المالي الخارجي** (تصل للمورد/المالية) تحتاج برامج مخصصة، بينما مستندات التداول الداخلي (PR/Indent/SWO/Transactions) تطبع بالشكل القياسي — **حدود التخصيص = حدود العبور المؤسسي للمستند**.
