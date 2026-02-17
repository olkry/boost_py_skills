class Book:
    def __init__(self, isbn, title, author, year, is_available=True):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.is_available = is_available

    def borrow(self):
        if self.is_available:
            self.is_available = False
            return f"Книга '{self.title}' выдана"
        return f"Книга '{self.title}' уже выдана"

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            return f"Книга '{self.title}' возвращена"
        return f"Книга '{self.title}' уже была доступна"

    def get_info(self):
        return (f"'{self.title}' by {self.author} "
                f"({self.year}) - ISBN: {self.isbn}")


# Тестирование
book1 = Book("978-5-699-12014-7",
             "Мастер и Маргарита",
             "Михаил Булгаков",
             1966)
book2 = Book("978-5-17-090324-5",
             "Преступление и наказание",
             "Федор Достоевский",
             1866,
             False)

print(book1.get_info())
print(book2.get_info())

print(book1.borrow())
print(book1.borrow())  # Попытка повторной выдачи
print(book2.return_book())
print(book2.return_book())  # Попытка повторного возврата

print(f"Книга 1 доступна: {book1.is_available}")
print(f"Книга 2 доступна: {book2.is_available}")