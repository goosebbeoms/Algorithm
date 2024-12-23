SELECT id, email, first_name, last_name FROM developer_infos
WHERE (skill_1 LIKE "Python") OR (skill_2 LIKE "Python") OR (skill_3 LIKE "Python")
ORDER BY id;