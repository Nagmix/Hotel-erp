# 00 — نظرة عامة (Overview) — وحدة Point of Sale (POS)

> وحدة **نقاط البيع (المنافذ)** — الأوسع تشغيلياً في النظام (مطاعم/بارات/متاجر/كافيهات...). المقروء عميقاً (الجلسة 4/5): **POS-SET (42 قسماً، 122 ص) + POS-GST (12 وظيفة Guest History، 56 ص) + POS-LUK (7 استعلامات، 14 ص) + Touch Screen Manual (34 ص — العمليات الفعلية: Shift/Outlet/Order/KOT/Bill/Settlement)**. POS-REP (158 ص) مؤجل للمرحلة 7.

---

## 1. حدود الوحدة

| البند | الوصف الموثق |
|---|---|
| الاسم النظامي | Point of Sale (POS) — "In any Property all the retails outlets where the sales happen are considered as point of sale. Example: Restaurant, Food Court, Bar, Banquets, Gift Shop, Ice Cream Café" (POS-LUK ص2) |
| الوظيفة الجوهرية | دورة مبيعات المنفذ كاملة: **فتلح Shift/Outlet/Session → Order Entry → KOT للمطابخ → Check/Split → Settlement (6 أنماط) → إقفال Shift/Outlet اليومي** (Touch Screen Manual كاملاً) |
| المركز المعماري | **مصدر مبيعات نقدية/ائتمانية** خارج الغرف: يرحّل إلى FAS (رابط POS→Finance: منفذ × مجموعة قائمة) ويسوّي ائتمانياً إلى AR (Guest/Company settlement) ويرحّل لفواتير الغرف عبر FO |
| النطاق | Outlets/Sessions/KOT Types/Currencies · Menus (4 مستويات + Rates محلية وأجنبية) · Modifiers · Happy Hours/Promotions · Tables/Layout/Booking · KOT Books · NC · Discounts (Manual/Predefined/Member/Loyalty) · Guest History (12 وظيفة) · طباعة مخصصة كاملة |
| خارج النطاق | تقارير POS التفصيلية (POS-REP — مؤجل)؛ مواد/مخزون (MGT)؛ الولائم (BNQ) |

## 2. جرد الوظائف الموثقة (42+12+7+عمليات = ~75 وظيفة)

| المجموعة | الوظائف | العدد | المصدر |
|---|---|---|---|
| **Setup** | Setup Outlets · Outlet Sessions · Outlet Order Type · Link Outlet Sessions · Link Outlet Order Types · Link Outlet Currencies · Departments for NC · Menu Groups · Servers · Server Outlet Mapping · Menu Levels · Restaurant Table Master · Item Hot Keys · Touch Screen Groups · Kitchens · Sales Report Definition · Outlet Settlements · POS Report Options · Open Items Definition · POS User Access · Setup Area · Restrict Outlet Access · User Defined Print Forms · Parameter List · Menu Master · Point of Sale Rate Master · Modifier Master · Touch Screen Modifiers · Quick Menu Update · Batch Rate Change · Issue KOT Book · Happy Hours Definition · Sales Promotion Master · Central KOT Definition · Bill Printer Selection · DSR Session Group · Purge KOT Books · Guest Survey Template · Design Table Layout · Update NC Change · Member Discount Defn. · Taxcode Mapping | 42 | POS-SET TOC ص1-3 |
| **Guest History** | Guest Master (10 تبويبات) · Setup Loyalty Cards · Setup Loyalty Master · Post Guest History · Anniversary List · Birthday List · Mailing Labels · Mailing Letters · Repeat Guest List · Guest Comments Entry · Guest Comment Report · Guest Comment Analysis | 12 | POS-GST TOC ص1-2 |
| **Lookups** | Pending KOTs · Pending Bills · Table Booking Status · Browse KOTs · Settlement Summary · Session Statistics · Consolidated Sales | 7 | POS-LUK TOC ص1 |
| **العمليات (Touch Screen)** | Login/DB · Open/Close Shift · Open/Close Outlet · Change Session/Outlet · Order Entry (4 مستويات + QTY + Modifiers + Open Items + Promo/Comp + Repeat) · Table/Servver Transfer · Link Tables · Table Suffix · Check Print (Provisional/Reprint) · Discounts (Manual/Revenue) · Tax Exemption · Split (3 أنماط) · Settlements (6 أنماط + Resettlement) · NC KOT/Bill/Tips · Day Closing | ~20 إجراءً | Touch Screen Manual كاملاً |

> ⚠️ **فجوة مصدر:** §42 Taxcode Mapping في POS-SET **بلا متن إطلاقاً** (ص122 فارغة) — GAP-POS-D01. و§10 Server Outlet Mapping عنوان بلا شرح تفصيلي (ص34-35 صورتان فقط).

