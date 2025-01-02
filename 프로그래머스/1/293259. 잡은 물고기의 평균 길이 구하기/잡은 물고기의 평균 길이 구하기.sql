SELECT ROUND(AVG(length), 2) AS average_length
FROM (
    SELECT
        IF(length IS NULL, 10, length) AS length
    FROM fish_info
) fish_info;