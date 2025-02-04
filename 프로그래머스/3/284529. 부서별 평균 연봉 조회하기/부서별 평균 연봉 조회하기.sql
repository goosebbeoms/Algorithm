-- 부서별 평균 연봉 구하기 (부서 ID, 영문 부서명, 평균 연봉)
-- 부서 ID를 기준으로 부서 정보 테이블과 사원 정보 테이블을 INNER JOIN
-- 부서 ID를 GROUP BY로 묶어서 연봉 값을 연산 처리

SELECT hr_department.dept_id,
    hr_department.dept_name_en,
    ROUND(AVG(hr_employees.sal), 0) AS avg_sal
FROM hr_department
INNER JOIN hr_employees
ON hr_department.dept_id LIKE hr_employees.dept_id
GROUP BY hr_department.dept_id
ORDER BY avg_sal DESC;