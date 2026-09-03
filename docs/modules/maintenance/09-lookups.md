# 09 — الاستعلامات والمساعدات (Lookups & Helps) — وحدة MNT

> لا قائمة "Lookups" مستقلة في MNT (الوحدة تحمل استعلامها التفاعلي داخل RPL) — القيمة هنا في **عائلة شاشات F1 Help** المتخصصة + **Complaint Status (Q)** كاستعلام معدِّل + **Job Order Help** بمعايير بحث مركبة.

---

## 1. الاستعلام التفاعلي: Complaint Status (Q) ⭐

| البند | الوصف |
|---|---|
| المصدر | RPL ص5-7 (التقرير الثالث) |
| الفلاتر | Pending / WIP / Closed |
| التفاعل | نقر مزدوج → سجل Complaint Information كامل |
| **التعديل** | "You can **change the status**... **enter the action taken**... **select the priority level**" + Save برسالة |
| التصنيف المعماري | **Query-as-Console** — ثاني نمط في المشروع (بعد TEL View-Update Telephone Error) — راجع 07 §3 للمخاطر |

## 2. عائلة شاشات F1 Help الموثقة ⭐

| شاشة Help | المعروض | الاستدعاء | المصدر |
|---|---|---|---|
| **Job Order Help** | "The search criteria can be **Complaints or PM Schedules and further Date, Department, Room or Location**" — بحث مركب رباعي الأبعاد! | F1 في Action Taken (مسار Job Order #) | OPR ص7 |
| Complaint Help | قائمة الشكاوى → Select | F1 في Action Taken (مسار Complaint #) | OPR ص13-14 |
| PM Schedule Help | قائمة الجداول الوقائية → Select | F1 في Action Taken (مسار PM #) | OPR ص14-15 |
| Room/Location Help | "select the room number/location code **based on the room or location option you selected**" — متكيف مع الثنائية | F1 في Register Complaints | OPR ص3 |
| Vendor Help | "vendor details like **name and address** appear on screen" | F1 في Equipment Master (Vendor Code) | OPR ص18 |
| Equipment Help | قائمة أكواد المعدات (واتساعها: Equipment Wise From/To) | F1 في Equipment/PM/Reading | OPR ص18/21/27 |
| Service Type/Rhythm Help | قوائم الماسترات | F1 في PM Master | OPR ص21 |
| Shift Help | قائمة الورديات (نقر مزدوج في خلايا الجدول) | Assign Shifts | OPR ص16 |
| Color Help | "Press F1 to view the **Color options**" | Complaint Priorities | SET ص16 |
| Designation Help | "predefined Employee Designations" | Define Employees | SET ص14 |
| EMP# Help | قائمة الموظفين | Employee Wise Action Taken | RPL ص13 |
| Item Help (Inventory) | أصناف المخازن — "picked up from Inventory stores" | Repair Details | OPR ص13 |
| كود Help العام | "list of predefined codes" (كل ماستر كودي) | كل شاشات SET | SET عام |

- **النمط:** F1 حاضر في كل حقل مرجعي بلا استثناء موثق — و**أعمقها Job Order Help** بمعايير (المصدر × التاريخ × القسم × الغرفة/الموقع): أغنى Help بحثي في وحدة عمليات.

## 3. الاستعلامات الكامنة في التقارير (RPL)

| الاستعلام | طبيعته | المصدر |
|---|---|---|
| Equipment Details List بمعيار **AMC** | جرد "ما هو تحت عقد صيانة" — استعلام تعاقدي | RPL ص15 |
| Complaint Status (Q) — موثق أعلاه | معدِّل | RPL ص5 |
| Duty Chart | روزنامة قراءة فقط (بلا تعديل من التقرير) | RPL ص4 |
| Print Engine | استعلام طباعة بمسارين متشعبين | RPL ص25 |

## 4. ما لا يوجد (الرصد السلبي)

- لا استعلام **لأعطال المعدة المتكررة** (نوع Repeated يُسجَّل ولا يُستعرض مركزياً!) — GAP-MN-P4.
- لا استعلام **AMC منتهية/قاربت** (لا في التقارير ولا الاستعلامات) — GAP-MN-P2.
- لا استعلام **مقارنة قراءات** أو رسوم بيانية (المقارنة متاحة يدوياً من Equipment Readings List فقط).
- لا دفتر عناوين/بحث حر على النمط التشغيلي لTEL — الوحدة أدواتية صرفة.
