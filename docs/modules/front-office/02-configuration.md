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

## 2. مجالات الإعداد المكتشفة (هيكل FOM-SET)

من فهرس FOM-SET: بنية الإعداد تشمل (وفق الفهرس الآلي): Property/Room/Rate/Plan Setup، Transaction Types، Module Attributes، INI Switches... — `[PENDING DEEP READ]` السرد الكامل.

**اعتماديات إعداد موثقة أثناء التشغيل:**
- Rate Table تعتمد على: Room Type × Meal Plan × Currency (RES ص6-7).
- Group Billing يعتمد على تعريف Outlets (REG §21).
- Activate/Deactivate Extension يعتمد على بنية تمديدات TEL (REG §26).

## 3. أثر الإعدادات على السلوك (مصفوفة أولية)

| الإعداد | ON | OFF |
|---|---|---|
| Attribute 16 | طباعة الفاتورة تجمد الفوليو → Release Stop Posting متاح | الفوليو يستقبل ترحيلاً بعد الطباعة |
| INI 64 | Clear Room# نافذة تظهر بعد Save تسوية | سلوك مختلف (غير موثق تفصيلاً) |
| Post History | صور/بيانات الضيف تُرحَّل للتاريخ | لا ترحيل |
