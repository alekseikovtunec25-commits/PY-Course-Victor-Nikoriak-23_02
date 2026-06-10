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