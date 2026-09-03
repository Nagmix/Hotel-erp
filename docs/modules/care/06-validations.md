# 06 — قواعد التحقق والقيود (Validations) — وحدة Care

> **V-CA-01..16**: قيود الإدخال والتحقق الموثقة نصاً أو المستنتجة من الرسائل المذكورة، مع درجة التوثيق (نصي/مستنتج).

---

## 1. قيود موثقة نصاً

| # | القاعدة | الرسالة/السلوك | المصدر |
|---|---|---|---|
| V-CA-01 | الشهر/السنة في الروستر ≥ الحالي | "(Note: The month and year should be **greater than or equal to** the current month and year)" | OPR ص6 |
| V-CA-02 | لا حذف ورديات تواريخ ماضية | "You **cannot delete shifts for the past dates**" | OPR ص9 |
| V-CA-03 | تعديل الروستر للأيام المستقبلية فقط | "alterations can be made **only to the future days of the current month**" | OPR ص14 |
| V-CA-04 | الطوابق تتطلب ورديات معرفة | رسالة على الشاشة عند محاولة تعريف طوابق بلا ورديات | OPR ص11 |
| V-CA-05 | لا دخول بلا روستر للشهر | رسالة خطأ **'Schedule Not Entered'** | OPR ص20 |
| V-CA-06 | تنبيه وردية غير معينة (سماح) | "alert message" + متابعة الدخول | OPR ص19 |
| V-CA-07 | تنبيه عطلة/إجازة (سماح بـ Yes) | "alert message that the selected date is a holiday/leave" | OPR ص20 |
| V-CA-08 | اختيار الوردية مشروط | "enabled **only if** the employee is not assigned any shift in the monthly roster **or** if the employee is trying to login to a shift that is not assigned to him" + "The available shifts **during the login time** will be listed" | OPR ص24 |
| V-CA-09 | Special Instructions ≤ 25 خانة | "maximum of **25 alphanumeric characters**" | OPR ص36 |
| V-CA-10 | الطلب المسبق (Request/Incidents) لخيار ROOM فقط | "This option is **not available** for 'UNOCCUPIED ROOM' or 'OTHER AREA'" | OPR ص51 |
| V-CA-11 | إلغاء/إيقاف للمهام غير المبدوءة | "if you want to cancel / stop the tasks that are **not yet started**" | OPR ص49 |
| V-CA-12 | لا تعديل اسم الموظف | "You **cannot edit the employee name**" | OPR ص24 SET |
| V-CA-13 | Response Time Analysis: لا Details مع Yearly | "(Note: The Details option will **not be available** if the time frame Yearly is selected)" | REP ص14 |
| V-CA-14 | Repeated Issues/Incidents by Floor: لا Floor مع Other Locations | "The floor option will **not be available** if you select Other Locations option" | REP ص42/45 |
| V-CA-15 | Task List: لا فلتر Main مع All Departments | "If you select All Departments, you will **not get the option** to select the task type from the Main field" | REP ص70 |
| V-CA-16 | Top Tasks: Open يُحسب بـ Assigned Date حصراً | "If you select the Open Complaint Status, Task status can be viewed **only by assigned date**" | REP ص38 |

## 2. قيود مستنتجة (من الرسائل الموثقة للسلوك)

| # | القاعدة | الأساس الاستدلالي | درجة الثقة |
|---|---|---|---|
| V-CA-17 | الرد SMS يُقبل من رقم الموظف المسجل فقط (Mobile# في Login) | رسالة `TASK #1 IS NOT ASSIGNED TO YOU. WORK NOT STARTED` تعني تحقق ملكية الرقم/المهمة | عالية |
| V-CA-18 | الخروج يتطلب إغلاق/نقل كل المهام | "Once all the assigned tasks have been **closed or transferred**... and feedback entered... can logout" | عالية (نص إرشادي — آلية الإجبار غير موثقة) |
| V-CA-19 | Multi Task يتطلب مهام معرفة مسبقاً في Task Definition | بحث تدريجي داخل "department's task" القائمة | عالية |
| V-CA-20 | Room# يجب أن يكون من PMS (لا إدخال حر) | F1 من Locations retrieved from PMS Maintenance | عالية |
| V-CA-21 | Group SMS يتطلب نصاً غير فارغ | "Type the message in the SMS Message Text field and click Send" (بلا حد طول موثق!) | متوسطة — **الحد الأقصى لطول SMS غير موثق** (UNK) |
| V-CA-22 | أرقام Group SMS الخارجية تقبل الصيغة الرقمية | "enter extra mobile numbers other than those available in the CARE system" | متوسطة |
| V-CA-23 | استرجاع الموظف المحذوف متاح من نفس التصنيف | مسار Help→Deleted List داخل Designation | متوسطة |

## 3. الاكتشافات التحليلية

1. **نمط التحقق ثلاثي الأغراض** في Care: (أ) **منع بنيوي** (V-CA-05/12: لا بديل)، (ب) **تنبيه مع سماح** (V-CA-06/07: قرارات بشرية)، (ج) **تعطيل تدريجي للواجهة** (V-CA-13/14/15: خيارات تختفي بتغير السياق) — آخرها نمط UX ناضج يستحق الترجمة الحرفية في إعادة البناء (F-CA-7).
2. **حصانة زمنية مصغرة**: قيود الماضي (V-CA-02/03) هي "عائلة التجميد" الخامسة في المشروع (FO يومي، MGT شهري، FAS سنوي، HRP رواتب، **Care روستري**) — راجع 12-integrations §4.
3. **غيابات ملحوظة**: لا تحقق موثق لصيغ الموبايل/البيجر، ولا لتفرد رقم الموبايل بين موظفي الوردية (خطر الازدواج إن سُمح برقمين لنفس الوردية — يُسجل كخطر تصميم D-CA-R1).
4. **العلاقة مع IVR**: أكواد IVR موجودة في Task List بلا أي تحقق موثق لتفرد الكود أو صيغته (GAP-CA-D04).
