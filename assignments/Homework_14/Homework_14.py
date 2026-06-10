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

#Task2

def stop_words(words: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            for word in words:
                result = result.replace(word, "*")

            return result

        return wrapper
    return decorator


@stop_words(["pepsi", "BMW"])
def create_slogan(name: str) -> str:
    return f"{name} пьет pepsi в своем новеньком BMW!"


# Проверка
assert create_slogan("Steve") == "Steve пьет * в своем новеньком *!"

print(create_slogan("Steve"))