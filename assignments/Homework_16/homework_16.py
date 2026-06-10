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

teacher = Teacher("Анна", "Сидорова", 40, "Математика", 16000)

print(student.introduce())
print(student.study())
print("Средняя оценка:", student.average_mark())

print(teacher.introduce())
print(teacher.teach())
print("Зарплата:", teacher.get_salary())