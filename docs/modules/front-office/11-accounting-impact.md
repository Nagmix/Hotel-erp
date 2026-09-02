# 11 — الأثر المحاسبي (Accounting Impact) — وحدة Front Office

> **قاعدة صارمة (Phase 6):** لا قيد يُخترع — غير الموثق يوسم `[NOT DOCUMENTED]`.
> هذه الوثيقة تجمع الأدلة المحاسبية المرصودة في وثائق FO؛ التحليل الكامل لقواعد الترحيل يجري في `docs/accounting/` (Phase 6).

---

## 1. موضع FO في خريطة الترحيل

من FAS-SET (روابط الترحيل الستة الموثقة في `document-map.md` §1):

| الرابط | المصدر | الوجهة |
|---|---|---|
| **FO → Finance** | إيرادات الفندق الأمامي | Financial Management (GL) |
| **AR → Finance** | تسويات AR | Financial Management (GL) |

**الوسيط الأساسي:** كل التسويات الائتمانية تمر تلقائياً عبر Accounts Receivables (FOM-CAS ص69: "All credit settlements are transferred to the Accounts Receivables module automatically").

---

## 2. الأحداث المولدة للقيمة المالية (Revenue/Receipt Events)

| الحدث | الوثيقة/الصفحة | طبيعة الأثر | تفاصيل |
|---|---|---|---|
| Post Charges (شحنة يدوية) | CAS ص4-9 | مديونية على الفوليو | Revenue Code + Currency + Charges + Exchange Rate → Total شامل الضرائب |
| Room Rate Posting (Individual) | CAS ص20-21 | مديونية تعرفة | Rate + Plan (+Extra Bed) — Day Charge 1 أو 0.5 |
| Room Rate Posting (All Rooms) | CAS ص22 | مديونية جماعية | تُنفَّذ عادة وقت Night Audit |
| Additional Room Rate | CAS ص23-25 | مديونية | أنواع: Rate / Plan / Extra Bed / **Retention Charges** (كل نوع Taxable/Tax منفصل) |
| Post Extra Charges | CAS ص43-46 | مديونية بالسعة | Adult/Child لكل يوم حتى المغادرة؛ شامل الضرائب |
| Fixed Charge Posting | CAS ص46-49 | مديونية ليوم محاسبي | لا تكرار (revenue, guest, day) |
| Deposits (Guests/Rsvn/City Ledger) | CAS ص9-17 | **نقدية مقدمة (دائنية)** | Cash/Credit Card (+Authorization)/Cheque |
| Paid Outs | CAS ص17-19 | **مصروف مدفوع** | للضيوف أو City Ledger + Reason + Voucher# |
| Miscellaneous Charges | CAS ص19-20 | مديونية لغير المقيمين | Settlement فوري (Cash/CC/Cheque) |
| Bill Allowance / Consolidated Allowance | CAS ص25-35 | **خصم (عكس مديونية)** | على Charge/Tax/كليهما + تفويض |
| Settlements (9 أنماط) | CAS §13 | **تسوية الفاتورة** | تفاصيل §4 أدناه |
| Deposit Refund | CAS §83-86 | رد نقدية | Refund Amount أو Retention Charges |
| Foreign Exchange Entry | CAS §86-89 | عملية صرف | فئات + عمولة → Net Amount + ضريبة ممكنة |
| Credit Card Encashment | CAS §89-91 | صرف من بطاقة | Total − Commission% = Net |
| Retentions (Cancel/No-Show) | RES ص67-68 | **إيراد عقوبة** | يُدخل يدوياً Charge Amt |
| Extra Charges (وقت الحجز) | RES ص24-25 | مديونية مبكرة | Reservation/Rooms/Guests كهدف |
| Invoice by Arrival | REG §9 | فاتورة وكيل سفر | + Ad hoc Charges + Control Report |

---

## 3. التسويات — البنية المالية (CAS §13)

**بنية النمط الواحد (المشترك):** Amount (+ Tip Amount) + Remarks → Confirm → Save (يجب أن تتطابق التسويات مع صافي الفاتورة وإلا رفض).

