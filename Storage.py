import sqlite3 as sq
from Book import *

class Storage():
    def __init__(self, filename: str) -> None:
        self.db = sq.connect(filename)
        self.cursor = self.db.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Book(Code TEXT, Name TEXT, Author TEXT, Year INTEGER, Piece INTEGER, Price REAL)')

    def add(self, b: Book) -> None:
        self.cursor.execute(f'INSERT INTO Book VALUES("{b.code}", "{b.name}", "{b.author}", "{b.year}", "{b.piece}", "{b.price}")')
        self.db.commit()

    def update(self, b: Book) -> None:
        self.cursor.execute(f'UPDATE Book SET Name="{b.name}", Author="{b.author}", Year="{b.year}", Piece="{b.piece}", Price="{b.price}" WHERE Code="{b.code}"')
        self.db.commit()

    def delete(self, code: str) -> None:
        self.cursor.execute(f'DELETE FROM Book WHERE Code="{code}"')
        self.db.commit()

    def getAll(self) -> list:
        self.cursor.execute('SELECT * FROM Book')
        return self.cursor.fetchall()

    def close(self) -> None:
        self.db.close()