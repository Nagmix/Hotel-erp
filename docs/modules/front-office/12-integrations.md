# 12 — التكاملات (Integrations) — وحدة Front Office

> التفاعلات الموثقة نصاً بين FO والوحدات الأخرى (لمصفوفة Phase 10).

---

| # | التفاعل | الطرف | الاتجاه | الآلية الموثقة | المصدر |
|---|---|---|---|---|---|
| I1 | فواصل المطاعم تُرحَّل لفوليو الضيف | POS | POS → FO | "Restaurant bill will be posted for POS module" + Double-click يعرض بنود Outlet | FOM-CAS ص4 |
| I2 | كل التسويات الائتمانية → AR | Accounts Receivables | FO → AR | تلقائي: "transferred to the Accounts Receivables module automatically" | FOM-CAS ص69 |
| I3 | ترحيل إيرادات FO إلى GL | Financial Management | FO → FAS | رابط الترحيل الموثق | FAS-SET (رابط FO→Finance) |
| I4 | تعليمات Cashier/Housekeeping تظهر عند Night Audit | Night Audit (داخلي) | REG → NA | pop-out وقت Night Audit | FOM-REG ص84 |
| I5 | تفاعل تمديدات الهاتف مع check-in/checkout | Telephones | FO ↔ TEL | two-way communication link (Activate/Deactivate + Local/STD/IDD) | FOM-REG ص102 |
| I6 | رسائل SMS للحجوزات/check-ins/الشكاوى/المغادرات | SMS Gateway (داخلي) | FO → SMS | Send SMS (Yes/No) + Adhoc SMS + SMS Status real-time | FOM-REG §27-28 + RES ص16 |
| I7 | صور الضيف → Guest History | Guest History (GST) | REG → GST | إذا Post History = Y | FOM-REG ص66-67 |
| I8 | Room Blocks (OOO/OOS) | Housekeeping / Maintenance | RES ↔ HSK/MNT | OOO بـ Department + Reason؛ OOS للصيانة | FOM-RES ص54-56 |
| I9 | الودائع تظهر عند Check-in | (RES ↔ REG داخلي) | RES → REG | "details of the deposits... displayed at the time of check-in" | FOM-CAS ص9 |
| I10 | فواصل POS إعادة الطباعة من FO | POS | FO ↔ POS | Reprint POS Bill (تاريخ/شهر + مطعم + Normal/Compliment + Bill#) | FOM-CAS ص43 |
| I11 | Billing Broadcast للمنافذ | POS/Outlets | FO → Outlets | رسائل scrolling عند الفوترة لفترة محددة | FOM-REG §24 |
| I12 | Group Billing Instructions توجيه منافذ محددة | POS/Outlets | FO → Outlets | Clubbing فواتير أعضاء المجموعة لفوليو القائد حسب الـ Outlet | FOM-REG §21 |
| I13 | Vouchers للمجموعات | (داخلي) | REG → Reg# متعددة | Extension Password لكل Reg# | FOM-REG §25 |
| I14 | Invoice by Arrival لوكيل سفر | AR/Travel Agents | FO → Agent | فاتورة لحجوزات الوكيل + Control Report | FOM-REG §9 |
| I15 | Tag Agent Commission | AR | FO ↔ AR | وسم الفواتير المسددة (تختفي من قائمة الدفع) | FOM-CAS §19 |
| I16 | Hurdle Rate / Daywise Over Booking | Revenue Management (داخلي) | FO | تعرفة يومية + سقف overbooking | FOM-REG §14/§22 |

> `[PENDING]` تكاملات FOM-SET (بنية التكوين) وFOM-REP (تقارير للوحدات) تُوثق بعد القراءة العميقة. راجع `docs/analysis/00-discovery/document-map.md` §1-6 للروابط المحاسبية الست.
