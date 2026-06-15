-- Task1

-- 1. Имя, фамилия, номер отдела и название отдела для каждого сотрудника
SELECT
    e.first_name,
    e.last_name,
    e.department_id,
    d.depart_name AS department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id;

-- 2. Имя, фамилия, отдел, город и штат для каждого сотрудника
SELECT
    e.first_name,
    e.last_name,
    d.depart_name AS department,
    l.city,
    l.state_province
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN locations l   ON d.location_id   = l.location_id;

-- 3. Имя, фамилия, номер и название отдела для сотрудников отделов 80 или 40
SELECT
    e.first_name,
    e.last_name,
    e.department_id,
    d.depart_name AS department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id
WHERE e.department_id IN (80, 40);

-- 4. Все отделы, включая те, в которых нет ни одного сотрудника
SELECT
    d.department_id,
    d.depart_name AS department_name,
    COUNT(e.employee_id) AS num_employees
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_id, d.depart_name;

-- 5. Имя всех сотрудников, включая имя их руководителя
SELECT
    e.first_name || ' ' || e.last_name AS employee,
    m.first_name || ' ' || m.last_name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.employee_id;

-- 6. Должность, полное имя сотрудника и разница между максимальной зарплатой
--    по данной должности и зарплатой сотрудника
SELECT
    e.job_id AS job_id,
    e.first_name || ' ' || e.last_name AS full_name,
    j.max_salary - e.salary AS salary_difference
FROM employees e
JOIN jobs j ON e.job_id = j.job_id;

-- 7. Должность и средняя зарплата сотрудников
SELECT
    job_id,
    ROUND(AVG(salary), 2) AS avg_salary
FROM employees
GROUP BY job_id;

-- 8. Полное имя и зарплата сотрудников, работающих в отделах, расположенных в Лондоне
SELECT
    e.first_name || ' ' || e.last_name AS full_name,
    e.salary
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN locations l   ON d.location_id   = l.location_id
WHERE l.city = 'London';

-- 9. Название отдела и количество сотрудников в каждом отделе
SELECT
    d.depart_name AS department_name,
    COUNT(e.employee_id) AS num_employees
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_id, d.depart_name;
