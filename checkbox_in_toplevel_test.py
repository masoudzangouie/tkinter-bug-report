
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

    test_btn = tk.Button(toplevel_window, text='Test', command=local_bool_var_1.get)
    test_btn.pack()


bool_var_1 = tk.BooleanVar(value=True)
bool_var_2 = tk.BooleanVar(value=False)


check_on_top = tk.Checkbutton(root, text='bool_var_1', variable=bool_var_1)
check_on_top.pack()

check_bg_remove = tk.Checkbutton(root, text='bool_var_2', variable=bool_var_2)
check_bg_remove.pack()

tk.Button(root, text='open toplevel', command=open_toplevel).pack()

root.mainloop()
