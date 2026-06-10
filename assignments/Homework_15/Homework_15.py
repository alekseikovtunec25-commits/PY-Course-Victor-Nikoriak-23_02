#Task 1
class Person:
    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def talk(self):
        print(f"Здравствуйте, меня зовут {self.first_name} {self.last_name}, и мне {self.age} лет")


# Пример использования
person = Person("Карл", "Джонсон", 26)
person.talk()

#Task 2

class Dog:
    age_factor = 7  # атрибут класса

    def __init__(self, age: int):
        self.age = age  # возраст собаки

    def human_age(self):
        return self.age * self.age_factor


# Пример использования
dog = Dog(4)
print(dog.human_age())  # 28