#Task1
def my_function():
    a = 10
    b = 20
    c = 30

    return a + b + c


print("Количество локальных переменных:",
      my_function.__code__.co_nlocals)