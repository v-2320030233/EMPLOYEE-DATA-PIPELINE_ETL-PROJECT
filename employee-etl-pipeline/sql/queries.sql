-- 1. All employees with salary above 80,000
SELECT * 
FROM employees
WHERE salary > 80000;

-- 2. Average salary per department
SELECT department, ROUND(AVG(salary), 2) as average_salary
FROM employees
GROUP BY department
ORDER BY average_salary DESC;

-- 3. Employee count per department
SELECT department, COUNT(employee_id) as employee_count
FROM employees
GROUP BY department
ORDER BY employee_count DESC;

-- 4. Top 5 highest paid employees
SELECT employee_id, name, department, salary
FROM employees
ORDER BY salary DESC
LIMIT 5;

-- 5. Employees who joined in the last 2 years
SELECT employee_id, name, join_date
FROM employees
WHERE join_date >= DATE_SUB(CURDATE(), INTERVAL 2 YEAR)
ORDER BY join_date DESC;
