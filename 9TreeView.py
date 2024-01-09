import tkinter as tk
from tkinter import ttk
from random import choice

# Create Application Window
window = tk.Tk()
window.title('TreeView: Tables')
window.geometry('800x500')

# data
first_names = ['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Henry', 'Lisa', 'Anna', 'Lisa']
last_names = ['Smith', 'Brown', 'Wilson', 'Thomson', 'Cook', 'Taylor', 'Walker', 'Clark']

# TreeView Table
table = ttk.Treeview(master=window, columns=('first', 'last', 'email'), show='headings')
table.heading('first', text='First Name')
table.heading('last', text='Surname')
table.heading('email', text='Email Address')
table.pack(fill='both', expand=True)

# Insert Values into Table
# table.insert(parent='', index=0, values=('John', 'Doe', 'JohnDoe@gmail.com'))
for i in range(100):
    first = choice(first_names)
    last = choice(last_names)
    email = f"{first}_{last}@email.com"
    data = (first, last, email)
    table.insert(parent='', index=i, values=data)


# table.insert(parent='', index=tk.END, values=('XXX', 'YYYY', 'ZZZ'))

# table events and table items
def item_select(_):
    # print(table.selection())
    for item in table.selection():
        print(table.item(item)['values'])


def item_delete(event):
    print('Delete Item detected')
    for item in table.selection():
        table.delete(item)


# table.bind('<<TreeviewSelect>>', lambda event: print(event))
# table.bind('<<TreeviewSelect>>', lambda event: print(table.selection()))  # shows item IDs
table.bind('<<TreeviewSelect>>', item_select)
table.bind('<Delete>', item_delete)


# Run the Application
window.mainloop()
