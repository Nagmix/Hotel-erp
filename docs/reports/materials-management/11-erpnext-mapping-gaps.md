# 11 — تحويل طبقة تقارير MGT إلى ERPNext + فجوات (Phase 7)

> Mapping + Gaps لطبقة تقارير MGT (~53 فريداً). مرجع الوحدة الأم: `docs/modules/materials-management/16-erpnext-mapping.md`.

---

## 1. جدول التحويل F-MR-1..16

| # | عنصر FN6i | مقابل ERPNext | القرار |
|---|---|---|---|
| F-MR-1 | **نمط الخطوتين Preview→Generate** | Query/Script Report + Print Preview القياسي | التكافؤ وظيفي مباشر — معاينة التخطيط قبل التوليد (Standard UX) |
| F-MR-2 | **عائلة الماستر (1/6.x/9.x)** | Item/Supplier/Contract List Views + **Stock Ledger / Stock Balance** بالفلاتر | Physical Location → Warehouse/بنية رف (Custom) · Last-Updated sort قياسي · 5 مناظير المورد = تفكيك حقول Supplier |
| F-MR-3 | **§2/§3 حالة DPR/PO** | Material Request + Purchase Order status queries (status/status filter) | 4 حالات POS مقابل 3 DPR → توحيد على 4 (Partial حالة صريحة في ERPNext أصلاً) — يغلق عدم التناظر |
| F-MR-4 | **§4 عائلة الاستلام (8 تقارير)** | Purchase Receipt (register/item-group/supplier ملخصات) | Store Break → Group By Warehouse في الطباعة · ثلاثية Complimentary → فلتر is_return/free (المجاني = سلعة مجانية بلا سعر — Custom checkbox) |
| F-MR-5 | **4.3 Capital Goods Receipt** | Purchase Receipt → Asset capitalization + تقرير مدخلات ضريبة الأصول | الجسر الموازي لFDX mapping الأصل — عمود "Capital" على PR line |
| F-MR-6 | **9.3 Ledger by Item + 18.4 Stores Ledger** | **Stock Ledger** (1:1 حرفياً — نفس الجوهر: Opening/Vouchers/Closing للصنف) | أثقل توافق بنيوي في المرحلة 7 كلها: Process Stores Ledger = تجميع شهري للـStock Ledger (Virtual/Scripted) · Zero-transactions = فلتر no-entries |
| F-MR-7 | **9.4 Item Expiry** | Batch + تقرير **Batch-Wise Expiry** | N-أيام الإنذار → فلتر expires_within_days — يبنى فوق Batch natively |
| F-MR-8 | **§5 الاستهلاك + §22 الموازنات** | Stock Analytics + **Budget** (Budget vs Actual) + فلاتر Cost Center/Project | ثنائية Purchase/Consumption → Budget against Purchase Order vs Stock Issue · Stockable/Direct → فلتر Item is_stock_item عكسه! |
| F-MR-9 | **§11 ABC Analysis** | **تقرير ABC المدمج في ERPNext** (Stock/Procurement) | توافق native كامل تقريباً: العتبتان A/B قابلتان للضبط — % by Group = تشغيله لكل Item Group |
| F-MR-10 | **§12-14 FSN/Slow/Non-Moving** | **تقارير FSN/Non-Moving/SLOW المدمجة** (Serial-Batch/Stock Ageing) | معاملات لكل مجموعة → تشغيل متعدد أو Custom report؛ الإدخال المدمج (double-click Days) → حوار إعدادات التقرير |
| F-MR-11 | **§15 عائلة طباعة المستندات (7)** | Print Formats لـMaterial Request/PO/Purchase Receipt/Stock Entry | **Print Forms (FAS) → Print Format + Custom Print Format لكل عميل** — قانون "customized programs per client" يتحقق طبيعياً بHTML/Jinja مخصص لكل موقع! (يغلق D04 ببنية ERPNext) |
| F-MR-12 | **§16 Sub Store/CC** | Stock Entry (Transfer) + **Warehouse structure** (Main→Sub) + Stock Balance by Warehouse | Sub-CC → Cost Center هرمية (ERPNext CC tree قياسي) — حيازة CC = Warehouse per CC أو حقل CC على SE |
| F-MR-13 | **§17 Re-Order (as-of-now + Load)** | **Reorder level تقرير ERPNext المدمج** (Items below reorder) | نفس المعادلة `qty < reorder_level` — native؛ Auto Indent → **Material Request auto** (يقابل FNB mapping) |
| F-MR-14 | **§18 Physical Stock family** | **Stock Reconciliation** (الفرق = actual vs system native) + variance report | 18.3 Negative → فلتر negative-only · قبل/بعد الترحيل = نفس التوقيت في SR (قبل التقديم/بعده) — مرونة موثقة تتحقق |
| F-MR-15 | **§10 Supplier Bill + §19 Comparative** | 3-Way Match (PR/PO/Invoice) + **Supplier Quotation مقارنة** | verify يومي → Purchase Invoice matching · Quotation comparison native |
| F-MR-16 | **§23 Audit Trial + §24 VAT/Tax** | **Version History** (كل DocType) + Purchase Taxes register + **Taxes India package** | "modified AND deleted" → Version + **amendments/cancellations trail** — المحذوف = Cancelled مع أمومة الفلتر (أقرب ممكن؛ الفرق: ERPNext لا يعرض deleted-rows كتقرير استعلامي واحد — أصل Custom صغير) · PJV-wise → ترتيب حسب Purchase Invoice/Journal |

