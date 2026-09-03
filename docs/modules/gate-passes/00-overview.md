# 00 — نظرة عامة (Overview) — وحدة GTP (Gate Passes)

> **تصاريح البوابة**: **أداة ضبط حركة المواد خارج/داخل الفندق** — وحدة فرعية تحت Financial Management بوظائف 7 فقط: إصدار تصريح (NOTE موثِّق "authenticating the details of goods taken out of the premises") · استلام بجزئية · استعلام · سجل · معلق · طباعة · تقرير. **أضأف دليل في المشروع كله (13 ص)** وأصفى "جزيرة ضبطية": صفر GL · صفر إهلاك · صفر موظفين · صفر صلاحيات · صفر User/Last Updated — الوثيقة موجودة لسبب واحد: **مسؤول البوابة يحتاج ورقة**.

---

## 1. حدود الوحدة

| البند | الوصف الموثق |
|---|---|
| الاسم النظامي | Gate Pass — قوائم فرعية تحت **Financial Management**: "Gate Pass is used by Financial Management to issue or receive gate pass..." (ص1) |
| الوظيفة الجوهرية | **سبع وظائف**: (1) **Issue Gate Pass** — إصدار تصريح خروج مواد "for reasons like **serving, material transfers etc**"؛ (2) **Receive Gate Pass** — وسم الأصناف العائدة "Provision to tag **partial items** received"; (3) Gate Pass Query؛ (4) Gate Pass Register؛ (5) Pending Gate Passes؛ (6) Gate Pass Print؛ (7) Gate Pass Report |
| المركز المعماري | **أداة ضبط أمني/لوجستي محض**: "A gate pass is a **NOTE** issued **authenticating** the details of goods taken out" — الوحدة لا تحاسب ولا تخزّن مخزنياً ولا تُرحّل: تُصدر ورقة يصدّقها حرس البوابة. وضعها تحت FAS (مثل FXD!) قرار تصنيفي غريب بلا تفسير نصي |
| نمط التشغيل | معاملات نادرة آنية (إصدار عند كل خروج) + **دورة عودة** (استلام كلي/جزئي بتواريخ) + استعلامات لحظية + سجلات مطبوعة يومية |
| النطاق | كل مراكز التكلفة (Issue) · موردون (Code+Name!) · أصناف نصية حرة (Particulars) · وحدات قياس · **ثنائية Returnable/Non-Returnable** · تاريخ عودة متوقع · ملاحظات |
| خارج النطاق | أي قيد GL أو إيراد · أي حركة مخزن (لا ربط MGT نصي رغم أن "material transfers" سبب معلن!) · أصول ثابتة (لا إحالة FXD) · صلاحيات/موظفون نظاميون · أسعار/قيم مالية (لا حقل Amount واحد!) |

> ⚠️ **أربع ملاحظات معمارية:** (1) **Vendor Code يُختار وVendor Name يُدخل يدوياً** — "In the Vendor Code field **select** the vendor code. In the Vendor Name **enter** the vendor's name" — أول انفصال Code/Name في المشروع (FXD اختار الكود فقط!) — امتداد سابع لمجهول المواطن (UNK-058/074). (2) **الاستلام الجزئي موثق حرفياً** — "Provision to tag **partial items received** are also provided" + تعديل بالـdouble-click — أضأل وحدة بأرقى دورة استلام. (3) **ثنائية Returnable/Non-Returnable تنظم كل شيء**: الاستعلام والسجل (المرتجع فقط!) والطباعة والتقرير كلها تفترق على هذا المحور. (4) **السجل (Register) للمرتجع فقط** — "all **returnable** Gate Passes issued by various departments" — غير المرتجع لا يظهر بالسجل أصلاً (له القنوات الأخرى).

## 2. جرد الوظائف الموثقة (7 من TOC ص1)

| # | الوظيفة | النوع | المصدر |
|---|---|---|---|
| 1 | **Issue Gate Pass** | معاملة (إصدار + شبكة أصناف) | §1 ص2-3 |
| 2 | **Receive Gate Pass** | معاملة (استلام جزئي/كلي + تعديل) | §2 ص3-5 |
| 3 | Gate Pass Query | استعلام | §3 ص6-7 |
| 4 | Gate Pass Register | تقرير (مرتجع فقط) | §4 ص7-8 |
| 5 | Pending Gate Passes | تقرير (as-on) | §5 ص8-9 |
| 6 | Gate Pass Print | طباعة انتقائية | §6 ص10-11 |
| 7 | Gate Pass Report | تقرير تفصيلي | §7 ص11-12 |

