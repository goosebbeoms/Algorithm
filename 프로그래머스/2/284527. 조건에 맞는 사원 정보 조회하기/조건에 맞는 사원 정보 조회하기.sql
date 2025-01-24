SELECT filtered_grade.score,
    hr_employees.emp_no,
    hr_employees.emp_name,
    hr_employees.position,
    hr_employees.email
FROM hr_employees
INNER JOIN (
    SELECT emp_no, SUM(score) AS score
    FROM hr_grade
    GROUP BY emp_no
    ORDER BY score DESC
    LIMIT 1
) filtered_grade
ON hr_employees.emp_no = filtered_grade.emp_no