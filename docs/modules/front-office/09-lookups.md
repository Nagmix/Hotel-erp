# 09 — شاشات البحث والقوائم (Lookups) — وحدة Front Office

> وثيقة FOM-LUK مقروءة **كاملة (الجلسة 3 — Quality Gate)**: 22 وظيفة Lookups + أنماط F1 Help الموثقة في RES/REG/CAS.

---

## 1. كتالوج Lookups الكامل (22 وظيفة) — FOM-LUK

> Lookups = "وصول فوري لمعلومات الضيوف والغرف وأنواع الغرف وخطط الوجبات والوصولات والمغادرات والمعاملات الإيرادية" (FOM-LUK ص2).

| # | الوظيفة | الغرض والسلوك الموثق | قواعد/تفاصيل | المصدر |
|---|---|---|---|---|
| 1 | **Rev. Management Tool** | أداة الإدارة لعرض الإيراد واتخاذ القرارات | Legend (ألوان Events/Demand Codes) + Criteria + Group By + ملخص عند Double-click على أي رقم + تمثيل بياني في الأسفل | FOM-LUK §1 ص2-7 |
| 2 | **Guest Search** | البحث في In-house + Reserved + Checked-out + Room History | تبويبات جاهزة (Inhouse/Expected Arrivals/Todays Checkout/Management Block)؛ بحث بـ Guest Name/Country/Company/Room؛ **VIP = pink**؛ Room History بنمطي Date Range أو Summary؛ Agent Record: Occupancy/Transaction/Reservation | FOM-LUK §2 ص7-14 |
| 3 | **InHouse Statistics** | إشغال الغرف/pax بأنواع الفرز | خيارا Inhouse (حتى تاريخه) أو Todays Arrivals؛ **Show Special Rooms** checkbox؛ فرز: room type/status/plan/nationality/company/rate | FOM-LUK §3 ص15-17 |
| 4 | **Expected Arrivals** | وصولات نطاق تاريخ بخصائص | فرز بـ room type/arrival time/company/group؛ **Company وType حصرية** (اختيار شركة يعطّل النوع والعكس)؛ Guest Detail بثلاث عمليات: **Link to Guest History** (Visit/Likes/Complaints/Preferences/Spouse/Card) + **Guest Message** (رسالة للضيف المحجوز) + **Print Reg Card** (عدد نسخ) + Summary | FOM-LUK §4 ص18-25 |
| 5 | **Waitlist Query** | حجوزات قائمة الانتظار بنطاق تاريخ | Property + date range | FOM-LUK §5 ص25 |
| 6 | **Provisional No Show** | No-shows الافتراضية ليوم المحاسبة | **بناءً على arrival time المحدد في الحجز** | FOM-LUK §6 ص26 |
| 7 | **Hotel Position** | جرد الغرف التفصيلي + rack سنوي | Detailed Position (حالات كل الغرف؛ Next للتنقل؛ Print) + Yearly Chart (Double-click للشهر → التوفر)؛ **تمثيلات بيانية + أرقام** | FOM-LUK §7 ص27-29 |
| 8 | **Room Status** | الحالة اللحظية (Clean/Dirty/OOO/Vacant/Occupied) | فرز بنوع الغرفة/البلوك/الطابق (أو All)؛ **color legends + عدّاد لكل حالة**؛ Room Browser: Guest/Block/Lost&Found/Features/Room History | FOM-LUK §8 ص29-31 |
| 9 | **Vacant Rooms** | الشاغرة بنوع + خصائص | فرز بخصائص الغرفة | FOM-LUK §9 ص31 |
| 10 | **Room Blocks** | أنواع البلوكات (Guest/Maintenance/Management) بنطاق | From Date + Property + Block type | FOM-LUK §10 ص32 |
| 11 | **Inhouse Rates** | تعرفة + رسوم الخطة لكل المقيمين بنطاق | Load مباشر | FOM-LUK §11 ص33 |
| 12 | **Quick Balances** | رصيد الغرفة عبر رقمها | كل معاملات الغرفة (مشتريات/مدفوعات/الرصيد) + تفاصيل بالتاريخ عند Double-click | FOM-LUK §12 ص34-36 |
| 13 | **Rate Query** | أسعار كل نوع غرفة بين تاريخين | **Arrival ≥ تاريخ المحاسبة؛ Departure ≥ Arrival**؛ Property + Company؛ النتيجة: تعرفة كل نوع | FOM-LUK §13 ص36-38 |
| 14 | **Exchange Rates** | العملات بأحدث سعر صرف ليوم معين | عرض فقط | FOM-LUK §14 ص38 |
| 15 | **Todays Check Outs** | مغادرات اليوم (متوقعة/منتهية) | خيارا Expected أو Checked Out + Load + إجمالي + تفاصيل Guest/Room | FOM-LUK §15 ص39 |
| 16 | **Check Out Status** | مغادرات تاريخ معين | **date ≤ تاريخ المحاسبة**؛ الحقول: Bill#/Room#/Company/Group/Guest/Net/Status/DateTime؛ Print + Clear | FOM-LUK §16 ص40-41 |
| 17 | **View Billing Broadcast** | بث الفوترة للمنافذ المعرفة | **date ≥ اليوم** | FOM-LUK §17 ص41-42 |
| 18 | **Agent Chart** | تخصيص غرف الشركة **لمدة 30 يوماً** من تاريخ | Company + Property؛ عرض بأنواع الغرف | FOM-LUK §18 ص42-43 |
| 19 | **Delivery Pending** | تسليمات الغسيل غير المنجزة بتاريخها | التاريخ الافتراضي = اليوم | FOM-LUK §19 ص43-44 |
| 20 | **Browse Lost Articles** | المفقودات (مستلمة وغير مستلمة) | نطاق التاريخ **داخل الشهر نفسه**؛ إدخال عودة المفقود: Date + Whom + **Authorized By** + Confirm؛ قائمة Return + Print | FOM-LUK §20 ص44-47 |
| 21 | **Revenue Forecast** | **ARR لنطاق 15 يوماً** (يحسب End آلياً) | **Include Complimentary/House Guest in ARR** checkbox؛ فرز: Room Type/Company/Group/Guest Classification/Nation/Business Source/Market Segment/Provisional Booking؛ توسع بالـ Double-click + Print | FOM-LUK §21 ص48-50 |
| 22 | **Room History** | إشغال الغرفة وتنقل الضيوف بين الغرف/البلوكات | بنطاق تاريخ (راجع Guest Search) | FOM-LUK §22 ص50-51 |

