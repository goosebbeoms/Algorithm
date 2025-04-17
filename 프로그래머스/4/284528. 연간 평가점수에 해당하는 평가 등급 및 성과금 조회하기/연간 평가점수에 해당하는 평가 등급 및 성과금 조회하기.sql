SELECT hr_employees.emp_no, hr_employees.emp_name, g.grade,
    IF(g.grade = 'S', hr_employees.sal * 0.2,
      IF(g.grade = 'A', hr_employees.sal * 0.15,
        IF(g.grade = 'B', hr_employees.sal * 0.1, 0))) AS bonus
FROM hr_employees JOIN (
    SELECT emp_no, IF(SUM(score)/COUNT(*) >= 96,
             'S', IF(SUM(score)/COUNT(*) >= 90,
                    'A', IF(SUM(score)/COUNT(*) >= 80,
                           'B', 'C'))) AS grade
    FROM hr_grade
    GROUP BY emp_no
) G
ON hr_employees.emp_no = g.emp_no;

