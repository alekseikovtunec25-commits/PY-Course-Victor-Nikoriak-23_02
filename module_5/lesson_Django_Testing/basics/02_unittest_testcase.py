"""
02 · UNITTEST.TESTCASE

Запуск:
    python -m pytest 02_unittest_testcase.py -v
    # або
    python -m unittest 02_unittest_testcase -v

unittest.TestCase — базовий клас для організованих тестів.
Переваги:
  - setUp() / tearDown() — код що виконується до/після кожного тесту
  - setUpClass() / tearDownClass() — один раз на весь клас
  - Багато методів assert* з кращими повідомленнями про помилки

Django використовує django.test.TestCase — підклас unittest.TestCase.
"""

import unittest


# ─────────────────────────────────────────────────────────────────────────────
# Клас що тестуємо (імітує модель або сервіс)
# ─────────────────────────────────────────────────────────────────────────────

class BankAccount:
    """Проста модель банківського рахунку для демонстрації."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сума поповнення має бути > 0")
        self.balance += amount
        self.transactions.append(('deposit', amount))

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сума зняття має бути > 0")
        if amount > self.balance:
            raise ValueError("Недостатньо коштів")
        self.balance -= amount
        self.transactions.append(('withdraw', amount))

    def __str__(self):
        return f"BankAccount({self.owner}, {self.balance} грн)"


# ─────────────────────────────────────────────────────────────────────────────
# Тестовий клас
# ─────────────────────────────────────────────────────────────────────────────

class BankAccountTest(unittest.TestCase):
    """
    Кожен метод test_* — окремий тест.
    setUp() виконується ПЕРЕД кожним тестом.
    tearDown() виконується ПІСЛЯ кожного тесту.
    """

    def setUp(self):
        """
        Готуємо стан перед кожним тестом.
        Після кожного тесту Python створює новий екземпляр класу BankAccountTest,
        тому self.account завжди свіжий (balance=100).
        """
        self.account = BankAccount(owner='Alice', balance=100)

    def tearDown(self):
        """
        Очищення після тесту.
        Тут можна закрити файл, з'єднання з БД, тощо.
        Для простих unit-тестів часто не потрібний.
        """
        pass  # Нічого не потрібно очищати

    # ── Базові тести ──────────────────────────────────────────────────────────

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 100)

    def test_owner_name(self):
        self.assertEqual(self.account.owner, 'Alice')

    def test_str_representation(self):
        self.assertEqual(str(self.account), "BankAccount(Alice, 100 грн)")

    # ── Тести deposit ─────────────────────────────────────────────────────────

    def test_deposit_increases_balance(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)

    def test_deposit_records_transaction(self):
        self.account.deposit(50)
        self.assertIn(('deposit', 50), self.account.transactions)

    def test_deposit_zero_raises_error(self):
        """Очікуємо ValueError при поповненні на 0."""
        with self.assertRaises(ValueError):
            self.account.deposit(0)

    def test_deposit_negative_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.account.deposit(-10)
        # Можемо перевірити і текст помилки
        self.assertIn("має бути > 0", str(context.exception))

    # ── Тести withdraw ────────────────────────────────────────────────────────

    def test_withdraw_decreases_balance(self):
        self.account.withdraw(30)
        self.assertEqual(self.account.balance, 70)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError) as context:
            self.account.withdraw(200)
        self.assertIn("Недостатньо коштів", str(context.exception))

    def test_withdraw_exact_balance(self):
        """Можна зняти рівно стільки, скільки є."""
        self.account.withdraw(100)
        self.assertEqual(self.account.balance, 0)

    # ── Тести транзакцій ──────────────────────────────────────────────────────

    def test_multiple_transactions(self):
        self.account.deposit(200)    # balance = 300
        self.account.withdraw(50)   # balance = 250
        self.account.withdraw(100)  # balance = 150

        self.assertEqual(self.account.balance, 150)
        self.assertEqual(len(self.account.transactions), 3)

    def test_fresh_account_has_no_transactions(self):
        """setUp() дає нам свіжий рахунок у кожному тесті."""
        self.assertEqual(len(self.account.transactions), 0)


# ─────────────────────────────────────────────────────────────────────────────
# SETUPTESTCASE — один раз на клас (дорогі ресурси)
# ─────────────────────────────────────────────────────────────────────────────

class ExpensiveSetupTest(unittest.TestCase):
    """
    setUpClass() — викликається ОДИН РАЗ перед усіма тестами класу.
    Корисно коли ініціалізація дорога (підключення до БД, парсинг файлу).
    """

    @classmethod
    def setUpClass(cls):
        print("\n[setUpClass] Виконується один раз")
        cls.shared_data = list(range(1000))  # дорога операція

    @classmethod
    def tearDownClass(cls):
        print("\n[tearDownClass] Виконується один раз")
        cls.shared_data = None

    def test_data_length(self):
        self.assertEqual(len(self.shared_data), 1000)

    def test_data_first_element(self):
        self.assertEqual(self.shared_data[0], 0)

    def test_data_last_element(self):
        self.assertEqual(self.shared_data[-1], 999)


if __name__ == '__main__':
    unittest.main(verbosity=2)
