import unittest
from notes import NotesManager


class TestNotesManager(unittest.TestCase):

    def setUp(self):
        # Новий об'єкт перед кожним тестом
        self.manager = NotesManager()

    # ── ADD ───────────────────────────────────────────────

    def test_add_returns_id(self):
        """add() повертає числовий id"""
        note_id = self.manager.add("Купити молоко")
        self.assertEqual(note_id, 1)

    def test_add_stores_note(self):
        """Нотатка зберігається і доступна через get_all"""
        self.manager.add("Купити молоко")
        notes = self.manager.get_all()
        self.assertIn(1, notes)
        self.assertEqual(notes[1], "Купити молоко")

    def test_add_multiple_unique_ids(self):
        """Кілька нотаток отримують різні id"""
        id1 = self.manager.add("Перша")
        id2 = self.manager.add("Друга")
        self.assertNotEqual(id1, id2)

    def test_add_empty_text_raises(self):
        """Порожній текст → ValueError"""
        with self.assertRaises(ValueError):
            self.manager.add("   ")

    # ── UPDATE ────────────────────────────────────────────

    def test_update_changes_text(self):
        """update() змінює текст нотатки"""
        note_id = self.manager.add("Старий текст")
        self.manager.update(note_id, "Новий текст")
        self.assertEqual(self.manager.get_all()[note_id], "Новий текст")

    def test_update_nonexistent_raises(self):
        """update() з неіснуючим id → KeyError"""
        with self.assertRaises(KeyError):
            self.manager.update(999, "Текст")

    # ── DELETE ────────────────────────────────────────────

    def test_delete_removes_note(self):
        """delete() видаляє нотатку"""
        note_id = self.manager.add("Тимчасова")
        self.manager.delete(note_id)
        self.assertNotIn(note_id, self.manager.get_all())

    def test_delete_nonexistent_raises(self):
        """delete() з неіснуючим id → KeyError"""
        with self.assertRaises(KeyError):
            self.manager.delete(999)

    # ── GET_ALL ───────────────────────────────────────────

    def test_get_all_empty(self):
        """get_all() повертає порожній словник на старті"""
        self.assertEqual(self.manager.get_all(), {})

    def test_get_all_returns_copy(self):
        """get_all() повертає копію — зміна не ламає дані"""
        self.manager.add("Нотатка")
        copy = self.manager.get_all()
        copy[1] = "Зламана?"
        self.assertEqual(self.manager.get_all()[1], "Нотатка")


if __name__ == "__main__":
    unittest.main()
