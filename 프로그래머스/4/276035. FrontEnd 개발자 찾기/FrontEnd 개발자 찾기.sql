SELECT DISTINCT D.id, D.email, D.first_name, D.last_name
FROM developers D
INNER JOIN skillcodes S
ON D.skill_code = S.code | D.skill_code
WHERE S.category = 'Front End'
ORDER BY D.id;