## 3. المفاهيم الجوهرية الموثقة

| المفهوم | الدلالة | المصدر |
|---|---|---|
| **التصريح كوثيقة** | "A gate pass is a **NOTE** issued **authenticating** the details of goods taken out of the premises for reasons like **servicing, material transfers etc**" — التصريح إثبات وليس حركة مخزنية | ص2 |
| **Returnable / Non-Returnable** | المحور الثنائي: صنف يُسجل بالشبكة "select if the goods are **returnable or not**" — يقرر السجل والاستعلام والطباعة والتقرير والمعلق | ص3 |
| **Expected date of return** | حقل الشبكة — أساس مفهوم **Pending** ("print pending Gate Passes register **as on a date**") | ص3/ص8 |
| **الاستلام الجزئي** | "tag items that are received... Provision to tag **partial items** received are also provided" + "If you want to modify the details... double-click on the record that you want to modify" — وسم بالتاريخ والكمية وتعديل لاحق | ص3/ص5 |
| **استرجاع ثلاثي** | "retrieve gate passes based on: **Gate Pass #, Vendor Name or Gate Pass Ref#**" — ثلاثة مفاتيح وصول للاستلام | ص4 |
| **Authorized By** | "the name of the person who has **authorized** the issue" — إدخال حر (لا صلة ماستر موثقة — عائلة UNK-038/076) | ص2 |
| **Responsibility** | "the name of the person who has **issued** the gate pass" — حامل المسؤولية التشغيلية (يختلف عن Authorizer!) | ص3 |
| **Gate Pass Ref#** | مرجع المستخدم للبضاعة — "a reference number for the goods to which a gate pass has to be issued" — مفتاح بحث ثالث مستقل عن رقم النظام | ص2 |
| **Cost Center** | "From the Cost Center dropdown list select the cost center to which the selected goods belong" — القناة التنظيمية الوحيدة الموثقة | ص2 |

## 4. الإحصاءات المقروءة

| المؤشر | القيمة |
|---|---|
| صفحات مقروءة عميقاً | **13 (أضأل دليل في 65 ملفاً!)** |
| وظائف موثقة | 7 (2 معاملات + 1 استعلام + 3 تقارير/سجلات + 1 طباعة) |
| شاشات | ~9 (راجع 03) |
| قواعد عمل موثقة | BR-GP-01..12 (راجع 05) |
| قيود إدخال موثقة | V-GP-01..07 (راجع 06) |
| قيود GL | **صفر مطلق** — لا حقل Amount واحد في الوحدة! |
| مفاتيح INI | **صفر** (ثامن عضو في عائلة "بلا INI": CARE/MEM/SLM/TEL/MNT→انكسرت→FNB/FXD — تعود هنا) |
| مجهولات جديدة | UNK-074..077 (راجع 17) |
| حقول المالية | Cost Center فقط — لا عملة ولا مبلغ ولا حساب |

## 5. موقعها في خريطة المشروع

- **قبلها:** FO (1) → FAS (2) → ACR (3) → POS (4) → SYS (5) → MGT (6) → BNQ (7) → HRP (8) → Care (9) → MEM (10) → SLM (11) → TEL (12) → MNT (13) → FNB (14) → FXD (15) → **GTP (16 — هذه الوحدة — الأغلق للـ17/17 مع TSC الموثقة داخل POS)**.
- **علاقاتها الواردة:** Cost Centers (عائلة FAS/SLM) · Vendor Master [مصدر غير محسوم — امتداد UNK-058 السابع] · UOM [ماستر غير محسوم] · **MGT (موضوعياً لا نصياً!)** — "material transfers" سبب معلن بلا جسر واحد.
- **علاقاتها الصادرة:** **ورق مطبوع** (تصاريح/سجلات/معلق/تقارير) · لا جسر رقمي واحد لأي وحدة.
