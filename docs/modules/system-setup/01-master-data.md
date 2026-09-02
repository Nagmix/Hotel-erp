# 01 — البيانات الرئيسية (Master Data) — وحدة System Setup

> كل كيانات General Setup (الفصل 3) + كيان المستخدم/المجموعة (الفصل 1). القاعدة العامة الموثقة: **Applicable From + Status Active/Passive + تعديل مقيد بعد الإنشاء**. الحقول موثقة من جداول المتن (ص8-109) لأن المستخرج الآلي التقط صفر جداول لهذا الملف.

---

## 1. كيان المستخدم (User) — Ch1 §1 ص9-12

| الحقل | النوع/الطول | القواعد الموثقة |
|---|---|---|
| User | أبجدي-رقمي ≤10 | **معرّف الدخول** ("used to log in to the application") |
| Name | أبجدي-رقمي ≤40 | الاسم الكامل |
| Short Name | أبجدي-رقمي ≤10 | "used in **reports and lookups**" (نمط موحد عبر النظام كله) |
| Designation | قائمة (من Designations) | اختياري قابل للتحديث لاحقاً — **واختياره يولّد كلمة المرور آلياً!** ("Once the designation selected, the password generates automatically... which is of a alphanumeric value" ص10) |
| Group | قائمة/نص حر | معرَّف من المستخدم؛ "To define a new group, **type the group name in the Group field**" (ص9) — إنشاء مجموعة بالمفتاح |
| Supervisor | Yes/No | Yes = "total access to **all menu items** in the product" (ص10) |
| Password | توليد آلي | أبجدي-رقمي؛ إعادة التوليد من User Management (المشرف) والنص الجديد **يُعرض مكشوفاً في العمود** (ص39) |
| Password Expires | رقمي ≤3 خانات | عدد الأيام قبل إلزام التغيير |
| Status | Active/Passive | Passive = غير قابل للدخول (إعادة التنشيط من User Management) |

**تعديل المستخدم:** Modify → "a message prompting the user to **redefine Access Rights**" (ص11) — تعديل بيانات المستخدم **يُبطل/يستوجب مراجعة الصلاحيات**.

## 2. كيانات المجموعة والصلاحيات — Ch1 §2-4

| الكيان | الحقول/الأبعاد | المصدر |
|---|---|---|
| User Access | User Classification (Groups/Users) × Main Module × Sub Module × عناصر القائمة × حقوق **Add/Modify/Delete** (نافذة Options Rights تنبثق للعناصر المؤهلة فقط: Settings/Transaction/Master) + أزرار De-assign all/Assign all | ص12-15 |
| User Menu Access | User × Menu Programs (**max 3**) × Graphs (**min 3/max 5** + علم Default لعنصر واحد) × Guest Information (checkbox) × Statistics (checkbox) — يسري بعد **خروج/دخول** | ص15-17 |
| Report Access | User × Module × Report × **Spool (Y/N)** × **Export (Y/N)** × Format (**Excel/Open Calc/Direct**) — التبديل بالنقر المزدوج أو Space/Enter | ص17-19 |

## 3. Property Codes — Ch3 §1 ص41-46

| الحقل | النوع/الطول | القواعد |
|---|---|---|
| Applicable From | تاريخ ddmmyy | **> = اليوم** (لتاريخ مستقبلي)؛ افتراضياً اليوم |
| Property Code | أبجدي-رقمي ≤3 | معرّف الخصيص |
| Name | أبجدي-رقمي ≤30 | — |
| Short Name | أبجدي-رقمي ≤10 | للتقارير والاستعلامات |
| Round Off | None/Nearer/Higher/Lower | مع **Round Amount** رقمي — يطبق على "guest bill during check-out" (أمثلة رقمية كاملة في BR-SYS-08) |
| Address | نموذج فرعي | زر Address يفتح شاشة عنوان كاملة |
| — | — | **التعديل مسموح للعنوان والحالة فقط** (ص46 Note) |

**دلالة:** "A property can be a Hotel, a Resort, an Inn, a Motel, a Club, a Bar or a Restaurant, a Food Court, a Hotel Management School" (ص41) — النموذج متعدد الخصائص.

