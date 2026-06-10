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

#Task3

def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(arg):

            # 1. Проверка типа
            if not isinstance(arg, type_):
                print("Type check failed")
                return False

            # 2. Проверка длины
            if len(arg) > max_length:
                print("Max length exceeded")
                return False

            # 3. Проверка содержимого
            for item in contains:
                if item not in arg:
                    print(f"Missing required substring: {item}")
                    return False

            # если всё ок — вызываем функцию
            return func(arg)

        return wrapper
    return decorator


@arg_rules(type_=str, max_length=15, contains=["05", "@"])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


# Проверка
print(create_slogan("johndoe05@gmail.com"))  # False
print(create_slogan("S@SH05"))                # корректная строка
assert create_slogan("johndoe05@gmail.com") is False
assert create_slogan("S@SH05") == "S@SH05 drinks pepsi in his brand new BMW!"