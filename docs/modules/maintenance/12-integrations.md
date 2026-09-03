# 12 — التكاملات (Integrations) — وحدة MNT

> **I-MN-01..12** — وحدة **مستهلك نقّي**: تستقبل من MGT (ثلاث قنوات: مخازن/مراكز تكلفة/أصناف) ومن مصدر موردين غير موثق ومن FO ضمنياً (غرف) ومن SYS (سمات ENG) — **ولا تصدر شيئاً** سوى قراءة بارامترات عابرة (Parameter Listing) والورق.

---

## 1. MNT ← MGT (الجسر الأثق) ⭐⭐

| القناة | النص الموثق | الاستهلاك |
|---|---|---|
| **I-MN-01: المخازن** | "Select from the list of **all stores defined in the Inventory module**... A minimum of one store... Store code Definition option under the **Customize sub module of the Material Management module**" (SET ص17) | Equipment Master (Spares) · Action Taken (Repair Details) |
| **I-MN-02: مراكز التكلفة** | "all Cost Centers defined in the Inventory module... cost center code Definition option under the Customize sub module of the Material Management module" + حد أدنى 1 (SET ص18) | Action Taken → Cost Analysis/Repair Details |
| **I-MN-03: الأصناف** | "Item code will be **picked up from Inventory stores**" (OPR ص13) | Repair Details (بسعر يغذي الحساب الآلي للقيمة) |

- **الاتجاه:** وارد فقط؛ لا تُصدر MNT حركة مخزنية (P3) — جسر قراءة أحادي.
- الانتقاء بمستوى الوحدة (Engg Stores) يضيّق نطاق F1 للأصناف — فلتر أعمال مصرفي فعلياً.

## 2. MNT ← مصدر الموردين (Vendor/Service Provider) ⭐

| موضع | الاستخدام | المصدر |
|---|---|---|
| Equipment Master | Vendor Code + F1 → "name and address appear" | OPR ص18 |
| PM Schedule Master | Service Provider (F1) | OPR ص21 |
| Job Order Generation | الإسناد الخارجي "(Vendor)" | OPR ص25 |
| Cost Analysis | Service Provider (F1) | OPR ص11 |

- **UNK-058:** أي ماستر موردين؟ (MGT Purchase؟ FAS؟ SYS؟) — لا إحالة نصية في الملفات الثلاثة — أربعة مواضع استهلاك بانتظار حسم المصدر (الأرجح ماستر موردو MGT — يُفحص عند FNB/متبقي MGT).

## 3. MNT ← FO (ضمني)

- الشكاوى "for **any room** in the property" (OPR ص2) وRoom # بF1 — يقضي بوجود قائمة غرف مشتركة (مصدرها FO Rooms المنطقي) — **لا إحالة نصية مباشرة** (UNK-059 المرافق: مصدر الغرف والدلالات).
- ثنائية Room/Location تكررت في 5+ شاشات — الغرف "مفهوم مستعار" في MNT.

## 4. MNT ← SYS (Module Attributes ENG) ⭐

- **I-MN-06:** ENG#1 (طباعة Job Request) + ENG#2 (طباعة Job Order) — عائلة سمات جديدة كلياً (الخامسة المعروفة بعد FO/POS/... ) — تُعرَّف حصراً في SYS بنمط Module Attributes (استنتاج نمطي — UNK-061 للاكتمال).

## 5. MNT ← HRP: العدم الموثق ⭐

- "define **all the employees in the Engineering Department**" محلياً (SET ص14) + ورديات "only to those employees defined in the Define Employees option **in this module**" (OPR ص15).
- **المخزن الخامس** للموظفين (HRP الكانوني · Care · SLM/FO-Executives · مشغّلو TEL) — **UNK-038 تتسع للمرة الخامسة**: لا مزامنة أجور/غياب/مهارات مع HRP.
- **الأثر التشغيلي:** فني موجود في HRP **لن يظهر** في روزنامة MNT حتى يُعرَّف مرة ثانية يدوياً برقم مختلف.

## 6. MNT → لا شيء (الصادرات الشكلية)

| القناة "الصادرة" | الحقيقة المعمارية |
|---|---|
| Job Request / Job Order (ورق) | مستندات طباعة تحملها اليد — لا تكامل بيانات |
| UDPF | **مصمم مشترك تستهلكه MNT** (قوائمه POS-المحورية: Bill/KOT/NC Bill/Invoice) — أصل نظامي عام وليس صادراً من MNT |
| Parameter Listing | **قراءة عابرة** لبارامترات "various modules" (I-MN-07) — MNT مستضيف التقرير لا مالكه |

## 7. مصفوفة التكامل الشاملة

| # | القناة | الاتجاه | النوع | الموثقية |
|---|---|---|---|---|
| I-MN-01 | MGT → MNT مخازن | وارد | بيانات مرجعية + فلتر | ✅ نص كامل |
| I-MN-02 | MGT → MNT مراكز تكلفة | وارد | بيانات مرجعية | ✅ نص كامل |
| I-MN-03 | MGT → MNT أصناف/أسعار | وارد | بيانات + حساب قيمة | ✅ نص |
| I-MN-04 | ? → MNT موردين | وارد | مرجعي (4 مواضع) | ⚠️ UNK-058 |
| I-MN-05 | FO → MNT غرف | وارد | مرجعي ضمني | ⚠️ استنتاج |
| I-MN-06 | SYS → MNT سمات ENG | وارد | سلوك طباعة | ✅ نص (سمتان) |
| I-MN-07 | MNT ↔ كل الوحدات (Parameter Listing) | قراءة عابرة | تدقيق تكوين | ✅ نص (نطاق؟ UNK-062) |
| I-MN-08 | MNT → GL | **لا شيء** | — | ✅ (نفي بالتحليل) |
| I-MN-09 | MNT → FAS (أصول) | **لا شيء موثق** | — | ❌ فجوة D05 |
| I-MN-10 | MNT → HRP | **لا شيء** | — | ✅ (نفي نصي) |
| I-MN-11 | MNT → MGT (استهلاك) | **لا شيء موثق** | — | ❌ فجوة P3 |
| I-MN-12 | UDPF ↔ MNT | داخلي/مشترك | طباعة | ✅ |

## 8. موقع MNT في خريطة الروابط الكبرى (تحديث عائلات)

- **الحلقات المكتملة سابقاً (POS/BNQ/FO→AR→HRP وCare↔PMS)** — MNT **خارج كل الحلقات**: جذر استهلاكي طرفي (Leaf Consumer).
- **عائلة "الموظفون الخمسة"** تكتمل توثيقياً هنا — راجع 01 §2 — أول تقرير تكاملي يشير لهذا التشرذم كمشكلة معمارية مركزية (يُرفع للمرحلة 10).
- **عائلة شركات الهروب الرقمية تكبر:** 9999999999 (TEL — شراكات تعرفة) ثم **999999999999 (MNT — صنف مفتوح)** — نفس الفلسفة بأطوال مختلفة.
