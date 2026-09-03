# 03 — تقارير التسوية والتحصيل (§2/3/4 + §5.1–5.6)

> عائلة أموال المنافذ: تسويات الفواتير (§2-4) وتقارير الكاشير والوردية (§5) + العملة الأجنبية والبقشيش.

---

## 1. التسويات الثلاثة (§2/§3/§4)

### 1.1 Settlement by Bill # (§2) — التسوية الفاتورة-بالفاتورة

| البند | القيمة |
|---|---|
| المدخل | Date واحدة (≤ Accounting) · Outlets · Session · **Cancelled Bills Only** checkbox |
| المخرجات | bill# · table/room# · net · mode · amount · **paid out** · **tip** · **description** · **User name** |
| اللافت | الفواتير الملغاة تعرض **"the new bill numbers of the bills that were cancelled"** + "the user name who has worked on the cancelled bills" — **رابط الاستبدال (rebill linkage) + أثر المستخدم** |
| الملخص | "total sales in amount by each settlement mode, **including the paid out amount if any**" |

**الدلالة:** الفاتورة الملغاة ليست نهاية القصة — التقرير يربطها بفاتورتها البديلة (شاهد نظام Cancel-and-Rebill داخل POS).

### 1.2 Settlements by Date (§3) — المجموع اليومي

- نطاق تاريخ (**< Accounting Date حرفياً** — الاستبعاد الصارم الوحيد) + منفذ + Page skip.
- الأنماط المذكورة حرفياً: "Cash, Credit, Cheque, Staff, Company etc" — **Staff** نمط تسوية قائمة (موظف!) يظهر هنا فقط في العائلة.
- لكل تاريخ: إجماليات التحصيل لكل نمط + إجمالي مبلغ الفواتير لكل منفذ وكل المنافذ.

### 1.3 Settlements by Mode (§4) — التفصيل النمطي

- **Summary XOR Details** — في وضع Details تظهر **تفاصيل KOT أيضاً** (KOT# · وصف الأصناف · كمية · قيمة).
- لكل فاتورة: bill# · session · covers · table# · bill amount · settlement amount · tips · **Remarks** · **"user name who has settled the bill"**.
- القاعدة الذهبية للوضعين: Summary = رؤوس الفواتير فقط · Details = رؤوس + بنود KOT.

## 2. تقارير التحصيل الستة (§5)

### 2.1 Collection Summary (§5.1)

- **Bill Date XOR Shift Date** (اختيار مرجع الزمن) + Grouping: **Outlet XOR Cashier** + Print Consolidated + Void/Comp.
- المخرجات: "The **users responsible for the collections** under each outlet" + Net + Tips + تحصيل cash/card/company/room/**void** — انتبه: void هنا نمط تحصيل معروض!

### 2.2 Cashier Summary (§5.2) — بوابة الورديات المغلقة

> **"Note: You can generate reports only for Closed Shifts."**

- المدخل: Shift Date (عبر **Shift Help** بـF1) → Cashier dropdown → Shift dropdown.
- المخرجات: bill# · net · mode · **exchange difference amount** · paidout · tip + إجمالي.
- **الدلالة المعمارية**: التقارير مقفلة على الورديات المغلقة = **تقرير Z-Report بشرط إغلاق** — دورة حياة الوردية (Open→Close→Report) لها بوابة في طبقة التقارير (بازل "تقارير ما بعد القفل" في FO Night Audit).

### 2.3 Cashier Summary (Group) (§5.3)

- **By Group XOR By Bill** + Port ID + 4 مفاتيح طباعة: **Print Sales / Print Settlement / Print Tax / Print Paidouts** — أغنى تقرير تحكم بمحتوى الطباعة (عائلة checkbox الطباعة التدريجية).
- يعرض: نوع الضرائب + "amounts **rounded off** to" + covers + tips + تحصيل كل نمط.

### 2.4 Cashier Report (By Type) (§5.4)

- الغرض المعلن: "to know **which type of menu is in demand** and generating good revenue".
- **Shift information: open and close time of shift** + **Starting and ending bill numbers and the total number of bills** — **نطاق أرقام الفواتير للوردية** (Bill sequence audit!) — أقوى شاهد على أن الفواتير تُرقم داخل الوردية تسلسلياً.

### 2.5 Foreign Exchange Statement (§5.5)

- عملة واحدة (Currency Help) + نطاق ≤ Accounting.
- لكل فاتورة: **exchange rate** · net · paidout · tips + "total collections **by the end of the day** from the currency" — كشف نهاية يوم **لكل عملة على حدة** (بازل FO Foreign Exchange لأرصدة الصرافة).

### 2.6 Tips Statement (§5.6)

- نطاق (≤ Current + نفس الشهر) + Session + **Server Summary** checkbox.
- لكل بقشيش: bill date · bill# · net · session · **server** · tip amount · **"mode of receiving the Tip (cash/credit/guest etc)"** · remarks — البقشيش بعملة تسوية (وضع استلام!) وليس مبلغاً ساذجاً.

## 3. الأنماط العابرة في العائلة

| النمط | الشاهد | التقارير |
|---|---|---|
| **أثر المستخدم** (Settler/Cashier/User) | "user name who has settled the bill" · "users responsible for the collections" · "User who has generated the KOT" (1.15) | 2 · 4 · 5.1 · 1.15 |
| **مرجعا زمن مزدوجان** | Bill Date XOR Shift Date | 5.1 · 1.9 (Accounting XOR Shift) |
| **Paid Out كمواطن درجة أولى** | عمود مستقل في 2 · 1.3 · 5.2 + Print Paidouts في 5.3 | 4 تقارير |
| **Exchange difference** | حقل مستقل في 5.2 | Cashier Summary |
| **بوابة إغلاق الوردية** | Closed Shifts only | 5.2 (وحدها — 5.4 تعرض أوقات الافتتاح/الإغلاق لكن لا تشترط الإغلاق!) |

## 4. معجم أنماط التسوية كما تجلى في REP

| النمط | المواضع | ملاحظة |
|---|---|---|
| Cash | في كل مكان | المرجع الدائم |
| Credit Card | 1.9 · 3 · 5.1 | |
| Room | 1.9 · 5.1 | جسر FO (نقل للفوليو) |
| Company | 1.9 · 3 · 5.1 | جسر AR/City Ledger |
| Cheque | 3 | |
| **Staff** | 3 | نمط موظف — يظهر صراحة هنا فقط |
| City Ledger | 16.4 (تعريف حرفي) | "bills of the Guest are debited to his Company" |
| **others** | 1.9 | "all other settlement modes other than cash, credit card, room and company" — **سلة مفتوحة** |
| Void / Complimentary / NC | كل العائلة | ظهور بلا احتساب (Invariant المصفوفة) |

> القائمة الكاملة للماستر: مذكورة في POS-SET/GST (راجع `modules/point-of-sale/`) — REP يضيف "Staff" و"others" كأدلة استعمال.

## 5. ملاحظات تحويل سريعة

- 5.2 → **POS Closing (Z-Report)** في ERPNext: تقرير مغلق على Shift مغلق + نطاق أرقام الفواتير (5.4) = تدقيق تسلسل فوري.
- 5.5 → كشف عملة: Exchange Rate من سجل الفاتورة + تجميع عملة.
- 2 (cancelled) → علاقة amended-of بين الفواتير الملغاة والبديلة (Versioning) — لا حقل حرفي موثق في REP لكن السلوك يفرضه.
