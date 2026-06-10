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