## 3. المفاهيم الجوهرية الموثقة

| المفهوم | الدلالة | المصدر |
|---|---|---|
| **Outlet** | وحدة البيع الذرية: كود 3 خانات + Department + Cost Center + **Linkage (FO/Finance/كلاهما)** + Tax Structure/Currency + Round Off + Bill Init Type + طابعات (KOT/Bill/Settlement) | POS-SET §1 ص5-9 |
| **Session (فترة وجبة)** | فترة تشغيل المنفذ (Start/End 24h) مرتبة بـ Order يبدأ بـ 1 + **Minimum Cover Charge** + أيام السريان | POS-SET §2/§4 |
| **KOT** | Kitchen Order Ticket — أمر المطبخ: أنواع (Standard **إلزامي لكل مطعم** / Complimentary / Staff...) + ترقيم (Auto / **Validate KOT Book** / Manual) + كتابات KOT Books (**≤100 ورقة**) | POS-SET §3/§5/§30 + TS ص18 |
| **Check** | فاتورة المنفذ: طباعة (Print Bill) أو **Provisional/Dummy (بلا رقم)**؛ **إعادة الطباعة قبل التسوية تلغي الرقم القديم وتولد رقماً جديداً!** | TS ص24/41 |
| **Settlement** | تسوية بـ 6 أنماط فاعلة فقط: **Cash · Credit Card · Cheque · Coupon · Guest · Void** ("Others will not work") + قاعدة **Balance = 0.00 قبل الحفظ** + **Resettlement** بوضع آخر | TS ص32-36 |
| **Split Check** | تقسيم الفاتورة **ثلاث طرق**: Equal/Covers · **Item-wise** · **Quantity-wise** (كميات كسرية 0.5!) | TS ص28-31 |
| **NC (Non Chargeable)** | طلب غير محاسب: أقسام داخلية/خارجية (Tax/Justice/Health) + KOT خاص + فاتورة خاصة + Tips | POS-SET §7 + TS ص37-40 |
| **Covers** | عدد ضيوف الطاولة (± أو مباشر؛ افتراضي 1) — مقياس Average Per Check | TS ص10 + POS-LUK ص12 |
| **Steward/Server** | النادل المرتبط بالطلب (كود 3 + Employee #6) — نقل طلبات بين النادلين (S.Trnf) | POS-SET §9 + TS ص42 |
| **Table Layout** | مخطط طاولات مصمم بصرياً بأيقونات ملونة: **أخضر=شاغرة · أحمر=مشغولة · أزرق=مفوترة · بني=محجوزة** | POS-SET §39 ص112 |
| **Open Item** | صنف غير معرَّف بالقائمة: مطبخ + وصف + مجموعة (نوع وضريبة تلقائيان) + سعر — **غير قابل للتعديل بعد الإنشاء (حذف+إعادة)** | POS-SET §19 + TS ص20-21 |
| **Happy Hours** | خصومات فترة زمنية (تاريخ+وقت) لصنف أو مجموعة؛ P (نسبة) أو A (مبلغ — للصنف فقط!) + نسب لكل يوم أسبوع + **منع التداخل الزمني** | POS-SET §31 |
| **Member Discount** | خصومات العضو (نسبة) لكل منفذ × نوع قائمة (Food/Liquor/Soft Drinks/Tobacco/Others) — **INI 404**: 1=رئيسي فقط / 0=رئيسي+ثانوي | POS-SET §41 |
| **Bill Initialization** | دورة ترقيم الفواتير: **Yearly (+Init Date DDMM) / Monthly / Daily / None** | POS-SET §1 ص7-8 |

## 4. التفاعلات مع الوحدات (موثقة نصاً)

- **POS → FAS:** رابط منفذ × مجموعة قائمة → حسابات D/C (مبيعات Credit / خصومات Debit) — من الروابط الست (FAS-SET §7).
- **POS → AR:** تسويات Guest/Company/BoH = AR/Company Settlements بنمط Guest Settlement نفسه (TS ص36) → قيود مدينة تلقائية في AR.
- **POS → FO:** تسوية Guest برقم الغرفة (Room # → قائمة الضيوف المقيمين) → folio الغرفة؛ **Card Types للولاء معرَّفة في FO** ("The card types are defined in the Front Office Module" — POS-GST ص10).
- **POS ↔ FO Guest Data:** "The details captured in Guest Preferences option of **Front Office module** will be shown here" (POS-GST ص18) — تشارك تفضيلات الضيف.
- **SYS → POS:** Departments/Cost Centers/Currencies (General Setup) + Module Attributes (6 NC Bill Print · 29 Common Menu · 32 Network Printer) + INI 404 (Member Discount) + Pgm IDs.
- **MEM → POS:** Member Discount Defn تسحب الأعضاء من Membership (Member Section screen) بنِسب خصم لكل منفذ.
- **الأجهزة:** طابعات شبكية لكل مطبخ/فاتورة/تسوية/Token + قارئ بطاقات (Swipe) + PDA + Touch Screen + Online Keyboard.

## 5. أهم الاكتشافات المعمارية (الجلسة 4)

1. **ثلاثية الفتح/الإقفال اليومي:** Open **Shift** لكل كاشير على حدة + Open **Outlet** شخص واحد فقط (مع Accounting Date = Bill Date) + **Session** تُغيَّر بإعادة فتح المنفذ دون إغلاق؛ الإغلاق **يحجبه أي KOTs/Bills معلقة** — إيقاع تشغيلي يومي صارم (TS ص4-5/46).
2. **فصل المستند الثلاثي:** KOT (مطبخ) → Check (فاتورة) → Settlement (تسوية) — كل مرحلة قواعدها؛ **إعادة طباعة الفاتورة قبل التسوية تُرقِّم من جديد** (إبطال الرقم القديم) — عكس مفهوم Reprint في AR!
3. **Split الدقيق:** 3 أنماط تقسيم (متساوٍ/بالأصناف/**بالكميات الكسرية**) + **Link Tables** (دمج فواتير طاولات متعددة في فاتورة واحدة) + **Table Suffix** (طاولة مؤقتة لدمج/فصل) — عائلة كاملة من عمليات التجميع/التقسيم (TS ص28-31/43-45).
4. **قاعدة "6 أنماط فقط":** Cash/CC/Cheque/Coupon/Guest/Void هي الفاعلة حصراً في التسوية ("Others will not work") مع **إلزام توازن Balance=0** — وCash **وضع إلزامي لا يُلغى** في إعداد Outlet Settlements ("bill settlement by cash is a mandatory mode... not optional for any of the outlets").
5. **البعد الزمني للبيانات المركزية (Applicable From) في كل شيء:** كل Masters في POS-SET (Outlet/Session/KOT Type/Currency/Menu Group/Server/Kitchen/Modifier/Promotion/Hot Keys...) تحمل Applicable From + قاعدة **"المعرف بتاريخ اليوم يُعدَّل في الـ Status فقط؛ الباقي بسجل جديد لتاريخ مستقبلي"** — إصدارية زمنية منهجية.
6. **Guest History مستقل في POS:** POS-GST Guest Master **يُفتح باختيار المنفذ أولاً** (Outlet-scoped) + كود ضيف يولَّد آلياً + تفضيلات FO **تُعرض** فيه — أي: قاعدتا ضيوف (FO للمقيمين، POS للزوار) مع تشارك انتقائي → **حسم UNK-001 جزئياً** (راجع `17-gap-analysis.md`).
7. **Menu Master بنمطين:** Module Attribute **29** = YES → أصناف **مشتركة** لكل/مختارة من المنافذ؛ NO → أصناف **لكل منفذ على حدة** + نقل أصناف بين منافذ (POS Rate Master — بشرط **تطابق العملات الأجنبية** بين المصدر والهدف) + **Quick Menu Update بخيارين** (فوري عند إعادة التحميل / من الغد) + **Batch Rate Change** (All/Range + تغيير الضرائب).
8. **إدارة الكاشير المحكمة:** POS User Access (كاشير × KOT/Billing/Settlement × **نوع التطبيق: Regular/Touch/PDA!**) + **Restrict Outlet Access** (مستخدم × منافذ) + رؤية Session Statistics **للمنافذ المخوَّلة فقط** — نموذج صلاحيات ثلاثي الأبعاد.
9. **مصمم طباعة كامل مدمج:** User Defined Print Forms = **مصمم مرئي بمشاريع** (Toolbox بالأعمدة + خصائص F3/F4 + Body Details **إلزامي** + شعار + **6 صفوف = 1 بوصة** + **Make Project Active** للتفعيل) + مطابع KOT/فاتورة/Token مركزية أو موزعة (Central KOT/Bill Printer Selection).
10. **التسويات بالبطاقة تُقرأ بالسحب:** "Swipe the Card through Touch Screen Card Slot. All the details will be captured automatically" + **Tips** حقل في تسويات CC/الشيك/Guest (TS ص34-36).

## 6. خريطة وثائق الوحدة

`01` البيانات الرئيسية · `02` الإعداد · `03` الشاشات · `04` سير العمل · `05` قواعد العمل · `06` التتحققيات · `07` الصلاحيات · `08` التقارير · `09` الاستعلامات · `10` المعاملات · `11` الأثر المحاسبي · `12` التكاملات · `13` الحالات الحدية · `14` نموذج البيانات · `15` تحليل UX · `16` ربط ERPNext · `17` تحليل الفجوات · `18` معايير القبول.
