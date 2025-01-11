SELECT book.category, SUM(BS.sales) AS TOTAL_SALES
FROM book
INNER JOIN (
    SELECT *
    FROM book_sales
    WHERE YEAR(sales_date) = 2022 AND MONTH(sales_date) = 1
) BS
ON book.book_id = BS.book_id
GROUP BY book.category
ORDER BY book.category;