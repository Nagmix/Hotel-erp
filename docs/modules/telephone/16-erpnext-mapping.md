# 16 — الموائمة مع ERPNext/Frappe (ERPNext Mapping) — وحدة TEL

> **F-TE-1..10** — الوحدة **أكثر وحدة تحتاج أصولاً مخصصة من نوع "محرّك"** في المشروع: قلبها محرك تسعير نبضي لا مقابل له في ERPNext، واستقبال EPABX عامل استقبال مستقل. لكن **Holiday List وContact وCountry** جاهزة! التقدير: **~7 أصول مخصصة / 4-5 أسابيع**.

---

## 1. الخريطة العامة

| مكون TEL | الأصل Frappe/ERPNext | الحالة | القرار |
|---|---|---|---|
| Holiday Table | **Holiday List** (ERPNext HR/payroll) | ✅ جاهز | F-TE-4 |
| Address Book / Yellow Pages | **Contact + Address** (+ تصنيف) | ✅ جاهز بنمط | F-TE-7 |
| Country Codes | **Country** (+ حقل كود مخصص) | ✅ شبه جاهز | F-TE-5 |
| Posting → Folio | نمط Journal/Folio كما FO | ✅ عائلة مشتركة | F-TE-6 |
| Call Record | لا مقابل | 🔧 مخصص | F-TE-1 |
| **محرك التسعير النبضي** | لا مقابل | 🔧 مخصص | F-TE-2 |
| Extension + بوابات | لا مقابل | 🔧 مخصص | F-TE-3 |
| Time-Rate Slabs (خلود زمني) | شبه (Item Price) | 🔧 مخصص أبسط | F-TE-2 |
| EPABX Worker | لا مقابل | 🔧 تكامل | F-TE-8 |
| Door Lock (Onity) | لا مقابل | 🔧 تكامل | F-TE-9 |

## 2. القرارات التفصيلية

### F-TE-1: Call Record = DocType مخصص «Telephone Call» ⭐
- حقول: extension (Link)، called_number، place، call_type (Select)، duration_sec، pt_charge، guest_charge، tax، status (Posted/Error/Unbilled)، error_type، posting_ref.
- **فهرسة:** (date، extension، call_type) — أحمال التقارير.
- الاستيراد عبر worker (F-TE-8) — لا إدخال يدوي إلا للتصحيح.

### F-TE-2: محرك التسعير (Asset #1 — الأكبر) ⭐
- **DoTypes:** `Telephone Rate Slab` (مفتاح مركب slab_code+applicable_from + فرض الخلود بالتحقق `validate: no modify/delete`) · `Area Code` · `Call Identifier`.
- **المنطق (server-side Python):** classification → routing → slab (latest-applicable-from) → holiday check → pulses → calc% → min/max → rounding → tax.
- **الأداء:** دوال rating خالصة قابلة للاختبار الوحدوي (أرقام الدليل = حالات اختبار جاهزة: 60c/100%/150%/200%).
- لا استخدام Item/Price List — التعرفة نبضية زمنية لا سعر وحدة (تجربة تمليها طبيعة النبضة).

### F-TE-3: Extension Manager
- `Telephone Extension`: link لأملاك الغرف/الأقسام (Room/Department) + calc% ×4 + line_status + local/std/idd_gates.
- `Extension Link` (جدول فرعي رئيس/أتباع).

### F-TE-4: Holiday List (جاهز!)
- تعيين واحد لكل Property + **مولد أيام الأسبوع**: dialog مخصص صغير (client script) يولد Dates — لا حاجة DoType جديد.
- الانتباه: Holiday List في ERPNext مرتبط بالرواتب — يُشارك أو يُنسخ لقائمة «Telephone Holidays» حسب القرار المؤسسي.

### F-TE-5: Country + Area
- Country الأصلي (name/code) + DoType `Area Code` (country FK + slab + min/max).
- **إدخال أولي إلزامي:** seed script يزرع الشراكات الست (LCA/9999999999×3) — و**قفل تعديلها بدور SysAdmin** (فجوة الأصل).
- فرض الشراكات بتحقق On-Submit.

### F-TE-6: الترحيل للفوليو (عائلة FO)
- نفس عمارة FO Posting: **Folio Entry** إضافي على فاتورة مسودة النزيل + Income Account لكل نوع (Revenue Code → Account Mapping).
- **Consolidate:** عملية day-end scheduler (لكل نوع Yes) تجمع اليوم في بند — مقابل بند لكل مكالمة.
- الربط الحرج: Accounting Date Pickup كما FO (ترحيل متأخر عند Repost).

### F-TE-7: Contact + Address للـYellow Pages
- Contact مع: first/last (prefix/name) + phones + email + **custom: pager?** (متجاوز تاريخياً — يحذف) + Address (residence/office بنوعين) + **Contact Category tree** (Main/Sub).
- الوصول العالمي: عنصر قائمة (navbar) — يلعب دور Panel→Yellow Pages.

