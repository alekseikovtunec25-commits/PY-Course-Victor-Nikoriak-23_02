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