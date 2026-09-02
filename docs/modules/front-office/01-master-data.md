# 01 — البيانات الرئيسية (Master Data) — وحدة Front Office

> البيانات المرجعية التي تعتمد عليها عمليات FO. الحقول التفصيلية لكل Master موجودة في `field-extracts/Front_Office/FN6i-NT-FOM-SET.json` (استخراج آلي) — والسرد الوظيفي يُستكمل بقراءة FOM-SET العميقة `[PENDING DEEP READ]`.

---

## 1. البيانات الرئيسية المشغِّلة للعمليات (الموثقة نصاً)

| Master | استخدامه الموثق | المصدر |
|---|---|---|
| **Room Rate Master** | مصدر التعاريف: "The rates are predefined in the Room Rate Master in the Front office Setup" (Rack/Discounted/Contract/Package) | FOM-RES ص6-7 |
| **Room Master / Room Rack** | الغرف وحالاتها (Vacant/Dirty/Occupied/OOO/OOS/Reserved) + Blocks + Floors + Features | RES §3 + REG §1/§3/§5 |
| **Room Type Master** | أنواع الغرف (مثال موثق: QU / Queen Room / Standard / Suite) | RES ص6 + ص35 + REG ص7 |
| **Meal Plan (Plan Code)** | خطة الوجبات مع التعرفة (Rate Table: Room Type × Plan × Currency) | RES ص6-7 + REG §3 |
| **Company Master** | بيانات الشركة (Company Code + Details) | RES ص4 + REG §3 |
| **Booker Types** | أنواع وكلاء الحجز | RES ص5 |
| **Guest History** | سجل الضيوف السابقين (مطابقة تلقائية عند الحجز/check-in؛ Guest Code يظهر آلياً للمتكرر) | RES ص8 + ص15-16 |
| **Pay Modes** | "Pay modes are defined on Fortune using the Pay Modes option" | RES ص13 |
| **Billing Instructions** | تعليمات الفوترة (Bill Inst #) | RES ص13 + REG §3/§21 |
| **Business Source / Market Segment** | تصنيف مصدر العمل/السوق | RES ص13 + REG §3 |
| **Revenue Codes** | رموز الإيرادات (Post Charges / Stop Posting / Allowances) | CAS §1 + REG §16 |
| **Discount Id / Revenue Discount** | هوية الخصم + الوصف + Revenue item | REG §3 + RES §Revenue Discount |
| **Credit Card Types** | أنواع البطاقات + Company Code | CAS §13/§Deposits |
| **Currency Master** | العملات + أسعار الصرف اليومية | CAS §1 + RES §Rate Info |
| **Nationality List** | جنسيات الضيوف (F1) | CAS §17 + REG §6 |
| **Guest Classification** | تصنيف الضيف (عادي/Time-share...) | REG §3 + §6 |
| **Guest Status List** | حالات الضيف (F1) | REG §3 |
| **OOO Reasons** | قائمة أسباب تعطيل الغرف | RES §3 OOO |
| **Paid Out Reasons** | قائمة أسباب المصروف المدفوع | CAS §Paid Outs |
| **Group Master** | المجموعات (Code/Name) + القائد + ربط FIT | REG §17-§21 |
| **Property Master** | الفنادق (Multi-property) | RES §1.1 + REG §23 |
| **Departments** | الأقسام (OOO، Trace، الشكاوى) | RES §Trace + REG §7 |
| **Features (Hotel/Room)** | مميزات الغرف/الفندق (مثال: Balcony, View...) | REG §1 + RES §1.5 |
| **Wake-up/Extension Master** | التمديدات الهاتفية (Room/Extension) | REG §7/§25-26 |

## 2. النمط الإصداري الموحد (من `docs/domain/master-data.md`)

الـ Masters تتبع نمط: **Status Active/Passive + Applicable From + Last Updated** — إصدارية زمنية (لا حذف فعلي) + قاعدة تجميد بعد الاستخدام.

## 3. المعلَّق

`[PENDING DEEP READ]` FOM-SET كاملاً (خاصة: Room Rate Master §7، Room Master §8، Transaction Types، Module Attributes، INI Switches) — الجداول مستخرجة آلياً في field-extracts والسرد الوظيفي يُكمل بالقراءة العميقة القادمة.
