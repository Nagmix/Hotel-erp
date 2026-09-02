# 04 — سير العمل (Workflows) — وحدة POS

> 16 سير عمل (WF-POS-01..16) — من فتح الوردية حتى إقفال اليوم. العمليات من Touch Screen Manual (المصدر التشغيلي الموثق) والإعداد من POS-SET.

---

## WF-POS-01 · إعداد منفذ جديد (تأسيس)

1. **Setup Outlets**: كود ≤3 + Department/Cost Center + Linkage (FO/Finance) + Tax Structure/Currency + Round Off + Bill Init + طابعات + Flags (POS-SET §1).
2. **Outlet Sessions** → **Link Outlet Sessions** (Order من 1 + أوقات + Minimum Cover + أيام) (§2/§4).
3. **Outlet Order Type** → **Link** (**Standard KOT إلزامي** + KOT # Type) (§3/§5).
4. **Link Outlet Currencies** إذا Multi Currency=Yes (§6).
5. **Menu Master** (بنمط Attr 29) + **Kitchens** + **Menu Groups/Levels/Touch Groups** + Modifiers.
6. **Restaurant Table Master** + **Design Table Layout** (بالأرضيات والألوان) (§12/§39).
7. **Outlet Settlements** (النقد إلزامي + المختارة) (§17).
8. طابعات: KOT/Bill/Settlement/Token + Central KOT + Bill Printer Selection.
9. **POS User Access + Restrict Outlet Access** للكاشيرين.
10. **User Defined Print Forms**: نماذج Bill/KOT/NC/Invoice + **Make Project Active** (§23).

## WF-POS-02 · دورة اليوم: فتح الوردية والمنفذ (TS ص1-6)

1. **Login**: اختيار قاعدة البيانات (PMS للأصلية / Dummy للتدريب!) + Userid/Password (لوحة مفاتيح على الشاشة).
2. **Open Shift** — **لكل كاشير على حدة**: Cashier Name (افتراضي) + Restaurant + Shift → Open (Preview لعرض المسجلين) — **"If you want to change Shift you need to close previous shift first"**.
3. **Open Outlet** — **شخص واحد فقط**: Accounting Date (تاتجيء آلياً = Bill Date) + Restaurant + Session → Open — **Session change = إعادة فتح المنفذ دون إغلاق**.
4. تغيير المنفذ: Others → Change Restaurant.

**القواعد الحاكمة:** الوردية فردية لكل كاشير؛ المنفذ واحد لكل واحد؛ التاريخ المحاسبي تلقائي.

## WF-POS-03 · إدخال طلب (Order Entry) وطباعة KOT (TS ص7-15)

1. Order Entry → اختيار المنفذ.
2. **Steward Selection** (تلقائي بعد المنفذ) → **Table #** (الطاولة المشغولة).
3. **Covers**: +/- أو قيمة مباشرة (افتراضي 1).
4. **الأصناف بمستويات القائمة الأربعة**: الصفوف 1-3 = Level 1، التالية = Level 2، الأخيرة = Level 3 — **الصنف الفعلي في Level 4**.
5. **Quantity**: +/- أو QTY بلوحة الأرقام + Enter — لكل صنف.
6. **Order** → طباعة KOT **في المطابخ المعنية** (حسب Kitchen لكل صنف).
7. الشاشة الرئيسية تعرض: Total Value + Taxes + Net Amount.

**التعديل/الإلغاء (TS ص16-17):** Tables → الطاولة بأيقونة النادل → تعديلات (كميات/covers/حذف/إضافة) → **Order** — **حذف صنف يتطلبه أولاً ثم Delete Item** → **Reason إلزامية** (من قائمة معرَّفة أو إنشاء جديد بوصف وحفظ).

## WF-POS-04 · المُعدِّلات والأصناف المفتوحة والمجانية (TS ص18-22)

| العملية | الخطوات | القواعد |
|---|---|---|
| **Chaser/Modifier مفتوح** | Modifier → Open → نص + Rate (إن وجد) → OK | حر النص |
| **Modifier معرَّف** | تظهر تلقائياً عند اختيار الصنف → اختيار الزر | تُضاف مع الشحنة إن وجدت |
| **Open Item** (خارج القائمة) | Open/Not Defined → Kitchen + وصف + Group (**Type وTax تلقائيان**) + Rate → OK | **غير قابل للتعديل بعد الإنشاء — حذف وإعادة** |
| **Promo/Comp** | Promo/Comp → قيمة الصنف تصبح **صفراً** | تصنير مجاني بالقيمة |
| **Repeat Order** | Repeat → اختيار الأصناف المكررة → Confirm | إعادة إدخال سريعة |

## WF-POS-05 · الطباعة والتحويلات على الطاولات (TS ص11-12/42-45)

| العملية | المسار | القواعد |
|---|---|---|
| **Table Transfer (T.Trnf)** | Source Table (Help) + Target Table → Load → Transfer | نقل طلب لطاولة أخرى |
| **Server Transfer (S.Trnf)** | Transfer From + Transfer To → Load → YES للطاولات المنقولة → Transfer | نقل طلبات بين نادلين |
| **Link Tables** | Tables → الطاولة الرئيسية → Others → Link Tables → اختيار الطاولات → Save → Check: اختيار أي طاولة يعرض **المرتبطة كلها** → OK → **فاتورة واحدة مدمجة** | مثال موثق: 11 رئيسية + ربط 23 و31 |
| **Table Suffix** | Table Suffix → كود اللاحقة + طاولة من القائمة | **مجموع الخانات (مع اللاحقة) ≤ 6** — طاولة مؤقتة للدمج/الفصل |

## WF-POS-06 · طباعة الفاتورة (Check) (TS ص23-24)

1. **Check** → عرض **الطاولات ذات KOT فقط** ("This screen will show only those tables for which KOT Entry has been done").
2. أزرار الشاشة: **Print Bill** (طباعة + **تسوية تلقائية نقداً!**) · **Provisional/Dummy Bill** ("Check with zero Bill Number") · Discount · Tax (إعفاء) · View KOT (أرقام KOT + أنواع الأصناف Food/Liquor/Tobacco + Menu Groups + **Split Numbers**).
3. عرض: Bill Amount (البيع الفعلي) + Discount + Taxes + Net.

**إعادة الطباعة قبل التسوية (TS ص41):** اختيار الطاولة ذات أيقونة الطابعة → **"Re-printing a check before settlement cancels old check number and generates a new check number"**.

## WF-POS-07 · الخصومات (TS ص25-26)

| النمط | المسار | القواعد |
|---|---|---|
| **Manual** | Discount → Type (%/Amount) → القيمة (لوحة أرقام) → Reason → OK | **Discountable Amount يأتي آلياً**؛ مثال: 10% |
| **Predefined/Revenue** | **Revenue Discount** → Options: **Predefined** → Load → اختيار Discount Code من الجدول → OK | مرتبط بـ Company Profile (راجع ACR §1.7) |
| **Happy Hours** (آلي) | يطبَّق ضمن الفترة المعرفة (POS-SET §31) | نسبة/مبلغ + أيام الأسبوع |
| **Member Discount** | بالبطاقة/العضوية (POS-SET §41) | منفذ × نوع قائمة + INI 404 |

## WF-POS-08 · إعفاء الضرائب (TS ص27)

1. **Tax** → تبديل **Tax Tag → YES** للضرائب المستثناة (مثال موثق: V02 وV03 "exemptible Taxes").
2. Reason → OK → **Tax Amount = 0.00**.

## WF-POS-09 · تقسيم الفاتورة (Split Check) — ثلاث طرق (TS ص28-31)

| الطريقة | الخطوات | مثال موثق |
|---|---|---|
| **Equal / by Covers** | Split Equal → عدد التقسيمات (لوحة أرقام) → Enter | فاتورة → جزأين |
| **Item-wise** | **Split Bill** → قيم Split للأصناف → OK → Print Bill (للمحدد فقط؛ اختيار الجميع يطبع تتابعياً) | "Food Bill Separately & Liquor Bill Separately" |
| **Quantity-wise** | **Split Quantity** → الصنف → الكمية (لوحة) → Enter — **"Value should be less than the actual item quantity"** → ثم Split Bill | **كمية 1 → 0.5 و0.5!** |

## WF-POS-10 · التسوية (Settlement) (TS ص32-36)

> **القاعدة الذهبية: "Make sure Balance on Main Screen is 0.00... otherwise check will not be settled"** — والأنماط الفاعلة حصراً: **Cash · Credit Card · Cheque · Coupon · Guest · Void**.

| النمط | الخطوات | حقول خاصة |
|---|---|---|
| **Cash** | Check No → Cash → المبلغ المستلم → OK | **Balance = الباقي للضيف** (الصرافة) |
| **Credit Card** | Check No → CC → **Swipe Card (التركيز في حقل السحب — التفاصيل تُلتقط آلياً!)** → **Tips** → OK | قراءة البطاقة بالسحب |
| **Cheque** | Check No → Cheque → Cheque No + Date + Bank + Branch → Tips → OK | المبلغ آلي |
| **Coupon/Gift Voucher** | Check No → Coupon → Coupon Number + Remarks → OK | خصم/هدية |
| **Guest** | Check No → Guest → **Room # + Enter → اختيار الضيف من الجدول** → Tips → OK | **"AR or Company Settlements and Bill on Hold Settlements are same as Guest Settlements"** |
| **Void** | Check No → Void | إبطال مع السبب (Reason) |
| **Resettlement** | اختيار Check مسوّى (Help) → **"Bill is already Settled. Do you want to resettle it?"** → YES → التسوية بوضع آخر | إعادة تسوية |

## WF-POS-11 · عمليات NC (Non Chargeable) (TS ص37-40)

1. Others → **NC KOT** (أو زر NC الرئيسي).
2. **NC Details** → اختيار **NC Type من Order Types** → **Department** (من الأقسام المعرفة في §7: داخلية أو خارجية Tax/Justice/Health) → **Guest Name** (المُستضاف) → OK.
3. متابعة Table/Server/Item كالمعتاد → Order (KOT).
4. **NC Bill Print** → اختيار الطاولة بـ Help → Print.
5. **NC Tips** إن لزم.

## WF-POS-12 · ضيف History والولاء (POS-GST)

1. **Guest Master** (بعد اختيار المنفذ) → تبويبات البيانات العشرة (راجع `01-master-data.md` §5).
2. **Post Guest History**: المطعم + التاريخ (**≤ تاريخ المحاسبة**) + Session (أو All) → Load → **Double-click على القيد** → بحث الضيف → **Yes للتأكيد** — وإن لم يوجد: **إنشاء سجل جديد فوراً** (ص24-28).
3. **Loyalty**: Setup Cards → **Loyalty Master** (بطاقة + ضيف + خصومات منفذ×نوع) → Post بعدها يغذي الزيارات.
4. قوائم: Anniversary/Birthday/Repeat + Labels/Letters + Comments/Analysis.

## WF-POS-13 · إدارة الأسعار والقوائم (POS-SET §25/§28/§29)

| العملية | الأداة | القاعدة |
|---|---|---|
| تحديث سعر صنف/مجموعة | **POS Rate Master** (منفذ + From/To + Currency) | سريان Applicable From |
| **نقل أصناف بين منافذ** | Rate Master → Transfer (Source → Target) | **"foreign currencies of the source restaurant should match with the target"** |
| تعديلات فورية | **Quick Menu Update Option 1** (ساعات/مستويات/تكلفة/طابعات...) | **فوري عند إعادة تحميل Order Entry** |
| تعديلات اسم/مجموعة | **Option 2** (New Name/Short/Group) | **من الغد فقط** |
| تغيير جماعي | **Batch Rate Change** (All/Range + عمود Tax قابل للتغيير) | منفذ + Applicable From |

## WF-POS-14 · دورة KOT Books (POS-SET §30/§37)

1. **Issue KOT Book**: مطعم + نوع KOT + Start/End + المستلم — **≤100 ورقة**.
2. أثناء الطلب: نمط **Validate KOT book** يتحقق من رقم الكتاب الصادر للنادل.
3. نهاية السنة: **Void KOTs** (تحت Billing) → **Purge KOT Books** (لنوع Validate حصراً) → Delete=Yes → Save.

## WF-POS-15 · اليوم: إقفال الوردية والمنفذ (TS ص46)

1. **Close Shift** — لكل كاشير: اختيار Cashier ID + **Password** → OK.
   - **الحاجب: "if Pending KOTs/Bills exists in your ID you will not be able to close your shift"**.
2. **Close Outlet** — شخص واحد: اختيار المنفذ → Close → تأكيد YES.
   - **الحاجب: "If pending KOTs/Bills exists you will not be able to close outlet"**.

## WF-POS-16 · صيانةNC والتقارير المخصصة

- **Update NC Change**: مطعم → Group → نسبة NC → Save (§40).
- **Sales Report Definition**: أعمدة التقرير (A/C Group/Taxes/Round Off/Discount/Total/Settlement(s)/Tip(s)) + معاينة (§16).
- **DSR Session Group**: تجميع ≤3 فئات (Breakfast/Lunch/Dinner) لخدمة DSR (§36).
- **Guest Survey Template** → **Guest Comments Entry** (في GST §10) → **Analysis**.
