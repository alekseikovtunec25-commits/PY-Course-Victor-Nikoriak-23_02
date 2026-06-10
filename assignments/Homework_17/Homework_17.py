#Task1
class Animal:
    def talk(self):
        raise NotImplementedError("Subclasses must implement talk method")


class Dog(Animal):
    def talk(self):
        print("woof woof")


class Cat(Animal):
    def talk(self):
        print("meow")


# универсальная функция
def make_talk(animal: Animal):
    animal.talk()


# ===== Проверка =====

dog = Dog()
cat = Cat()

make_talk(dog)  # woof woof
make_talk(cat)  # meow

#Task2

class Author:
    def __init__(self, name: str, country: str, birthday: str):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __str__(self):
        return f"Author: {self.name}"

    def __repr__(self):
        return f"Author(name={self.name}, country={self.country})"


class Book:
    total_books = 0  # переменная класса

    def __init__(self, name: str, year: int, author: Author):
        self.name = name
        self.year = year
        self.author = author

        # добавляем книгу автору
        self.author.books.append(self)

        # увеличиваем общее количество книг
        Book.total_books += 1

    def __str__(self):
        return f"{self.name} ({self.year}) by {self.author.name}"

    def __repr__(self):
        return f"Book(name={self.name}, year={self.year}, author={self.author.name})"


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name: str, year: int, author: Author):
        book = Book(name, year, author)

        self.books.append(book)

        if author not in self.authors:
            self.authors.append(author)

        return book

    def group_by_author(self, author: Author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year: int):
        return [book for book in self.books if book.year == year]

    def __str__(self):
        return f"Library: {self.name}, Books: {len(self.books)}"

    def __repr__(self):
        return f"Library(name={self.name}, books={len(self.books)})"
