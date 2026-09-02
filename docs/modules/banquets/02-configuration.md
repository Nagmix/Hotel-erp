# 02 — الإعدادات والتخصيص (Configuration) — وحدة Banquets

> مفاتيح INI/Module Attributes الموثقة (3 INI جديدة + 6 POS MA مُشارَكة) + روابط المنفذ الثلاث + صلاحيات BNQ + مصمم الطباعة.

---

## 1. مفاتيح الإعداد الموثقة في BNQ

### 1.1 مفاتيح INI (ملف property.ini)

| المفتاح | الوظيفة | القيم | المصدر |
|---|---|---|---|
| **INI #346** | تعديل Pax في Requirement Entry | "The Pax entered in this menu option can be altered by modifying the INI # 346" — قيمة رقمية (سقف التعديل؟) [UNCERTAIN الدلالة الدقيقة للقيمة] | BIL §11 ص49 |
| **INI #408** | توحيد حالات Availability Chart | "display the **user defined** reservation status instead of default... by activating the INI Switch 408 **as 1**. By default, it will be set to **0**" (0=الحالات الافتراضية الأربع المدمجة) | LUK §2 ص7 |
| **INI #409** | بنى الضرائب في الحجز | "Tax structures will be displayed based on the definition in the **INI 409** switch" (بنى ضريبية متاحة للقاعة/السعر) | BOK Make ص11 |

### 1.2 مفاتيح POS Module Attributes (مُشارَكة مع BNQ — البنية الهجينة!)

| المفتاح | النص/الوظيفة | المصدر |
|---|---|---|
| POS MA 3 | تقييد إعادة التسوية النقدية | "If POS Module Attribute 3 is set to 'Yes', then the bills that have been settled by **cash or foreign currency cannot be resettled**" | BIL §4 ص31 |
| POS MA 8 | Swipe Card | "The Swipe Card field is activated based on **POS Module Attribute 8**... If 'Yes' → swipe or manual; If 'No' → manual only" | BIL §4 ص22 |
| POS MA 16 | Require Non Chargeable Settlement | "activated only if... number 16... is set to 'Yes'" | BIL §4 ص29 |
| POS MA 21 | Credit Limit check in AR Settlement | "The credit limit of a Company is displayed if... number 21... 'Yes'" | BIL §4 ص25 |
| POS MA 26 | Restrict Closure of Shift if pending Bills/KOTs | "If... 'Yes'... the cashier **must settle** all the pending bills/KOTs" | BIL §5 ص33 |
| POS MA 29 | Menu Master بنمطين | "Set the Module Attribute 29 as 'YES' to define **common menu items**... 'NO'... individually" — **نفس مفتاح POS-SET!** | CFG §8 ص22 |

> **الأثر المعماري:** BNQ تستدعي مفاتيح **POS** حرفياً ("POS Module Attribute") — دليل إضافي أن محرك الكاشير واحد. الجدول التراكمي للمشروع يصل **28+ مفتاحاً** (إضافة 408/409/346).

---

## 2. روابط المنفذ الثلاث (Link Outlet ×)

### 2.1 Link Outlet-Sessions
**المصدر:** SET §1. الحقول: Applicable From (≥ اليوم) + Outlet + Session (F1) + **Session Order** ("has to begin with one") + Start/End Time (**24 ساعة HH:MM**) + **Minimum Cover Charge** + **Applicable On** (الأيام). **مثال الدليل الكامل:** "For the Outlet Banquets, there will be 9 sessions: Breakfast 8-11 **$20**/person all days... Lunch 13-16 **$45**... Dinner 20-23 **$60**". **قاعدة التعديل:** "all the fields... for a **future date**. For... the **current date**, you can modify **only the status**".

### 2.2 Link Outlet-Order Types
**المصدر:** SET §2. ربط أنواع KOT بالمنافذ: Restaurant (النوع يُظهر تلقائياً) + KOT Type (F1) + Name (تلقائي) + **KOT Number Type: Auto Generation / Validate KOT book / Manual Entry**. **قاعدة:** "The **Standard KOT type is mandatory** for every restaurant" — لا يُبنى منفذ بلا KOT قياسي. نفس قاعدة تعديل المستقبلي/الحالي.

### 2.3 Link Outlet Currencies
**المصدر:** SET §3. **نسخة طبق الأصل من POS-SET §6:** "You must tag 'Yes' to **Multi-Currency** option under Setup Outlet for the Outlet to be displayed here" + Currency (F1) + **Round Off: Nearer/Higher/Lower/None** + Round Off Amount — "For Examples on Round Off options, refer **Property Codes in System Setup**" (إحالة متبادلة لمصدر الأمثلة الرقمية).

---

## 3. BNQ User Access (§20 — "POS User Access")

**المصدر:** SET §20 ص96-98.

- **النص الدقيق:** "The **POS User Access** option is used to provide/restrict user access rights for the users in the **Banquet** module. There are three options such as **KOT, Billing and Settlement**" — البرنامج المشترك مع POS.
- **By User / By Group** (Enter).
- **KOT: "There are 28 lists of operations displayed"** (updation/deletion/table transfer...) — نقر مزدوج → Yes + **لون أخضر**.
- **Settlement: "15 lists of operations"**.
- **الاستخدام الموثق:** إعادة التسوية ("The cashier must be given access using the POS User Access option to **resettle** a bill") + كل نمط تسوية ("access... for each type of Settlement mode") + Open/Close Shift/Outlet.

---

## 4. Print Forms (برامج الطباعة)

**المصدر:** SET §16 ص67-68.

- **Program IDs الموثقة:** `FP-NBIDSFP` (Function Prospectus) · `Voucher-NB001AD` · `BILL PRINTING-NB001BL` · `PROVISIONAL BILL-NB001PB`.
- **حقول الربط الفاتوري:** Function Prospectus code + **Tax Structure للـ Hall Charges** (F1) + **Group Code (Hall Charges)** + Receipt Printing code + **Tax Structure (Rate/Pax)** + **Group Code (Non F&B)** + Provisional/Invoice Bill + **Printer Name** (dropdown) — "this will be considered for **billing purposes**".
- **User Defined Print Forms (SET §17):** نفس مصمم POS الكامل (New/Open/Delete/Browse Project + Page Layout **"6 rows = 1 Inch"** + Header/Footer/Body + Match Samples + Toolbox + Scales + Grid + Lock controls + **F4 Properties** + F3 للأعمدة + Logo (Caption/Width/Height/Picture) + User Text + Make Project Active).

## 5. إعدادات تشغيل المنفذ (Billing 1-2/5-6)

| الإعداد | القاعدة الموثقة |
|---|---|
| Open Shift | "The **same person cannot operate 2 shifts** at a time" + حق الوصول من "Setup User Access under System Setup" |
| Open Outlets | "User must be **PO Cashier**... grouped as POCashier using the option **Create User** under System Setup" + "The **Server date and the accounting date should be the same**" + **Skipping Session** → تحذير (Continue/Cancel) + آخر جلسة اليوم وتبدّل التاريخ → "continue with the same accounting date... After the session is over, you can open the outlet for the next date" |
| Close Shift | **مصادقة بكلمة مرور** + ملخص معاملات الكاشير + MA 26 (تسوية المعلقات قبل الإغلاق) |
| Close Outlet | "prevent unauthorized users from closing" + للتاريخ المحاسبي الحالي + "If an outlet operates for only specific hours... must be closed at the end of the day. This process... will **record sales accurately**" |