## 4. Departments — Ch3 §2 ص46-50

| الحقل | النوع/الطول | قواعد |
|---|---|---|
| Applicable From | ddmmyy | ≥ اليوم |
| Department Code | أبجدي-رقمي ≤4 | — |
| Name | ≤30 | أمثلة الدليل: Finance & Accounts · Human Resource & Administration · Sales & Marketing · Front Office |
| Short Name | ≤10 | — |
| Module | **General / Banquet** | General: "department name/s gets displayed in certain menu items of **All modules... excluding the Banquet module**"؛ Banquet: يظهر في وحدة الولائم **فقط** (ص47-49) — **فلتر ظهور لا تصنيف محاسبي** |

**التعديل:** الحالة فقط (ص50 Note).

## 5. Cost Centers — Ch3 §3 ص50-53

| الحقل | النوع | ملاحظات |
|---|---|---|
| Applicable From / Cost Center Code (≤4) / Name (≤30) / Short Name (≤10) | — | التعريف المفهومي: "units or divisions of a department or a department itself that add to the expenses of the Organization, indirectly contributing to its income or profits" (ص50) |

**التعديل:** الحالة فقط.

## 6. Designations — Ch3 §4 ص53-57

| الحقل | النوع | قواعد |
|---|---|---|
| Designation Code | أبجدي-رقمي ≤3 | "3 digit designation code" |
| Name / Short Name | ≤30 / ≤10 | — |
| **Guest Type** | قائمة نظامية | **Guest**: مسميات الضيوف الرسمية في عناصر قوائم Front Desk · **Others**: مسميات الموظفين في HR & Payroll · **S & M**: مسميات مندوبي المبيعات في Sales & Marketing (ص54-55) — **كيان واحد يخدم ثلاث مجالات بمفتاح تصنيف** |

**التعديل:** Guest Type + الحالة فقط (ص57 Note) — الاستثناء الثاني بعد Property.

## 7. Units of Measurement (UOM) — Ch3 §5 ص57-60

| الحقل | النوع | ملاحظات |
|---|---|---|
| U.O.M Code | ≤3 | "mainly used in the **Point of Sale, Materials Management and F&B costing** modules" (ص57) |
| Unit Name | ≤15 | — |

**التعديل:** الحالة فقط.

## 8. Reason Codes — Ch3 §6 ص60-64

| الحقل | النوع | قواعد |
|---|---|---|
| Module | قائمة: Banquets · Finance · Front Office · **Gift Shop** · Laundry(s) · Membership · Point of Sale · Purchase · Sales | 9 وحدات — **Gift Shop وحدة غير موجودة بأدلة مستقلة في الحزمة!** [UNCERTAIN] هل هي منفذ POS أم وحدة مستقلة |
| Reason Code | أبجدي-رقمي ≤3 | — |
| Description | ≤20 | "standard reasons... **mandatory for justification**" — لحالات "food & beverages order modification or cancellation, attribution of discount and tax exemptions" (ص60) |

**التعديل:** الحالة فقط.

## 9. Currencies — Ch3 §7 ص64-69 ⭐

| الحقل | النوع | القواعد |
|---|---|---|
| Currency Code | ≤3 | — |
| Name / Short Name | ≤30 / ≤10 | — |
| Type | **Currency / Travellers Cheque** | نوعان نظاميان |
| Local Currency | **Local / Foreign** | — |
| Standard Rate | رقمي | "in local currency. The valuation is based on that standard rate. **By default, one is taken**" — للعملة الأجنبية وشيك السياحة فقط |
| Million/Lakh | قائمة | صيغة عرض الأرقام (مثال هندي: Lakhs 99,99,999.00) |
| **Division Method** | checkbox | التحويل بالقسمة بدل الضرب: "If you have 5000 USD and the Exchange Rate for a USD is 49.00... Exchange Value = 5000÷49 = 102"؛ افتراضياً **Multiplication** (5000×49=245,000) (ص65-66) |
| Text before Decimal | ≤20 | "US$ 150.10" / "Bahraini Dinar 1000.500" |
| Text after Decimal | ≤20 | "US$ 150.10 **cents**" / "INR 200.50 **paisa**" |
| Decimal Length | قائمة 0/1/2/3 | دقة الكسر النقدية لكل عملة |

