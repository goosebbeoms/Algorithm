SELECT FP.category AS CATEGORY,
    A.max_price AS MAX_PRICE,
    FP.product_name AS PRODUCT_NAME
FROM food_product FP
INNER JOIN (
    SELECT category, MAX(price) AS max_price
    FROM food_product
    GROUP BY category
) A
ON FP.category LIKE A.category
WHERE 1 = 1
    AND FP.category IN ('과자', '국', '김치', '식용유')
    AND FP.price = A.max_price
ORDER BY max_price DESC;