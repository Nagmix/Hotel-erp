# 12 — التكاملات (Integrations) — وحدة ACR

> 15 تكاملاً موثقاً (I-AR-01..15). AR = **مصبّ تسويات المنظومة الفندقية كلها** ومصدر ترحيل فوري إلى GL. راجع `11-accounting-impact.md` للجانب المالي.

---

| ID | التكامل | الاتجاه | المفصل الموثق | المصدر |
|---|---|---|---|---|
| I-AR-01 | **FO → AR** | FO → ACR | "credit settlements are transferred to the Accounts Receivables module **automatically**" + قيود مدينة تلقائية + عارض فاتورة FO المصدر | FOM-CAS ص69 + ACR-OPR §1 ص2+ص9 |
| I-AR-02 | **POS → ACR** | POS → ACR | قيود مدينة تلقائية للشركات + عارض فاتورة POS | ACR-OPR §1 ص2+ص9 |
| I-AR-03 | **Banquets & Conferencing → ACR** | BQT → ACR | "auto posted (bills settled on credit) from the Front Desk, Point of Sale, **Banquets & Conferencing** & Membership" | ACR-OPR §1 ص2 |
| I-AR-04 | **Membership → ACR** | MEM → ACR | نفس النص | ACR-OPR §1 ص2 |
| I-AR-05 | **ACR → FAS (ترحيل تفاعلي)** | ACR → FAS | INI #56=0 + حسابات Link AR to Finance (Sundry Debtors/Cash/Bank/Commission) + شاشة FA عند الحفظ | ACR-OPR §1 ص10 |
| I-AR-06 | **ACR ↔ FAS (Aging مشترك)** | ثنائي | "queries and report options in the Accounts Receivable **and Financial Management** module is based on this definition" — نفس التعريف يظهر في FAS-SET §26 | ACR-SET §3 ص8 |
| I-AR-07 | **FO Setup → ACR (Company Types)** | FO → ACR | أول 3 خانات من Company Code = Company Types من FO Setup | ACR-SET §5 ص11 |
| I-AR-08 | **Company Profile مشترك (7 وحدات)** | مركزي | "used in Front Desk, Sales & Marketing, Point of Sale, Accounts Receivables, Banquets, Conferencing and Membership" | ACR-SET §5 ص10-11 |
| I-AR-09 | **S&M ← ACR (Watch List Report)** | ACR → S&M | Watch List/To Date يغذي "Watch List Companies under Sales & Marketing" | ACR-SET §5 ص11-12 |
| I-AR-10 | **SYS (Module Attributes ×4)** | SYS → ACR | #1 Receipt# آلي · #2 نطاق طباعة الفواتير · #3 Audit trail · #6 Invoice Matching | ACR-OPR §1 ص4-5 + BIL §2 ص4 + RPL §11 ص20 |
| I-AR-11 | **SYS (INI ×2 — منطق معكوس)** | SYS → ACR | #56 ACR2FAS (0=ممكن، افتراضي معطل) · #74 ACRALLOWUPDATION (0=يسمح بعد الطباعة) | ACR-OPR §1 ص10 |
| I-AR-12 | **SYS (Pgm ID for Print Forms)** | SYS → ACR | شرط إلزامي لطباعة Monthly Invoice Statement | ACR-BIL §1 ص2 |
| I-AR-13 | **FAS Exchange Entry → ACR** | FAS → ACR | سعر الصرف يُعرض غير قابل للتحرير في القيود | ACR-OPR §1 ص3 |
| I-AR-14 | **شركات البطاقات (خارجي)** | ACR → CC Company | Credit Card Register: "covering letter... along with bill details and Charge Slips for receiving payment after deducting the commission" + Consolidation بمجموعات | ACR-RPL §8 ص13 + ACR-OPR §4 |
| I-AR-15 | **البنك (خارجي)** | ACR → Bank | Cheque Deposit Statement "replaces the number of deposit forms the Cashier will have to fill in" + تقسيم Local/Outstation | ACR-RPL §15 ص23 + ACR-SET §2 ص6 |

## أنماط تكاملية موثقة (تُعتمد في المعمارية)

1. **نمط المصبّ الائتماني الموحد (Credit Sink):** كل تسوية ائتمانية بأي وحدة → قيد AR تلقائي واحد — لا ازدواج محاسبي، والمطابقة تتم في مركز واحد.
2. **نمط الترحيل التفاعلي:** AR وحدها ترحّل **عند الحفظ بشاشة FA** — قرار UX معماري (مقابل دفعات FO/POS المجتمعة).
3. **نمط القفل العابر للوحدات:** Credit Limit في Profile يمنع التسوية **قبل حدوثها** في FD/POS/BQT — تحقق Upstream مركزي.
4. **نمط الملف المشترك:** Company Profile ملكية مشتركة (7 مستهلكين) مع بادئة نوع موحدة من FO — يحسم UNK-001 جزئياً باتجاه **Master مركزي واحد** (ولكن للشركات؛ Guest Master حالة منفصلة).
5. **نمط إخراج خارجي جاهز:** خطابات CC + كشوف إيداع بنكي بديلة النماذج الورقية — مخرجات عملية موثقة.
6. **نمط "Getting Started" المرجعي:** User Defined Print Forms وPrint Form Designer يحيلان لوثيقة Getting Started خارج حزمة الـ65 — تبعية وثائقية خارجية (GAP-AR-D02).
