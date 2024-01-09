import tkinter as tk
from tkinter import ttk


def button_func(str_var):
    print(str_var.get())


def button_fn(str_var):
    def inner_func():
        print('Function returning a function')
        print(str_var.get())
    return inner_func


# app, window
window = tk.Tk()
window.title('Buttons, Functional and Arguments')
window.geometry('600x400')

# widgets
entry_string=tk.StringVar(value='test')
entry = ttk.Entry(master=window, textvariable=entry_string)
entry.pack()

button = ttk.Button(master=window, text='Button 1 with Lambda Function', command=lambda:button_func(entry_string))
button.pack()

button2 = ttk.Button(master=window, text='Button 2 with Function returning Function',
                     command=button_fn(entry_string))
button2.pack()

# run
window.mainloop()
