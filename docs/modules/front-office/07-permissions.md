# 07 — الصلاحيات (Permissions) — وحدة Front Office

> الصلاحيات الموثقة نصاً في وثائق FO. المصادر الرئيسية الكاملة (SYS-SSP + FAS Transaction Type Rights + AR User Access) تُقرأ في Phase 8.

---

## نقاط الصلاحيات الموثقة سلوكياً

| العملية | نمط التفويض الموثق | المصدر |
|---|---|---|
| Create Hotel Chart | **username/password صالحان** (تحقق صريح) | FOM-REG ص97-98 |
| Cancel Check-In | Reason + تفويض (Reason Entry window) | FOM-REG ص93-94 |
| Cancel Reservation | اسم المعتمد + بيانات المتصل | FOM-RES §1.3 |
| Room Transfer / Swap | نافذة تفويض (Remarks + Authorization personnel) | FOM-REG ص50-52 |
| Transfer Folios / Pax Transfer | Authorized Person | FOM-CAS ص61 + §20 |
| الخصومات (Bill/Consolidated Allowance) | Reason + Remarks + Authorized By | FOM-CAS ص28 + ص33 |
| خصم تعرفة Change Guest Info | Reason + Authorized By + Remarks | FOM-REG ص46 |
| Foreex / CC Encashment | Authorized By + Remarks | FOM-CAS §17-18 |
| Re-Instate (الفوليو/الحجز) | بدون تفويض موثق صراحة — `[NOT DOCUMENTED]` | FOM-CAS §14 |

## أنماط ملاحظة

1. **نمط التفويض بالاسم (Named Authorization):** معظم العمليات الحساسة تسجل اسم المصرِّح — النظام يوثق "من أذن" لا "من نفذ" فقط. (نمط تصميمي مهم للنظام الجديد: Audit Trail مزدوج).
2. **Audit Trail للحجز:** تغييرات Amend تُسجل بالمستخدم والوقت عبر 5 أبعاد (RES §Audit).
3. **التنبيه دون منع:** بعض الحالات تنبه فقط (Alert للغرفة المعلمة صيانة).

## مصفوفة FO User Authorization الموثقة (الجلسة 3)

> من FOM-SET §35 (ص84-85): نافذة تربط **عمليات مميزة × مستخدمين** — "الوصول يُمنح أساساً للمشرفين أو الضباط ذوي السلطة الأعلى":

| العملية المميزة | السلوك | المصدر |
|---|---|---|
| **Over Booking — Accept** | قبول الحجز الزائد (فوق Over Booking % في Room Type) | FOM-SET §35 |
| **Hurdle Rate — fix** | تحديد الحد الأدنى للتعرفة (Revenue Management) | FOM-SET §35 |
| **Hotel Chart — update** | تحديث مخطط الفندق | FOM-SET §35 |
| **Folio Re-Open** | إعادة فتح فوليو الضيف | FOM-SET §35 |
| **Market Segment — edit** | تعديل قطاع السوق (لحجز قائم) | FOM-SET §35 |

المنح/السحب: Select العملية (أعلى الشاشة) → تحديد المستخدمين → أزرار منح/سحب جماعي → Save. — تُبنى عليها مصفوفة الأدوار في Phase 8 (`docs/security/`).

`[PENDING]` مصفوفة الصلاحيات الرسمية الشاملة (من SYS-SSP: أدوار × وظائف) + Transaction Type Rights (FAS) + AR User Access — Phase 8 — `docs/security/`.