**التقدير الإجمالي**: ≈ **4-6 أصول مخصصة / 3-4 أسابيع** — **أنسب وحدات المرحلة 7 للتحويل**: ABC/FSN/Reorder/Stock Ledger/Reconciliation/3-Way **native تماماً** (جذور ERPNext مخزنية!) · الأصول المخصصة: تقرير العائد §21 (Yield FROM/TO) + سجل المحذوفات التجميعي + VAT assessment-format + R2 dual-layout.

## 2. فجوات GAP-MR-*

### فجوات تصميم (D)

| ID | الفجوة | الأثر | الشاهد |
|---|---|---|---|
| GAP-MR-D01 | **~53 تقريراً بلا صلاحية واحدة** (11/17 عائلة الصفر) — تشمل Audit Trial وVAT | reproduction يفرض Report Permission Matrix | REP كله |
| GAP-MR-D02 | **تكرارات كتالوغية**: §1≡6.1 حرفياً + VAT/Tax أوصاف متطابقة + ازدواج رقم 6 | تضخم كتالوغي — دمج إلزامي عند التحويل | C-MR-01/02/03 |
| GAP-MR-D03 | **صفر قنوات إلكترونية** (لا Spool/Export في REP كله — مقابل 4/5 قنوات FO/POS) | تراجع نمطي داخل المرحلة 7 نفسها | REP كله |
| GAP-MR-D04 | **Print Forms عبر FAS**: طباعة PO/SPO/GRN معلّقة ببرامج لكل عميل (Pgm.ID في FAS-SET §15) | اعتماد تكويني عابر للوحدات + كود خارج الحزمة | 15.3/15.4/15.6 |
| GAP-MR-D05 | **R2 Variant (5.4)**: فرق التخطيط عن 5.3 غير موثق | قرار دمج/إبقاء معلق | UNK-089 |
| GAP-MR-D06 | **كل تخطيطات المخرجات غائبة** ("following format:" بلا صور) — أعمق فجوة معلوماتية في الوحدة | بنية أعمدة ~53 تقريراً مجهولة (مقابل FO/POS الغنية نصياً) | REP كله |
| GAP-MR-D07 | **FSN معاملات Grid-embedded** بلا ماستر صريح في REP (يقابل SET §18) + بطء §13 بمرجع نسبة مجهول | تكوين مشتت عبر طبقتين | §12/§13 |

### فجوات تشغيل (P)

| ID | الفجوة | الأثر |
|---|---|---|
| GAP-MR-P01 | **عتبتا ABC (A%/B%) بلا افتراضيات أو حدود** | تحقق رقمي غائب — تصنيف قابل للعبث الأعمى |
| GAP-MR-P02 | **Audit Trial يعرض المحذوفات لكن بلا استرجاع** | قراءة بلا عضو تصحيحي |
| GAP-MR-P03 | **§17 لا يعمل تاريخياً** (Current Date فقط) | لا تحقيق بعد-الوقت في إعادة الطلب — يتطلب Snapshot |
| GAP-MR-P04 | **"comments of customer"** في سياق مخزني — عبارة غريبة عابرة (نسخ من وحدة ضيف؟) | دليل تحريري — لا أثر تشغيلي، يوثق |
| GAP-MR-P05 | **Printer pre-defined list** المصدر غير موثق | قرار إعداد أجهزة عند التنفيذ |

