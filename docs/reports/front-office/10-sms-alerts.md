# 10 — نظام تنبيهات SMS (FOM-SMS — 14 ص)

> المصدر: `FN6i-NT-FOM-SMS.txt`. التعريف الرسمي: "The SMS Setup Sub Module of the Front Office module explains the various settings that are necessary to **send SMS to the guest and the authorized Supervisor** of the Property."
> **⚠️ التناقض التسميّ C-FO-02:** الدليل يسمي المنتج "**Fortune Next Enterprise 2.0**" ("SMS to be sent by Fortune Next Enterprise 2.0") بينما الحزمة كلها FortuneNext **6i** — تسريب تسمية إصدار تاريخية (مؤشر أن SMS وحدة أقدم لم تُحدّث تسميتها).

---

## 1. Mobile Master (§1)

تعريف مستقبلي الرسائل (Manager/Supervisor/Staff):

| الحقل | القيد الحرفي |
|---|---|
| Code | "maximum of **four alphanumeric characters**" |
| Name | "maximum of **30 alphanumeric characters**" |
| Mobile No. | "the **unique mobile number**... maximum of **15 numeric characters**" — فريدة! |

الاستخدامات المعلنة حرفياً: "events such as **Guest Complaints, Check-ins, In-house Guest Birthday/ Anniversary, High Bills, Room Transfer, Checkout and Hotel Statistics**" — (7 أحداث في المتن مقابل 8 في dropdown الخدمة — الثامن: High Bills **Value**).

Edit: بحث → تعديل (مثال الدليل: تغيير رقم موبايل) — Master CRUD كامل.

## 2. SMS Service Definition (§2) — الثمانية خدمات

**توجيه البنية**: خدمة واحدة → (Guest Status مرشح) + **متلّقون متعددون** (checkboxes) — "You can assign one or more SMS services to the tagged person."

| الخدمة | حقول خاصة | محتوى الرسالة (حرفياً) |
|---|---|---|
| a. Guest Complaints | Guest Status | Room# · Guest Name · Nationality · Guest Status · **Complaint** — يربط بخيار Log Complaints |
| b. Check-ins | Guest Status | Guest Name · Room# · Nationality · Guest Status |
| c. In-house Guest Birthday/Anniversary | Guest Status | **Greeting Type (Birthday/Anniversary)** · Guest Name · Property Name |
| d. High Bills | Guest Status | Guest Name · **Settlement amount for the day** · Room# · Nationality · Guest Status — "when a guest **exceeds the high bill value**" |
| e. Room Transfer | Guest Status | Guest Name · **Old Room# · New Room#** · Nationality · Guest Status |
| f. Checkouts | Guest Status | Room# · **Checkout Time** · Nationality · Guest Status — **"one hour prior to the guest checkout time"!** |
| g. High Bills Value | **High Bill Value** (المبلغ) | (تعريف العتبة — تُستهلك في d) |
| h. Hotel Statistics | **Start Time / End Time** | "Statistics For – Date · **Occ %** (Occupancy Percentage) · **Rm Rev** · **FB Rev** · FB Revenue–**Non F&B Revenue** · **Tel Rev** · **Bnq Rev** · **Coll** (Total Collection)" — إحصاء يومي كامل عبر قنوات SMS! + "The Statistics will be sent **only once in a day**" |

**بوابات الحقول المشروطة (حرفياً):**

- Guest Status: "enabled only if you choose any option **other than High Bills Value and Hotel Statistics**".
- High Bill Value: "enabled only if you choose **High Bills Value**".
- Start/End Time: "enabled only if you choose **Hotel Statistics**".

— ثلاثي enable-gating مثالي للتحويل إلى dynamic form.

**ملاحظة بيانات**: خدمة الإحصاء تكشف **تقسيم الإيراد الرسمي في نص الرسالة**: Room / F&B / **Non-F&B** / Telephone / Banquet + المجموع — مصفوفة تقسيم تُقابل تقارير Sales Summary by Outlet (103).

## 3. Department Checkout Alert (§3)

- "When the Guest is checking out, an SMS alert is sent to **relevant departments to look for consumption of items in that particular room**. For example; **room service will check the mini bar for any consumption**."
- الإدخال: "Enter person's name in Name column and phone number in Mobile # column" → Save.
- **الدلالة**: تنبيه استباقي عبر الإدارات قبل/أثناء الشطب لتحصيل الاستهلاك المتأخر (mini-bar) — جسر تشغيلي FO↔الإدارات عبر SMS بدل الورق (يقابل Room Instructions 41 الموجه للكاشير).

## 4. القرارات المعمارية

1. **الإخطار كوحدة مستقلة**: Mobile Master (مستقبلون) + Service Definition (حدث→متلقين) + Department Alert (توجيه إداري) — فصل نظيف Receive/Schedule/Route يقابله ERPNext **Notification** (Email/SMS/Webhook) مع قوالب Jinja — الحقول الخمسة لكل قالب تنقل حرفياً.
2. **عتبة High Bills Value مركزية**: الخدمة g ليست إشعاراً بل **تعريف threshold** تستهلكه d — عائلة العتبات تتوسع (IT Report 58 · High Bills 77 · High Bills Value SMS) — ثلاث عتبات فندقية: نظامية/ائتمانية/تنبيهية.
3. **نافذة الإرسال اليومية**: Hotel Statistics "once in a day" ضمن Start/End — جدولة + نافذة زمنية (Scheduled Notification with window) — يقابل ERPNext Scheduled Job + شرط.
4. **Checkout -1 ساعة**: توقيت الإرسال مشروط بحدث مستقبلي (وقت مغادرة متوقع) — يتطلب job دقيقي أو Scheduler قائم على حقل Departure Time (الموثق أيضاً في 68.2 الفرز!).
5. **UNK-082 (جديد)**: **آلية الإرسال/البوابة غير موثقة** — لا Gateway/SMS provider/queue في FOM-SMS؛ التوازي الوحيد: "SMS Queued" في Care-REP — استنتاج: بوابة مركزية خارج الوحدتين → قرار تنفيذ: SMS Gateway واحد + Queue موحد.