| النمط | الخصوصيات المالية | الترحيل اللاحق |
|---|---|---|
| Cash | Amount + Tip + Remarks | نقدية |
| Credit Card | Type + Company + Card# + Expiry (M/Y) + **Authorization#** + Currency + Amount | طرف بطاقة/AR إن ائتماني |
| Companies | Company Code + Amount + Remarks | **→ AR تلقائياً (City Ledger)** |
| Staff | Staff Code + Amount + Remarks | موظف |
| Bill on Hold | Amount + Remarks | تعليق الفاتورة |
| Foreign Exchange | العملة → Received → تحويل آلي للعملة المحلية + Tip | صرف |
| Complimentary | المبلغ آلي + Tips + Remarks | **تسقاط (إيراد مكتوب/مجاني)** |
| Cheque | Cheque#/Date/Bank/Branch + Amount + Tips | أوراق دفع |
| Multi-settlement | أنماط متعددة لنفس الفاتورة | تركيب |

**خصائص موثقة:**
- Partial settlement + إبقاء الضيف مشغولاً بعد التسوية (ص69).
- Clear Room# بعد Save مرتبط بـ INI Switch 64 (ص78) — أي أن تحرير الغرفة من التسوية سلوك قابل للضبط.
- Receipt لكل تسوية + Receipt Print + Foreign Exchange Entry للتفاصيل (ص78-79).
- Resettlement لفاتورة مسواة بنمط مختلف (ص79-80).

---

## 4. قيود البنية الضريبية الموثقة

- Post Charges: Total Amount = شامل الضرائب (CAS ص9).
- Additional Room Rate: Taxable Amount + Tax Amount منفصلان → Day Total + Local Value (CAS ص25).
- Bill Allowance: خيار الضريبة Yes/No/**Exempt** (CAS ص27).
- Consolidated Allowance: اختيار الضريبة حسب الوصف — **luxury tax / service tax / value added tax** (CAS ص33).
- Extra Charges: خيار Tax Inclusive أو لا (RES ص25).
- Foreign Exchange: "Tax amount can also be calculated for Foreign Exchange" (CAS ص89).
- الحزمة (Package): تعرفة حصرية / شاملة الضرائب / خطة شاملة ضرائبها (RES ص7-8).

---

## 5. التسلسل اليومي (Night Audit) — القيود البنيوية

من FOM-DEP (الجلسة 1) — الترتيب المحاسبي الحاكم:

1. **Post Tariff** — ترحيل التعاريف لكل الغرف (يوازي Room Rate → All Rooms).
2. **Guest Balance** — بعد منتصف الليل فقط؛ حظر الترحيل إلا للتاريخ التالي.
3. **Night Balance** — تسوية الفواتير المعلقة؛ **Excess/Short = 0** إلزامياً (توازن الكاشير).
4. **Open New Date** — تجميد نهائي لليوم المحاسبي.

**UNK-006 (تحديث الحالة):** تفاصيل قيود Night Audit المحاسبية (أطراف القيد D/C وحسابات الوساطة) — **[NOT DOCUMENTED]** في وثائق FOM المقروءة؛ متوقع توثيقها في FAS-TRN. تبقى Unknown مفتوحة → `docs/analysis/unknowns.md`.

---

## 6. أسئلة محاسبية معلقة (تُحل في Phase 6)

| # | السؤال | الحالة |
|---|---|---|
| QA-1 | أطراف القيود (Debit/Credit) لكل حدث أعلاه | `[NOT DOCUMENTED]` — يُستخرج من FAS-TRN/FAS-SET |
| QA-2 | توقيت الترحيل (فوري vs نهاية يوم vs Night Audit) لكل نوع | جزئي: Room Rate→Night Audit موثق (CAS ص22)؛ البقية `[NOT DOCUMENTED]` |
| QA-3 | حسابات الوساطة (Suspense/Clearing) | `[NOT DOCUMENTED]` |
| QA-4 | معالجة Tips في القيود | `[NOT DOCUMENTED]` |
| QA-5 | معالجة Complimentary (تسقاط مقابل مصروف ترويج؟) | `[NOT DOCUMENTED]` |
| QA-6 | تسوية الفائض/العجز في Night Balance (آلية) | موثق المبدأ (Excess/Short=0) دون تفاصيل القيد |
