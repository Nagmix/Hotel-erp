# 11 — تحويل طبقة تقارير FAS إلى ERPNext + فجوات (Phase 7 — **خاتمة الحزمة**)

> Mapping + Gaps لطبقة تقارير FAS (46 تقريراً + شبحان). مرجع الوحدة الأم: `docs/modules/financial-accounting/16-erpnext-mapping.md`.

---

## 1. جدول التحويل F-FA-1..16

| # | عنصر FN6i | مقابل ERPNext | القرار |
|---|---|---|---|
| F-FA-1 | **قنوات الإخراج الخمس** (Print/Email/Spool-to-file/Excel/132) | Print Format + **إرسال بالبريد PDF** + تنزيل XLSX/CSV + **Letter/A4** بدل 80/132 | Spool بملف = تنزيل مسمى؛ Broadgun/Outlook → إرسال ERPNext القياسي (يغلق كومة الاعتمادات!) · 132 → Landscape/A3 |
| F-FA-2 | **§1 CoA + شجرة Sub group/Sub Head/Category** | Chart of Accounts (شجرة native) + تقرير COA | التصنيف الرباعي = Root types (Asset/Liability/Income/Expense) 1:1 |
| F-FA-3 | **§2/2(2) + §33 المحذوفات والمعدلات** | Version History + **Audit Log** + Cancelled (مع أمومة الفلتر) | Txn-Date-XOR-Updated = فلتر creation vs modified-on — أصل custom صغير فوق Audit Log · "deleted" = Cancelled entries |
| F-FA-4 | **§4 Day Books ×3** | **Bank/Cash Ledger** (Payment+Receipt) + running balance | Format 2 (Contra) = نفس دفتر المصرف بمرآة الطرف المقابل — Custom view واحد؛ مثال A008000 يُعاد كاختبار |
| F-FA-5 | **§5/§6/§17 الدفاتر** | **General Ledger (native!)** + Party/Dimension فلاتر | GL/SL/Dept/CC = Dimension native؛ Detail Register = GL بالفواتير (bill no حقل مرجعي)؛ Adaptive Cursor → conditional fields |
| F-FA-6 | **§7 P&L ×2 + §8 BS** | **Profit and Loss / Balance Sheet (native!)** + CC/Dimension + Period Comparison (YTD/PrevYr native!) | PL-CC = P&L بdimension — الفترات الرباعية قياسية |
| F-FA-7 | **§9 TB ×4** | Trial Balance (native) + Sort/format variants | XOR 0/132 → layout option؛ Sub group ترتيب = شجرة COA؛ الفروق التخطيطية تُدمج في تقرير واحد بوضع عرض |
| F-FA-8 | **§10 Creditors Outstanding (Ageing)** | **Accounts Payable Summary/Ageing (native!)** | As On/Month/Date = as-at filter native؛ Net D/C/Both |
| F-FA-9 | **§11-13 سجلات المشتريات/المصروف/الضريبة** | Purchase Register + Purchase Taxes + **GL بفلاتر** + Vendor | ثلاثية أرقام (Reg/Service/VAT) → حقول Custom على Supplier/Invoice |
| F-FA-10 | **§15/16 Contract Debit Note** | **Debit Note (native!)** + فرق سعر العقد (Custom: Contract Rate على Item-Supplier) | قصة الفرق economics → BOM price vs supplier contract؛ waive = خصم يدوي على DN |
| F-FA-11 | **§18 Pending Receipts for PJV** | **Purchase Receipt not billed (native query!)** | Regular/Service PJV → فصل Goods vs Services (Service PR = Service Entry)؛ Misc. Supplier = Supplier Group |
| F-FA-12 | **§19/20/21 طبقة النزاهة التكاملية** | **ERPNext يمنع الحفظ بلا Account** (عكس FN6i!) — تقارير 19/21 تُستبدل بQuery مخصص "مفاتيح بلا حساب" | **قرار معماري D-مهم**: من نموذج "احفظ ثم نبّه" إلى "اربط ثم احفظ"؛ Auto-Posted = Journal Entry بorigin-filter (FOM/ACR/INV → Origin/Series) |
| F-FA-13 | **§23 Bank Reconciliation + PDC** | **Bank Reconciliation (native!)** + Bank Statement Import (يغلق الرصيد اليدوي!) | Realized = clearance date native؛ Unrealized = uncleared؛ PDC → **Payment Entry post-dated** أو State-tracking (custom) |
| F-FA-14 | **§24/25 Advice/Cheque + Voucher Print** | Print Format لPayment/Journal Entry + **Cheque printing** (custom format شائع) | Tag/Load → اختيار checkboxes قبل الطباعة (UX أرقى)؛ Normal/Repeat → سجل إعادة طباعة |
| F-FA-15 | **جناح TDS (7 تقارير + 16A بتفاصيله)** | **India Compliance / TDS native** (ERPNext هندي الأصل!) + شهادات | أرباع ×4 + Ack → حقول إيداع ربع سنوي؛ Height 11/12 → Page Height للPrint Format؛ Email/Spool → القنوات القياسية |
| F-FA-16 | **§34 User Reports + §22 Budget** | **Report Builder/P&L مخصص** + Budget (native) + **Lakh/Million (Compact Numbers native هندي!)** | مصفوفة القيم الست = Format settings (absolute/rounded/brackets/Lakh) — native أو إعدادات؛ (-ve) بين قوسين = خيار عرض محاسبي قياسي |

