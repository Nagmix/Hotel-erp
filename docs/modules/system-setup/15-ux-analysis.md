# 15 — تحليل UX — وحدة System Setup

> SYS-SSP هو **أبعد الوحدات عن الاستخدام اليومي** (مسؤول النظام فقط) لكنه أغنى وحدة بأنماط UI القياسية الموحدة (Identifying Standards ص6-7) — لأنها تُعرض فيه أولاً.

---

## 1. الأدوار والمسارات

| الدور | مساراته في SYS | تكرار الاستخدام |
|---|---|---|
| **Service Provider** (IDS) | إنشاء مسؤول النظام الأول + GUI .dat للتشخيص | مرة عند التركيب + دعم |
| **System Administrator** | كل شيء (Supervisor) — خصوصاً: Users · Access · Attributes · INI · FO Defaults · DB Extract | أسبوعي (مستخدمون) / نادر (إعدادات) |
| **Department Head** (استشاري) | لا دخول مباشر — "in consultation with the respective Heads of Departments" (INI) | بلا شاشة! |
| **الجهة المعنية** (Concerned authority) | موافقة السمات — بلا شاشة | بلا شاشة! |

> **ملاحظة UX معمارية:** سلسلة الحوكمة (موافقة → استشارة) **غير ممثلة في النظام** — أوراق/إجراءات خارجية. البنية الجديدة قد تعيد تمثيلها (workflow موافقة اختياري).

## 2. الأنماط القياسية الموحدة (من SYS-SSP — عمود فقري لواجهة المنتج كله)

| النمط | التفاصيل الموثقة | ترجمة Next.js/shadcn |
|---|---|---|
| **شريط CRUD الأفقي** | New / Modify / Delete (مشروط) / Browse / Prev / Next / Save / Exit | شريط أعلى النموذج أو Actions dropdown |
| **أدوات جانبية** | "Command Window, Internode Communication, Calculator, Calendar, Scratch Pad, Yellow Pages" (زر واحد يفتح القائمة!) | تُدمج: آلة حاسبة/تقويم dock RTL |
| **Status toggle** | Active/Passive — افتراضي Active | Switch مألوف |
| **تذييل التتبع** | User (الداخل الآن) + Last Updated (آخر تحديث بالمستخدم والوقت) | شريط تذييل ثابت في كل شاشة Master — **متطلب انعكاس مباشر** |
| **F1 = بحث مرجعي** | كل حقل علاقة: "Double-click or press F1" → شاشة Help → Select | Command palette/Combobox searchable |
| **نقر مزدوج للتبديل** | صلاحيات (Yes/No) + Format cells + Attributes | Toggle inline في الجداول |
| **الشاشات النقطية** | كل Master: List → Add → Modify → Help (نفس الأربعة) | قالب CRUD موحد |

## 3. تقييم UX للوظائف الرئيسية

### 3.1 Create User (Fig2)
- **قوة:** توليد كلمة مرور آلي يمنع كلمات ضعيفة مبتدئة.
- **ضعف:** لا تأكيد كلمة مرور (غير قابل للإدخال أصلاً!) · Group نص حر يخلق مجموعات بالخطأ المطبعي · Supervisor = مفتاح واحد **بلا تأكيد خطر**.
- **ترجمة:** نفس الحقول + مولد كلمة مرور بعرض منسوخ + تحذير عند Supervisor + Group بـ combobox قابل للإنشاء (تمييز visual).

### 3.2 User Access (Fig3-4 + Options Rights)
- **قوة:** تدريج منطقي (Classification → Module → Sub → Item → Rights).
- **ضعف:** التفاعل التسلسلي البطيء لمنح مئات العناصر؛ Assign-all الخطير (منح كل شيء بزهقة!).
- **ترجمة:** **Role Templates** (نسخ صلاحيات مجموعة → مستخدم) + شجرة Module/Sub/Item مع checkbox ثلاثي الحالة + منح جماعي بتأكيد صريح + diff view.

