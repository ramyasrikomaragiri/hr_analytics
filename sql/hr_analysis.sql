-- =========================================================
-- HR ANALYTICS - BUSINESS ANALYSIS
-- =========================================================

-- 1. Overall HR KPIs
SELECT
    COUNT(*) AS total_employees,
    COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
    ROUND(
        COUNT(*) FILTER (WHERE attrition = 'Yes') * 100.0 / COUNT(*),
        2
    ) AS attrition_rate,
    ROUND(AVG(age), 2) AS average_age,
    ROUND(AVG(monthly_income), 2) AS average_monthly_income
FROM hr_employees;


-- 2. Attrition by Department
SELECT
    department,
    COUNT(*) AS total_employees,
    COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
    ROUND(
        COUNT(*) FILTER (WHERE attrition = 'Yes') * 100.0 / COUNT(*),
        2
    ) AS attrition_rate
FROM hr_employees
GROUP BY department
ORDER BY attrition_rate DESC;


-- 3. Attrition by Job Role
SELECT
    job_role,
    COUNT(*) AS total_employees,
    COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
    ROUND(
        COUNT(*) FILTER (WHERE attrition = 'Yes') * 100.0 / COUNT(*),
        2
    ) AS attrition_rate
FROM hr_employees
GROUP BY job_role
ORDER BY attrition_rate DESC;


-- 4. Attrition by Overtime
SELECT
    overtime,
    COUNT(*) AS total_employees,
    COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
    ROUND(
        COUNT(*) FILTER (WHERE attrition = 'Yes') * 100.0 / COUNT(*),
        2
    ) AS attrition_rate
FROM hr_employees
GROUP BY overtime
ORDER BY attrition_rate DESC;


-- 5. Attrition by Gender
SELECT
    gender,
    COUNT(*) AS total_employees,
    COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
    ROUND(
        COUNT(*) FILTER (WHERE attrition = 'Yes') * 100.0 / COUNT(*),
        2
    ) AS attrition_rate
FROM hr_employees
GROUP BY gender
ORDER BY attrition_rate DESC;


-- 6. Attrition by Marital Status
SELECT
    marital_status,
    COUNT(*) AS total_employees,
    COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
    ROUND(
        COUNT(*) FILTER (WHERE attrition = 'Yes') * 100.0 / COUNT(*),
        2
    ) AS attrition_rate
FROM hr_employees
GROUP BY marital_status
ORDER BY attrition_rate DESC;


-- 7. Attrition by Business Travel
SELECT
    business_travel,
    COUNT(*) AS total_employees,
    COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
    ROUND(
        COUNT(*) FILTER (WHERE attrition = 'Yes') * 100.0 / COUNT(*),
        2
    ) AS attrition_rate
FROM hr_employees
GROUP BY business_travel
ORDER BY attrition_rate DESC;


-- 8. Salary and Attrition
SELECT
    attrition,
    COUNT(*) AS employees,
    ROUND(AVG(monthly_income), 2) AS average_monthly_income,
    ROUND(AVG(job_level), 2) AS average_job_level,
    ROUND(AVG(years_at_company), 2) AS average_years_at_company
FROM hr_employees
GROUP BY attrition
ORDER BY attrition;


-- 9. Attrition by Job Satisfaction
SELECT
    job_satisfaction,
    COUNT(*) AS employees,
    COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
    ROUND(
        COUNT(*) FILTER (WHERE attrition = 'Yes') * 100.0 / COUNT(*),
        2
    ) AS attrition_rate
FROM hr_employees
GROUP BY job_satisfaction
ORDER BY job_satisfaction;


-- 10. Attrition by Environment Satisfaction
SELECT
    environment_satisfaction,
    COUNT(*) AS employees,
    COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
    ROUND(
        COUNT(*) FILTER (WHERE attrition = 'Yes') * 100.0 / COUNT(*),
        2
    ) AS attrition_rate
FROM hr_employees
GROUP BY environment_satisfaction
ORDER BY environment_satisfaction;