**التعديل:** الحالة + **Division Method** فقط (ص69 Note) — الاستثناء الثالث.

## 10. Exchange Entry — Ch3 §8 ص69-71

| الحقل | النوع | القواعد |
|---|---|---|
| Currency Code | ≤3 | — |
| Serial # | آلي تصاعدي | "A **maximum of 4 entries** can be made for each type of currency code" (ص70) |
| Time | رقمي | وقت ضبط السعر |
| Rate | رقمي | — |
| Applicable From | ddmmyy | إصدارية زمنية للسعر |

## 11. محرك الضرائب (Tax Code → Slab → Structure) — Ch3 §9-11 ص71-83 ⭐

### Tax Code (§9)
| الحقل | النوع | قواعد |
|---|---|---|
| Code | ≤3 | — |
| Name / Short Name | ≤30 / ≤10 | — |
| **Applicable To** | checkboxes | **Front Office · Point of Sale · Banquet · Purchase** (فقط!) — يحدد أين يظهر الكود |

### Tax Slab (§10)
| الحقل | النوع | قواعد |
|---|---|---|
| Module | قائمة: Front Office · Laundry · Laundry (S) · Purchase · Banquets · Restaurant · **ROOM SERVICE** | 7 أهداف |
| Slab Code | رقمي ≤4 | — |
| Description | ≤30 | — |
| Tax Code | F1 | ربط بالكود |
| **Cumulative Tax** | Yes/No | تراكمي: كامل المبلغ بشريحة وقوعه (750→3.5%=26.25)؛ غير تراكمي: تقسيم المبلغ على الشرائح (500×2%+250×3.5%=18.75) — **مثال الدليل الرقمي الكامل** (ص76-77) |
| Serial # | آلي من 0 | ترقيم الشرائح |
| Amount From | آلي | "starts with zero followed by the next amount of 'Amount To' you have entered" — **استمرارية آلية للشرائح** |
| Amount To | رقمي | — |
| Cal. Type | Percentage/Amount | طريقة الحساب |
| Factor | رقمي | النسبة أو المبلغ |

### Tax Structure (§11)
| الحقل | النوع | القواعد |
|---|---|---|
| Module | قائمة 7 (مثل Slab + Room service) | — |
| Tax Structure | رقمي ≤3 | — |
| Description | ≤30 | — |
| Tax # | آلي من 1 | ترتيب الضريبة داخل البنية |
| Tax Code | ≤3 | — |
| Calculation Type | **Percentage / Amount / Slab** | Factor لا يُستعمل مع Slab؛ Slab # يُستعمل مع Slab فقط |
| Factor | رقمي | النسبة/المبلغ |
| **On Value** | radio | ضريبة على المبلغ الفعلي |
| **On Discounted Value** | radio | على المبلغ بعد الخصم |
| **On Tax** | radio | **ضريبة فوق ضريبة** — "include the tax on another tax" + إلزام إدخال **Tax #** (رقم الضريبة السابقة) — التسلسل الضريبي |

**التعديل (الثلاثة):** الحالة فقط. Slab له أزرار Save/Modify/Delete في الشاشة (ص79).

## 12. Guest Comments — Ch3 §12 ص83-86

| الحقل | ملاحظات |
|---|---|
| Code | آلي |
| Description | ≤30 |

**القاعدة الفارقة:** "the ratings 1 to 25 in the list are **system-defined** which includes Excellent, Good, Satisfactory etc… and **cannot be modified**. You can modify the guest comments **from 26 onwards**" (ص84-85) — تقييمات استبيان الضيوف (Guest Survey Template في FO وPOS).

## 13. Program ID for Print Forms — Ch3 §13 ص86-93

