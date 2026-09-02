# شبكة علاقات الكيانات (Entity Relations — Functional Knowledge Graph)

> **المرحلة:** Phase 1 — تراكمي، يُحدَّث كل جلسة | **القاعدة:** كل علاقة بمصدرها. هذه الوثيقة هي "ذاكرة النظام" التي تمنع فقدان العلاقات العابرة للوحدات.

---

## 1. المعجم المختصر للعلاقات

| الرمز | المعنى |
|---|---|
| `→` | يرحّل إلى / يغذي / ينشئ |
| `↔` | علاقة ثنائية الاتجاه (تحديث متبادل) |
| `⊣` | يقيد / يحجب (تأثير حالة على سلوك) |
| `A ... B` | علاقة "جزء من/تفصيل لـ" |

---

## 2. الرسم الكلي للشبكة (Level 0)

```
                    ┌────────────── SLMM (عقود الشركات والأسعار) ──────────────┐
                    │                                                        │
   GUEST ──→ RESERVATION ──→ REGISTRATION ──→ FOLIO ──→ SETTLEMENT ──→ AR ──┴──→ FAS (GL)
                │                │              ↑ │
                │                ├──→ ROOM ──↔──┘ │ (شحنات الغرفة)
                │                ├──→ ROOM STATUS │
                │                │                ├──→ POS (Bills → Folio: "room charge")
   COMPANY ─────┤                │                ├──→ TEL (Calls → Folio تلقائياً)
   TRAVEL AGENT─┘                │                ├──→ LAUNDRY (HSK)
   MEMBER ──→ MEMBERSHIP ────────┼────────────────┤
                                 │                └──→ NIGHT AUDIT (إقفال يومي)
                                 │                        │
                                 │                        ├──→ Night Balance / Revenue Posting
                                 │                        └──→ FAS (GL عبر FO to Finance Link)
                                 │
   BANQUET BOOKING ──→ REQUIREMENTS ──→ PRE-COSTING ──→ AUTO INDENT ──→ MGT (شراء)
        │                └──→ DEPOSIT ──→ BILLING ──→ SETTLEMENT ──→ AR/FAS
        └──→ FUNCTION ROOM (Availability)
   POS SALE ──→ KOT ──→ KITCHEN ──→ FNB COSTING ──→ MGT (استهلاك)
        └──→ REVENUE ──→ FAS (POS to Finance Link)
   VENDOR ──→ PO ──→ GOODS RECEIPT ──→ STORE ──→ ISSUE ──→ DEPARTMENT/KITCHEN
                    └──→ FAS (MM to Finance Link) + A/P [موثق جزئياً]
   EMPLOYEE ──→ ATTENDANCE ──→ PAYROLL ──→ FAS (Payroll to FAS Link)
        └──→ CARE (Roster/Tasks) ──→ GUEST (Service)
   ASSET ──→ DEPRECIATION ──→ FAS (FI Depr Posting)
   MEMBER ──→ SUBSCRIPTION ──→ AR (Post Subscription to AR) ──→ FAS (Membership to FAS Link)
```

---

## 3. العلاقات الموثقة (Evidence Table)

> مرتبة حسب المسار. كل صف: العلاقة — دليلها — ملاحظة السلوك الموثقة.

### 3.1 مسار النزيل (Guest Journey)

