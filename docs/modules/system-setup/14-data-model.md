# 14 — نموذج البيانات (Data Model) — وحدة System Setup

> 32 كياناً — الأكبر بين الوحدات لأنه يحمل كل المرجعيات المشتركة + طبقة الصلاحيات.

---

## 1. كيانات المستخدمين والصلاحيات (7)

| الكيان | الحقول الجوهرية | المفتاح | علاقات |
|---|---|---|---|
| **User** | user(10), name(40), short_name(10), designation→Designation, group→UserGroup, supervisor(bool), password(auto), password_expires(days≤3), status | user | 1→N UserAccess, UserMenuAccess, ReportAccess |
| **UserGroup** | group_name (إنشاء بالنص الحر) | group_name | N→M User |
| **UserAccess** | holder(group/user) × main_module × sub_module × menu_item × can_add/can_modify/can_delete | مركب | →User/UserGroup |
| **UserMenuAccess** | user × menu_program[≤3] × graphs[3-5] × default_graph × guest_info(bool) × statistics(bool) | user | →User |
| **ReportAccess** | user × module × report × spool(bool) × export(bool) × format(Excel/OpenCalc/Direct) | مركب | →User |
| **PasswordHistory** [INFERENCE اسم] | user, new_password, reset_by, reset_date | — | →User (الدليل يعرض expiry/last-changed في User Management) |
| **Caption** | menu_item, standard_name, new_name, apply_to_report(bool) | menu_item | →عناصر القوائم |

## 2. كيانات المرجعيات العامة (18)

