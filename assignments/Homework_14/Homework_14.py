#Task1
def logger(func):
    def wrapper(*args, **kwargs):
        # печатаем имя функции и аргументы
        print(f"{func.__name__} called with {', '.join(map(str, args))}")

        # вызываем оригинальную функцию
        return func(*args, **kwargs)

    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


# Проверка
add(4, 5)
square_all(1, 2, 3)