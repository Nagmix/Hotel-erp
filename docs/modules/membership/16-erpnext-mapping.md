# 16 — الإسقاط على ERPNext/Frappe (Seed Mapping) — وحدة MEM

> **F-ME-1..12**: وحدة العضويات **ليست نمط ERPNext النووي** (لا Club Management في Core) — لكن Frappe يملك بذرة قوية غير متوقعة: **Membership doctype في تطبيق non-profit** + بنية Subscription/Recurring Invoice + Price Lists الثلاثية. التقدير: **7-9 أصول مخصصة** — وحدة متوسطة صعوبة (أسهل من HRP، أصعب من CARE).

---

## 1. قرار الهوية المركزي

### F-ME-1: Member = Customer (مع Is Member flag) ⭐
- الأصل: Membership Master + جسر MEMC001 → AR
- الإسقاط: **Customer** في ERPNext مع Custom Fields (`is_member`, `member_category`, `valid_upto`, `member_family` child table)
- **الزوج/الأبناء**: Contact child table بحقل `is_member` (يقابل Accept/Member flags) — نفس قرار F-CA-2 (توحيد الهوية) لكن هنا المالك هو الوحدة نفسها
- AR Account: Customer هو Account Receivable نفسه — جسر MEMC001 **يصبح مجانياً** في Frappe (العلاقة أصيلة في النموذج!)

### F-ME-2: بذرة non-profit Membership (كقالس، لا كتطبيق)
- ERPNext لديه doctypes: **Membership / Membership Type / Member** (للجمعيات) — بنية (نوع، فترة، مبلغ، تجديد) قريبة جداً
- الاستخدام: **نمط تصميمي** لاستلهام حقول `member_since/valid/amount` وليس تثبيت تطبيق non-profit كاملاً (قرار معماري: تطبيق نادي مخصص `club_membership` فوق Accounts)

## 2. محركات الفوترة

### F-ME-3: الاشتراك الدوري = Subscription/Recurring Invoices
- أصل: Process Subscription + Once/Recurring + Membership Structure (Primary/Adult/Child × Currency)
- إسقاط: **Subscription** أو Scheduler-Generated **Sales Invoice** شهرياً من Item = Revenue Code
- Once/Recurring: Item type flag — حرفياً "Once يظهر يدوياً/Recurring لا يظهر" = عزل قناتي Item يظهر في Service Bill UI أم لا

### F-ME-4: الشرائح الثلاث = Price Lists
- أصل: Member/Guest/Affiliated × Adult/Children
- إسقاط: **3 Price Lists** (أو Item Price بفلاتر Customer Group) × Items × Adult/Child = **6 Item Prices لكل خدمة** — استنساخ حرفي للماستر الأصلي
- Affiliated Club = Customer Group "Affiliated" مرتبطة بـ Affiliated Club Master doctype

### F-ME-5: Service Bill = Sales Invoice (POS-like simplified)
- أصل: Service Bill Entry (non-F&B + discount + settlement)
- إسقاط: **Sales Invoice** ضد Customer-العضو ببنود Items الخدمية + Discount row + Payment (Cash/Card/Cheque native)
- سمة #11 (default Company settlement): دائماً Account Defer — أي Invoice بلا Payment فوري

### F-ME-6: رسوم التأخير = Scheduled Job + Custom Report
- أصل: Posting Late Charges (رصيد آخر يوم من الشهر السابق لو Debit → رسوم ببنية ضريبة FO)
- إسقاط: **Monthly Scheduled Job** يقرأ GL Balance للشهر-1 → ينشئ Invoice رسوم (Item: Late Fee)
- بنية الضريبة من FO = **Sales Taxes and Charges Template** (مشترك أصلاً في Frappe — الجسر I-ME-03 يصبح مجانياً!)

## 3. دورة الانضمام

### F-ME-7: Application → Screening → Interview = Lead/Applicant pipeline
- إسقاط مخصص: **Membership Application doctype** بحالات (Submitted/Screened/Interview/Considered/Rejected/Cancelled/Converted) — استلهام **Job Applicant** من HRMS (نفس البنية النفسية!)
- Screening checklist = Checklist child table من Membership Category
- Transfer = زر "Create Membership (Customer)" — يحمل البيانات + يستدعي أول إيصال (نمط استدعاء السمات 2-5 = زر إدخال متتابع Mandatory)

### F-ME-8: الإنهاءات = Workflow states + Cascade hook
- أصل: 4 إنهاءات + تتالٍ هابط + خلافة الوفاة
- إسقاط: **Workflow** على Customer (Active/Blacklisted/Terminated/Resigned/Deceased) + **server hook** يتالي لأسفل فقط (شرط `primary` في child table)
- الخلافة: dialog اختيار البديل (أو Cancel الكل مع الالتزام بتحذير صريح — أصل GAP-UX)

## 4. الأنظمة المساندة

### F-ME-9: شركة MEMC001 تلقائي = Customer creation hook
- في Frappe: **العضو هو Customer أصلاً** (F-ME-1) — لا حاجة لإنشاء شركة منفصلة! القرار: **الإسقاط يلغي الجسر الأصلي** (تبسيط إيجابي — قارن F-CA-2)
- سمة #10 (لا رجعة) تصبح غير منطبقة — توثيق القرار في ADR

### F-ME-10: مساءلة الأحداث = Workflow + User
- أصل: AuthPerson + Reason نصيان
- إسقاط: **owner/comments + State transition** بإلزامية Reason — الاسم يُستبدل بمستخدم الجلسة الحقيقي (تحسين أمان أصيل)

### F-ME-11: CRM البريدي = Email Templates + Newsletter
- أصل: Birthday lists + Send Email + Mailing Labels
- إسقاط: **Birthday reminder report + Email Template** (Send wishes) + **Print Format ملصقات** + **Contact/Address filter query**
- Mailing Labels بترتيب Pin Code/City = Report view sorting

### F-ME-12: استعلامات الحفر = Script Reports
- أصل: Membership Summary (3 مستويات) + Spending Pattern (للفاتورة) + Settlement Query
- إسقاط: **Script Report + Drill-down links** (أنماط Query Report القياسية) + إخفاء أعمدة client-side

## 5. جدول الأولويات الهندسية (تقدير جهد)

| الأصل | الأصل النموذجي | الجهد |
|---|---|---|
| Member/Category/Family | Customer + Custom + child table | 2 أسابيع |
| Rate Master 3-tier | Price List × 6 | 3 أيام |
| Service Bill | Sales Invoice مخصص | 1 أسبوع |
| Subscription engines ×4 | Scheduled Jobs + Invoices | 2-3 أسابيع |
| Application pipeline | doctype + workflow | 1-2 أسبوع |
| الإنهاءات + الخلافة | workflow + hooks | 3 أيام |
| 38 تقريراً | Script Reports (مرحلة لاحقة) | 4+ أسابيع (Phase 7) |
| **الإجمالي التشغيلي الأساسي** | | **~6-8 أسابيع** |

> **الخلاصة:** Membership وحدة **"Accounts-front"** بامتياز — بذرتها Frappe أقوى مما يوحي اسمها (Customer+Subscription+Price Lists+Workflow تغطي 70% من البنية) — نقطة الضعف الوحيدة: **38 تقريراً** فوق المتوسط.
