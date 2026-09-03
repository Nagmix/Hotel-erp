# 01 — محرك التقارير والبنية التحتية — Financial Management (Phase 7)

> الأنماط المشتركة لـ46 تقريراً + **القوانين الخمسة** التي ينفرد بها هذا الملف.

---

## 1. قنوات الإخراج: **الأغنى في المرحلة 7** (5 قنوات)

| القناة | الشاهد | التفصيل |
|---|---|---|
| **Print** | كل التقارير | + اختيار طابعة من قائمة (16A/Advice/Voucher) |
| **Email** | **Form 16A فقط** | "available only if you select Account Type – **Vendor**" — قناة مقيّدة بنوع الكيان |
| **Spool** | **16A** | "enter the **file name** to save the file in the 'File Name for Certificate' field" — Spool بمعنى **حفظ لملف مسمى** (أوضح توثيق Spool في الحزمة — يغلق جزءاً من غموض قناة FO الرابعة) |
| **Excel** | **User Reports (§34)** | "Select type of Print option from **Direct or Excel**" — ثاني توثيق Excel بعد MNT Parameter Listing (عائلة Excel: MNT + FAS) |
| **80/132** | Auto Posted (§21) + TB F2 (§9) | **XOR مع Zero Balance في TB F2** — أول اقتران إجباري بين محورين كانا مستقلين في FO/POS |

**التسلسل عبر المرحلة 7:** FO (4 قنوات موحدة + Email) → POS (4 + Port ID) → MGT (**صفر إلكتروني**) → FAS (**5 قنوات بأوضح مواصفة**) — MGT تؤكد كونها الشاذة.

## 2. مسار البريد الموثق بالعتاد (16A — فريد بالحزمة)

```
Outlook مثبّت + Broadgun PDF printer مثبّت + Broadgun = الطابعة الافتراضية
       ↓ (PDF Settings "highlighted in red" — إعدادات إلزامية)
بريد المورد (محفوظ في Vendor Master — "email setting for Vendor is required under Vendor Master")
       ↓
رسالة تأكيد ظهور ("You will get the following confirmation message")
```

- **منتجان تجاريان بالاسم**: Microsoft Outlook + **Broadgun PDF printer** — البنية الوحيدة الموثقة بهذه الدقة (يعني: الطباعة-إلى-PDF هي آلية توليد المرفق — الطابعة الافتراضية = المولد!).
- تكامل مع **Vendor Master** (بريد المورد شرط) — وF1-lookups في كل مكان.

## 3. قانون Print Forms — النمطان المسجلان

### النمط الأول (قائمة مستقلة — كما في MGT):
- **Balance Confirmation (§14)**: "The letter is generated in a **customized format**. Therefore it is necessary to define the relevant **Program ID** for Balance Confirmation format in the **Print Forms option** under Setup sub module."

### النمط الثاني (ضد Transaction Codes — فريد بFAS):
- **Voucher Print (§25)**: "The printing of these forms is based on **Voucher Print program IDs specified against the Transaction Codes in the Transaction Types parameter**" — البرنامج **يُربط بنوع المعاملة** (كل نوع قسيمة له برنامج طباعته) — تسجيل لامركزي بالكيان!

### النمط الأول بعتاد موثق (Advice/Cheque §24):
> "developed as per your specifications on **pre-printed or plain, continues or cut sheet stationery** on **Dot Matrix / Desk Jet / Laser Jet Printers**. (Refer Print Forms option under Setup)"

- **ثلاثية الطابعات**: Dot Matrix / Desk Jet / **Laser Jet** (امتداد ثلاثية الورق MGT بثلاثية عتاد!) — إرث Dot Matrix حرفياً.

**مجموع تقارير Print-Forms الحاكمة عبر الوحدتين: 6** (MGT: PO/Standing PO/GRN + FAS: Balance Confirmation/Advice/Cheque/Voucher Print) — القانون يؤكد: **مستندات العبور المؤسسي** (مورد/ضريبة/دفع) = كود مخصص لكل عميل.

## 4. نمط Tag/Load التفاعلي (×4 — عائلة عابرة للوحدات)

| التقرير | الفعل | التفاصيل الحرفية |
|---|---|---|
| Debit Note Print (15) | Load | "Click **Load**. The data will display" → "Under **Tag column** double-click to change the option to **Yes**" |
| Advice/Cheque (24) | Load | Tag افتراضي **No** — "keep the cursor on the row and press **Enter or Double Click**" + **أزرار: Un Tag / TagAll / Un TagAll** |
| Voucher Print (25) | Load | "click **Toggle Tag** button" لاختيار الكل |
| User Reports (34) | Load | "double-click in the field to change the tag to **YES**" |

- **الدورة الموحدة**: معايير → **Load** (يجلب شبكة) → **Tag YES** انتقائياً → طباعة الموسوم فقط.
- **عائلة عابرة**: MNT Job Order Generation (الجلسة 13) + MGT §17 (Load) — **Tag-YES نمط UI مركزي في FN6i** للطباعة الانتقائية (ERPNext سيقابله checkboxes في Print Dialog).

## 5. مفاتيح المساعدة: دلالات ثابتة (F1/F3)

- **F3 = Financial Year** حصراً (2/12/13/33... في كل موضع FY).
- **F1 = كيان**: Account Name · Vendor · Sub Ledger · Sl. Name · Certificate No · Doc No · Budget Types · Report numbers.
- أدق التزام دلالي في الحزمة (FO خلطت F1/F3 في مواضع).

## 6. الطابعة الافتراضية الديناميكية (Voucher Print §25)

> "All printer definitions through the **Printer Settings** will be displayed in the provided list. **The printer connected to the System from where the Print Command is being executed, will appear as a Default printer**."

- **الطابعة الافتراضية = تابعة لموقع التنفيذ** (وليست ثابتة) — طباعة محطية (station-aware) — يقفل UNK-093 جزئياً من جهة FAS: القائمة من **Printer Settings** (طبقة SYS/Setup) — نفس اسم القائمة "pre-defined" في MGT.

## 7. الصلاحيات: صفر — **الوحدة 12/17 والأخيرة**

46 تقريراً بلا صلاحية واحدة — لكن هنا الأخطر في الحزمة كلها:
- **Audit Trial** (بالمحذوفات والمعدلات وبأثر Users!) · **TDS** (نماذج ضريبية رسمية) · **Voucher/Advice Print** (مستندات دفع!) · **Unlinked/Linked** (بنية GL نفسها!).
- بلا صلاحيات = **أي مستخدم يطبع شيكات ويرسل نماذج ضريبية** — أعلى خطورة ممكنة (أخطر من POS-GL سابقاً).

## 8. حصيلة محرك المرحلة 7 النهائية (FO+POS+MGT+FAS)

| الميزة | FO | POS | MGT | **FAS** |
|---|---|---|---|---|
| قنوات الإخراج | 4 + Email | 4 + Port | 1 (ورق) | **5** (Print/Email/Spool/Excel/132) |
| نمط التوليد | مباشر | مباشر | **خطوتان** | مباشر + **Load/Tag ×4** |
| Print Forms | — | — | 3 | **3** (بنمطي تسجيل) |
| INI switches | 63 | 137/335 | — | **—** (عائلة INI تُقفل عند 6 مفاتيح) |
| Program IDs | FOMRR## | — | — | — (لكن Pgm.ID في SET) |
| أشباح | 1 (Report Designer + IDS) | 1 (KDS) | — | **2 (IDS + iDesigner)** |
| صلاحيات | 0 | 0 | 0 | **0** (12/17 النهائية للوحدات المقروءة REP) |