| الكيان | الحقول (الأطوال) | قيود خاصة |
|---|---|---|
| **Property** | code(3), name(30), short_name(10), round_off(enum: None/Nearer/Higher/Lower), round_amount(num), address(→Address), applicable_from, status | تعديل: العنوان+الحالة |
| **Address** | نموذج فرعي من Property | — |
| **Department** | code(4), name(30), short_name(10), module(enum: General/Banquet), applicable_from, status | الحالة فقط |
| **CostCenter** | code(4), name(30), short_name(10), applicable_from, status | الحالة فقط |
| **Designation** | code(3), name(30), short_name(10), guest_type(enum: Guest/Others/S&M), applicable_from, status | GuestType+الحالة |
| **UOM** | code(3), unit_name(15), applicable_from, status | الحالة فقط |
| **ReasonCode** | module(enum×9: Banquets/Finance/FO/GiftShop/Laundry(s)/Membership/POS/Purchase/Sales), code(3), description(20), applicable_from, status | الحالة فقط |
| **Currency** | code(3), name(30), short_name(10), type(enum: Currency/TravellersCheque), local(enum: Local/Foreign), standard_rate(default 1), display_format(enum: Million/Lakh), division_method(bool), text_before(20), text_after(20), decimal_length(0-3), applicable_from, status | DivisionMethod+الحالة |
| **ExchangeRate** | currency→Currency, serial(auto 1-4), time, rate, applicable_from | ≤4/عملة؛ آلي |
| **TaxCode** | code(3), name(30), short_name(10), applicable_to[FO,POS,Banquet,Purchase], applicable_from, status | الحالة فقط |
| **TaxSlab** | module(enum×7), slab_code(num 4), description(30), tax_code→TaxCode, cumulative(bool), rows[serial(auto 0+), amount_from(auto), amount_to, cal_type(Pct/Amount), factor], applicable_from, status | الحالة فقط |
| **TaxStructure** | module(enum×7), structure_code(num 3), description(30), items[tax#(auto 1+), tax_code→TaxCode, calc_type(Pct/Amount/Slab), factor, slab#(Slab only), on(enum: Value/DiscountedValue/Tax), on_tax#(Tax only)], applicable_from, status | الحالة فقط |
| **GuestComment** | code(auto; 1-25 system), description(30) | تعديل ≥26 فقط |
| **CreditCardType** | card_type(10), floor_limit(12.2), card_file_drive(N/A), conversion_id(N/A) | — |
| **PrintBillMessage** | from_date, to_date, subject(10), outlets[], message(100) | فترة صلاحية |
| **Religion** | code(2), description(30), applicable_from, status | الحالة فقط |
| **Occupation** | code(2), description(30), applicable_from, status | الحالة فقط |
| **GroupNationality** | [UNCERTAIN] — شاشة اختيار + Save بلا حقول موثقة | — |

## 3. كيانات الإعداد التقني (7)

| الكيان | الحقول | ملاحظات |
|---|---|---|
| **ModuleAttribute** | module, attribute_no, attribute_name [NOT DOCUMENTED — خارج الحزمة], value(Yes/No, default No) | 1..67+ لكل وحدة |
| **INIFile / INIKey** | file(N6IRPRP.BAS مصدر), key(مثل 56/58/64/74/283/404/504), value, description [خارج الحزمة] | GAP-SYS-D01 |
| **FODefault** | property→Property, field(14 enum), value(ref) | 14 قيمة |
| **ProgramID** | module(FO/AR1/AR2/AR3/Laundry), form_name, program_id(7), printer_port(enum: LPT1/LPT2/COM1/COM2/COM3/USB) | جدول 20+ نموذجاً seed |
| **DBExtraction** | tables[], include_history(bool), month_year(MMYY), mode(Table/SelectAll/GUI/File), target(C:\PMSDATA .INS) | — |
| **User mgmt audit** | user, status_change, password_reset(by/date) | عرض فقط |
| **ParameterList** | (استعلام وليس كيان تخزين) | R-SYS-03 |

## 4. مخطط العلاقات (Knowledge Graph additions)

```
User ──designation──> Designation ──guest_type──> {Guest|Others|S&M}
User ──group──> UserGroup                    UserGroup ──access──> UserAccess
User ──menu_access──> UserMenuAccess          User ──report_access──> ReportAccess
User ──supervisor(bool)──> (كل القوائم)

Property ──round_off──> BillRounding          Property ──address──> Address
Department ──module(Banquet)──> (فلتر ظهور)    CostCenter ──(استهلاك POS/FO)──> Outlets
Currency ──1..4──> ExchangeRate (زمني)        Currency ──text/format──> DisplayFormat
TaxCode ──applicable_to──> {FO,POS,BQT,PUR}
TaxSlab ──tax_code──> TaxCode ──rows──> SlabRow(auto-from)
TaxStructure ──items──> TaxStructureItem ──on_tax#──> (بند سابق في نفس البنية)
CreditCardType ──floor_limit──> {FO,POS,BQT} settlements
ReasonCode ──module──> {9 وحدات}              GuestComment(1-25) ──> {FO,POS} Survey
ProgramID ──printer_port──> Printer/USB-PDF   PrintBillMessage ──outlets──> {FO,POS}
ModuleAttribute/INIKey ──module──> (كل الوحدات)
```

## 5. قيود التصميم الموثقة (6)

1. **Uniqueness**: User.user · كل Code لكل كيان مرجعي · (group, module, item) في UserAccess · (user, report) في ReportAccess · serial في ExchangeRate (≤4 لكل currency).
2. **إلزامية المراجع**: ExchangeRate→Currency · TaxSlab/Structure→TaxCode · FODefault.value→Master المصدر.
3. **قيود آلية**: SlabRow.amount_from = الصف السابق.amount_to (استمرارية) · Tax# ترقيم ذاتي · Serial تصاعدي.
4. **التجميد المرجعي (Modify-lock)**: 12+ كياناً بلا تعديل جوهري بعد الإنشاء — **يُفرض على طبقة الخدمة لا الحقول**.
5. **الإصدارية الزمنية**: applicable_from > اليوم عند الإدخال — **فعالية مستقبلية فقط**.
6. **الحدود الكمية**: Menu Programs ≤3 · Graphs 3-5 · Exchange ≤4 · Subject ≤10 · Message ≤100 · Program ID =7 · Floor Limit 12+2.

## 6. أين تُخزَّن كلمات المرور؟ (تحليل أمني)

- الدليل: عرض **مكشوف** لكلمة المرور الجديدة في عمود User Management (ص39) — [INFERENCE قوي] التخزين **قابل للاسترجاع** (غير hashed) في الأصل.
- **القرار F-SYS-6:** البنية الجديدة تمنع الاسترجاع جذرياً (hash + reset links) — النظير الوظيفي: "المشرف يعيد التعيين" فقط.
