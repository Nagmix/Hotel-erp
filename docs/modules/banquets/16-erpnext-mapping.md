# 16 — Seed Mapping إلى ERPNext/Frappe — وحدة Banquets

> **الوحدة الأصعب إسقاطاً حتى الآن** (بعد POS): لا نظير قياسي لحجز الفعاليات/القاعات في ERPNext — تخصيص واسع مع إعادة استخدام محرك POS المستقبَل. التصنيف: A/B/C/D/E/F.

---

## 1. جدول المطابقة الأساسي

| # | كيان FN6i | نظير ERPNext/Frappe | التصنيف | الملاحظات/القرار |
|---|---|---|---|---|
| 1 | Function Room | `PMS Function Room` (custom) | **C/F-BQ-2** ⭐ | لا نظير (Table في POS ≠ قاعة قابل للحجز)؛ 6 تبويبات + أبعاد + سعة × نمط جلوس |
| 2 | Associated Room / Sub Venue | custom child + self-link | C | حصرية Sub للأم |
| 3 | Reservation Status (ملونة) | custom field + kanban state | C | الألوان في View states |
| 4 | Event Calendar (الحاجب) | **Event** (Frappe) + custom gate | **B/F-BQ-5** | Calender view قياسي + تحقق حجز |
| 5 | Cancellation Policy | `PMS Cancellation Policy` | C | مثل FO/POS policies |
| 6 | **Banquet Booking (Res#)** | `PMS Banquet Event` (رأس حدث) | **C/F-BQ-2** | قلب الوحدة — يحمل Party/Company/Rooms/Pax/Terms |
| 7 | Across-Dates vs Slot | custom booking_type + منع تداخل | **E** | محرك توافر زمني مخصص (slot grid) |
| 8 | Requirement Entry (WS) | `PMS Function Worksheet` + items | **C** | أقرب لـ Sales Order مخصص + Allowed counts |
| 9 | F11 Rename / F12 Complimentary | حقول override في Worksheet Item | B | — |
| 10 | Pre Costing | `PMS Pre-Costing` (Recipe/Inventory link) | C | يستهلك BOM (FNB) + Item |
| 11 | **Auto Indent** | **Material Request (MGT) توليدي** | **A-** ⭐ | يستدعي محرك MGT — F-BQ-6: hook WS→MR |
| 12 | Deposit + Vouchers | **Payment Entry** (advance) + Print | **B** | + حالات modified/deleted (سجل إصداري) |
| 13 | Refund/Retention | Payment Entry (return) + custom type | B | — |
| 14 | Banquet Bill | **POS Invoice** (BNQ كمنفذ!) | **A-/F-BQ-1** ⭐ | إعادة استخدام محرك POS كاملاً (splits/settlement) |
| 15 | Settlement (11) | = POS modes (مشاركة) | A | Void يُعطّل لمنفذ BNQ |
| 16 | Corporate Rate ×3 | `PMS Rate Card` (بنمط FO/SLM) | C | توحيد مع SLM لاحقاً |
| 17 | Menu Master (BNQ) | = POS Menu Master (MA 29) | A | نفس DocType — منفذ BNQ |
| 18 | Menu Card / Package | `PMS Menu Card` + package (BOM-like) | C | Allowed per group |
| 19 | Equipment (Category/Sub/Equipment) | `Item` (non-FB) + InHouse Qty/Rate | B | — |
| 20 | Supplier Rates (أدوان 5) | Item Supplier price lists (5 فترات) | **C** | أدوان الساعات عملة جديدة — custom child |
| 21 | Event Question/Template (feedback) | `PMS Feedback Template` | C | بعد الحدث (Post-Function) |
| 22 | Service Managers / Banquet Staff | Contact + User Permission | B | — |
| 23 | Availability Chart | **Calendar/Gantt View مخصص** | **E/F-BQ-3** | أهم مكون Frontend مخصص |
| 24 | Shift/Outlet/Session | = POS engine | A | F-BQ-1 |
| 25 | Country/State/City | **Country/State/City** (Frappe!) | **A** ⭐ | مطابقة قياسية موجودة |
| 26 | Property Information | Company + Website + attachments | B | — |
| 27 | Print Forms (4 Program IDs) | Print Format + Print Settings | D | F-BQ-4 |
| 28 | BNQ User Access | = POS ACL | A | — |

## 2. القرارات المعمارية (F-BQ-1..8)

| # | القرار | المبرر |
|---|---|---|
| **F-BQ-1** ⭐ | **BNQ = منفذ POS متكامل**: بناء الولائم فوق محرك POS المخصص (Shift/Outlet/Session/S Invoice/S settlement/ACL/MA keys) بدل وحدة كاشير مستقلة | توثيق الأصل يستدعي POS hرفياً (MA/User Access/أنماط)؛ توفير تكرار هائل |
| **F-BQ-2** | `PMS Banquet Event` DocType مخصص (رأس الحدث + الغرف + الشروط) + `PMS Function Room` — لا نظير قياسي | حجز الفعاليات خارج نطاق ERPNext القياسي |
| **F-BQ-3** | Availability Chart = مكون Frontend مخصص (React) على API توافر زمني (slot grid + حالات ملونة) | القيمة الجوهرية للواجهة الجديدة — أعلى مكون ترجمة |
| **F-BQ-4** | FP/BEO/Vouchers = Print Formats قياسية (HTML/Jinja) بترتيب Menu Group Sequence | يستبدل المصمم المرئي القديم (نمط POS Print Designer نفسه — قرار مشترك) |
| **F-BQ-5** | Event Calendar = Event قياسي + **Booking Gate hook** (تحقق الحجز حسب allowed/made-by) | يجعل الحاجب التقويمي قابلاً للتطبيق موحداً مع FO blocker |
| **F-BQ-6** | **Auto Indent hook:** WS Finalize/Pre-Costing → Material Request (Department/CC + BOMs) — **يحسم UNK-011** | الأصل موثق النص؛ ERPNext يدعم MR من BOM |
| **F-BQ-7** | Complimentary/NC = فروع فاتورة بلا إيراد (is_cancelled-like revenue flag) — قاعدة "ليست مبيعات" | موثق نصاً |
| **F-BQ-8** | Deposits = Payment Entry مع **سجل إصداري** (أصلي/modified/deleted vouchers) + Running Balance محسوب | وفاء للنموذج الأصلي بالتدقيق |

## 3. تقييم الجاهزية

- **إعادة استخدام مباشرة:** Country/State/City · محرك POS كامل (الفوترة/التسوية/الإقفال) · Material Request (Auto Indent) · Payment Entry (Deposits).
- **تخصيص واسع:** Function Room/Event/Worksheet/Availability slot-grid/Corporate Rates/Menu Cards.
- **جديد كلياً:** محرك التوافر الزمني (Across-Dates/Slots) + أدوان الإيجار بالساعات (1hr/2hrs/Half/Full/Multi).
