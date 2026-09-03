# 05 — قواعد العمل (Business Rules) — وحدة TEL

> **BR-TE-01..24** — أقوى تركّز لقواعد **التسعير الفني** في المشروع (نبض × شريحة × نسبة × حدود × تقريب) + قواعد **حماية الإيراد** (شراكات بأغلى تعرفة، 0% الممنوعة) + قواعد **الفوترة العلاقاتية** (مصفوفة التحويل، كلمات المرور بالإقامة).

---

## أ) قواعد التسعير (Rating Engine)

### BR-TE-01: دلالات نسبة الحساب ⭐
- "If the Service Provider's rate for a single call is 60c, and if 100% is mentioned, then the original rate, which is 60c, is retained. If 150%... one and a half time... 200%... double."
- **الصياغة الحسابية:** سعر النزيل = سعر المزوّد × (Calculation% / 100) — لكل (امتداد، نوع).
- المصدر: SET ص4-5.

### BR-TE-02: صفر بالمئة الممنوعة للنوعين الدوليين
- "0.00%... is considered as an uncharged call. **(0% is applicable for all call types except STD and IDD)**" — الاستثناء يعمل للمحلي/Others فقط؛ STD/IDD لا تُمجّن أبداً.
- المصدر: SET ص4-5.

### BR-TE-03: المكالمات الأخرى = حد أدنى أو مجان
- "Toll free numbers, calls made from a Calling Card, AT&T calls etc." — "If the Hotel decides to charge a certain **minimum amount**... specify the amount... If the Hotel offers this facility **free of charge**... specify **00.00 %**".
- ⚠️ **تناقض موثق:** الحقل نسبة (%) لكن النص يصفه أحياناً كمبلغ (amount) — راجع GAP-TE-D04.
- المصدر: SET ص5.

### BR-TE-04: النبض أساس التسعير
- "The pulse rate in seconds should be mentioned under the **Seconds field** and call rate per pulse... under the **Rate field**" — لكلٍّ من P&T والفندق، لكلٍّ من العادي والأعياد.
- **الصياغة:** الرسوم = ceil/floor(المدة ÷ ثواني النبضة) × سعر النبضة (اتجاه التقريب = Round Off Seconds).
- المصدر: SET ص20.

### BR-TE-05: ثنائية المستفيدين
- "The rate charged by the Property is for calls made from a Room or an Outlet and will be **charged to the guest**. The rate charged by the Service Provider is for **all the calls** made from the Property and will be **charged to the Property**" — محاسبتان متوازيتان لنفس الحدث.
- المصدر: SET ص18.

### BR-TE-06: تعرفة الأقسام بلا ربح
- "Calls recorded from any of the departments are charged at the **normal Service Provider's rates**" — امتدادات الأقسام تُحمَّل بتكلفة المزوّد حرفياً (الإدارة لا تُربّح من نفسها).
- المصدر: SET ص4.

### BR-TE-07: المكالمة الناضجة والتقاط زمن الرد
- "The time taken to connect a call is not considered... the actual call charge is calculated **when the called number responds**" + Battery Reverse Signal يوفر زمن الاتصال.
- المصدر: SET ص16.

### BR-TE-08: المدّة المجانية
- "If the duration of the call is less than or equal to the value defined against **uncharged duration**" → **خطأ فوترة** (لا تُرحّل) — عتبة Uncharged Duration من Telephone Link Setup.
- المصدر: CAC ص5.

### BR-TE-09: تقريب رباعي الاتجاه
- Round Off Required: **Higher / Nearer / Lower / None** + Round Amount "read at the time of billing" + Round Off Seconds للمدة.
- المصدر: SET ص16-17.

### BR-TE-10: حدود الوجهة تسقف/ترفع الشريحة
- Minimum/Maximum Charge في Area Code — "If you give a minimum rate charge then **this will overwrite the Slab code**" (وكذلك الأقصى).
- المصدر: SET ص24-25.

## ب) قواعد حماية الإيراد (الشراكات)

### BR-TE-11: الشراكات الإلزامية الست (بلد + منطقة)
- Country: **LCA** + **9999999999** — Area: **LCA/LCA/LOCAL** + **9999999999×2 (أعلى IDD)** + **فارغ/9999999999 (أعلى STD)**.
- **الأثر:** "9999999999... used to tag a slab code for countries that are not defined" — غير المعرف يُسعَّر بالأغلى.
- المصدر: SET ص22 + ص25.

