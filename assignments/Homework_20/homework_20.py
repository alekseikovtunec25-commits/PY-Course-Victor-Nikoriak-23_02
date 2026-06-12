#Task 1
import unittest

from with_index import with_index


class TestWithIndex(unittest.TestCase):

    def test_default_start(self):
        result = list(with_index(["a", "b", "c"]))

        expected = [
            (0, "a"),
            (1, "b"),
            (2, "c")
        ]

        self.assertEqual(result, expected)

    def test_custom_start(self):
        result = list(with_index(["a", "b"], start=5))

        expected = [
            (5, "a"),
            (6, "b")
        ]

        self.assertEqual(result, expected)

    def test_empty_iterable(self):
        result = list(with_index([]))

        self.assertEqual(result, [])

    def test_tuple(self):
        result = list(with_index(("x", "y")))

        expected = [
            (0, "x"),
            (1, "y")
        ]

        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
