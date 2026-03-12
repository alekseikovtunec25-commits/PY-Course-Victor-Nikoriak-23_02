#Task 1

sentece = input("введите предложение: ")
words = sentece.split() # разделение строки на списки
a_dict = {} # создание пустого словаря
for word in words: # цикл для проверки вхождения слов
    if word in a_dict:
        a_dict[word] += 1
    else:
        a_dict[word] = 1
print(a_dict)