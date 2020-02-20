
class Library():
    def __init__(self, books, signing_time, scanning_capacity):
        self.books = set(books)
        self.sign_time = signing_time
        self.scan_cap = scanning_capacity

class Book():
    def __init__(self, id, value):
        self.id = id
        self.value = value

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"<Book {self.id}>"