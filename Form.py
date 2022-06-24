from tkinter import *
from tkinter import ttk
from Book import *

class Form():
    width = 500
    height = 500

    def __init__(self, title, book=("", "", "", "", "", "")) -> None:
        self.window = Tk()
        self.book = book

        self.widgets()

        self.window.title(title)
        self.window.geometry(f'{self.width}x{self.height}+100+100')
        self.window.resizable(False, False);
        self.window.mainloop()

    def widgets(self) -> None:
        # line 1
        f1 = Frame(self.window)
        f1.pack(side=TOP, pady=(30, 20))
        Label(f1, text="Name", width=10).pack(side=LEFT)
        name = Text(f1, height=1, width=35)
        name.insert('1.0', self.book[1])
        name.pack()
        
        # line 2
        f2 = Frame(self.window)
        f2.pack(side=TOP, pady=(0, 20))
        Label(f2, text="Author", width=10).pack(side=LEFT)
        author = Text(f2, height=1, width=35)
        author.insert('1.0', self.book[2])
        author.pack()

        # line 3
        f3 = Frame(self.window)
        f3.pack(side=TOP, pady=(0, 20))
        Label(f3, text="Year", width=10).pack(side=LEFT)
        year = Text(f3, height=1, width=35)
        year.insert('1.0', self.book[3])
        year.pack()

        # line 4
        f4 = Frame(self.window)
        f4.pack(side=TOP, pady=(0, 20))
        Label(f4, text="Piece", width=10).pack(side=LEFT)
        piece = Text(f4, height=1, width=35)
        piece.insert('1.0', self.book[4])
        piece.pack()

        # line 5
        f5 = Frame(self.window)
        f5.pack(side=TOP, pady=(0, 20))
        Label(f5, text="Price", width=10).pack(side=LEFT)
        price = Text(f5, height=1, width=35)
        price.insert('1.0', self.book[5])
        price.pack()

        # bottom bar
        f7 = Frame(self.window)
        f7.pack(side=BOTTOM, anchor=SE, fill=Y, pady=(0, 10), padx=(0, 10))
        btn = Button(f7, text="Ok", width=15)
        btn.pack(side=RIGHT)

        f6 = Frame(self.window)
        f6.pack(side=BOTTOM, fill=X, pady=(0, 10))
        ttk.Separator(f6, orient="horizontal").pack(fill=X)