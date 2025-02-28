SELECT T.cnt AS fish_count, fish_name_info.fish_name
FROM (
    SELECT fish_type, COUNT(*) AS cnt
    FROM fish_info
    GROUP BY fish_type
) T
LEFT JOIN fish_name_info
ON T.fish_type = fish_name_info.fish_type
ORDER BY fish_count DESC;