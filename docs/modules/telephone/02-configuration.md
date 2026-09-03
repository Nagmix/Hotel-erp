# 02 — التهيئة (Configuration) — وحدة TEL

> **تهيئة مزدوجة الطبقة:** (1) **Telephone Link Setup** — قلب EPABX التقني (بادئة/برنامج تحويل/مدة غير مفوترة/ربط FO/تواصل ثنائي/تقريب رباعي/ضريبة حكومية)؛ (2) **Telephone Revenue Posting** — قلب الترحيل المالي (موحد/تفصيلي + كود إيراد لكل نوع)؛ + التهيئة السلوكية عبر **Module Attributes** في SYS (عرض المدة). **لا مفاتيح INI في الوحدة كلها**.

---

## 1. Telephone Link Setup — تهيئة EPABX المركزية ⭐

> "the user have to complete the telephone link setup **accurately to ensure proper functioning of the telephones in the Property**"

| الحقل | المواصفات الموثقة |
|---|---|
| EPABX Prefix | "a single alphabet/digit code... displayed along with the extension number" — اختياري |
| Conversion Program | "a code set to **post the call made by the Guest, sensing the information sent to the EPABX**" — أبجدي-رقمي ≤7 |
| Uncharged Duration | "the default charge fixed by the Property for all the **Matured Local Calls**" — عتبة المجانية |
| Link to Front Office | Yes/No — "to post the calls made by the guest to front office and will be **charged to guest port folio**" — **المفتاح الرئيس للإيراد** |
| 2-Way Communication | Yes/No — "activate / de-activate the **phones, voice mails, wake-up calls and room status**" — قناة التحكم العكسي |
| Round Off Seconds | "the number of seconds to which a call actually is rounded off" |
| Round Off Required | **Higher / Nearer / Lower / None** |
| Round Amount | "will be **read at the time of billing**" — إلزامي فقط عند اختيار Higher/Nearer/Lower |
| Government Tax Structure | "the tax structure decided by the Government. Example: **Sale Tax**... applicable only to those countries where **telephone sales are taxed**" |

### المفاهيم التقنية الموثقة (فريدة في المشروع)

| المفهوم | النص الحرفي |
|---|---|
| **Matured Calls** | "The time taken to connect a call is **not considered** while calculating the call charges. The actual call charge is calculated **when the called number responds**" |
| **Battery Reverse Signal** | "a facility provided by the **Local Telephone Exchange**, which gives you the time elapsed to connect a call" |
| **عدّ المدّة الحقيقي** | "Even if the guest has called from many extensions, **minutes of actual call duration only should be recorded**" |

## 2. Telephone Revenue Posting — تهيئة الترحيل المالي

| الحقل | المواصفات |
|---|---|
| Consolidate Postings | **Yes/No لكل نوع من الأربعة** (Local/STD/IDD/Other) — خيار لكل نوع على حدة! |
| Revenue Code | F1 لكل نوع — "select the revenue code to which the revenue generated from each call type can be posted" |

**دلالة التوحيد:** Yes = "one entry for the day for each category of calls in the guest folio" / No = "post each call entry separately to the guest folio, and these entries **will appear on the guest bill**".

> **قراءة تصميمية:** مزج Hybrid مشروع — يمكن توحيد المحلي التافه وإفصال IDD المكلف — قرار لكل فندق. (F-TE-6: بنود فاتورة موحدة/مفصلة.)

## 3. التهيئة السلوكية عبر SYS (خارج الوحدة)

| الإعداد | الموضع | الأثر |
|---|---|---|
| **عرض المدة** | "If you want the call duration to be printed in **minutes**, then change the settings in **Module Attributes**. (Refer CHAPTER SUPERVISOR under MODULE SYSTEM SETUP)" | مدة الطباعة في Print Telephone Bill: ثوانٍ (افتراضي) أو دقائق |

- **إحالة SYS الوحيدة في الوحدة** — TEL ثالث وحدة بلا INI ذاتية (بعد CARE وMEM) لكن الأولى التي تُحال لـ**Module Attributes** صراحة (سمة Module مستقلة عن مفاتيح property.ini).

