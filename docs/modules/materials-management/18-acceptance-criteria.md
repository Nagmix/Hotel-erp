# 18 — معايير القبول والدخان (Acceptance Criteria & Smoke Test) — وحدة Materials Management

> مجموعات القبول AC-MG-01..10 + **Smoke Test تنفيذي من 28 خطوة**. كل معيار قابل للتحقق من التوثيق أعلاه (Traceability: AC ← BR/V/WF).

---

## 1. مجموعات معايير القبول

### AC-MG-01 — التأسيس (Stores/Items/OB)

| # | المعيار | التتبع |
|---|---|---|
| 1.1 | إنشاء Main + Sub + Independent والتحقق من قيد "Sub يستلم من Main فقط" | BR-MG-01/V-MG-03 |
| 1.2 | اختيار WA لمخزن وFIFO لآخر — **التقييم خاصية مخزن** يتوقف بعد الحفظ | BR-MG-02/F-MG-1 |
| 1.3 | حذف/تعديل Store مرفوض؛ Passive + بديل يعمل | EC-MG-01 |
| 1.4 | Item Code رقمي ≤12 مرفوض بتكرار عبر المخازن | V-MG-08/09/10 |
| 1.5 | Sub Code مرفوض عند تطابق UOMs | V-MG-11 |
| 1.6 | Opening Balance: Gr.Date تصاعدي + Value تلقائي + **يقفل بعد أول معاملة** | V-MG-37/BR-MG-10 |
| 1.7 | Reorder Level/Qty لكل صنف×مخزن (مطابقة Item Reorder) | 16-erpnext §1.9 |

### AC-MG-02 — دورة الطلب والتفويض

| # | المعيار | التتبع |
|---|---|---|
| 2.1 | PR يدوي + آلي (Re-Order)؛ Request# تلقائي | 10-trans §4 |
| 2.2 | INI 355=2 → إصدار مرفوض قبل تفويضين **تسلسلياً** | BR-MG-05/V-MG-31/32 |
| 2.3 | Indent بثلاثة أنماط (Adhoc/Template/Repeat) وأعمدة CC | WF-MG-04 |
| 2.4 | Close Indent/PR يعمل (يدوي/تلقائي) | WF-MG-03/04 |
| 2.5 | DPR يولد عند Nil balance وينعكس في Receipt | A-MG-02/EC-MG-08 |

### AC-MG-03 — دورة العطاءات

| # | المعيار | التتبع |
|---|---|---|
| 3.1 | السبع وظائف كاملة (Invite→Close) برقم عطاء | WF-MG-05 |
| 3.2 | Tender Form قابل للطباعة بالبيانات تلقائية | 08-reports §1 |
| 3.3 | Close بReason إلزامي | WF-MG-05.7 |

### AC-MG-04 — الشراء (PO/SPO/SWO)

| # | المعيار | التتبع |
|---|---|---|
| 4.1 | PO: دمج PR + Copy PO + Consolidate Discount% + Other Details (9 حقول) + Misc Tax | WF-MG-06 |
| 4.2 | SPO: نطاق صلاحية + **Fixed (بلا خصم) مقابل MRP (خصم)** | BR/V WF-MG-07 |
| 4.3 | SPO يعمل فقط عند المفتاح النصي "In Receipt / PO Indent is not mandatory"=Yes | V-MG-34 (مع GAP-MG-D01 توثيقياً) |
| 4.4 | SWO: Cancel/Close بReason + تأكيد | WF-MG-08/EC |
| 4.5 | تفويض PO متعدد المستويات فعّال (F-MG-3 موحد) | 07-permissions §2 |

### AC-MG-05 — الاستلام (Receipt)

| # | المعيار | التتبع |
|---|---|---|
| 5.1 | الأنماط الثلاثة + تحميل المورد تلقائياً لـ Contract/PO | WF-MG-09 |
| 5.2 | قواعد GR الزمنية الثلاث مفروضة | V-MG-21/EC-MG-18/19 |
| 5.3 | Bill#/Date إلزام عند المفتاح + **جسر Payment Match** | V-MG-22/E-MG-14 |
| 5.4 | Batch# إلزام عند تكرار الصنف + Expiry ≥ اليوم | V-MG-23/24 |
| 5.5 | Complimentary بلا Rate/Tax | BR-MG-06.4 |
| 5.6 | Misc Tax: عملة مختلفة → Amount فقط | V-MG-25/EC-MG-32 |
| 5.7 | Other Details (Gate/Rejected/Transport) + Images | WF-MG-09.6 |
| 5.8 | Cost Center/SubStore لNon-Stockable/Cash/Main فقط | V + 06-validations §4 |

### AC-MG-06 — الإصدار والمرتجعات والتسويات

| # | المعيار | التتبع |
|---|---|---|
| 6.1 | Issue Direct: رصيد اليوم + توزيع Batch تصاعدي (FEFO) + Rate تلقائي | WF-MG-10/A-MG-05 |
| 6.2 | Issue Indent: ضد طلبات مفوضة + DPR عند الصفر | WF-MG-11 |
| 6.3 | Receipt Return يحمل كل حقول GRR تلقائياً | WF-MG-12 |
| 6.4 | Issue Return: GRR/Batch مطابقة + Indent# 3-10 | V-MG-27 |
| 6.5 | Adjustment ± Qty/Value + Zero balance + Type للسالب فقط | WF-MG-13/EC-MG-10/11 |

### AC-MG-07 — التحويلات والتحويل التصنيعي

