# كتالوج المعاملات ودورات حياتها (Transactions & Lifecycles)

> **المرحلة:** Phase 1 | المعاملات هنا بمعناها الوظيفي (مستندات أعمال). الحالات الموثقة فقط — لا حالات مخترعة.

---

## 1. حالات المستندات الموثقة حتى الآن

| المستند | الحالات/الأحداث الموثقة | المصدر |
|---|---|---|
| **Reservation** | Make → Amend → Cancel → Re-Instate Cancel → No-Show (Provisional) → Assign Room → Copy → Waitlist (Booking type: Confirmed/Waiting) | FOM-RES فهرس + خطوات |
| **Registration** | Express/Reservation/Walk-in Check-in → Amend Stay → Room Transfer → Cancel Check-Ins → Check-out (Confirm/Pax) | FOM-REG فهرس، FOM-CAS |
| **Folio/Bill** | ترحيلات متتابعة → Print → Settle (جزئي/كلي/معلق) → Folio Re-Instate | FOM-CAS فهرس |
| **Banquet Booking** | Make → Amend → Cancel → No-Show Cancellation → Block → Release → Copy → Browse | BNQ-BOK فهرس |
| **Banquet Bill** | Requirement → Deposit → Pre-Costing → Bill → Settlement → Reprint / Pending | BNQ-BIL فهرس |
| **Membership Application** | Application → Screening → Interview Dates → Interview Details → Transfer → Approve (Master) | MEM-MPF فهرس |
| **Membership** | Active → Renewal / Address Change / Category Transfer / Termination / Resignation / Deceased / Blacklist → Revoke Blacklist | MEM-MMN فهرس |
| **PO (MGT)** | PR → Indent → PO → Receipt → Status (Pending/Cancelled/Closed) | MGT-DNT/LUK فهرس |
| **Task (Care)** | Raise → Assign → Work Start → Close / Transfer / Extend / Cancel / Stop | Care-Ops فهرس |
| **Complaint (MNT)** | Register → Action Taken → (Status Q) | MNT-OPR/RPL فهرس |
| **Voucher (FAS)** | إنشاء → Authorization → ترحيل | FAS-TRN (Voucher Authorization) |
| **Night Audit** | Post Tariff → Guest Balance → Night Balance → [Cancel/Redo] → Open New Date (لا رجوع بعدها) | FOM-DEP كامل |
| **Generic Masters** | Active / Passive (الحالة القياسية في كل شاشات الإعداد) | FOM-SET "Identifying Standards" |

> **نمط موحد مكتشف:** كل Master له Status: **Active/Passive** + **Applicable From** (سريان زمني) + **User** + **Last Updated** — موثقة في فصل "Identifying Standards" المكرر في الأدلة. هذا النمط سيصبح معيار DocTypes المخصصة لدينا.

---

## 2. أحداث النظام المؤتمتة الموثقة (System-Automated Events)

| الحدث | الوصف الموثق | المصدر |
|---|---|---|
| ترحيل مكالمات TEL للنزلاء المقيمين | تلقائي (Automatic) | FOM-DEP ص4 |
| ترحيل التسويات الائتمانية إلى ACR | تلقائي | FOM-CAS ص69 |
| توليد رقم الحجز | تلقائي عند الحفظ | FOM-RES ص9 |
| توليد رمز المجموعة عند بلوغ العتبة | تلقائي | FOM-SET §1 |
| تعبئة بيانات النزيل المتكرر | تلقائي من Guest History | FOM-RES ص15-16 |
| استدعاء بيانات الوصفة عند اختيار الصنف | تلقائي | FNB-LUK (فهرس) |
| Night Balance يجمع مبيعات/تحصيلات اليوم | تلقائي | FOM-DEP §2 |
| حساب Net Amount = Amount − Allowance | تلقائي | FOM-DEP §4 |
| تحديث حالة الغرفة عند وصول/مغادرة | تلقائي عبر التكامل | FOM-REG/HSK |

---

## 3. قيود التحقق الموثقة (Documented Validations)

| القيد | المصدر |
|---|---|
| عدد الغرف في الرجز = مجموع تفاصيل الغرف | FOM-RES ص6 |
| مجموع نسب عناصر الحزمة = 100% | FOM-SET §3 |
| (مدين − خصم) = دائن في Consolidated Entry — وإلا منع الخروج | FOM-DEP §3 ص9-10 |
| Excess/Short = 0 قبل متابعة Night Audit | FOM-DEP ص6 |
| تسوية الفواتير المعلقة قبل Night Balance (تسويات POS/FO) | FOM-DEP ص5-6 |
| Applicable From ≥ التاريخ الحالي لتفعيل الإعداد | FOM-SET (جداول الحقول) |
| تاريخ Adjustment ≤ التاريخ المحاسبي الحالي وضمن السنة | FOM-DEP §4 |
| كشف ازدواج حجز النزيل (Duplicate reservation screen) | FOM-RES ص8 |
| Settlement يجب أن يتطابق (رسالة "Settlement is not tallied") | FOM-CAS ص~50 |

---

## 4. الأثر بعد الإقفال اليومي (Post-Close Behavior)

- تعديل/حذف ممنوعان بعد **Open New Date** — والتصحيح عبر: Night Audit Adjustments (مالية)، Rollback SOA (AR)، أو مستندات معاكسة.
- القيد المسبق: "Posting of rate is not allowed" بمجرد بدء Night Audit — تحذير موثق.
- هذه السلوكيات **إلزامية التمثيل** في معمارية نظامنا (Business Date Lock) — قرار معماري مؤجل لـ `docs/decisions/ADR-002` (سيُنشأ).