### 3.3 Restrict Report Options (Fig7-8)
- **ضعف:** جدول ضخم (كل تقارير كل الوحدات!) بتبديل خلية-بخلية.
- **ترجمة:** فلترة عمودية (module) + bulk toggle + قالب "قيّد الكل ثم اسمح" (Secure-by-default معكوس الأصل).

### 3.4 Module Attributes (Fig15)
- **خطورة UX:** نقر مزدوج يقلب مفاتيح **تغير سلوك النظام الأساسي** بلا تأكيد ولا شرح مضمّن (الشرح في وثيقة خارجية!).
- **ترجمة:** وصف inline إلزامي لكل مفتاح + Badge "سلوك غير قياسي" + تأكيد + **سجل تغييرات مضمّن** (الأصل: بلا سجل شاشة).

### 3.5 Tax Structure (Fig47)
- **القوة الوظيفية:** التسلسل On Tax مرئي بالـ Tax#.
- **الضعف:** radios ثلاثة (Value/Discounted/Tax) + حقل مشروط (Tax#) — إدراك معرفي عالٍ.
- **ترجمة:** جدول بنود مع أعمدة مشروطة حسب النوع + معاينة حسابية حية (Amount → tax breakdown) — الأصل: **لا معاينة**.

### 3.6 User Management (Fig S-SYS-19/20)
- **كارثة أمنية مكشوفة:** كلمات المرور معروضة نصاً في الجدول.
- **ترجمة:** زر "إرسال رابط تعيين" بدل العرض.

### 3.7 Dashboard personalization (S-SYS-07/08)
- **سبق وظيفي:** تخصيص برامج قوائم + رسوم (3-5) + Guest Info/Statistics **لكل مستخدم** — بأبعاد محدودة.
- **ترجمة:** Next.js Dashboard قياسي مع تراخيص Widget-aware — يفوق الأصل بمراحل (الرسم الافتراضي + RTL).

## 4. أنماط RTL/تعريب تخص SYS تحديداً

| البند | الأصل | القرار |
|---|---|---|
| Captions | إعادة تسمية يدوية + عرض الاسمين | i18n قاموس كامل ar/en — أسماء نظامية قياسية + تخصيص خاصية اختياري |
| Million/Lakh | صيغة عرض أرقام | **غير متوافق مع سياق عربي** → استبدال بـ Intl.NumberFormat (ar) مع الحفاظ على البنية (مليون نظامي) |
| Text before/after decimal | "US$ 150.10 cents" | يُدعم عبر Intl currency display names — العناصر البنيوية تُحفظ |
| Guest Comments 1-25 إنجليزية | Excellent/Good/... | تُترجم seeded مع أرقام مستقرة |
| أسماء الحقول الإنجليزية | — | تسميات عربية + المصطلح التقني ثانياً (نمط القاموس الموحد) |

## 5. جرد ملاحظات UX للمصممين (Top 8)

1. قالب Master CRUD موحد (List/Add/Modify/Help) — **تقطع 12+ شاشة بنمط واحد**.
2. تذييل User + Last Updated إلزامي في كل Master.
3. F1/double-click = Select مرجعي — اختصار لوحة مفاتيح مستمر عبر المنتج.
4. جداول قابلة للنقر المزدوج للتبديل — تعميم Switch في RTL.
5. تنبيهات الخطر (Supervisor/Attributes/INI/Delete) تحتاج تأكيدات — الأصل بلا شبكة.
6. Round-off يشرح بصيغ تفاعلية (شاشة المعاينة بالنسبة للفاتورة).
7. صلاحيات: نسخ القوالب = أهم تحسين إنتاجية للمشرف.
8. بووتستراب الإعداد (Bootstrap sequence WF-SYS 1-8) = **Wizard إعداد أولي** يغطي Property→Currency→Tax→Users — الأصل: 8 قوائم متفرقة.