| البعد | القواعد |
|---|---|
| Program ID | ≤7 أبجدي-رقمي — لكل نموذج طباعة |
| Print Option | **LPT1/LPT2/COM1/COM2/COM3/USB** — USB "to view the report through BroadgunPdfMachine and PrinoPdf" (تحويل PDF!) |
| التسمية | القياسية بكود زبون 001 (`FM001BL`)؛ المخصصة بكود زبون الخاصية (`FM326BL` لـ ABC Hotel) — "A unique code is assigned to each customer for license validation" |
| الوحدات | Front Office · A/C Receivables (1)(2)(3) · Laundry |
| جدول النماذج الموثق | FO: Resv.Voucher FM001VO · Meal Voucher · Tax Form [Luxury Tax] FMIDSLT · Service Voucher · Exchange Print FM001EC · Coupon Form FMLEMCP · Reserved Guest Msg. FM001RG · In House Guest Msg. FM001GM · Pre Reg.Card FMIDSPR · Check Out Bill FM001BL · Departure Slips · Whitney Slips. AR: Bill Covering AR001IN · Reminder AR001RM · Receipt Voucher AR001RC · Balance Confirmation AR001BC · Pre Paid Voucher · Credit/Debit Note FA001DN. Laundry: Laundry Bill LA001BL |
| مرجعية التعريف | "The format for the print forms is pre-defined using **User Defined Print Forms** menu item in the Setup menu under Front Office module. The same option is available in the Setup menu of Point of Sale, Accounts Receivable, Banquets, Financial Management, Materials Management, Maintenance Management and HR & Payroll" — أما MM/FM/HRP/Maintenance فتعرَّف "using **Print Forms under Setup menu of Financial Management**" (ص93 Note) |

## 14. Setup Credit Cards — Ch3 §14 ص93-96

| الحقل | النوع | قواعد |
|---|---|---|
| Credit Card Type | ≤10 | نوع البطاقة |
| Floor Limit | رقمي 12 خانة + كسران | "Ex: 100000000000.00" — يُتحقق منه "during settlement of Room, Point of Sale and Banquet bills" |
| Card File Drive / Conversion Id | **Not Applicable** (نصاً!) | حقول موروثة معطلة — دليل على تاريخ تطوري |
| — | + | "setup interface to third party equipment or device to get online authorization" |

## 15. Print Bill Message — Ch3 §15 ص96-99

| الحقل | القواعد |
|---|---|
| From Date / To Date | فترة الصلاحية (From = اليوم افتراضياً) |
| Subject | ≤10 حرفاً (مع المسافات) |
| Outlet | متعدد |
| Message | ≤100 حرفاً |

## 16. Religions / Occupations — Ch3 §16-17 ص99-106

| الكيان | Code | Description | الاستهلاك | التعديل |
|---|---|---|---|---|
| Religions | ≤2 | ≤30 | "selected at the time of creation of **HR Payroll Master and Guest History**" (ص99) | الحالة فقط |
| Occupations | ≤2 | ≤30 | "quick selection during creation of **Guest and Staff** details" (ص103) | الحالة فقط |

## 17. Parameter List + Group Nationality — Ch3 §18-19 ص106-109

- **Parameter List:** "view the settings in the system... print, spool, and export" + **Show All Records** (Active+Passive؛ بدونه Active فقط) — تقرير إعدادات شامل.
- **Group Nationality (§19):** [UNCERTAIN] — صفحة ونصف: شاشة + F1 Help + Select + Save بلا جداول حقول ولا شرح وظيفي؛ غير مدرجة في TOC (يوقف الفهرس عند 18).

## 18. ملخص أطوال الحقول (لنموذج البيانات)

| الكيان | الكود | الاسم | Short Name |
|---|---|---|---|
| User | 10 | 40 | 10 |
| Property | 3 | 30 | 10 |
| Department | 4 | 30 | 10 |
| Cost Center | 4 | 30 | 10 |
| Designation | 3 | 30 | 10 |
| UOM | 3 | 15 | — |
| Reason Code | 3 | 20 (وصف) | — |
| Currency | 3 | 30 | 10 |
| Tax Code | 3 | 30 | 10 |
| Tax Slab (رقمي) | 4 | 30 (وصف) | — |
| Tax Structure (رقمي) | 3 | 30 (وصف) | — |
| Guest Comment (آلي) | — | 30 | — |
| Credit Card Type | 10 | — | — |
| Religion / Occupation | 2 | 30 | — |
| Program ID | 7 | — | — |
