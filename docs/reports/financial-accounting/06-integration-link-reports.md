# 06 — طبقة النزاهة التكاملية (Integration Link Reports) — FAS-REP (Phase 7)

> §18 Pending Receipts for PJV + §19 Unlinked Account Codes + §20 Linked Account Codes + §21 Auto Posted Check List = **أهم 4 تقارير في المرحلة 7 كلها** — مستوى meta: تقارير **تُدقّق الجسور بين الوحدات**.

---

## 1. §19 Unlinked Account Codes — **فاحص اكتمال الجسور**

**الوصف الحرفي:** "generate a list of all **Revenue Codes, Item groups and Tax Codes related to the Front office, Point of Sale and Purchase modules that are not linked to financial Account Heads** in the following parameters: FO to Finance Defn. / POS to Finance Defn. / Pur Tax link to Finance / Vendor Tax link to FA. **Using this list, you can define Account Heads accordingly so that all figures related to Sales (Income) and Purchase Journals are accurately reflected in the General Ledger**."

**الأنواع الأربعة (كما تُفصّل ص40-41):**

| النوع | ما يعرضه |
|---|---|
| **FO to Finance Defn** | "all **Revenue Types** that are not linked to Account Heads in the **Link FOM to Finance parameter**" |
| **POS to Finance Defn** | "**Restaurant wise Item Groups** Codes and Names that are not linked to Account Heads in the **Link POS to Finance parameter**" |
| **Pur Tax link to Finance** | "**Tax codes pertaining to Purchase** that are not linked to Account Heads in the **Link Exmp Tax to Finance parameter**" |
| **Vendor Tax link to FA** | "**Tax Codes not tagged to Vendors** in **Vendor Tax Split parameter**. Tax Codes along with the Vendor Codes and Names" |

**النقاط البنيوية الكبرى:**
1. **هذا هو الفاحص التشغيلي لعائلة جسور F** التي وثّقها المشروع عبر 17 وحدة — التقرير يجيب: "أي كود إيراد/صنف/ضريبة **يضيع ترحيله** لأن الربط غائب؟".
2. **أسماء معاملات الربط الرسمية المسربة** (4!): Link **FOM** to Finance · Link **POS** to Finance · Link **Exmp Tax** to Finance · **Vendor Tax Split** — **رابع بنية ربط مكتشفة** بعد ماستر الربط في FO/POS/شراء — و**Exmp** (Exempt!) — ضريبة معفاة لها ربط خاص!
3. **POS-ربط بمستوى Restaurant×Item Group** — أعمدة الترحيل: المنفذ×المجموعة (نفس عمق MGT Group-Value).
4. **Vendor Tax Split** — توزيع ضريبة المورد (ضريبة على مستوى المورد — شبيكه Split الضرائب المركبة).

## 2. §20 Linked Account Codes — الوجه المكتمل

"list of all Revenue Codes, Item groups and Tax Codes related to the Front office, Point of Sale, Purchase modules and Property that **are linked** to financial Account Heads in: **Sub Ledger / FOM to FA / FOS to FA**."

- **الاختلاف الاصطلاحي الصارخ مقابل §19**: "POS to Finance Defn" (19) ↔ **"FOS to FA"** (20) — نفس الجسر باسمين مختلفين (**FOS** = Front Office System؟ POS؟ — **حديقة تسميات**: FO / FOM / FOS / POS / FA / Finance) → **C-FA-01**.
- **Sub Ledger** كنوع ربط ثالث هنا (الربط عبر SL) — القائمة المرتبطة أوسع (بما فيها SL والملك).
- الغرض: **توثيق الربط القائم** (عكس 19) — ثنائية فاحص/سجل تكامل كاملة.

## 3. §21 Auto Posted Check List — **خريطة الترحيل الآلي الرسمية**

**الوصف الحرفي:** "generate a list all transactions that are **auto posted from other modules i.e., Front Desk, Point of Sales, Accounts Receivable, Materials Management etc** to the financial management module. Auto posted transactions will be reflected in this report **only if the links between the front office and financial module is established accurately**."

**أنواع الترحيل الثلاثة (حرفياً):**

| Type | المصدر |
|---|---|
| **FOM** | "transactions auto posted from **Front Desk and Point of Sale modules**" — الاثنان تحت نوع واحد! |
| **ACR** | "transactions pertaining to **Accounts Receivable**" |
| **INV** | "transactions pertaining to **Materials Management module**" |

