# 12 — التكاملات (Integrations) — وحدة System Setup

> I-SYS-01..18 — SYS هو **أكبر مورّد تكامل في النظام**: كل وحدة تستهلك مرجعياته. التوثيق هنا بالاتجاه (SYS → المستهلك) مع عكسها عند الحاجة.

---

| ID | التكامل | الاتجاه | المحتوى الموثق | المصدر |
|---|---|---|---|---|
| **I-SYS-01** | SYS → FO: FO Defaults | PUSH مرجعي | 14 قيمة افتراضية (Property/Room Type/Currency/Market/Source/Nationality/Plan/DFC/CheckIn/RateTable/TimeDiff/BillingInstr/PayMode) — "displayed in the respective menu options only after the settings are defined" | ص25-31 |
| **I-SYS-02** | SYS → FO/POS: Tax engine | PUSH حسابي | Codes (Applicable To) + Slabs + Structures تستهلكها عمليات البيع | ص71-83 |
| **I-SYS-03** | SYS → FO/POS/BQT/Purchase: Credit Cards + Floor Limits | GATE | "validates... during settlement of Room, Point of Sale and Banquet bills" + واجهة أجهزة online authorization | ص93-94 |
| **I-SYS-04** | SYS → كل الوحدات: Currencies + Exchange | PUSH قيمي | العملات (10 حقول) + أسعار (≤4 زمنية) — AR يثبت سعر تاريخ الفاتورة | ص64-71 |
| **I-SYS-05** | SYS → الأقسام/التكاليف | PUSH تنظيمي | Departments (فلتر General/Banquet) + Cost Centers | ص46-53 |
| **I-SYS-06** | SYS → HR&P + FO: Designations | PUSH تصنيفي | Guest Type (Guest→FD · Others→HR · S&M→SLM) — **كيان واحد ثلاثي الخدمة** | ص53-55 |
| **I-SYS-07** | SYS → POS/MM/FNB: UOM | PUSH قياسي | "mainly used in the Point of Sale, Materials Management and F&B costing" | ص57 |
| **I-SYS-08** | SYS → 9 وحدات: Reason Codes | PUSH إلزامي | التبرير الإلزامي للإلغاء/الخصم/الإعفاء — Banquets/Finance/FO/**Gift Shop**/Laundry(s)/Membership/POS/Purchase/Sales | ص60-61 |
| **I-SYS-09** | SYS → FO+POS: Guest Comments | PUSH استطلاعي | تقييمات Guest Survey Template (1-25 نظامية + 26+) | ص83-86 |
| **I-SYS-10** | SYS → FO/AR/Laundry: Program IDs + Printer Ports | PUSH إخراجي | 7 خانات + LPT/COM/USB — جدول 20+ نموذجاً قياسياً | ص86-93 |
| **I-SYS-11** | SYS → FO/POS: Print Bill Message | PUSH تسويقي | From/To/Subject/Outlets/Message على الفواتير | ص96-99 |
| **I-SYS-12** | SYS → HR&P/FO: Religions + Occupations | PUSH بياناتي | "HR Payroll Master and Guest History" / "Guest and Staff details" | ص99/103 |
| **I-SYS-13** | SYS(Supervisor) → سلوك كل الوحدات | SWITCH | Module Attributes + INI (المفاتيح المرقمة المبعثرة: FO 1-67 · POS 6/29/32 · INI 56/58/64/74/283/404/504 · FAS Sw4 · INV 1/3/4) | ص31-33/36-37 |
| **I-SYS-14** | SYS → كل التقارير: Report Restrictions + Engine | GATE إخراجي | Spool/Export/Format لكل تقرير لكل مستخدم | ص17-19 |
| **I-SYS-15** | SYS → UI: Captions + Menu/Graph personalization | PUSH عرضي | إعادة تسمية القوائم والتقارير + داشبورد (≤3 programs/3-5 graphs) | ص23-24/15-17 |
| **I-SYS-16** | SYS ↔ مزود الخدمة: Extract DB + GUI .dat | PULL تشخيصي | "system analysis, trouble shooting and maintenance by your authorized service provider" + PR series | ص33-36 |
| **I-SYS-17** | SYS → AR: Property-level Round Off | PUSH تعديلي | تقريب فواتير الخروج — لكن AR bills تستعمل سلوكها الخاص [UNCERTAIN تفاصيل تطبيقه على AR] | ص42-45 |
| **I-SYS-18** | SYS → قاعدة البيانات: History Tables | DB | جداول MMYY قبل التاريخ الجاري + النسخ .INS | ص33-34 |

## رسالة التكامل المعمارية

**SYS = طبقة المرجعية الزمنية (Applicable From) + طبقة الصلاحيات المظلية + طبقة المفاتيح السلوكية.** كل وحدة تعمل فوقها. في البنية الجديدة (Frappe): مرجعيات SYS = **DocTypes أساسية seeded قابلة للتوسيع** — راجع `16-erpnext-mapping.md`.

> **Gift Shop**: ظهرت كوحدة هدف لـ Reason Codes [UNCERTAIN] — لا دليل مستقل في الحزمة (لا manuals) — يُرجَّح أنها منافذ POS متخصصة أو وحدة قديمة؛ يُسجل في unknowns.
