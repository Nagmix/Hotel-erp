# 14 — نموذج البيانات (Data Model) — وحدة MNT

> **~20 كياناً / ~110 حقلاً موثقاً** — قلبها **Complaint/JobOrder/ActionTaken** (المثلث التشغيلي) و**Equipment** بأربعته الفرعية، و**PMSchedule** بثنائية Master/Entry، و**ShiftAssignment** الشبكي.

---

## 1. مخطط العلاقات (ERD نصي)

```
┌─────────────┐   1..*   ┌──────────────┐
│  Location   │◄─────────│   Equipment  │◄──┐
└─────────────┘          └──────┬───────┘   │ 1..*
   ▲ (أو Room/FO)               │ 1         │
   │                     ┌──────┴────────┐  │
   │                     │ AMC / Spares / │  │
   │                     │ StdReadings /  │  │
   │                     │ Remarks (4 sub)│  │
   │                     └──────┬────────┘  │
   │                            │ 1
   │                            ▼
┌──────────────┐  1..*  ┌─────────────────┐
│EquipmentCat- │        │ PMScheduleMaster│
│  egory       │◄───(cat)└───────┬─────────┘
└──────────────┘                │ 1..*
                                ▼
┌─────────────┐        ┌─────────────────┐
│ServiceType/ │◄───────│ PMScheduleEntry │ (تواريخ آلية + MustCompleteBy ≤ Lag)
│ServiceRhythm│        └───────┬─────────┘
└─────────────┘                │
        │                      │ (مع Complaint كلاهما → Job Order)
        ▼                      ▼
┌──────────────┐  1..*  ┌──────────────┐  1..1/1..*  ┌───────────────┐
│ Complaint    │───────►│  JobOrder    │────────────►│ ActionTaken   │
└──────┬───────┘  (sel) └──────────────┘ (assign)    └───┬───────┬───┘
       │                    ▲  Priority (لون)             │       │
       │                    │                              ▼       ▼
       │             ┌──────┴──────┐              CostAnalysis  RepairDetails
       │             │EngEmployee /│               (فئة+مزوّد+   (مخزن+صنف+
       │             │Vendor       │                مبلغ)        مركز+كمية)
       │             └──────┬──────┘
       │                    │
       ▼                    ▼
┌──────────────┐    ┌──────────────┐
│ComplaintPrior│    │ShiftAssignment│ (تواريخ×موظف، ≤31d)
│ity (لون)     │    └──────────────┘
└──────────────┘           │
                    ┌──────┴──────┐
                    │ Skill/Shift │
                    └─────────────┘
   [MGT] Stores/Items/CostCenters (استعارة) · [SYS] ENG Attributes · [UDPF] PrintProject
   [ReadingFlow] Equipment → EquipmentReading (ActualValue × StdReadings)
```

## 2. جرد الكيانات والحقول

