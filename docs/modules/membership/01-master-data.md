# 01 — البيانات الرئيسية (Master Data) — وحدة MEM

> **E-ME-01..25**: الكيانات الدائمة التي تُبنى عليها العضويات — مقسمة: (أ) كيانات التهيئة الـ12 من SET، (ب) كيانات العضوية الفعلية من MPF/MMN، (ج) كيانات المعاملات الداعمة من MTR.

---

## أ) كيانات التهيئة (SET)

### E-ME-01: Member Category (فئة العضوية)
| الحقل | الوصف الموثق | ملاحظة |
|---|---|---|
| Membership category | كود الفئة | فئات مثل NRI/executive "used in various operations across modules" |
| Subscription | Yes/No — هل تشترك | |
| Corporate | Yes/No | يفعّل حقول المرشحين |
| Number of nominees | عدد المرشحين | **يُفعَّل فقط إذا Corporate** |
| Children Age Limit | حد عمر الأبناء | يحدد من يُعد طفلاً |
| Number of References | عدد المُحالين | "Based on the number of references enter the reference details. Click Ref. Details" |
| Tenure (Y/M/D) | مدة العضوية | **"will not be applicable for Lifetime Membership"** |
| Spouse/Children/Additional family | عمودان لكل: Accept + Member | Accept=قبول التفاصيل، Member=اعتبارهم أعضاء Property |

### E-ME-02: Screening Detail (بند فحص)
- مسلسل تلقائي + وصف (مثال: Blood Group, Contact details) + Individual/Corporate + لكل فئة: Applicable؟ + Is it Mandatory؟
- **قائمة تحقق ديناميكية** تُعرض في Application Screening لكل طلب حسب فئته.

### E-ME-03: Service Rate Master (أسعار الخدمات)
- Application Date (**يجب ≥ تاريخ اليوم**) + Service Type (من Facility Codes) + Code/Description
- **ثلاث جداول**: Member Rates / Guest Rates / Affiliated Member Rates — كل واحد: Adult + Children + Tax Structure
- **إلزامي لـ Service Bill Entry**: "This option is mandatory for the Service Bill Entry" (SET ص7)
- لا تعديل إلا إذا "Applicable From > current date" (نمط future-only).

### E-ME-04: Membership Revenue Code (كود الإيراد)
| الحقل | الأثر التشغيلي |
|---|---|
| Code + Description | تعريف الإيراد |
| Subscription Details: **Once / Recurring** | Once → يظهر في Revenue/Facility Entry؛ Recurring → **لا يظهر** (يُرحّل دورياً فقط) |
| Refundable / Non Refundable | |
| Subscription Charge (checkbox) | "Members can be charged for these revenue codes during subscription if they are tagged as Subscription Charge" |

### E-ME-05: Membership Structure (هيكل الاشتراك)
- Application Date + Revenue Type + Category + **Currency (Exchange Rate يظهر تلقائياً)**
- أسعار: **Primary Applicant / Additional Adult / Child** "for different payment terms applicable" (راجع E-ME-08).

### E-ME-06: Complaints Category (Main/Sub) — لتصنيف شكاوى الأعضاء، "useful for browsing the pending complaints and for graphical representation".

### E-ME-07: System Attributes — 13 سمة Yes/No (انظر 02-configuration §2).

### E-ME-08: Facility Fixed Rates (الأسعار الثابتة)
- Applicable Date (≥ اليوم) + Service Type
- مصفوفة: **Primary Applicant / Spouse / Child / Additional Family Member (Child) / Additional Family Member (Adult)** × **Once / Annual / Half Yearly / Quarterly / Monthly**.

### E-ME-09: Membership Facility Code — Code + Short Name + Long Name ("Example: Boating, Billiards").

### E-ME-10: Cover Charges (رسوم الغطاء)
- Applicable Date + فترة (Monthly/Quarterly/Half year/Annual) + Revenue Code + Revenue details + Amount لكل فئة
- **Age limit** (بخيارات) + **Membership years** (بخيارات) + Adjustment Debit to be Consider + **Senior Citizen Exemption**.

