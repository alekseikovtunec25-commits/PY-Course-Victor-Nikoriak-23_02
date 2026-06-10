#Task1
class Person:
    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def introduce(self):
        return f"Меня зовут {self.full_name()}, мне {self.age} лет"


class Student(Person):
    def __init__(self, first_name, last_name, age, grade: int):
        super().__init__(first_name, last_name, age)
        self.grade = grade
        self.marks = []

    def add_mark(self, mark: int):
        self.marks.append(mark)

    def average_mark(self):
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)

    def study(self):
        return f"{self.full_name()} учится в {self.grade} классе"


class Teacher(Person):
    def __init__(self, first_name, last_name, age, subject: str, salary: int):
        super().__init__(first_name, last_name, age)
        self.subject = subject
        self.__salary = salary  # инкапсуляция (приватный атрибут)

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary

    def teach(self):
        return f"{self.full_name()} преподаёт {self.subject}"


# ===== Пример использования =====

student = Student("Иван", "Петров", 15, 9)
student.add_mark(5)
student.add_mark(4)

teacher = Teacher("Анна", "Сидорова", 40, "Математику", 16000)

print(student.introduce())
print(student.study())
print("Средняя оценка:", student.average_mark())

print(teacher.introduce())
print(teacher.teach())
print("Зарплата:", teacher.get_salary())

#Task 2

class Mathematician:

    def square_nums(self, nums: list):
        return [num ** 2 for num in nums]

    def remove_positives(self, nums: list):
        return [num for num in nums if num <= 0]

    def filter_leaps(self, years: list):
        result = []
        for year in years:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                result.append(year)
        return result


# ===== Проверка =====

m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

print("Все тесты пройдены!")

#Task 3

class Product:
    def __init__(self, type_: str, name: str, price: float):
        self.type = type_
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        # name -> [product, amount, price_with_markup]
        self.products = {}
        self.income = 0

    def add(self, product: Product, amount: int):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")

        price_with_markup = product.price * 1.3  # +30%

        if product.name in self.products:
            self.products[product.name][1] += amount
        else:
            self.products[product.name] = [product, amount, price_with_markup]

    def set_discount(self, identifier, percent, identifier_type='name'):
        if percent < 0 or percent > 100:
            raise ValueError("Invalid discount percent")

        for name, data in self.products.items():
            product = data[0]

            if (identifier_type == 'name' and product.name == identifier) or \
               (identifier_type == 'type' and product.type == identifier):

                data[2] = data[2] * (1 - percent / 100)

    def sell_product(self, product_name, amount):
        if product_name not in self.products:
            raise ValueError("Product not found")

        product, stock, price = self.products[product_name]

        if amount > stock:
            raise ValueError("Not enough items in stock")

        self.products[product_name][1] -= amount
        self.income += price * amount

    def get_income(self):
        return self.income

    def get_all_products(self):
        return [
            (product.name, amount, price)
            for product, amount, price in self.products.values()
        ]

    def get_product_info(self, product_name):
        if product_name not in self.products:
            raise ValueError("Product not found")

        product, amount, _ = self.products[product_name]
        return (product.name, amount)


# ===== ПРОВЕРКА =====

p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

s.add(p, 10)
s.add(p2, 300)

s.sell_product('Ramen', 10)

assert s.get_product_info('Ramen') == ('Ramen', 290)

print("Все тесты пройдены!")

#Task4
class CustomException(Exception):

    def __init__(self, msg):
        super().__init__(msg)

        self.msg = msg

        # записываем ошибку в файл
        with open("logs.txt", "a", encoding="utf-8") as file:
            file.write(self.msg + "\n")