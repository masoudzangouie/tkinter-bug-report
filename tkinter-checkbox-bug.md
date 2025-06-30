-----

# 🧩 باگی عجیب در Tkinter: وقتی چک‌باکس تیک نمی‌خوره، حتی با مقدار `True`\!

-----

✨ **مقدمه**

در حال توسعه‌ی یک برنامه با Tkinter بودم که با یک رفتار کاملاً غیرمنتظره مواجه شدم: داخل پنجره‌ی `toplevel`، چک‌باکسی که مقدار اولیه‌اش `True` بود، تیک نمی‌خورد\! حتی با بررسی مقدار `BooleanVar` با `print()`، مطمئن شدم مقدارش `True` است. اما چک‌باکس همچنان خالی نمایش داده می‌شد.

-----

🔍 **بازسازی مشکل**

یک برنامه برای آزمون و خطا به صورت زیر نوشتم تا حالت‌های مختلف را بررسی کنم. چک‌باکس‌هایی که داخل پنجره اصلی هستند، به درستی مقداردهی می‌شوند؛ اما چک‌باکس‌های داخل پنجره `toplevel` مقداردهی نمی‌شوند:

```python
'''this is a test'''

import tkinter as tk

root = tk.Tk()
root.title("Checkbutton Comparison")
root.geometry("300x100+100+200")

def open_toplevel():
    '''open toplevel window'''
    toplevel_window = tk.Toplevel()
    toplevel_window.title('Toplevel window')
    toplevel_window.geometry('300x200+100+350')
    # toplevel_window.attributes('-topmost', True)
    toplevel_window.grab_set()

    local_bool_var_1 = tk.BooleanVar(value=True)
    local_bool_var_2 = tk.BooleanVar(value=False)

    up_checkbox = tk.Checkbutton(toplevel_window, text='local_bool_var_1', variable=local_bool_var_1)
    up_checkbox.pack()

    tk.Checkbutton(toplevel_window, text='local_bool_var_2', variable=local_bool_var_2).pack()

    # test_btn = tk.Button(toplevel_window, text='Test', command=local_bool_var_1.get)
    # test_btn.pack()

bool_var_1 = tk.BooleanVar(value=True)
bool_var_2 = tk.BooleanVar(value=False)

check_on_top = tk.Checkbutton(root, text='bool_var_1', variable=bool_var_1)
check_on_top.pack()

check_bg_remove = tk.Checkbutton(root, text='bool_var_2', variable=bool_var_2)
check_bg_remove.pack()

tk.Button(root, text='open toplevel', command=open_toplevel).pack()

root.mainloop()
```

چک‌باکس اول که داخل پنجره `toplevel` است، به خاطر مقدار متغیر کنترلی‌ای که به آن وصل است، باید با تیک نمایش داده شود. اما در عمل، این چک‌باکس خالی ظاهر می‌شود حتی با مقدار `True`.

-----

🧪 **چه چیزهایی را تست کردم؟**

من همه‌ی راه‌حل‌های رایج و حتی پیشنهادی مستندات Tkinter را امتحان کردم:

  * استفاده از `.set(True)` بعد از ساخت متغیر
  * استفاده از `IntVar(value=1)` به‌جای `BooleanVar`
  * تغییر تم با `ttk.Style().theme_use('clam')`
  * استفاده از `.select()` یا `.state(['selected'])`
  * حتی `after()` برای تأخیر در اعمال وضعیت

❌ **هیچ‌کدام جواب نداد.**

-----

✅ **تنها راه‌حل واقعی (و عجیب\!)**

کاملاً تصادفی متوجه شدم که اگر از متغیر `BooleanVar` که متغیر کنترلی چک‌باکس اول است، در تابع رویداد کلیک یک دکمه استفاده کنم، حتی اگر آن دکمه هیچ‌وقت کلیک نشود، چک‌باکس به‌درستی مقدار `True` را نمایش می‌دهد\!

```python
test_btn = tk.Button(toplevel_window, text='Test', command=local_bool_var_1.get)
test_btn.pack()
```

با اضافه کردن این ویجت، چک‌باکس به‌درستی تیک خورد.

-----

🧠 **چرا این اتفاق می‌افتد؟**

به نظر می‌رسد Tkinter در بعضی شرایط، متغیرهایی که فقط به ویجت وصل شده‌اند ولی هیچ‌جا از آن‌ها استفاده نشده، را به‌درستی `bind` نمی‌کند. اما وقتی آن متغیر در یک تابع فقط با `get()` استفاده شود، Tkinter متوجه می‌شود که این متغیر واقعاً مهم است و مقدارش را به ویجت منتقل می‌کند.

-----

✨ **نتیجه‌گیری**

اگر در پنجره `toplevel` با چک‌باکسی مواجه شدید که مقدار `True` دارد ولی تیک نمی‌خورد، و هیچ‌کدام از راه‌حل‌های معمول جواب نداد، بدانید:

✅ تنها راه‌حل واقعی این است که از متغیر `BooleanVar` در یک تابع دیگر (مثل تابع رویداد کلیک یک دکمه) استفاده کنید، حتی اگر آن تابع اجرا نشود.

-----

✍️ **نوشته‌شده توسط:** Masoud Zangouie
📅 **تاریخ کشف:** 2025-06-30