| # | من | إلى | العلاقة الموثقة | المصدر |
|---|---|---|---|---|
| G1 | Reservation | Reservation No | يولَّد رقم حجز تلقائياً عند الحفظ (Post Save Dialog) | FOM-RES ص9 |
| G2 | Reservation | Room Assignment | تخصيص غرف أثناء الحجز (خيار Assign Rooms) + إظهار الغرف المتصلة وحالتها | FOM-RES ص9-12 |
| G3 | Reservation | Deposit | إدخال وديعة أثناء الحجز (نقد/بطاقة/شيك) | FOM-RES ص12-13 |
| G4 | Guest History | Reservation | النزيل المتكرر: معلوماته تظهر تلقائياً + Guest Code يعرض تلقائياً + كشف الأسماء المتشابهة ومنع التكرار | FOM-RES ص8, ص15-16 |
| G5 | Reservation | Group | Group Code/Name يُدخل عند حجز المجموعات؛ ويولَّد رمز المجموعة تلقائياً عند ≥ Group Count (معرف في Room Type) | FOM-RES ص13, FOM-SET §1 |
| G6 | Reservation | Registration | Reservation Check In (تسجيل من حجز) + Express Check In | FOM-REG §1-2 |
| G7 | Registration | Room | تخصيص رقم الغرفة عند الوصول (Walk-in/حجز) — الغرف المتاحة من النوع المحجوز تُعرض | FOM-REG §1 |
| G8 | Registration | Room Status | تغيّر حالة الغرفة عند الوصول/المغادرة (Vacant/Occupied, Clean/Dirty عبر HSK) | FOM-HSK, FOM-REG |
| G9 | Registration | Folio | فتح فوليو للإقامة؛ الشحنات من FO/POS/TEL/غسيل تُرحَّل إليه | FOM-CAS §1 |
| G10 | Folio | Split/Transfer | تقسيم الفوليو (Split FO Charges / Split F&B / Split Folios) ونقله | FOM-CAS §5-8 |
| G11 | Folio | Settlement | تسوية بطرق: Cash/Credit Card/Cheque/Company/Staff/Bill on Hold/Forex — جزئية ممكنة + إبقاء النزيل محتلاً بعد التسوية | FOM-CAS §13 |
| G12 | Settlement (Credit) | ACR | **كل التسويات الائتمانية تُرحَّل تلقائياً إلى Accounts Receivable** | FOM-CAS ص69 |
| G13 | Check-out | Confirm Checkouts | قائمة مغادري اليوم + Pax Checkout | FOM-CAS §10-12 |
| G14 | Registration ↔ Extension | تفعيل/تعطيل الامتداد الهاتفي للغرفة (من REG!) | FOM-REG §26-27 |
| G15 | Reservation | Trace | احتياجات خاصة تُوجَّه لقسم مسؤول بتاريخ/وقت | FOM-RES ص20 |
| G16 | Company/Agent | Reservation | حجز باسم شركة/وكالة (كود Company/Booker Type) | FOM-RES ص4-5 |

### 3.2 مسار الإيراد والمحاسبة

| # | من | إلى | العلاقة | المصدر |
|---|---|---|---|---|
| F1 | Posting (FOM) | Folio | Post Charges: Revenue Code + Currency + Charges → فوليو الغرفة | FOM-CAS §1 |
| F2 | POS | Folio | فاتورة المطعم تُرحَّل لفوليو الغرفة ("Restaurant bill will be posted for POS module") | FOM-CAS ص4 (Note) |
| F3 | TEL | Folio | المكالمات تُرحَّل تلقائياً للنزلاء المقيمين (سبب منع Guest Balance قبل منتصف الليل) | FOM-DEP ص4 |
| F4 | Night Audit | FAS | ترحيل إيراد اليوم عبر FO to Finance Link | FAS-SET (فهرس) + FOM-DEP |
| F5 | POS | FAS | POS to Finance Link | FAS-SET (فهرس) |
| F6 | MGT | FAS | MM to Finance Link | FAS-SET (فهرس) |
| F7 | HRP | FAS | Payroll to FAS Link | FAS-SET (فهرس) |
| F8 | MEM | FAS | Membership to FAS Link | FAS-SET (فهرس) |
| F9 | ACR | FAS | Link AR to Finance | FAS-SET (فهرس) |
| F10 | MEM-MTR | ACR | Post Subscription to AR | MEM-MTR (فهرس) |
| F11 | Consolidated Entry | Night Audit Info + GL | قيد مزدوج: Department + Cost Center + GL Code — توازن إلزامي (debit − allowance = credit) | FOM-DEP §3 |
| F12 | FXD | FAS | FI Depreciation Posting to FA | FAS-FXD (فهرس) |
| F13 | TEL | FAS/FO | Telephone Revenue Posting | TEL-SET (فهرس) |
| F14 | ACR-OPR | ACR | Match Bills–Receipts / Outstanding Update / Rollback SOA | ACR-OPR (فهرس) |
| F15 | Night Audit | Business Date | Open New Date = تجميد تعديلات التاريخ المغلق | FOM-DEP §5 |

### 3.3 مسار التوريد والتكلفة

