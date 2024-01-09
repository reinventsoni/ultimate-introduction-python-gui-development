import tkinter as tk
from tkinter import ttk

# setting up application window
window = tk.Tk()
window.geometry('600x400')
window.title('ComboBox and SpinBox')

# Combobox
items = ['Ice Cream', 'Brocoli', 'Pizza']
food_string = tk.StringVar(value=items[0])
cbox = ttk.Combobox(master=window, textvariable=food_string, values=items)
# cbox['values']=items
# cbox.configure(values=items)
cbox.pack()
# combobox events
cbox.bind('<<ComboboxSelected>>',
          lambda event:
          combo_label.configure(text=f'Selected Value:  {food_string.get()}'))
combo_label = ttk.Label(window, text='A Label')
combo_label.pack()

# Spinbox
spin_var = tk.IntVar(value=1)
spin = ttk.Spinbox(master=window,
                   from_=0, to=20, increment=2,
                   textvariable=spin_var,
                   command=lambda:print(f"Selected Value in Spin Box is: {spin_var.get()}"))
# spin['value'] = [1, 2, 3, 4, 5]

spin.bind('<<Increment>>', lambda event: print('Spin Box, Up'))
spin.bind('<<Decrement>>', lambda event: print('Spin Box, Down'))
spin.pack()

# exercise
letters = ['A','B','C','D','E']
spin1_var = tk.StringVar(value=letters[0])
spin1 = ttk.Spinbox(master=window, values=letters, textvariable=spin1_var)
spin1.bind('<<Decrement>>', lambda event: print(f'Spin Box Down Event, Value was: {spin1_var.get()}'))
spin1.pack()
# run
window.mainloop()
