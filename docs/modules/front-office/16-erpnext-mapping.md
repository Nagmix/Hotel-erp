# 16 — الربط مع ERPNext/Frappe (Mapping) — وحدة Front Office

> **تصنيف A-F:** A=موجود مباشرة | B=تكوين | C=تخصيص | D=Custom DocType/App | E=يُبنى من الصفر | F=غير واضح.
> الربط على **المستوى الدلالي الوظيفي** (Business Semantics) لا أسماء المستندات. التحليل الكامل في Phase 11 — هذه بذرة أولية لأهم الكيانات.

---

## 1. بذرة الربط (Seed Mapping)

| المتطلب الوظيفي (من التحليل) | مرشح ERPNext/Frappe | الفئة | ملاحظات |
|---|---|---|---|
| ملف الضيف الموحد (Guest/History) | Customer (مع Custom Fields) | C | يحتاج حقول فندقية (جنسية، جواز، تفضيلات) |
| الحجز (Reservation) | — (لا مكافئ مباشر) | **D** | Custom DocType: Hotel Reservation (فندقي بحت) |
| الغرفة/نوع الغرفة/الطابق/البلوك | — | **D** | Room/Room Type (أصول فندقية) + إدارة حالة |
| Room Rack / Floor Plan (موقف الغرف) | — | **E** | واجهة تخطيطية تفاعلية (بيت خبرة فندقي) |
| التسجيل/الإشغال (Registration) | — | **D** | Hotel Check-in (يربط Reservation ↔ Room ↔ Folio) |
| الفوليو (Folio) | — | **D/E** | بنية مالية فندقية (Tab/الشحنات/التسقاطات) — لا يشبه Sales Invoice مباشرة |
| Folio → Bill → Settlement | Sales Invoice + Payment Entry | **B/C** | التسويات التسعة تحتاج أنماط دفع موسعة (Companies→AR موجود) |
| الودائع (Deposits) | Payment Entry (Advance) | B | موجود كتقدمات؛ الرصد الفندقي (عند الحجز/الوصول) يحتاج تخصيصاً |
| Post Charges على الغرفة | Journal/Sales Invoice Line | **D** | ترحيلات لحظية لبنود متعددة المصادر (POS/TEL/HSK) على الفوليو |
| AR للشركات/الوكلاء | Accounts Receivable (موجود) | **A** | التحويل التلقائي موثق — يتطلب أتمتة Flow |
| GL / دفتر الأستاذ | General Ledger (موجود) | **A** | عبر روابط الترحيل |
| التعاريف/الخطط (Rate/Plan Master) | Price List/Item Price | **C** | هيكل فندقي (Room Type × Plan × Currency × تاريخ) يتجاوز Price List القياسي |
| Night Audit (دورة اليوم) | — | **E** | محرك أعمال فندقي بحت (Post Tariff/Balances/Freeze) |
| Housekeeping/Status الغرف | — (Tasks لا يكفي) | **D** | دورة حالة الغرف (Vacant/Dirty/OOO/OOS) |
| SMS/Broadcast | — | **E/C** | تكامل Gateway + قوالب |
| الهاتف/التمديدات (TEL) | — | **E** | تكامل PMS↔PBX (two-way) |
| الأدوار (20 دوراً فندقياً) | Role/Permissions | **B/C** | تعريف أدوار + Module Profile |
| Multi-Property | Company/ERPNext Sites | **F/C** | قرار معماري (موقع واحد متعدد الفنادق؟) — `decisions/` |
| Multi-Currency | Exchange Rate (موجود) | **A** | مع سعر يومي |
| الضريبة (Luxury/Service/VAT) | Tax Templates | **B** | فئات فندقية |
| التقارير الفندقية (REP) | Report Builder/Query | **C** | تقارير مخصصة بنفس الأعمدة/الغرض |

## 2. استنتاجات أولية

1. **الفندقي الصرف (PMS Core)** — Reservation/Room/Folio/Registration/Night Audit — ليس له مكافئ ERPNext: يُبنى كـ **Custom Frappe App** (وهذا متوقع في البرومبت الرئيسي: hotel-pms-core).
2. **المحاسبة (GL/AR/Tax/FX)** — تغطية ERPNext ممتازة (A/B) والفجوة في **الأتمتة** (الفوليو→فاتورة→تسوية→AR).
3. **نمط التفويض المزدوج** — يحتاج نمط Frappe: Role + Workflow states مع Document Approval.

> هذا الملف يُوسَّع بعمق في Phase 11 بعد اكتمال تحليل كل الوحدات (التسلسل المعتمد: FOM ← FAS ← POS ← ACR ← ...).
