# 14 — نموذج البيانات (Data Model) — وحدة POS

> 30 كياناً موثقاً + العلاقات + القيود. الحقول من جداول الأدلة النصية.

---

## 1. عائلة المنفذ

| الكيان | الحقول الجوهرية | المصدر |
|---|---|---|
| **Outlet** | code(≤3 alnum) · name(30)/short(10) · outlet_type · **linkage (FO/Fin/both)** · tax_currency · **round_off(None/Nearer/Higher/Lower)** · department_id · cost_center_id · kot_form_id · bill_form_id · bill_printer · settlement_printer · tax_structure · **all_inclusive** · multi_currency · **bill_init_type(Y/M/D/N)** + init_date(DDMM) · fnb_flag · copies · delivery_active · token_printer · order_entry_flags(5) · applicable_from · status | POS-SET §1 |
| **OutletSession** | code(≤2) · name/short + applicable_from | §2 |
| **OutletSessionLink** | outlet × session · **order (يبدأ 1)** · start/end(HH:MM 24h) · **min_cover_charge** · applicable_days | §4 |
| **KOTType** | kot_type(numeric ≤2) · name/short | §3 |
| **OutletKOTTypeLink** | outlet × kot_type · **kot_no_type(Auto/ValidateBook/Manual)** — Standard إلزامي | §5 |
| **OutletCurrencyLink** | outlet × currency · round_off · round_off_amount | §6 |
| **NCDepartment** | code(≤3) · name/short · applicable_from | §7 |
| **Area** | area(40) · zip(30) · city(30) · distance · travel_time | §21(2) |

## 2. عائلة القوائم

| الكيان | الحقول | المصدر |
|---|---|---|
| **MenuItem** | item_code(numeric ≤4) · name/short · menu_group_id · menu_type · classification(TS group) · cost_pct · **outlets[]** (Common) أو outlet (Per) · **available_hours** · sub_store_code · preparation_time · kitchen_id · kot_printer · tax_structure_id · default_bill · print_order · nc_flag · discount_flag · **gl_code** · level1/2/3 · uom · quantity · **rates: local + foreign[]** · remarks | §24 |
| **MenuGroup** | code(≤3 numeric) · name/short | §8 |
| **TouchScreenGroup** | code(≤2 numeric) · name/short | §14 |
| **MenuLevel** | outlet × major_classification · sub_code(≤2) · name | §11 |
| **Modifier** | restaurant × item_code · modifier_id(≤2) · name(40) · **recipe** · additional_charge | §26 |
| **TSModifier** | modifier_id(≤4) · name(20) · additional_charge | §27 |
| **ModifierGroup** | group_code(≤3) · name(30) · modifiers[] | §27 |
| **ItemHotKey** | restaurant · **ctrl_key × fn_key** · item_code · quantity | §13 |
| **ItemLink/ModifierGroup** | restaurant × item × groups[] | §27 |

## 3. عائلة التسويق

| الكيان | الحقول | المصدر |
|---|---|---|
| **HappyHour** | outlet · from/to date · from/to time · scope(Item/MnGrp) · item_or_group · type(**P/A**) · rates(all أو لكل يوم أسبوع) · status | §31 |
| **SalesPromotion** | code(≤4) · name(40) · covers · value · calc_type(Min/Max/Avg/None) · tax_structure · group · **items[main/additional/complimentary]** (Main ≥1) · qty · available_days | §32 |
| **MemberDiscount** | **member_id (+srl)** × **outlet** × **menu_type(5+All)** = pct · INI 404 يحدد النطاق | §41 |
| **OpenItemDef** | menu_type · nc_cost_pct · discount_allowed · default_bill · **kitchens[]×printers (إلزامي)** | §19 |

## 4. عائلة التشغيل

| الكيان | الحقول | المصدر |
|---|---|---|
| **Server** | code(≤3) · name/short · **employee_no(≤6)** | §9 |
| **ServerOutletMapping** | server × outlet | §10 |
| **RestaurantTable** | restaurant · **table_no(≤5 alnum)** · max_covers(≤3) · location_view(30) | §12 |
| **TableLayout/Floor** | outlet × floor · objects(tables/flowers/labels/lines/texts) · **copy بلا أسماء** | §39 |
| **Kitchen** | code(≤3) · name/short · **network_printer (Attr 32)** | §15 |
| **KOTBook** | restaurant · kot_type · **start/end (≤100)** · issued_to | §30 |
| **DSRSessionGroup** | record#(≤3) · description(20) · sessions[] | §36 |
| **SalesReportDef** | outlet · column# · desc · **column_type(7: A/C Group/Taxes/RoundOff/Discount/Total/Settlements/Tips)** | §16 |
| **BillPrinter** | outlet × printers[] | §34 |
| **CentralKOT** | outlet → printer | §33 |

## 5. عائلة المعاملات

