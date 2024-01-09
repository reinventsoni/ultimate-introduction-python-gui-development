import tkinter as tk
from tkinter import ttk

# application window setup
window = tk.Tk()
window.title('Canvas')
window.geometry('800x500')

# canvas
canvas = tk.Canvas(master=window, bg='white')
canvas.pack()


#
# canvas.create_rectangle((50, 20, 100, 200),
#                         fill='red',
#                         outline='green', width=10,
#                         dash=(1, 10))
# canvas.create_line((50,20,100,200),fill='blue')
# canvas.create_oval((0,0,100,100), fill='green')
# canvas.create_polygon((150,250, 100,200, 300,50))
# canvas.create_arc((0,0,100,100),
#                   fill='red', start=60, extent=145,
#                   style=tk.CHORD, outline='blue', width=5)

# canvas.create_text((5,5), text="This is some Text - the first section")
# canvas.create_text((150,50),
#                    text='This is some another Text',
#                    fill='green',
#                    width=50)

# draw widgets on canvas
# canvas.create_window((150,100), window=ttk.Label(window, text='This is Label Text to be displayed on Canvas'))
# canvas.create_window((150,200), window=ttk.Button(window, text='This is Label Text to be displayed on Canvas'))

# draw a basic paint app, draw line with mouse using event binding
def draw_on_canvas(event):
    x = event.x
    y = event.y
    canvas.create_oval((x - brush_size / 2, y - brush_size / 2,
                        x + brush_size / 2, y + brush_size / 2),
                       fill='black')


def brush_size_adjust(event):
    global brush_size
    if event.delta > 0:
        brush_size += 2
    else:
        brush_size -= 2

    brush_size = max(0, min(brush_size, 50))


brush_size = 2
canvas.bind('<Motion>', draw_on_canvas)
canvas.bind('<MouseWheel>', brush_size_adjust)

# run the application
window.mainloop()
