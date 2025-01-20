SELECT YEAR(online_sale.sales_date) AS YEAR,
    MONTH(online_sale.sales_date) AS MONTH,
    user_info.gender AS GENDER,
    COUNT(DISTINCT user_info.user_id) AS USERS
FROM online_sale
INNER JOIN user_info
ON online_sale.user_id = user_info.user_id
WHERE user_info.gender IS NOT NULL
GROUP BY YEAR(online_sale.sales_date), MONTH(online_sale.sales_date), user_info.gender
ORDER BY YEAR, MONTH, GENDER;