from tkinter import *
from tkinter import ttk

class MainWindow():
    width = 1200
    height = 700

    def __init__(self, books, newBookF, updateBookF, delBookF) -> None:
        self.books = books
        self.newBookF = newBookF
        self.updateBookF = updateBookF
        self.delBookF = delBookF
        self.window = Tk()
        
        self.widgets()

        self.window.title('Book Store')
        self.window.geometry(f'{self.width}x{self.height}+50+50')
        self.window.minsize(width=500, height=500)
        self.window.mainloop()

    def widgets(self) -> None:
        frame = Frame(self.window)
        frame.pack(side=TOP, anchor=NW, padx=(5, 5), pady=(5, 5))

        newBook = Button(frame, text="Add", command=self.newBookF, width=25)
        newBook.pack(side=LEFT, padx=(0, 5))
        updateBook = Button(frame, text="Update", command=self.updateBookF, width=25)
        updateBook.pack(side=LEFT, padx=(0, 5))
        delBook = Button(frame, text="Delete", command=self.delBookF, width=25)
        delBook.pack(side=LEFT)

        columns = ('code', 'name', 'author', 'year', 'piece', 'price')
        self.tree = ttk.Treeview(self.window, columns=columns, show='headings')
        self.tree.heading('code', text='Code')
        self.tree.heading('name', text='Name')
        self.tree.heading('author', text='Author')
        self.tree.heading('year', text='Year')
        self.tree.heading('piece', text='Piece')
        self.tree.heading('price', text='Price')

        scrollbar = ttk.Scrollbar(self.window, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)

        for i in self.books:
            self.tree.insert('', END, values=i)
        self.tree.pack(fill=BOTH, expand=True)