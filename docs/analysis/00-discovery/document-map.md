# PHASE 0 — خريطة الوثائق والعلاقات (Document Map)

> **الغرض:** تحديد أي الوثائق تُقرأ معاً، وأيها مرجع لأي مسار عمل، وأين تقع نقاط التكامل الموثقة.
> **الرمز:** `→` يعني "يرحّل إلى / يغذي". العلاقات مبنية على عناوين موثقة في الفهارس.

---

## 1. مسار النزيل والمالية (Guest & Revenue Flow) — الأولوية القصوى

```
FOM-SET (الإعدادات: الغرف، الأسعار، الضرائب، الخطط)
   │
FOM-RES (الحجز) ──→ FOM-REG (تسجيل الوصول) ──→ FOM-CAS (الفوليو/الكاشير/المغادرة)
   │                     │                           │
   │                     ├──→ FOM-HSK (حالة الغرفة)  │
   │                     ├──→ TEL (مكالمات → folio)  │
   │                     ├──→ POS (شحنات المطاعم → folio)
   │                     │                           │
   ▼                     ▼                           ▼
FOM-DEP (إقفال اليوم/Night Audit) ──→ ترحيل الإيراد ──→ FAS (GL)
                                     │
                                     └──→ ACR (مدينة الشركات/الوكالات) ──→ FAS
                                          ACR-OPR (تحصيل/مطابقة)   ACR-BIL (فواتير شهرية)
```

**وثائق المسار (تُحلَّل كحزمة واحدة):**
1. `FN6i-NT-FOM-SET.pdf` (145 ص) — أساس كل شيء: Room/Rate/Tax/Meal Plan/Package
2. `FN6i-NT-FOM-RES.pdf` (68 ص) — الحجوزات
3. `FN6i-NT-FOM-REG.pdf` (105 ص) — الوصول والإقامة
4. `FN6i-NT-FOM-CAS.pdf` (95 ص) — الكاشير والفوليو والمغادرة
5. `FN6i-NT-FOM-DEP.pdf` (14 ص) — Night Audit
6. `FN6i-NT-ACR-*.pdf` (5 وثائق، 89 ص) — الحسابات المدينة
7. `FN6i-NT-FAS-SET/TRN.pdf` — قواعد الترحيل

---

## 2. نقاط التكامل المحاسبي الموثقة (من FAS-SET)

| الرابط الموثق في الفهرس | المعنى المتوقع | الوثائق المرجعية للطرفين |
|---|---|---|
| **FO to Finance Link** | ترحيل إيراد/مديونيات الاستقبال إلى GL | FOM-DEP + FOM-CAS ↔ FAS-SET |
| **POS to Finance Link** | ترحيل مبيعات المنافذ إلى GL | POS-SET ↔ FAS-SET |
| **MM to Finance Link** | ترحيل مخزون/مشتريات إلى GL | MGT-DNT/MGT-SET ↔ FAS-SET |
| **Payroll to FAS Link** | ترحيل الرواتب إلى GL | HRP-PNT ↔ FAS-SET |
| **Membership to FAS Link** | ترحيل إيراد العضويات إلى GL | MEM-MTR ↔ FAS-SET |
| **Link AR to Finance** | ربط الحسابات المدينة بـ GL | ACR ↔ FAS-SET |
| Telephone Revenue Posting (TEL-SET) | ترحيل إيراد المكالمات | TEL-SET ↔ FOM-CAS/FAS |
| FI Depr. Posting to FA (FXD) | ترحيل قيود الإهلاك | FN6i-NT-FAS-FXD ↔ FAS-TRN |
| Post Subscription to AR (MEM-MTR) | ترحيل الاشتراكات إلى AR | MEM-MTR ↔ ACR |

> ⚠️ هذه الروابط هي **أهم اكتشاف في Phase 0** لأنها تحدد بنية الترحيل المحاسبي للنظام المستهدف.

---

## 3. دورة المشتريات والتكلفة (Procurement & Cost Cycle)

```
MGT-DNT: Purchase Requisition → Indent → Purchase Order → Goods Receipt → Issue
              │                                          │
              │                                          ├──→ FAS (MM to Finance Link)
              │                                          └──→ MGT-LUK/REP (الحالة والتقارير)
              ▼
FNB-COP (تكاليف): Kitchen Stock → Consumption → Standard vs Actual ──→ FNB-REP
              │
              ├──→ MGT (Auto Indent Creation — طلب تلقائي للمطبخ)
              └──→ POS (الوصفات تصدر من مبيعات POS → استهلاك نظري)
BNQ-BIL: Requirement Entry → Pre-Costing (Chef) → Auto Indent → MGT
```

