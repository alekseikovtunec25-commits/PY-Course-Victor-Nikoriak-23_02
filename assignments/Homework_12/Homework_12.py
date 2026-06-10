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

#Task3

def choose_func(nums: list, func1, func2):
    # проверяем, все ли числа положительные
    if all(num > 0 for num in nums):
        return func1(nums)
    else:
        return func2(nums)


# Assertions
nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]

def square_nums(nums):
    return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]

assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]

print("Все тесты пройдены!")