## 4. تهيئة التشغيل اليومي (Call Accounting)

### 4.1 تفعيل/إيقاف الامتداد + بوابات الأنواع

| الإعداد | القيم | الدلالة |
|---|---|---|
| الهدف | Room أو Extension | "If you select Room, the cursor will move to Room # field... If Extension... Extension Location field" |
| Function | **Activate / De-activate** | حالة الخط |
| Local Call | Yes/No | "though the telephone line is activated, **you cannot make any local calls** from this line" |
| STD Call | Yes/No | بوابة مستقلة |
| IDD Call | Yes/No | بوابة مستقلة |

- **قراءة تصميمية:** تفعيل الخط وتفعيل كل نوع قراران مستقلان — إدارة مخاطر دقيقة (إتاحة الاتصال المحلي فقط لغرف محددة، أو منع IDD دون إطفاء الخط).

### 4.2 كلمة مرور الامتداد

- "set up a password to a Room or Departmental Telephone extension **when a Guest registration is done**. This password will be **valid till the Guest checkouts**" — دورة حياة مقيدة بالإقامة.
- قيود: أرقام فقط ≤10 خانات · الغرف: "only **occupied rooms**" · مع Reg# (F1) للغرف · Location يُعرض تلقائياً للامتداد.

## 5. تهيئة كروت الأبواب (Door Lock User Interface)

| النمط | متى | قيود |
|---|---|---|
| Issue New Card | "new Guest check-ins to the Property" | Room #1 + Room #2 (غرفة إضافية!) + No of Nights + From/To + CI/CO Time |
| Copy Card | "room is shared by a family or a group... primary guest requesting another access card **with same features**" | نفس حقوق الكرت الأصلي |
| Single Open Card | "authorized representative from the hotel will issue a new card with a facility to access the respective requested room **only once**" | **Onity فقط** |
| Check Out | "disable the Door Card Key when the Guest... is checking out" | "the card reader should be attached... and the card should be inserted in the card slot" |
| Read a Card | "view the Guest's information stored in the card" (CI/CO dates + times) | **Onity فقط** |

- **آلية الترميز الموثقة:** "Click **Encode** for the card information to be transferred to the key card system, **saved in the backend, read by the door lock interface program and send to the device**" — سلسلة: شاشة → Backend → برنامج وسيط → جهاز.

## 6. مصفوفة قرارات التهيئة (ماذا يحدث عند كل موضع)

| الموضع | القيمة | السلوك الموثق |
|---|---|---|
| Link to FO | No | المكالمات لا تُرحّل للفوليو (تظهر في Unbilled؟ — غير مصرح؛ الأرجح تسجيل فقط) |
| Consolidate | Yes | بند واحد يومي لكل نوع في الفوليو |
| Consolidate | No | بند لكل مكالمة "appear on the guest bill" |
| Calculation % Others | 00.00 | "Hotel offers this facility free of charge" (مجاني) |
| Calculation % (STD/IDD) | 0 | **ممنوع** حرفياً (فقط لغير STD/IDD) |
| Round Off Required | None | "you need not enter the amount" (حقل المبلغ يُترك) |
| 2-Way Communication | Yes | التحكم بالهواتف/البريد الصوتي/المنبهات/حالة الغرفة |
| Uncharged Duration | — | المكالمات ≤ القيمة تُسجل **خطأ** (CAC ص5) |

## 7. التبعيات والمخاطر

1. **الدقة الحرجة:** صياغة "have to complete the telephone link setup **accurately** to ensure **proper functioning**" — الوحدة الوحيدة التي تحذّر من سوء التهيئة بهذه الصراحة (طبيعة العتاد).
2. **الضريبة الحكومية اختيارية جغرافياً:** "applicable only to those countries where telephone sales are taxed" — تهيئة مشروطة بالبلد (عائلة Geo-specific مع Statutory في HRP).
3. **بادئة EPABX عرضية فقط:** "displayed along with the extension number" — وظيفة إظهار لا توجيه.
4. **لا مسار تهيئة لبرنامج التحويل:** كود ≤7 محارف يُدخل بلا توثيق لماذا/كيف يربط الملفات (UNK-055).