### BR-TE-12: تصنيف بادئة الأصفار
- "one zero at the beginning are STD, two zeroes are IDD and no zeroes are Local calls. 09986056565, 005674486754, 9980688744".
- المصدر: SET ص31.

## ج) قواعد الترحيل

### BR-TE-13: بوابة الربط بـFO
- "Select the option **YES** if the calls need to be posted to front office" — صمام الإيراد الرئيس (No = لا فوليو).
- المصدر: SET ص16.

### BR-TE-14: التوحيد قرار لكل نوع
- "Specify the method of posting required for **each call type**... Select options Yes or No for call types Local Call, STD, IDD and Other Calls" — Yes = "one entry for the day for each category" / No = "each call entry separately... will appear on the guest bill".
- المصدر: SET ص14-15.

### BR-TE-15: كود إيراد لكل نوع
- "select the revenue code to which the revenue generated from **each call type** can be posted" — أربع قنوات إيراد مستقلة.
- المصدر: SET ص14.

### BR-TE-16: ضريبة هاتفية مشروطة بالبلد
- "Government Tax Structure... Example: Sale Tax... applicable only to those countries where **telephone sales are taxed**".
- المصدر: SET ص17.

## د) قواعد العلاقات التشغيلية

### BR-TE-17: مصفوفة تحويل المكالمات ⭐ (جدول الدليل الحرفي)

| Call Transfer **Allowed** | Call Transfer **Not Allowed** |
|---|---|
| Department to Room | Room to Department |
| Department to Shop | Shop to Department |
| Department to Department | **Room to Room / Shop to Shop** |

- "The extension from where the call is getting transferred should **always be a department**... The application **does not allow** the call transfer option from a room or a shop".
- المصدر: CAC ص6.

### BR-TE-18: ربط غرف التوائم إلزامي
- "The Extensions in Linked Rooms **must be linked** using this option **so as to avoid errors during billing**" (Twin Rooms, Banquets, shops, Public rooms).
- المصدر: SET ص7.

### BR-TE-19: كلمة المرور بدورة الإقامة
- "when a Guest registration is done... **valid till the Guest checkouts**" — أرقام ≤10 خانات — غرف مشغولة فقط.
- المصدر: CAC ص7-9.

### BR-TE-20: بوابات الأنواع المستقلة عن حالة الخط
- "though the telephone line is activated, you **cannot make any local calls**" عند Local=NO — التفعيل لا يعني فتح كل الأنواع.
- المصدر: CAC ص3.

## هـ) قواعد الماستر

### BR-TE-21: خلود الشرائح الزمنية
- "You **cannot Modify or Delete** a time rate slab record... Add a new record with the same slab code but with a **new applicable from date**... latest applicable from date" — مثال: 18-Dec-2011 ضد 1-Jul-2012 → الأخيرة.
- المصدر: SET ص20.

### BR-TE-22: ثبات كود الدولة
- "cannot modify the **Country Code**" (الاسم والحالة فقط).
- المصدر: SET ص23.

### BR-TE-23: أعياد بتواريخ مستقبلية ومولد أسبوعي
- "The date entered should be **greater than the accounting date**" + Auto Generation لأيام الأسبوع في مدى — وتعرفة العيد مختلفة عن العادي.
- المصدر: SET ص10-13 + ص20.

### BR-TE-24: إعادة الترحيل بصيغة YES
- "Under the Select column double-click... to change the status to **YES**... the calls will be **reposted** to the Guest/Room folio for billing" — التحويل اليدوي الوحيد من خطأ إلى فاتورة.
- المصدر: CAC ص6.

## ف) مصفوفة الأثر (قواعد × كيانات)

| القاعدة | تمس | السلوك عند المخالفة |
|---|---|---|
| BR-01/02 | Extension.Calc% | 0 لSTD/IDD غير مقبول (تحقق إدخال) |
| BR-08 | CallRecord | سجل خطأ (مدة قصيرة) |
| BR-11 | Country/Area | بيانات ناقصة → أغلى تعرفة |
| BR-13/14 | Folio Posting | لا ترحيل / توحيد |
| BR-17 | Call Transfer | "does not allow" — رفض تطبيقي |
| BR-21 | Time Rate Slab | لا UI للتعديل أصلاً |
| BR-24 | Error → Folio | بقاؤها Unbilled حتى YES يدوي |