| الكيان | الحقول | المصدر |
|---|---|---|
| **Shift** | cashier · outlet · shift · open/close (**بلا معلقات للإغلاق**) | TS |
| **OutletDay** | outlet · **accounting_date (= Bill Date)** · session (قابلة للتغيير) | TS |
| **KOT** | kot_no (Auto/Book/Manual) · outlet · table · steward · session · items[] (item/qty/modifiers) · status (Pending/Revised Old→New/NC) | TS + LUK |
| **Check (Bill)** | bill_no (**دورة Y/M/D/N**) · outlet · table · kot_refs · bill_amount · discount · taxes · **net** · status (NotPrinted/Printed/Settled/Pending/Cancelled/Provisional) · splits[] | TS |
| **Settlement** | check · mode(6) · amount · **balance(=0 إلزام)** · tips · cc_details(swipe) · cheque_details · coupon_no · **room#/guest (FO)** · reason(void) | TS |
| **NCRecord** | kot_type · **department** · guest_name · bill · tips | TS |

## 6. عائلة الضيوف (POS-GST)

| الكيان | الحقول | المصدر |
|---|---|---|
| **POSGuest** | **guest_code آلي** · (outlet-scoped) · name/address/city/state/country/zip/tel/email · designation/nationality/guest_status/classification · gender · special_instruction · nights · **black_listed** · company_code (FO!) · secretary | GST §1 |
| **Passport** | passport# · issue_date/place · valid_until | GST §1 |
| **Personal** | dob · anniversary · smoker · occupation · frequent_flyer · loyalty · cc_type+no · spouse{...} · children[{name,dob,gender}] · privilege_card{type(FO), number} | GST §1 |
| **VisitDetail** | date/time · restaurant · session · amount · settlement_mode · cc# · **breakup[{item,qty}]** | GST §1 |
| **LikeDislike / Comment / Complaint** | type/val · complaint{department, nature, date/time} | GST §1 |
| **LoyaltyCardType** | code(≤3) · description | GST §2 |
| **LoyaltyCard** | type · **card#(≤15 alnum)** · join/expiry · guest · display_text · discounts[outlet×menu_type×covers] · status | GST §3 |
| **GuestComment** | outlet · date/time · guest · table · server · captain · ratings{} · remarks | GST §10 |
| **SurveyTemplate** | outlet · line# · description(60) · comments_defined[] | POS-SET §38 |

## 7. العلاقات (ERB)

```
Outlet 1─N OutletSessionLink N─1 OutletSession
Outlet 1─N OutletKOTTypeLink N─1 KOTType (Standard إلزامي)
Outlet 1─N OutletCurrencyLink N─1 Currency (بشرط multi_currency)
Outlet 1─N MenuItem (أو N─M في Common)
Outlet 1─1 Department/CostCenter/TaxStructure (SYS)
Kitchen 1─N MenuItem ("Every item must be tagged to the kitchen")
MenuItem 1─N Modifier / 1─N ItemHotKey / N─N ModifierGroup (TS)
RestaurantTable N─1 Outlet — Layout N─1 Floor N─1 Outlet
Server N─M Outlet (Mapping) — Server 1─N KOT (steward)
KOTBook N─1 KOTType — KOT N─1 KOTBook (Validate)
Shift N─1 Server(cashier) · OutletDay N─1 Outlet · KOT N─1 OutletDay+Table+Server
Check N─N KOT — Settlement N─1 Check — Settlement N─1 FO-Guest(Room) / AR-Company
POSGuest 1─N VisitDetail 1─N VisitBreakupItem
POSGuest N─1 FO-Company (company_code) — LoyaltyCard N─1 POSGuest/LoyaltyCardType
MemberDiscount N─1 Membership-Member × N─1 Outlet
HappyHour/SalesPromotion N─1 Outlet × N─1 Item/MenuGroup
```

## 8. قيود التصميم (Design Constraints)

| # | القيد | الأساس |
|---|---|---|
| C-POS-1 | **Settlement.balance = 0** قيد حفظ | TS ص33 |
| C-POS-2 | **bill_no دورة Y/M/D/N** لكل منفذ | POS-SET §1 |
| C-POS-3 | **Reprint قبل التسوية ⇒ bill_no جديد** (إبطال القديم) | TS ص41 |
| C-POS-4 | **kot_no (Auto/Book/Manual)** + كتاب ≤100 | POS-SET §5/§30 |
| C-POS-5 | كل Master **إصداري** (applicable_from + status) وسجل اليوم = status فقط | POS-SET |
| C-POS-6 | **Standard KOT إلزامي** لكل مطعم | POS-SET §5 |
| C-POS-7 | Settlement.mode ∈ {Cash,CC,Cheque,Coupon,Guest,Void} والنقد متاح دوماً | TS + §17 |
| C-POS-8 | Table#+suffix ≤6 خانات؛ qty المقسومة < الأصلية | TS |
| C-POS-9 | **Close Shift/Outlet ممنوع مع KOTs/Bills معلقة** | TS ص46 |
| C-POS-10 | **MenuItem ↔ Kitchen إلزامي** ("Every item must be tagged") | POS-SET §15 |
