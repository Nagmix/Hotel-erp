# 03 — جدول المرادفات والمعجم الموحد (Synonyms & Glossary)

> **حل GAP-SYS-D02/C-FA-01 توثيقياً**: الحزمة تستعمل مصطلحات متبدلة للكيان نفسه ورموزاً غير معرَّفة في أي قاموس واحد. هذا الملف هو القاموس الموحد الذي يُرجَع إليه عند التنفيذ وقبل بناء أي Model.
> المصدر: 65 ملفاً مقروءة + سجل التناقضات (12) — كل مرادف موثق بمصدره الأول.

---

## 1. حديقة أسماء الجسور (C-FA-01) — الجسر المالي الواحد بخمسة أسماء

> الأخطر توثيقياً: نفس منظومة «ترحيل إيراد FO/POS إلى المالية» بثلاث اصطلاحات في ثلاثة أقسام متتالية من FAS-REP.

| المصطلح | المصدر | المقصود الموحد |
|---|---|---|
| **FOM** | FAS-REP §21 (نوع Auto-Posted) | Front Office Module — النوع الرسمي ويشمل «Front Desk **and** Point of Sale» |
| **FOS to FA** | FAS-REP §20 | FOS غير معرَّفة في أي مكان — الأرجح **Front Office System** (=POS هنا!) |
| **POS to Finance Defn** | FAS-REP §19 | الاسم الثالث لنفس معاملات الربط |
| FO / Finance / FA | عبر كل الوحدات | Front Office / Financial Accounting |
| **الحسم التنفيذي** | — | **نوع ترحيل واحد `FOM`** يغطي FO+POS + جدول link-parameters موحد (Link FOM/POS/Exmp Tax to Finance · Vendor Tax Split) |

## 2. معجم أنماط الدفع والتسوية (Pay & Settlement Lexicon)

