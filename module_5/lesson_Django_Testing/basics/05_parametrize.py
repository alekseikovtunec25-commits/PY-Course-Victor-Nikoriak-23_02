"""
05 · PYTEST.MARK.PARAMETRIZE — Один тест, багато наборів даних

Запуск:
    python -m pytest 05_parametrize.py -v

Проблема:
    def test_is_even_2(): assert is_even(2) is True
    def test_is_even_4(): assert is_even(4) is True
    def test_is_even_6(): assert is_even(6) is True
    ... × 10 тестів — дублювання коду

Рішення — parametrize:
    @pytest.mark.parametrize("n", [2, 4, 6, 8, 10])
    def test_is_even(n):
        assert is_even(n) is True

pytest запустить 5 незалежних тестів з одним рядком коду.
"""

import pytest


# ─────────────────────────────────────────────────────────────────────────────
# Функції що тестуємо
# ─────────────────────────────────────────────────────────────────────────────

def is_even(n):
    return n % 2 == 0


def clamp(value, min_val, max_val):
    return max(min_val, min(value, max_val))


def normalize_username(username):
    """Нормалізує ім'я користувача: trim + lowercase."""
    return username.strip().lower()


def slugify(text):
    """Спрощений slugify: пробіли → дефіси, lowercase."""
    return text.strip().lower().replace(' ', '-')


def grade(score):
    """Повертає оцінку за балом (0-100)."""
    if score >= 90:
        return 'A'
    elif score >= 75:
        return 'B'
    elif score >= 60:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'


def parse_priority(value):
    """Перетворює рядок пріоритету на число (1-4)."""
    mapping = {'low': 1, 'medium': 2, 'high': 3, 'urgent': 4}
    key = value.lower().strip()
    if key not in mapping:
        raise ValueError(f"Unknown priority: '{value}'")
    return mapping[key]


# ─────────────────────────────────────────────────────────────────────────────
# БАЗОВИЙ PARAMETRIZE
# ─────────────────────────────────────────────────────────────────────────────

@pytest.mark.parametrize("n", [0, 2, 4, 100, -6])
def test_is_even_true(n):
    """Усі ці числа мають бути парними."""
    assert is_even(n) is True


@pytest.mark.parametrize("n", [1, 3, 7, -5, 99])
def test_is_even_false(n):
    assert is_even(n) is False


# ─────────────────────────────────────────────────────────────────────────────
# PARAMETRIZE З КІЛЬКОМА АРГУМЕНТАМИ
# ─────────────────────────────────────────────────────────────────────────────

@pytest.mark.parametrize("username,expected", [
    ("Alice", "alice"),
    ("  BOB  ", "bob"),
    ("CHARLIE123", "charlie123"),
    ("  MiXeD  ", "mixed"),
])
def test_normalize_username(username, expected):
    assert normalize_username(username) == expected


@pytest.mark.parametrize("text,expected", [
    ("Hello World", "hello-world"),
    ("  Django  Testing  ", "django--testing"),  # подвійний пробіл → подвійний дефіс
    ("python", "python"),
    ("My Blog Post", "my-blog-post"),
])
def test_slugify(text, expected):
    assert slugify(text) == expected


# ─────────────────────────────────────────────────────────────────────────────
# PARAMETRIZE З NAMED CASES (ids)
# ─────────────────────────────────────────────────────────────────────────────

@pytest.mark.parametrize("score,expected", [
    (95, 'A'),
    (75, 'B'),
    (60, 'C'),
    (50, 'D'),
    (30, 'F'),
    (100, 'A'),
    (0,   'F'),
], ids=[
    "score_95_is_A",
    "score_75_is_B",
    "score_60_is_C",
    "score_50_is_D",
    "score_30_is_F",
    "max_score_is_A",
    "zero_is_F",
])
def test_grade(score, expected):
    """ids= дає зрозумілі назви у pytest виводі."""
    assert grade(score) == expected


# ─────────────────────────────────────────────────────────────────────────────
# PARAMETRIZE ДЛЯ ПЕРЕВІРКИ ПОМИЛОК
# ─────────────────────────────────────────────────────────────────────────────

@pytest.mark.parametrize("priority_str,expected_int", [
    ("low", 1),
    ("Low", 1),     # case-insensitive
    ("LOW", 1),
    ("medium", 2),
    ("high", 3),
    ("urgent", 4),
    ("  urgent  ", 4),   # зайві пробіли
])
def test_parse_priority_valid(priority_str, expected_int):
    assert parse_priority(priority_str) == expected_int


@pytest.mark.parametrize("invalid_value", [
    "extreme",
    "5",
    "",
    "критичний",
])
def test_parse_priority_invalid(invalid_value):
    """Невалідні значення мають кидати ValueError."""
    with pytest.raises(ValueError):
        parse_priority(invalid_value)


# ─────────────────────────────────────────────────────────────────────────────
# PARAMETRIZE З pytest.param (для skip або xfail)
# ─────────────────────────────────────────────────────────────────────────────

@pytest.mark.parametrize("value,min_v,max_v,expected", [
    pytest.param(5,   0, 10, 5,  id="within_range"),
    pytest.param(-5,  0, 10, 0,  id="below_min"),
    pytest.param(15,  0, 10, 10, id="above_max"),
    pytest.param(0,   0, 10, 0,  id="exactly_min"),
    pytest.param(10,  0, 10, 10, id="exactly_max"),
    pytest.param(5,   5,  5, 5,  id="single_point_range"),
])
def test_clamp(value, min_v, max_v, expected):
    assert clamp(value, min_v, max_v) == expected


# ─────────────────────────────────────────────────────────────────────────────
# ПОРІВНЯННЯ: unittest vs parametrize
# ─────────────────────────────────────────────────────────────────────────────

# НЕПРАВИЛЬНО — дублювання коду:
#
# def test_grade_95(): assert grade(95) == 'A'
# def test_grade_75(): assert grade(75) == 'B'
# def test_grade_60(): assert grade(60) == 'C'
# def test_grade_50(): assert grade(50) == 'D'
# def test_grade_30(): assert grade(30) == 'F'
#
# ПРАВИЛЬНО — parametrize: один тест, 5 наборів даних (вже написано вище)
