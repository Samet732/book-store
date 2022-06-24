import uuid

class Book():
    def __init__(self, name: str, author: str, year: int, piece: int, price: float, code=uuid.uuid4()) -> None:
        self.code = code
        self.name = name
        self.author = author
        self.year = year
        self.piece = piece
        self.price = price
    
    @classmethod
    def tupleToBook(cls, tup):
        b = Book(tup[1], tup[2], tup[3], tup[4], tup[5])
        b.code = tup[0]
    
        return b

    @classmethod
    def bookToTuple(cls, b) -> tuple:
        return (b.code, b.name, b.author, b.year, b.piece, b.price)