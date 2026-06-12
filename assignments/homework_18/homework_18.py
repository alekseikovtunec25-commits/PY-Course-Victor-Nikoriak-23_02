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

#Task 2

class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.__workers = []

    @property
    def workers(self):
        return self.__workers.copy()

    def add_worker(self, worker):

        if not isinstance(worker, Worker):
            raise TypeError("Можно добавлять только Worker")

        if worker not in self.__workers:
            self.__workers.append(worker)


class Worker:

    def __init__(
        self,
        id_: int,
        name: str,
        company: str,
        boss
    ):
        self.id = id_
        self.name = name
        self.company = company

        self.boss = boss

    @property
    def boss(self):
        return self.__boss

    @boss.setter
    def boss(self, value):

        if not isinstance(value, Boss):
            raise TypeError("boss должен быть объектом Boss")

        self.__boss = value

        if self not in value.workers:
            value.add_worker(self)