| # | الكيان | الحقول الموثقة (النوع/القيد) | المفتاح/العلاقات |
|---|---|---|---|
| 1 | **Location** | code(6α) · name(30,≥3) · short(10,≥3) · status(Passive) | code PK |
| 2 | EquipmentCategory | code(3α) · name · short · status | code PK |
| 3 | CostCategory | code(3α) · name · short · status | → CostAnalysis |
| 4 | Shift | code(3α) · name · short · start_time · end_time · shift_order | → ShiftAssignment |
| 5 | ServiceType | code(3α) · name · short | → PMScheduleMaster |
| 6 | ServiceRhythm | code(3α) · name · short · **no_of_days** | → PMScheduleMaster (محرك التاريخ) |
| 7 | Skill | code(3α) · name · short | → EngEmployee |
| 8 | **EngEmployee** | emp#(**numeric 7**) · name(30) · designation(**code 3α** F1) · skill(FK) | emp# PK — **معزول عن HRP** |
| 9 | **ComplaintPriority** | code(3α) · name · short · priority_order · **color** | → JobOrder (تلوين) |
| 10 | **Equipment** | code(8α) · name · category(FK) · room XOR location · manufacturer · model_no · serial_no · install_date · vendor(FK? UNK-058) · value · currency | code PK |
| 11 | EquipmentAMC | equipment(FK) · required(Y/N) · vendor · expiry_date | child of 10 |
| 12 | EquipmentSpares | equipment(FK) · store(FK MGT) · item(FK MGT) · qty · vendor · **lead_time** | child of 10 |
| 13 | EquipmentStdReading | equipment(FK) · reading_name? · **min · max · UOM** | child of 10 — يقيّد Readings |
| 14 | **PMScheduleMaster** | equipment(FK) · service_provider(FK?) · rows[service_type(FK) · service_rhythm(FK) · **amc_yn(auto)** · start_date · **lag_days** · task] | سيد الوقائية |
| 15 | **PMScheduleEntry** | pm#(auto) · equipment(FK) · start_date · **must_complete_by (≤ lag)** · task · *(dates: calculated)* | pm# PK |
| 16 | **Complaint** | complaint#(auto) · ref_no(10α) · room XOR location · department · type(Common/Repeated) · details · reported_by · status(P/W/C) | complaint# PK |
| 17 | **JobOrder** | jo# · source(Complaint/PM select) · source_ref · priority(FK 9) · **assignee_type(Employee/Vendor)** · assignee_ref · status(P/C) · print(ENG#2) | جسر الإشراف |
| 18 | **ActionTaken** | path(JO/Complaint/PM) · ref · action_text · **status** · start_dt · end_dt | لكل مرجع |
| 19 | CostAnalysisLine | complaint# · cost_category(FK 3) · service_provider(FK) · amount | child of 18 |
| 20 | RepairDetailsLine | complaint# · equipment(FK) · store(FK MGT) · item(FK MGT **أو 999999999999**) · item_name(يدوي للمفتوح) · cost_center(FK MGT) · qty · value(**auto**) | child of 18 — بلا حركة مخزنية! |
| 21 | EquipmentReading | equipment(FK) · date_time(from) · **actual_value(s)** (حسب StdReadings) | — |
| 22 | ShiftAssignment | employee(FK 8) · date · shift(FK 4) — **نافذة ≤31d مستقبلية** | (employee,date) |
| 23 | EnggStoreLink / EnggCostCenterLink | checkbox selections من MGT | **≥1** كلاهما |
| 24 | PrintProject (UDPF) | module · program_type · printer_type · desc · layout(header/footer rows) · toolbox fields · logo | أصل مشترك |
| 25 | ParameterListing | "all parameters... various modules" → **MS-Excel** | قراءة عابرة — UNK-062 |

## 3. الحقول المحسوبة/المشتقة

| الحقل | المنطق | المصدر |
|---|---|---|
| RepairDetails.value | qty × سعر الصنف (من Inventory) — "auto calculated" | OPR ص13 |
| PMScheduleEntry dates | start + rhythm.no_of_days × n — "automatically calculated based on frequency" | OPR ص21 |
| PMScheduleMaster.amc_yn | من EquipmentAMC — "auto populate" | OPR ص21 |
| Complaint.complaint# | توليد تسلسلي | OPR ص3 |
| PMScheduleEntry.pm# | بعد اكتمال الإلزامي | OPR ص22 |
| JobOrder.color-display | من ComplaintPriority.color — تلوين الصف | OPR ص24 |

## 4. جودة النموذج (ملاحظات)

- **نقاط القوة:** فصل نظيف Master/Entry للوقائية · مرجعية موحدة (Complaint/PM → JO → Action) تسمح بتقارير ثلاثية المصدر · السجلات الطفل (Cost/Repair) منفصلة بوضوح.
- **النقاط الضعيفة:** (1) Employee/Designation/Vendor بلا مصدر نظامي موثق؛ (2) **لا كمية-متبقية/حالة مخزنية** في RepairDetails — نموذج استهلاك بلا أثر؛ (3) Reading بلا عتبة إنذار؛ (4) Complaint.status محفوظ بلا Audit Trail (من غيّرها ومتى — بلا User+Timestamp موثقين للتعديل من Q!).
- **التخمين المحسوب:** الحقول المعلمة بـ(FK?) هي ذات UNK-058/059 — تُحسم عند القراءة النهائية لمتبقي MGT/SYS.
