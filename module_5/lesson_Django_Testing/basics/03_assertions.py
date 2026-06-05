"""
03 · ASSERTIONS — Методи перевірки в unittest.TestCase

Запуск:
    python -m pytest 03_assertions.py -v

Чому не писати просто assert?

    assert a == b                     ← якщо провалиться: "AssertionError"
    self.assertEqual(a, b)            ← якщо провалиться: "1 != 2"

assertEqual дає набагато зрозуміліше повідомлення про помилку.

ДОВІДНИК:
  assertEqual(a, b)         a == b
  assertNotEqual(a, b)      a != b
  assertTrue(x)             bool(x) is True
  assertFalse(x)            bool(x) is False
  assertIsNone(x)           x is None
  assertIsNotNone(x)        x is not None
  assertIn(a, b)            a in b
  assertNotIn(a, b)         a not in b
  assertIs(a, b)            a is b  (тотожність, не рівність)
  assertIsNot(a, b)         a is not b
  assertIsInstance(a, T)    isinstance(a, T)
  assertRaises(Exc, fn, .)  fn(.) кидає Exc
  assertAlmostEqual(a, b)   abs(a-b) <= 1e-7
  assertGreater(a, b)       a > b
  assertLess(a, b)          a < b
  assertGreaterEqual(a, b)  a >= b
  assertLessEqual(a, b)     a <= b
  assertListEqual(a, b)     lists equal (кращий вивід)
  assertDictEqual(a, b)     dicts equal (кращий вивід)
  assertSetEqual(a, b)      sets equal
  assertMultiLineEqual(a,b) strings equal (diff по рядках)
"""

import unittest
import math


class AssertionDemoTest(unittest.TestCase):

    # ── Рівність ──────────────────────────────────────────────────────────────

    def test_assertEqual(self):
        self.assertEqual(2 + 2, 4)
        self.assertEqual("hello".upper(), "HELLO")
        self.assertEqual([1, 2, 3], [1, 2, 3])

    def test_assertNotEqual(self):
        self.assertNotEqual(2 + 2, 5)
        self.assertNotEqual("hello", "world")

    # ── Булеві значення ───────────────────────────────────────────────────────

    def test_assertTrue(self):
        self.assertTrue(True)
        self.assertTrue(1)           # truthy значення
        self.assertTrue([1, 2])      # непорожній список — truthy

    def test_assertFalse(self):
        self.assertFalse(False)
        self.assertFalse(0)          # falsy значення
        self.assertFalse([])         # порожній список — falsy
        self.assertFalse("")         # порожній рядок — falsy

    # ── None ─────────────────────────────────────────────────────────────────

    def test_assertIsNone(self):
        result = None
        self.assertIsNone(result)

        def returns_none():
            pass  # функція без return повертає None

        self.assertIsNone(returns_none())

    def test_assertIsNotNone(self):
        result = 42
        self.assertIsNotNone(result)

    # ── Приналежність ─────────────────────────────────────────────────────────

    def test_assertIn(self):
        fruits = ['apple', 'banana', 'cherry']
        self.assertIn('banana', fruits)
        self.assertIn('a', 'cat')         # символ у рядку
        self.assertIn('name', {'name': 'Alice'})   # ключ у словнику

    def test_assertNotIn(self):
        fruits = ['apple', 'banana']
        self.assertNotIn('grape', fruits)

    # ── Тип (isinstance) ──────────────────────────────────────────────────────

    def test_assertIsInstance(self):
        self.assertIsInstance(42, int)
        self.assertIsInstance(3.14, float)
        self.assertIsInstance("hello", str)
        self.assertIsInstance([1, 2], list)
        self.assertIsInstance(True, bool)
        self.assertIsInstance(True, int)  # bool — підклас int!

    def test_assertIsInstance_with_tuple(self):
        value = 42
        # Перевірити чи один з кількох типів
        self.assertIsInstance(value, (int, float))

    # ── Порівняння (числа) ────────────────────────────────────────────────────

    def test_assertGreater(self):
        self.assertGreater(5, 3)
        self.assertGreater(0.1, 0.0)

    def test_assertLess(self):
        self.assertLess(3, 5)

    def test_assertGreaterEqual(self):
        self.assertGreaterEqual(5, 5)
        self.assertGreaterEqual(6, 5)

    def test_assertLessEqual(self):
        self.assertLessEqual(5, 5)
        self.assertLessEqual(4, 5)

    # ── Числа з плаваючою точкою ──────────────────────────────────────────────

    def test_assertAlmostEqual(self):
        # Небезпечно: 0.1 + 0.2 != 0.3 через floating point
        self.assertNotEqual(0.1 + 0.2, 0.3)

        # Правильно — порівнюємо з точністю
        self.assertAlmostEqual(0.1 + 0.2, 0.3, places=10)
        self.assertAlmostEqual(math.sqrt(2) ** 2, 2.0, places=10)

    def test_assertAlmostEqual_custom_delta(self):
        # Або через delta — максимальна різниця
        self.assertAlmostEqual(100.05, 100.0, delta=0.1)

    # ── Винятки ──────────────────────────────────────────────────────────────

    def test_assertRaises_context_manager(self):
        """Рекомендований спосіб — context manager."""
        with self.assertRaises(ZeroDivisionError):
            _ = 1 / 0

    def test_assertRaises_with_message(self):
        with self.assertRaises(ValueError) as ctx:
            int("not a number")
        # ctx.exception — об'єкт виключення
        self.assertIn("invalid literal", str(ctx.exception))

    def test_assertRaises_callable(self):
        """Альтернативний синтаксис (менш популярний)."""
        self.assertRaises(TypeError, int, [1, 2, 3])

    # ── Колекції ─────────────────────────────────────────────────────────────

    def test_assertListEqual(self):
        # assertEqual теж працює, але assertListEqual дає кращий diff
        self.assertListEqual([1, 2, 3], [1, 2, 3])

    def test_assertDictEqual(self):
        expected = {'name': 'Alice', 'age': 30}
        actual = {'age': 30, 'name': 'Alice'}  # порядок не важливий
        self.assertDictEqual(expected, actual)

    def test_assertSetEqual(self):
        self.assertSetEqual({1, 2, 3}, {3, 1, 2})  # порядок не важливий

    # ── Рядки ────────────────────────────────────────────────────────────────

    def test_assertIn_substring(self):
        error_message = "ValueError: Invalid priority value 5"
        self.assertIn("priority", error_message)
        self.assertIn("Invalid", error_message)

    def test_assertMultiLineEqual(self):
        """Для довгих рядків — показує diff по рядках."""
        text1 = "Hello\nWorld\n"
        text2 = "Hello\nWorld\n"
        self.assertMultiLineEqual(text1, text2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
