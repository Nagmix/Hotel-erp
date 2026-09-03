# 01 — البيانات الرئيسية (Master Data) — وحدة MNT

> **12 ماستراً تهيويياً** بعائلتين: (أ) ماسترات كودية صغيرة نمطية (كود 3 محارف + Name 30 + Short Name 10 + قاعدة الخلود "لا حذف — Passive")؛ (ب) ماسترات ارتباطية (مخازن/مراكز تكلفة من Inventory) ومصمم الطباعة. **الموظفون والورديات والمهارات والأولويات الملونة هنا — لا في HRP!**

---

## 1. عائلة الماسترات الكودية النمطية ⭐

> النمط الموحد الموثق (يُكرر حرفياً في 7 ماسترات): كود إلزامي بمساعدة F1 (قائمة أكواد معرفة مسبقاً) + Name إلزامي (حد أقصى 30، **حد أدنى 3 محارف**) + Short Name إلزامي (حد أقصى 10، حد أدنى 3) + قاعدة: "Once a ... Code is defined, **it cannot be deleted**. The Status of ... code that is not in use can be **made to Passive**. Click Modify to modify any ... details".

| # | الماستر | الكود | حقول إضافية | يُستخدم في |
|---|---|---|---|---|
| 1 | **Location** | 6 محارف ألف-رقمية إلزامي | — | Equipment Master · Complaints Registering · Reports (SET ص3-4) |
| 2 | **Equipment Category** | 3 محارف | — | تصنيف المعدات + التقارير؛ أمثلة: Electrical, Air conditioning, Laundry (SET ص5-6) |
| 3 | **Cost Category** | 3 محارف | — | "additional charges incurred during the **repair/maintenance**" → **Action Taken + التقارير** (SET ص6-7) |
| 4 | **Shift** | 3 محارف | **Starting Time · Ending Time · Shift Order** | "Shift Master Program and in the **Duty Chart Report**" (SET ص8-9) |
| 5 | **Service Type** | 3 محارف | — | أمثلة موثقة: **Overhauling, Decarburizing, Lubrication** → PM Schedule Master (SET ص10) |
| 6 | **Service Rhythm** | 3 محارف | **No of Days** — "between two consecutive service rhythms" | محرك جدولة PM (SET ص11-12) |
| 7 | **Skill** | 3 محارف | — | Define Employees + "assigning shifts and tasks" (SET ص12-13) |
| 9 | **Complaint Priority** | 3 محارف | **Priority Order · Color (F1 → خيارات ألوان!)** | "prioritization is done for each task during the **Job Order generation**" (SET ص15-16) |

- **دلالة عائلية:** 7 من 12 ماستراً بنفس النمط الحرفي — أقوى "عائلة نمطية" بعد عائلة أكواد POS؛ الموقع وحده بكود 6 (البقية 3).
- **الخلود السلوبي:** الحذف ممنوع والمخرج هو Passive — عائلة "الإسكات لا الإعدام" الرابعة في المشروع (بعد موظفي HRP وعملاء AR وأصناف MGT).
- **⚠️ تنويه مصدر تعارض:** ملاحظة SET حرفية تقول "Once a **Shift** is defined, it cannot be deleted. The Status of **Category** code..." — خطأ تحريري في الأصل (استنساخ ملاحظة Category) — يوثق كما هو مع تصحيح استنتاجي: القاعدة تنطبق على Shift نفسها.

## 2. موظفو الهندسة (Define Employees) ⭐

| الحقل | المواصفات الموثقة | ملاحظات |
|---|---|---|
| Employee # | "maximum of **7 numeric characters**" إلزامي + F1 | **رقمي خالص** — مخالف لنمط الأكواد الألف-رقمية في الوحدة كلها؛ لا ذكر لتوليد آلي |
| Name | 30 محرفاً ألف-رقمياً، إلزامي، حد أدنى 3 | — |
| Designation | **3 محارف ألف-رقمية**، إلزامي، F1 لقائمة Designations المعرفة | المسمّى الوظيفي **كود** يُختار — ماستر مسميات غير مرئي (مصدره؟ UNK-059) |
| Skill | "Select the employee's **skill level** from the list provided" | من Define Skills — الرابط المهاري للإسناد |

- **المركز المعماري:** "define **all the employees in the Engineering Department** and their respective skills" — **مخزن موظفين خامس** بجزر معزولة (HRP الكانونية + Care + SLM/FO-Executives + مشغّلو TEL الضمنيون) — **UNK-038 تتسع للمرة الخامسة**.
- Assignment بالورديات "can be made **only to those employees defined in the Define Employees option** in this module" — عزلة إدارية مقصودة.
- **لا يوجد في الماستر:** تاريخ تعيين، قسم، راتب، مستخدم نظام — الحد الأدنى التشغيلي فقط (رقم/اسم/مسمى/مهارة).

## 3. الأولويات الملونة (Complaint Priorities)

| الحقل | المواصفات |
|---|---|
| Priority | 3 محارف + F1 |
| Priority Order | "Enter the **order** of the priority being defined" — ترتيب خطورة |
| **Color** | "Press **F1** to view the Color options. Select the desired color **to tag it to the priority**" |

