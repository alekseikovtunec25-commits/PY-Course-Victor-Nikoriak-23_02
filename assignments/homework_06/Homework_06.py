#Task1

import random #импортируем модуль random

number = [] # создаем пустой список
i = 0
while i < 10: # создаем цикл while
    number.append(random.randint(0, 10)) #генерируем 10 случайных чисел
    i += 1
max_number = number[0] # создаем новый список и берем первое число из списка
j = 1 # берем новую переменную и берем 1 вместо 0 для избежания проверки одного и того числа
while j < len(number): # проходимся по всей длине списка
    if number[j] > max_number:
        max_number = number[j]
    j += 1
print(number)
print(max_number)
