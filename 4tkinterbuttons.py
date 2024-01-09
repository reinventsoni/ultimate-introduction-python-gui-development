import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.title('Buttons')
window.geometry('600x400')


# button
def button_func():
    print('A Basic Button')
    print(radio_var.get())


button_string = tk.StringVar(value='A Button with String Var')
button = ttk.Button(master=window, text='A Simple Button',
                    command=button_func, textvariable=button_string)
button.pack()

# check button
check_var = tk.IntVar(value=10)
check = ttk.Checkbutton(master=window, text='CheckBox1',
                        variable=check_var, command=lambda: print(check_var.get()),
                        onvalue=10,
                        offvalue=5)
check.pack()

# radio buttons
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(master=window, text='RadioButton1',
                         value='radio1', variable=radio_var)
radio2 = ttk.Radiobutton(master=window, text='RadioButton2',
                         value=2, variable=radio_var)
radio1.pack()
radio2.pack()


# exercise
# create another checkbutton and 2 radiobuttons
# radio button:
# values for the buttons are A and B
# ticking either prints the value of the checkbutton
# ticking the radio button, unchecks the checkbutton

# check button
# ticking the checbutton prints the value of teh radio button
# use tkinter var for booleans


def check1_command():
    print(radio_var1.get())


check1_var = tk.BooleanVar()
check1 = ttk.Checkbutton(master=window, text='CheckButton1',
                         onvalue=True, offvalue=False,
                         variable=check1_var, command=check1_command)
check1.pack()


def radio_check():
    print("Current Value of Checkbox is: ", check1_var.get())
    print("Unchecking the Checkbox Now")
    check1_var.set(False)


radio_var1 = tk.StringVar(value='A')
radio_button1 = ttk.Radiobutton(master=window, text='RadioButton1',
                                value='A', variable=radio_var1, command=radio_check)
radio_button2 = ttk.Radiobutton(master=window, text='RadioButton1',
                                value='B', variable=radio_var1, command=radio_check)
radio_button1.pack()
radio_button2.pack()
# run
window.mainloop()
