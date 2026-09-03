# 00 — نظرة عامة على طبقة تقارير Point of Sale (Phase 7)

> **المصدر:** POS-REP (158 ص / 3,898 سطر — أضخم ملف تقارير متبقٍّ في الحزمة، وثاني أضخم ملف REP بعد FOM-REP).
> **الموقع في المشروع:** هذه الطبقة تُكمل — ولا تكرر — `docs/modules/point-of-sale/08-reports.md` (الذي وثّق 18 مخرجاً تشغيلياً من SET/GST/LUK + محرك IDS قبل قراءة REP).

---

## 1. النطاق والإحصاء

| البند | القيمة |
|---|---|
| ملف المصدر | `FN6i-NT-POS-REP.txt` (158 ص) |
| عدد الأقسام المرقّمة في TOC | **24 قسماً** (1–24) |
| بنود فرعية مرقّمة | 1.1–1.16 (المبيعات **16**) + 5.1–5.6 (التحصيل 6) + 6.1–6.3 (الخصومات 3) + 7.1–7.3 (التوصيل 3) + 11.1–11.4 (NC 4) + 16.1–16.5 (الضرائب 5) + 17.1–17.5 (التدقيق 5) = **42 تقريراً فرعياً** |
| أقسام مفردة | 2, 3, 4, 8, 9, 10, 12, 13, 14, 15, 18, 19, 20, 21, 22, 23, 24 = **17** |
| إجمالي بنود الكتالوج | **59 بنداً** (42 + 17) |
| بنود بلا متن (أشباح) | **§24 KDS REPORT** — عنوان في TOC + عنوان في ص157-158 ثم تنتهي الوثيقة — صفر جسم → **UNK-083** |
| ازدواج تسمية | **Discount Register موثق مرتين** (§6.1 و§12 بمعايير مختلفة!) → **C-POS-01** |
| تقدير التقارير الفريدة القابلة للتوليد | **~57 تقريراً فريداً** (59 − شبح KDS − تكرار Discount Register) |
| مرجع التاريخ الغالب | Accounting Date (الأغلبية) ثم Server/Current Date — انظر `10-date-validation-matrix.md` |

**التعريف الرسمي للوحدة** (REP ص4 — حرفياً):

> "Reports - Reports is a sub-module under Point Of Sale Module... used by Users to generate various reports relating to **sales, bill settlements, tax, audits, revenue** etc. and use these reports to ensure all the day to day operations at the outlet are working smoothly."

لاحظ الترتيب في التعريف: sales → settlements → **tax → audits** → revenue — الوحدة الوحيدة التي تضع التدقيق والضرائب في صلب تعريفها الغرضي (بازل FO التي وصفت نفسها بـ"information/print/audit" فقط).

## 2. مفارقة الترتيب الفيزيائي (TOC ≠ الجسم)

الجسم لا يطابق ترتيب الفهرس: القسم **§6 (Discount Reports, ص96-103) يقع فيزيائياً بعد §11 (NC Sales, ص88-95)** — أي أن تسلسل الصفحات الفعلي هو:
1→2→3→4→5 (ص5-75) → **7** Delivery (ص75) → 8 Loyalty → 9 PAN → 10 Re-print → **11** NC (ص88) → **6** Discount (ص96!) → 12 (ص103) → 13→24.

هذا دليل تحريري على **إدراج لاحق لكتلة الخصومات** (أو إعادة ترتيب صفحات دون تحديث الفهرس) — نفس ظاهرة "الترتيب ليس مجموعات" في FOM-REP لكن هنا **انزياح فيزيائي فعلي لقسم كامل**. يُوثّق ضمن C-POS-01 (عائلة أخطاء Discount).

## 3. العائلات الموضوعية (خريطة الكتالوج)

