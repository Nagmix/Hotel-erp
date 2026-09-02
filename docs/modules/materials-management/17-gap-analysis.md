# 17 — تحليل الفجوات (Gap Analysis) — وحدة Materials Management

> **فئة A: فجوات المصدر** (نواقص توثيق الأصل) · **فئة B: فجوات ERPNext** (فوارق المنصة المستهدفة).

---

## أولاً: فجوات المصدر (Source Gaps) — GAP-MG-D01..D12

| # | الفجوة | الدليل | الأثر | المعالجة |
|---|---|---|---|---|
| GAP-MG-D01 | **تعارض ترقيم مفتاح SPO/Direct** | §4: "To activate SPO, **Switch #8**" ثم نفس الفقرة: "set tag against **Serial No. 5** 'In Receipt / PO Indent is not mandatory'"؛ و§6: "The Module Attribute **# 5** 'In Receipt / PO Indent is not mandatory'" | لا يمكن الجزم برقم المفتاح (5 أم 8) ولا هل هما مفتاح واحد بوظيفتين أم مفتاحان | توثيق بالاسم النصي؛ يُحسم عند توفر وثيقة Attributes (GAP-SYS-D01) |
| GAP-MG-D02 | **منطق Stop Payment معكوس التسمية** | "select NO... to stop... Unless you change to YES, the system will not allow payments" | التسمية (Stop) تناقض السلوك الظاهر (NO=منع!) | [UNCERTAIN] تسجيل حرفي + قرار تسمية عربية صريحة في الجديد ("السماح بالسداد") |
| GAP-MG-D03 | **بلا نصوص رسائل خطأ** | كل المنع موثق بالقواعد فقط | UX عربي يحتاج نصوصاً | تأليف عربي قياسي (Phase 4) |
| GAP-MG-D04 | **توقيت الترحيل MM→FAS غير موثق** | رابط الترحيل موثق (SET §16) دون توقيت (فوري/دفعة/شهري) | قرار معماري معلق | Phase 6 — أنماط FO/POS (دفعة) مقابل AR (فوري) تحتاج الفصل |
| GAP-MG-D05 | **وصف ECC No مقطوع** | جدول Other Details: حقل ECC يظهر مباشرة بعد سطر "Enter the Personal details..." | حقل بلا وصف | [UNCERTAIN] ECC=Excise Control Code استنتاج سياقي |
| GAP-MG-D06 | **تفويض PO بلا قيد تسلسل موثق** | §3 يذكر Auth 1/2/3 بلا قيد "1 قبل 2" (الموثق للـ PR فقط) | هل PO أيضاً تسلسلي؟ | إفتراض التسلسل [INFERENCE من نمط PR الموثق] |
| GAP-MG-D07 | **صور مفقودة في الاستخراج النصي** | شاشات النتائج بلا محتوى نصي (Screenshots only) | حدود أعمدة النتائج غير معروفة | إن ذُكرت أعمدة نصاً وُثقت؛ وإلا [NOT DOCUMENTED] |
| GAP-MG-D08 | **آلية فوائد التأخير الحسابية** | Vendor Master يوثق الشرائح مفهوماً ("91st to 100th day → 10%") | هل تُحسب آلياً في FAS؟ لا ذكر | Phase 6/11 |
| GAP-MG-D09 | **Vendor "مقيد المورد مقابل"** | لا قيد موثق يمنع PO على مورد Black Listed | [INFERENCE: منع متوقع] | تحقق في POS/FO المشابه — موثق FO Credit Limit حاجب؛ هنا [NOT DOCUMENTED] |
| GAP-MG-D10 | **REP كامل غير مقروء** | 112 ص مؤجلة (بروتوكول) | قوائم التقارير الكاملة | المرحلة 7 |
| GAP-MG-D11 | **مصير Complimentary في الدفاتر** | "Rate Plan and Tax Structure will not be applicable" | هل القيمة صفر في GL؟ | [NOT DOCUMENTED] — Phase 6 |
| GAP-MG-D12 | **لا وصف لسلوك "Deleted" Indent** | LUK يذكر حالة Deleted للـ Indent — لا وظيفة Delete موثقة في DNT | قناة حذف غامضة | [UNCERTAIN] — غالباً Purging |

