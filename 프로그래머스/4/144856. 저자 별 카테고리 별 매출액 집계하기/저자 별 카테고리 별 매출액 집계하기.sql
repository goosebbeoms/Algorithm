SELECT TEMP.author_id AS AUTHOR_ID,
    TEMP.author_name AS AUTHOR_NAME,
    TEMP.category AS CATEGORY,
    SUM(BS.sales * TEMP.price) AS SALES
FROM (
    SELECT *
    FROM book_sales
    WHERE 1 = 1
        AND YEAR(sales_date) = 2022
        AND MONTH(sales_date) = 01
) BS
INNER JOIN (
    SELECT B.book_id, B.author_id, A.author_name, B.category, B.price
    FROM book AS B
    LEFT JOIN author AS A
    ON B.author_id = A.author_id
) TEMP
ON BS.book_id = TEMP.book_id
GROUP BY TEMP.author_id, TEMP.category
ORDER BY TEMP.author_id ASC, TEMP.category DESC;