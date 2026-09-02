# 17 — تحليل الفجوات (Gap Analysis) — وحدة Banquets

> فئة A: فجوات المصدر · فئة B: فجوات ERPNext.

---

## أولاً: فجوات المصدر (GAP-BQ-D01..D11)

| # | الفجوة | الدليل | المعالجة |
|---|---|---|---|
| GAP-BQ-D01 | **لا ملف BNQ-REP في الحزمة** — التقارير بلا دليل (FP تفاصيله في Program IDs فقط) | فهرس الحزمة (5 ملفات BNQ فقط) | 08-reports: تعويض بالمتطلب من Program Types |
| GAP-BQ-02 | صياغة Resettlement الملتبسة | "and the guest has already checked out" — تُقرأ حرفياً كشرط سماح؟ أم منع؟ | [UNCERTAIN] تسجيل + قرار تنفيذي (المنطق: منع ما رُحِّل لغرفة مغادرة) |
| GAP-BQ-D03 | قائمة عمليات KOT الـ 28 وSettlement الـ 15 | "28 lists of operations... displayed" بلا تعداد | 3 أمثلة فقط — يُستكمل من POS User Access المقروء |
| GAP-BQ-D04 | INI 346 دلالة القيمة | "can be altered by modifying the INI # 346" | [UNCERTAIN] سقف تعديل؟ |
| GAP-BQ-D05 | Coupons: استمرار/قيود Multiple | نمط موثق بلا قواعد مزج | [NOT DOCUMENTED] |
| GAP-BQ-D06 | تعديل Function Room بعد الإنشاء | "cannot be deleted" فقط — هل تعدل الحقول؟ | [UNCERTAIN] (Modify بالكود Help موثق) |
| GAP-BQ-D07 | توقيت BNQ→FAS | رابط الستة بلا توقيت | UNK-027 (Phase 6) |
| GAP-BQ-D08 | قيد الوديعة/الغرامات في GL | Vouchers بلا بنود | Phase 6 |
| GAP-BQ-D09 | Wedding/Birthday مقدمّة لكن Event Classification القائمة الكاملة؟ | "like AGM, Birthday..." | [UNCERTAIN] — قائمة افتراضيات شبه مكتملة |
| GAP-BQ-D10 | تعارض إدخال Inquiry (نسخه ممنوع لكن فوترة/وديعة؟) | Deposit "except Inquiry" — الفوترة على Inquiry؟ | [NOT DOCUMENTED] |
| GAP-BQ-D11 | صور الأنماط (Setup Style images) | "If the images... saved in the system" — آلية الرفع | [NOT DOCUMENTED] |

## ثانياً: فجوات ERPNext (GAP-BQ-E01..E12)

| # | الفجوة | الوصف | القرار |
|---|---|---|---|
| GAP-BQ-E01 | **لا حجز فعاليات/قاعات** | ERPNext بلا Event Booking/Floor plan | F-BQ-2 (PMS Banquet Event) |
| GAP-BQ-E02 | محرك التوافر الزمني | slot grid + Across-Dates | F-BQ-3 |
| GAP-BQ-E03 | Void معطّل لمنفذ BNQ | POS Invoice settlement rules | F-BQ-1 (تكوين منفذ) |
| GAP-BQ-E04 | سعة القاعة × نمط جلوس | لا نظير (Table seats واحد) | custom child |
| GAP-BQ-E05 | أدوان إيجار الساعات (5) | Item price بلا فترات | custom |
| GAP-BQ-E06 | Allowed per Menu group | BOM بلا قيود انتقاء | F-BQ-2 worksheet |
| GAP-BQ-E07 | FP ألوان الحالة (Printed/Finalized) | لا حالة طباعة قياسية | custom flags |
| GAP-BQ-E08 | Columns Order تخصيص رأسي | View column settings (موجودة جزئياً) | D — قياسي حديث |
| GAP-BQ-E09 | Booking Gate تقويمي | لا تحقق حجز تقويمي | F-BQ-5 |
| GAP-BQ-E10 | auto email بـ Outlook Express | تقنية متقادمة | Frappe Email/Notification |
| GAP-BQ-E11 | Vouchers معدلة/محذوفة كنماذج | Print بلا إصداريات | F-BQ-8 (سجل) |
| GAP-BQ-E12 | Dry Days/auspicious | لا مفهوم قياسي | custom في Event |

## ثالثاً: مقارنة كثافة الفجوات (تحديث الجدول التراكمي)

| الوحدة | مصدر D | ERPNext E |
|---|---|---|
| FO | 10 | 10 |
| FAS | 8 | 9 |
| ACR | 10 | 10 |
| POS | 11 | 12 |
| SYS | 8 | 9 |
| MGT | 12 | 14 |
| **BNQ** | **11** | **12** |

> **الاستنتاج:** فجوة BNQ الأبرز **غياب REP كلياً** (فريدة) — مقابل قابلية إعادة استخدام قياسية عالية جداً لمحرك POS (F-BQ-1) تُقابلها كلفة بناء "PMS Banquet Event" المخصص.
