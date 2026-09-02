# 10 — المعاملات ودورات الحياة (Transactions) — وحدة POS

> كتالوج مستندات POS وحالاتها — **سلسلة اليوم الكاملة** (Shift→Outlet→KOT→Check→Settlement→Close) هي جوهر الوحدة.

---

## 1. سلسلة مستندات الوحدة

| المستند | المولِّد | الترقيم | المصدر |
|---|---|---|---|
| **Shift** | Open Shift (لكل كاشير) | معرف الكاشير | TS ص4 |
| **Outlet Day** | Open Outlet (شخص واحد) | Accounting Date (= Bill Date) | TS ص5 |
| **KOT** | Order Entry (زر Order) | حسب KOT # Type: **Auto / Validate Book / Manual** | POS-SET §5 + TS |
| **KOT Book** | Issue KOT Book | Start–End (**≤100**) | POS-SET §30 |
| **NC KOT** | NC Details (Type + Department + Guest) | كـ KOT | TS ص37-39 |
| **Check (Bill)** | Check Printing → Print Bill | بدورة Bill Init (Yearly/Monthly/Daily/None) | TS + POS-SET §1 |
| **Provisional Check** | Provisional/Dummy Bill | **رقم صفر** | TS ص24 |
| **Split Check** | Split Equal/Item/Quantity | فواتير مشتقة | TS ص28-31 |
| **Settlement** | Settle (بعد Balance=0) | — | TS ص32-36 |
| **Resettlement** | إعادة تسوية فاتورة مسوّاة | — | TS ص36 |
| **Void Bill / Void KOT** | Void (بأسباب) / Void KOTs (Billing) | — | TS + POS-SET §37 |
| **Guest Visit Record** | Post Guest History | — | POS-GST §4 |
| **Loyalty Card** | Setup Loyalty Master | **Card# ≤15 alphanum يدوي** | POS-GST §3 |
| **Guest Comment** | Guest Comments Entry | Line# + Date/Time | POS-GST §10 |

## 2. دورة حياة اليوم التشغيلية (State Machine)

```
[LOGIN: DB+Userid]
   └─> SHIFT-OPEN (كاشير × مطعم × وردية)            ← Password + إغلاق سابقة للتغيير
        └─> OUTLET-OPEN (واحد، Accounting Date)      ← Session قابلة للتغيير بإعادة فتح
             └─> TABLE-OPEN (Steward + Table + Covers)
                  └─> KOT (طباعة للمطابخ)
                       ├─> (تعديل/إلغاء: Reason + KOT جديد)
                       └─> CHECK (Print Bill | Provisional)
                            ├─> REPRINT قبل التسوية ⇒ إبطال رقم + رقم جديد
                            ├─> SPLIT (3 أنماط) / LINK (دمج) / SUFFIX (مؤقتة)
                            └─> SETTLEMENT (Balance=0; 6 أنماط; Tips CC/شيك/Guest)
                                 ├─> RESettLEMENT (باستفتاء)
                                 └─> [CLOSE-SHIFT (لا معلقات) → CLOSE-OUTLET (لا معلقات)]
```

## 3. حالات المستندات الموثقة

### KOT
| الحالة | الدلالة | المصدر |
|---|---|---|
| Pending | **KOT بلا فاتورة** (يظهر في Pending KOTs ويحجب الإغلاق) | LUK §1 + TS ص46 |
| Revised | **KOT Audit: Old→New** | LUK §6 |
| NC | نوع خاص (Department + Guest) | TS ص37 |

### Check (الفاتورة)
| الحالة | الدلالة | المصدر |
|---|---|---|
| Not Printed | طاولة بلا أيقونة طابعة | TS ص41 |
| **Printed-Not-Settled** | أيقونة الطابعة — **Reprint يُبطله ويرقِّم من جديد** | TS ص41 |
| **Settled** | معروضة في التسوية ("Settled") | TS ص33 |
| **Pending** | معروضة ("Pending") — تحجب الإغلاق | TS ص33/46 |
| **Cancelled (Void)** | معروضة ("Cancelled") | TS ص33 |
| Provisional | رقم صفر | TS ص24 |

### Settlement
| الحالة | الدلالة | المصدر |
|---|---|---|
| Pending | Balance ≠ 0 — غير محفوظة | TS ص33 |
| Settled | Balance = 0 محفوظة | TS ص33 |
| **Re-settled** | بعد الاستفتاء — بوضع آخر | TS ص36 |

### Table
| الحالة | اللون | المصدر |
|---|---|---|
| Vacant | أخضر (G) | POS-SET §39 |
| Occupied | أحمر (R) — + أيقونة Waiter في TS | §39 + TS ص16 |
| Billed | أزرق (B) | §39 |
| Reserved | بني (Y) | §39 |

### Shift/Outlet
| الحالة | الشرط | المصدر |
|---|---|---|
| Open | Open Shift/Outlet | TS ص4-5 |
| Closed | Close (Password/تأكيد) — **ممنوع مع معلقات** | TS ص46 |

## 4. الأحداث المؤتمتة الموثقة

| الحدث | المشغّل | المصدر |
|---|---|---|
| **Print Bill ⇒ تسوية نقدية تلقائية** | زر Print Bill | TS ص24 |
| **Reprint ⇒ رقم جديد** | إعادة طباعة قبل التسوية | TS ص41 |
| عرض Total/Taxes/Net | أثناء Order Entry | TS ص15 |
| **Capture CC تلقائي بالسحب** | حقل Swipe Card | TS ص34 |
| **Discountable Amount آلي** | شاشة Discount | TS ص25 |
| **Item Type + Tax آليان للـ Open Item** | اختيار Group | TS ص21 |
| **Modifiers تظهر تلقائياً** عند الصنف المعرف | اختيار الصنف | TS ص19 |
| Chasers/الكميات الملونة | التحديث الفوري | TS |
| ربط الطاولات يعرض الكل عند اختيار أي واحدة | Link Tables | TS ص44 |
| Accounting Date آلي | Open Outlet | TS ص5 |
| Code الضيف آلي | Guest Master | POS-GST §1 |

## 5. دورات حياة التكوين (Masters الإصدارية)

```
MASTER (Applicable From ≥ اليوم)
  ├─ FUTURE: كامل الحقول قابل للتعديل
  └─ TODAY: Status فقط
       └─ التعديل ⇒ NEW RECORD (تاريخ > تاريخ المحاسبة)
```

**استثناءات موثقة على النمط:**
| Master | قاعدة تعديل خاصة | المصدر |
|---|---|---|
| Menu Level | Name + Status فقط (أي تاريخ!) | §11 ص37 |
| Restaurant Table | Covers + Location View فقط | §12 ص39 |
| Item Hot Keys | Status فقط (لا مفاتيح) | §13 ص41 |
| KOT Book | اسم المستلم فقط | §30 ص95 |
| DSR Session Group | Description + Sessions فقط | §36 ص108 |
| Guest Survey | الكل عدا Outlet وLine # | §38 ص111 |
| Happy Hours | From Date ≤ اليوم معطّل؛ جارٍ اليوم ⇒ سجل من الغد؛ **Passive لا يعود Active** | §31 ص98 |
| TS Modifiers (الربط) | اختيار/إلغاء المجموعات فقط | §27 ص88 |
