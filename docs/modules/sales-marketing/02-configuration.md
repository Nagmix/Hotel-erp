# 02 — الإعدادات (Configuration) — وحدة SLM

> **كل مقابض التهيئة الموثقة للوحدة.** SLM وحدة **ثقيلة الماسترات خفيفة الـINI** — لكنها تُضيف **مفتاحي INI جديدين (#239 و#41)** ووثّقت **Module Attribute #8** من عائلة سمات FO — بلا System Attributes داخلية (بعكس MEM).

---

## 1. مفاتيح INI الموثقة (2 مفتاحان جديدان)

| المفتاح | الوظيفة الموثقة | السلوك | المصدر |
|---|---|---|---|
| **INI # 239** | "Option can be **extended to all users** by changing property.ini flag 239" | Executive Planner: افتراضياً لمندوبي المبيعات المربوطين فقط؛ المفتاح يفتحه لكل المستخدمين | SLT §9 (ص21) |
| **INI # 41** | "To activate the cutoff days validation during Reservation, **Setting # 41 in the .INI file needs to be activated by setting it to '0'**" | تحقق تواريخ التحرر (Release Dates) عند الحجز — **الصفر يُفعّل (عائلة مقلوبة!)** | PRF §14 (ص27) |

> ⚠️ **عائلة INI المقلوبة تتسع:** الصفر يُفعّل — نفس نمط 56/74/220 الموثق سابقاً (FO/HRP). الإجمالي التراكمي: **31+ مفتاح INI** عبر المشروع (راجع سجل INI في 02-configuration لكل وحدة).

## 2. سمات الوحدات المستهلكة (Module Attributes — عائلة FO)

| السمة | الوظيفة الموثقة | المصدر |
|---|---|---|
| **Module Attribute # 8 for Reservations** | في Agent Allocation: "The Week Access column is **dependent on the Module Attribute # 8 for Reservations**. If the Module Attribute is set to **'NO', the system by default shows week access screen** wherein the rooms allocated are attributed to the days selected. If set to **'YES', the system shows day access screen** wherein the rooms can be allocated day wise" | PRF §12 (ص25) |

> **إثراء لجرد FO Module Attributes:** المعروف سابقاً Attribute 16 (Release Stop Posting — FO-CAS)؛ الآن **#8 موثق الوظيفة** (Week/Day Access للحجوزات) — يُضاف لجرد G-3 في FO (gap جزئي قائم).

## 3. الإعدادات الهيكلية داخل الشاشات (ماسترات فعل بدل INI)

| الإعداد | الموضع | الوثيقة |
|---|---|---|
| Include/Exclude Tax for Tariff | نافذة اختيار Rate Structure عند Link Rates — "Select an appropriate option to include or exclude tax for tariff" | PRF §9 (ص19) |
| CGR checkbox في Daily Sales Call | "Select the checkbox to view the **CGR Company codes** available in the company Master" — فلتر مستودع vs CGR | SLT §6 (ص16) |
| Watch List To Date | قيمة تاريخية داخل Company Profile — نطاق مراقبة العميل | PRF §7 |
| Multiple Periods (Company Budgets) | "Click to enter information for a **multiple period for the same company**" | SLT §3 |
| Over Booking (Hotel Position) | "You can view the chart **including Over Booking** by selecting the option" — عرض فقط | SLT §9 (ص15) |
| Show Past Reservation | "Select the checkbox–**Show Past Reservation** to view past reservations" — عرض Reservations في Sales Manager Tool | SLT §11 (ص12) |

## 4. تهيئات مشتركة من وحدات أخرى (تعريفات مرجعية)

| المرجع | الوحدة المالكة | الاستهلاك في SLM |
|---|---|---|
| Company Types | **Front Office Setup** | أول 3 خانات من كود الشركة (COM/TAG/AIR...) |
| Sales Office / Sales Executives / Collection Executives | **Front Office Setup** (نفس البيانات!) | شاشات SLM تعرضها مباشرة — "For more information, refer... under Front Office Setup" |
| Bookers Type Definition | **Front Office Setup** | تصنيف الحاجزين في Bookers Master |
| Billing Instructions / Market Segments | FO (ماسترات مشتركة) | حقول في Company Profile (F1 lookup) |
| User Setup | **System Setup** | خريطة Map Users/Sales Exec |
| Rate Master (Non-rack/Package) | FO (بنية الأسعار) | يُربط بالشركات عبر Link Rates to Company |

> **نمط "الماستر المستضاف":** SLM لا تكرر تعريف 5 ماسترات FO — بل توفر **واجهات وصول ثانية** لها (نفس نمط Care مع PMS). قرار إعادة البناء: مصدر واحد (F-SM-2).

## 5. إعدادات خارجية

| البند | الوثيقة |
|---|---|
| **Microsoft Outlook** كقناة بريد لـCompany Letters — "we can send the letters through **Microsoft outlook as E-Mail with attachments**" | REP §12 (ص13) |
| **Word processing software** لتحرير محتوى الخطابات — "You can use **Word processing software** to create the textual content of the Letter" | REP §12 (ص14) |
| **BMP فقط** لصور الفندق في Hotel Profile — "You can upload only bmp files" | PRF §17 (ص41) |
| تنسيق تاريخ ddmmyy في Revenue Discount Master — "The date format is **ddmmyy**" | PRF §5 (ص6) |

## 6. ما لا وجود له (سلبية موثقة)

- **لا System Attributes داخلية** (بعكس MEM بـ13 سمة).
- **لا مفاتيح INI في REP/LUK** — المفتاحان كلاهما في SLT/PRF.
- **لا User Rights/Access section** في أي ملف — الوحدة الوحيدة حتى الآن بلا أي صلاحيات موثقة (راجع 07-permissions).
- **لا إعدادات عملة داخلية** — العملات تُستهلك من ماستر العملات عند العرض (LUK §3: "in local and foreign currency").
