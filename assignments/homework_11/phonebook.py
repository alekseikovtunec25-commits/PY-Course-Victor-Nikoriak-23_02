import json
import sys
import os


def load_phonebook(filename):
    if not os.path.exists(filename):
        print(f"Ошибка: файл {filename} не найден.")
        sys.exit()

    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def save_phonebook(filename, data):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def add_record(phonebook):
    record = {
        "first_name": input("Имя: "),
        "last_name": input("Фамилия: "),
        "phone": input("Телефон: "),
        "city": input("Город: ")
    }

    phonebook.append(record)
    print("Запись добавлена.")


def search_by_name(phonebook):
    name = input("Введите имя: ")

    for person in phonebook:
        if person["first_name"].lower() == name.lower():
            print(person)


def search_by_surname(phonebook):
    surname = input("Введите фамилию: ")

    for person in phonebook:
        if person["last_name"].lower() == surname.lower():
            print(person)


def search_by_full_name(phonebook):
    first = input("Имя: ")
    last = input("Фамилия: ")

    for person in phonebook:
        if (
            person["first_name"].lower() == first.lower()
            and person["last_name"].lower() == last.lower()
        ):
            print(person)


def search_by_phone(phonebook):
    phone = input("Телефон: ")

    for person in phonebook:
        if person["phone"] == phone:
            print(person)


def search_by_city(phonebook):
    city = input("Город: ")

    for person in phonebook:
        if person["city"].lower() == city.lower():
            print(person)


def delete_record(phonebook):
    phone = input("Введите номер телефона: ")

    for person in phonebook:
        if person["phone"] == phone:
            phonebook.remove(person)
            print("Запись удалена.")
            return

    print("Запись не найдена.")


def update_record(phonebook):
    phone = input("Введите номер телефона: ")

    for person in phonebook:
        if person["phone"] == phone:
            person["first_name"] = input("Новое имя: ")
            person["last_name"] = input("Новая фамилия: ")
            person["city"] = input("Новый город: ")

            print("Запись обновлена.")
            return

    print("Запись не найдена.")


def menu():
    print("\nТелефонная книга")
    print("1 - Добавить запись")
    print("2 - Поиск по имени")
    print("3 - Поиск по фамилии")
    print("4 - Поиск по полному имени")
    print("5 - Поиск по телефону")
    print("6 - Поиск по городу")
    print("7 - Удалить запись")
    print("8 - Обновить запись")
    print("9 - Выход")


def main():
    if len(sys.argv) < 2:
        print("Использование: python phonebook.py phonebook.json")
        return

    filename = sys.argv[1]
    phonebook = load_phonebook(filename)

    while True:
        menu()

        choice = input("Выберите действие: ")

        if choice == "1":
            add_record(phonebook)

        elif choice == "2":
            search_by_name(phonebook)

        elif choice == "3":
            search_by_surname(phonebook)

        elif choice == "4":
            search_by_full_name(phonebook)

        elif choice == "5":
            search_by_phone(phonebook)

        elif choice == "6":
            search_by_city(phonebook)

        elif choice == "7":
            delete_record(phonebook)

        elif choice == "8":
            update_record(phonebook)

        elif choice == "9":
            save_phonebook(filename, phonebook)
            print("Данные сохранены.")
            break

        else:
            print("Неверный пункт меню.")


if __name__ == "__main__":
    main()