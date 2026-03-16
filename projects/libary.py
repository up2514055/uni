class LibraryBook:


    max_copies = 5

    def __init__(self, title, author):#constructor
        self.title = title
        self.author = author
        self._copies_available = 3


    @property #getter
    def copies_available(self):
        return self._copies_available
    
    @copies_available.setter #setter has same vairable name as the getter so if the variable name is car it will be car.setter
    def copies_available(self, new_value):
        if 0 <= new_value <=LibraryBook.max_copies:
            self._copies_available = new_value

    
    def borrow_book(self):
        if self.copies_available > 0:
            self.copies_available -= 1

    def return_book(self):
        self.copies_available += 1
        return f"{self.title} by {self.author} has been returned"

    def __str__(self):
        return f"The {self.title} by {self.author} - {self.copies_available} copies available"
    


def test_libary_book():
    book1 = LibraryBook("Hobbit", "Tolkien")
    print(book1)

    book1.borrow_book()
    print(book1)
    message = book1.return_book()
    print(message)
    print(book1)


test_libary_book()