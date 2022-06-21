from tkinter import *
from turtle import width

class Form():
    width = 500
    height = 500

    def __init__(self, title) -> None:
        self.window = Tk()

        self.widgets()

        self.window.title(title)
        self.window.geometry(f'{self.width}x{self.height}+100+100')
        self.window.minsize(width=self.width, height=self.height)
        self.window.maxsize(width=self.width, height=self.height)
        self.window.mainloop()

    def widgets(self) -> None:
        f1 = Frame(self.window)
        f1.pack(side=TOP)