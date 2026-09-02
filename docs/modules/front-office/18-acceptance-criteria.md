# 18 — معايير القبول (Acceptance Criteria) — وحدة Front Office

> معايير قابلة للفحص مستخلصة من القواعد الموثقة (BR/V). تُستخدم لاحقاً في التحقق النهائي (Phase 16) وقبول كل شاشة/سير عمل.

---

## AC-FO-01: الحجز

1. إنشاء حجز بأقل مدخل (تواريخ/نوع/ضيوف) ثم **إثراؤه لاحقاً** بنفس الرقم.
2. التاريخ: Enter→اليوم، N+Enter→N أيام، F1→تقويم — والليالي تُحسب آلياً.
3. مطابقة أسماء Guest History وازدواج الحجز قبل الحفظ (تنبيه).
4. مجموع غرف التفاصيل = عدد غرف الحجز (رفض عند التعارض).
5. Rate Table تعرض (نوع×خطة×عملة) بأسعار Room Rate Master.
6. إلغاء حجز: سبب+معتمد+متصل؛ مع ودائع → مسار Refund إجباري.
7. Re-Instate (إلغى/No-Show) يولد **رقماً جديداً**.
8. Close Inventory (C) يمنع الحجز لليوم/النوع ويسمح بـ walk-in.

## AC-FO-02: Check-in

1. الأنماط الأربعة تعمل: Express (حجز+غرفة معينة) / Reservation Check-in / Express Walk-in (3 حقول) / Walk-in كامل.
2. Walk-in يعرض Vacant + OOO (للمنع)؛ غرفة صيانة → Alert.
3. الودائع المسبقة تظهر عند Check-in (Tag).
4. Partial Check-in: ضيف من حجز متعدد الضيوف، مع استكمال البقية.
5. Registration يرث بيانات الحجز (شركة/خطة/عملة/تعليمة فوترة).
6. إلغاء Check-in: سبب+تفويض والغرفة تعود للموقف.

## AC-FO-03: الإقامة

1. تغيير بيانات الضيف يسجل في Audit (5 أبعاد + مستخدم + وقت).
2. تعديل التعرفة للأيام المستقبلية فقط (ماضٍ → رفض).
3. نقل/تبديل غرفة: vacant فقط + التاريخ المحاسبي + تفويض.
4. Amend Stay يعدل Departure ويوازن الإقامة.
5. Credit Limit: زيادة موثقة بـ Card Use Amount أو مبلغ.
6. Stop Charges Posting يحظر Revenue codes محددة (أو الكل) للضيف.
7. Group: ربط/فصل/Link FIT + توجيه فوترة القائد (Direct/Company حسب Outlet).

## AC-FO-04: الترحيل والفوليو

1. Post Charge: Revenue+عملة+سعر صرف→Total شامل ضريبة؛ وعرض بنود POS بالنقر.
2. Room Rate: Individual (DayCount 1/0.5) وAll (تأكيد Continue/Abort)؛ تكرار Individual = آخر قيمة فقط.
3. Additional Room Rate: الأنواع الأربعة (Rate/Plan/ExtraBed/Retention) بضرائبها.
4. Fixed Charge: منع تكرار (revenue,guest,day).
5. Deposits بثلاث بوابات (Guest/Rsvn/City) + CC Authorization.
6. Paid Outs: Rooms/City + سبب من قائمة + Voucher.
7. Allowances: ضمن مدى الإقامة + Yes/No/Exempt للضريبة + Reason+Auth.
8. Print Bill يجمد الفوليو (إن Attribute16) وRelease يعيده.

## AC-FO-05: التسوية والمغادرة

1. التسويات التسعة + Multi-settlement + جزئية + Tip.
2. عدم التطابق → رفض ("not tallied").
3. التسوية الائتمانية (Companies) → AR تلقائياً.
4. إمكانية إبقاء الإشغال بعد التسوية.
5. Receipt لكل تسوية (قائمة+طباعة).
6. Split Folios يتطلب Pax>1؛ Transfer Folios بتفويض؛ Link لفاتورة واحدة.
7. Cutoff Date يفصل تسوية فترة أولى.
8. Folio Re-Instate: قبل NA فقط؛ الرئيسية قبل التابعة.

## AC-FO-06: النقدية والصرف

1. Foreex: فئات البنكنوت + عمولة + (ضريبة) → Net؛ Voucher آلي/يدوي.
2. CC Encashment: رقم آلي + عمولة%.
3. Deposit Refund: مبلغ/Retention بثلاث وسائل.
4. Tag Agent Commission: وسم + Retrieve.

## AC-FO-07: العمليات المساندة

1. Wakeup (فردي/جماعي/تذكير)، Messages، Locator، Likes، Complaints (Log/Attend/Browse).
2. Room Instructions تظهر pop-out عند Night Audit (يومي/بتاريخ).
3. Billing Broadcast: فترة+منافذ، تعديل المستقبلي فقط.
4. SMS: إرسال جماعي/فردي + حالة real-time.
5. Extension Password (رقمية، حتى المغادرة) + Activate/Deactivate (Local/STD/IDD).
6. OOO (سبب+قسم) / OOS؛ From/To ثابتة.
7. Mask VIP؛ Turn Away → Denial Report؛ Guest Photo → History (إن PostHistory=Y).

## AC-FO-08: معايير عابرة للوحدة

1. كل عملية مالية بتاريخ محاسبي، وكل تعديل حساس بتفويض موثق.
2. الأرقام المسلسلة (Res/Reg/Folio/Bill/Receipt) لا تُعاد.
3. تتبع كامل: من يتشغيل الشاشة، ومن يصرح بالعملية.
4. Multi-currency بسعر صرف اليوم في كل معاملة.
5. UI عربية RTL كاملة بمصطلحات `terminology.md` مع أرقام مرجعية لاتينية.

---

> هذه المعايير مرجع اختبار قبول الوحدة؛ تُحدَّث مع نضج التحليل وتُربط بمصفوفة Traceability (Phase 14).