## 3. مجهولات جديدة (UNK-089..095) — تُسجل في unknowns.md

| ID | السؤال | الأثر | المصدر |
|---|---|---|---|
| UNK-089 | **R2 (5.4)**: ما الذي يميز تخطيطه عن 5.3؟ (لاحقة إصدار أولى في اسم تقرير) | قرار دمج/إبقاء — عائلة "Format 2" القادمة في FAS-REP تعمّق السؤال | REP 5.3/5.4 |
| UNK-090 | **VAT (24.1) مقابل Tax (24.2)**: تقريران مختلفان بشاشات مختلفة أم تكرار كتالوغي؟ (الأوصاف حرفياً متطابقة) | كتالوغ + تحويل | REP §24 |
| UNK-091 | **Print Forms (FAS-SET §15)**: قائمة Pgm.ID الكاملة؟ صيغة التسجيل؟ من يملأها (مستخدم أم تنصيب)؟ | الاعتماد التكويني MGT→FAS يبقى بلا مواصفة كاملة | REP 15.x + FAS-SET |
| UNK-092 | **PJV**: التوسيع الكامل (Purchase Journal Voucher؟) ونطاق استخدامه — "Print Sequence PJV Wise" ترتيب حسب كيان FAS غير معرَّف هنا | مصطلح عابر للوحدات بلا تعريف في أي وحدة | REP 24.1 + FAS-REP §18 |
| UNK-093 | **قائمة الطابعات المعرفة مسبقاً** (pre-defined list): أين تُعرَّف؟ (SYS Hardware؟ MGT-SET؟ FAS؟) | طباعة MGT معلقة على تكوين مجهول المصدر | REP 15.1/15.3/15.4 |
| UNK-094 | **FSN Specifications**: أين تُخزَّن فعلاً — Grid التقرير (12) أم Define FSN parameter (SET §18)؟ من الشاشة الأم؟ | تكوين مشتت + ازدواج مرجعي | REP §12 + SET §18 |
| UNK-095 | **حالة DPR المفقودة**: لماذا لا تملك Requisitions حالة Cancelled (بينما PO تملكها)؟ هل تُلغى طلبات الأقسام أصلاً؟ | عدم تناظر دورة المستندات | REP §2/§3 |

## 4. تناقضات جديدة (C-MR-01..03) — تُسجل في contradictions.md

- **C-MR-01**: **القسم 6 مرقّم مرتين** في TOC والجسم معاً (Item & Vendor List + Closing Stock by Type) + بند TOC مكسور "6._Item___Vendor_List" — ازدواج ترقيم بلا إعادة تسلسل.
- **C-MR-02**: **§6.1 نسخة حرفية كاملة من §1** (نفس النص والخطوات والمعايير) تحت قسم مختلف.
- **C-MR-03**: **§24.2 Tax Report وصفه حرفياً مطابق لـ§24.1 VAT Report** (جملة-بجملة) رغم أنهما تقريران بشاشتين مختلفتين.

> (دون مستوى التناقض — أثر تحريري: "Sun Cost Center" (16.3 ص90) · "Audit Trial" بدل Trail (23) · "comments of customer" (4.1) · أخطاء ترقيم خطوات في 4.6/5.1.)

## 5. معايير قبول (AC-MR — عينة قابلة للتوسيع)

