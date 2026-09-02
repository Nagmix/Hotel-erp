# 12 — التكاملات (Integrations) — وحدة POS

> 16 تكاملاً (I-POS-01..16) — POS عقدة مركزية: تستهلك SYS/FO/MEM وتُصدِّر إلى FAS/AR/FO.

---

| ID | التكامل | الاتجاه | المفصل الموثق | المصدر |
|---|---|---|---|---|
| I-POS-01 | **POS → FAS** | POS → FAS | Restaurant × Menu Group → D/C (مبيعات Credit/خصومات Debit)؛ ترحيل بعد Day End | FAS-SET §7 |
| I-POS-02 | **POS → AR** | POS → ACR | تسويات Guest/AR/Company/BoH = Guest Settlement ⇒ قيود AR تلقائية | TS ص36 + ACR-OPR §1 |
| I-POS-03 | **POS → FO (Folio)** | POS → FO | Guest Settlement بـ Room # → فاتورة فوليو الغرفة | TS ص36 |
| I-POS-04 | **FO → POS (بيانات الضيف المقيم)** | FO → POS | جدول الضيوف برقم الغرفة (بحث Guest) | TS ص36 |
| I-POS-05 | **FO → POS (Card Types)** | FO → POS | Privilege/Loyalty card types "defined in the Front Office Module" | POS-GST ص10 |
| I-POS-06 | **FO ↔ POS (Preferences)** | ثنائي | "details captured in Guest Preferences option of Front Office module will be shown here" | POS-GST ص18 |
| I-POS-07 | **SYS → POS (مراجع عامة)** | SYS → POS | Departments · Cost Centers · Currencies (General Setup) | POS-SET §1 ص7 |
| I-POS-08 | **SYS → POS (Module Attributes)** | SYS → POS | **#6 NC Bill Print · #29 Common Menu · #32 Network Printer** | POS-SET §1/§24/§15 |
| I-POS-09 | **SYS → POS (INI 404)** | SYS → POS | نطاق خصومات الأعضاء (رئيسي/ثانوي) | POS-SET §41 |
| I-POS-10 | **MEM → POS (Member Discounts)** | MEM → POS | Member Section screen + خصومات منفذ×نوع قائمة | POS-SET §41 |
| I-POS-11 | **ACR → POS (Revenue Discount)** | ACR/S&M → POS | خصومات Predefined من Company Profile (Revenue Discount Masters) | TS ص26 + ACR-SET §5 |
| I-POS-12 | **POS → Guest History** | داخلي | Post Guest History (زيارات + Breakup) | POS-GST §4 |
| I-POS-13 | **POS → طابعات الشبكة** | POS → أجهزة | KOT للمطابخ (لكل صنف/مطبخ/مركزي) + Bill متعدد + Settlement + Token | POS-SET §1/§15/§33/§34 |
| I-POS-14 | **قارئ البطاقات** | POS → أجهزة | Swipe يلتقط التفاصيل آلياً في تسوية CC | TS ص34 |
| I-POS-15 | **POS ↔ Banquets** (مفاهيمي) | POS/BQT | المنافذ تشمل قاعات؛ FAS يذكر ضرائب Banquets في رابط POS (Taxes type) | POS-LUK ص2 + FAS-SET §6/§7 |
| I-POS-16 | **Touch/PDA/Regular** | POS → منصات | ثلاث منصات تشغيل بصلاحيات منفصلة (Applicable To) | POS-SET §20 |

## أنماط تكاملية موثقة (تُعتمد في المعمارية)

1. **نمط نزيف القيود التلقائي (Automatic Debit Bleed):** كل تسوية ائتمانية بأي وحدة بيع تتحول آلياً لقيد AR — **مصبّ واحد** للمدينين (مثل FO تماماً) — يمنع الازدواج المحاسبي.
2. **نمط الرابط التعريفي المزدوج:** POS يعرّف خرائطه في FAS-SET (منفذ×مجموعة) **مسبقاً** — الترحيل يقرأ الخريطة (لا حسابات مضمّنة).
3. **نمط ثلاث منصات بذات النواة:** Regular/Touch/PDA بصلاحيات منفصلة لكن سلوك موحد — قرار معماري مباشر للـ Frontend الجديد (منصة واحدة متعددة الأجهزة).
4. **نمط البيئة المزدوجة:** Login بـ PMS/Dummy DB — فصل إنتاج/تدريب على مستوى **الاتصال** (قرار بيئات للنظام الجديد).
5. **نمط الطابعة ككيان:** كل طابعة معرَّفة باسم في الإعداد (KOT/Bill/Settlement/Token/Central) — طباعة موجهة بالبيانات لا بالأجهزة.
6. **نمط التاريخ المحاسبي المستقل:** Accounting Date للمنفذ (= Bill Date) آلي — يسمح بمعاملات ما بعد منتصف الليل تنتمي لليوم المحاسبي السابق (مثل Night Audit في FO).
7. **نمط الخصومات كعائلة موحدة المصب:** كل أنواع الخصومات تصب في بند Debit واحد بالرابط — تبسيط مقصود للترحيل مع تفاصيل تحليلية في التقارير.
