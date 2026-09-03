# 16 — التخطيط لإعادة البناء على Frappe/ERPNext (ERPNext Mapping) — وحدة Care

> **F-CA-1..10**: قرارات الترجمة. **كفاءة البذرة عالية جداً** (أعلى نسبة في المشروع بعد BNQ): Issue/ToDO + Shift/Attendance + Notification/SMS — **3 أصول مخصصة فقط** (مفسر أوامر SMS، لوحة الروستر D&D، حسابات التصعيد).

---

## 1. مصفوفة التحويل الأساسية

| مكوّن Care | مرشح Frappe | الجهد | ملاحظات |
|---|---|---|---|
| Task/Incident | **Issue** (Issue Type = Main, مؤشر Priority, وصف، مرجع غرفة/ضيف) | بذرة | مع حقول مخصصة: est_minutes, esc_level, runner |
| تعريف المهام | **Issue Type + Template** أو doctype مخصص TaskDef | صغير | EscTimeout[4] child table |
| Multi Task | مجموعة Issue Templates → توليد N Issues | صغير | سكربت إنشاء متسلسل |
| Employee المحلي | **Employee (HRMS)** + Care Profile child | صغير | F-CA-2 قرار التوحيد |
| Reporting Link | **Reporting To** في HRMS (already exists!) | بذرة | نفس الدلالة |
| Agent/Supervisor | **Roles** (Care Agent / Care Supervisor) | بذرة | مع Permissions مخصصة |
| Define Rights | **Role Permissions Manager + User Permissions** | بذرة | نمط Frappe الأمثل |
| Restrict Reports | **Report Permission + Print Format** | صغير | Spool/Export/Format |
| الروستر | **Shift Assignment** (جدولي) أو Shift Request | متوسط | الواجهة D&D = أصل مخصص F-CA-6 |
| Staff Login/Logout | **Employee Checkin** (in/out) + عهدة | صغير | checkin_type=IN/OUT |
| Group SMS | **Notification** + SMS Gateway | بذرة | مستلمون متعددون |
| Lost & Found | doctype مخصص L&F (+ عرض PMS) | صغير | F-CA-9 |
| التقارير 20 | **Query Report + Frappe Charts** | متوسط | 7 Charts + 3 Drilldown |
| Supervisor Lookup | ** لوحة Kanban/List حية** | متوسط | live updates |
| Manual Entry | Form مخصص سريع | صغير | + قسم بيانات الضيف الحية |
| SMS ثنائي الاتجاه | **SMS Gateway Settings + Webhook** | **أصل مخصص F-CA-3** | مفسر `# S`/`# C` |
| التصعيد | **Scheduled Event** (scheduler دقيقي) | متوسط | F-CA-5 بمحرك SLA |

## 2. القرارات المعمارية (F-CA)

### F-CA-1: هوية موحدة عبر PMS=Frappe
User واحد + Roles (Care Agent/Supervisor) + User Permissions (Department) — يلغي مشكلة "المشرف يرى قسمه فقط" بجعلها User Permission قابلة للتهيئة (مع انتباه إلى انعكاس BR-CA-18).

### F-CA-2: توحيد كيان الموظف (حسم UNK-010 هندسياً)
- **القرار**: Employee (HRMS) هو الكيان الوحيد + child table `care_profile` (mobile/pager/walky/extension/email/photo).
- **السبب**: حل E-CA-16 (مغادرة موظف بقاء مهامه)، ومزامنة الأسماء، وأخذ Reporting To الجاهز.
- الأقسام/التصنيفات: Department + Designation (فريدة Frappe) — تلقائياً توحّد أبعاد PMS.

### F-CA-3: طبقة SMS Reply Processor (الأصل المخصص الأول)
- webhook من المزوّد → مطابقة الرقم على LoginSession النشطة (عهدة الموبايل!) → تحليل `# S`/`# C` → انتقال حالة Issue → ردود النظام الموثقة حرفياً (راجع 13 §4 — رسائل الأصل نفسها تُعاد استخدامها كقوالب).
- إخطار إغلاق المشرف للحاضر = Notification منفصل.

### F-CA-4: مصادر الورديات/المواقع
Shift Type + Location doctypes عامة تشاركها MNT (المصدر الأصلي "Maintenance module in PMS") — توثيق I-CA-03.

### F-CA-5: محرك SLA/التصعيد
Scheduled job كل دقيقة: مهام غير مغلقة تجاوزت est → رفع esc_level وفق Reporting To لـ designation المهمة + timeout[] من تعريفها + SMS للمستوى — الأصل الحرفي.

### F-CA-6: لوحة الروستر D&D (الأصل المخصص الثاني)
شبكة شهر × موظف مع FullCalendar-like drag — مع قيود الأصل (ماضٍ محمي، طوابق بعد ورديات، Weekly Off لكل مماثلات اليوم).

### F-CA-7: ترجمة UX الحرفية
Type-ahead (F1) → Frappe Link؛ الألوان → Indicators + رموز؛ الرسائل السفلية → Toast؛ Zoom → pane layouts.

### F-CA-8: ملكية السجلات
بخلاف الأصل (أي وكيل يلغي أي مهمة)، يُقيّد Cancel/Feedback بمالك الجلسة/المشرف — تحسين أمني موثق كفرق مقصود.

### F-CA-9: Lost & Found موحد
doctype واحد مع source (PMS الأصلي→واجهة استيراد) + module (outlet) — يخدم FO وCare معاً.

### F-CA-10: الأرشفة
Retention سياسة للأكوان التشغيلية (Tasks/SMS) — الأصل بلا أرشفة موثقة.

## 3. ما يحتاج بناءً مخصصاً حقاً (خلاصة الجهد)

| # | الأصل المخصص | التقدير |
|---|---|---|
| 1 | SMS Reply Processor + قوالب الرسائل الحرفية | 3-5 أيام |
| 2 | لوحة الروستر D&D | 5-8 أيام |
| 3 | محرك التصعيد الدقيقي + تقارير الإنتاجية (avg variance/escalation ratio) | 3-4 أيام |
| 4 | Supervisor Lookup الحية | 2-3 أيام |
| **الإجمالي** | **~2-3 أسابيع** مقابل أسابيع التخصيص في HRP | أعلى كفاءة بذرة في المشروع |

## 4. ما يُحسم في Phase 6 (مؤجل بقرار)

- فوترة المهام من الأصل (الخيار A/B في 11 §5).
- قناة IVR الحديثة (استبدال telephony حديث).
- إبقاء SMS أم Push (أو الاثنان).
- عمق الأرشفة.
