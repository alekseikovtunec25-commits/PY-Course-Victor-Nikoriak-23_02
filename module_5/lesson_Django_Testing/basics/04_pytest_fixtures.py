"""
04 · PYTEST FIXTURES

Запуск:
    python -m pytest 04_pytest_fixtures.py -v

Фікстура — це функція з декоратором @pytest.fixture.
pytest автоматично передає її як аргумент у тест-функцію.

Переваги над setUp():
  - Можна переиикористовувати між файлами (conftest.py)
  - Декларативні залежності (фікстура може залежати від фікстури)
  - yield-фікстури для teardown (без окремого tearDown методу)
  - Scope: function (default) / class / module / session
"""

import pytest


# ─────────────────────────────────────────────────────────────────────────────
# Класи для демонстрації
# ─────────────────────────────────────────────────────────────────────────────

class User:
    def __init__(self, username, role='user'):
        self.username = username
        self.role = role
        self.is_active = True

    def is_admin(self):
        return self.role == 'admin'


class UserRepository:
    """Простий сховище користувачів (імітує БД)."""

    def __init__(self):
        self._users = {}

    def save(self, user):
        self._users[user.username] = user
        return user

    def get(self, username):
        return self._users.get(username)

    def all(self):
        return list(self._users.values())

    def count(self):
        return len(self._users)


# ─────────────────────────────────────────────────────────────────────────────
# БАЗОВІ ФІКСТУРИ
# ─────────────────────────────────────────────────────────────────────────────

@pytest.fixture
def db():
    """
    Фікстура scope='function' (default) — новий репозиторій для кожного тесту.
    Тести ізольовані: зміни в одному тесті не впливають на інший.
    """
    return UserRepository()


@pytest.fixture
def alice(db):
    """
    Фікстура що залежить від іншої фікстури.
    pytest автоматично передає db у alice.
    """
    user = User('alice', role='user')
    db.save(user)
    return user


@pytest.fixture
def admin(db):
    user = User('admin', role='admin')
    db.save(user)
    return user


# ─────────────────────────────────────────────────────────────────────────────
# ТЕСТИ ЩО ВИКОРИСТОВУЮТЬ ФІКСТУРИ
# ─────────────────────────────────────────────────────────────────────────────

def test_db_starts_empty(db):
    """Кожен тест отримує свій чистий db."""
    assert db.count() == 0


def test_save_user(db):
    user = User('bob')
    db.save(user)
    assert db.count() == 1
    assert db.get('bob') is user


def test_alice_is_not_admin(db, alice):
    """Можна запитати кілька фікстур одночасно."""
    assert db.count() == 1  # тільки alice у цьому тесті
    assert alice.is_admin() is False


def test_admin_is_admin(db, admin):
    assert admin.is_admin() is True


def test_multiple_users(db, alice, admin):
    """Обидві фікстури додали своїх користувачів."""
    assert db.count() == 2
    assert db.get('alice') is alice
    assert db.get('admin') is admin


# ─────────────────────────────────────────────────────────────────────────────
# YIELD-ФІКСТУРИ (setup + teardown в одній функції)
# ─────────────────────────────────────────────────────────────────────────────

@pytest.fixture
def temp_log():
    """
    yield-фікстура:
      - Код ДО yield — це setUp (підготовка)
      - Значення після yield — передається в тест
      - Код ПІСЛЯ yield — це tearDown (очищення)

    Аналог у unittest:
      def setUp(self): ...
      def tearDown(self): ...
    """
    log = []
    log.append("START")

    yield log  # <-- тест отримує log, коли доходить сюди

    # Цей код виконується після тесту (навіть якщо тест провалився)
    log.clear()
    # print(f"\n[teardown] log cleared")  # розкоментуй щоб побачити


def test_log_has_start_entry(temp_log):
    assert temp_log == ["START"]


def test_log_append(temp_log):
    temp_log.append("step 1")
    assert "step 1" in temp_log
    assert len(temp_log) == 2


# ─────────────────────────────────────────────────────────────────────────────
# SCOPE — Час життя фікстури
# ─────────────────────────────────────────────────────────────────────────────

@pytest.fixture(scope='module')
def shared_config():
    """
    scope='module' — фікстура створюється ОДИН РАЗ для всього модуля.
    Використовуй для дорогих операцій (завантаження файлу, парсинг).

    Інші значення:
      scope='function'  — за замовчуванням, новий для кожного тесту
      scope='class'     — один для всього тестового класу
      scope='module'    — один для всього файлу
      scope='session'   — один для всього запуску pytest
    """
    return {'debug': True, 'max_retries': 3, 'timeout': 30}


def test_config_has_debug(shared_config):
    assert shared_config['debug'] is True


def test_config_has_timeout(shared_config):
    assert shared_config['timeout'] == 30


# ─────────────────────────────────────────────────────────────────────────────
# ФІКСТУРИ У КЛАСАХ
# ─────────────────────────────────────────────────────────────────────────────

class TestUserRepository:
    """Фікстури pytest також працюють у тест-класах."""

    def test_save_and_get(self, db, alice):
        found = db.get('alice')
        assert found is alice

    def test_get_nonexistent(self, db):
        result = db.get('nobody')
        assert result is None

    def test_all_returns_list(self, db, alice, admin):
        users = db.all()
        assert isinstance(users, list)
        assert len(users) == 2
