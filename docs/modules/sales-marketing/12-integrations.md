# 12 — التكاملات (Integrations) — وحدة SLM

> SLM = **أكثر وحدة عقداً خارجياً متنوعاً بعد FO**: تُنشئ كيانات تستهلكها 7 وحدات نصاً، وتستضيف 5 ماسترات FO، وتبث قيوداً سلوكية (أسعار/خصومات/تخصيصات/أقفال) إلى 4 وحدات تنفيذية — وتملك التكامل الخارجي الوحيد من نوعه (Outlook).

---

## 1. جسور الكيانات (المستودعات)

### 1.1 SLM → AR: جسر Company Profile (الأعمق في المشروع)

```
SLM: Company Profile (PRF §7)
  ├── الحزمة المالية (Bypass Invoice/Allow Credit/Credit Days/
  │   Invoice Currency/Interest %/Credit Limit/Commission %/
  │   Collection Executive/Billing Address)
  ├── Transfer Prospects (SLT §10) → إنشاء Company Master آلياً (كود TTT+حرف+مسلسل)
  └── Update Company Profile (PRF §8) → تحديث جماعي للرباط
        │
        ▼
AR (وحدة ACR): أرصدة/فوترة/تحصيل لذات الكيان
FO: حجوزات وتسويات بذات الكيان (القفل الائتماني!)
POS: فواتير outlets بذات الكيان
BNQ: عقود البنوك بذات الكيان
MEM: شركات العضويات بذات الكيان
```

> **نص التعدد الموثق:** "Information recorded here is used in **Front Desk, Sales & Marketing, Point of Sale, Accounts Receivables, Banquets, Conferencing and Membership** modules. The Guest/Company profiles are primarily used during **settlement of bills on credit and linking of assured room rates and discounts** to take effect in billing." — PRF ص9-10 (سبع وحدات! — "Conferencing" سادسة غير مذكورة في TOC BNQ — راجع UNK-052)

### 1.2 SLM (داخلي): Prospect ≠ Company Master

مستودعان منفصلان بجسر تحويل مشروط (الاستيفاء) — بلا عودة موثقة (no reverse transfer).

## 2. جسور التهيئة (ماسترات FO المستضافة)

| الماستر | مالكه الأصلي (FO Setup) | واجهة SLM | النمط |
|---|---|---|---|
| Sales Office | FO | PRF §1 — "refer Sales Office under Front Office Setup" | مستضاف |
| Sales Executives | FO | PRF §2 | مستضاف |
| Collection Executives | FO | PRF §3 | مستضاف |
| Bookers Type | FO | PRF §4 (Bookers Master) | مستضاف |
| Company Types | FO | PRF §7 (بنية الكود!) | **حاكم بنيوياً** |
| Rate Master (non-rack/Package) | FO | PRF §9 + LUK | مستهلك |
| Billing Instructions / Market Segments | FO | PRF §7 (F1) | مستهلك |

> **قرار F-SM-2:** في إعادة البناء: مصدر واحد لكل ماستر (Frappe doctype) بواجهات متعددة — يمنع انقسام البيانات الذي سمح به الأصل.

## 3. جسور التنفيذ (SLM تقرر — وحدات أخرى تنفذ)

| القرار في SLM | المنفذ | الآلية الموثقة |
|---|---|---|
| CGR Rates (Link Rates) | **FO** | "linking of assured room rates... to take effect in billing" |
| Revenue Discount Master | **POS + FO** | "applicable during the generation of Bills in **F&B outlets** and various transaction entries" + "tagged during **reservations/Registrations**" |
| Retention Policy | **FO** | "charged to the company by using **Retention-Cancel/No show option under front office**" |
| Cancellation Policy | **FO** | "compare the number of days... cancellation date prior to arrival date and levy the charges" |
| Agent Allocation/Forecast/Release | **FO** | "the **reservation program prompts** you to assign the rooms requested as **Inside or Outside allocation**" + cutoff بـINI #41 |
| Hotel Amenities | **FO** | "highlighted when a **reservation is being made** for that particular company" |
| Credit Limit القفل | **FO/POS/BNQ + يدوي** | "settlement... is not allowed" (PRF ص13) |
| Hotel Profile | **FO (Room Booking!)** | "This information can be **browsed from Room Booking screen**" (LUK §4) |

