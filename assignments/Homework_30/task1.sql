-- task1.sql
-- Создание таблицы
DROP TABLE IF EXISTS students;

CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    age INTEGER NOT NULL
);

-- Добавление строк
INSERT INTO students (full_name, age) VALUES
('Іван Петренко', 20),
('Олена Коваль', 21),
('Андрій Шевченко', 19);

-- Переименование таблицы
ALTER TABLE students RENAME TO learners;

-- Добавление нового столбца
ALTER TABLE learners ADD COLUMN email TEXT;

-- Обновление данных
UPDATE learners
SET email = 'ivan.petrenko@example.com'
WHERE full_name = 'Іван Петренко';

UPDATE learners
SET email = 'olena.koval@example.com'
WHERE full_name = 'Олена Коваль';

UPDATE learners
SET email = 'andrii.shevchenko@example.com'
WHERE full_name = 'Андрій Шевченко';

UPDATE learners
SET age = 22
WHERE full_name = 'Олена Коваль';

-- Удаление столбца
DELETE FROM learners
WHERE full_name = 'Андрій Шевченко';

-- Результат 
SELECT * FROM learners;
