# 12 — التكاملات (Integrations) — وحدة FXD

> **I-FX-01..09** — وحدة "أقمار مالية": كل علاقاتها الجوهرية مع FAS (COA الرباعي + FY + Transaction Types)؛ جسر صاعد وحيد (**F12: FI Depr Posting → FAS**)؛ علاقات مرجعية حرة مع MGT (PO/GRR/Bill)؛ وتقاطع كياني صامت مع MNT (Equipment مقابل Asset) بلا جسر نصي واحد.

---

## 1. خريطة التكاملات

| ID | من | إلى | النوع | النص/الأساس | المصدر |
|---|---|---|---|---|---|
| **I-FX-01** | FXD (Sub Group) | FAS COA | مرجعي رباعي | BS Depr A/c + BS Depr S/L + PL Depr A/C + PL Depr S/L (+sub ledger) | ص5 |
| **I-FX-02** | FXD (Sub Group) | FAS Cost Centers | مرجعي | حقل Cost center/department | ص5 |
| **I-FX-03** | FXD | FAS Financial Year | **استهلاك F3** | Method + FI Posting + كل الاستعلامات/التقارير | ص10/16/18 |
| **I-FX-04** | FXD (FI Posting) | FAS GL | **⭐ ترحيل شهري (F12)** | "post the depreciated data into financial module... monthly... month's end date... SLM only... sub group wise" | ص16-17 |
| **I-FX-05** | FXD (Transaction) | FAS GL | ترحيل بيع | "FA posting screen will populate... Sales amount will be posted to cash or bank account" | ص13 |
| **I-FX-06** | FXD (Master) | SYS Currency | مرجعي آلي | "By default, the local currency will be loaded... rate as per currency factor" | ص7-8 |
| **I-FX-07** | FXD (Master) | [Vendor Master?] | مرجعي بلا موطن | Supplier code بF1 — مصدر غير محسوم (عائلة UNK-058 السادسة!) | ص9 |
| **I-FX-08** | MGT (PO/GRR/Bill) | FXD (Master) | **حقول حرة بلا ربط** | "PO #, PO date, Grr #, Grr date, Bill #, Bill date — User define fields... mandatory, with INI switch validation" | ص9 |
| **I-FX-09** | FXD ↔ MNT | **تقاطع كياني صامت** | Equipment Master (MNT) مقابل Fixed Asset Master — لا إحالة نصية بأي اتجاه | [INFERENCE] |

## 2. تحليل الجسر الصاعد (I-FX-04 = F12)

```
[Depreciation محسوبة حتى MMYY]
        ↓ FI Depr Posting (Load)
   Sub Groups: مربوط ✓ / غير مربوط (أزرق — يُستثنى)
        ↓ Save
[FAS: قيود شهرية نهاية الشهر — PL Debit / BS Credit — SLM فقط]
```

- **موقعها في عائلة الجسور المالية**: F4 (FO→FAS) · F5 (POS) · F6 (MGT) · F7 (HRP) · F8 (MEM) · F9 (AR) · **F12 (FXD)** · F13 (TEL) — **ثامن جسر** وثاني أصغر حجم ترحيل (بعد MEM؟) لكنه الأكثر انتظاماً (شهري آلي محدد البنية).
- **انفصال Calc/Post** يجعل الجسر اختيارياً زمنياً (يمكن حساب شهور بدون ترحيل ثم ترحيلها دفعة؟ [UNCERTAIN] — سلوك الترحيل التراكمي غير موثق).

## 3. التقاطع الصامت مع MNT (I-FX-09) — أهم اكتشاف تكاملي

| السؤال | MNT (Equipment Master) | FXD (Fixed Asset Master) |
|---|---|---|
| الكيان | معدات بأكواد و"Asset Group" في Equipment Master! | أصول بـSub Groups |
| الصيانة | أوامر عمل كاملة + PM Schedules | حقل نصي "Asset maintenance" حر! |
| القيمة | ❌ لا قيمة | قيمة + إهلاك |
| الإهلاك | ❌ | ✅ |
| الجسر المتبادل | لا ذكر للأصول الثابتة | لا ذكر للمعدات |

> **الاستنتاج المعماري [INFERENCE]:** كيانان متوازيان لنفس الأشياء المادية بلا مزامنة — Equipment ليست Asset والأصل ليس Equipment؛ عند إعادة البناء يُبنى **Asset واحد** (ERPNext) وترتبط به Equipment/Schedules (Asset Maintenance) — راجع 16 F-FX-9.

## 4. عائلة الموردين (I-FX-07) — التوسع السادس لUNK-058

- الملاحظات السابقة: MNT استهلك موردين بلا موطن → المرجح ماستر MGT.
- هنا: Supplier code بF1 في Master — **بلا F1 في بقية الشاشات** ولا Vendor Name (بعكس GTP التي تسأل Code+Name!).
- القرار المتراكم: **Vendor Master في ERPNext** واحد يخدم MGT/MNT/FXD/GTP (راجع 17 GAP-FX-D05).

## 5. ما ليس تكاملاً (عزل بنيوي)

| العنصر | الشاهد |
|---|---|
| لا جسر HRP | لا موظف صيانة/مالك موثق |
| لا جسر FO/POS/BNQ | مسارات إيراد لا تلمس الأصول |
| لا جسر FNB | مطابخ/أصول مطبخ غير متقاطعة |
| لا جسر SYS-INI عدا #475 | بوابة التهيئة ضيقة |
| Gate Pass للأصول؟ | ❌ GTP عام للمواد الخارجة — لا إحالة للأصول (راجع gate-passes/12) |
