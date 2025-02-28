SELECT COUNT(*) AS fish_count, MAX(fish_info.length) AS max_length, fish_info.fish_type
FROM fish_info
INNER JOIN (
    SELECT fish_type, AVG(length) AS length_avg
    FROM (
        SELECT fish_type, IF(length IS NULL, 10, length) AS length
        FROM fish_info
    ) fish_info_changed
    GROUP BY fish_type
    HAVING length_avg >= 33
) filter_table
ON fish_info.fish_type = filter_table.fish_type
GROUP BY fish_info.fish_type
ORDER BY fish_type;