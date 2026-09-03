# 16 — الموائمة مع ERPNext/Frappe (ERPNext Mapping) — وحدة MNT

> **F-MN-1..12** — من **أفضل تواءمات المشروع** (تضاهي SLM/Care): نواة الوحدة تنطبق على أصول معيارية ناضجة — **Issue** (شكاوى بأولويات وحالات وإسناد) و**Asset + Asset Maintenance/Maintenance Visit** (الوقائية!) و**Asset Repair** (الإصلاح **باستهلاك قطع عبر Stock Entry — يحل P3 جذرياً!**) و**Shift Assignment** (الورديات). الأصول المخصصة تتركز في **جهاز التوليد/الإسناد (Job Order Console)** وقراءات المعدات. التقدير: **~6 أصول مخصصة / 3-4 أسابيع**.

---

## 1. الخريطة العامة

| مكون MNT | الأصل Frappe/ERPNext | الحالة | القرار |
|---|---|---|---|
| Complaint | **Issue** (+ حقول مخصصة Room/Location/Dept/Type) | ✅ جاهز بنمط | F-MN-1 |
| Complaint Priority + Color | **Issue Priority** (+ حقل لون) | ✅ شبه جاهز | F-MN-2 |
| Equipment Master | **Asset** (+ Asset Category/Location!) + امتدادات | ✅ جاهز بنمط | F-MN-3 |
| PM Master/Entry | **Asset Maintenance + Maintenance Schedule + Maintenance Visit** | ✅ جاهز بنمط | F-MN-4 |
| Action Taken + Repair | **Asset Repair** (يستهلك قطع بـ**Stock Entry**!) | ✅✅ جاهز قوي | F-MN-6 |
| الورديات + Duty Chart | **Shift Type + Shift Assignment** (Frappe HR) | ✅ جاهز | F-MN-8 |
| Employees | **Employee** (وحدة HRMS) | ✅ جاهز — مع قرار جسر | F-MN-8 |
| Job Order Generation | لا مقابل مباشر (أقرب: قوائم + Kanban + إسناد جماعي) | 🔧 مخصص | F-MN-7 ⭐ |
| Equipment Readings + Min/Max | لا مقابل (Asset Log تحريري) | 🔧 مخصص | F-MN-9 |
| ENG#1/#2 + Job Request/Order prints | لا مقابل (Print Format فقط) | 🔧 مخصص | F-MN-10 |
| UDPF (مصمم الطباعة) | **Print Format Builder** | ✅ يستبدل كلياً | F-MN-11 |
| Parameter Listing | تصدير التقارير XLSX الأصلي | ✅ يُستبدل | F-MN-12 |
| تقارير (Resolution/Spares/Duty) | Script Report | 🔧 مخصص | F-MN-5 |

## 2. القرارات التفصيلية

### F-MN-1: Complaint = Issue ⭐
- حقول مخصصة على Issue: `room` (Link Room) · `location` (Link) · `department` · `complaint_type` (Common/Repeated) · `ref_no` (10) · `reported_by`.
- الحالة: Pending/WIP/Closed تُطابق دورة Issue (Open→In Progress→Resolved/Closed) مع تسميات عربية.
- **مكسب غير متوقع:** SLA/إشعارات Issue تحل نصف P1 (عدّاد تقادم) مجاناً.
- أي قسم يرفع: إسناد الدور لكل المستخدمين (07) + اختياري Web Form للشكاوى البسيطة.

### F-MN-2: Priority + Color
- Issue Priority مخصص اللون: حقل `color` (HTML color) + عرض Kanban للأولويات — **الفكرة الأصلية (صف يتلوّن) ترتقي إلى لوحة كانبان** بلا فقدان الدلالة.

### F-MN-3: Equipment = Asset + امتدادات
- Asset يمنح: الكود · الفئة (Asset Category = Equipment Category!) · **الموقع (Asset Location = Location!)** · القيمة والعملة · المزوّد (Supplier!) · تاريخ الشراء/التركيب.
- امتدادات مخصصة: `manufacturer/model/serial` (serial موجود جزئياً) + **child tables**: `Equipment AMC` (vendor+expiry+required) · `Equipment Spares` (item+qty+lead time) · `Equipment Standard Reading` (name+min+max+UOM).
- **F-MN-5 (جسر FAS):** الربط مع الوحدة المستقبلية Fixed Assets في المشروع يتم **بجعل Asset هو مصدر الحقيقة الواحد** — إغلاق GAP-MN-D05 بنيوياً.

### F-MN-4: الوقائية = Asset Maintenance ⭐
- Asset Maintenance Task يقابل صفوف PM Master: `maintenance_type` (Preventive) · `frequency` (Daily/Weekly/Monthly/Quarterly/Half-Yearly/Yearly = **Service Rhythm!**) · start/end date · Task · Vendor.
- **Lag → custom `tolerance_days`** يقيّد Must Complete By (قيد تحقق on_validate — V-MN-16).
- توليد التواريخ: **Maintenance Schedule/Maintenance Visit** (أو scheduler Frappe يولد المهام دورياً) — "dates automatically calculated" يقابلها بالضبط.