| # | من | إلى | العلاقة | المصدر |
|---|---|---|---|---|
| S1 | Indent/PR | PO | Requisition → Indent → Purchase Order (دورة) | MGT-DNT (فهرس) |
| S2 | Quotation | PO | Quotation Analysis قبل الشراء | MGT-DNT (فهرس) |
| S3 | PO | Goods Receipt | استلام يغلق/يحدث حالة PO (PO Status) | MGT-DNT/LUK |
| S4 | Receipt | Store/Inventory | إضافة للمخزون + Receipt Register | MGT-REP |
| S5 | Store | Kitchen (FNB) | Inter Store Transfer → Kitchen Stock | MGT-DNT, FNB-COP |
| S6 | BNQ Requirements | MGT | Auto Indent (توليد طلب تلقائي من متطلبات الوليمة) | BNQ-BIL (فهرس) — تفاصيله [ND] |
| S7 | FNB | MGT | Auto Indent Creation من التكاليف | FNB-COP (فهرس) |
| S8 | POS Sales | FNB | الاستهلاك النظري من المبيعات مقابل الوصفة (Standard vs Actual) | FNB-REP/LUK (عناوين) |
| S9 | Recipe | Item (MGT) | مكونات الوصفة = أصناف مخزنية | FNB-SET [INFERENCE من العناوين] |

### 3.4 مسار فريق العمل والخدمة

| # | من | إلى | العلاقة | المصدر |
|---|---|---|---|---|
| H1 | Employee | Care Tasks | إسناد المهام + قياس الإنتاجية (Task by Runner/Technician) | Care-REP (فهرس) |
| H2 | Employee | HRP Payroll | Attendance → Payroll Processing → ترحيل | HRP-PNT (فهرس) |
| H3 | Employee | HSK | Employee Schedule + Room Cleaning Assignments | FOM-HSK (فهرس) |
| H4 | Employee | MNT | Define Employees (هندسة) + Action Taken | MNT-SET/OPR |
| H5 | Guest | Complaint/Task | Raising a Task/Complaint (Care) — Feedback → إحصاءات | Care-Ops (فهرس) |
| H6 | Complaint | MNT Job Order | شكوى صيانة → أمر عمل → قراءة معدات | MNT-OPR (فهرس) |

---

## 4. قواعد سلوك مؤثرة في الشبكة (Business Rules with Graph Impact)

| القاعدة | أثرها على الشبكة | المصدر |
|---|---|---|
| بعد Open New Date تُمنع تعديلات/حذف معاملات التاريخ المغلق | كل الكيانات التشغيلية "تتجمد" تاريخياً — ضرورة نموذج إصدارات/تجميد | FOM-DEP ص7 |
| خلال Create Guest Balance يُسمح بالترحيل للتاريخ التالي فقط (FO/POS/BNQ) | آلية "Next Day posting window" أثناء التدقيق | FOM-DEP ص4 |
| Guest Balance لا يبدأ قبل منتصف الليل (بسبب ترحيل TEL التلقائي) | قيد زمني على جدولة Night Audit | FOM-DEP ص4 |
| KOTs المعلقة لا تمنع Night Balance، لكن مبالغها لا تدخل فوليو النزيل | حالة "معلق" بلا أثر مالي حتى التسوية | FOM-DEP ص6 |
| Night Report (Oprn): يجب أن يكون Excess/Short = صفر قبل المتابعة | بوابة جودة يومية إلزامية | FOM-DEP ص6 |
| عدد الغرف في الحجز = مجموع تفاصيل غرف الحجز | قيد اتساق داخلي | FOM-RES ص6 |
| نسب عناصر الحزمة يجب أن تجمع 100% | قيد تكامل Package Elements | FOM-SET §3 |
| Over Booking % لكل نوع غرفة | يسمح بالحجز فوق الطاقة المعلنة | FOM-SET §1 |
| Advance% / Cancellation% / Retention% معرفة على مستوى نوع الغرفة | تُستخدم عند الحجز/الإلغاء/No-Show | FOM-SET §1 |
| تسوية Company تفتح مديونية ACR تلقائياً | أتمتة FO→AR | FOM-CAS ص69 |
| Night Audit Adjustments: بدون شرط توازن (عكس Consolidated Entry) | قناة تعديل مالي مرنة للمالية | FOM-DEP ص11 |

---

## 5. فجوات المعرفة الحالية في الشبكة (تُسد في Phase 3/6)

- تفاصيل حقول AR Invoice/Statement والـ aging buckets (ACR).
- آلية Tax Posting التفصيلية (FOM-SET §6 + SYS Tax Slabs) — خاصة التراكم/الاحتواء.
- سلوك Multi-currency الكامل في الفوليو (Forex Settlement موجود؛ FAS exchange mechanics [ND]).
- بنية دليل الحسابات (Main/Sub Heads) وعمقها.
- توزيع الـ POS revenue على GL (POS to Finance Link تفاصيله).
- Payroll ED Equations → FAS mapping التفصيلي.
