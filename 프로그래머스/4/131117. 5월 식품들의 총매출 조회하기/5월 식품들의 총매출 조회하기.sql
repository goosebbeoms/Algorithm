SELECT P.product_id, P.product_name, SUM(P.price * O.amount) AS TOTAL_PRICE
FROM food_product P
RIGHT JOIN food_order O
ON P.product_id = O.product_id
WHERE YEAR(O.produce_date) = 2022
    AND MONTH(O.produce_date) = 05
    AND P.product_id IS NOT NULL
GROUP BY P.product_id
ORDER BY total_price desc, P.product_id;