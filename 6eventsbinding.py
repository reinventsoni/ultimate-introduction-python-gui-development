import tkinter as tk
from tkinter import ttk


def get_pos(event):
    print(f'x:{event.x}, and y: {event.y}')


# define application window
window = tk.Tk()
window.title('Events and Event Binding')
window.geometry('600x500')

# widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(master=window)
entry.pack()

btn = ttk.Button(window, text='A Button')
btn.pack()

# events
# .bind('EVENT', 'Function') where EVENT = '<modifier:type:detail>' for e.g ALT-Keypress-a

# window.bind('<Alt-KeyPress-a>', lambda event:print(event))
# btn.bind('<Alt-KeyPress-a>', lambda event:print(event))
# window.bind('<Motion>', get_pos)
# text.bind('<Motion>', get_pos)
# window.bind('<KeyPress>', lambda event:print(f'A Key was pressed: {event.char}'))
entry.bind('<FocusIn>', lambda event:print('Entry Field has been selected'))
entry.bind('<FocusOut>', lambda event:print('Entry Field has been de-selected'))
# EVENT Details on this website:
# pythontutorial.net/tkinter/tkinter-event-binding

# Exercise:
# Print 'MouseWheel' when the user holds down shift, and uses the mousewheel wile text is selected.
text.bind('<Shift-MouseWheel>', lambda event: print('Mousewheel'))
# run
window.mainloop()
