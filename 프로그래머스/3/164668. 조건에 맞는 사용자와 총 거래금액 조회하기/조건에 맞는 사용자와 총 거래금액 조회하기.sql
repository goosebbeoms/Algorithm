SELECT GU.user_id, GU.nickname, GB.total_sales
FROM (
    SELECT writer_id, SUM(price) AS TOTAL_SALES
    FROM used_goods_board
    WHERE status LIKE 'DONE'
    GROUP BY writer_id
    HAVING SUM(price) >= 700000
) GB
INNER JOIN (
    SELECT user_id, nickname
    FROM used_goods_user
) GU
ON GB.writer_id LIKE GU.user_id
ORDER BY GB.total_sales;