| الرمز/المصطلح | المصدر | المعنى الموثق |
|---|---|---|
| **ADQ** | FO | Advanced Payment — دفع مقدم (Guest Ledger) |
| **ADC** | FO | Advanced Deposit against Charge (شحن مقدم) |
| **ADV** | FO | Advance (عمومي) |
| **POT** | FO | Pot Money / petty-type |
| **City Ledger** | POS-REP (تعريف حرفي!) | «bills of the Guest are **debited to his Company**» — جسر AR |
| **Credit** | POS-REP (تعريف حرفي!) | «settlement **other than Cash, Void, Complimentary and NC**» |
| **Staff** | POS | تسوية موظفين |
| **others** | POS | النوع الخامس في 132 عموداً |
| **(V)/(C)** | POS | علامات Void/Cancelled على أرقام الفواتير — مثل 974(V) |
| **NC** | POS/BNQ/MEM | Non-Chargeable/Complimentary family — «ليست مبيعات» (قاعدة Invariant) |
| CGR | SLM/MEM | **C**orporate/**G**roup **R**ate? — شركة/مجموعة (عائلة مقابل NON-CGR) |

## 3. أزمة تسميات التحليل المالي (C-FB-01 + FAS)

| المصطلح المرادف | السياق | الحسم |
|---|---|---|
| Standard Cost ↔ Recipe-based | FNB-LUK ص12 ↔ FNB-REP ص22 | **Standard = من الوصفة** (المتن حاسم — C-FB-01) |
| Actual Cost ↔ Consumption-based | نفس | **Actual = استهلاك مراكز التكلفة** |
| **Sl. Name** / **SL#** / Sub Ledger / Sub | FAS-REP §4/§25 · TEL-LUK | غموض ثلاثي: Serial-Line؟ مرادف Sub Ledger؟ — UNK-053/102 يُحسم بالماستر |
| **Trial** ↔ Trail | MGT-REP §23 + FAS-REP §33 | خطأ إملائي **منسوخ عبر وحدتين** (دليل القوالب L8) — الصواب Trail |
| **Transfer** ↔ Extension | TEL (تحويل غرفة مقابل تمديد إقامة!) | أزمة داخل وحدة واحدة — يفصل المصطلحان |
| **deference value** ↔ difference | FAS-REP §16 | خطأ تحريري (C-FA-03) |
| Sun Cost Center ↔ **Sub** Cost Center | MGT-REP §16 | خطأ تحريري |

## 4. تسميات الوحدات المتبدلة

| المصطلح | المصدر | المقصود |
|---|---|---|
| **Conferencing** | SLM-PRF ص9 (قائمة مستهلكي Company Profile) | الأرجح مرادف BNQ (Banquets & Conferencing) — UNK-052 |
| **Gift Shop** | FO/BNQ | ليس وحدة — **مخزن+منفذ POS** (UNK-024: Outlet Code = Store Code!) |
| **Enterprise 2.0** ↔ **6i** | FOM-SMS + ACR-RPL ↔ الحزمة كلها | إصداران — 6i هو المرجع (C-FO-02) |
| **FORTUNE CARE v6** | Care (أغلفة VER 10 AUGUST + REVISION 1 Aug 2013!) | تضارب إصداري ثلاثي |
| **Front Office System (FOS?)** | FAS-REP §20 | غير معرَّفة — الأرجح POS |
| **Asset Issue Gate Pass** | GTP متن §1 (vs TOC) | بقايا وحدة أصول مدمجة تاريخياً |
| **Non Employee** | HRP | بلا تعريف (GAP-HR-D07) |

## 5. اختصارات الحزمة (Acronym Dictionary)

### 5.1 المستندات والمعاملات

| الرمز | الوحدة | المعنى |
|---|---|---|
| KOT | POS/BNQ | Kitchen Order Ticket — طلب المطبخ |
| BEO | BNQ | Banquet Event Order |
| FP | BNQ | Function Plan/Prospectus? — وثيقة الفعالية |
| GRN | MGT | Goods Receipt Note |
| SPO | MGT | **Single/Simple Purchase Order** (شراء مباشر) |
| PR / Indent | MGT | Purchase Requisition |
| DPR | MGT | Daily Purchase Requirement (محرك nil-balance الآلي) |
| PO | MGT | Purchase Order |
| PJV | MGT-REP/FAS-REP | **Purchase Journal Voucher** (استنتاج — UNK-092: Regular/Service) |
| SOA | ACR | Statement of Account |
| PDC | FAS | Post-Dated Cheque (مستقبلي) |
| JV | HRP/FAS | Journal Voucher |
| Reg Card | FO | Guest Registration Card |
| C-Form | FO | Indian statutory (الشرطة/الضرائب) |
| RLM | FO | RBI-Ledger? Money encashment |

### 5.2 المحاسبة والمالية

| الرمز | المعنى |
|---|---|
| GL / CoA | General Ledger / Chart of Accounts |
| AR | Accounts Receivable |
| TDS | Tax Deducted at Source (جناح هندي ×7 نماذج) |
| PAN | Permanent Account Number (عتبة INI 137) |
| WDV / SLM | Written Down Value / Straight Line Method (إهلاك — INI 475) |
| TB / PL / BS | Trial Balance / Profit & Loss / Balance Sheet |
| CC | Cost Center |
| YTD | Year-to-Date (ضحية XOR 80/132 في FO!) |
| Lakh/Million | أنماط عرض الأرقام الهندية (user reports 6-value matrix) |

### 5.3 التشغيل الفندقي

| الرمز | المعنى |
|---|---|
| ARR | Average Room Rate |
| Occ | Occupancy |
| ADT | Average Daily Traffic? (مقابل ADR القياسي!) |
| MM Class | Menu Mix Class (Menu Engineering) |
| FSN | Fast/Slow/Non-moving (تحليل حركة المخزون) |
| ABC | Activity-Based Classification (Pareto بعتبات A/B) |
| PM | Preventive Maintenance (MNT — بLag وMust-Complete-By) |
| AMC | Annual Maintenance Contract (MNT Equipment) |
| ED | Earnings/Deductions (محرك HRP الرباعي: Normal/Cumulative/Step-Over/Eligibility) |
| F&F | Full & Final settlement (HRP) |
| ESI/PT/LWF | Indian statutory (شرائح PYINDSP) |

### 5.4 البنية والتقنية

| الرمز | المعنى |
|---|---|
| FN6i | Fortune Next 6i — هوية الحزمة |
| PMS | Property Management System |
| EPABX | الهاتف المكتبي (TEL — Serial + Conversion Program ≤7) |
| KDS | Kitchen Display System (شبح POS-REP §24) |
| IVR | Interactive Voice Response (Care — صندوق أسود) |
| MA | Module Attribute (سبع عائلات) |
| INI | ملف التهيئة (من N6IRPRP.BAS!) |
| 80/132 | عرض الطباعة بالأعمدة (عائلة متقلبة §3.7) |
| Pgm.ID | معرف برنامج الطباعة في FAS-SET §15 |
| Program IDs | FOMRR## (اصطلاح FO-REP) |

---

## 6. معجم الأنماط الدلالية (Semantic Patterns)

> عبارات تكررت عبر الوحدات وتحمل معنى اصطلاحياً ثابتاً — فُكّت شيفرتها هنا:

| العبارة الحرفية | المواضع | الدلالة الموحدة |
|---|---|---|
| «**etc.**» بعد قائمة قيم | NC/Session/Menu (FNB) · Event (BNQ) · Asset status (FXD) | قائمة مفتوحة بلا جرد = ماستر غير موثق الموطن |
| «**displayed**» بلا شاشة | KOT-28/Settlement-15 (BNQ) | قوائم يستدعيها كود بلا توثيق |
| «**as explained in the section**» | FAS-REP TB (3.3) | إحالة ذاتية = نسخ كتالوغي |
| «**will be provided later**» | FXD (بطاقة ائتمانية) | وعد مستقبلي بلا مواصفة (عائلة 3.18) |
| «**Not Applicable**» لحقول معروضة | SYS (Card File Drive) | حقل ميت — إرث واجهة |
| «**carefully... Else, there could be functionality issues**» | SYS (INI editing) | تحذير تشغيلي من العبث بالتكوين |
| «**details will appear... NOT be included in the grand total**» | POS-REP ×25 | Invariant مصفوفة Report Options |
| «**This mandatory report**» | FO-REP (Occupancy Statistics) | الوحيدة الموصوفة بالإلزامية في 65 ملفاً |
| «**applicable only for Indian Government**» | POS-REP (INI 137/PAN) | محدد نطاق امتثال |

---

## 7. قواعد الاستخدام عند التنفيذ

1. **ممنوع نقل مرادف بلا تحويله للاسم الموحد** من هذا الجدول (مثلاً: لا يُكتب FOS أبداً — يُكتب FOM).
2. كل رمز من §5 يُعرَّف عند أول استعمال في أي مستند جديد بمرجع هذا الملف.
3. الأخطاء الإملائية الأصلية (Trial/deference/Sun) تُنقل بالصحيح مع توثيق الأصل في `contradictions.md` فقط.
4. المصطلحات المحجوزة للقرار (UNK مرتبطة): Sl. Name · SL# · Non Employee · Conferencing — لا تُستعمل قبل حسمها.