## 4. جسور العرض (SLM تستهلك بيانات الآخرين)

| العرض | المصدر | التوثيق |
|---|---|---|
| Sales Manager Tool: Reservations (incl. Cancelled/No Show/Past) | **FO** | SLT ص12 |
| Sales Manager Tool: In-house Guests | **FO** | SLT ص12 |
| Sales Manager Tool: Revenue (Tariff/Food/Beverages شهرية) | **FO/POS** | SLT ص13 |
| Sales Manager Tool: Receivables (opening/charges/payment/closing) | **AR** | SLT ص13 (cutoff=Accounting date) |
| Sales Manager Tool: Hotel Position (توفّر/Over Booking) | **FO** | SLT ص14-16 |
| Executive Planner: In-house Guest | **FO** | SLT §9 |
| Company Productivity/Contribution/Sales/Variance | **FO/POS/AR** | REP §14-18 |

## 5. التكامل الخارجي (Outlook)

| البند | الموثق |
|---|---|
| القناة | "send the letters through **Microsoft outlook** as E-Mail with attachments" — REP §12 |
| منطق التوجيه | CEO → بريد الشركة؛ غيره → قائمة جهات الاتصال في Company Master |
| المحتوى | "You can use **Word processing software** to create the textual content" |
| مرفقات | زر Attach + Subject |

> **إعادة البناء (F-SM-5):** استبدال Outlook بقناة Frappe Email (SMTP) + Email Template + Newsletter — يحقق ذات الوظيفة دون اعتماد سطح مكتب مستخدم.

## 6. جسور الهوية (SYS/HRP)

| الجسر | الوثيقة | ملاحظة |
|---|---|---|
| Map Users/Sales Exec ↔ **SYS User Setup** | PRF §16 | شرط تشغيل Executive Planner |
| INI #239 / #41 | SLT §9 / PRF §14 | مفاتيح SYS |
| Sales Executives/Collection Executives ← **FO Setup** (لا HRP!) | PRF §2/§3 | ⚠️ ثالث مخزن موظفين (بعد HRP-employee وCare-PMS-employee) — UNK-038 تتسع |

## 7. مصفوفة الجسور الإجمالية (الوحدة 11/17)

| الاتجاه | الجسور | الأثر |
|---|---|---|
| SLM → | AR (كيان) · FO (أسعار/سياسات/تخصيصات/خصومات/توقف) · POS (خصومات/قفل) · BNQ (كيان/قفل) · MEM (كيان) · SYS (ربط هوية) · **Outlook (بريد خارجي)** | عالٍ جداً |
| SLM ← | FO (7 ماسترات مستضافة + بيانات عرض 6) · SYS (مستخدمون/INI) | عالٍ |
| SLM ↔ HRP | **✗ لا شيء موثق** | غياب صريح (نمط Care) |

## 8. جرد الروابط الجوهرية الست (تحديث الموقف)

| الرابط الجوهري (المشروع) | الحالة بعد SLM |
|---|---|
| 1. FO↔AR (فوليو→مديونية) | ✓ موثق سابقاً |
| 2. POS→AR (outlets) | ✓ موثق سابقاً |
| 3. MM→FAS (مشتريات→قيود) | ✓ (التوقيت UNK-027 قائم) |
| 4. BNQ→AR (عقود) | ✓ موثق سابقاً |
| 5. Payroll→Finance | ✓ موثق (HRP) |
| 6. **SLM→AR/FO (كيان موحد + قرارات تسعير)** | ✓ **اكتمل توثيقه الآن** — وحدة SLM كانت آخر حلقة كيان العميل (الرابط السادس بمعنى الكيان المشترك) |
