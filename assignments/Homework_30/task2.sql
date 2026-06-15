-- Задание 2: SQL-запросы к базе данных hr.db

-- 1. Вывод имён сотрудников с псевдонимами «First Name» и «Last Name»
SELECT
    first_name AS "First Name",
    last_name  AS "Last Name"
FROM employees;

-- 2. Уникальные идентификаторы отделов из таблицы сотрудников
SELECT DISTINCT department_id
FROM employees;

-- 3. Все сведения о сотрудниках, отсортированные по имени в порядке убывания
SELECT *
FROM employees
ORDER BY first_name DESC;

-- 4. Имена, зарплата и PF (12% от зарплаты) каждого сотрудника
SELECT
    first_name AS "First Name",
    last_name  AS "Last Name",
    salary,
    salary * 0.12 AS PF
FROM employees;

-- 5. Максимальная и минимальная зарплата из таблицы сотрудников
SELECT
    MAX(salary) AS "Max Salary",
    MIN(salary) AS "Min Salary"
FROM employees;

-- 6. Месячная зарплата каждого сотрудника (с точностью до 2 знаков после запятой)
SELECT
    first_name AS "First Name",
    last_name  AS "Last Name",
    ROUND(salary / 12, 2) AS "Monthly Salary"
FROM employees;
