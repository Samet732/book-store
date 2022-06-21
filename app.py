from MainWindow import *
from Book import *

books = [
    Book.bookToTuple(Book("c++", "Samet", "2012", "10", "60")),
    Book.bookToTuple(Book("python 3", "Samet", "2015", "1", "100")),
    Book.bookToTuple(Book("java", "Samet", "2013", "5", "85")),
    Book.bookToTuple(Book("c++", "Samet", "2012", "10", "60")),
    Book.bookToTuple(Book("python 3", "Samet", "2015", "1", "100")),
    Book.bookToTuple(Book("java", "Samet", "2013", "5", "85")),
    Book.bookToTuple(Book("c++", "Samet", "2012", "10", "60")),
    Book.bookToTuple(Book("python 3", "Samet", "2015", "1", "100")),
    Book.bookToTuple(Book("java", "Samet", "2013", "5", "85")),
    Book.bookToTuple(Book("c++", "Samet", "2012", "10", "60")),
    Book.bookToTuple(Book("python 3", "Samet", "2015", "1", "100")),
    Book.bookToTuple(Book("java", "Samet", "2013", "5", "85")),
    Book.bookToTuple(Book("c++", "Samet", "2012", "10", "60")),
    Book.bookToTuple(Book("python 3", "Samet", "2015", "1", "100")),
    Book.bookToTuple(Book("java", "Samet", "2013", "5", "85")),
    Book.bookToTuple(Book("c++", "Samet", "2012", "10", "60")),
    Book.bookToTuple(Book("python 3", "Samet", "2015", "1", "100")),
    Book.bookToTuple(Book("java", "Samet", "2013", "5", "85")),
    Book.bookToTuple(Book("c++", "Samet", "2012", "10", "60")),
    Book.bookToTuple(Book("python 3", "Samet", "2015", "1", "100")),
    Book.bookToTuple(Book("java", "Samet", "2013", "5", "85")),
    Book.bookToTuple(Book("c++", "Samet", "2012", "10", "60")),
    Book.bookToTuple(Book("python 3", "Samet", "2015", "1", "100")),
    Book.bookToTuple(Book("java", "Samet", "2013", "5", "85")),
    Book.bookToTuple(Book("c++", "Samet", "2012", "10", "60")),
    Book.bookToTuple(Book("python 3", "Samet", "2015", "1", "100")),
    Book.bookToTuple(Book("java", "Samet", "2013", "5", "85")),
    Book.bookToTuple(Book("c++", "Samet", "2012", "10", "60")),
    Book.bookToTuple(Book("python 3", "Samet", "2015", "1", "100")),
    Book.bookToTuple(Book("java", "Samet", "2013", "5", "85"))
]

def newBook():
    print('New Book')

def updateBook():
    print('Update Book')

def deleteBook():
    print('Delete Book')

MainWindow(books, newBook, updateBook, deleteBook)