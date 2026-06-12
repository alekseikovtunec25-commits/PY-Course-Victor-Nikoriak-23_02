import os
import unittest

from Homework_21.homework_21 import MyFile


class TestMyFileContextManager(unittest.TestCase):

    def setUp(self):
        """Подготовка перед каждым тестом"""
        self.test_file = "test_file.txt"
        self.log_file = "test_log.txt"

        # очищаем файлы перед тестом
        for f in [self.test_file, self.log_file]:
            if os.path.exists(f):
                os.remove(f)

    def test_write_file_success(self):
        """Файл создаётся и записывает данные"""

        with MyFile(self.test_file, "w", self.log_file) as f:
            f.write("Hello test")

        # проверяем содержимое файла
        with open(self.test_file, "r", encoding="utf-8") as f:
            content = f.read()

        self.assertEqual(content, "Hello test")

    def test_log_created(self):
        """Проверяем, что лог файл создаётся"""

        with MyFile(self.test_file, "w", self.log_file) as f:
            f.write("data")

        self.assertTrue(os.path.exists(self.log_file))

        with open(self.log_file, "r", encoding="utf-8") as log:
            log_content = log.read()

        self.assertIn("OPEN", log_content)
        self.assertIn("CLOSE", log_content)

    def test_file_is_closed(self):
        """Файл должен быть закрыт после with"""

        cm = MyFile(self.test_file, "w", self.log_file)

        with cm as f:
            f.write("test")

        self.assertTrue(f.closed)

    def test_exception_handling(self):
        """Проверка поведения при ошибке внутри with"""

        try:
            with MyFile(self.test_file, "w", self.log_file) as f:
                f.write("start")
                raise ValueError("test error")
        except ValueError:
            pass

        # файл всё равно должен существовать и содержать данные
        with open(self.test_file, "r", encoding="utf-8") as f:
            content = f.read()

        self.assertEqual(content, "start")

        # лог должен содержать ошибку
        with open(self.log_file, "r", encoding="utf-8") as log:
            log_data = log.read()

        self.assertIn("ERROR", log_data)

    def test_counter_increases(self):
        """Проверка работы счётчика"""

        with MyFile(self.test_file, "w", self.log_file) as f:
            f.write("1")

        with MyFile(self.test_file, "w", self.log_file) as f:
            f.write("2")

        # просто проверяем что лог существует и операции фиксируются
        with open(self.log_file, "r", encoding="utf-8") as log:
            log_data = log.read()

        self.assertGreaterEqual(log_data.count("OPEN"), 2)


if __name__ == "__main__":
    unittest.main()