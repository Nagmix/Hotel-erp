# 04 — القوائم المالية (P&L / Balance Sheet / Trial Balance ×4) — FAS-REP (Phase 7)

> §7 (×2) + §8 + §9 (**أربعة إصدارات Trial Balance**) = 7 تقارير — قلب المخرجات المالية.

---

## 1. §7 Profit and Loss Statement

**الوصف:** "arrive at the Profit and Loss Statement for a specific **Month & Year** based on the transaction details i.e., **Income & Expenses**. The report processes the Debit and Credit transactions of General Ledger Codes."

| # | المعيار |
|---|---|
| 1 | Property + FY + date range |
| 2 | **Nil Balance Required** — "include transactions with Nil Balance" |
| 3 | **Print Summary** — ملخص القائمة |
| 4 | OK |

- قائمة **شهرية** (Month & Year) رغم إدخال نطاق — الفترة الشهرية هي نطاق القائمة.
- **Nil Balance** خيار إظهار الحسابات صفرية الرصيد (نفس عائلة Zero Balance في TB — هنا بمسمى Nil).
- **Print Summary** — نسخة ملخصة من القائمة (ثنائية تفصيل/ملخص تصل القوائم المالية).

## 2. §7 PL Report by CC/Department — **المقارنة الرباعية الزمنية**

**الوصف:** "arrive at the Profit and Loss Statement for a specific Month & Year on the basis of **Department or Cost Center**. Transaction details can be processed for all or any specific Department / Cost Center."

**الأعمدة الزمنية (حرفياً):** "details include debit and credit transaction amount, **for the month, year to date, and for the previous year along with total amount**."

| العمود | الدلالة |
|---|---|
| Month | الشهر المعالج |
| **YTD** | تراكمي السنة |
| **Previous Year** | **نفس الفترة السنة الماضية** (مقارنة YoY!) |
| Total | الإجمالي |

- **أوسع مقارنة زمنية في قوائم الحزمة**: شهر/تراكمي/سابقة/إجمالي — قائمة ربحية بأربع فترات + منظمان (Dept/CC) — **أعمق قائمة تحليلية** في FN6i (تتفوق على FO Budget).
- المدين والدائن معاً في القائمة (عرض طبيعي مزدوج).

## 3. §8 Balance Sheet Statement

**الوصف:** "process a report to ascertain the **Assets and Liabilities** of a Property for a specific Month & Year. The report reflects the Debit and Credit transactions of each Account Codes **that are grouped as Assets and Liabilities**."

- المعايير: Property + FY + **Nil Balance Required** + OK (أبسط القوائم).
- **التجميع حسب المجموعات الميزانية** — الحسابات مصنفة مسبقاً مجموعاتِ أصول/خصوم (من CoA Master) — القائمة تجميع تصنيفي لا حسابي.
- يقابل فلاتر §1 (Assets/Liabilities) — نفس التصنيف الرباعي من مصدر واحد.

## 4. §9 Trial Balance — **العائلة الرباعية**

### 4.1 Trial Balance (الأصل)
"Summary of all General Ledger Account Balances, along with the Transactions figures for a given **Date or Month and Year**." — خيارات: **Zero (Nil) Account Balances** + عرض بـ**Account Name أو Codes** + GL/**Sub Ledger** (F1).

### 4.2 Trial Balance Format 2
نفس الوصف **حرفياً** + القواعد الحاكمة:

| القاعدة | النص الحرفي |
|---|---|
| **قيد الماضي (تاريخ)** | "Date entered should be **less than or equal to the Current System Date**" |
| **قيد الماضي (شهر)** | "month and year that is **less than or equal to the Current System Month**" |
| **XOR جديد** | "Select **any one option** from **Zero balance or Print 132 Column**" — "If you select zero balance, the report displays all transactions and balances including zero balance... If you select **Print 132 column, according to the size of the columns** the report is generated" |
| By Name/By A/C Code | "the Name option... **as specified in the Sub Head Definition parameter**" |

- **XOR الأصفار×132**: أول اقتران إجباري (في FO/POS كانا محورين مستقلين؛ MGT بلا 132 أصلاً!) — **التوسعة العرضية تتعارض مع إظهار الأصفار** (منطق عرض: 132 عموداً تضيق؟).
- **Sub Head Definition parameter** — مصدر ترتيب الاسم (ماستر جديد يُذكر من التقرير — طبقة CoA الوسيطة: Sub Head!).
- past-only **مزدوج** (تاريخ وشهر) — أصرح قيود ماضية في الحزمة (FO ضمنتها).

### 4.3 Trial Balance (3.3)
"Fill in all the fields **as explained in the section 'Trial Balance Format 2'** to generate the report." — **إحالة ذاتية كاملة** (لا جسم!) — الوصف الثلاثي المتطابق حرفياً (TB = TB-F2 = TB-3.3 في النص) → الفرق **تخطيطي غير موثق** → UNK-099.

### 4.4 Trial Balance (الرابع — Print Sequence)
"used to **specify a order or sequence in which the assets or liability gets displayed**."

| # | المعيار |
|---|---|
| 1 | Property + FY |
| 2 | Date أو Month & Year (بنفس قيود ≤ الجاري) |
| 3 | **A/C Code Range أو All** |
| 4 | **Print Sequence: Sub group / Department / Cost Center** |
| 5 | **Transaction Details** checkbox |
| 6 | **Required Nil Balance** checkbox |

- **هدف التقرير = التسلسل ذاته**: إعادة ترتيب ميزان المراجعة حسب (Sub group/Dept/CC) — **تسلسل بمجموعات هرمية** (ميزان مرتب حسب شجرة الحسابات/الأبعاد).
- **Sub group** بعد **Sub Head** (TB-F2) — طبقتا تنظيم تحت الحساب: Sub Head (ترتيب الاسم) وSub group (تجميع الطباعة!) — **معجم تنظيم CoA الثلاثي**: Account → Sub group → Sub Head.

## 5. جدول العائلة المالية

| القائمة | الفترة | المنظور | الخاصية القصوى |
|---|---|---|---|
| P&L | Month & Year | طبيعي (دخل/مصروف) | Nil + Summary |
| PL by CC/Dept | Month & Year | **Dept/CC** | **4 فترات: Month/YTD/PrevYear/Total** |
| Balance Sheet | Month & Year | أصول/خصوم | تجميع تصنيفي |
| TB ×4 | Date/Month&Year | GL/SL + **Range** | **XOR 0×132 · past-only · Sub group/Head** |

**الاكتشافات التجميعية:**
1. **سلّم النضج الكتالوغي**: قائمة واحدة لكل وظيفة ثم **نسخ تناظرية** (P&L→by CC، BS→واحدة، TB→**أربع**) — TB تعامل معاملة "التقرير الذي يستهلكه الجميع" فتعددت تخطيطاته.
2. **دائرة مفاهيم CoA المكتملة من طبقة REP**: Account (1) → Category رباعية (1/8) → **Sub group (TB-4)** → **Sub Head (TB-F2)** → Account Head (كل مكان) — **شجرة حساب كاملة معلنة من التقارير وحدها!** (أدق مما وثقت وحدة MST على ما يبدو — تُقابل عند القراءة التراجعية).
3. **قواعد past-only المزدوجة** (TB-F2/4) — المراجعة لا تُستقبل (منطقي: لا مستقبل محاسبي إلا إقفال يُراجع بعد حدوثه).
4. أوصاف TB الثلاثة المتطابقة + الإحالة الذاتية في (3.3) — **أكبر عائلة نسخ-لصق نصية** في وحدة واحدة (C-FA-02).
