# 08 — التقارير (Reports) — وحدة MNT

> **15 تقريراً/استعلاماً**: 10 تقارير قياسية + **استعلام تفاعلي معدِّل (Complaint Status Q)** + **محرك طباعة مستندات** + **تصدير بارامترات عابر للوحدات إلى Excel** + قائمة قراءات. كل التقارير بنمط: فلاتر → عرض → طباعة (و9 منها بنمط معيار/نطاق/ترتيب ثلاثي).

---

## 1. Complaints List (RPL ص2-4)
- **الغرض:** "list of complaints registered during a specified date range".
- الفلاتر: نطاق تاريخ · **Location أو Department** · الحالة **All/Pending/Closed**.
- الاستخدام: السجل الإداري الشامل للشكاوى.

## 2. Duty Chart (RPL ص4-5)
- **الغرض:** "list of employees on the predefined shifts... **on which date which employee is assigned which shift**".
- الفلاتر: نطاق تاريخ فقط.
- **شرط مسبق موثق:** "first the Shift should be defined under 'Define Shifts'... and shift should be assigned... under 'Assign Shifts'" — تقرير مشروط بالتهيئة (نمط نادر التصريح).

## 3. Complaint Status (Q) ⭐ (RPL ص5-7)
- **الغرض:** "view and print all the complaints that are **Pending, Work in Progress and also that are Closed**".
- الفلاتر: Pending/**WIP**/Closed → قائمة.
- **التفاعل:** "Double-click on any of the records to view the Complaint Information. You can **change the status** of the complaint. **Enter the action taken** if the complaint status is changed and **select the priority level**" → Save → رسالة.
- **الدلالة:** تقرير = وحدة تحكم إغلاق (راجع 04 WF-MN-09 و07 §3) — أقوى "Query-as-Console" بعد TEL Error View.

## 4. Equipment Wise Complaints (RPL ص7-9)
- الفلاتر: نطاق معدات From/To (**أو F1**) + نطاق تاريخ.
- الاستخدام: موثوقية المعدات (أعطال معدات بعينها).

## 5. Location Wise Complaints (RPL ص9-11)
- الفلاتر: **Room أو Location** + نطاق + تاريخ + All/Pending/Closed.
- الاستخدام: خرائط الأعطال المكانية (غرف/مواقع).

## 6. Action Taken Report (RPL ص11-13)
- الفلاتر: نطاق تاريخ + **Complaints / PM Schedules / كلاهما**.
- الاستخدام: سجل الإجراءات المنجزة شاملاً الوقائية.

## 7. Employee Wise Action Taken (RPL ص13-15)
- الفلاتر: نطاق تاريخ + **All أو Selected Employee (EMP# + F1)**.
- الاستخدام: **إنتاجية الفنيين** — أساس تقييم الأداء الهندسي.

## 8. Equipment Details List (RPL ص15-17)
- **المعيار (اللافت):** "Equipment/Category/Location **or AMC**" — إخراج سجل المعدات **بمفعّل AMC** (أصول تحت عقد!).
- الفلاتر: نطاق حسب المعيار + الترتيب **by Name/Category/Location**.
- الاستخدام: الجرد الهندسي والمسح التعاقدي.

## 9. PM Schedule List (RPL ص17-19)
- الفلاتر: نطاق تاريخ + معيار **Service Type/Service Rhythm/Equipment** + نطاق + ترتيب **by Category/Location**.
- الاستخدام: مراقبة برنامج الوقائية.

## 10. Resolution Time Report ⭐ (RPL ص19-21)
- **الغرض:** "list of complaints along with **the time taken for resolving it**" — قياس زمن الإغلاق!
- الفلاتر: معيار **Date (نطاق) أو Priority (مستويات)** — تحليل الSLA البدائي (راجع 17-P1: لا SLA حقيقي، لكن القياس موجود).
- الاستخدام: مؤشر الأداء الأهم للوحدة (زمن الاستجابة حسب الأولوية).

## 11. Job Order Report (RPL ص21-23)
- الفلاتر: نطاق تاريخ + نوع **Complaints/PM Schedules** + حالة **Pending/Closed/All**.
- الاستخدام: سجل أوامر العمل وأعمارها.

## 12. Spares and Cost Report ⭐ (RPL ص23-25)
- **الغرض:** "prints the **spares cost and the other costs** occurred for each Complaint/PM Schedule".
- الفلاتر: نطاق تاريخ + معيار **Equipment/Location/Room** + نطاق.
- الاستخدام: **الوحيد المالي الطابع** — يجمع تكلفة قطع الغيار + الفئات الإضافية لكل أمر (تحليل فقط — لا GL — راجع 11).

## 13. Job / Complaint Print Engine ⭐ (RPL ص25)
- **الغرض:** "print the job order or complaints that are generated... in the **local printer**. The print format is based on the **user specifications**".
- المسارات: Complaint → (Complaint#-wise أو date-range) · Job Order → (Complaint أو PMS) + (بJS# أو بتاريخ) + **اختيار Printer** → Ok.
- الاستخدام: **إعادة طباعة مستندات العمل** بلا العودة للشاشات المصدر (يغلق فجوة WF-MN-11 جزئياً).

## 14. Equipment Readings List (RPL ص26-28)
- الفلاتر: نطاق تاريخ.
- **الغرض الموثق:** "record of all the equipments **based on the location** of the equipment for a specified date range".
- الاستخدام: أرشيف القياس (بلا عتبات — راجع P5).

## 15. Parameter Listing ⭐ (RPL ص28-29)
- **الغرض:** "list **all the parameters defined by the user in various modules**. The details are displayed in the form of **MS-Excel reports**".
- **المسار:** "Select the Parameter" → عرض → توليد.
- **الدلالة المعمارية:** أداة **تدقيق تكوين عابرة للوحدات تسكن MNT** — مخرج Excel مباشر (الأولى الموثقة بهذه الصياغة منذ HRP REP)؛ نطاق "parameters" الدقيق UNK-062 (سِمة؟ ماستر؟ إعداد INI؟).

---

## مصفوفة التغطية التحليلية

| البعد | التقارير |
|---|---|
| الزمن (زمن الحل) | **Resolution Time** · Job Order Report (حالة) |
| المكان | Location Wise · Equipment Wise · Equipment Details · Spares (Room/Location) |
| الشخص | **Employee Wise Action Taken** · Duty Chart |
| الأصل (المعدة) | Equipment Wise · Equipment Details · PM Schedule List · Equipment Readings |
| المال (تحليلي) | **Spares and Cost** (+ Cost Analysis داخلياً) |
| الورق | **Print Engine** (+ Job Request/Job Order عبر الحوارات) |
| التكوين | **Parameter Listing** (عابر للوحدات) |

> **الأنماط العابرة:** (1) ثلاثية "معيار → نطاق → ترتيب" في 4 تقارير (8/9/10/12) — نسخة مبسطة من مولدات POS/HRP؛ (2) **Room أو Location** ثنائية في 3 تقارير؛ (3) لا تقرير مواعيد AMC منتهية (راجع 17-P2) ولا تقرير أعطال متكررة (P4) — ثقب تحليلي مزدوج.
