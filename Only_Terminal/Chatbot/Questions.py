তুমি এখন যেহেতু `leave_policy.csv` ফাইল থেকে একটি চ্যাটবট তৈরি করেছো, তুমি মূলত যেসব প্রশ্ন করতে পারো, সেগুলো ফাইলের তথ্য অনুযায়ী হওয়া উচিত। নিচে কিছু উদাহরণ প্রশ্ন দিচ্ছি যেগুলো তুমি করতে পারো:

---

### ✅ **Leave Policy সম্পর্কিত প্রশ্ন:**

1. `একজন কর্মচারী বছরে কত দিন ছুটি পায়?`
2. `Employee001 কতদিন ছুটি নিয়েছে?`
3. `২০২4 সালে কে কে ২০ দিনের ছুটি নিয়েছে?`
4. `Employee004 কি টাইপের ছুটি নিয়েছে?`
5. `সবচেয়ে বেশি ছুটি কে নিয়েছে?`
6. `যাদের ছুটি বাকি আছে তাদের নাম বলো।`
7. `Employee002 এর ছুটি ব্যবহারের ইতিহাস বলো।`

---

### ✅ **General / Summary টাইপ প্রশ্ন:**

1. `ছুটির উপর সারাংশ দাও।`
2. `সব কর্মচারীর ছুটির সংক্ষিপ্ত বিবরণ দাও।`
3. `সকল কর্মচারীর ছুটি গ্রহণের গড় কত?`

---

### ✅ **Yes/No টাইপ প্রশ্ন:**

1. `Employee003 কি ছুটি নিয়েছে?`
2. `Employee005 কি Paid Leave নিয়েছে?`

---

### ✅ **Instruction টাইপ প্রশ্ন:**

1. `ছুটির ডেটা টেবিল আকারে দাও।`
2. `একটি Excel summary তৈরি করে দাও।` (এটা আসলে বাস্তব Excel না, তবে টেবিল আকারে দিতে পারে)

---

### 💡 **Advanced Prompt Tips:**

> ✅ তুমি চাইলে প্রশ্নের সাথে নির্দিষ্ট employee ID, leave type, year, taken days, বা allowed days উল্লেখ করতে পারো।
> ✅ সহজ ভাষায় জিজ্ঞেস করলেও কাজ করবে:
>
> * “কতদিন ছুটি পাওয়া যায়?”
> * “নোমান কতদিন ছুটি নিয়েছে?”
> * “২০২৪ সালে মাতৃত্বকালীন ছুটি কতো?”

---



🧑 আপনি: hi
🤖 Bot:  Hello! Here's a summary of the leaves taken by employees in 2024:

1. Paid Leave: Fahim Hasan (1) - 13/20 days, Moushumi Begum (11) - 15/20 days, Salma Akter (21) - 14/20 days, Tania Chowdhury (20) - 15/20 days, Sadia Rahman (26) - 3/20 days, Rafiqur Rahman (15) - 7/20 days, Nabila Islam (33) - 2/10 days, Fahim Hasan (28) - 9/20 days, Sadia Rahman (29) - 2/20 days, Rafiqur Rahman (30) - 7/20 days, Moushumi Begum (41) - 19/20 days.

2. Maternity Leave: Karim Ahmed (2) - 82/180 days, Arif Hossain (6) - 64/180 days, Nabila Islam (7) - 174/180 days, Nabila Islam (8) - 59/180 days, Fahim Hasan (9) - 48/180 days, Sadia Rahman (13) - 123/180 days, Arif Hossain (17) - 47/180 days, Nabila Islam (42) - 151/180 days.

3. Sick Leave: Karim Ahmed (23) - 10/10 days, Rahim Khan (14) - 8/10 days, Rahim Khan (27) - 9/10 days, Fahim Hasan (28) - 9/10 days, Sadia Rahman (31) - 9/10 days, Arif Hossain (37) - 4/10 days, Karim Ahmed (38) - 125/180 days, Sadia Rahman (39) - 4/10 days, Rafiqur Rahman (40) - 33/180 days, Moushumi Begum (41) - 2/10 days, Tania Chowdhury (46) - 10/10 days, Karim Ahmed (47) - 5/10 days, Rafiqur Rahman (49) - 5/10 days.

If you have a specific question about these leaves or need more information, please let me know!

🧑 আপনি: একজন কর্মচারী বছরে কত দিন ছুটি পায়?
🤖 Bot:  এই তালিকার অনুসরণ করে নিয়ে, কোন কর্মচারীকে বছরে কত দিন ছুটি পাই হলে নেই জানাতে যায়। অন্যদিগে ছুটি নেই হলে, ০ (Zero) দিন ছুটি পাবে। কোন কর্মচারী যে সে অপরের কর্মচারীদের তালিকায় কিছু ক্ষেত্রে থাকে, সে ভাগ বা টাইম বৈঠক উপাদান হয়ে এই প্রশ্নে জুড়ে যাবে না।


