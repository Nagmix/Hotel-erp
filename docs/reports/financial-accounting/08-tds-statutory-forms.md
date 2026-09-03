# 08 — جناح TDS الهندي + تأكيدات الأرصدة — FAS-REP (Phase 7)

> TDS Details Report + §26-31 (Forms 16A/26J/27/26A/26C/26K) + §14 Balance Confirmation = 8 تقارير — **أضخم كتلة امتثال نظامي في الحزمة**.

---

## 1. خلفية: ما TDS؟

**TDS = Tax Deducted at Source** — النظام الضريبي الهندي حيث **يخصم المُصرف** الضريبة عند المصدر (عند دفع المورد/الإيجار/العمولة...) ويودعها السلطة **نيابة عن** المستفيد — ثم يُصدر **شهادة خصم** للمستفيد (Form 16A) لاسترداده/احتسابه.

**لماذا هذا الجناح موجود؟** الفندق **مُصرف كبير** (موردون/عقود/عمولات) — عليه التزامات TDS دورية ونماذج رسمية لكل مستفيد — **FAS هو المنفذ التشغيلي للامتثال** (مقابل امتثال الضيف في FO وPOS).

## 2. TDS Details Report — **كشف الخصومات**

"view **only those transactions for which TDS is deducted** by the Property."

| # | المعيار |
|---|---|
| 1 | Property Code dropdown |
| 2 | FY — إدخال **أو double-click أو F1** — "invoke Financial Year help window" |
| 3 | Month & Year — "**from Date [MMYY] help window**" — صيغة إدخال مختصرة موثقة! |
| 4 | **From/To Vendor** — "supplier/s for which TDS is deducted" |
| 5 | Tax Code block — **All أو اختيارات** |
| 6 | Ok |

- **MMYY** — إدخال الشهر-السعر مختصراً (نفس عائلة DDMMYY في FO HK) — عائلة صيغ مختصرة عبر الوحدات.
- **three-way للوصول لFY**: إدخال حر + double-click + F1 — أوسع مسارات مساعدة لحقل واحد.

## 3. §26 Print Form 16A — **النموذج الأكمل مواصفة في الحزمة**

**الوصف:** "print TDS Form 16A with the option of **New, Reprint** and for account type **direct payment, vendor and sub ledger**. **TDS Tagging must be done for the vendor** to be able to send the TDS Form 16A."

**خطوات كاملة (12 خطوة — أطول إجراء في الوحدة):**

| # | الخطوة |
|---|---|
| 1 | **New / Reprint** |
| 2 | Property + FY + **Account Type: Direct Payment / Vendor / Sub Ledger** — (Direct→Account · Vendor→Vendor · SubLed→SL) |
| 3 | date range |
| 4 | **Run Date** |
| 5 | **Ack Num button** → شاشة: "Fill in the **acknowledge number and cheque/DD numbers for the four quarters** and click **Save**" — **أرباع السنة الأربعة برقم إشعار + شيك/DD لكل ربع!** |
| 6 | Save |
| 7 | **Print / Email / Spool** — "(Email option is available **only if you select Account Type – Vendor**)" |
| 8 | Spool → **"enter the file name to save the file in the 'File Name for Certificate' field"** |
| 9 | Email → **"Microsoft Outlook and Broadgun PDF printer should be installed and Broadgun PDF printer should be set as default printer"** + "The following **PDF Settings highlighted in red** are required" |
| 10 | "The following **email setting for Vendor is required under Vendor Master option**" — بريد صحيح محفوظ |
| 11 | Print → Printer dropdown + **"Select the height of the form 11 or 12 IN"** |
| 12 | Ok |

**النقاط البنيوية المجمّعة:**
- **TDS Tagging شرط مسبق** — وسم TDS على المورد (من TRN) قبل أي إرسال.
- **رباعية الأرباع (Quarters)** — بنية إيداع TDS الهندية الرسمية (إيداع ربع سنوي) داخل الشاشة!
- **New/Reprint** — إعادة الإصدار وضع رسمي (تُقابل Normal/Repeat في Advice §24 — عائلة إعادة الطباعة الموثقة ×3).
- **Height 11 أو 12 IN** — **ارتفاع ورق النموذج موثق بالبوصة** (ورق قانوني هندي بحجمين!) — أدق مواصفة ورقية في الحزمة.
- **مسار Email = Outlook + Broadgun PDF + default printer + PDF settings حمراء + بريد Vendor Master + رسالة تأكيد** — (يُفصّل في 01 §2) — **أكبر كومة اعتمادات بريدية موثقة**.
- **Account Type ثلاثي**: Direct Payment / Vendor / Sub Ledger — نموذج واحد لثلاث علاقات خصم (مستفيد مباشر/مورد/حساب فرعي).

