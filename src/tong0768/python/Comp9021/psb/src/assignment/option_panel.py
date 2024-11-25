from tkinter import *


class Options:
    def __init__(self, win, app):
        self.__app = app

        player1_name_label = Label(win, text="player1 name:")
        player1_name_label.grid(row=0, column=0)
        player1_name_entry = Entry(win)
        player1_name_entry.grid(row=0, column=1)

        player2_name_label = Label(win, text="player2 name:")
        player2_name_label.grid(row=0, column=2)
        player2_name_entry = Entry(win)
        player2_name_entry.grid(row=0, column=3)

        player3_name_label = Label(win, text="player3 name:")
        player3_name_label.grid(row=0, column=4)
        player3_name_entry = Entry(win)
        player3_name_entry.grid(row=0, column=5)

        ai1_name_label = Label(win, text="ai1 name:")
        ai1_name_label.grid(row=0, column=6)
        ai1_name_entry = Entry(win)
        ai1_name_entry.grid(row=0, column=7)

        ai2_name_label = Label(win, text="ai2 name:")
        ai2_name_label.grid(row=0, column=8)
        ai2_name_entry = Entry(win)
        ai2_name_entry.grid(row=0, column=9)

        ai3_name_label = Label(win, text="ai3 name:")
        ai3_name_label.grid(row=0, column=10)
        ai3_name_entry = Entry(win)
        ai3_name_entry.grid(row=0, column=11)

        confirm_btn = Button(win, text="OK")
        confirm_btn.grid(row=1, column=11, pady=10)


