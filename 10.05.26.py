'''import tkinter
win = tkinter.Tk()
canvas = tkinter.Canvas(win, bg='black', width=1000, height=300)
canvas.pack()
win.mainloop()

import tkinter
win = tkinter.Tk()
canvas = tkinter.Canvas(win, bg='#0ff', width=700, height=700)
canvas.create_oval((300,300), (500, 500), fill='yellow')
canvas.create_line((0, 0), (100, 200), (300, 300), (200, 100), (0, 0), fill='black')
canvas.pack()
win.mainloop()'''

'''import tkinter as tk

def move_by_keys(event):
    info_coords = canvas.coords(oval)
    x = info_coords[0]
    y = info_coords[1]
    label.config(text=str(x) + ' ' + str(y))
    if event.keysym == 'Up':
        canvas.move(oval, 0, -20)
    elif event.keysym == 'Down':
        canvas.move(oval, 0, 20)
    elif event.keysym == 'Left':
        canvas.move(oval, -20, 0)
    elif event.keysym == 'Right':
        canvas.move(oval, 20, 0)


win = tk.Tk()
label = tk.Label(win, text='INGINIRIUM')
label.pack()
canvas = tk.Canvas(win, bg='#fff', width=700, height=700)
oval = canvas.create_oval((300, 300), (400, 400), fill='yellow')
canvas.pack()
win.bind("<KeyPress>", move_by_keys)
win.mainloop()'''

import tkinter
win = tkinter.Tk()
canvas = tkinter.Canvas(win, bg='white', width=400, height=400)
'''canvas.create_line((50, 0), (50, 400), fill='black')
canvas.create_line((100, 0), (100, 400), fill='black')
canvas.create_line((150, 0), (150, 400), fill='black')
canvas.create_line((200, 0), (200, 400), fill='black')
canvas.create_line((250, 0), (250, 400), fill='black')
canvas.create_line((300, 0), (300, 400), fill='black')
canvas.create_line((350, 0), (350, 400), fill='black')
canvas.create_line((400, 0), (400, 400), fill='black')'''
for i in range(50, 400, 50):
    canvas.create_line((i, 0), (i, 400), fill='black')
    canvas.create_line((0, i), (400, i), fill='black')
'''canvas.create_line((0, 50), (400, 50), fill='black')
canvas.create_line((0, 100), (400, 100), fill='black')
canvas.create_line((0, 150), (400, 150), fill='black')
canvas.create_line((0, 200), (400, 200), fill='black')
canvas.create_line((0, 250), (400, 250), fill='black')
canvas.create_line((0, 300), (400, 300), fill='black')
canvas.create_line((0, 350), (400, 350), fill='black')
canvas.create_line((0, 400), (400, 400), fill='black')'''
canvas.pack()
win.mainloop()
