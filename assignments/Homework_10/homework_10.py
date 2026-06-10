#Task1
# Функция, которая явно вызывает исключение IndexError
def oops():
    raise IndexError("Это ошибка IndexError")


# Функция, которая перехватывает исключение
def safe_call():
    try:
        oops()
    except IndexError as err:
        print("Перехвачено исключение:", err)


safe_call()

# Функция, которая явно вызывает исключение KeyError
def oops():
    raise KeyError("Это ошибка IndexError")


 #Функция, которая перехватывает исключение
def safe_call():
    try:
        oops()
    except IndexError as err:
        print("Перехвачено исключение:", err)


safe_call()

#Task2

def calculate():
    try:
        a = float(input("Введите число a: "))
        b = float(input("Введите число b: "))

        result = (a ** 2) / b
        return result

    except ValueError:
        print("Ошибка: необходимо вводить только числа.")

    except ZeroDivisionError:
        print("Ошибка: деление на ноль невозможно.")


print(calculate())