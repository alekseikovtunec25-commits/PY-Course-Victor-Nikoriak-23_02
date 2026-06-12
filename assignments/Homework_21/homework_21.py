import datetime


class MyFile:
    _counter = 0  # общий счётчик всех операций

    def __init__(self, filename, mode="r", log_file="log.txt"):
        self.filename = filename
        self.mode = mode
        self.log_file = log_file
        self.file = None

    def _log(self, message):
        """Запись в журнал"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, "a", encoding="utf-8") as log:
            log.write(f"[{timestamp}] {message}\n")

    def __enter__(self):
        """Открытие файла"""
        self.file = open(self.filename, self.mode, encoding="utf-8")
        MyFile._counter += 1

        self._log(f"OPEN file={self.filename}, mode={self.mode}, counter={MyFile._counter}")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Закрытие файла + обработка ошибок"""
        if self.file:
            self.file.close()
            MyFile._counter += 1
            self._log(f"CLOSE file={self.filename}, counter={MyFile._counter}")

        # если была ошибка — логируем её, но не подавляем
        if exc_type:
            self._log(f"ERROR {exc_type.__name__}: {exc_val}")

        # False -> ошибки не скрываем
        return False

