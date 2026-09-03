# 12 — التكاملات (Integrations) — وحدة Care

> **I-CA-01..14**: Care أعلى كثافة جسور PMS في المشروع (7 قنوات واردة) + قنوات خارجية (SMS/IVR) + **حسم UNK-010 الكامل** (لا جسر HRP).

---

## 1. الجسور الموثقة

### I-CA-01: Care ← PMS — هوية المستخدمين ⭐
- **النص**: "You cannot create new Users; you can only map the Users that are created in PMS. If you want to create a new User, login to PMS, create the new User and map that User in Fortune Care." (SET ص5) + "the Groups & Users will be retrieved from PMS" (ص7).
- **الطبيعة**: مرجعية أحادية الاتجاه (read + link).
- **القرار (F-CA-1)**: User واحد في Frappe عبر الوحدات مع Roles خاصة بـ Care.

### I-CA-02: Care ← PMS — الأقسام والتصنيفات الوظيفية ⭐
- **النص**: "All the Departments that are available from PMS database will be displayed" (SET ص11) + "All the Designations that are available from PMS database will be displayed" (ص13).
- **القرار**: Department + Designation doctypes مشتركة (نفس مصدر FO).

### I-CA-03: Care ← PMS/Maintenance — الورديات والمواقع ⭐
- **النص**: "The Shifts and Locations parameters are mapped from the **Maintenance module in PMS**" (OPR ص5) + "The Locations parameter is retrieved from the Maintenance module in PMS" (ص33).
- **الدلالة**: وحدة صيانة PMS (MNT في خريطة 17 وحدة) هي مصدر الورديات والأماكن "Other Area" — **جسر MNT→Care موثق** لم يكن مرسوماً في Knowledge Graph.
- **القرار (F-CA-4)**: Shift Type + Location doctypes عامة يملؤها MNT/Care معاً.

### I-CA-04: Care ← PMS — الغرف وبيانات الضيوف الحية ⭐
- **النص**: "When you select the Room #, Room # will appear in the Room # field and the respective Guest details will appear on the right side of the window" (OPR ص34) + سجل المهمة يحمل Check-in/Check-out dates (REP ص25) + الغرف غير المشغولة خيار صريح (Unoccupied Room).
- **القرار**: قراءة حية من Room/Guest Folio (فحص الإشغال) في Frappe.

### I-CA-05: Care ← PMS — Lost and Found ⭐
- **النص**: "You can view the PMS Lost and Found details from this option" (OPR ص60) + إضافة سجلات محلية بـ Module=outlet (ص64).
- **الدلالة**: L&F كيان مشترك PMS↔Care — PMS يسجل، Care يوسع (outlet).
- **القرار (F-CA-9)**: doctype L&F واحد مع source field.