1. **AC-MR-01** (الرصيد الافتتاحي): 4.8 يقبل الشهر الجاري حصراً — طلب افتتاحية شهر سابق → رفض.
2. **AC-MR-02** (إعادة الطلب): صنف رصيده 5 وre-order 10 → يظهر في §17؛ صنف رصيده 15 → لا يظهر. (تاريخ النظام فقط).
3. **AC-MR-03** (بوابة البيانات): 18.1 لتاريخ بلا جرد مُدخل → لا توليد؛ لتاريخ فيه جرد → يعمل.
4. **AC-MR-04** (التباين السالب): جرد فعلي أقل من النظام → الصنف في 18.3؛ بعد Variance Update مباشرة → يبقى قابلاً للتوليد (قبل/بعد).
5. **AC-MR-05** (ABC): A=70/B=20 على استهلاك مجموع 10000 → أصناف التراكمي ≤70% صنف A، ≤90% B، الباقي C.
6. **AC-MR-06** (العائد): From 10كغ×4 = 40 · To 8كغ×5 = 40 → التباين الكمي −2كغ، الكفاءة الكمية 80%.
7. **AC-MR-07** (FSN): cut-off 30 يوماً + Fast qty 100 → أصناف تتحرك <30 يوماً وكمية ≥100 = Fast.
8. **AC-MR-08** (المحذوفات): حذف معاملة ثم Audit Trial مع "deleted" → تظهر مع علامتها.
9. **AC-MR-09** (VAT): فترتان ضريبيتان 10%/12% في نفس الاستلام → كلاهما؛ Print PJV-wise يرتب حسب قسيمة المشتريات لا التاريخ.
10. **AC-MR-10** (Store Break): مخزنان في 4.2 → كل مخزن يبدأ صفحة جديدة.
11. **AC-MR-11** (ثلاثية Comp): 4.2 بوضع "only Complimentary" → الأصناف المجانية وحدها.
12. **AC-MR-12** (الحالات): DPR مستلم نصفه → Pending؛ PO ملغى → Cancelled (وDPR لا يملك Cancelled — عدم التناظر المقصود).
13. **AC-MR-13** (8 Store Balance): نطاق يعبر شهرين → رفض (of the month).
14. **AC-MR-14** (الإنذار المبكر): N=7 → صنف ينتهي بعد 5 أيام يظهر؛ بعد 10 → لا.
15. **AC-MR-15** (R2): توليد 5.3 و5.4 بنفس المدخلات → مخرجان يختلفان في التخطيط (غير قابل للتحقق قبل التنفيذ — UNK-089).

## 6. Smoke Test (خطة 20 خطوة لطبقة تقارير MGT)

1. Inventory Item List بترتيب **Last Updated** ثم **Physical Location** → تسلسلان مختلفان (§1).
2. Passive checkbox → الأصناف الخاملة تدخل القائمة (§1).
3. Vendor List منظور bank ثم tax → حقول مختلفة؛ وضع Black List → المحظورون فقط (6.3).
4. Contract List بBy Expiry Date → العقود مرتبة زمنياً (6.4).
5. Item Expiry بN=7 → إنذار استباقي (9.4/AC-14).
6. Requisition Status لDPR مستلم جزئياً → Pending (AC-12a).
7. PO Status لملغى → Cancelled (AC-12b) — مع توثيق غياب حالة DPR المقابلة.
8. Transaction Checklist بنوع Issue → الشاشة تتبدل (Adaptive) (4.1).
9. Receipt Register بمخزنين + Store Break → صفحة لكل مخزن (AC-10).
10. Receipt Register بوضع only Complimentary → المجاني فقط (AC-11).
11. Capital Goods Receipt → استلامات رأسمالية بVAT (4.3).
12. CC Consumption بوضع Department ثم CC → منظوران (5.1) · فلتر Stockable → Direct يختفي (5.2).
13. 5.3 ثم 5.4 بنفس المدخلات → توثيق الفرق (R2/UNK-089).
14. Opening Balance بطلب شهر سابق → رفض (AC-01).
15. Closing Stock as-on تاريخ قديم → رصيد ذلك اليوم (16') + Zero balance toggle.
16. Re-Order: صنف 5/10 يظهر — بلا معامل تاريخ (AC-02).
17. Physical Stock Entry ليوم X → 18.1 يعمل لX ويرفض ليوم بلا جرد (AC-03) · 18.3 قبل وبعد Update (AC-04).
18. ABC بA=70/B=20 → توزيع الفئات (AC-05) · FSN بcutoff 30/qty 100 → تصنيف (AC-07).
19. Efficiency لتحويل 10كغ→8كغ → تباين −2 وكفاءة 80% (AC-06).
20. Audit Trial بعد حذف معاملة → المحذوفة تظهر (AC-08) · VAT بترتيب PJV (AC-09).
