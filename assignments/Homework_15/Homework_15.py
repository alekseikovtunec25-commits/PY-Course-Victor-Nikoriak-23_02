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

#Task 3

class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.current = 0  # индекс текущего канала (0 = первый)

    def first_channel(self):
        self.current = 0
        return self.channels[self.current]

    def last_channel(self):
        self.current = len(self.channels) - 1
        return self.channels[self.current]

    def turn_channel(self, n):
        self.current = n - 1
        return self.channels[self.current]

    def next_channel(self):
        self.current = (self.current + 1) % len(self.channels)
        return self.channels[self.current]

    def previous_channel(self):
        self.current = (self.current - 1) % len(self.channels)
        return self.channels[self.current]

    def current_channel(self):
        return self.channels[self.current]

    def exists(self, value):
        if isinstance(value, int):
            return "Yes" if 1 <= value <= len(self.channels) else "No"
        elif isinstance(value, str):
            return "Yes" if value in self.channels else "No"
        else:
            return "No"


# Пример использования
CHANNELS = ["BBC", "Discovery", "TV1000"]

controller = TVController(CHANNELS)

print(controller.first_channel())     # BBC
print(controller.last_channel())      # TV1000
print(controller.turn_channel(1))     # BBC
print(controller.next_channel())      # Discovery
print(controller.previous_channel())   # BBC
print(controller.current_channel())    # BBC
print(controller.exists(4))           # No
print(controller.exists("BBC"))       # Yes