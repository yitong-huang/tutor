import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class UnitGui(tk.Frame):

    def __init__(self, parent, unit, app, is_ai=False):
        tk.Frame.__init__(self, parent)
        self.__app = app
        self.__unit = unit
        self.__is_ai = is_ai

        img = Image.open(unit.getProfession().value + ".png")
        img = img.resize((100, 100), Image.ANTIALIAS)
        img_label = tk.Label(self)
        img_label.photo = ImageTk.PhotoImage(img)
        img_label.config(image=img_label.photo)
        img_label.bind('<Button-1>', self.selected)
        img_label.grid(row=0, column=0, rowspan=2)
        hp_bar = ttk.Progressbar(self, length=100, mode='determinate', orient=tk.HORIZONTAL)
        hp_bar['value'] = unit.getCurrentHp() / unit.getMaxHp() * 100
        hp_bar.grid(row=2, column=0)

        attack_btn = tk.Button(self, text='Attack', command=self.click_attack)
        self.__attack_btn = attack_btn
        heal_btn = tk.Button(self, text='Heal')
        self.__heal_btn = heal_btn

    def selected(self, event):
        print(event)
        if not self.__is_ai:
            self.__app.players_un_select()
            self.__attack_btn.grid(row=0, column=1)
            self.__heal_btn.grid(row=1, column=1)
        else:
            self.__app.attack(self)

    def click_attack(self):
        self.__app.select_to_attack(self)

    def un_select(self):
        self.__attack_btn.grid_forget()
        self.__heal_btn.grid_forget()

    def refresh(self):
        print(self.__unit)

    def get_unit(self):
        return self.__unit

