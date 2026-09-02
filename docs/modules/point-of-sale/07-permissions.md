# 07 — الصلاحيات والأدوار (Permissions) — وحدة POS

> POS تملك **أغنى نموذج صلاحيات في النظام** (ثلاثي الأبعاد) — وتكتمل الصورة مع AR User Access وFAS Transaction Type Rights في نموذج موحد (UNK-013).

---

## 1. POS User Access — النموذج ثلاثي الأبعاد (POS-SET §20 ص56-58)

| البعد | القيم | ملاحظة |
|---|---|---|
| **User** | كاشيرو POS فقط ("This field displays only PO Cashiers") | نطاق أدوار محدد |
| **Operation** | **KOT · Billing · Settlement** (كل واحدة بوظائفها الدقيقة — عمود Description) | مستوى الشاشة/الوظيفة |
| **Applicable To** | **Regular · Touch Screen · PDA** | **نوع التطبيق!** — صلاحيات منفصلة لكل شكل تشغيل |

**القيم:** Yes/No بـ Double-click. `[NOT DOCUMENTED]` الافتراضي (الراجح No بالقياس على AR).

### الوظائف المذكورة في العمليات (من TS — مواضع الصلاحيات المحتملة)

| المجموعة | الوظائف الحساسة الموثقة | المصدر |
|---|---|---|
| KOT | Modify/Void (بأسباب) · NC KOT · Open Items | TS ص16-22/37 |
| Billing | Check Print · Reprint (يُرقِّم من جديد!) · Split · Discount · **Tax Exemption** · View KOT | TS ص23-31 |
| Settlement | **Settle (Balance=0)** · Void Settlement · **Resettlement** | TS ص32-36 |

## 2. Restrict Outlet Access (§21 ص60-61)

- **النموذج:** مستخدم × منافذ (استثناء) — الافتراضي: الوصول للكل.
- **المثال الموثق:** IDSS-Supervisor مقيَّد عن: Health Club, LE Grand Hall, Minibar, Pastry Shop, Souq Cafe.
- **دلالة معمارية:** تقييد **بالسلب** (blocklist) هنا مقابل AR User Access (allowlist) — يجب توحيدهما في النظام الجديد (قرار معماري).

## 3. حواجز التشغيل المعرفية (من TS)

| الحاجز | القاعدة | المصدر |
|---|---|---|
| Close Shift | **Password الكاشير** + لا معلقات | TS ص46 |
| Login | Userid/Password بلوحة على الشاشة + اختيار DB | TS ص1-3 |
| رؤية المنافذ | Session Statistics للمخوَّلين فقط | POS-LUK §6 |

## 4. الأدوار المستنبطة (Function Inference)

> `[INFERENCE]` من الوظائف الموثقة — تُطابق مع `docs/domain/hotel-roles.md`.

| الدور | الوظائف | المصدر |
|---|---|---|
| **POS Cashier** | Open/Close Shift · Order Entry · Check · Settlement (بالأنماط المخوَّلة) | TS |
| **Captain/Steward** | إدخال الطلبات للطاولات (Steward Selection) + نقل الطلبات | TS ص8/42 |
| **Outlet/POS Manager** | إعداد المنافذ والقوائم والأسعار + Open/Close Outlet (شخص واحد) | POS-SET + TS |
| **F&B Controller** | Menu Master/Rate/Batch · Happy Hours/Promotions · NC Cost · Session Statistics | POS-SET |
| **Guest Relations** | Guest History + Comments + Analysis + Labels/Letters | POS-GST |
| **Revenue Manager** | Rate Master · Happy Hours · Member Discounts | POS-SET §25/§31/§41 |
| **System Admin** | User Access · Restrict Access · Print Forms · Parameter List | POS-SET |

## 5. أسئلة صلاحيات مفتوحة

| السؤال | الأثر | الحالة |
|---|---|---|
| هل Void/Comp تحتاج صلاحية مستقلة عن Settlement؟ | نموذج السماح | `[NOT DOCUMENTED]` (مذكورة كوظائف مستقلة) |
| من يملك Resettlement؟ (خطر مالي) | قرينة: ضمن Settlement rights | `[NOT DOCUMENTED]` |
| هل صلاحيات PDA تختلف فعلياً عن Touch؟ | تصميم أدوار متعددة المنصات | `[NOT DOCUMENTED]` — الوثيقة تثبت البعد فقط |
| افتراضي POS User Access (Allow-all أم Deny-all؟) | نموذج الأمان | `[NOT DOCUMENTED]` |