**التقدير الإجمالي**: ≈ **5-7 أصول مخصصة / 3-4 أسابيع** — **أنسب تحويل بعد MGT مباشرة**: القوائم/الدفاتر/TB/AP-ageing/Bank-Rec/TDS/Debit-Note/Pending-Receipts **كلها native أو شبه native** (ERPNext نبت محاسبي!) · الأصول المخصصة: طبقة النزاهة المقلوبة (12) · Contra view · PDC lifecycle · Tag-Print التفاعلي · صيغة 16A الرسمية.

## 2. فجوات GAP-FA-*

### فجوات تصميم (D)

| ID | الفجوة | الأثر | الشاهد |
|---|---|---|---|
| GAP-FA-D01 | **46 تقريراً بلا صلاحية** (12/17 — الأخطر في الحزمة: Audit+TDS+شيكات+GL-structure!) | reproduction يفرض Report Permission Matrix صارمة | REP كله |
| GAP-FA-D02 | **شبحان ختاميان** (IDS Crystal + iDesigner) — IDS **متكرر عبر وحدتين** (FO+FAS) | قوالب TOC مشتركة بلا جسم — طبقة مصمم وعد لا مواصفة | TOC تحت §34 |
| GAP-FA-D03 | **أوصاف TB الثلاثة المتطابقة حرفياً** + إحالة ذاتية (3.3) | تضخم كتالوغي — دمج في تقرير بوضع عرض | §9 |
| GAP-FA-D04 | **HRP غائب من أنواع الترحيل الآلي (FOM/ACR/INV)** — وكذلك FXD (إهلاك F12!) | خريطة الترحيل الآلي **غير شاملة** — مصير رواتب/إهلاك مجهول المسار | §21 → UNK-098 |
| GAP-FA-D05 | **حديقة تسميات الجسور**: FOM/FOS/POS/FO-to-Finance/FA — نفس الكيان بأسماء مختلفة بين §19/§20/§21 | خطر التباس عند التحويل — جدول مرادفات إلزامي | C-FA-01 |
| GAP-FA-D06 | **مسار Email هش**: Outlook+Broadgun+default-printer+PDF-settings-الحمراء | اعتماد عتادي مكتبي 2000s — يُستبدل ببريد الخادم | 16A |
| GAP-FA-D07 | **ورق قانوني hard-coded** (Height 11/12 IN) | تخصيص ورق محصور بنمطين قانونيين | 16A خطوة 11 |

### فجوات تشغيل (P)

| ID | الفجوة | الأثر |
|---|---|---|
| GAP-FA-P01 | **Voucher Print IDs لكل Transaction Code** — عبء تسجيل برامج لكل نوع | تحويل: Print Format لكل Doctype (أرخص) |
| GAP-FA-P02 | **رصيد كشف المصرف يدوي** (Unrealized) | يُغلق بBank Statement Import native |
| GAP-FA-P03 | **XOR 0/132 في TB-F2** يمنع الأصفار+العريض معاً | تقييد عرض غير مبرر — يُفك الارتباط |
| GAP-FA-P04 | **Advance Paid = تقرير فقط** — لا دورة تسوية إيداعات من FAS | دورة الإيداع تُدار في FO — تقرير قراءة فقط |
| GAP-FA-P05 | **Repeat/Reprint بلا تعطيل أو إلزام إشعار** (Advice 24 · 16A 26) — مقابل لصق بلا رقم في POS | ثغرة مستنديات موثقة ×2 |

## 3. مجهولات جديدة (UNK-096..102) — تُسجل في unknowns.md (الإجمالي النهائي 102)

