SELECT COUNT(T.M) AS fish_count, T.M AS month
FROM (
    SELECT MONTH(time) AS M
    FROM fish_info
) T
GROUP BY T.M
ORDER BY month;