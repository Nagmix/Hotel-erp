# 09 — الولاء وإعادة الطباعة وKDS (§8 + §10 + §24)

> ثلاث خاتمات: Loyalty Report (جسر Guest History) · Re-print POS Bill (آلية إعادة الطباعة الأغنى) · **KDS REPORT (الشبح الختامي)**.

---

## 1. Loyalty Report (§8) — بطاقة الولاء في طبقة التقارير

> "gives the list of **all POS transactions based on the loyalty card selected** for any or all the Outlets."

| البند | القيمة |
|---|---|
| المدخل | Date (≤ Accounting + نفس الشهر) · Outlets (checkboxes) · **CARD#** عبر **Loyalty Card Help** (نقرة مزدوجة) |
| المخرجات | **menu type · Card number · Guest Name · restaurant code · session · bill date · table number · covers** + Tax + **Round Off** + discount + net + settlement amount + **settlement mode** |

**الدلالات:**

1. **عرض معاملة-بمعاملة لبطاقة واحدة** — سجل شراء كامل لحامل البطاقة (بما فيه الطاولة والأغطية) — أبسط شكل لـ"كشف حساب ولاء".
2. البطاقة تخترق كل بنية المعاملة (لا رقم بطاقة فقط) — الولاء **مفتاح استرجاع** كامل مثل Reg# في FO.
3. الجسر: Loyalty Card Master في POS-GST §4 (راجع 08-reports.md للوحدة R-POS من GST) — REP يستهلكه عبر Help.
4. غياب: **لا نقاط/مكافآت/مستويات في التقرير** — الولاء هنا **تعريف/تجميع** بلا محرك استحقاق ظاهر (بازل MEM/SLM) — الفجوة النقاطية موثقة في mapping الوحدة الأم.

## 2. Re-print POS Bill (§10) — إعادة الطباعة الموثقة

> "to print **already settled POS bills** based on the date and bill numbers entered. The user can enter the required fields and either **preview or print** the bills."

### 2.1 البنية (8 خطوات — أطول إجراء في الملف)

| الخطوة | التفصيل |
|---|---|
| 1 | **Specific Date XOR Month & Year** — "If you want to print a bill and you **know the bill date**... If you want to print a bill but you **don't remember the bill date**, select this option and enter the month and year" |
| 2 | Date ≤ Accounting |
| 3 | Outlet |
| 4 | **Bill Type dropdown** |
| 5 | Bill# يدوياً أو **Bill# Help** — **تتكيف Help مع الوضع**: Specific Date → "all the bills generated on the date specified appear" · Month & Year → "all bills generated for the specified month and year appear" |
| 6 | **Print XOR Preview** ("click Preview if you just want to view the bill not print it") |
| 7-8 | Exit من المعاينة → Print "on a **local or network printer configured**" |

### 2.2 الدلالات

1. **وضعان للذاكرة**: أعرف التاريخ / لا أذكره → بحث شهري — تصميم تعاطف مع المستخدم المكتبي (بازل "Month & Year mode").
2. **Help ديناميكي حسب الوضع** — الحقل المساعد يعيد بناء محتواه من سياق اختيار سابق (نمط واجهة ذكي نادر في FN6i).
3. **إعادة طباعة الفواتير المسواة فقط** ("already settled") — لا إعادة طباعة فاتورة مفتوحة (النسخة الأولى تطبع وقت التسوية).
4. **الطباعة موجهة طابعة معرفة** (local/network) — ليس قناة إخراج REP الرباعية بل آلية طباعة وثيقة مستقلة.
5. **التدقيق المقابل**: كل إعادة طباعة هنا تُسجل في **Bill Audit (17.5) بتاريخ ووقت** — آلية + مراقبة موثقتان معاً (انظر `06-audit-reports.md` §5) — أقوى ثنائي إعادة-طباعة/تدقيق في المشروع (يقابل GAP-GP-D02).

## 3. KDS REPORT (§24) — الشبح الختامي

> TOC: "24. KDS REPORT" — المتن: عنوان "24. KDS REPORT" في ص157-158 ثم **تنتهي الوثيقة (158 ص) بلا كلمة واحدة**.

| البند | القيمة |
|---|---|
| الجسم | **صفر** — لا وصف، لا شاشة، لا خطوات |
| الحضور | TOC + عنوان متن فقط |
| التفسير المرجح | **K**itchen **D**isplay **S**ystem — نظام عرض المطبخ الإلكتروني (بديل KOT الورقي) |
| القرينة الداخلية | **KOT Books Usage (17.1)** يوثق الدفتر الورقي — §24 عنوان الانتقال الورقي→الرقمي المبتور |
| التصنيف | **Ghost Section** — عائلة "عنوان بلا جسم" (بازل SMS الشبح في TEL-SET وReport Designer في FOM-REP → UNK-078/UNK-083) |

> **UNK-083 (مسجل):** هل KDS وحدة/تقرير KOT-Display رقمي؟ هل له شاشات إعداد؟ علاقته بـTouch Screen Manual؟ — لا جسم يوثق. القرار التنفيذي: يُبنى KOT Display كشاشة مطبخ (Frappe Realtime) عند الحاجة، ويُسجل §24 كدليل على قصد تطويري غير موثق.

## 4. عائلة "الأشباح" عبر المشروع (تحديث الخريطة)

| الوحدة | الشبح | النوع |
|---|---|---|
| TEL-SET | SMS الشبح (مقدمة بلا جسم) | وصف بلا شاشات |
| FOM-REP | Report Designer + IDS Crystal (TOC بلا متن) | بنود فهرس |
| FNB-SET | "provided later" (بطاقة ائتمان) | وعد مستقبلي |
| FXD | بطاقة "will be provided later" | وعد مستقبلي |
| **POS-REP** | **KDS REPORT (§24)** | **قسم ختامي بعنوان فقط** — أول شبح يُغلق به ملف (الصفر المكتمل عند آخر صفحة) |

> النمط الاستنتاجي: كل "شبح" يشير إلى **حافة تطوير متروكة** (وحدات لم تنضج في التحرير) — KDS تحديداً يوفر أقوى إشارة أن إصداراً لاحقاً كان مخططاً فيه استبدال ورق KOT بشاشات مطبخ.