| ID | السؤال | الأثر | المصدر |
|---|---|---|---|
| UNK-096 | **الشبحان الختاميان**: IDS Crystal Report Designer (**شبح متكرر مع FO!**) + Advice/Cheque iDesigner — مصمم iDesigner؟ علاقة IDS؟ | عائلة TOC-template تكاد تكون مثبتة — طبقة تصميم غير موثقة | FAS-REP TOC نهاية |
| UNK-097 | **Transaction Checklist (2)**: ما يميزه فعلاً عن (1)؟ (شاشاته غير موثقة والمثال الوحيد Doc#-Delete) | كتالوغ + تحويل | §2/§2(2) |
| UNK-098 | **مصير ترحيل HRP (الرواتب) وFXD (الإهلاك F12)**: غائبان من أنواع Auto-Posted الثلاثة (FOM/ACR/INV) — يدويان؟ أنواع غير موثقة؟ | **يلامس UNK-010 (أصل المشروع!)** — خريطة الترحيل الكاملة معلقة | §21 |
| UNK-099 | **Trial Balance (3.3)**: فرق التخطيط عن TB-F2 (إحالة ذاتية بلا جسم) | قرار دمج ×4 | §9 |
| UNK-100 | **نماذج TDS الست**: الفروق الرسمية بين 26C/26K (توأمان وصفاً) ومتى يُستخدم كل نموذج | امتثال — مواصفة ناقصة رغم الوفرة | §27-31 |
| UNK-101 | **Broadgun PDF printer**: إصدار/إعدادات PDF-الحمراء (غير ظاهرة — صورة غائبة) | مسار الإيميل القديم كله يُستبدل | 16A خطوة 9 |
| UNK-102 | **Sl. Name** (Serial Name في Cash/Bank Book وVoucher Print): الكيان والدلالة — نفس Sub Ledger؟ | غموض كيان متكرر | §4/§25 |

## 4. تناقضات جديدة (C-FA-01..03) — تُسجل في contradictions.md (الإجمالي 12)

- **C-FA-01**: **حديقة أسماء الجسور** — §19 "POS to Finance Defn" مقابل §20 "FOS to FA" مقابل §21 "FOM (يشمل Front Desk **and** Point of Sale)" — نفس منظومة الجسور بثلاث اصطلاحات (FOS لا تُعرَّف في أي مكان).
- **C-FA-02**: **أوصاف Trial Balance الثلاثة متطابقة حرفياً** (TB / TB Format 2 / TB (3.3)) — والثالث يحيل "Fill in all the fields as explained in the section 'Trial Balance Format 2'" — أكبر عائلة نسخ-نص في وحدة واحدة.
- **C-FA-03**: **"deference value"** في أعمدة Contract Debit Note List (خطأ مطبعي صارخ لdifference) + "continues" بدل continuous (§24/25) + خطوة "8" بين 1 و3 في Voucher Print — عنقود أخطاء تحريرية.

## 5. معايير قبول (AC-FA — عينة قابلة للتوسيع)

1. **AC-FA-01** (past-only): TB-F2 بتاريخ > تاريخ النظام → رفض؛ بتاريخ أمس → قبول.
2. **AC-FA-02** (past-only شهري): TB-F2 بشهر > الشهر الجاري → رفض.
3. **AC-FA-03** (month-bound): Advice بتاريخ خارج Month/Year المحددين → رفض.
4. **AC-FA-04** (قيد FY): PDC بFrom خارج السنة المالية → رفض.
5. **AC-FA-05** (Contra مثال الدليل حرفياً): A008000 مدين 1000$ + قبض 500$ من المدينين → Day Book F2 يعرض حركة الدائن على المدينين (contra).
6. **AC-FA-06** (الرباعية): PL-CC يعرض 4 أعمدة: Month + YTD + Previous Year + Total.
7. **AC-FA-07** (XOR): TB-F2: اختيار Zero Balance **يعطّل** خيار 132 (واحد فقط).
8. **AC-FA-08** (فاحص النزاهة): إيراد FO بلا ربط حساب → يظهر تحت "FO to Finance Defn"؛ بعد الربط → ينتقل إلى §20 Linked.
9. **AC-FA-09** (الترحيل الآلي): معاملة MGT مرحّلة → تظهر تحت Type=INV فقط.
10. **AC-FA-10** (PJV): GRN غير مرحّلة → Pending؛ بعد ترحيلها لPJV → تختفي من Pending وتظهر Auto-Posted (INV).
11. **AC-FA-11** (Tag): Advice: TagAll يوسم الكل · UnTagAll يفرغها · Un Tag يفك الموسوم فقط.
12. **AC-FA-12** (16A): Vendor بدون TDS Tagging → لا إرسال؛ Email متاح فقط لAccount Type=Vendor.
13. **AC-FA-13** (16A أرباع): شاشة Ack تقبل 4 أرباع برقم إشعار وشيك/DD لكل ربع.
14. **AC-FA-14** (Audit): حذف قسيمة ثم تقرير بUpdated Date + Deleted → تظهر؛ بTransaction Date → لا تظهر (حصلت "أول مرة" فقط).
15. **AC-FA-15** (User Reports): اختيار (-ve) in bracket → سالب 500 يُطبع (500)؛ Lakh → 1,00,000 تُعرض 1.00.

## 6. Smoke Test (خطة 20 خطوة لطبقة تقارير FAS)

1. CoA بفلاتر Assets ثم Expenses → قائمتان مختلفتان (تصنيف رباعي).
2. Transaction Checklist بخيار deleted transaction → المحذوفات تظهر (§2).
3. TC (2) بDoc# + Delete → حركات Doc# المحذوفة فقط (مثال الدليل).
4. Day Book لفترة بPrint Narration → السرديات تظهر (§4).
5. Day Book Format 2 بحساب مصرفي أُدخل له قبض من مدين → حركة Contra تظهر (AC-05).
6. General Ledger بمنظور Cost Center → الخيارات الإضافية تتبدل (Adaptive) + نطاق شهور.
7. P&L عادي ثم PL-CC → أعمدة Month/YTD/PrevYear/Total (AC-06).
8. TB-F2 بتاريخ مستقبلي → رفض (AC-01) · بتاريخ اليوم → يعمل.
9. TB-F2 بZero Balance → خيار 132 يتعطل (AC-07 XOR).
10. Creditors Outstanding بAs On + Ageing → أعمار الدائنين (تفصيلي ثم ملخص).
11. Expense Register بAbove=1000 → مصروفات ≥1000 فقط.
12. Debit Note Print: Load → Tag صنفين → طباعة موسومة فقط؛ ثم CDN List تعرضها بأعمدة GRN/deference/waive (§15/16).
13. Unlinked بنوع POS → مجموعات أصناف منافذ بلا حسابات؛ اربطها في Setup → تنتقل إلى Linked (AC-08).
14. Auto Posted بType=INV → ترحيلات MGT فقط (AC-09).
15. Pending PJV: GRN قائمة → ترحّل → تختفي وتظهر INV (AC-10).
16. Bank Rec بRealized Date range → الشيكات المتحققة (§23).
17. Advice: تاريخ خارج M/Y → رفض (AC-03)؛ TagAll/UnTagAll دورة كاملة (AC-11)؛ Repeat لإعادة طباعة موثقة.
18. Voucher Print: Toggle Tag يوسم الكل · Name/Address يظهر على القسيمة (§25).
19. 16A: Vendor بلا TDS Tagging → رفض الإرسال (AC-12)؛ Ack بأرباع ×4 (AC-13)؛ Spool بFile Name.
20. Audit Trial: عدّل قسيمة ثم احذفها → Updated+Deleted يعرضها · Transaction Date لا يعرض الحذف (AC-14) · User Reports ب(-bracket)+Lakh (AC-15).

---

## 7. الخاتمة التجميعية للمرحلة 7 (خاتمة الحزمة 65/65)

بإغلاق FAS-REP تكتمل قراءة **65/65 ملفاً** وثائق طبقة التقارير لأربع وحدات كبرى (FO ~135 · POS ~57 · MGT ~53 · FAS 46 = **~291 تقريراً موثقاً في المرحلة 7**) فوق 306 ملفات وحدات — **الحصيلة الكلية للمشروع: 17/17 وحدة · 306+48=354 ملف وثائق**.

**أهم خلاصات المرحلة 7 النهائية:**
1. **هوية السوق**: حزمة هندية بامتياز (PAN · TDS ×7 · C-Form/RLM · assessment · Lakhs · MMYY).
2. **الطبقة المخفية الكبرى**: طبقة النزاهة التكاملية (FAS §19/20/21) — الجواب النظامي على سؤال الجسور.
3. **عائلات عابرة مؤكدة**: 80/132 (اتجاهان متعاكسان!) · Format-2/R2 (لاحقة تخطيط) · Tag-YES (MNT+MGT+FAS) · الأشباح (IDS Crystal ×2) · Print Forms (6 تقارير عبر وحدتين) · المحذوفات (MGT+FAS) · عتبات المبلغ (FAS ×2) مقابل عتبات الزمن (MGT).
4. **مفارقات حاكمة**: 46+57+53+135 تقريراً **بلا صلاحية واحدة** (12/17 وحدة REP) — أكبر فجوة إنتاجية موحدة.
5. **المتبقي (Phase 8+)**: المراجعة الشاملة + cross-referencing + Knowledge Graph النهائي + توحيد العائلات العابرة أعلاه في مرجع واحد.