- **80 أو 132 column sheet** — خيار العرض العريض هنا أيضاً.
- **القيد الشرطي الموثق**: الانعكاس "only if the links... established accurately" — **الترحيل الآلي معلّق بالربط** (نفس قانون 19/20 — النزاهة شرط عمل لا مجرد فحص).
- **الفجوة الحاكمة: HRP غائب!** — أنواع الترحيل FOM/ACR/INV فقط — **لا يوجد نوع Payroll** رغم أن HR-PNT (ماستر ترحيل الرواتب) وثّق قيوداً → إما أن رواتب HRP تُرحَّل **بمسار غير آلي** (قسائم يدوية!) أو بنوع غير موثق → **UNK-098** (يلامس UNK-010 القديم من أصل المشروع!) — وكذلك **FXD** (ترحيل الإهلاك شهرياً بنهاية الشهر — F12 موثق!) غائب عن الأنواع → الأنواع الثلاثة **غير شاملة** (الترحيلات من FXD/FNB/SLM/Care/MEM إما يدوية أو مدمجة).

## 4. §18 Pending Receipts for PJV — **طابور GRN→قسيمة**

**الوصف:** "generate a list of all **Grrs that are not posted to the Purchase Journal Voucher**. The Pending Grrs can be viewed on the basis of **Regular or Service PJVs** for All or specific Vendors."

| # | المعيار |
|---|---|
| 1 | **Pending أو Tagged GRN** + **Regular أو Service PJV** |
| 2 | All vendors / selected (نطاق) |
| 3 | Date range — **"Date entered should be less than or equal to the Current System Date"** |
| 4 | **Misc. Supplier Group Summary Required** — "consolidated summary of all **Miscellaneous Vendors**" |
| 5 | Print Sequence: **Vendor Wise / GRN Wise / Doc Date Wise** |

**النقاط البنيوية:**
- **PJV نوعان**: Regular و**Service** — قسيمة مشتريات خدمية (بدون بضاعة — تقابل SWO في MNT/MGT!) — ثنائية قسيمة موثقة.
- **Misc. Supplier Group** — فئة موردون متنوعون (تجميع خاص لهم) — ماستر مورد فئوي.
- **ثلاثية Print Sequence** (Vendor/GRN/Doc Date) — ترتيب بثلاثة مفاتيح (تقابل PJV-Wise في MGT-24.1 — الآن يتكامل المعنى: الترتيب حسب القسيمة/المورد/التاريخ).
- **GRN لا يرحَّل ذاتياً!** — الترحيل عبر PJV (دورة: GRN (MGT) → [طباعة 15.6 → نسخة Finance] → PJV (FAS) → أعمار (10)) — **PJV هو جسر الاستلام→المحاسبة الرسمي**.

## 5. خريطة النزاهة التكاملية الكاملة (الاكتشاف المركزي للملف)

```
                     ┌── §19 Unlinked ── (ما لم يُربط)
FO ─Revenue──┐       │
POS ─ItemGrp─┼─ Link FOM/POS to Finance ──→ §21 Auto Posted (FOM/ACR/INV)
PUR ─Tax─────┘       │        ↓ قيود GL
                     └── §20 Linked ──── (ما رُبط عبر Sub Ledger/FOM/FOS)
MGT ── GRN ──→ §18 Pending PJV ──→ PJV (Regular/Service) ──→ GL
HRP ──؟── ✕ غائب من §21 (UNK-098)
FXD ── إهلاك F12 شهري ──؟ أيضاً غائب من الأنواع
```

**الاكتشاف التجميعي الأهم في المرحلة 7 كلها:** FAS يملك **طبقة meta-تقارير** — لا تقرر المال بل **تدقّق سلامة انتقاله من كل الوحدات** — وهذا يجيب سؤال "كيف يضمن FN6i عدم ضياع الإيراد بين الوحدات؟" الجواب الموثق: **ثلاث أدوات**: فاحص الجسور المكسورة (19) + سجل الجسور السليمة (20) + كشف الترحيلات الواصلة (21) — **بازل نظامية كاملة** (تُقابل في ERPNext ب"Account Head مطلوب عند الحفظ" — فرق فلسفي: FN6i يسمح بالحفظ بلا ربط ثم يُبلّغ؛ ERPNext يمنع — قرار تحويل D-مهم).
