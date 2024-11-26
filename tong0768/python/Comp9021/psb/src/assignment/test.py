from tkinter import *

win = Tk()
win.geometry("300x300+500+400")

data = {'AAAAAA': 'Red', 'BBBB': 'Yellow', 'CCCCCCC': 'Orange', 'DDD': 'Purple'}
x = 0
y = 0
for k, v in data.items():
    btn = Button(win, text=k, bg=v)
    btn.place(x=x, y=y)
    y += 100
    x += 10

win.mainloop()
