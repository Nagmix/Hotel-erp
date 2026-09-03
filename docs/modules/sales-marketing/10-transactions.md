# 10 — المعاملات (Transactions) — وحدة SLM

> **16 معاملة تشغيلية موثقة** T-SM-01..16 — طابع الوحدة: **معاملات CRM غير مالية بطبيعتها** (تتبع/علاقات) لكن أثرها المالي يظهر عند الحدود (تحويل→AR، خصم→FO/POS، قفل ائتماني→ثلاث وحدات). **لا ترحيل GL مباشر من أي معاملة SLM.**

---

## 1. معاملات دورة العميل

| ID | المعاملة | المدخلات | الأثر | المصدر |
|---|---|---|---|---|
| T-SM-01 | **Prospect Entry** | بيانات شركة محتملة كاملة + Frequent Travelers | إنشاء سجل Prospect (مستودع منفصل!) | SLT §4 |
| T-SM-02 | **Transfer Prospects** | اختيار من قائمة (No→double-click) + كود جديد (آلي TTT+حرف+مسلسل أو مقترح) | **إنشاء Company Master = فتح كيان AR/FO/POS/BNQ/MEM** | SLT §10 |
| T-SM-03 | **Company Profile Add/Modify** | الحزم الست (أساسية/AR/اتصال/خصم/حاجزين/قائمة سوداء) | تعديل الكيان المركزي المشترك | PRF §7 |
| T-SM-04 | **Update Company Profile** | Old Value → New Value (dropdown البنية) | **تحديث جماعي** لرباط بني الأسعار | PRF §8 |
| T-SM-05 | **Link Rates to Company** | Rate Structure + Tax include/exclude + Package + Amenities | تفعيل أسعار مضمونة CGR في فوترة FO | PRF §9 |

## 2. معاملات التتبع اليومي

| ID | المعاملة | المدخلات | الأثر التحليلي | المصدر |
|---|---|---|---|---|
| T-SM-06 | **Daily Sales Call** | Date/Time/Exec/Account/Contact/Activity/Notes/Follow-up | قاعدة Sales Call + Follow-up Reports + Sales Performance | SLT §6 |
| T-SM-07 | **Entertainment/Gift Entry** | Type (Ent: Type/Outlet/Session أو Gift) + Place + Date + Amount + **Authorizer** | مصروف تسويقي موثق "need to be **accounted by the Sales Executives**" (بلا مسار GL — GAP-SM-P2) | SLT §7 |
| T-SM-08 | **Business Loss Entry** | Company/date/competitor/reason/remarks | قاعدة Business Lost Report + تحليل حصة | SLT §8 |
| T-SM-09 | **F&B Promotion Entry** | مهرجان (مدى/Outlet/راعي/تكلفة/عائدات) | سجل ترويجي (بلا ترحيل) | SLT §2 |
| T-SM-10 | **Daily Occupancy Entry** | Property/date/rooms/%/ARR + breakup أنواع | بيانات تاريخية ما قبل التشغيل → MIS | SLT §1 |
| T-SM-11 | **Company Budgets Entry** | شركة/فترة/تصنيف/room nights/إيراد متوقع × فترات | قاعدة قياس Budget Variance (CGR فقط!) | SLT §3 |

## 3. معاملات المخطط التنفيذي

| ID | المعاملة | المدخلات | المصدر |
|---|---|---|---|
| T-SM-12 | **Appointment Create/Reschedule/Cancel/Transfer** | Time/Contact/Designation/Notes (+سبب في الثلاث الأخيرة +مندوب في Transfer) | SLT §9 |
| T-SM-13 | **Things To Do Entry/Complete** | ساعة + مهمة + Important/Normal + tag completed | SLT §9 |

## 4. معاملات الوكلاء (تُستهلك في FO)

| ID | المعاملة | المدخلات | الأثر الحجزي | المصدر |
|---|---|---|---|---|
| T-SM-14 | **Agent Allocation Entry** | مدى + شركة/Property/RoomType + غرف + **Over-book%** + أيام تأكيد + Week/Day Access | سقف حجز الوكيل + فائض نسبي | PRF §12 |
| T-SM-15 | **Agent Forecast Entry** | مدى + شركة/Property/RoomType + غرف متوقعة | توقع شبه مؤكد (تخطيط إشغال) | PRF §13 |
| T-SM-16 | **Agent Release Dates Entry** | cutoff days لمدد داخل المدى الرئيسي (From مولّد آلياً) | توجيه الحجز **Inside/Outside** عند الطلب | PRF §14 |

## 5. خريطة الأثر المالي عبر الحدود (لا GL داخلي!)

```
T-SM-02 Transfer ─────────────→ AR: كيان جديد (Customer)
T-SM-03/04 Profile/Update ────→ AR: شروط ائتمان (قفل 3 وحدات!)
T-SM-05 Link Rates ───────────→ FO: أسعار تفاوضية في الفوترة
PRF §5 Revenue Discount ──────→ POS/FO: خصم عند توليد الفواتير
PRF §10 Retention Policy ─────→ FO: احتفاظ No-Show (Retention-Cancel)
PRF §11 Cancellation Policy ──→ FO: رسوم إلغاء بحساب الأيام
T-SM-14..16 الوكلاء ──────────→ FO: سقوف وتوجيه الحجوزات
T-SM-07 Entertainment ────────→ (؟) مصروف — مسار غير موثق
```

> **النمط الجوهري:** SLM "مصمّمة قرارات" — كل معاملاتها تولّد **قيوداً سلوكية** تنفذها وحدات أخرى عند حدودها. أثرها المالي كله **مفوَّض (delegated)**.

## 6. خصائص القيد/التراجع

| الخاصية | الموثق | ملاحظة |
|---|---|---|
| Cancel/Reverse | **غير موثق لأي معاملة SLM!** | لا إلغاء تحويل Prospect، لا استرجاع budget — انعكاس كامل لعائلة BNQ/AR Posting القابلة للإلغاء |
| Post/Close دوري | ✗ لا يوجد | لا دورة إقفال شهرية للوحدة (بعكس MEM/HRP) |
| تاريخ القطع | Receivables عرض = Accounting date (عرض فقط) | BR-SM-29 |
| تعديل بعد الإنشاء | Company Profile: Modify موثق · Budgets: multi-period additions | الإضافة لا الاستبدال |

> **دلالة إعادة البناء (R-SM-4):** غياب أنماط التراجع يجعل SLM أنسب وحدة لنمذجة **append-only مع تعديل Profile** — سجلات التتبع immutable والتحويل واحد-اتجاه (Prospect→CGR لا رجعة — على الأرجح بلا "إرجاع شركة إلى prospect" أصلاً).
