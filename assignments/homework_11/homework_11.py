#Task1
#Создание файла
with open(r"C:\Temp\myfile.txt", "w") as file:
    file.write("Hello file world!")

print("Файл успешно создан.")

#Открытие файла
with open("myfile.txt", "r") as file:
    content = file.read()

print(content)
