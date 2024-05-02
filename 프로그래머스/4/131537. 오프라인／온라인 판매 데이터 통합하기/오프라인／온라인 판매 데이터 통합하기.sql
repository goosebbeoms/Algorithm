SELECT *
FROM (SELECT DATE_FORMAT(sales_date, '%Y-%m-%d') AS sales_date, product_id, user_id, sales_amount
    FROM online_sale
    UNION
    SELECT DATE_FORMAT(sales_date, '%Y-%m-%d') AS sales_date, product_id, NULL, sales_amount
    FROM offline_sale) AS combined_table
WHERE sales_date LIKE '2022-03%'
ORDER BY sales_date, product_id, user_id;