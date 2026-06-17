#Task1
import math


def is_prime(number):
    """
    Возвращает True, если число простое,
    иначе False.
    """

    if number < 2:
        return False

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    limit = int(math.sqrt(number)) + 1

    for divisor in range(3, limit, 2):
        if number % divisor == 0:
            return False

    return True
#Проверка
NUMBERS = [
    2,
    1099726899285419,
    1570341764013157,
    1637027521802551,
    1880450821379411,
    1893530391196711,
    2447109360961063,
    3,
    2772290760589219,
    3033700317376073,
    4350190374376723,
    4350190491008389,
    4350190491008390,
    4350222956688319,
    2447120421950803,
    5,
]

for number in NUMBERS:
    print(f"{number}: {is_prime(number)}")