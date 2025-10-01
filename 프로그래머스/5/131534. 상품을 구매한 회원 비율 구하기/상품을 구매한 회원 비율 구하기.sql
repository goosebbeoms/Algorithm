SELECT 
    T.sales_year AS year,
    T.sales_month,
    COUNT(DISTINCT T.user_id) AS purchased_users,
    ROUND(
        COUNT(DISTINCT T.user_id) / 
        (SELECT COUNT(*) FROM user_info WHERE YEAR(joined) = 2021),
        1
    ) AS purchased_ratio
FROM (
    SELECT 
        U.user_id,
        O.product_id,
        O.sales_amount,
        YEAR(O.sales_date) AS sales_year,
        MONTH(O.sales_date) AS sales_month
    FROM user_info U
    INNER JOIN online_sale O
        ON U.user_id = O.user_id
    WHERE YEAR(U.joined) = 2021
) T
GROUP BY T.sales_year, T.sales_month
ORDER BY year, sales_month;
