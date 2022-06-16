import uuid

class Book():
    def __init__(self, name: str, writer: str, year: int, piece: int, price: float) -> None:
        self.code = uuid.uuid4()
        self.name = name
        self.writer = writer
        self.year = year
        self.piece = piece
        self.price = price
        

def tuppleToBook(tup) -> Book:
    b = Book(tup[1], tup[2], tup[3], tup[4], tup[5])
    b.code = tup[0]
    
    return b