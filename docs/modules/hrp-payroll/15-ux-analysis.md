# 15 — تحليل تجربة المستخدم (UX Analysis) — وحدة HRP

> أنماط التفاعل الموثقة في HRP وما تعنيه للواجهة العربية-أولاً الجديدة.

---

## 1. الأنماط التفاعلية الكثيفة (فئة Office 2000s)

| النمط | الموضع | الدلالة |
|---|---|---|
| **Search-first navigation** | Personnel/Change Info/معظم REP: شاشة معايير → قائمة → سجل | Filter wizard |
| **Multi-tab record editors** | Statutory (4) · Supplementary (3) · F&F (sub-screens) | Tabs |
| **Grid-bulk editing** | Number Deduction Updation (جدول كل الموظفين + F8) · Attendance codes grid · Payroll Transaction (أكثر موظف) | Bulk editable tables |
| **Prompt-driven numbering** | Employee# بعد Save | auto-suggest |
| **Processing modal wizard** | Payroll Processing: نافذة تقدم + ACCEPT ED list أثناء الاحتساب! | Wizard steps حية |
| **Live totals** | Rate Master: "total salary amount will display on the right side" | computed footer |

## 2. الاختصارات الموثقة (Keyboard Map)

| المفتاح | الوظيفة | المواضع |
|---|---|---|
| F1 | استعراض قوائم الكودات | كل حقول الكود |
| F2/F3 | نسخ/لصق مبلغ المعاملة | Payroll Transaction |
| **F3** | **إعادة ترتيب أولويات الخصم** | ED Calculation |
| F4 | خصائص الحقل | Print Forms |
| **F5/F6** | إجازة يوم كامل/نصف | Leave Transaction |
| F8 | معلومات إضافية | Number Deduction |
| Ctrl+Arrows | تحريك الحقول المقفولة | Print Forms |

> قرار UX: تُستبدل بحوار حديث — لكن **F5/F6 (يوم/نصف)** تتحول إلى toggle يومي في منتقي الإجازات، و**Test Equation** يبقى زر تحقق فوري.

## 3. نقاط الألم الموثقة (التي يجب تحسينها لا استنساخها)

| الألم | الدليل | التحسين |
|---|---|---|
| **حضور فردي إلزامي** | "single employee at a time" | Bulk + import |
| **لا self-service** | لا شاشة موظف | ESS portal (إجازات/سلايب) |
| **80/132 عموداً** | كل REP | HTML/A4 + تصدير |
| **DBF export** | Form 3A | CSV/XLSX |
| **Denomination يدوي** | قيم Notes/Coins | محرك كسر تلقائي |
| **ACCEPT يتوقف على إدخال** | شاشة أثناء المعالجة | pre-run checklist يجهّز القيم قبل التنفيذ |
| **تعديل الرقم في شاشة جملة** | Number Deduction | inline edit موحد |
| **لا رسائل خطأ مفصلة** | V-section: غياب نصوص | رسائل عربية صريحة |

## 4. الأنماط الإيجابية الواجب الحفاظ عليها

| النمط | الدليل | البقاء |
|---|---|---|
| **Copy/Template** | ED Calc Copy + Salary Template + Rate Copy | استنساخ التعريفات |
| **Preview قبل الحفظ** | Starting Period Preview | معاينة فترات |
| **Test Equation / Check Formula** | محركان للتحقق | sandbox للمعادلات |
| **Audit بقيم قبل/بعد** | REP §19 | Versioning شفاف |
| **تقارير المواسم** | Birthday/Anniversary (Spouse/Children!) | dashboard تهنئة |
| **Skip rows في الطباعة** | Signature List وغيره | قابل للإسقاط عبر خيارات تقرير |

## 5. خصوصيات RTL/العربية

- حقول **Caste/Classification (SC/ST/OBC)** و**Religion** — سياق هندي: تُهيكل كحقول قابلة للتهيئة الديموغرافية حسب بلد التشغيل (فجوة سياق — راجع 17).
- أسماء ثنائية (Father's Name مركزي في النماذج الهندية) → **الاسم الرباعي العربي** (الاسم/الأب/الجد/العائلة) قرار نموذج.
- عملة الروبية/الدولار سياقية في Denomination → عملة قابلة للتهيئة.
- الأرقام الهندية (Crore/Lakh في SYS) لا تظهر في HRP نصاً — لكن百万/لاك عائلة SYS تُراعى في العرض.