- **الدلالة:** أولوية = (كود + ترتيب + **لون**) — ثلاثية تُستهلك عند Job Order Generation حيث "the record will be **highlighted in the color** that was set for the priority level" (OPR ص24).
- "The different levels of priorities at which the **Complaints/PM Schedules** have to be addressed" — الأولوية تشمل مساري الشكاوى والوقائية معاً.
- **UNK-060:** لوحة الألوان — ثابتة أم قابلة للتمديد؟ (المصدر F1 يعرض "Color options" بلا جرد).

## 4. الارتباطات الهندسية بمخزون MGT ⭐

### 4.1 Identify Engg Store (s)
- "Stores associated with **Engineering items**. Select from the list of **all stores defined in the Inventory module**" (SET ص17).
- آلية: قائمة **checkbox** — "A store can be checked or un-checked by clicking on it. **A minimum of one store has to be selected**".
- الاستهلاك: "used to pick the **Spare parts and other items in the Equipment Master and Action Taken** programs" — أي أن كل اختيارات الأصناف في الوحدة مقيّدة بهذا التحديد.
- المصدر الحرفي: "defined in Fortune using the **Store code Definition option under the Customize sub module of the Material Management module**" — إحالة MGT نصية كاملة (I-MN-01).

### 4.2 Identify Engg Cost Center
- "Cost Centers associated with the Engineering items. Select from the list of all Cost Centers defined in the **Inventory module**" + **حد أدنى مركز واحد** (SET ص18).
- الاستهلاك: "Information recorded here is used in the **Action taken option during Cost Analysis**" — مركز التكلفة يظهر في شاشة Repair Details (OPR ص13).
- المصدر: "cost center code Definition option under the **Customize sub module of the Material Management module**" (I-MN-02).

> **دلالة معمارية:** MNT لا تملك مخازنها ولا مراكز تكلفتها — تستعيرها من MGT **بالانتقاء** (view/list وليس مزامنة) — نمط "المستهلك الانتقائي" الذي رأيناه في MEM (مصادر FO) وSLM (ماسترات FO-مستضافة).

## 5. مصمم الطباعة العام (User Defined Print Forms) ⭐

> **ماستر تصوير نادر التوثيق في المشروع:** محرر نماذج طباعة كامل بمفردات مشاريع وأدوات — يوثق هنا لكنه **أصل مشترك** تستهلكه كل الوحدات (قائمة اختيار Module/Restaurant وقائمة أنواع Bill print/KOT Print/NC Bill Print/Invoice Print بصياغة POS-محورية — راجع 15 §5 و12).

| العنصر | المواصفات الموثقة |
|---|---|
| المشاريع | New/Open/Delete/Browse/Save/Print/Print Preview — دورة حياة مشروع طباعي كامل |
| Page Layout | "Set the **Header Row value, Footer row values** and select the format for page continue... **The sum of Header rows, Footer rows, body rows must be equal to the total length of the stationery** (**6 rows = 1 Inch**)" — حساب محطية رقمي حرفي! |
| Match Samples | "take a **sample printout**... **Printer = Print match samples**" + عدد النسخ + المحارف الأفقية/العمودية — معايرة قياس قبل الاعتماد |
| Tool Box | "all the possible fields or column names in the report. You can select the required names" — **نقر مزدوج** للإضافة، ثم سحب للعمود |
| خصائص الحقل (F4) | Line # · Left position · Width · Alignment · **Print From/To** (بتر النص الطويل حسب المحطية!) · **Last Page** ("field in the last page on a multiple page bill... **UserId** – displayed only in the last page" — مثال حرفي) |
| Body Details | Top Line # · Left · Rows · Columns (بـF4)؛ وخصائص عمود مفرد بـ**F3**: Width · Print Bold |
| Logo | "insert a logo... Caption (non-editable) · Width · Height · **Picture: browse the image and upload**" |
| أدوات المحاذاة | Scales (مساطر أعلى/جانبية) · Grid Lines · Status bar · **Lock controls** ("lock all the fields... to prevent the change in the alignment... you can still move the fields with **Ctrl + arrow keys**") |
| التفعيل | "File = New = **Make Project Active**" — لا تحرير قبل تفعيل المشروع! |
| تسلسل الإنشاء | اختيار Module/Restaurant → نوع البرنامج (Bill/KOT/NC Bill/Invoice) → **Printer Type** (Normal/**Slip Printer** — الافتراضي Normal) → Description ("Suppose you are creating debit notes, then give the description as Debit note") |

- **دلالة:** هذا المصمم هو الطبقة التي تجعل "The print format is **based on the user specifications**" في Job/Complaint Print Engine (RPL ص25) ممكنة — كل مستندات الطباعة الحرّة تمر من هنا.

## 6. جرد حقول الماسترات (ملخص)

| الماستر | عدد الحقول الموثقة | مفتاح |
|---|---|---|
| Location | 3 | الكود (6) |
| Equipment Category / Cost Category / Service Type / Skill | 3 لكل | الكود (3) |
| Shift | 5 | الكود (3) |
| Service Rhythm | 4 | الكود (3) |
| EngEmployee | 4 | Employee # (7 رقمي) |
| Complaint Priority | 4 | الكود (3) |
| Engg Stores / Cost Centers | — (انتقاء checkbox) | متعدد |
| UDPF Project | ~12 مواصفة | الوصف + النوع |
| **الإجمالي** | **~30 حقلاً موثقاً + 4 محددات انتقاء** | — |
