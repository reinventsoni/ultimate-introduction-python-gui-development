import tkinter as tk
from tkinter import ttk


def button_pressed():
    # get the content of the entry
    # print(entry.get())
    entry_text = entry.get()

    # Update the text
    # label.config(text='Some Other Text') #may be removed in later versions
    # label.configure(text='Some Other Text')  #not preferred

    # label['text'] = 'Some Other Text'
    label['text'] = entry_text
    entry['state'] = 'disabled'
    print(label.configure())


def reset_label():
    label['text'] = 'Some Text'
    entry['state'] = 'enabled'


# window
window = tk.Tk()
window.title('Getting and Setting Widgets')
window.geometry('800x500')

# label widget
label = ttk.Label(master=window, text="My Label")
label.pack()

# entry widget
entry = ttk.Entry(master=window)
entry.pack()

# button widget
button = ttk.Button(master=window, text='Update Label', command=button_pressed)
button.pack()

# exercise button
reset_button = ttk.Button(master=window, text='Reset Label', command=reset_label)
reset_button.pack()

# run
window.mainloop()
