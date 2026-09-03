# 15 — تحليل تجربة المستخدم (UX Analysis) — وحدة Care

> Care تحمل **أنضج UX تشغيلي في المشروع**: سحب وإفلات، قوائم سياقية، بحث تدريجي، تلوين دلالي، Zoom، آلة حاسبة/تقويم/ساعة مدن — مع غرفة عمليات حية (Supervisor Lookup).

---

## 1. الأنماط التفاعلية الموثقة

| النمط | المواضع | التقييم |
|---|---|---|
| **Drag & Drop** (سحب وإفلات) | الروستر: وردية على الاسم (شهر) أو التاريخ (يوم) | **الوحيد في المشروع** — نقلة إنتاجية حقيقية لتخطيط الطاقم |
| **Right-click Context Menus** | Org Structure (شجرة) + Supervisor Lookup + الروستر (Clear/WeeklyOff/Floors/Assign/Close/Transfer/Extend) | نمط متسق عبر كل الشاشات الجوهرية |
| **Type-ahead** (بحث تدريجي) | Task في Manual Entry + Multi Task + Selected Task (تقرير 10) | 3 مواضع — جاهز للترجمة الحرفية |
| **الغرفة الحية** | Room# → بيانات الضيف فوراً + Pink/Magenta | تقليل إدخال + ترميز لوني فوري |
| **Hover tooltips** | Special Instructions على SMS Status | تلميحات بلا شاشات |
| **Zoom control** | يمين Manual Entry + Close | لوحة للقراءة الجزئية |
| **الأدوات المكتبية** | آلة حاسبة 15 خانة · تقويم · "standard time of the selected city" (dropdown) | مجموعة مكتبية كاملة داخل الشاشة |
| **الإشعار البصري للدُفع** | "A message pops up at the bottom of the screen confirming that the complaint is raised" | Toast-before-toast! |
| **الصف الأبيض عند الاختيار** | Feedback Cancel: "the selected task record will appear in **white color**" | توضيح الاختيار |

## 2. لغة الألوان الدلالية (Color Semantics) — OPR ص30

| اللون | الدلالة | السياق |
|---|---|---|
| 3 درجات أولوية | Low/Normal/High | عمود Priority |
| 4 درجات | Escalation L1-L4 | حالة التصعيد |
| **Pink** | "complaint is raised for **Unoccupied room**" | عمود Guest Name |
| **Magenta** | "complaint is raised for **Other Area**" | عمود Room# |
| **Yellow** | صفوف Designation | شبكة الروستر |
| 'O' | Weekly Off | خلية اليوم |

> **ملاحظة ترجمة**: لوحات الألوان تحتاج تعريف Accessible Alternatives (أيقونات/نصوص) للامتثال (F-CA-7).

## 3. تدفقات الاستخدام الثلاثة (Personas)

### 3.1 الوكيل (Agent) — عالي التردد
`Manual Entry → (Room/Unoccupied/Other) F1 → Task بحث → Special ≤25 → Confirm (+مزيد) → Thank You → مراقبة SMS Status → (Feedback Cancel عند اكتمال) / (Request/Incidents لسجل الغرفة)`
- **نقاط القوة**: أقل ضغطات ممكن لكل شكوى؛ بيانات الضيف تلقائية.
- **نقاط الضعف**: 25 حرفاً فقط للتعليمات الخاصة — قيد صارم يتكرر إزعاجه عملياً (ملاحظة تحليلية).

### 3.2 المنفذ (Runner/Technician) — عبر الهاتف فقط!
- كامل تفاعله بـ SMS نصي: استلام `Complaint #... Est. Time... Priority... Esc Level: 0` → رد `1 S` → رد `1 C`.
- **رؤية UX تحليلية**: هذه **واجهة Frontend كاملة بلا شاشة** — أعظم ابتكار تشغيلي في الحزمة: الموظف الحقلي لا يحتاج كمبيوتر إطلاقاً.
- رسائل الخطأ صديقة ومباشرة (راجع 13 §4).

### 3.3 المشرف (Supervisor) — غرفة العمليات
`Supervisor Lookup → قسم → (مراقبة الألوان) → right-click: Close/Transfer/Extend/Assign → Clear Pending SMS`
- الرؤية مقيدة بقسمه (انعكاس BR-CA-18) بينما "Normal login users" يرون الكل — **قرار UX غريب** يستحق نقشه في إعادة البناء بحذر.

## 4. تقييم جاهزية الترجمة إلى Web (Frappe)

| المكوّن الأصلي | صعوبة الترجمة | المرشح |
|---|---|---|
| Drag & Drop روستر | متوسطة | FullCalendar / شبكة Kanban مخصصة |
| شجرة Org Structure + سياق | منخفضة | Frappe Tree + قائمة سياق مخصصة |
| Manual Entry اللوحة | منخفضة | Form + قسم حي (بيانات الضيف) |
| SMS ثنائي الاتجاه | **عالية** | Gateway + webhook معالج أوامر |
| لوحات التقارير + Charts | منخفضة | Frappe Charts / Query Report |
| ألوان الحالة | منخفضة | Indicators + Badge |
| الرسوم البيانية القديمة (Chart windows) | منخفضة | Charts موحدة |

## 5. مخاطر UX للترجمة

1. **فقدان نمط الهاتف**: الحل الأصلي "صفر شاشة للمنفذ" — أي Web-only سيرغم الفني على جهاز؛ الحل الحديث الأقرب: **Web App موبايل خفيف + Push notifications** بدل SMS (مع إبقاء SMS كاحتياط — F-CA-3).
2. **الرسوم البيانية القديمة** مقيّدة (اختيارات ثابتة) — يجب تعميمها.
3. **الصفوف الصفراء/الألوان** بلا مفاتيح بديلة في الأصل.
4. **Refresh غير موثق**: هل شبكة Supervisor Lookup تتحدث ذاتياً أم يدوياً؟ (UNK-042) — القرار الحديث: WebSocket/Polling.
