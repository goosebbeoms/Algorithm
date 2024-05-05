SELECT id, fish_name, C.length
FROM (
    SELECT A.fish_type, fish_name, length
    FROM (
        SELECT fish_type, MAX(length) AS length
        FROM fish_info
        GROUP BY fish_type
    ) A INNER JOIN fish_name_info B
        ON A.fish_type = B.fish_type
) C INNER JOIN fish_info D
    ON C.fish_type = D.fish_type and C.length = D.length
ORDER BY id;