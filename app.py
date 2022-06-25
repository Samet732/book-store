from MainWindow import *
from Form import *
from Book import *
from Storage import *

refresh = True

class App():
    def __init__(self) -> None:
        self.storage = Storage("bookstore.sqlite")
        self.books = self.storage.getAll()
        self.selectedItem = None
        self.mainWindow = MainWindow(self.books, self.addBook, self.updateBook, self.deleteBook, self.itemSelected)
        self.mainWindow.window.mainloop()

    def itemSelected(self, event) -> None:
        global selectedItem
        temp = Book.tupleToBook(tuple(self.mainWindow.tree.item(self.mainWindow.tree.selection())['values']))
        temp.code = self.mainWindow.tree.item(self.mainWindow.tree.selection())['values'][0]
        selectedItem = temp

    def addBook(self) -> None:
        print('New Book')
        Form("Add Book", self.addBookCallback)

    def updateBook(self) -> None:
        print('Update Book')
        if selectedItem != None:
            Form("Update Book", self.updateBookCallback, Book.bookToTuple(selectedItem))

    def deleteBook(self) -> None:
        print('Delete Book')
        if selectedItem != None:
            self.storage.delete(selectedItem.code)
            self.refresh()

    def refresh(self) -> None:
        global refresh
        refresh = True
        self.mainWindow.window.destroy()

    def addBookCallback(self, b: Book) -> None:
        self.storage.add(b)
        self.refresh()

    def updateBookCallback(self, b: Book) -> None:
        self.storage.update(b)
        self.refresh()

if __name__ == '__main__':
    while refresh:
        refresh = False
        app = App()