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

#Task 3

from math import gcd


class Fraction:
    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")

        # нормализация знака
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator

        # сокращение дроби
        common = gcd(numerator, denominator)
        self.numerator = numerator // common
        self.denominator = denominator // common

    def __add__(self, other):
        new_num = self.numerator * other.denominator + other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        new_num = self.numerator * other.denominator - other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        return Fraction(
            self.numerator * other.numerator,
            self.denominator * other.denominator
        )

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero fraction")

        return Fraction(
            self.numerator * other.denominator,
            self.denominator * other.numerator
        )

    def __eq__(self, other):
        return (self.numerator == other.numerator and
                self.denominator == other.denominator)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)

    result = x + y

    print(result)  # 3/4

    assert result == Fraction(3, 4)
