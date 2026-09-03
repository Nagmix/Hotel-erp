# 06 — العائلة المالية ودفاتر القيود (REP §72–106 + Guest Ledger Breakup)

> ~32 تقريراً — أضخم عائلة: من قوائم الماسترات إلى تقرير الليل وتباين الموازنة. هنا تتركز الصيغ الحرفية وقواعد XOR وقنوات الدفع.

---

## 1. الماسترات والأرصدة (72–77)

| # | التقرير | الخصوصية الموثقة |
|---|---|---|
| 72 | **Occ. List (Date Range)** | "In-house occupied guests for the given date range along with the **meal plan and tariff rates**" · **Newspaper Details** · Include Special Room · "≤ accounting date" |
| 73 | **Rate Master List** | جدول التعرفة الكامل · **All (rack+non-rack) / Rack / Non Rack** — والـNon Rack يفرع: **Rate Code wise / Company wise (مدى From-To!) / Tablewise Company / Untagged Company** · الأزمنة: "**All, Current, Past or Future**" — تعرفة إصدارية زمنية كاملة! · **Table #** dropdown |
| 74 | **Room Master List** | "type of room, **maximum PAX allowed**, rate table and User" · All Rooms أو **Range** (Start/End Room #) · Include Special Room |
| 75 | **On Line Room Balance** | **الصيغة الحرفية: "Room Balance = Previous Opening Balance + Current Tariff Charge + Luxury Tax"** · Individual (Room# → Folio # والاسم آلياً) / Group / All |
| 76 | **Credit Limit Report** | "Every room... and all the specified Credit Cards will have a certain credit limit set" · "charges incurred by the guest/s with **closing balance and variance**" · **Print All Rooms / Overflow Guest Only** (تجاوز الحد!) · Include Special Room |
| 77 | **High Bills/Online Balance** | "closing balance has **exceeded the credit limit** set for that room" · **Cut Off Amount**: "This should be only in numbers **without any special characters**" — قاعدة إدخال صريحة |

## 2. الإيرادات والمصروفات النقدية (78–91)

| # | التقرير | الخصوصية |
|---|---|---|
| 78 | **Room Charges Report** | "room charges charged to all guests... based on the **revenue code selected**" |
| 79 | **Guest Telephone Bill** | "list of calls made by guests during their stay... **in detail without any consolidation** by giving the registration #" · Room# → Reg# + Month/Year آلياً → Guest Name/Arrival/Departure آلياً · **Include Taxes / Print Include Taxes** — جسر TEL الكامل |
| 80 | **Misc. Sales Register** | "same Month and Year" إلزامي · **Select one Rev Code أو All** (All = "all of the POS listed in the dropdown"!) · **Require Revenue Wise Day Total** |
| 81 | **Allowance Register** | "if the Guests request for any kind of **discount or waive off** from the total amount, then the user gives **allowance**" — تعريف Allowance الرسمي · **Date Wise / In-House** (مع In-House: Reg# والفترة معطلة!) · Revenue code |
| 82 | **Guest Paidouts** | "In case the Guest has **paid more advance than his final bill**, then the extra amount will be **reimbursed**" · "≤ accounting date" + same year+month · **Req. Date Summary** |
| 83 | **C L Paidouts** | "City Ledger Paidouts" + المثال: "reserved a room or a conference room... Due to some reasons the Guest **cancels** the reservation... advance... will be **reimbursed** to him through City Ledger" · Req. Date Summary |
| 84 | **Tips Statement** | "Tips (extra money given by the guest **as a token of satisfaction**)" — تعريف موسعي · "≤ accounting date" + "**date difference should not be greater than 31 days**" |
| 85 | **Bill Summary** | "exhaustive list of all printed room bills with **settled, cancelled or pending status**" · "< current date" + same month |
| 86 | **Settlement Summary** | "all settled and final bills" · **Print 132 / Pending Bills / Cancelled & Reprinted Bills** (checkboxes) · same month |
| 87 | **Foreign Exchange List** | "entries made through **Foreign Exchange Entry screen**" · فترة عبر الشهور · **User id dropdown** · **Show Only Deleted Records** (!) — تدقيق حذف |
| 88 | **Foreign Exchange Summary** | شهر/سنة "≤ current month and year" |
| 89 | **Cashier Report** | "**User Wise أو Shift Wise**" · مع Shift Wise: "Enter the **Start time of the shift and the End time**... (Time should be entered in **24 Hour format**)" · User dropdown (أو All) · **checkboxes لاختيار فئات القيود** — تقارير الورديات تدخل FO (توازي POS Shifts!) |
| 90 | **Cash/Paidouts Report** | "along with the **currency exchange amount and the local amount**" · All / **Cash only / Paid outs Only** · User id · Summary "at the end of the report" |
| 91 | **Entries Posted at FO** | "manual entries posted at the Front Office with respect to **charges, tariff, allowances**" · Revenue Code · **Include Guest Name** |

## 3. الفواتير والضرائب (92–98)

| # | التقرير | الخصوصية |
|---|---|---|
| 92 | **Reprint FO Bill** | Month/Year "≤ Current Month/Year" · Bill# (F1) · **Load** (يعرض كل أرقام الفواتير) · **Continue → Details (breakup) → Back → Print** — دورة عرض مزدوجة |
| 93/94 | **Tax Report / Consolidated Tax Register** | → `03-security-statutory-reports.md` |
| 95 | **Rate Variance Report** | "variance in the room rates as on the Accounting Date" · All / **In House / Checkout** · **Special Instruction** checkbox · **"Select the radio button First Name or Middle Name depending on how you want the guest name to appear"** — تقرير مالي يتحكم في تركيبة الاسم! |
| 96 | **CC Encashment Report** | صرف بطاقات الائتمان · same month |
| 97 | **RLM Report** | → ملف الأمن §2 (RBI) |
| 98 | **Bill-Wise Revenue Report** | "revenue wise breakup of net amount for each bill" · **Report #** (F1 — الاسم يُولد آلياً!) · **Settlement Details** checkbox |

## 4. دفتر الضيوف وتقرير الليل (99–106 + Guest Ledger Breakup)

| # | التقرير | الخصوصية |
|---|---|---|
| 99 | **Guest Ledger Balance** | "opening and closing balances of all in-house and checkout guests" + "nationality, PAX details, Meal Plan, **discounts offered on the bill amount**, summary of transactions and settlements" · "≤ accounting date" |
| 100 | **Res. Advance List (GLB)** | التقدمات وقت الحجز · **Checklist (يضيف: transaction date, mode of payment, currency) أو Breakups** · **أنماط الدفع المعرفة نظامياً: "ADQ – Advance Cheque · ADC – Advance Credit Card · ADV – Advance Cash · POT – Paid Outs"** |
| 101 | **Oneline GL Print** | "After the Guest Ledger balances are created..." · الأعمدة تُخصص مسبقاً في **Setup Guest Ledger Report** · "≤ accounting date" |
| 102 | **Night Report (Oprn)** | "sales and collections done on a specific date... also gives the **excess or shortage** amount arrived at by **tallying the debit and credit amounts**" · "Transactions for the day, for the month and for the year... **for all the outlets**" · **قاعدة XOR الحرفية: "In 80 Column option you can view transactions for the day and for the month, whereas in 132 Column option you can also view transactions for the year. If option 80 Column is selected, you get the option to select 'Year to Date', and if 132 Column is selected, then the 'Year to Date' option will be deactivated"** — عكس بديهي! |
| — | **Guest Ledger Breakup** (غير مرقم) | "displays **brought forward and carry forward** breakup" · Date → Print مباشرة |
| 103 | **Sales Summary by Outlet** | "sales and collection summary of all **revenue codes** defined (Example: Rooms and Food and Beverages)" · "print **only rooms or Food and Beverage outlets** with **month to date and year to date**" · "total debit and credit amounts" |
| 104 | **User Defined Report** | "daily, monthly and yearly financial figures... obtained from the sales and collection amounts taken from **Night Audit** and based on **user defined parameter specifications**" · Report# (F1) + Accounting Date · **Print Net Values: "If you select this option, then the other two options are deactivated"** (XOR ثانٍ) · 80 = يوم+شهر · 132 = يوم+شهر+سنة · "current year and **the previous year**" |
| 105 | **N/A Adjustment/Cons.** | "(Night Audit Adjustments and Consolidation Entry)" · **Consolidation (قيود التجميع الليلي) / Adjustment** — إخراج منفصل لتعديلات Night Audit |
| 106 | **FO Budget Report** | Report# (F1) + Accounting Date · **Currency code dropdown → "The exchange rate will be auto populated. To change the exchange rate, delete the existing rate and enter the new exchange rate"** (سعر صرف قابل للتحرير!) · **Inc. Last Year · In Thousands ("10,000") · 80/132** |

## 5. القرارات المعمارية المالية

1. **الصيغة الحرفية الأولى في طبقة التقارير** (75): رصيد الغرفة = رصيد افتتاحي سابق + تعرفة حالية + ضريبة فاخرة — تفتح باب اختبارات الوحدة (literal numeric test).
2. **عائلة Paidouts ثلاثية المصدر**: Guest Paidouts (82 — زيادة سلفة الضيف) · CL Paidouts (83 — إرجاع سلفة ملغاة عبر دفتر المدينة) · C L في عنوان vs City Ledger في المتن (اصطلاح موحد).
3. **Allowance = credit note فندقياً** (81): التعريف الحرفي يربطها بطلب الضيف عند التسوية — مقابل 31.3 Transfer Folio الذي يذكر "allowances (credit note)" — توثيق متقاطع كامل.
4. **تدقيق الحذف في FX** (87): "Show Only Deleted Records" — الحذف لا يمسح الأثر؛ سجل soft-delete موثق سلوكياً.
5. **قنوات الدفع كمعجم مغلق**: ADQ/ADC/ADV/POT (100) + Cash/CC/MD/Draft (توثيق CAS سابقاً) + Cash only/Credit only (58) — يُصهر في قاموس Payment Mode موحد.
6. **Budget بعملة وسعر قابلين للتحرير** (106): التقارير المالية تسمح بالتقييم بعملة معدلة يدوياً — سلوك reporting currency لا accounting currency.
7. **إغلاق الليل كنقطة ميلاد بيانات**: 104 يستقي من "amounts taken from **Night Audit**" و105 يعرض ما ولّده — Night Audit مصدر Truth للتقارير المالية اليومية (وليس الترحيل GL فقط).
