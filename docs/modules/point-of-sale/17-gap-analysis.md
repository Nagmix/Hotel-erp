# 17 — تحليل الفجوات (Gap Analysis) — وحدة POS

> **D** = فجوات مصدر · **E** = فجوات ERPNext · **عكسية** = فرص يتفوق فيها الهدف.

---

## أ. فجوات توثيق المصدر (D)

| ID | الفجوة | الدليل | الأثر | المعالجة |
|---|---|---|---|---|
| **GAP-POS-D01** | **Taxcode Mapping (§42) بلا متن إطلاقاً** — صفحة فارغة | POS-SET ص122 | غموض ربط الضرائب | `[NOT DOCUMENTED]` — يُستدرك من FAS/SYS أو ميدانياً |
| **GAP-POS-D02** | Server Outlet Mapping (§10) صورتان بلا شرح حقول | POS-SET ص34-35 | بنية الربط غير معروفة بدقة | استنتاج بنيوي (N–M) |
| **GAP-POS-D03** | مرجعية "Print Report Options from **Getting Started** document" (خارج الحزمة) | POS-SET ص69/70 | آلية الطباعة العامة غير موثقة | Print Format في الهدف |
| **GAP-POS-D04** | **أرقام Module Attributes الكاملة للـ POS غير موثقة** (وصلنا 6/29/32 فقط) — "For more information, refer Module Attributes & INI Settings documents" (وثيقة SYS مستقلة خارج الحزمة؟) | POS-SET §15 ص45 | مفاتيح سلوكية كثيرة مجهولة | قراءة SYS-SSP (UNK متبقٍ) |
| **GAP-POS-D05** | الافتراضي (Allow/Deny) لـ POS User Access | §20 | نموذج الأمان | قرار تصميمي |
| **GAP-POS-D06** | سلوك Guest Settlement لغرفة غير موجودة/خارج الضيوف | TS ص36 | رفض غير موثق | تحقق صريح في الهدف |
| **GAP-POS-D07** | الإدخال اليدوي لبيانات CC عند فشل السحب | TS ص34 | ثغرة تشغيلية | خيار احتياطي بصلاحية |
| **GAP-POS-D08** | تسلسل Close Outlet ↔ Day End ↔ Post to Finance | TS + FAS-TRN §G | ترتيب الترحيل | Phase 6 (QA-POS عام) |
| **GAP-POS-D09** | Void KOTs (تحت Billing) — مسار موثق بالاسم فقط | POS-SET §37 ص109 | تفاصيل الشاشة غير مقروءة (POS-REP?) | تُستدرك |
| **GAP-POS-D10** | Tips: أثرها المحاسبي وتوزيعها | TS | حسابات غير معروفة | قرار + HR |
| **GAP-POS-D11** | Account/فهارس POS-REP (158 ص) مؤجلة | Phase 7 | تقارير غير مجردة | قراءة لاحقة |

## ب. فجوات ERPNext (E)

| ID | الفجوة | السبب | المعالجة |
|---|---|---|---|
| **GAP-POS-E01** | **فصل KOT/Bill/Settlement الثلاثي** | POS Invoice يجمع البنود والدفع في مستند واحد | Custom DocType KOT (F-POS-1) |
| **GAP-POS-E02** | **Sessions/Minimum Cover Charge/Applicable days** | لا جلسات فطرية | POS Shift/Session موسع |
| **GAP-POS-E03** | **Tips** (حقول تسوية) | لا native | Custom + سياسة توزيع |
| **GAP-POS-E04** | **Split Quantity الكسري** (0.5) | البنود بأعداد صحيحة عادة | كمية Float (مطاعم تسمح) — تكوين Item UOM |
| **GAP-POS-E05** | **Link Tables + Table Suffix** | لا مفهوم دمج الطاولات | Custom (دمج بنود في فاتورة) |
| **GAP-POS-E06** | **Reprint ⇒ إبطال الرقم وتوليد جديد** | إعادة الطباعة في ERPNext بلا ترقيم جديد | سلوك تسلسلي مخصص (قرار: نقل حرفي أم تحسين؟) |
| **GAP-POS-E07** | **NC بأقسام داخلية/خارجية + NC Cost%** | لا مكافئ مباشر | Invoice صفرية + مصروف NC |
| **GAP-POS-E08** | **Outlet-level Bill Init دورات Y/M/D/N** | Naming عام | Naming Series لكل POS Profile |
| **GAP-POS-E09** | **العملة الأجنبية للمنفذ + Round Off لكل عملة** | POS Profile بعملة واحدة عادة | تكوين عملات متعدد |
| **GAP-POS-E10** | **طابعات KOT المتعددة حسب المطبخ/الصنف** | طباعة واحدة لكل مستند عادة | توجيه طباعة خام لكل بنود المطبخ (Custom) |
| **GAP-POS-E11** | **صلاحيات لكل تطبيق (Regular/Touch/PDA)** | لا أبعاد منصات | منصة واحدة (F-POS-4) يحلها |
| **GAP-POS-E12** | **البحث التقريبي للضيوف** (زيارات/إيراد بمدى) | بحث دقيق فقط | تقارير/بحث مخصص |

## ج. فجوات عكسية (فرص تفوق)

| الميزة | الأصل | الربح |
|---|---|---|
| **POS Opening/Closing Shift** native | مبني يدوياً بالأصل | جاهز ومتين |
| **Loyalty Program** native بنقاط | خصومات ثابتة فقط | برنامج نقاط أقوى |
| **Pricing Rule** (زمنية/عميل/صنف) | Happy Hours + Member + Revenue منفصلة | موحد قابل للتوسيع |
| **User Permissions per POS Profile** | Restrict Outlet Access يدوي | مركزية وأدق |
| **Web-based single responsive app** | 3 منصات منفصلة | صيانة واحدة |
| **Multi-currency Item Price** | تبويبات Local/Foreign | native |
| **طباعة عربية RTL حديثة** | محارف وأدوات قديمة | تحسين جوهري |
