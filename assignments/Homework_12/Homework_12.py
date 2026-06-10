#Task1
def my_function():
    a = 10
    b = 20
    c = 30

    return a + b + c


print("Количество локальных переменных:",
      my_function.__code__.co_nlocals)

#Task2

def outer_function(x):
    def inner_function(y):
        return x + y  # использует переменную из внешней функции
    return inner_function  # возвращаем функцию

# создаём функцию-результат
add_five = outer_function(5)

# вызываем внутреннюю функцию
result = add_five(10)

print(result)  # 15