# 02 — الإعدادات (Configuration) — وحدة Front Office

> مفاتيح الإعداد الموثقة المؤثرة في سلوك FO. الجداول الكاملة في `field-extracts/Front_Office/FN6i-NT-FOM-SET.json`.

---

## 1. مفاتيح السلوك الموثقة نصاً

| المفتاح | الأثر الموثق | المصدر |
|---|---|---|
| **INI Switch 64** | سلوك Clear Room# بعد التسوية (Settlements) | FOM-CAS ص78 |
| **INI Switch (Foreex Voucher)** | Voucher# تلقائي أو يدوي في Foreign Exchange Entry | FOM-CAS ص87 |
| **FO Module Attribute 16** | "Posting to be stopped once the bill is printed" — يفعّل Release Stop Posting | FOM-CAS ص82-83 |
| **Post Guest History (Y/N)** | ترحيل صور/بيانات الضيف إلى Guest History | FOM-REG ص66-67 |
| **Check Out Time Format** | 12 Noon أو 24 Hour (لكل تسجيل) | FOM-REG ص22 |

## 2. هيكل إعداد FOM-SET المكتمل (الجلسة 3 — Quality Gate)

> FOM-SET = **67 قسماً** (145 صفحة). التصنيف الكامل في `01-master-data.md` §3. أهم بنى الإعداد المكتشفة:

| البنية | الدلالة | المصدر |
|---|---|---|
| **Applicable From دفترياً في كل ماستر** | لا تفعيل إلا بتاريخ ≥ اليوم؛ التعديل الجذري = نسخة بتاريخ مستقبلي (نسخية زمنية) | FOM-SET §1-§46 Notes |
| **INI Setting No. 58** | "Set the INI Setting No. 58 = 0 in the property INI file to activate this option" — تفعيل خيار §16 (Reservation Mode) | FOM-SET صـ1544 نصاً |
| **Resv. Mandatory Fields §34** | تحويل حقول الحجز لإلزامية (*) ديناميكياً | FOM-SET ص83-84 |
| **FO User Authorization §35** | مصفوفة تفويض المستخدمين للعمليات المميزة | FOM-SET ص84-85 |
| **User Defined Print Forms (SYS)** | قوالب القسائم (Vouchers) للكونسيرج تُعرّف مسبقاً هنا — وإلا خطأ "Category does not exist" | FOM-CRG ص6/ص19 |

**اعتماديات إعداد موثقة أثناء التشغيل:**
- Rate Table تعتمد على: Room Type × Meal Plan × Currency (RES ص6-7).
- Group Billing يعتمد على تعريف Outlets (REG §21).
- Activate/Deactivate Extension يعتمد على بنية تمديدات TEL (REG §26).
- **Voucher Printing للـ Revenue Codes**: Prgm. ID + Print Port لكل من Debit/Credit (FOM-SET §24).
- **قوالب القسائم (Concierge/Laundry/Lost&Found) من SYS-SSP** — تكامل إعدادي موثق (FOM-CRG).

## 3. أثر الإعدادات على السلوك (مصفوفة أولية)

| الإعداد | ON | OFF |
|---|---|---|
| Attribute 16 | طباعة الفاتورة تجمد الفوليو → Release Stop Posting متاح | الفوليو يستقبل ترحيلاً بعد الطباعة |
| INI 64 | Clear Room# نافذة تظهر بعد Save تسوية | سلوك مختلف (غير موثق تفصيلاً) |
| Post History | صور/بيانات الضيف تُرحَّل للتاريخ | لا ترحيل |