| # | المعيار | التتبع |
|---|---|---|
| 7.1 | Inter/Sub Store بنطاق صحيح + الأعلام الاتجاهية محترمة | BR-MG-03/08/EC-MG-14 |
| 7.2 | Conversion: نفس المخزن + Yield≤100 + To=From + Component Cost يضاف | V-MG-19/20/30 |
| 7.3 | Butchery Split (مثال الدجاج) يعمل | WF-MG-16 |

### AC-MG-08 — الشهر الختامي (الأهم）

| # | المعيار | التتبع |
|---|---|---|
| 8.1 | Physical Stock: مساران (Independent/Group) + Date < الخادم + Variance view | WF-MG-17/V-MG-35 |
| 8.2 | Variance Update: **تنبيه "هل راجعت تقرير الفروقات؟"** + Adjustment آلي + السالب → Variance CC | WF-MG-18/A-MG-09 |
| 8.3 | Process Ledger: تجميد ما عدا الحالي + **Cancel ثم إعادة** يعمل | BR-MG-09/EC-MG-04/05 |
| 8.4 | Stores Ledger قابل للطباعة بعد المعالجة | 08-reports |

### AC-MG-09 — الصلاحيات

| # | المعيار | التتبع |
|---|---|---|
| 9.1 | البعد Store: مستخدم لا يرى إلا مخازنه | 07 §1 |
| 9.2 | البعد Option + F2 تبديل جماعي | 07 §1 |
| 9.3 | البعد Dept/CC قوائم Authorized | 07 §1 |
| 9.4 | **البعد Backdate: نافذة أيام لكل نوع معاملة مُفروضة بالتحقق** | F-MG-4/V-MG-38 |

### AC-MG-10 — البيانات المرجعية والتحليلات

| # | المعيار | التتبع |
|---|---|---|
| 10.1 | Vendor 7 خانات = Type(FO)+4 + 7 عائلات + 5 شرائح خصم + 9 أيام ثابتة | 01 §9 |
| 10.2 | VendorItem: Last Rate يتحدث تلقائياً عند استلام Normal | A-MG-03 |
| 10.3 | Budget Fixed/Apportion + F2/F4 | BR-MG-15 |
| 10.4 | FSN بقيد Fast>Slow | V-MG-18 |
| 10.5 | 20 استعلاماً بالفلاتر + Drill-down الثلاثي + Print | 09-lookups |

---

## 2. Smoke Test التنفيذي (28 خطوة)

**التأسيس:**
1. إنشاء Store (WA) + Store (FIFO Sub) + Independent → ✅AC-1.1
2. Group + Item Stockable + Item Cash Purchase + Reorder Level → ✅AC-1.4/1.7
3. Stores Start Date + OB بدفعتين (Batch) → ✅AC-1.6
**الشراء:**
4. PR يدوي → Auth 1 → 2 (INI 355=2) → محاولة إصدار قبل التفويض **مرفوضة** → ✅AC-2.2
5. Quotation Cycle كامل → ✅AC-3.1/3.3
6. PO من PR + Misc Tax 5% → ✅AC-4.1
7. SPO (MRP مع خصم) → ✅AC-4.2
**الاستلام/الإصدار:**
8. Receipt PO (GR<PO date **مرفوض**) → سليم + Bill# + Batch مكرر **مرفوض بلا Batch** → ✅AC-5.2/5.3/5.4
9. Receipt Contract بعد انتهاء العقد **مرفوض** → ✅AC-5.2
10. Receipt Complimentary (بلا ضريبة) → ✅AC-5.5
11. Issue Indent → توزيع FEFO + صنف صفر → DPR → يظهر في Receipt جديد → ✅AC-6.1/6.2/2.5
12. Receipt Return جزئي على GRR → ✅AC-6.3
13. Adjustment سالب بلا Type **مرفوض** → ✅AC-6.5
14. Conversion Split (دجاج→2 منتجات Yield 90%) + Component Cost → ✅AC-7.2/7.3
**الشهر:**
15. Physical Stock (مجموعة) → 16. Variance (تنبيه التقرير) → 17. Process Ledger → 18. تعديل شهر معالج **مرفوض** → 19. Cancel → تعديل يعمل → إعادة معالجة → ✅AC-8.1-8.3
**الصلاحيات:**
20. مستخدم محصور بمخزن واحد → ✅AC-9.1 · 21. Backdate خارج النافذة **مرفوض** → ✅AC-9.4
**التحليلات:**
22. Re-Order Process (رصيد ≤ Level) → PR آلي → ✅A-MG-01 · 23. L17 Drill-down 3 مستويات → ✅AC-10.5 · 24. Spending Pattern سنة/سنة → ✅ · 25. VendorItem Last Rate تحديث تلقائي → ✅AC-10.2 · 26. Budget Apportion + F2/F4 → ✅AC-10.3
**الحوكمة:**
27. Purge PO انتقائي (checkbox) → ✅BR-MG-16 · 28. Authorization Details Lookup يعرض التفويضات → ✅07 §2.4

---

## 3. عتبة الجودة للانتقال للوحدة التالية

- ✅ كل AC مرتبطة بتتبع موثق (48 معياراً)
- ✅ Smoke Test يحاكي القواعد الرفض/القبول الحرجات (14 حالة رفض مغطاة)
- ⬜ تحقق QR-6 (مراجعة المعايير مع FAS Payment Match) — مؤجل لPhase 6 عمداً (توقيت الترحيل GAP-MG-D04)
- نقطة الاستئناف القادمة: **BNQ (الولائم — 5 ملفات/255 ص) ثم HRP** وفق module-inventory §5.
