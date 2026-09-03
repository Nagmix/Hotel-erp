# 05 — قواعد العمل (Business Rules) — وحدة MEM

> **BR-ME-01..18**: القواعد السلوكية المستخلصة نصاً — أبرزها **قاعدة التتالي الهابط** (BR-ME-08) و**خلافة المتوفى** (BR-ME-09) و**مفتاح Once/Recurring** (BR-ME-03).

---

## قواعد الهوية والتوليد

### BR-ME-01: توليد رقم العضوية قابل للتبديل
"Membership number is manually entered: Yes - The Membership number has to be manually recorded. No - The Membership number is automatically generated" (SET ص11). قرار تصميمي مبكر يؤثر على كل الشاشات اللاحقة.

### BR-ME-02: MEMC001 — شركة AR من اسم العائلة
"If the Member name is DAVID S CRAIG where CRAIG is the surname / last name. When this membership master detail is saved, **a company master is automatically created as MEMC001** where 'C' is the first letter of the Surname/Last name" (SET ص12). لو No: حرف الاسم الأول بدل الأخير.

### BR-ME-03: Once/Recurring يوجهان مسار الفوترة
"Once – the corresponding Membership Revenue Code **will appear** in Revenue/Facility Entry... Recurring - **will NOT appear**" (SET ص9) — أي أن الإيراد المتكرر يفوتر حصراً عبر محرك Process Subscription الدوري، والمرة الواحدة يدوياً.

### BR-ME-04: استدعاء الإيصال من نقاط الحفظ
عائلة السمات 2-5: استدعاء شاشة Revenue/Facility عند SAVE من {طلب شركة، Corporate Master، طلب عضوية، Membership Master} — يضمن تحصيل الرسوم لحظة الانضمام/الإدخال.

### BR-ME-05: سلسلتا إيصالات
"Receipt number is separate for application: Yes - Separate running receipt number will be generated for **Members & Applicants**" (SET ص11) — فصل مسلسلات الطالبين عن الأعضاء.

## قواعد الأسعار والفوترة

### BR-ME-06: ثلاث شرائح عملاء × فئتا عمر
Member/Guest/Affiliated × Adult/Children — لكل خدمة، لكل فئة عضوية (SET ص6-8).

### BR-ME-07: الأدوار الخمسة في الأسعار الثابتة
Primary Applicant / Spouse / Child / Additional Family (Child) / Additional Family (Adult) × 5 فترات (SET ص12) — تمييز دقيق للأسرة الواحدة.

### BR-ME-08: التتالي الهابط الموحد (القاعدة الذهبية)
"If the primary member is blacklisted/terminated/resigned/deceased then the additional members, spouse, and children of the primary members are **automatically** [affected]. However, if the spouse, children, or additional members are [affected], then the **primary member is not affected** and he can continue his club membership" (MMN ص6/8/9/12 — حرفياً 4 مرات!). تتالٍ باتجاه واحد فقط: لأسفل.

### BR-ME-09: خلافة العضو الأساسي المتوفى
"If the Primary Member is deceased... You have an option to choose additional member, Spouse, or Children as the Primary Member. **If you choose 'None', then all the members of the membership will be removed**" (MMN ص11).

### BR-ME-10: إعفاء كبار السن + الاعتبارات المالية في Cover
"Select the checkbox for Adjustment Debit to be Consider and **Senior Citizen Exemption**" (SET ص15) + قيود العمر وسنوات العضوية — رسوم اجتماعية متدرجة.

### BR-ME-11: رسوم التأخير على أرصدة الشهر السابق
"if the outstanding amount is **Debit** amount then it will calculate the Latefee and post it to ACR" (MTR ص18) — لا رسوم على الأرصدة الدائنة (Credit).

### BR-ME-12: الترحيل الانتقائي
Post Subscription to AR: "By default, all subscription charges will be posted to the AR account. This facility offers the flexibility to **withhold, withdraw, or overwrite** the subscription charges" (MTR ص17).

### BR-ME-13: إلغاء ترحيل Cover الشهري
"The user can also **cancel the posting** of cover charges for the specified month" (MTR ص17) — Process/Cancel ثنائية.

### BR-ME-14: التسوية الافتراضية للشركة
"Set default settlement to Company: Yes - When a service bill entry is made, the bill will be **settled to the Company /Member account**" (SET ص12) — الدَّين أولاً ثم التحصيل.

## قواعد العضوية والعائلة

### BR-ME-15: القبول ≠ العضوية لأفراد العائلة
عمودان منفصلان في Category: Accept ("accept the details") وMember ("consider... as the Member of the Property") (SET ص4) — يمكن قبول بيانات الزوج دون منحه عضوية.

### BR-ME-16: الطفولة بحد عمري
"Children Age Limit: Enter the age limit of the children" لكل فئة (SET ص4) — يحدد تسعير Child ونهاية الاستحقاق.

### BR-ME-17: العضوية المؤبدة بلا مدة
"Tenure... will not be applicable for **Lifetime Membership**" (SET ص4) + سمة #13 تجعل UPTO إلزامياً لغير المؤبدة ("A valid date in the UPTO field has to be mandatorily recorded").

### BR-ME-18: المقابلة بوابة اختيارية مشروطة
"Select 'Yes' for Interview Required **if necessary** for the Applicant" (MPF ص13) — تحدد حالة ثلاثية Considered/Rejected/Cancelled (MPF ص21).

## ملاحظات تحليلية

- **القائمة السوداء احتجابية وليست مالية**: سمة #8 تمنع المرافق فقط — لا منع موثق للإيصالات/الفوترة (فرق دقيق عن ACR Block).
- **الشكاوى ثنائية الاتجاه**: من عضو وضد عضو (MTR ص12-13) — دورة إدارة علاقات كاملة داخل الوحدة.
- **المرشح المؤسسي**: Corporate Application ثم المرشحون كطلبات Membership Application مستقلة، وتجمعهم Transfer Corporate Application (MPF ص21-24).
