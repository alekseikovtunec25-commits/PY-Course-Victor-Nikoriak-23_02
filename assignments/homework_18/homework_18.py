#Task 1

class User:
    def __init__(self, email):
        self.validate(email)
        self.email = email

    def validate(self, email):
        if not isinstance(email, str):
            raise TypeError("Email должен быть строкой")

        if "@" not in email:
            raise ValueError("Email должен содержать символ @")

        username, domain = email.split("@", 1)

        if not username:
            raise ValueError("До символа @ должна быть часть адреса")

        if "." not in domain:
            raise ValueError("Домен должен содержать точку")

        if domain.startswith(".") or domain.endswith("."):
            raise ValueError("Некорректный домен")


if __name__ == "__main__":
    try:
        user = User("test@gmail.com")
        print("Email корректный:", user.email)

        user2 = User("testgmail.com")
    except Exception as e:
        print("Ошибка:", e)

