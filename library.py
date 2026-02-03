class Book:

    def __init__(self, title, author, isbn):
        self.available = True
        self.title = title
        self.author = author
        self.isbn = isbn

    def borrow_book(self):
        if self.available:
            self.available = False
            return "Book has been borrowed"
        return "Book is already being borrowed"

    def return_book(self):
        if not self.available:
            self.available = True
            return "Book has been returned"
        return "Book is currently not being borrowed"

    def __str__(self):
        return f"The book {self.title} written by {self.author} with the number {self.isbn}"


#digital book class

class DigitalBook(Book):

    compatibility_options = {'Kindle', 'PDF', 'Apple'}

    def __init__(self, title, author, isbn):
        super().__init__(title, author, isbn)
        self.compatibility = {'Kindle'}
        self.compatibility = ", ".join(self.compatibility)

    def borrow_book(self):
        # Don't remove the pass
        return "You have borrowed the digital book"
        pass

    def return_book(self):
        # Don't remove the pass
        return "You have returned the digital book"
        pass

    def __str__(self):
        return f"The digital book {self.title} written by {self.author} with the number {self.isbn} is compatible with {self.compatibility}"


#libary class

class Library:
    "libary"

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.available:
                    return book.borrow_book()
                else:
                    return f"Book with ISBN {isbn} is already borrowed."
        return f"Book with ISBN {isbn} is not in the library"

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book.return_book()
        return f"Book with ISBN {isbn} is not in the library"

    def __str__(self):
        output = "Library contains:\n"
        for book in self.books:
            status = "Available" if book.available else "Borrowed"
            output += f"{book} and is currently {status}\n"
        return output


#test function

def test_library():
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")
    book2 = Book("1984", "George Orwell", "978-0451524935")
    book3 = Book("Jane Eyre", "Charlotte Bronte", "978-0141441146")

    # Give digital a different ISBN so you can see behaviour clearly
    book4 = DigitalBook("1984", "George Orwell", "978-0451524935-DIGI")

    library = Library()
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)

    print(library)

    print(library.borrow_book("978-0451524935-DIGI"))
    print(library)

    print(library.borrow_book("978-0451524935"))
    print(library)

    print(library.return_book("978-0451524935"))
    print(library)


test_library()