**وثائق المسار:** `MGT-SET` → `MGT-DNT` → `FNB-SET` (Recipe Master) → `FNB-COP` → `BNQ-BIL` (Requirement/Pre-Costing) → `FAS`.

---

## 4. دورة الولائم (Banquet Cycle)

```
BNQ-CFG (تهيئة: القاعات، أنماط التجهيز، سياسات الإلغاء، قوائم الطعام)
   └─→ BNQ-BOK (الحجز: Make/Amend/Cancel/No-Show/Block-Release)
          └─→ BNQ-BIL (الودائع، المتطلبات، التسعير المسبق، الفوترة، التسوية)
                 ├──→ FNB (Pre-Costing) ──→ MGT (Auto Indent)
                 └──→ FAS/ACR (الترحيل والتحصيل)
BNQ-SET (Country-State-City، Property Info، أنواع البنود) — يخدم BOK/BIL
BNQ-LUK (Availability Chart) — استعلام التوفر
```

---

## 5. دورة الموظفين (Employee Lifecycle)

```
HRP-RQP (التوظيف: طلب→مقابلة→عرض)
   └─→ HRP-SET (التعريفات: Grade, ED Codes, Attendance Codes)
          └─→ HRP-PNT (الحضور، معالجة الرواتب، الإغلاق)
                 └─→ HRP-REP (التقارير)
                        └─→ FAS (Payroll to FAS Link)
Care (الروستر، المهام، الإنتاجية) — يستخدم نفس بيانات الموظفين
FOM-HSK (Employee Schedule للتنظيف) — موازيع بسيطة داخل HSK
MNT-SET (Define Employees للصيانة) — موظفو الهندسة
```

> [INFERENCE] يبدو أن بيانات الموظفين (Personnel Master) مركزية في HRP وتستهلكها Care وHSK وMNT — يُدقق عند تحليل HRP-SET وCare-SET.

---

## 6. ملفات العملاء والشركات (Profiles Network)

```
FOM-GST (Guest Master — النزيل الفرد)
POS-GST (Guest Master — نسخة POS + Loyalty) [يُفهم العلاقة بين النسختين عند التحليل]
SLM-PRF (Company Profile + Rates + Contracts — الشركات والوكالات)
SLM-LUK (استعلامات الأسعار والعقود)
FOM-SET (Company Types, Business Sources, Group Business Sources)
MEM (Member Master — الأعضاء)
```

> ⚠️ **سؤال مفتوح (UNK):** هل Guest Master في FOM وPOS قاعدة واحدة أم مزامنة بين نسختين؟ يُدقق عند قراءة POS-GST مقابل FOM-GST.

---

## 7. وثائق التهيئة العامة (System-wide)

- `FN6i-NT-SYS-SSP.pdf` (110 ص): المستخدمون، الصلاحيات، قواعد البيانات (PMS/Training)، معايير النظام — **يجب قراءته مبكراً** لأنه يعرّف نمط المستخدمين والصلاحيات في كل الوحدات.
- `Touch_Screen_Manual.pdf` (46 ص): واجهة POS اللمسية — **مرجع UX** لكيفية تفكير التصميم التشغيلي السريع (شاشة واحدة، أزرار كبيرة).
- فصل **"Identifying Standards"** المتكرر في عدة وثائق: معايير موحدة للتعرف على العناصر في الواجهة — يُجمع في وثيقة UX واحدة.

---

## 8. مصفوفة "الوثيقة ← من يقرأها" (حسب المراحل)

| المرحلة | الوثائق المطلوبة |
|---|---|
| Phase 1 (Domain Model) | FOM-SET, FOM-RES, FOM-REG, FOM-CAS, FOM-DEP, SYS-SSP, SLM-PRF, MEM-MPF |
| Phase 2 (Modules) | كل وثائق الوحدة المعنية |
| Phase 5 (Workflows) | RES+REG+CAS+DEP / MGT-DNT / BNQ-BOK+BIL / HRP-PNT / MEM-MTR |
| Phase 6 (Accounting) | FAS-SET (الروابط), FAS-TRN, FOM-DEP, FOM-CAS, POS-SET, ACR-OPR, MEM-MTR, HRP-PNT, FXD, TEL-SET |
| Phase 7 (Reports) | كل وثائق REP/RPL (إجمالي ~15 وثيقة، ~900 صفحة) |
| Phase 8 (Security) | SYS-SSP, ACR-SET (AR User Access), FAS-SET (Transaction Type Rights), Care-SET (Define Rights) |
| Phase 4/18 (UX) | Touch_Screen, لقطات الشاشات في كل الوثائق (~7,763 صورة) |
