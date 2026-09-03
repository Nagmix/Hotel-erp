# 12 — التكاملات (Integrations) — وحدة FNB

> **I-FB-01..13** — الوحدة **الأضخم استهلاكاً للبيانات الواردة** في المشروع (POS + MGT كاملين + SYS)، مع **جسر صاعد وحيد** إلى MGT (Auto Indent)، وحاجب لحظي مثير يعمل في الاتجاه المعاكس (SWITCH 511 يغير سلوك POS). **لا جسر HRP، لا جسر FAS، لا FO** — نقاء تكاملي ثنائي الأطراف (POS+MGT).

---

## أ) التدفقات الواردة (Inbound)

### I-FB-01: POS → FNB (المبيعات) ⭐
- **الدليل**: "the **Sales**... details will get extracted from the **Point of Sales**... modules" (SET ص3) + "Costing Extraction will extract the data from **Sales**, Consumption and recipe items" (COP ص3).
- **المحتوى**: مبيعات المنافذ كلها (الكميات/القيم/الجلسات/Covers/KOTs) — أساس Sales Analysis.
- **الوضعان**: Batch (Date Range + Process) أو لحظي (INI#368).

### I-FB-02: MGT → FNB (الاستهلاك/Issues)
- **الدليل**: "the... **Consumption** details will get extracted from... **Materials Management**" (SET ص3) + "Online transfer of **Issues** from inventory to costing" (COP ص3).
- **المحتوى**: قيم/كميات الأصناف المصروفة للمطابخ ومراكز التكلفة — أساس Actual Cost.

### I-FB-03: MGT → FNB (ماستر المطابخ)
- **الدليل**: "Kitchen is selected **all Kitchens defined in the Kitchens option under the Materials Management module**" (SET ص7).
- **الدلالة**: المطبخ كيان MGT أصلاً — FNB تستعيره محوراً لكل تقاريرها ("reflected based on Kitchens" — SET ص4).

### I-FB-04: SYS → FNB (ماستر المنافذ/المطاعم)
- **الدليل**: "a list of all Restaurants defined in the **Setup Outlet under the System**" (SET ص7).
- **الدلالة**: Outlet SYS هو مصدر المطاعم — عائلة Setup Outlet المشتركة (POS/BNQ/TEL...).

### I-FB-05: MGT → FNB (ماستر الأصناف + UOM)
- **الدليل**: "Items defined in the **Inventory Master option of Material Management module**" (SET ص11) + "This data is defined in the **Master Entry in Material Management**" (UOM مقفل — COP ص12) + مخازن الجرد (COP ص5) + مراكز التكلفة "pre-defined Cost Centers" (SET ص7).
- **الدلالة**: كل بيانات صنفية/مخزنية مستعارة — لا ماستر أصناف في FNB إطلاقاً.

### I-FB-06: POS → FNB (قوائم/أصناف/جلسات/KOT/Menu Types)
- **الدليل**: "recipe for all food and beverage **menu items existing in the Point of Sale outlets**" (SET ص10) + "POS Item can tag for only one Recipe" (SET ص12) + Manual Sales (Session/KOT/Menu Type — COP ص10) + Open/Modifiers "at POS" (COP ص15).
- **الدلالة**: الحضور الصنفي والجلسي الكامل لعالم POS.

### I-FB-07: POS → FNB (المبيعات غير المحوسبة المعكوسة)
- **الدليل**: Manual Sales Entry "used for Sales from **non-computerized outlets**" (COP ص9).
- **الدلالة**: FNB تعوّض غياب POS نفسه (فروع ورقية) — إدخال قيم مبيعات يدوية بجلسات/KOT/قوائم POS نفسها!

### I-FB-08: SYS → FNB (INI/Switches)
- **الدليل**: INI#368 ONLINEFBCOSTING + SWITCH 511 (COP ص3-4) + Audit Date/property.
- **الدلالة**: عائلة INI التراكمية (368/511 بعد 355/220/239/41...) — أول مفاتيح لFNB.

## ب) التدفقات الصادرة (Outbound)

### I-FB-09: FNB → MGT (Auto Indent) ⭐⭐ الجسر الصاعد الوحيد
- **الدليل**: "Auto indent is one of the option to create indent and **created indent can be used in inventory**" (COP ص19) + "link **POS menu items with their ingredients**" (COP ص17).
- **الدلالة**: انفجار BOM باتجاه الطلب — مطالب مكونات تولَّد من الوصفات/المبيعات المتوقعة وتستقبلها دورة MGT (Indent→PR→Receipt المعروفة).
- **⚠️ الخلود**: "Once the indent is generated, it will not be allowed to modify or delete" — عقد غير قابل للفك مع MGT.

### I-FB-10: FNB → POS (الحاجب اللحظي!) ⭐⭐ فريد المشروع
- **الدليل**: "SWITCH 511... if this switch is set to 0, in real time during **Current stock balance will be checked KOT punch. Items cannot be sold, if the quantity is greater than the current stock**" (COP ص3).
- **الدلالة**: سلوك بيع POS (قَبول/رفض KOT) يُضبط من مفاتيح موثقة في دليل FNB، بقراءة رصيد "Current stock" تحليلي (حوض FNB أم مخزون MGT؟ — غير محدد! UNK-063).
- **النمط**: أول تكامل **سلوكي عكسي** (وحدة تحليلية تتحكم في بوابة وحدة تشغيلية).

### I-FB-11: FNB → الطابعة (Buffet)
- **الدليل**: "Select the **printer** to print the report from the list of printer provided" (REP ص27) — مخرج ورقي تشغيلي مباشر للمطبخ.

### I-FB-12: FNB → Link Help (استعلام يربط)
- **الدليل**: "Click Link Help to **link the Restaurant/Cost Center and Kitchen**" (LUK ص15) — صيانة ربط Costing Link من داخل Profitability Analysis.

## ج) الغائبون (توضيح سلبي مهم)

| الوحدة | الجسر | القراءة |
|---|---|---|
| **FAS** | ❌ لا شيء | متعمد: MIS صرف (راجع 11) — عائلة "الفجوة العامة" تكتمل هنا بلا حتى تفويض |
| **FO** | ❌ لا ذكر | لا غرف/فوليو/نزلاء في الوحدة (على خلاف كل الوحدات التشغيلية!) — نقاء F&B صرف |
| **HRP** | ❌ لا شيء | **لا موظف واحد في 76 صفحة** — أول وحدة تشغيلية بلا مخزن موظفين محلي أصلاً (عائلة UNK-038 لا تتسع هنا — لا وجود أصلاً!) |
| **BNQ** | ❌ لا ذكر | البوفيهات تظهر كطباعة معلومات فقط — لا ربط حجوزات/مناسبات |
| **AR/MEM/SLM/TEL/Care** | ❌ | لا علاقة نصية |

## د) مصفوفة التكامل الختامية

```
        POS ──(مبيعات/KOT/قوائم/جلسات/معدلات + حاجب 511!)──▶  ┌──────┐
                                                             │ FNB  │──(Auto Indent خالد)──▶ MGT
        MGT ──(استهلاك/مطابخ/أصناف/مخازن/مراكز/فواتير?)──▶    │      │──(Buffet Print)──▶ الطابعة
                                                             └──────┘
        SYS ──(منافذ + INI#368/511)──▶                          │
                                                                 └──(تقارير MIS)──▶ الإدارة (ورق/شاشة)
```

- **الدرجة الكلية**: 2 ماستر-مصدر (POS+MGT) + 1 مصدر إعدادي (SYS) + مخرجان (MGT indent + ورق) — **تكامل عمودي ثنائي الأضلاع** أنقى من أي وحدة كبرى.