### F-TE-8: EPABX Ingestion Worker (Asset #2) ⭐
- خدمة خلفية (RQ worker/Frappe background job) تستمع للملف/Serial-برنامج التحويل القديم → تنشئ Telephone Call.
- **فحوصات الاعتراض الأربعة** كحالة (status=Error + error_type) — بما فيها فحص الإشغال الفوري ضد PMS.
- قناة 2-Way: أمر كتابة للبوابة (activate/deactivate/بوابات أنواع/كلمة مرور) — معمارية: queue أوامر.

### F-TE-9: Door Lock Integration (Asset #3)
- خدمة مستقلة (app صغير) تقرأ جدول `Door Card Tx` (backend) وترسل لأجهزة Onity عبر الوسيط.
- تشغيل CI/CO كأحداث (hooks على تسجيل/مغادرة FO) — اليدوي يبقى شاشة.
- Single Open/Read: Onity-locked بالمزوّد (يُقصيران على وجود تكامل المزوّد).

### F-TE-10: التقارير
- Query Report لكل تقرير REP الثمانية — **رصف جاهز:** الفلاتر الموثقة = حقول الفلتر، و"Order By Extension#/Date&Time/Trunk" = حقول فرز.
- Print Telephone Bill = **Print Format** (Jinja) على مجموعة مكالمات الغرفة/Reg.

## 3. الأصول المخصصة والجهد

| # | الأصل | الحجم | الأسبوع |
|---|---|---|---|
| 1 | محرك التسعير + DoTypes الشرائح/المنطقة/المعرّف + اختبارات أرقام الدليل | كبير | 1.5 |
| 2 | EPABX Worker (استقبال + أوامر 2-Way) + معالجة الأخطاء | كبير | 1 |
| 3 | Door Lock Service (Onity) | متوسط | 0.75 |
| 4 | Extension Manager + بوابات + روابط + كلمات مرور | متوسط | 0.5 |
| 5 | Folio Posting (موحد/تفصيلي + Repost + Scheduler) | متوسط | 0.5 |
| 6 | Operator Console (Guest Information + Messages Tag) | صغير | 0.25 |
| 7 | التقارير الثمانية + Print Format | صغير | 0.5 |
| — | **الإجمالي** | ~7 أصول | **~4.5 أسابيع** |

- **الجاهز المجاني:** Holiday List · Contact/Address · Country · فرض القيود (Validate hooks) · الأدوار (Frappe Roles) · Report Framework.

## 4. القرارات المعمارية المستحدثة (D-TE)

| ID | القرار |
|---|---|
| D-TE-1 | التعرفة **نبضة زمنية** لا Item Price — DoType مخصص أنظف من إسقاط التجارة |
| D-TE-2 | الشرائح **خالدة** بالتصميم (validate no-update) — تتوافق مع عائلة HRP/MEM |
| D-TE-3 | **Folio دائماً مسودة الفاتورة** (نمط FO) — الترحيل الأسبوعي/Monthly Run للـGL |
| D-TE-4 | **فصل خدمات العتاد** كتطبيقات مستقلة قابلة للتوزيع (worker لا doc events) |
| D-TE-5 | إعادة الترحيل = **سجل تدقيق** (قبل/بعد + منفذ) — يسد فجوة الصلاحيات |
| D-TE-6 | كلمات المرور الرقمية تُدار كأوامر EPABX (منطق العتاد القديم) لا كمصادقة نظام |
| D-TE-7 | الشراكات seed إلزامي + قفل دور — حماية كارثة الحذف |

## 5. تقييم الموائمة الإجمالي

| المعيار | الدرجة | التعليل |
|---|---|---|
| Data Model | 6/10 | Contact/Country/Holiday جاهزة؛ القلب كله مخصص |
| Business Logic | 4/10 | محرك التسعير لا مقابل — أكبر منطق مخصص نسبياً في المشروع |
| Integrations | 3/10 | عتاد مزدوج (EPABX+Onity) — خارج نطاق ERPNext كلياً |
| UI | 7/10 | الفلاتر/التقارير/المعيار قريب؛ Console بسيط |
| Accounting | 8/10 | عائلة Folio/Posting مشتركة مع FO جاهزة |
| **الإجمالي** | **5.5/10** | وحدة "أصول مخصصة" حقيقية — الأداء التشغيلي يعوض فقر الجاهز |

> **الخلاصة:** ثالث أدنى موائمة بعد BNQ (POS-hybrid) وCARE (ساتلية PMS) — لكن بمنطق مختلف: كل أصل مخصص هنا **محرّك معرفي قابل للاختبار بأرقام الدليل** (60c × 150% = 90c!) — أي أن الفقر جاهزية يعاد خسارته بوضوح تنفيذ عالٍ.