## ثانياً: فجوات ERPNext (Platform Gaps) — GAP-MG-E01..E14

| # | الفجوة | الوصف | القرار المرتبط |
|---|---|---|---|
| GAP-MG-E01 | **التقييم لكل مخزن** | ERPNext: Valuation Method إعداد **شامل** واحد (FIFO/MA)؛ FN: **لكل مخزن** | F-MG-1 (custom + محرك) |
| GAP-MG-E02 | **FEFO إلزامي** | لا فرز انتهاء تلقائي في Pick/Issue القياسي | F-MG-2 hook |
| GAP-MG-E03 | **مستندات Item Types الأربعة** | is_stock_item ثنائي؛ لا Butchery/Cash Purchase | custom `item_type` enum + منطق إصدار |
| GAP-MG-E04 | **SubCode** | Variants أثقل من الحاجة | F-MG-10 |
| GAP-MG-E05 | **دورة عطاءات كاملة** | Supplier Quotation بلا Invite/Tender/Evaluation/Analysis/Close | F-MG-5 |
| GAP-MG-E06 | **تفويض متعدد المستويات بشرط** | Workflow قياسي يفعل لكن ربطه بمفتاح INI متدرج يحتاج Feature Toggle + Workflow ديناميكي | F-MG-3 |
| GAP-MG-E07 | **البعد الرابع (Backdate أيام)** | لا نظير | F-MG-4 |
| GAP-MG-E08 | **الإقفال الشهري للمخزن** | Period Closing موجود للـ GL لا للمخزن | F-MG-8 |
| GAP-MG-E09 | **Vendor العائلات السبع** | Supplier فقير جداً بالمقارنة | F-MG-2 + child tables |
| GAP-MG-E10 | **أعلام اتجاه الحركة (صنف×مخزن)** | لا نظير (MTO lead time ليس هذا) | F-MG-12 |
| GAP-MG-E11 | **DPR من نقص الإصدار** | لا توليد آلي PR من فشل Issue | F-MG-6 |
| GAP-MG-E12 | **Budget Apportion بأنماط** | Monthly Distribution موجود لكن F2/F4 نسخ مراكز + أنماط FN غير قياسية | client script |
| GAP-MG-E13 | **هوية Company Type** | مالك الكيان: FO أم SYS أم Supplier Group؟ | F-MG-11 (Phase 11) |
| GAP-MG-E14 | **قيد التسلسل في Store Ledger** | الفرق بين "معالج" و"مفتوح" بلا حالة قياسية للمخزن | F-MG-8 |

## ثالثاً: مقارنة كثافة الفجوات مع الوحدات السابقة

| الوحدة | فجوات مصدر | فجوات ERPNext | الملاحظة |
|---|---|---|---|
| FO | 10 | 10 | مرجع |
| FAS | 8 | 9 | أقل تعقيداً محاسبياً |
| ACR | 10 | 10 | — |
| POS | 11 | 12 | — |
| SYS | 8 | 9 | — |
| **MGT** | **12** | **14** | **الأعلى إجمالاً** — طبيعي لوحدة تشغيلية كثيفة بمعاملاتها، مع أفضل قابلية إسقاط قياسي عكسياً (Stock Entry!) |

> **الاستنتاج المعماري:** فجوات MGT **كمية لا نوعية** — معظمها "سلوك موثق غني يفوق المنصة" (العكس من فجوات SYS النمطية "مرجع غائب") — أي أن عبء التنفيذ هنا **تخصيص حقول وسلوك** أكثر منه ابتكار بنى. أعلى عنصر ابتكار: محرك التقييم للمخزن الواحد (F-MG-1) + الإقفال الشهري (F-MG-8).
