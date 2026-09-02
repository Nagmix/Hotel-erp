# 08 — التقارير (Reports) — وحدة FAS

> **FAS-REP (~858 سطراً مستخرجاً) مؤجل للقراءة العميقة في Phase 7.** هذا الملف يجرد التقارير الموثقة في LUK/SET/TRN فقط.

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

## 4. المعلق

`[PENDING DEEP READ]` FAS-REP: كتالوج التقارير الرسمي الكامل — Phase 7 (`docs/reports/`).
