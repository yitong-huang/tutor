import tkinter as tk
from PIL import Image, ImageTk
from profession import *
from unit_widget import UnitGui
from unit import Unit
from option_panel import Options


class App:
    def __init__(self, root):

        self.__win = root
        self.__coin_text = tk.StringVar()
        self.__coin_text.set('0')

        root.geometry('600x450+300+400')
        info_frame = tk.Frame(root)
        battle_frame = tk.Frame(root, width=400, height=450, highlightbackground="black", highlightthickness=1)
        info_frame.pack(side=tk.LEFT)
        battle_frame.pack(side=tk.LEFT)

        coin_frame = tk.Frame(info_frame)
        coin_frame.grid(row=0, column=0, sticky='nw')
        coin_frame.grid_propagate(0)

        coin_img = Image.open('coin.png')
        coin_img = coin_img.resize((40, 40), Image.ANTIALIAS)
        coin_label = tk.Label(coin_frame)
        coin_label.photo = ImageTk.PhotoImage(coin_img)
        coin_label.config(image=coin_label.photo)
        coin_label.pack(side=tk.LEFT)
        coin_text = tk.Label(coin_frame)
        coin_text.config(textvariable=self.__coin_text)
        coin_text.pack(fill=tk.BOTH, side=tk.RIGHT)

        log_frame = tk.Frame(info_frame)
        log_frame.grid(row=1, column=0, sticky='nw')
        log_title_label = tk.Label(log_frame, text="Game Log")
        log_title_label.pack(anchor="w")
        log_text = tk.Text(log_frame, state=tk.DISABLED, width=30)
        scroll = tk.Scrollbar(log_frame)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        scroll.config(command=log_text.yview)
        log_text.config(yscrollcommand=scroll.set)
        self.__log_text = log_text
        log_text.pack(pady=10)

        menu_frame = tk.Frame(info_frame, width=200, height=40)
        menu_frame.grid(row=2, column=0)

        start_btn = tk.Button(menu_frame, text='Restart', command=self.restart)
        start_btn.pack(side=tk.LEFT)
        option_btn = tk.Button(menu_frame, text='Options', command=self.options)
        option_btn.pack(side=tk.LEFT, padx=10)
        exit_btn = tk.Button(menu_frame, text='Exist', command=self.exit)
        exit_btn.pack(side=tk.LEFT)

        self.__player_units = []
        self.__ai_units = []

        for row in range(0, 3):
            for column in range(0, 2):
                prof = Profession.WARRIOR if (row + column) % 2 == 0 else Profession.TANKER
                name_pre = "player-" if column == 0 else "ai-"
                unit = UnitGui(battle_frame, Unit(name_pre + str(row), prof), self, True if column == 1 else False)
                if column == 0:
                    self.__player_units.append(unit)
                else:
                    self.__ai_units.append(unit)
                unit.place(y=(150 * row), x=(250 * column))

        self.__select_player = None
        self.__attack_ai = None

    def restart(self):
        self.__coin_text.set("30")

    def exit(self):
        self.__win.destroy()

    def players_un_select(self):
        for player in self.__player_units:
            player.un_select()

    def attack(self, unit):
        self.__log_text['state'] = tk.NORMAL
        self.__log_text.insert(tk.END, "[Game Message] " + self.__select_player.get_unit().getName() + " attacked "
                               + unit.get_unit().getName() + " damage \n")
        self.__log_text['state'] = tk.DISABLED

    def options(self):
        panel = tk.Tk()
        Options(panel, self)
        panel.mainloop()

    def select_to_attack(self, unit):
        self.__select_player = unit


win = tk.Tk()
App(win)
win.mainloop()
