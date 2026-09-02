# 05 — قواعد العمل (Business Rules) — وحدة System Setup

> BR-SYS-01..15 موثقة نصاً من SYS-SSP.

---

| ID | القاعدة | النص/السلوك | المصدر |
|---|---|---|---|
| **BR-SYS-01** | علم Supervisor يتجاوز كل الصلاحيات | "Select Yes if the user is in the Supervisor category. This enables **total access to all menu items** in the product" + "The User Access rights can be defined only for those who are **not** categorized as Supervisors" | ص10/ص13 |
| **BR-SYS-02** | كلمة المرور تولَّد آلياً بمجرد اختيار Designation | "Once the designation selected, the password **generates automatically** in the password field, which is of a alphanumeric value" | ص10 |
| **BR-SYS-03** | تعديل المستخدم يستوجب إعادة تعريف الصلاحيات | عند الحفظ بعد التعديل: "a message **prompting the user to redefine Access Rights**" | ص11 |
| **BR-SYS-04** | صلاحيات Add/Modify/Delete محصورة بعناصر معينة | "You can also control the access for Add, Modify and Delete options of **Settings, Transaction and Master menu options**" + "The Options Rights screen is displayed **only for selected menu items**" | ص12/ص15 |
| **BR-SYS-05** | حدود Menu Access: 3 برامج و3-5 رسوم | "You can select a **maximum of three menu programs** only" · "minimum three and a **maximum of five graphs** only" — رسم واحد يوسم Default | ص16 |
| **BR-SYS-06** | تفعيل تخصيص الشاشة الرئيسية يتطلب إعادة دخول | "You have to **logout from the application and login again** to view the options saved" | ص17 |
| **BR-SYS-07** | Applicable From ≥ تاريخ اليوم | "You must enter a date **greater than the current date** to activate the setting active for a future date" — يتكرر في 12+ كياناً (Property/Dept/CC/Desig/UOM/Reason/Currency/Exchange/Tax×3/Religion/Occupation) | كل Ch3 |
| **BR-SYS-08** | تقريب فاتورة الضيف عند الخروج (مستوى الخصيص) | Round Off: **None/Nearer/Higher/Lower** + Round Amount. أمثلة الدليل الرقمية: مبلغ 1000.49 بمقدار 1.00 → None: 1000.49 · Lower: 1000.00 · Nearer: 1000.00 · Higher: 1001.00؛ وبمقدار 0.50: Nearer عند 1000.49→1000.00 لكن **1000.50→1001.00** (الكسر يساوي المقدار يرفع للأعلى في Nearer!) | ص42-45 |
| **BR-SYS-09** | أقسام General تظهر في كل الوحدات عدا Banquet؛ Banquet تظهر في الولائم فقط | Module dropdown في Departments | ص47-49 |
| **BR-SYS-10** | تقييمات الضيوف 1-25 نظامية غير قابلة للتعديل | "the ratings 1 to 25 in the list are **system-defined**... and **cannot be modified**. You can modify the guest comments **from 26 onwards**" | ص84-85 |
| **BR-SYS-11** | تعديل ما بعد الإنشاء محصور جداً | Property: العنوان+الحالة فقط · Designation: Guest Type+الحالة · Currency: Division Method+الحالة · **البقية كلها: الحالة فقط** (Dept/CC/UOM/Reason/Tax×3/Religion/Occupation) — سلسلة Notes ص46-106 | Notes Ch3 |
| **BR-SYS-12** | بحد أقصى 4 أسعار صرف لكل عملة | "A **maximum of 4 entries** can be made for each type of currency code" بترقيم آلي تصاعدي | ص70 |
| **BR-SYS-13** | شرائح الضريبة متصلة آلياً | "Amount From... starts with zero followed by **the next amount of 'Amount To' you have entered**" — البداية = نهاية الشريحة السابقة | ص77 |
| **BR-SYS-14** | ضريبة On Tax تتطلب رقم الضريبة السابقة | "When you select 'On Tax' radio-button, you must enter the **tax number (serial number)**" — تسلسل تكديس ضريبي صريح | ص82 |
| **BR-SYS-15** | تسمية بطاقة الائتمان بحد أرضي يتحقق منه عند التسويات الثلاث | "validates the set limit credit limit during settlement of **Room, Point of Sale and Banquet bills**" | ص93-94 |

---

## حساب الضريبة — الطريقتان الموثقتان رقمياً (ص76-77)

مثال الدليل: Bill = 750$ والشرائح: 0-500 = 2% · 500.01-1500 = 3.5% · 1500.01-2500 = 5% · 2500.01-10000 = 7.5% · +10000 = 10%.

- **Cumulative (تراكمي):** المبلغ كله بشريحة وقوعه: 750 → 3.5% = **26.25**.
- **Non-Cumulative (غير تراكمي/تدريجي):** تقسيم المبلغ: 500×2% = 10.00 + 250×3.5% = 8.75 → **18.75**.

> ⚠️ للترجمة إلى ERPNext: الشريحة التراكمية = Slab 기فكر بالوصول إلى الشريحة؛ غير التراكمية = **Incremental taxation** — Sales Taxes/Item Tax القياسية لا تدعم الاثنتين معاً مباشرة → راجع `16-erpnext-mapping.md` قرار F-SYS-7.

## توزيع الوعاء الضريبي (Tax Structure — ص81-83)

| الخيار | المعنى |
|---|---|
| On Value | على المبلغ الفعلي |
| On Discounted Value | على المبلغ **بعد الخصم** (خصم يخفض الوعاء) |
| On Tax | **على ضريبة سابقة** (رقمها إلزامي) — VAT فوق Service Charge مثالاً |

## تفويض التشغيل (سلسلة الثقة)
"Initially, The **Service Provider** creates user information for the user's **System Administrator** and assigns global rights... Using this privilege, the System Administrator can further define additional user information and grant access rights accordingly" (ص6) — **مستويان**: مزود الخدمة (تفويض مطلق) → مسؤول النظام (تفويض تفصيلي).

## حوكمة السمات وINI
- Module Attributes: "changed by your System Administrator **with the approval of the concerned authority**" (ص31).
- INI: "carried out by the System Administrator... **in consultation with the respective Heads of Departments**. The setting should be done **only after clearly understanding each option**" (ص36).
- سلوك غير قياسي صريح: السمات المفعلة "will function **uniquely from the standard functionality** of relevant menu items" (ص31).