| العائلة | البنود | عدد | ملف التوثيق |
|---|---|---|---|
| محرك التقارير والبنية التحتية | POS Report Options + قنوات الإخراج + Port ID | — (عرضي) | `01-report-engine-infrastructure.md` |
| تقارير المبيعات | 1.1–1.16 + 13 + 14 + 15 | ~19 | `02-sales-reports.md` |
| التسوية والتحصيل (Cashier/Shift) | 2, 3, 4 + 5.1–5.6 | 9 | `03-settlement-collection-reports.md` |
| الخصومات وNC والتوصيل | 6.1–6.3 + 12 + 11.1–11.4 + 7.1–7.3 | 13 | `04-discount-nc-delivery-reports.md` |
| الضرائب والامتثال الهندي | 16.1–16.5 + 9 PAN | 6 | `05-tax-statutory-reports.md` |
| التدقيق (KOT/Bill) | 17.1–17.5 | 5 | `06-audit-reports.md` |
| قوائم الماستر (Menu/Modifier/Happy Hours) | 18, 19, 20, 21 | 4 | `07-menu-master-lists.md` |
| التحليل وMenu Engineering | 22 (Menu Eng.) + 23 (Cover Analysis) | 2 | `08-analytics-menu-engineering.md` |
| الولاء وإعادة الطباعة وKDS | 8 + 10 + 24 | 3 | `09-loyalty-pan-reprint-kds.md` |
| مصفوفة قواعد التواريخ | — (عرضي) | ~20 قاعدة | `10-date-validation-matrix.md` |
| التحويل والفجوات | F-PR-1..15 + GAP + AC | — | `11-erpnext-mapping-gaps.md` |

> ملاحظة: بنود التحليل 13/14/15 (Popularity ×2 + Order Analysis) وُزّعت عملياً داخل `02` (سياق المبيعات) مع إحالة من `08` الذي يحتفظ بالتحليل الأعمق (Menu Engineering 15 عموداً + Cover Analysis 80/132).

## 4. أبرز الاكتشافات البنيوية (Session 17)

1. **مصفوفة POS Report Options** (أول نمط Config-per-Report في المشروع): إدراج Void/Complimentary في التقرير **يُضبط لكل تقرير على حدة** من SETUP → POS Report Options — ~15 تقريراً على الأقل مرتبط بهذه المصفوفة، مع الثابت الحرفي: *"The Void and Complimentary sales details will appear in the report but the sales amount will NOT be included in the grand total"* — ظهور بلا احتساب (Invariant) يُختبر رقمياً (AC-PR-04).
2. **مفتاحا INI جديدان من ملف تقارير واحد**: **Switch 137** (عتبة PAN — امتثال هندي: "PAN information is required for settlements above the prescribed limit. This is affected by Switch 137") + **Switch 335** (F&B Factor % في Menu Engineering) — عائلة INI تتوسع (63/368/475/511 → +137/335) والـREP نفسه أصبح مصدر مفاتيح نظامية.
3. **Menu Engineering بمعجم STAR / PUZZLE / PLOW HORSE / DOG** (§22): مصفوفة 2×2 (CM Class × MM Class) بصيغ حرفية كاملة + عمود Profit Factor — **أعمق منهجية تحليلية في المشروع كله** (نموذج Kasavana-Smith الكلاسيكي مطبقاً حرفياً).
4. **DS Report (§1.6)**: مصفوفة 8 أعمدة زمنية (Breakfast/Lunch/Dinner/Day/LastWeek/WTD/MTD/YTD) × 11 مقياساً (Sales/Trans/APT/Covers/APC/Tax/Cash×2/Credit×2/Tip) وكل عمود ينشطر Amount+% — مع عمود تنبؤ بلغة عامية: **"Where are we headed with this average?"** = (إجمالي MTD ÷ أيام الشهر) × عدد الأيام المنقضية.
5. **Bill Audit (§17.5)**: إعادة التسوية تُعرض بزوج **قديم→جديد كامل** (old mode+amount → new mode+amount) — أثر تدقيق قبل/بعد لإعادة التسوية، أغنى من تعديل الكمية في KOT Audit.
6. **Settlement by Bill # (§2)**: الفواتير الملغاة تُعرض **مع أرقام الفواتير الجديدة البديلة** (rebill linkage) + مستخدم العملية.
7. **Cashier Summary (§5.2)**: التقارير **للورديات المغلقة فقط** ("You can generate reports only for Closed Shifts") — بوابة دورة حياة وردية في قلب طبقة التقارير.
8. **80/132 بعكس دلالة FO**: في POS الصيغة 132 **تضيف** معلومات (Popularity Time: المبالغ · Cover Analysis: نوع القائمة الخامس "Others" + عمود Total) بينما 132 في FO كانت **تحذف** YTD — عائلة XOR ذات اتجاهين متعاكسين بين الوحدتين!
9. **Happy Hours List (§19)**: التقرير **الوحيد** الذي يقبل تواريخ مستقبلية ("The From date can be less than, equal to or greater than the accounting/system date") — استثناء وحيد في مصفوفة التواريخ كلها.
10. **تعريف City Ledger حرفياً** (§16.4): "where the bills of the Guest are debited to his Company" — شاهد جسر AR من داخل تقرير ضرائب.
11. **KOT Books Usage (§17.1)**: تدقيق دفاتر KOT الورقية (used/unused/void + تاريخ الإصدار + المستلم) — طبقة جنائية ورقية.
12. **أخطاء تحريرية ثلاثة**: C-POS-01 (Discount Register مرتين) + C-POS-02 (إحالة Discount Summary إلى "Sales By Item" — خطأ نسخ/لصق) + C-POS-03 (تكرار الخطوة 3 حرفياً في Menu List).

