class NotesManager:
    def __init__(self):
        # Зберігаємо нотатки у словнику: {id: text}
        self.notes = {}
        self._next_id = 1

    def add(self, text):
        """Додає нотатку, повертає її id."""
        if not text.strip():
            raise ValueError("Текст нотатки не може бути порожнім")
        note_id = self._next_id
        self.notes[note_id] = text
        self._next_id += 1
        return note_id

    def update(self, note_id, new_text):
        """Змінює текст нотатки за id."""
        if note_id not in self.notes:
            raise KeyError(f"Нотатку з id={note_id} не знайдено")
        if not new_text.strip():
            raise ValueError("Текст нотатки не може бути порожнім")
        self.notes[note_id] = new_text

    def delete(self, note_id):
        """Видаляє нотатку за id."""
        if note_id not in self.notes:
            raise KeyError(f"Нотатку з id={note_id} не знайдено")
        del self.notes[note_id]

    def get_all(self):
        """Повертає копію всіх нотаток."""
        return dict(self.notes)
