# 12 — التكاملات (Integrations) — وحدة FAS

> FAS هي **مركز التكامل المحاسبي** — كل الروابط موثقة نصاً (راجع `11-accounting-impact.md` للتفصيل المحاسبي الكامل).

---

| ID | التكامل | الاتجاه | المفصل الموثق | المصدر |
|---|---|---|---|---|
| I-FA-01 | **FO → Finance** | FO → FAS | ربط Revenue Types (13 نوعاً) × أكواد الإيراد D/C؛ الترحيل: Post FO to Finance بعد Day End/Open New Date | FAS-SET §6 + FAS-TRN §G |
| I-FA-02 | **POS → Finance** | POS → FAS | Restaurant × Menu Group → D/C (مبيعات Credit، خصومات Debit) | FAS-SET §7 |
| I-FA-03 | **MM → Finance (شراء)** | MM → FAS | Item/Group × Store → حسابات (أصل شراء)؛ GRN → PJV؛ Bill إلزامي | FAS-SET §8 + FAS-TRN §H |
| I-FA-04 | **MM → Finance (استهلاك)** | MM → FAS | Issues → Consumption Posting (شهري/يومي INI 283) | FAS-TRN §J |
| I-FA-05 | **Payroll → FAS** | HR → FAS | ED Codes → حسابات GL (+CC/Dept ثنائي) — إلزامي لترحيل journal | FAS-SET §9 |
| I-FA-06 | **Membership → FAS** | MEM → FAS | Revenue Headings → D/C؛ Post Membership to Finance | FAS-SET §10 + FAS-TRN §K |
| I-FA-07 | **AR → Finance** | AR → FAS | قيود AR تُرحّل فورياً بالحسابات المرتبطة (تعديل F5 ممكن)؛ أنواع Client×Cash/Bank/Others — **مكتمل الآن: راجع `../accounts-receivable/11-accounting-impact.md` (الترحيل التفاعلي عند الحفظ + INI #56=0 شرط التمكين + حسابات Sundry Debtors/Cash/Bank/Commission)** | FAS-SET §11 + ACR-OPR §1 ص10 |
| I-FA-08 | **SYS (Property/CC/Dept/Tax)** | SYS → FAS | Property Codes، Cost Centers، Departments، Tax Codes — مرجع أساسي | FAS-SET عدة أقسام |
| I-FA-09 | **SYS Module Attributes** | SYS → FAS | FAS Switch 4 (FOM to FAS Posting)؛ SYS 1/2 (ترتيب الطباعة)؛ INV 1/4/3؛ Module Attr 9 (TDS) | FAS-SET §11/§21 + FAS-TRN §H/§I + FAS-MST |
| I-FA-10 | **FO ↔ FAS (بالاتجاهين مفاهيمياً)** | ثنائي | Guest Ledger B/F (Credit) وC/F (Debit) — دفتر الضيوف ينعكس في GL | FAS-SET §6 |
| I-FA-11 | **AR (Aging مشترك)** | FAS ↔ AR | Specify Aging يخدم استعلامات/تقارير الوحدتين | FAS-SET §26 |
| I-FA-12 | **Banquets (ضرائب)** | BQT → FAS | نوع Taxes يشمل ضرائب Banquets | FAS-SET §6 |
| I-FA-13 | **طباعة/Prgm** | FAS → Output | Print Forms (Pgm.ID ≤7 + منفذ) لـ MM/FAS/PM/Eng | FAS-SET §15 |

## أنماط تكاملية موثقة (تُعتمد في المعمارية)

1. **نمط الرابط التعريفي (Definition Link):** كل وحدة مُصدِّرة تُعرّف خرائطها الحسابية في FAS-SET مسبقاً؛ الترحيل يقرأ الخريطة (لا حسابات مضمّنة في الشيفرة).
2. **نمط الفروق → Suspense → إعادة معالجة:** أي فجوة تعريف تظهر فرقاً وتُعالج بإعادة الترحيل بعد الإصلاح (لا تعديل مباشر على القيود المرحّلة).
3. **نمط الإيقاع المتدرج:** فوري (AR) / يومي بعد Day End (FO/POS) / عند الطلب (PJV/Payroll/Membership) / شهري أو يومي (Consumption).
4. **نمط القفل المتدرج:** الشهر Audited → العام Open FY → مع الشيك المطبوع (Cancel فقط).