## 5. علاقة هذه الطبقة بالوحدات الأخرى

| الجسر | الاتجاه | الشاهد |
|---|---|---|
| POS → SYS | اعتماد | INI Switch 137 + 335 + محرك IDS Report Engine (R-POS-09) |
| POS → FAS | محاسبي | Tax Reports كلها (16.1–16.5) تُغذي كشوف الضرائب؛ City Ledger → AR |
| POS → AR | تسوية | تعريف City Ledger (16.4) + أنماط Settlement: Company/Cheque/City Ledger |
| POS → FO | تشغيلي | نمط Settlement "Room" (5.1/1.9) — نقل فاتورة الضيف إلى Folio |
| POS → FNB | تحليلي | Food Cost في Menu Engineering (22) يقابل Cost% من Recipe Master في FNB-SET |
| POS → HRP | تشغيلي | Servers/Cashiers ككيانات مستخدمين في 1.11/5.2/5.4 |
| POS → Guest History (GST) | تكاملي | Loyalty Report (8) يستهلك Loyalty Card Master من POS-GST §4 |
| POS ↔ KDS | شبح | §24 عنوان بلا جسم — أول ذكر KDS (Kitchen Display System؟) في الحزمة → UNK-083 |

## 6. ملاحظات الجرد (POS-REP)

- **التقارير الكبرى الخمس** التي تستحق اسم "منصة" وليس "تقريراً": DS Report (1.6) · Weekly Manager (1.10) · User Defined Sales Report (1.16) · F&B Menu Engineering (22) · Tax Register (16.1).
- **User Defined Sales Report (1.16)** يستهلك **Sales Report Definition** من POS-SET §16 (7 أنواع أعمدة نظامية) — الطبقة المخصصة الموثقة في R-POS-07 تتصل الآن بمولّدها الفعلي.
- **DSR Session Group** (شرط عمل DS Report: "In SETUP, DSR Session Group has to be defined") = جسر تكوين إلزامي نادر: تقرير **لا يعمل أصلاً** بدون Setup مسبق (بازل FO: Room Rate for the Day "only once the Tariff is posted").
- الخدمات/الطابعات: حقل **Port ID** (اختيار الطابعة) في 1.5/5.3/5.4 — قناة إخراج خامسة ضمنية موجودة فقط في POS.
