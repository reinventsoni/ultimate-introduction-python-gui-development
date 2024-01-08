import tkinter as tk
from tkinter import ttk


def button_function():
    print('Button was pressed')


def say_hello():
    print('Hello')


# create a window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x500')

# tk.text
text1 = tk.Text(master=window)
text1.pack()

# ttk widgets
label = ttk.Label(master=window, text="This is a text")
label.pack()

# ttk Entry
entry = ttk.Entry(master=window)
entry.pack()

# exercise label
hello_label = ttk.Label(master=window, text='My Label')
hello_label.pack()

# ttk Button
button = ttk.Button(master=window, text='A Button', command=button_function)
button.pack()

# exercise
# add one more text label and a button with function that prints 'hello'
# the label should say 'my label' and be between entry widget and the button

# exercise button
hello_button = ttk.Button(master=window, text='Say Hello!', command=say_hello)
hello_button.pack()
# run
window.mainloop()
