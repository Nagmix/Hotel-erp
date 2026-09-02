# 12 — التكاملات (Integrations) — وحدة Banquets

> I-BQ-01..14 — **أكثافة تكاملية قصوى**: تستهلك FO/SYS/POS وتغذي AR/MGT/FAS/FNB.

---

## 1. مصفوفة التكامل

| # | التكامل | الاتجاه | النص الموثق | المصدر |
|---|---|---|---|---|
| I-BQ-01 | **FO Defaults → BNQ** | استهلاك | "Market Segment and Business Source... displayed by default as defined in the **SET UP FO defaults**" + Pay Mode كذلك | BOK ص8-9 |
| I-BQ-02 | **FO Guest → Guest Settlement** | قراءة لحظية | Room# → "Guest Name, Meal Plan, Pax, Birthday, Anniversary and Guest status" | BIL §4 ص25 |
| I-BQ-03 | **FO (طباعة) ↔ Resettlement** | تحقق | "only if it has **not been originally printed at Front Office**" | BIL §4 |
| I-BQ-04 | **BNQ → AR (Credit Card)** | ترحيل ذمم | "sent to the Accounts Receivable module for further processing" | BIL §4 |
| I-BQ-05 | **BNQ → AR (Company)** | ترحيل outstanding | + Available Credit (MA 21) + **Blacklist message بالاسم والسبب** | BIL §4 |
| I-BQ-06 | **BNQ → AR (Staff)** | ترحيل | "saved in the Accounts Receivables module" | BIL §4 |
| I-BQ-07 | **BNQ → FO Folio (Guest)** | ترحيل غرفة | قناة الائتمان الفندقية الموحدة | BIL §4 |
| I-BQ-08 | **BNQ → MGT (Auto Indent)** ⭐ | **طلب مخزني آلي** | Work Sheet → Department/CC → recipes → indent | BIL §§12-13 |
| I-BQ-09 | **FNB Recipes → Pre Costing** | استهلاك وصفات | "ingredient details will be obtained from the **recipe**" | BIL §12 |
| I-BQ-10 | **MGT Inventory Items → Pre Costing** | استهلاك مخزون | "inventory items can be linked manually... should be tagged" | BIL §12 |
| I-BQ-11 | **SYS Create User → BNQ** | مستخدمون | Banquet Staff + **PO Cashier grouping** | CFG §11 + BIL §2 |
| I-BQ-12 | **SYS Currencies/Round Off → BNQ** | استهلاك | Link Outlet Currencies (Multi-Currency tag) — "refer **Property Codes in System Setup**" | SET §3 |
| I-BQ-13 | **POS Engine (مشاركة كاملة)** | بنية هجينة | Shift/Outlet/Session + أنماط التسوية + **POS Module Attributes 3/8/16/21/26/29** + **POS User Access** | BIL كامل + SET §20 + CFG §8 |
| I-BQ-14 | **BNQ → FAS** | ترحيل | رابط الستة الموثقة (FAS-SET) | FAS |

## 2. سلاسل التكامل المكتملة

### 2.1 سلسلة حدث كاملة (Booking → Cash)

```
FO Defaults ──► Make Booking (سوق/مصدر/دفع) ──► Requirement Entry ──► Pre Costing (FNB recipes + MGT items)
                                                        │
                    Deposit (Cash/Card/Cheque) ──► Refund/Retention ──► Banquet Bill (splits + tax)
                                                        │
                                                        ▼
                                     Settlement (11) ──┬─► AR (CC/Company/Staff)
                                                        ├─► FO Folio (Guest)
                                                        └─► FAS (BNQ→Finance link)
```

### 2.2 سلسلة Auto Indent (UNK-011 Resolved)

```
Requirement Entry (أصناف F&B/Non F&B/Open) ──► Pre Costing Chef Eng
        (Recipe ingredients أو Inventory Items يدوية) ──► Auto Indent
        (Work Sheet# + Department + Cost Center + recipes by dept) ──► MGT Indent
```

## 3. حدود التكامل [NOT DOCUMENTED]

| السؤال | الحالة |
|---|---|
| توقيت BNQ→FAS | UNK-027 (مشترك مع MGT) |
| هل Event Template (feedback) يتكامل مع Care/MEM؟ | لا إشارة — [NOT DOCUMENTED] |
| Corporate Rate ↔ SLM Contracts? | التسمية مشتركة لكن لا جسر موثق — يفحص عند SLM |
| الربط مع POS Guest Master (UNK-001)؟ | Guest Settlement يقرأ FO فقط — بلا POS Guest هنا |
