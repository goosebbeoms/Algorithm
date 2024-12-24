SELECT D.id
FROM (
    SELECT A.id AS first_id, B.id AS second_id
    FROM ecoli_data A
        INNER JOIN ecoli_data B
        ON A.id = B.parent_id
    WHERE A.parent_id IS NULL
    ) C
    INNER JOIN ecoli_data D
    ON C.second_id = D.parent_id
ORDER BY D.id;