## 4. §27 Print Form 26J — **نموذج العائدات (Royalty)**

**الوصف الحرفية:** "**26J is a TDS Form pertaining to Royalty. It is an annexure of Form 16A**."

- المعايير: Certificate number range (From/To) — **F1** لقائمة الشهادات → Ok.
- **التبعية المعلنة**: 26J **ملحق بـ16A** — أول علاقة نماذج أب-ابن موثقة.
- **Royalty** — خصم عوائد (عقود امتياز/علامة) — يكشف نوع مدفوعات الفندق الخاضعة (مع Service PJV للخدمات).

## 5. §28/§29 Print Form 27 / 26A — **نماذج Challan**

"print Form 27 for the TDS with option of range between TDS certificate numbers" / "Form 26A for the TDS certificates generated..."

- المعايير (كلاهما): **Challan number + Challan Date** → Print.
- **Challan** = إيصال الإيداع الضريبي لدى السلطة — نموذج **إيداع** (مقابل 16A **شهادة** للمستفيد) — ثنائية نموذجية: إثبات دفع/إثبات خصم.

## 6. §30/§31 Print Form 26C / 26K

"print the Form 26C for the TDS Transactions" / "Form 26K for the TDS transactions" — كلاهما: **date range** → Print/OK.

- أوصاف أفقية متطابقة تقريباً — **إصدارا 26C/26K شبه توأمين** (بلا تمييز موثق — عائلة توائم نموذجية → مرشح UNK طفيف — يُدرج ضمن UNK-100 العام).

## 7. §14 Balance Confirmation — **خطاب التأكيد المخصص**

**الوصف:** "arrive at the outstanding balance for **Debtors and Creditors** and generate a **balance confirmation letter to be sent to Companies / Vendors for verification / confirmation** of the outstanding. The letter is generated in a **customized format**. Therefore it is necessary to define the relevant **Program ID** for Balance Confirmation format in the **Print Forms option** under Setup."

| # | المعيار |
|---|---|
| 1 | Property |
| 2 | A/C Code (مدين/دائن) |
| 3 | SL Code range |
| 4 | **Cut Off Date** — "**should be less than or equal to the Current System Date**" — "The details of payments displayed are **as on the Cut Off Date**" |
| 5 | **Debit / Credit / Both** |
| 6 | **Print Zero Balance** |
| 7 | **printer** |
| 8 | Print |

- **أداة تدقيق خارجي**: خطاب رسمي يطلب من الطرف المقابل تأكيد رصيده (معيار مهني في المراجعة!) — ثنائية مدين/دائن (تخدم ACR وFAS معاً).
- **Print Forms** (نمط 1 — قائمة Setup) + **Cut Off** بpast-only + **Zero Balance** خيار.
- التاريخ الافتتاحي للرصيد يُقطع عند Cut Off (يُجمّد التاريخ المرجعي).

## 8. جدول الجناح

| التقرير | النموذج القانوني | الميزة القصوى |
|---|---|---|
| TDS Details | — (كشف داخلي) | MMYY + F1/double-click/F3 ثلاثية |
| **16A** | **شهادة خصم** | New/Reprint + **أرباع ×4** + Email/Spool + Height 11/12 |
| 26J | **ملحق عوائد** | تبعية 16A معلنة |
| 27 / 26A | **Challan إيداع** | Challan No + Date |
| 26C / 26K | معاملات | توأمان |
| Balance Confirmation | **خطاب** | Program ID + Cut Off + D/C/Both |

**الاكتشاف التجميعي:** هذ الجناح **يخلّص هوية السوق الهندية** النهائية للمنتج: بعد (PAN-POS · C-Form/RLM/IT-FO · assessment-MGT · Lakhs) — **TDS الفندق كمُصرف** بستة نماذج رسمية وبنية أرباع سنوية ومسار بريد بمنتجات مسماة — **الحزمة كلها مصممة أولاً لسوق هندي** (اكتشاف إجمالي للمرحلة 7 يُستكمل في 11).
