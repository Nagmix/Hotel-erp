# 09 — الاستعلامات (Lookups) — وحدة System Setup

> SYS بلا ملف LUK منفصل — استعلاماتها **مدمجة بشاشات الصيانة نفسها** (نمط F1 Browse الداخلي) + حقول مرجعية في وحدات أخرى تسحب من مرجعياتها.

---

## 1. نمط F1 Browse الموحد (كل Ch3)

كل شاشة Modify في General Setup تسير بالنمط ذاته:

```
Modify → نقر مزدوج/F1 → شاشة Help (قائمة القيم)
       → اختيار → Select → تعبئة الشاشة الأم → تعديل → Save
```

**الشاشات Help الموثقة (13+):**

| الاستعلام | المصدر |
|---|---|
| Property Codes Help | Fig20/ص60 |
| Departments Help | Fig23/ص64 |
| Cost Centers Help | Fig26/ص68 |
| Designation Help | Fig29/ص72 |
| UOM Help | Fig32/ص76 |
| Reason Code Help | Fig35/ص80 |
| Currency Help (للعملة) | Fig38/ص85 |
| Currency Help (لسعر الصرف — reuse!) | Fig41/ص89 |
| Tax Code Help | Fig43/ص92 |
| Tax Slab Help | Fig46/ص98 |
| Guest Comments Definition | Fig49/ص104 |
| Setup Credit Cards Help | Fig57/ص114 |
| Billing Broadcast Help | Fig60/ص118 |
| Religion Definition Help | Fig63/ص121 |
| Occupation Definition Help | Fig65/ص124 |
| Group Nationality Help | ص108-109 |
| Modify User (قائمة المستخدمين) | ص11-12 |

**النمط العام:** "Double-click or press F1 from your keyboard" — حقل مرجعي = استدعاء قائمة اختيار.

## 2. الحقول المرجعية في وحدات أخرى تسحب من SYS (خريطة الاستهلاك)

| مرجع SYS | يُستهلك في | الموثق |
|---|---|---|
| Property Codes | FO Defaults + INI generation precondition | ص26/ص37 |
| Departments | FO (قوائم الأقسام) + POS + كل الوحدات عدا Banquet (فلتر!) | ص47-49 |
| Cost Centers | POS Outlets + كل الوحدات | POS-SET §1 |
| Designations | Create User + Guest cards (Guest) + HR&P (Others) + S&M | ص9/ص54 |
| UOM | POS (الأصناف) + MM + F&B Costing | ص57 |
| Reason Codes | 9 وحدات (عمليات الإلغاء/الخصم/الإعفاء الضريبي) | ص61 |
| Currencies | FO + POS (Link Outlet Currencies) + AR (أسعار الفواتير) + Exchange | كل الوحدات |
| Exchange Rates | تسويات Forex + AR bill-date pinning | ACR-OPR §1 |
| Tax Codes/Slabs/Structures | FO/POS/BQT/Purchase/Laundry/Restaurant/RoomService | ص72/76/81 |
| Guest Comments | Guest Survey Template (FO+POS) | ص83 |
| Credit Cards | تسويات FO/POS/BQT + Authorizations | ص93 |
| Religions/Occupations | HR Master + Guest History / Guest+Staff | ص99/103 |

## 3. معايير تصميم الاستعلام للواجهة الجديدة

1. **اختصار F1 = نمط Search-Select عالمي** — يترجم إلى Combobox مع بحث (shadcn Command).
2. قوائم Help تعرض **Code + Name + Short Name** (الثلاثة هي مفاتيح العرض في "reports and lookups" — عبارات متكررة).
3. Passive لا يظهر في قوائم الاختيار افتراضياً (يظهر بـ Show All في Parameter List فقط) — [INFERENCE] من سلوك Status العام.
