# 08 — التقارير (Reports) — وحدة FAS

> **FAS-REP مكتمل الآن (Phase 7/الجلسة 18 — خاتمة الحزمة 65/65)** ووُثّق في **[`docs/reports/financial-accounting/`](../../reports/financial-accounting/)** — هذا الملف يحتفظ بجرد LUK/SET/TRN فقط.

---

## 1. الاستعلامات الحية (FAS-LUK — راجع `09-lookups.md` للتفاصيل)

| التقرير/الاستعلام | الخصائص الموثقة | المصدر |
|---|---|---|
| **Ledger Balance** | FY (F3) + Account/SL → أرصدة + تفاصيل المعاملات بالنarration | FAS-LUK §1 |
| **Day Book (Q)** | شهري → يومي → معاملة → **تعديل مباشر** | FAS-LUK §2 |
| **Trial Balance** | Main → Sub drill-down + Modify Column | FAS-LUK §3 |
| **Profit and Loss** | Drill-down ثلاثي + Modify Column | FAS-LUK §4 |
| **Balance Sheet** | Drill-down + Modify Column | FAS-LUK §5 |
| **Payable Outstanding** | FY + حساب/كل الموردين → تفاصيل فواتير + aging + drill للمعاملة | FAS-LUK §6 |
| **Cash Flow Query** | تدفقات بين تاريخي ميزانية؛ Main/Sub head drill؛ أعمدة قابلة للتعديل | FAS-LUK §8 |
| **Transaction Search** | معايير متعددة (≥ مبلغ، Bill#، تاريخ) + Grand Total + Ctrl+F | FAS-LUK §9 |

## 2. تقارير الإعداد (FAS-SET)

| التقرير | المصدر |
|---|---|
| **Create User Reports §17** — مصمم تقارير MIS كامل: Report# (3 رقم، Copy Report)؛ أساس Account Code/CC/Dept؛ 80/132 عموداً (حتى 18 عموداً)؛ **Group Definition** (Normal/Computed/Header؛ Income/Expense/None؛ Percentage؛ Line/Hide/**Page Break**/Sign Reverse؛ أسهم الإزاحة)؛ **Group Linking** (Normal→Computed)؛ **Formula Definition** (Column: Normal/Percentage/Description/Computed + Variance/Hide)؛ **Item Details**؛ **Report Linking** (تجميع تقارير متعددة في تقرير MIS رئيس — مثال موثق: A/B/C منافذ → D الإجمالي) | FAS-SET §17 |
| **Trial Balance Print Order §21** — ترتيب العرض والطباعة (مع SYS Switches 1/2) | FAS-SET §21 |
| **Pre Defined Narration §20** — مساعد إدخال لا تقرير | FAS-SET §20 |

## 3. تقارير مشتقة موثقة الناتج

| التقرير | الموثق | المصدر |
|---|---|---|
| Bank Reconciliation Query/Report | أساسه الوسم realized/unrealized | FAS-TRN §3 |
| **Form 16A (TDS)** | من TDS Tagging (Bank+Challan دقيقة) | FAS-TRN §6 |
| User Defined Reports (Budget vs Actual) | أنماط Apportion/Fixed مع Actuals آلية | FAS-SET §19 + FAS-TRN §4 |
| Room Statistics | من Statistics Master (Rooms Available/Sold S/D/T/Guests/Beds) + Statistics Transaction | FAS-MST §2 |
| Payable/Receivable Aging | من Specify Aging (راجع AR Setup) | FAS-SET §26 |

## 4. FAS-REP (مكتمل — Phase 7/الجلسة 18)

قُرئ كاملاً (64 ص/858 سطر — 48 بند TOC = 46 تقريراً + **شبحان ختاميان**) ووُثّق في **[`docs/reports/financial-accounting/`](../../reports/financial-accounting/)** (12 ملفاً 00→11).

**أهم ما أضافته قراءة REP لهذه الوثيقة:**

| الإضافة | الشاهد | التفصيل |
|---|---|---|
| **طبقة النزاهة التكاملية** — Unlinked/Linked/Auto-Posted | 19/20/21 | `reports/financial-accounting/06` — أسماء معاملات الربط المسربة (Link FOM/POS/Exmp Tax to Finance · Vendor Tax Split) + أنواع الترحيل FOM/ACR/INV — **يغلق البعد التشغيلي لعائلة جسور F من جهة المستهلك** |
| **Print Forms بFAS نفسها ×3** (Balance Confirmation · Advice/Cheque · Voucher Print بنمط تسجيل ضد Transaction Codes) | 14/24/25 | القسم 2 أعلاه (Create User Reports §17) يتصل الآن بأخواته الأربع |
| **TDS جناح كامل** (16A بNew/Reprint + أرباع ×4 + Email-بOutlook/Broadgun + Height 11/12 + 26J/27/26A/26C/26K) | 26-31 | `reports/financial-accounting/08` — يُكمل TDS Tagging/TRN §6 أعلاه |
| **Trial Balance ×4** (بXOR 0/132 · Sub group/Dept/CC تسلسل) | §9 | يوسّع LUK-TB (أعلاه) بوضعيات الإخراج |
| Day Book Format 2 = Contra (بمثال A008000/SBI حرفياً) | §4 | أغنى مثال مصرفي في الحزمة |
| **Invoice/Payment Check يُكمل Three-Way Match** (مع MGT-10 Supplier Bill) | تحت §25 | `reports/financial-accounting/09` §5 |
| Voucher Print ببرامج لكل Transaction Code + طابعة افتراضية محطية | §25 | نمط Print Forms الثاني (مقابل قائمة MGT) |
| شبحا الختام: **IDS Crystal (متكرر مع FO!) + iDesigner** | TOC تحت §34 | UNK-096 — يوصل عائلة TOC-template لأقوى دليل |

## 5. المعلق — **لا شيء (خاتمة الحزمة)**

65/65 ملفاً مقروءاً عميقاً — لا ملفات معلقة بعد الآن. المرحلة التالية: Phase 8+ (المراجعة الشاملة).