## 2. أنماط البحث الموثقة (من RES/REG/CAS)

| النمط | الاستخدام | المصدر |
|---|---|---|
| **Scan Booking** | بحث الحجوزات: guest name / Company / Group / arrival date / reserved date / reservation # | RES §1.3/§1.4 |
| **Length of Stay search** | بحث الوصولات بطول الإقامة | REG §2 (ص14) |
| **Guest selection في Posting** | فرز: Room# / Group / Company / Nationality / Room Type / Guest Name / Resv# / Gst.Status / Gst.Clf. / Reg# + Scan | CAS §1 (ص4-8) |
| **Reservation # selection** | Guest Name / Company Code / Group / Arr. Date / Ref# | CAS §Deposits (ص14) |
| **F1 Help الشامل** | Company / Booker / Plan Code / Pay Mode / Bill Inst / Business Source / Market Segment / Credit Card Type / Staff Code / Nationality / Department / Room / Currency / Discount Id / Room Features | مواضع متعددة |
| **Codewise / Namewise** | عرض نتائج Help بمرتبة الكود أو الاسم | RES ص5 |
| **Room Rack / Floor Plan** | عرض الغرف معلوماتياً (Block + Floor) | RES §3 + REG §5 |
| **Information Tips** | tooltip عند مؤشر الغرفة: arrival/departure, reg#, guest, rate, pax, company + بنود البلوك | RES §3 (ص61) |

## 3. سلوكيات مساعدة موثقة

- Double-click في الحقول كبديل F1 (نمط موحد في كل الوحدات).
- علامة * في Detailed Position تدل على قابلية التوسع — REG ص11.
- F5 لمسح رابط، F6 لمسح صف (Document Center) — REG ص20-21.
- F9 = Guest Note save&exit، F10 = Documents — RES ص22-23.
- **E28 سلوك الفحص الفوري:** نافذة Room Browser عند Double-click على غرفة في Room Status (5 تبويبات) — LUK §8.
