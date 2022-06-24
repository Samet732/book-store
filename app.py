import code
from MainWindow import *
from Form import *
from Book import *
from Storage import *

def itemSelected(event):
    global selectedItem
    temp = Book.tupleToBook(tuple(mainWindow.tree.item(mainWindow.tree.selection())['values']))
    temp.code = mainWindow.tree.item(mainWindow.tree.selection())['values'][0]
    selectedItem = temp

def addBook():
    print('New Book')
    Form("Add Book", storage.add)
    refresh()

def updateBook():
    print('Update Book')
    if selectedItem != None:
        Form("Update Book", storage.update, Book.bookToTuple(selectedItem))
        refresh()

def deleteBook():
    print('Delete Book')
    if selectedItem != None:
        storage.delete(selectedItem.code),
        refresh()


def refresh() -> None:
    global books
    books = storage.getAll()
    mainWindow.books = books
    mainWindow.frame.destroy()
    mainWindow.widgets()

storage = Storage("bookstore.sqlite")
books = storage.getAll()
selectedItem = None
mainWindow = MainWindow(books, addBook, updateBook, deleteBook, itemSelected)
mainWindow.window.mainloop()