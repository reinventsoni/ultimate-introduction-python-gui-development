import tkinter as tk
from tkinter import ttk


def set_text():
    print(string_var.get())
    string_var.set('Button Pressed')


# window
window = tk.Tk()
window.title('Tkinter Variables')
window.geometry('800x500')

# tkinter Variable
string_var = tk.StringVar()

# widgets
label = ttk.Label(master=window, text='Label Text', textvariable=string_var)
label.pack()

entry = ttk.Entry(master=window, textvariable=string_var)
entry.pack()

button = ttk.Button(master=window, text='Press Me', command=set_text)
button.pack()

# exercise
# create 2 entry fields and 1 labels, they should all be connected by a StringVar
# set a start value of test
another_string_var = tk.StringVar()
another_string_var.set('test')

entry1 = ttk.Entry(master=window, textvariable=another_string_var)
entry1.pack()

entry2 = ttk.Entry(master=window, textvariable=another_string_var)
entry2.pack()

label2 = ttk.Label(master=window, text='Another Label', textvariable=another_string_var)
label2.pack()

# run
window.mainloop()
