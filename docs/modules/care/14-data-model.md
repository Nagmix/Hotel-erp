# 14 — نموذج البيانات (Data Model) — وحدة Care

> **50+ حقلاً عبر ~17 كياناً** (6 مرجعية + 11 تشغيلية). ERD نصي مفاهيمي + جداول الحقول + المفاتيح والعلاقات كما توثيقها الدلائل (لا مخطط قاعدة في الأدلة — نموذج منطقي مستنبط موثق المصدر لكل حقل).

---

## 1. ERD المفاهيمي (نصي)

```
[PMS:User]─(map)─<CareUserGroup>─┬─> Group: Agent|Supervisor
                                  └─> BelongsToDept ─> [PMS:Department]

[PMS:Property] ─1:N─> [PMS:Department] ─1:N─> [PMS:Designation] ─1:N─> CareEmployee
                                    │                        │
                                    │                   ReportingLink (self-FK: Designation→Designation)
                                    │                        └─> سلسلة التصعيد
[PMS:Maintenance] ──> Shift · Location(OtherArea) · Floor
                                    │
CareEmployee ─1:N─> RosterCell(Month × Day: Shift|WeeklyOff|Floors[])
          ─1:N─> LoginSession(type, mobile#, pager#, in/out, items_returned)
                              │ (الموبايل عهدة تنتقل بين الجلسات)
TaskDefinition(Dept, Main, Sub, EstTime, Type, Charges, Feedback, Priority, EscTimeout[4], IVRCode)
          │
MultiTask ─1:N─> MultiTaskItem(TaskDefinition عبر الأقسام!)
          │
Task/Incident(# , place, room, guest(PMS), task_def, spec_ins, raised_by, raised_at,
              assigned_to?, runner, esc_level, est_time, elapsed, status, ci/co(PMS))
          ├─1:N─> SMSMessage(dir, body, status: Queued|Delivered|Sent, ack_at)
          ├─0..1─> Feedback(rating: Satisfied|Not|NotServed|GuestUnavailable, note, at)
          ├─0..1─> CancelStop(kind: Cancelled|Stopped, note, at)
          ├─0..N─> TaskExtension(D/H/M, reason, at, by)
          └─0..N─> TaskTransfer(to_employee, from_employee, reason, at)

LostFoundArticle(value, lost_loc, lost_at, found_by, found_at, found_loc,
                 returned_to, returned_at, authorized_person, source: PMS|Care, module: outlet?)

ReportAccess(user, report, spool: Y/N, export: Y/N, format: Excel|OpenCalc|Direct)
```

## 2. الجداول التفصيلية

### 2.1 CareEmployee (SET ص16-17)
| الحقل | النوع | قيود |
|---|---|---|
| last/middle/first_name | نص | **غير قابل للتعديل** (V-CA-12) |
| address, personal_phone | نص | — |
| extension, pager, **mobile**, walky_talky, email | اتصال | mobile = قناة SMS (عهدة) |
| photo | ثنائي | Photo/Clear Photo |
| designation_id | FK → PMS:Designation | المكان في الشجرة |
| is_deleted | منطقي | Deleted List (استرجاع) |

### 2.2 TaskDefinition (SET ص25-27)
| الحقل | النوع |
|---|---|
| department_id / main_code+desc / sub_code+desc | مرجعي |
| est_response_minutes / designation_id (المسؤول) | عدد/FK |
| type (Complaint/Request/Incident/Other) · charges (Y/N) · feedback_required (Y/N) | أعلام |
| priority (High/Normal/Low) | enum |
| esc_timeout_l1..l4 (دقائق) | أعداد |
| ivr_code (من Task List REP ص69) | كود |

### 2.3 Task/Incident (OPR REP عابر)
راجع 10 §1.1 — **34 حقلاً** بما فيها CI/CO من PMS.

### 2.4 LoginSession (OPR ص19-28)
user_type (Sup/GRE/DM) · employee_id · shift_id · mobile# · pager# · login_at · logout_at · mobile_returned · pager_returned.

### 2.5 RosterCell (OPR ص5-18)
month+year (≥ حالي) · department_id · employee_id · day(1-31) · shift_id | weekly_off 'O' · floors[] · default_floor.

### 2.6 SMSMessage
direction (out/in) · task_id · body (نصوص موثقة حرفياً!) · status (Queued/Delivered/Sent) · acknowledged_at (REP ص49).

### 2.7 Feedback (OPR ص47)
rating (4 قيم) · note · feedback_at · issue_at (التقارير تفصل — REP ص59).

### 2.8 LostFoundArticle (OPR ص60-65)
9 حقول ثلاثية المراحل + source + module(outlet).

## 3. المفاتيح والتفرد (مستنبط)

| الكيان | المفتاح الطبيعي المرجح | ملاحظات |
|---|---|---|
| Task | complaint# (تسلسلي، مستقل حتى داخل Multi Task — SET ص31) | نطاق التسلسل غير موثق (يومي/كلي؟ — UNK) |
| RosterCell | (month, dept, employee, day) | |
| LoginSession | (employee, date, shift?) | جلسات متعددة يومياً واردة (تقرير #19 يعرض لكل تاريخ) |
| SMSMessage | (task, direction, seq) | |
| TaskDefinition | (dept, main, sub) | |

## 4. سلامة مرجعية عبر قواعد الأصل (Referential by Rule)

- Task.assigned_to ∈ {LoginSession نشطة لنفس القسم} (BR-CA-04).
- Transfer.to ∈ {مسجلو نفس القسم} (OPR ص73).
- Task.room/place ∈ {PMS Maintenance Locations} (V-CA-20).
- Feedback/CancelStop فقط للمهام المؤهلة (V-CA-11).
- Escalation target = ReportingLink المنطلق من designation المهمة (BR-CA-08).

## 5. حجم البيانات التقديري (تحليلي)

| الكيان | التقدير الشهري (فندق 200 غرفة) |
|---|---|
| Task | 3-10 آلاف (شكاوى+طلبات) |
| SMSMessage | 3×Task تقريباً (تخصيص + رد + إشعارات) |
| RosterCell | موظفو الخدمة × 30 |
| LoginSession | × ورديات × أيام |
| Feedback | ~Feedback=Y فقط |

> **ملاحظة إعادة البناء**: الكيانات التشغيلية بلا أرشفة موثقة — التقارير الزمنية (Yearly) تفترض احتفاظاً غير محدد المدة → قرار Archiving في Phase 6 (F-CA-10).