-- 11. Attrition by Age Group
SELECT
    CASE
        WHEN age < 25 THEN 'Under 25'
        WHEN age BETWEEN 25 AND 34 THEN '25-34'
        WHEN age BETWEEN 35 AND 44 THEN '35-44'
        WHEN age BETWEEN 45 AND 54 THEN '45-54'
        ELSE '55+'
    END AS age_group,
    COUNT(*) AS employees,
    COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
    ROUND(
        COUNT(*) FILTER (WHERE attrition = 'Yes') * 100.0 / COUNT(*),
        2
    ) AS attrition_rate
FROM hr_employees
GROUP BY age_group
ORDER BY MIN(age);


-- 12. Attrition by Tenure
SELECT
    CASE
        WHEN years_at_company <= 2 THEN '0-2 Years'
        WHEN years_at_company BETWEEN 3 AND 5 THEN '3-5 Years'
        WHEN years_at_company BETWEEN 6 AND 10 THEN '6-10 Years'
        WHEN years_at_company BETWEEN 11 AND 20 THEN '11-20 Years'
        ELSE '20+ Years'
    END AS tenure_group,
    COUNT(*) AS employees,
    COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
    ROUND(
        COUNT(*) FILTER (WHERE attrition = 'Yes') * 100.0 / COUNT(*),
        2
    ) AS attrition_rate
FROM hr_employees
GROUP BY tenure_group
ORDER BY MIN(years_at_company);


-- 13. Top Job Roles by Employee Count
SELECT
    job_role,
    COUNT(*) AS employees
FROM hr_employees
GROUP BY job_role
ORDER BY employees DESC;


-- 14. Highest Average Salary by Department
SELECT
    department,
    ROUND(AVG(monthly_income), 2) AS average_monthly_income
FROM hr_employees
GROUP BY department
ORDER BY average_monthly_income DESC;


-- 15. Top 10 Highest Paid Employees
SELECT
    employee_number,
    job_role,
    department,
    monthly_income,
    years_at_company
FROM hr_employees
ORDER BY monthly_income DESC
LIMIT 10;


-- 16. Employees with High Attrition Risk Indicators
SELECT
    employee_number,
    age,
    job_role,
    department,
    overtime,
    job_satisfaction,
    monthly_income,
    years_at_company,
    attrition
FROM hr_employees
WHERE attrition = 'Yes'
  AND overtime = 'Yes'
ORDER BY monthly_income DESC;


-- 17. Department Salary Ranking
SELECT
    department,
    ROUND(AVG(monthly_income), 2) AS average_salary,
    RANK() OVER (
        ORDER BY AVG(monthly_income) DESC
    ) AS salary_rank
FROM hr_employees
GROUP BY department;


-- 18. Job Role Attrition Ranking
SELECT
    job_role,
    COUNT(*) AS employees_left,
    RANK() OVER (
        ORDER BY COUNT(*) FILTER (WHERE attrition = 'Yes') DESC
    ) AS attrition_rank
FROM hr_employees
GROUP BY job_role
ORDER BY attrition_rank;


-- 19. Department Summary
SELECT
    department,
    COUNT(*) AS employees,
    ROUND(AVG(age), 1) AS average_age,
    ROUND(AVG(monthly_income), 2) AS average_salary,
    ROUND(AVG(years_at_company), 1) AS average_tenure,
    ROUND(
        COUNT(*) FILTER (WHERE attrition = 'Yes') * 100.0 / COUNT(*),
        2
    ) AS attrition_rate
FROM hr_employees
GROUP BY department
ORDER BY attrition_rate DESC;


-- 20. Executive HR Summary
SELECT
    COUNT(*) AS total_employees,
    COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
    ROUND(
        COUNT(*) FILTER (WHERE attrition = 'Yes') * 100.0 / COUNT(*),
        2
    ) AS attrition_rate,
    ROUND(AVG(age), 1) AS average_age,
    ROUND(AVG(monthly_income), 2) AS average_monthly_income,
    ROUND(AVG(years_at_company), 1) AS average_tenure,
    COUNT(*) FILTER (WHERE overtime = 'Yes') AS overtime_employees
FROM hr_employees;