# 09 — شاشات البحث والقوائم (Lookups) — وحدة Front Office

> أنماط البحث/المساعدة (F1 Help) الموثقة في وثائق FO. وثيقة FOM-LUK الكاملة `[PENDING DEEP READ]`.

---

## أنماط البحث الموثقة

| النمط | الاستخدام | المصدر |
|---|---|---|
| **Scan Booking** | بحث الحجوزات بمعايير: guest name / Company / Group / arrival date / reserved date / reservation # | RES §1.3/§1.4 |
| **Length of Stay search** | بحث الوصولات بطول الإقامة | REG §2 (ص14) |
| **Guest selection في Posting** | فرز: Room# / Group / Company / Nationality / Room Type / Guest Name / Resv# / Gst.Status / Gst.Clf. / Reg# + Scan | CAS §1 (ص4-8) |
| **Reservation # selection** | Guest Name / Company Code / Group / Arr. Date / Ref# | CAS §Deposits (ص14) |
| **F1 Help الشامل** | Company / Booker / Plan Code / Pay Mode / Bill Inst / Business Source / Market Segment / Credit Card Type / Staff Code / Nationality / Department / Room / Currency / Discount Id / Room Features | مواضع متعددة في RES/REG/CAS |
| **Codewise / Namewise** | عرض نتائج Help بمرتبة الكود أو الاسم | RES ص5 |
| **Room Rack / Floor Plan** | عرض الغرف معلوماتياً (Block + Floor) | RES §3 + REG §5 |
| **Information Tips** | tooltip عند مؤشر الغرفة: arrival/departure, reg#, guest, rate, pax, company + بنود البلوك | RES §3 (ص61) |

## سلوكيات مساعدة موثقة

- Double-click في الحقول كبديل F1 (نمط موحد).
- علامة * في Detailed Position تدل على قابلية التوسع (Double-click) — REG ص11.
- F5 لمسح رابط، F6 لمسح صف (Document Center) — REG ص20-21.
- F9 = Guest Note save&exit، F10 = Documents — RES ص22-23.
