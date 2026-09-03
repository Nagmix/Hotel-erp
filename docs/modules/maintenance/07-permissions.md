# 07 — الصلاحيات والأدوار (Permissions & Roles) — وحدة MNT

> **لا قسم User Rights في أي من الملفات الثلاثة** — خامس وحدة في العائلة (بعد CARE/SLM/MEM/TEL). الأدوار تُستنتج من نصوص تشغيلية متفرقة، وأخطرها: **استعلام يغيّر حالة الشكاوى (Complaint Status Q) بلا ضابط موثق**.

---

## 1. ما هو موثق نصاً

| الإشارة الصريحة | الدلالة | المصدر |
|---|---|---|
| "used by a **Supervisory User in the Maintenance Department** to prioritize and allocate the complaints/PM Tasks" | Job Order Generation = **دور إشرافي محصور** — الوحيد المسمّى في الوحدة | OPR ص22 |
| "The complaints can be raised by **any Department**" (المقدمة: "Complaints can be raised by any Department and from any location or for any room in the property") | **مصدر الشكاوى عام** — كل الأقسام مُبلِّغون | OPR ص2 |
| "The **user** can print a job request, if the ENG Module Attribute #1 is 'YES'" | بوابة سلوك عامة بلا تمييز مستخدم | OPR ص4 |
| Assign Shifts / Equipment Master / PM / Action Taken | لا قيد دور في أي منها | OPR كله |

## 2. الأدوار المستنتجة (Inferred Roles — 🔶)

| الدور المستنتج | الوظائف المرجحة له | الأساس |
|---|---|---|
| **مشرف الصيانة (Supervisory User)** | Job Order Generation (انتقاء + أولويات + إسناد + طباعة JS) — وربما Complaint Status Q | OPR ص22 (النص الوحيد) |
| **كاتب/موظف صيانة (Clerk)** | Register Complaints · Action Taken · PM Entry · Equipment Reading Entry | غياب أي قيد + طبيعة الإدخال اليومي |
| **مهندس مسؤول Equipment/Masters** | Equipment Master · PM Master · الـ12 ماستراً | غياب القيود |
| **مستخدم جدولة** | Assign Shifts (الروزنامة) | غياب القيود |
| **SysAdmin (عبر SYS)** | ENG Attributes #1/#2 + UDPF | نمط Module Attributes الموثق في SYS |
| **أي قسم (كل المستخدمين تقريباً)** | رفع شكاوى | OPR ص2 |

## 3. مخاطر الصلاحيات غير الموثقة ⭐

| الخطر | الوصف | الخطورة |
|---|---|---|
| **استعلام يُحرِّر بلا ضابط** | Complaint Status (Q) تسمح "change the status of the complaint. Enter the action taken... and select the priority level" (RPL ص7) — أي مستخدم للتقرير يملك إغلاق الشكاوى! | **عالية** |
| تغيير الحالة من مسارين | Action Taken **و** Query — ازدواج قنوات الإغلاق بلا فصل أدوار | متوسطة |
| تكلفة بلا موافقة | Cost Analysis تُدخل مبالغ (مزوّد + فئة) بلا موافقة موثقة | متوسطة |
| الورديات بلا مالك | Assign Shifts بلا قيد — من يملك روزنامة الفنيين؟ | منخفضة-متوسطة |
| حذف الماسترات | "cannot be deleted" **مضمّنة بنيوياً** (إيجابي!) — لكن Passive بلا صلاحية معرفة | منخفضة |

## 4. مقترح الأدوار عند إعادة البناء (للمرحلة 8)

```
Engineering Supervisor: (R/W) Complaints, Job Orders, Priorities, Assignments, ActionTaken-approve
Engineering Clerk:      (Create/Read) Complaints, Readings, PM Entry; (R/W) ActionTaken-draft
Equipment Manager:      (R/W) Equipment Master + AMC + Spares + PM Master
Roster Planner:         (R/W) Shifts Assignments; (R) Duty Chart
All-Department User:    (Create-only) Complaint registration + own-department filters
Auditor/Manager:        (Read) all reports incl. Spares and Cost, Resolution Time
```

- **القاعدة الذهبية المقترحة:** تعديل الحالة/الأولوية حكر على Supervisory/Owner-role — يغلق فجوة Query-as-Console.
- **المصدر المرجعي:** نمط الصلاحيات المشتق في POS/HRP (الأقوى توثيقاً) يُستعاد هنا — راجع 16 §6 للترجمة Frappe (Role Permissions).