### F-MN-6: Action Taken = Asset Repair ⭐⭐ (الأثقل قيمة)
- Asset Repair: failure date · description (=action_text) · downtime · completion (status) · **consumes spare parts via Stock Entry Material Issue إلى cost center** — **يغلق GAP-MN-P3 جذرياً** (الكمية تُخصم من المخزن فعلاً!).
- Cost Analysis (فئة+مزوّد+مبلغ): child doctype مخصص `Repair Cost Line` على Asset Repair (قرار MIS خالص كالأصل — 11 §4).
- أثر جانبي موجب: الصنف "المفتوح" يصبح **Non-Stock Item** أو بند حر في Stock Entry — نفس فلسفة 999999999999 بلا شرِكة!

### F-MN-7: Job Order Generation = جهاز التوليد/الإسناد (Asset #1) ⭐
- **DocType مخصص `Job Order`**: source (Issue/PM Task) · priority · assignee (Employee **أو Supplier** — ثنائية XOR محفوظة) · status.
- **الواجهة:** قائمة موحدة للمرشحين (Issues Pending + PM Tasks المستحقة) **بتحديد جماعي + إسناد جماعي** (List view bulk actions) + **Kanban بالأولويات الملونة** (F-MN-2) — الاستبدال الحديث لشبكة NO→YES.
- مهارة/توافر: عرض skill الفني ومؤشر على الشفت الحالي (من Shift Assignment) — يجعل "based on their skills and availability" قابلاً للتنفيذ فعلاً (كان بالعين!).

### F-MN-8: الورديات = Shift Type + Shift Assignment
- Shift Type (start/end) + Shift Assignment لكل (employee, date) — **دورة ≤31 يوماً تُدار بإدخال دفعة**: واجهة شبكة (fill-down) تحوّل الروستا إلى Shift Assignments.
- Duty Chart = تقرير/تقويم على Shift Assignment (Script Report).
- **قرار الموظفين (يغلق UNK-038 تدريجياً):** الفنيون = **Employee** واحد (مصدر HRP الموحد للمشروع كله) + حقل department=Engineering — **إلغاء المخزن المحلي الخامس** بقرار معماري (يُثبت في 17).

### F-MN-9: Equipment Reading + إنذار (يغلق P5)
- DocType مخصص `Equipment Reading` (asset, datetime, قراءات قيم ضد Std Reading) + **تحقق فوري Min/Max + Notification** للإشراف — الأصل لم ينذر؛ إعادة البناء تصحح النقص (موسوم كتحسين مقصود).

### F-MN-10: بوابتا الطباعة (ENG#1/#2)
- Print Format للـJob Request (من Issue) والـJob Order + Property Setter/setting بديل ENG#: `print_on_register`/`print_on_assign` — الحوار بعد الحفظ يصبح إشعاراً + زر طباعة (قرار 15 §8-5).

### F-MN-11: UDPF → Print Format Builder
- المصمم الكامل (Toolbox/Scales/6-rows=1-inch/Match Samples) **يُستبدل** بـPrint Format Builder + Jinja — يُنقل فقط مفهومان متقدمان عند الحاجة: Last Page وPrint From/To (كسلوك متقدم نادر).

### F-MN-12: Parameter Listing → يُهجر
- Frappe يصدّر أي قائمة/تقرير إلى XLSX أصلاً + المفهوم الوظيفي (تدقيق تكوين) يُغطى بتقارير Standard في مرحلة 8 — لا يعاد بناء التقرير العابر (يُسجل كاستبدال بديل لا كفقد).

## 3. جرد الأصول (Custom Assets)

| # | الأصل | الحجم | يغلق |
|---|---|---|---|
| 1 | **Job Order doctype + Dispatch Console** | متوسط-كبير | تجسيد القلب الإشرافي |
| 2 | Equipment extensions (3 child doctypes + حقول) | صغير | D05 جزئياً |
| 3 | Equipment Reading + Alert hook | صغير | P5 |
| 4 | Print gates + Print Formats (JobRequest/JobOrder) | صغير | ENG#1/#2 |
| 5 | Script Reports (Resolution Time · Spares and Cost · Duty Chart) | صغير-متوسط | التغطية |
| 6 | Roster grid (شبكة الورديات بfill-down) | صغير | UX F2/F3 |

> **الإجمالي: ~6 أصول / ~3-4 أسابيع** — الفجوة الأدنى في المشروع تقريباً بفضل Asset Repair/Stock Entry.

## 4. مخاطر الموائمة

| الخطر | المعالجة |
|---|---|
| Asset مشحون بحقوق مالية (قييم/إهلاك) في ERPNext | تجميد الحقول المالية أو تفعيلها كقرار FAS (F-MN-5) — قرار موحد |
| Issue موجه للدعم الفني (raised_by عميل بريد) | إعادة تسمية عربية "بلاغ" + إخفاء حقول غير ذات صلة |
| Maintenance Schedule في ERPNext مبني على Serial No لا Asset | استخدام Asset Maintenance (المبني على Asset) كأساس — Schedule للSerial لا يلزمنا |
| ثنائية Room/Location | حقلان مخصصان مع تحقق XOR (V-MN-23) |

## 5. ترتيب التنفيذ المقترح (لخارطة الطريق)

1. **المassets المرجعية** (Issue+Priority / Asset+Category+Location / Employee+Shift) — أسابيع خلط منخفضة.
2. **Asset Maintenance + Repair + Stock Entry** — حلقة الوقائية والإصلاح (بما يغلق P3).
3. **Job Order Console** — القلب الإشرافي (مع Kanban).
4. Readings + Alerts + Reports + Print gates — الحزمة الأخيرة.