### I-CA-06: Care ← HRP — **UNK-010: RESOLVED نهائياً** ⭐⭐
- **النص الدامغ (SET ص5/11/13)**: المستخدمون/الأقسام/التصنيفات من PMS؛ والموظفون يُنشؤون داخل Care محلياً (اسم/عنوان/اتصال/صورة — SET ص16-17) **بلا أي إشارة إلى Personnel Master أو Payroll أو HRP في الدلائل الثلاثة كاملة**.
- **الحكم**: **مخزنان مستقلان تماماً للموظفين**:
  - HRP Personnel Master: كيان الرواتب (EMP# سبعة خانات، Dept/Grade/Category، ED engine).
  - Care Employee: كيان الخدمة الخفيف (اتصالات + صورة + تسلسل تصعيد).
  - التقاطع الوحيد: أبعاد Department/Designation من PMS (كلاهما يقرأها من نفس المصدر).
- **أثر إعادة البناء (F-CA-2)**: في Frappe يُستخدم **Employee** ككيان واحد (مع حقل "Care Profile" child: mobile/pager/walky/extension/photo/reporting) — أو doctype مستقل "Service Staff" مع رابط اختياري Employee. **التوصية**: التوحيد (HRMS) لأن ازدواجية الأصل ستضاعف صيانة الأسماء/المغادرة — والمغادرة بلا جسر تعني موظفاً "حياً" في Care بعد F&F في HRP (خلل موثق في الأصل نفسه!).
- **مرجع UNK-010 في unknowns.md**: يُحدّث إلى Resolved مع الإحالة لهذا القسم.

### I-CA-07: Care ↔ بوابة SMS (خارجية) ⭐
- **الأدلة**: إرسال آلي + حالات Queued/Delivered/SMS Sent + استقبال ردود (S/C) + **Clear Pending SMS** (OPR ص37/69).
- **الغياب**: لا مواصفة مزوّد/بروتوكول/حدود طول (GAP-CA-D05).
- **القرار (F-CA-3)**: Notification + SMS Gateway Settings (Frappe) + خادم معالجة ردود (webhook) يفسر `# S`/`# C`.

### I-CA-08: Care ↔ IVR (خارجية)
- **الأدلة**: "calls attended by agent/**IVR** or any other User" (REP ص5) + **IVR Code** في Task List (REP ص69).
- **الغياب**: لا تفصيل واحد (GAP-CA-D04).
- **القرار**: قناة إنشاء مهمة عبر هاتف = webhook/endpoint مستقبلي.

### I-CA-09: Care → PMS (المرشح غير الموثق — الفوترة)
- راجع 11 §3 — استنتاج فقط.

### I-CA-10: Care (داخلي) — Multi Task عبر الأقسام
- "Under the main task we can select the **other department's tasks also**" (SET ص29) — تجميع inter-department داخلي.

### I-CA-11: Care (داخلي) — الروستر × الحضور
- Login يقرأ الروستر (Schedule Not Entered) — لكن **لا تغذية عكسية إلى HRP Attendance** (GAP-CA-D02).

### I-CA-12: Care ← SYS (نمط عام)
- Define Rights بنمط SYS (Menu Options/Add/Modify/Delete) + Restrict Reports بنمط قيود التقارير العامة (SET §2/§6) — هوية وأنماط SYS دون Property codes إضافية موثقة.

### I-CA-13: Group SMS → أرقام خارجية
- "enter extra mobile numbers other than those available in the CARE system" (OPR ص58) — قناة خارج بيانات الموظفين.

### I-CA-14: Care ← FO Company/Outlet (ضمني)
- Add في Lost & Found: Module dropdown=outlet — قائمة المنافع من POS/FO family (استنتاج بدرجة عالية).

## 2. مصفوفة الجسور

| الجسر | الاتجاه | النوع | موثق؟ |
|---|---|---|---|
| PMS Users → Care | وارد | هوية | ✅ نصي |
| PMS Dept/Desig → Care | وارد | مرجعي | ✅ نصي |
| PMS MNT Shifts/Locations → Care | وارد | مرجعي | ✅ نصي |
| PMS Rooms/Guests → Care | وارد | حي | ✅ نصي |
| PMS L&F ↔ Care | ثنائي | بيانات | ✅ نصي |
| HRP ↔ Care | — | **لا شيء** | ✅ (غياب موثق) |
| SMS Gateway ↔ Care | ثنائي | تشغيلي | ◐ (سلوك بلا مواصفة) |
| IVR → Care | وارد | تشغيلي | ◐ (ذكر بلا تفصيل) |
| Care → FO Folio | صادر | مالي | ❌ غير موثق (مرشح) |

## 3. موقع Care في Knowledge Graph (تحديث الرسم)

```
                    ┌─ FO/PMS ──── [Users·Depts·Desigs·Shifts·Locations·Rooms·Guests·L&F] ──┐
                    │ (7 قنوات واردة — أعلى اعتماد أحادي)                                    │
[CARE] ═════════════╡                                                                     │
   │  ↕ SMS Gateway (I-CA-07)  ↕ IVR (I-CA-08)                                          │
   │  ✕ HRP (UNK-010: لا جسر — مخزنان مستقلان)                                            │
   └─ (مرشح غير موثق) → FO Folio (I-CA-09)                                                │
```

## 4. عائلة التجميد — الإضافة الخامسة
FO (يومي) → MGT (شهري) → FAS (سنوي) → HRP (رواتب مقفلة) → **Care (روستر: ماضٍ محمي V-CA-02/03)** — يكتمل بذلك نمط قابل للتعميم: "كل كيان زمني تشغيلي في 6i له نافذة تحرير وحيدة تتجه للمستقبل".
