# 09 — الاستعلامات (Lookups) — وحدة HRP

> HRP بلا ملف LUK مستقل (استثناء بنية الحزمة — راجع GAP-HR-D02). وظائف الاستعلام مضمّنة في REP §1 (Employee Information) وشاشات التشغيل.

---

## 1. الاستعلامات الموثقة

| # | الاستعلام | المصدر | الوظيفة |
|---|---|---|---|
| L-HR-01 | **Employee Lookup** (REP §1.1) | "view all the details relating to employees by selecting the Property and employee number... Click Prev/Next to navigate to different employee records" | بطاقة موظف تفاعلية بتنقل |
| L-HR-02 | Personal Info | REP §1.2 | قوائم مجمّعة Grade/Dep/CC/Emp |
| L-HR-03 | Blood Grp/Staff/Place | REP §1.8 | معلومات طوارئ مجمّعة |
| L-HR-04 | Personnel Master Search | PNT §1 | "search criteria... (application # criteria...)" — بحث متعدد المعايير بالمرشح |
| L-HR-05 | Change Info Search | PNT §3 | "search for the employee records using any one of the search options" |
| L-HR-06 | **F1 Lists** (كل الشاشات) | SET/PNT | Bank codes / ED codes / Employees / Cal Codes / Attendance codes / Leave groups / Loans / Templates / Reports |
| L-HR-07 | Rate Master Show Details + Address | PNT §4 | بطاقة تعرفة الموظف |
| L-HR-08 | Tag More ED Codes | PNT §8 | استعراض ED codes للموظف (زر في AR Transfer أيضاً) |
| L-HR-09 | AR Transfer Load | PNT §22 | استعراض خصومات AR الجاهزة للنقل |

## 2. أنماط البحث الموثقة

| النمط | المواضع | الإسقاط |
|---|---|---|
| **Search Criteria screen** (اختيار معيار ثم نافذة قيم) | Personnel Master / Change Info / REP معظم التقارير | Filter builder موحد |
| **F1 Help** | كل حقول الكودات | Link field + search |
| **Prev/Next navigation** | Employee Lookup | Pagination |
| **Double-click selection** | User IDs (Rights) / ED Codes (Calculation) / Employee (AR link) | Row selection |

## 3. الفجوة البنيوية

> **GAP-HR-D02:** كل وحدة أخرى تحمل ملف LUK مستقلاً (FOM-LUK 22 · FAS-LUK 9 · ACR لا — ACR أيضاً بلا LUK منفصل لكن فيه 13 تقارير استعلامية داخل RPL... بنية ACR استثنت LUK) — HRP **دمجت الاستعلامات في REP §1** — الدلالة: عند الإسقاط تُبنى lookahead واحدة لبطاقة الموظف (Employee Master view) بدل شاشات متفرقة.

## 4. الاستعلامات الضمنية (غير المصرّحة)

- Leave Master "Closing auto calculate and display" — عرض حسابي.
- Rate Master "total salary amount will display on the right side" — **إجمالي حي** أثناء الإدخال.
- Supplementary: زر عرض ED Code details في AR Transfer.
- PF Statement 3A: "the address in general table will be displayed" — fallback سلوكي.