### E-ME-11: Late Charge Fee Definition — لكل فئة: Structure Type (By Tax structure/Not applicable) + وصف/كود البنية من **بنيات ضريبة FO**.

### E-ME-12: Member User Defined Field (UDF) — Code + Name + **Field Data Type (dropdown)**.

## ب) كيانات العضوية (MPF/MMN)

### E-ME-13: Corporate Application (طلب شركة)
- Reference Number + Application Date/Valid until + Organization Name + Nature + Registered under law (Yes/No داخل/خارج البلاد) + Registration Particulars/Date
- **Financial Parameters: Net Worth + Turnover (Current + Previous year) + Net Profit for last year + Income Tax PA#** + Type of Business
- 3 تبويبات: General / Address (Register + Local + Mailing + أزرار نسخ + وسم مراسلات) / References (Membership# لو المُحيل عضو — F1، متعدد بأزرار تصفح)
- الحفظ يولّد **Application Number**.

### E-ME-14: Membership Application (طلب فرد)
- Reference Number + Name + Application Date/Valid until + تبويبات: Address (Residential/Work Place/Abroad + وسم مراسلات) / Work Details / Birth Reference Details / **Other Details (Credit Card + Bank + Personal + Vehicle!)**
- **Spouse**: General + work + Other + **Photo + Signature** (تصفح وإدراج)
- **Children** (متعدد)
- للمرشحين المؤسسيين (nominees) نفس الشاشة — "Non-Corporate (individual Members) and corporate nominees".

### E-ME-15: Interview — Date/Time/Interview Person/Remarks + Status: **Considered/Rejected/Cancelled**.

### E-ME-16: Credit Limit Details (عند التحويل) — **Allow Credit (Yes/No) + Credit Limit**.

### E-ME-17: Corporate Master / E-ME-18: Membership Master
- **إدخال مباشر دون طلب**: "you can enter the Corporate Membership details **without entering the initial application details**" — نفس بنية الطلبات + Credit Limit
- حفظ Membership Master يفعّل **إنشاء شركة ACR تلقائي** (سمة #10).

### E-ME-19: Affiliated Club Master (نادٍ متفق معه)
- Reference# + Name + Contact + **Affiliated Category Name** (فئة أعضاء النادي المستفيدين) + **Photo**.

### E-ME-20: Member Status Overlay — Blacklisted (مع Authorized Person + Reason) / Terminated / Resigned / Deceased (+ **Cause of Death** + خلافة) — تحتفظ كل وظيفة بمسؤول التغيير وسببه (مسار تدقيق).

## ج) كيانات المعاملات الداعمة (MTR)

### E-ME-21: Revenue/Facility Tag (وسم الفوترة الشهرية) — Revenue Type + Period (monthly/quarterly/yearly/half yearly/none) أو Facility (chargeable Y/N + **Fixed/Billing** + Period + Date).

### E-ME-22: Guest Visit — Check-in rows + ضيوف مرافقون (Insert/Edit Guest Details) + **Entry Fee** بفئة عضو أو **non-member A/C**.

### E-ME-23: Service Bill — Bill# تلقائي + Service rate code + Persons (بالغون/أطفال) + Discount (NONE/AMOUNT/PERCENTAGE + **Reason**) + Settlement.

### E-ME-24: Complaint (MEM) — من عضو / **ضد عضو**! + Nature + Priority + Assigned To + Action By + Remarks.

### E-ME-25: Member Event — Event Description + Venue + From/To (Date+Time) + Contact (+phone/mobile/email/fax) + **Chief Guest** + Remarks.

> **إحصاء:** ~25 كياناً جوهرياً — أثقلها E-ME-14 (طلب العضوية: 4 تبويبات + زوج + أبناء) وE-ME-03 (مصفوفة أسعار 3×2) وE-ME-08 (مصفوفة 5×5).
