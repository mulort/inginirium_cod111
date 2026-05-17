import tkinter
import random

def prepare_and_start():
    global player

    canvas.delete("all")
    player_pos = (random.randint(1, N_X - 1) * step,
                  random.randint(1, N_Y - 1) * step)
    player = canvas.create_image(
        (player_pos[0], player_pos[1]), image=player_pic, anchor='nw')
    label.config(text='найди выход!')
    win.bind("<KeyPress>", key_pressed)

def move_wrap(obj, move_x, move_y):
    xy = canvas.coords(obj)
    canvas.move(obj, move_x, move_y)
    print(xy)
    if xy[0] <= 0:
        canvas.move(obj, width, 0)
    if xy[0] >= width:
        canvas.move(obj, -width, 0)
    if xy[1] <= 0:
        canvas.move(obj, 0, height)
    if xy[1] >= height:
        canvas.move(obj, 0, -height)

def key_pressed(event):
    if event.keysym == 'Up':
        move_wrap(player, 0, -step)
    elif event.keysym == 'Down':
        move_wrap(player, 0, step)
    elif event.keysym == 'Right':
        move_wrap(player, step, 0)
    elif event.keysym == 'Left':
        move_wrap(player, -step, 0)

win = tkinter.Tk()

step = 32
N_X = 10
N_Y = 10
width = step * N_X
height = step * N_Y

player_pic = tkinter.PhotoImage(file=r'spritepaint (2).png')

canvas = tkinter.Canvas(win, bg='#FCAB08',
                        width=width, height=height)

player_pos = (random.randint(0, N_X - 1) * step,
              random.randint(0, N_Y - 1) * step)

print(player_pos)
label = tkinter.Label(win, text="Не попадись!")
restart = tkinter.Button(win, text="Начать заново",
                         command=prepare_and_start)

restart.pack()
label.pack()
canvas.pack()
prepare_and_start()
win.bind("<KeyPress>", key_pressed)
win.mainloop()