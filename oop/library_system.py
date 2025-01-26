class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

class Library:
    
    book = [Book, EBook, PrintBook]

    def add_book(self, book):
        self.book.append(book)

    def list_books(self):
        for i in self.book:
            print(i)
