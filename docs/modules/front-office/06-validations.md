# 06 — قواعد التحقق (Validations) — وحدة Front Office

> التحققات الموثقة نصاً في المصادر، مصنفة حسب نقطة الفرض.

---

## V-FO-01: تحقق الإدخال (Field-level)

| التحقق | النوع | المصدر |
|---|---|---|
| Extension Password يقبل **قيم رقمية فقط** | format | FOM-REG ص101 |
| Day Charge عند ترحيل التعرفة: 1 أو 0.5 فقط | domain | FOM-CAS ص21 |
| مجموع غرف التفاصيل = حقل Rooms | consistency | FOM-RES ص6 |
| صيغة إدخال التواريخ: Enter (افتراضي) / رقم+Enter (N أيام) / F1 (تقويم) / يدوي (dd/mm/yy) | input format | FOM-RES ص4 |
| Nights تُحسب آلياً من Arrival/Departure | derived | FOM-RES ص4 |
| صيغة وقت المغادرة: 12 Noon أو 24 Hour | enum | FOM-REG ص22 |
| From/To لـ Bill Allowance ضمن مدى Arrival↔Departure | range | FOM-CAS ص26 + ص29 |
| Settlements: التحقق من **التطابق (tally)** قبل الحفظ — رسالة رفض عند عدم التطابق | business | FOM-CAS ص77-78 |
| وسيوم OOO: From/To **غير قابلين للتحرير** | readonly | FOM-RES ص54-55 |
| كشف أسماء Guest History المتشابهة قبل حفظ الحجز | dedup | FOM-RES ص8 |
| كشف ازدواج الحجز (Duplicate reservation) | dedup | FOM-RES ص8 |

## V-FO-02: تحقق حالة الغرفة

| التحقق | السلوك | المصدر |
|---|---|---|
| Check-in على غرفة OOO | **ممنوع** — تُعرض في Walk-ins خصيصاً لمنعها | FOM-REG ص17 |
| تخصيص غرفة معلمة صيانة | تنبيه Alert للمستخدم | FOM-REG ص33 |
| Room Transfer | يتطلب **غرفة vacant** | FOM-RES ص59 |
| النقل/التبديل/Check-in | التاريخ المحاسبي فقط | FOM-RES ص58 + ص60 |
| Split Folios | يتطلب **Pax > 1** | FOM-CAS ص57 |
| Close Room Inventory | حرف C يمنع الحجز — walk-ins مستثناة | FOM-RES ص68 |

## V-FO-03: تحقق التفويض (Authorization)

| العملية | المطلوب | المصدر |
|---|---|---|
| Room Transfer / Swap | نافذة تفويض: Remarks + اسم المصرِّح | FOM-REG ص50-52 |
| Cancel Check-In | سبب + تفويض (Reason Entry) | FOM-REG ص93-94 |
| Cancel Reservation | سبب (قائمة/جديد) + معتمد + بيانات المتصل | FOM-RES §1.3 |
| Transfer Folios | Remarks + Authorized Person | FOM-CAS ص61 |
| Pax Transfer | Authorized By + Ok | FOM-CAS ص93-95 |
| خصومات Bill/Consolidated Allowance | Reason + Remarks + Authorized By | FOM-CAS ص28 + ص33 |
| خصم تعرفة Change Guest Info | Reason + Authorized By + Remarks | FOM-REG ص46 |
| Create Hotel Chart | username/password صالحان | FOM-REG ص97-98 |
| Foreign Exchange / Credit Card Encashment | Authorized By | FOM-CAS §17-18 |

## V-FO-04: تحقق التكرار والتسلسل

| التحقق | المصدر |
|---|---|
| Fixed Charge Posting: منع تكرار نفس (revenue, guest) في نفس اليوم المحاسبي | FOM-CAS ص46 |
| Room Rate: تنفيذ متكرر يسجل الأخير فقط (تحذير سلوكي) | FOM-CAS ص22 |
| Deposits عند إلغاء حجز: إجبار المرور بنافذة Deposit/Refund | FOM-RES §1.3 |
| Re-Instate Linked/Sub Room: يجب إعادة فتح **Main Room أولاً** | FOM-CAS ص82 |
| Billing Broadcast: تعديل الرسائل **المستقبلية فقط** | FOM-REG ص99-100 |
| Group Rate Updation → Change Plan: خيار All يطبق على المجموعة كلها | FOM-REG ص88 |

## V-FO-05: تحقق الحفظ والحالة

| التحقق | المصدر |
|---|---|
| Inquire Reservation: وضع قراءة فقط (تعطيل الحفظ) | FOM-RES ص41 |
| Post Room Rate (All Rooms): تأكيد Continue/Abort قبل الترحيل الجماعي | FOM-CAS ص22 |
| Checkout: تأكيد الرسائل النصية قبل إتمام العمليات (رسائل تأكيد متكررة) | FOM-CAS §Pax Checkout |
| Tag Deposits to Rooms: عرض ودائع الضيف عند Check-in | FOM-CAS ص46 |
| Paid Outs: Reason من قائمة معرفة (F1) | FOM-CAS §Paid Outs |

---

## مصفوفة الرسائل الموثقة (Documented Messages)

| الرسالة/السلوك | الشرط | المصدر |
|---|---|---|
| Alert عند تخصيص غرفة صيانة | غرفة معلمة صيانة | FOM-REG ص33 |
| Error عند تعديل تعرفة تاريخ ماضٍ | محاولة تعديل ماضٍ | FOM-REG ص47 |
| "Settlement is not tallied" | تسوية غير متطابقة | FOM-CAS ص77-78 |
| Guest Profile screen | أسماء متشابهة في History | FOM-RES ص8 |
| Duplicate reservation prompt | حجز مكرر | FOM-RES ص8 |
| Confirmation box برقم الفاتورة | حفظ Invoice by Arrival | FOM-REG ص73 |
| Operation Cancelled window | تأكيد إلغاء فاتورة | FOM-REG ص77-78 |
| Replace existing photo (Yes/No) | Guest Photo مع صورة قديمة | FOM-REG ص66-67 |

> `[PENDING DEEP READ]` رسائل النصوص الكاملة الدقيقة — النصوص الأصلية غير قابلة للنسخ الحرفي (ملكية IDS) وتُوثَّق وظيفياً فقط.
