# 07 — الصلاحيات والأدوار (Permissions) — وحدة ACR

> المصدر: ACR-SET §4 (AR User Access ص9-10) + استدلالات الأدوار من الوظائف الموثقة. **نموذج ACR هو أبسط نماذج الصلاحيات في النظام وأوضحها** — وسيُقارن بنموذج FAS (Transaction Type Rights) عند بناء نموذج الصلاحيات الموحد (UNK-013).

---

## 1. AR User Access — المصفوفة النظامية الموثقة

| البعد | القيم | المصدر |
|---|---|---|
| المحور الأول | **User** (من قائمة مستخدمي النظام) | ACR-SET §4 ص9 |
| المحور الثاني | **نوع القيد**: Debit · Credit · **Adjustment** · **Post** ("Online Bill wise Receipt posting") | ACR-SET §4 ص9 |
| القيم المسموحة | Yes / No (تبديل بـ Double-click أو Enter) | ACR-SET §4 ص10 |
| الافتراضي | **No** لكل الخلايا — deny-by-default | ACR-SET §4 ص10 |
| نطاق التطبيق | "transaction types... in the **Transaction Entry** menu option" — حصراً | ACR-SET §4 ص9 |

### دلالة كل نوع قيد (من سياق OPR)

| النوع | ما يحكمه | المصدر |
|---|---|---|
| Debit | إدخال فواتير مدينة يدوية | ACR-OPR §1 ص4 |
| Credit | تسجيل قسائم القبض (مطابَقة/غير مخصصة) | ACR-OPR §1 ص4 |
| Adjustment | قيود الصحو/التسوية | ACR-OPR §1 ص7 |
| Post | الترحيل الإلكتروني على مستوى الفاتورة (Online Bill wise Receipt posting) | ACR-SET §4 ص9 |

## 2. الأدوار الوظيفية المستنبطة (من الوظائف الموثقة)

> `[INFERENCE]` — الأدوار غير مصرَّحة بأسمائها في أدلة ACR؛ تُستنتج من الوظائف ومواضعها. تُطابق لاحقاً مع `docs/domain/hotel-roles.md` (20 دوراً موثقاً).

| الدور المستنتج | الوظائف الموثقة التي يملكها | المصدر |
|---|---|---|
| **AR Clerk / Credit Clerk** | Transaction Entry (D/C/A) · Match Bills–Receipts · Receipts Untagging · Browse | ACR-OPR §1/§2/§6 |
| **Collection Executive** | Debtors Follow-Up (تعيين المتابعات له من Profile) · Projection | ACR-SET §5 ص14 + CRT |
| **Credit Manager** | Company Profile (Allow Credit/Limit/Interest) · Blacklist (بمجيز) · SOA/Rollback | ACR-SET §5 |
| **Accounts Clerk (Bank)** | Cheque Deposit Statement · Outstanding Update | ACR-RPL §15 + ACR-OPR §5 |
| **Auditor** | Transaction Audit · SOA Print · Ledger Balance | ACR-RPL §11/§9/§4 |
| **System Administrator** | AR Start Date · Specify Aging · AR User Access · Purge · Print Forms | ACR-SET §1/§3/§4/§7/§8 |

## 3. أنماط التفويض الموثقة في ACR

| النمط | الموضع | المصدر |
|---|---|---|
| **تفويض الوصم** | Black List يتطلب اسم **مجيز** بشري إلزامي (مع السبب) | ACR-SET §5 ص12 |
| **تفويض التعيين** | Follow-Up تُعين لمستخدم محدد (Assigned To) | ACR-CRT ص3 |
| **قفل إجرائي** | Purge: توليد التقارير أولاً + منع الإدخال اليومي | ACR-SET §7 ص18 |

## 4. أسئلة الصلاحيات المفتوحة (تُحوَّل لنموذج ERPNext)

| السؤال | الأثر | المصدر |
|---|---|---|
| هل AR User Access يحكم **العرض** أم **الإدخال** فقط؟ | تصميم Role Profile | `[NOT DOCUMENTED]` — النص يقتصر على "allow or restrict user access to transaction types" |
| هل الصلاحية **لكل Property** أم عالمية؟ | نموذج User Permissions في Frappe | `[NOT DOCUMENTED]` |
| من يملك Rollback SOA؟ (خطر مالي) | قرينة: غير مقيد نصاً — **فجوة صلاحية حرجة** | ACR-OPR §8 ص21 |
| من يملك Cancel Invoice؟ | مثله — غير مقيد نصاً | ACR-BIL §2 ص5 |
