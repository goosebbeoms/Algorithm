SELECT (
    CASE
        WHEN (skill_code & (
            SELECT SUM(code)
            FROM skillcodes
            WHERE category LIKE 'Front%'
        )) AND (
            skill_code & (
                SELECT code
                FROM skillcodes
                WHERE name LIKE 'Python'
            )
        ) THEN 'A'
        WHEN skill_code & (
            SELECT code
            FROM skillcodes
            WHERE name LIKE 'C#'
        ) THEN 'B'
        WHEN skill_code & (
            SELECT SUM(code)
            FROM skillcodes
            WHERE category LIKE 'Front%'
        ) THEN 'C'
    END
) AS GRADE, ID, EMAIL
FROM developers
HAVING grade IS NOT NULL
ORDER BY grade, id;